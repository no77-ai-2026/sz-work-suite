#!/usr/bin/env python3
"""입력 JSON 을 문체 규칙으로 검사한다.

    python3 lint_report.py input.json [--series auto|A|B1|B2|B3]

build_report.py 가 서식(줄넘침·주석넘침·분량)을 본다면 이쪽은 문체를 본다.
CFO 수정본에서 역산한 규칙만 담는다 — 근거는 references/cfo-review-log.md.

심각도
  ERROR — 확정본에서 100% 교정된 항목
  WARN  — 자주 교정되나 예외가 있는 항목
  INFO  — 1회 관찰, 승격 대기
"""
import argparse
import json
import re
import sys

APOS = "\u0384"          # ΄ 원본이 쓰는 연도 기호

# ── 영문 약어 → 한국어 (style-guide §8 / term-map)
ABBR = {
    "CL": "여신", "ORL": "보험 증권 서명본", "MP": "보험료",
    "UBO": "(삭제) 보험 신청", "Credit Limit": "여신",
    "On-Risk Letter": "보험 증권 서명본", "Minimum Premium": "보험료",
    "Premium": "보험료", "PCG": "모회사 보증", "CGL": "모회사 보증",
}
KEEP_EN = {"Top-up", "Open Risk", "Seasonality", "Cover", "N-ERP", "IT Park",
           "Samsung Innovation Campus", "TUIT", "AI", "IoT", "CSR"}

# ── 부정형 (§10)
NEG = ["[미검증]", "미수령", "미산출", "미확인", "지연中", "未제정", "未수령", "未산출"]

# ── 서술체 종결 (§1)
DECL = [r"습니다", r"입니다", r"하였음", r"되었다", r"이다\b", r"할 예정입니다"]

# ── 제목 과정형 명사
TITLE_BAD = ["경과", "진행 현황", "관련", "현황 보고", "건"]

# ── 붙여 쓰면 안 되는 복합명사 (확정본에서 띄어쓰기로 교정된 것)
SPACING = {
    "입증책임": "입증 책임", "감사법인": "감사 법인", "내각결정": "내각 결정",
    "고용빈곤감소부": "고용빈곤 감소부", "인적자본": "인적 자본",
    "당사분담": "당사 분담액", "규제기관": "규제 기관", "반복검사": "반복적 검사",
    "주요내용": "주요 내용", "집계결과": "조사 결과",
}

# ── 한자 약어는 앞말에 붙인다
HANJA_TIGHT = ["中", "內", "外", "時", "上", "下", "後", "前"]

# ── 프레이밍 (§13)
CYNICAL = ["전가", "떠넘", "책임 회피", "부담 전가"]

VAGUE_END = ["모니터링", "검토", "지속 협의", "협의 예정", "추진"]


def lines_of(spec):
    out = []
    for b in spec.get("blocks", []):
        if b.get("type") == "table":
            continue
        out.append(b)
    return out


def notes_of(block):
    ns = block.get("notes")
    if ns is None and block.get("note"):
        ns = [{"anchor": block.get("anchor", ""), "text": block["note"]}]
    return [{"text": n} if isinstance(n, str) else n for n in (ns or [])]


def check(spec, series="auto"):
    issues = []

    def add(sev, code, msg, where=""):
        issues.append((sev, code, msg, where))

    blocks = lines_of(spec)
    heads = [b["text"] for b in blocks if b.get("level") == "head"]
    title = spec.get("title", "")

    # 계열 자동 판정
    if series == "auto":
        fin = any(k in title + " ".join(heads)
                  for k in ("여신", "보험", "자금", "계약", "헷징"))
        series = "A" if fin else "B"

    # ── 제목
    for bad in TITLE_BAD:
        if title.rstrip().endswith(bad):
            add("ERROR", "T1", f"제목이 과정형 '{bad}'로 끝납니다. 행위 결과로 바꾸세요.", title)
    if not re.match(r"^(SEUZ|우즈벡),\s", title):
        add("WARN", "T2", "제목은 'SEUZ, ' 또는 '우즈벡, ' 으로 시작합니다.", title)
    if len(re.findall(r"및|/|,", title.split(",", 1)[-1])) >= 1 and not spec.get("title_notes"):
        add("WARN", "T3", "제목이 항목을 나열합니다. 상위 범주 하나로 줄이고 "
                          "구체 항목은 title_notes 로 빼세요.", title)

    # ── 블록
    if series == "A" and len(heads) != 3:
        add("ERROR", "B1", f"재무 계열은 3블록입니다. 현재 {len(heads)}개: {heads}")
    if any("현 안" in h or h.strip() == "현안" for h in heads):
        add("ERROR", "B2", "「현 안」 블록은 세우지 않습니다. 향후 계획의 조치로 흡수하세요.")

    # 개요의 나열 순서 = 후속 블록 순서
    if heads and ("개 요" in heads[0] or "개요" in heads[0]):
        intro = " ".join(b["text"] for b in blocks
                         if b.get("level") != "head")[:200]
        order = [h for h in heads[1:-1]]
        pos = [intro.find(h.split("(")[0].strip()[:4]) for h in order]
        known = [p for p in pos if p >= 0]
        if len(known) >= 2 and known != sorted(known):
            add("WARN", "B3", "개요의 나열 순서와 후속 블록 순서가 다릅니다.", str(order))

    # ── 줄 단위
    for b in blocks:
        t = b.get("text", "")
        lvl = b.get("level", "")
        ns = notes_of(b)

        for ab, ko in ABBR.items():
            if re.search(rf"\b{re.escape(ab)}\b", t) and ab not in KEEP_EN:
                add("ERROR", "A1", f"영문 약어 '{ab}' → '{ko}'", t)

        for n in NEG:
            if n in t:
                sev = "ERROR" if series == "A" else "WARN"
                add(sev, "N1", f"부정형 '{n}' 이 본문에 있습니다. "
                               f"주석으로 강등하거나 조치로 바꾸세요.", t)

        for pat in DECL:
            if re.search(pat, t):
                add("ERROR", "S1", "서술체 종결입니다. 명사형으로 끝내세요.", t)

        for wrong, right in SPACING.items():
            if wrong in t:
                add("WARN", "W1", f"'{wrong}' → '{right}'", t)

        for h in HANJA_TIGHT:
            if re.search(rf"\S\s+{h}(?![가-힣])", t):
                add("WARN", "W2", f"한자 약어 '{h}' 는 앞말에 붙입니다.", t)

        for c in CYNICAL:
            if c in t:
                add("WARN", "F1", f"'{c}' — 법인 관점의 이익으로 프레이밍하세요.", t)

        if re.search(r"\d+\s*배\s*(인하|인상|감면)", t):
            add("INFO", "F2", "배수 표현보다 증감률(%)을 씁니다.", t)

        if APOS not in t and re.search(r"'\d{2}[.\s年月]", t):
            add("INFO", "C1", f"연도 기호가 ASCII 입니다. U+0384 '{APOS}' 를 쓰세요.", t)

        for n in ns:
            nt = n.get("text", "")
            if nt.startswith("* ") or nt.startswith("*  "):
                if nt.startswith("*  "):
                    add("INFO", "C2", "주석 접두 뒤 공백이 둘입니다.", nt)
            if APOS not in nt and re.search(r"'\d{2}[.\s年月]", nt):
                add("INFO", "C1", f"주석 연도 기호가 ASCII 입니다.", nt)
            if re.search(r"[А-Яа-я]{2}[-\u2013]?\d+", nt):
                add("INFO", "C3", "키릴 법령번호는 확정본에서 삭제된 사례가 있습니다.", nt)

    # ── 마지막 블록
    if heads:
        last_idx = max(i for i, b in enumerate(blocks) if b.get("level") == "head")
        tail = blocks[last_idx + 1:]
        tail_txt = " ".join(b.get("text", "") for b in tail)
        if series == "A":
            if "=" not in tail_txt:
                add("ERROR", "P1", "향후 운영 계획에 관리 지표 산식이 없습니다.")
            if not re.search(r"(만기|시점|여부 결정|여부 판단)", tail_txt):
                add("ERROR", "P2", "향후 운영 계획에 의사결정 시점이 없습니다.")
            for v in VAGUE_END:
                if tail and tail[-1].get("text", "").rstrip().endswith(v):
                    add("WARN", "P3", f"재무 계열 계획이 '{v}' 로 끝납니다.",
                        tail[-1]["text"])
        if tail and tail[0].get("level") != "dash":
            add("WARN", "P4", "블록 첫 줄은 - (dash) 로 엽니다.", tail[0].get("text", ""))

    # 블록 첫 줄은 법인 관점 — A 계열은 수치
    if series == "A":
        first = next((b for b in blocks if b.get("level") == "dash"), None)
        if first and not re.search(r"\d", first.get("text", "")):
            add("ERROR", "B4", "재무 계열 첫 줄은 총량 수치로 엽니다.",
                first.get("text", ""))

    return issues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("json_path")
    ap.add_argument("--series", default="auto", choices=["auto", "A", "B", "B1", "B2", "B3"])
    a = ap.parse_args()
    with open(a.json_path, encoding="utf-8") as f:
        spec = json.load(f)
    issues = check(spec, a.series[0] if a.series != "auto" else "auto")
    if not issues:
        print("문체 점검 이상 없음")
        return 0
    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    for sev, code, msg, where in sorted(issues, key=lambda i: order[i[0]]):
        print(f"[{sev}][{code}] {msg}")
        if where:
            print(f"        └ {where[:60]}")
    return 1 if any(i[0] == "ERROR" for i in issues) else 0


if __name__ == "__main__":
    sys.exit(main())
