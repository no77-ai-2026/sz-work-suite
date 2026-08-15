# 샌드박스/로컬 실행 패턴 (Sandbox Execution Patterns)

> Claude 세션(샌드박스)과 사용자 로컬 PC의 역할 분담, 그리고 세션 제약 회피 패턴. 대량 수집·대용량 IO·긴 루프를 **정직하고 견고하게** 돌리는 표준.

## 역할 분담 원칙

- **세션(샌드박스)** = 설계·집필·소표본 검증·문서생성·마운트 파일 분석.
- **로컬(사용자 PC)** = 대량 네트워크 수집·대용량 파싱(수십 GB)·회귀 재실행.
- 원칙: **세션=설계/검증, 로컬=대량실행.** 중요한 JSON/스크립트는 파일도구로 쓰고 로컬 실행 결과로 최종 확인.

## 세션 제약 (관찰된 사실)

1. **외부도메인 차단** — 다수 공공 API(opendart·FRED·data.go.kr·SEC·GIR 등)가 bash에서 HTTP 000. `web_fetch`는 HTML은 읽으나 **바이너리/JS-POST 다운로드는 타임아웃**.
2. **마운트 IO 지연** — 다수파일 IO 느림, 한글 멀티바이트 지점에서 읽기·쓰기 동기화 지연/절단 가능.
3. **bash ~45초 한계 + 백그라운드 미유지** — 긴 루프는 호출 종료 시 죽음. `&` 백그라운드 **금지**.

## 최강 패턴: "사용자 브라우저 → 마운트 → Claude 처리"

외부에서 직접 못 받는 파일은 **사용자가 브라우저로 받아 `raw/` 폴더에 넣으면 Claude가 세션 내에서 바로 파싱·매칭·분석.** 로컬 재실행 불필요. (배출·정책 데이터 등이 이 경로로 처리됨.)

## 재개형 배치러너 (45초 한계 회피)

긴 루프(수만 parquet 파싱, 수천 문서 스캔)는 **재개형 배치**로:
- `done-set(json)` + `parts/` 디렉터리 + **시간예산(예: 35초)** + 매 호출 이어받기.
- 백그라운드 대신 **여러 번 호출**로 나눠 진행.

```python
import json, os, time
DONE = 'done.json'; BUDGET = 35
done = set(json.load(open(DONE))) if os.path.exists(DONE) else set()
t0 = time.time()
for item in all_items:
    if item in done: continue
    if time.time() - t0 > BUDGET: break   # 시간예산 소진 → 다음 호출로
    process(item)                          # parts/{item}.csv 등에 저장
    done.add(item)
json.dump(list(done), open(DONE, 'w'))
print(f"[{len(done)}/{len(all_items)}] 진행 (재호출로 이어받기)")
```

## 공공포털 다운로드 함정

- 연도 선택 후 **반드시 [검색]→표 갱신 확인→[다운로드]** (안 하면 기본연도만 받아짐).
- 파일 잘림(truncated OLE2) 잦음 → **엑셀로 열어 .xlsx 재저장**하면 복구.
- 같은이름 저장은 덮어쓰기 실패로 구파일 잔존 → **연도별 파일명 구분 + md5/mtime로 실제 교체 확인**.

## 마운트 파일 자동적재

```python
import pandas as pd
def load_any(path):
    if path.endswith('.parquet'): return pd.read_parquet(path)   # pip install pyarrow --break-system-packages
    if path.endswith('.xlsx'):    return pd.read_excel(path)
    if path.endswith('.xls'):
        try: return pd.read_excel(path)                          # xlrd
        except Exception: return pd.read_html(path)[0]           # HTML위장 .xls
    for enc in ('utf-8','cp949'):
        try: return pd.read_csv(path, encoding=enc)
        except UnicodeDecodeError: continue
```
세션 sandbox에 `pyarrow·statsmodels·xlrd` 등 없을 수 있음 → `pip install --break-system-packages`.

## 정규화 업체명 매칭 (외부 처치레이어 조인)

```python
import re
def norm_name(s: str) -> str:
    s = re.sub(r'\(주\)|주식회사|㈜|\s+', '', str(s))
    return s.strip()
# corp_name 정규화 후 조인 → 상장기업 매칭
```

## 견고성 공용 util (모든 수집기가 상속)

재시도·캐시·이어받기·진척로그·인코딩 자동감지·전멤버병합을 **공용 모듈**로 추출. seed 고정, 원본 `raw/` 불변, 정제 `clean/`, 로그·인덱스 보존 → **각 논문 폴더가 재현 캡슐**.
