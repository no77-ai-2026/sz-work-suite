#!/usr/bin/env python3
"""초안 .docx 와 CFO 확정본 .docx 를 구조 단위로 대조한다.

    python3 diff_review.py 초안.docx 확정본.docx [--json out.json]

출력
  1) 블록 구조 변화 (□ 제목·순서)
  2) 줄 단위 매칭 — 유지 / 수정 / 삭제 / 신설
  3) 주석 변화 (신설·삭제·수정, 본문↔주석 이동)
  4) 용어 치환쌍 후보 (수정된 줄에서 자동 추출)

대조 결과를 references/cfo-review-log.md 에 사례로 옮기고,
2회 이상 반복되는 지적은 style-guide.md 규칙으로 승격한다.
"""
import argparse
import difflib
import json
import re
import sys
import zipfile
from lxml import etree

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


# ─────────────────────────────────────────────────────────────
# 추출
# ─────────────────────────────────────────────────────────────
def _in_textbox(el):
    while el is not None:
        if el.tag == W + "txbxContent":
            return True
        el = el.getparent()
    return False


def _body_text(p):
    return "".join(t.text or "" for t in p.iter(W + "t") if not _in_textbox(t))


def _notes(p):
    out, seen = [], set()
    for tb in p.iter(W + "txbxContent"):
        s = "".join(t.text or "" for t in tb.iter(W + "t")).strip()
        if s and s not in seen:          # Fallback 중복 제거
            seen.add(s)
            out.append(s)
    return out


LEVEL_PAT = [
    ("head", re.compile(r"^\s*□\s*")),
    ("dash", re.compile(r"^\s*-\s*")),
    ("dot", re.compile(r"^\s*·\s*")),
    ("arrow", re.compile(r"^\s*→\s*")),
    ("star", re.compile(r"^\s*※\s*")),
    ("tri", re.compile(r"^\s*▷\s*")),
]


def _level(text):
    for name, pat in LEVEL_PAT:
        if pat.match(text):
            return name, pat.sub("", text).strip()
    return "cont", text.strip()


def read_report(path):
    z = zipfile.ZipFile(path)
    root = etree.fromstring(z.read("word/document.xml"))
    body = root.find(W + "body")
    lines, title, title_notes = [], None, []
    for el in body:
        if el.tag != W + "p":
            continue
        raw = _body_text(el)
        notes = _notes(el)
        if not raw.strip() and not notes:
            continue
        if title is None:
            title, title_notes = raw.strip(), notes
            continue
        lvl, txt = _level(raw)
        lines.append({"level": lvl, "text": txt, "raw": raw.strip(), "notes": notes})
    return {"title": title, "title_notes": title_notes, "lines": lines}


# ─────────────────────────────────────────────────────────────
# 대조
# ─────────────────────────────────────────────────────────────
def norm(s):
    return re.sub(r"\s+", "", s)


def similarity(a, b):
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


def match_lines(old, new, threshold=0.45):
    """유사도 기반 정렬. 반환: [(kind, old_idx, new_idx)]"""
    sm = difflib.SequenceMatcher(
        None, [norm(l["text"]) for l in old], [norm(l["text"]) for l in new])
    ops = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                ops.append(("유지", i1 + k, j1 + k))
        elif tag == "replace":
            used = set()
            for i in range(i1, i2):
                best, bj = 0.0, None
                for j in range(j1, j2):
                    if j in used:
                        continue
                    s = similarity(old[i]["text"], new[j]["text"])
                    if s > best:
                        best, bj = s, j
                if bj is not None and best >= threshold:
                    used.add(bj)
                    ops.append(("수정", i, bj))
                else:
                    ops.append(("삭제", i, None))
            for j in range(j1, j2):
                if j not in used:
                    ops.append(("신설", None, j))
        elif tag == "delete":
            for i in range(i1, i2):
                ops.append(("삭제", i, None))
        elif tag == "insert":
            for j in range(j1, j2):
                ops.append(("신설", None, j))
    ops.sort(key=lambda o: (o[2] if o[2] is not None else -1, o[1] or 0))
    return ops


TOKEN = re.compile(r"[가-힣A-Za-z0-9΄'%·/\u4e00-\u9fff]+")


def term_pairs(a, b):
    """수정된 한 줄에서 치환된 어절 쌍을 뽑는다."""
    ta, tb = TOKEN.findall(a), TOKEN.findall(b)
    pairs = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, ta, tb).get_opcodes():
        if tag == "replace":
            pairs.append((" ".join(ta[i1:i2]), " ".join(tb[j1:j2])))
        elif tag == "delete":
            pairs.append((" ".join(ta[i1:i2]), "(삭제)"))
        elif tag == "insert":
            pairs.append(("(신설)", " ".join(tb[j1:j2])))
    return pairs


def run(old_path, new_path):
    old, new = read_report(old_path), read_report(new_path)
    report = {"title": {}, "blocks": {}, "lines": [], "terms": []}

    # 1) 제목
    if old["title"] != new["title"]:
        report["title"] = {"before": old["title"], "after": new["title"],
                           "terms": term_pairs(old["title"], new["title"])}
    if old["title_notes"] != new["title_notes"]:
        report["title"]["notes"] = {"before": old["title_notes"],
                                    "after": new["title_notes"]}

    # 2) 블록 구조
    ob = [l["text"] for l in old["lines"] if l["level"] == "head"]
    nb = [l["text"] for l in new["lines"] if l["level"] == "head"]
    if ob != nb:
        report["blocks"] = {"before": ob, "after": nb,
                            "count_changed": len(ob) != len(nb),
                            "reordered": sorted(ob) == sorted(nb) and ob != nb}

    # 3) 줄
    for kind, i, j in match_lines(old["lines"], new["lines"]):
        o = old["lines"][i] if i is not None else None
        n = new["lines"][j] if j is not None else None
        rec = {"kind": kind,
               "before": o["text"] if o else None,
               "after": n["text"] if n else None,
               "level_before": o["level"] if o else None,
               "level_after": n["level"] if n else None,
               "notes_before": o["notes"] if o else [],
               "notes_after": n["notes"] if n else []}
        if kind == "수정":
            rec["terms"] = term_pairs(o["text"], n["text"])
            report["terms"].extend(rec["terms"])
        if o and n:
            if o["level"] != n["level"]:
                rec["level_shift"] = f"{o['level']} → {n['level']}"
            if o["text"] != n["text"] and norm(o["text"]) == norm(n["text"]):
                rec["spacing_only"] = True
            if o["notes"] != n["notes"]:
                rec["note_change"] = True
        report["lines"].append(rec)
    return report


def render(r):
    out = []
    if r["title"]:
        out.append("## 제목")
        out.append(f"  before : {r['title'].get('before')}")
        out.append(f"  after  : {r['title'].get('after')}")
        if r["title"].get("notes"):
            out.append(f"  주석   : {r['title']['notes']['before']} → "
                       f"{r['title']['notes']['after']}")
        out.append("")

    if r["blocks"]:
        b = r["blocks"]
        out.append("## 블록 구조")
        out.append(f"  before : {b['before']}")
        out.append(f"  after  : {b['after']}")
        if b.get("reordered"):
            out.append("  ※ 순서만 변경 — 서술 순서 규칙을 확인할 것")
        if b.get("count_changed"):
            out.append("  ※ 블록 수 변경 — 계열 판정을 재검토할 것")
        out.append("")

    out.append("## 줄 단위")
    for rec in r["lines"]:
        k = rec["kind"]
        if k == "유지":
            if rec.get("level_shift"):
                out.append(f"  [레벨이동] {rec['after'][:40]}  ({rec['level_shift']})")
            if rec.get("spacing_only"):
                out.append(f"  [띄어쓰기] - {rec['before']}")
                out.append(f"             + {rec['after']}")
            if rec.get("note_change"):
                out.append(f"  [주석변경] {rec['after'][:40]}")
                out.append(f"             {rec['notes_before']} → {rec['notes_after']}")
            continue
        if k == "수정":
            out.append(f"  [수정] - {rec['before']}")
            out.append(f"         + {rec['after']}")
            if rec.get("level_shift"):
                out.append(f"         레벨 {rec['level_shift']}")
            if rec.get("note_change"):
                out.append(f"         주석 {rec['notes_before']} → {rec['notes_after']}")
        elif k == "삭제":
            out.append(f"  [삭제] - {rec['before']}")
            if rec["notes_before"]:
                out.append(f"         주석 {rec['notes_before']}")
        elif k == "신설":
            out.append(f"  [신설] + {rec['after']}")
            if rec["notes_after"]:
                out.append(f"         주석 {rec['notes_after']}")
    out.append("")

    if r["terms"]:
        out.append("## 용어 치환쌍 후보")
        seen = set()
        for a, b in r["terms"]:
            if (a, b) in seen or not a.strip() or not b.strip():
                continue
            seen.add((a, b))
            out.append(f"  {a}  →  {b}")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("final")
    ap.add_argument("--json")
    a = ap.parse_args()
    r = run(a.draft, a.final)
    print(render(r))
    if a.json:
        with open(a.json, "w", encoding="utf-8") as f:
            json.dump(r, f, ensure_ascii=False, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
