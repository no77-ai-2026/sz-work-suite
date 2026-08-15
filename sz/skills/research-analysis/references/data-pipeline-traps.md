# 데이터 파이프라인 11대 함정 (Data Pipeline Traps)

> 공시·재무·텍스트 원문을 수집→정제→회귀로 잇는 파이프라인에서 반복 발생한 **silent fail** 11종. 자동화 시 **코드에 내장**하라. (원문 수집 예: DART / 유사 규제공시 포털)

| # | 함정 | 증상 | 해결 |
|---|---|---|---|
| 1 | **코퍼스 미스매치** | 대량 수집 후 관심현상 3%뿐 | 대량수집 전 소표본 feasibility(대표 5~40개)로 base rate 확인 |
| 2 | **원문 다중 멤버 zip** | '가장 큰 파일 하나'만 저장 → 재무·주석 본문 절반 누락 | zip **전 멤버 병합** 저장. 판정: '영업이익' 등 앵커어 포함 여부 |
| 3 | **인코딩 혼재(UTF-8/CP949)** | 한 폴더에 두 인코딩 공존, 한쪽 디코드 시 글자 깨짐(0회 매칭) | `smart_decode`: utf-8/cp949 중 **U+FFFD(replacement char) 적은 쪽** 선택 |
| 4 | **패널의 절대경로** | 샌드박스에서 만든 파일경로가 로컬에 없음 → 전건 스킵(0%) | 경로 저장 대신 **식별자(접수번호 등)로 폴더 재구성** |
| 5 | **희소사건 완전분리** | 산업더미 다수 → 로짓 Singular matrix | 사건 0건 산업 '기타' 병합, BFGS, 클러스터 SE |
| 6 | **statsmodels Logit robust** | `get_robustcov_results` 없음 | `.fit(cov_type='cluster', cov_kwds={'groups':...})` |
| 7 | **규칙기반 오탐** | 유사표현(경상이익률·재작성조정·약정EBITDA·공정가치 EV/EBITDA·희석EPS·손상검사)이 오탐 | 가드 반복 + 모호어는 **긍정문맥(주요경영지표/성과/경영진 등) 요구** |
| 8 | **대량호출 후 접근 제한** | 요청 폭주 후 connect timeout | **공식 API 키 사용 + 요청간격 상향(예: 1.5초) + 지수백오프 재시도 + 캐시 이어받기.** 계속 막히면 **야간 분할·다음날 재개**로 정중히 우회(부하 유발·차단 우회 행위 금지) |
| 9 | **무인 실행 견고성** | 네트워크 한 번에 전체 크래시 | 모든 API콜 지수백오프 재시도 → 실패 시 스킵, 대상별 캐시, N건마다 인덱스 중간저장 |
| 10 | **requirements 인코딩** | pip가 cp949로 읽어 UnicodeDecodeError | `requirements.txt`는 **ASCII만**(한글 주석·em대시 금지) |
| 11 | **진척 가시성** | 로그 없어 '멈춤'처럼 보임 | `[n/total] 식별자` **매 건 flush 출력** |

## smart_decode (함정 #3 구현)

```python
def smart_decode(raw: bytes) -> str:
    best, best_bad = None, 1e18
    for enc in ('utf-8', 'cp949'):
        s = raw.decode(enc, errors='replace')
        bad = s.count('�')          # replacement char 개수
        if bad < best_bad:
            best, best_bad = s, bad
    return best
```

## 전 멤버 병합 (함정 #2 구현)

```python
import zipfile, io
def merge_zip_members(raw: bytes) -> str:
    parts = []
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        for n in z.namelist():
            parts.append(smart_decode(z.read(n)))
    return "\n".join(parts)   # '가장 큰 파일 하나'가 아니라 전부
```

## 표준 추출 3단 (규칙+문맥)

1. 인코딩 자동감지(smart_decode) → 태그제거 평문화.
2. 표면형 ±220자 구절 추출 → 신호(단서·항목·숫자·가드).
3. 확정규칙: `숫자 ∧ (단서 ∨ 항목) ∧ ¬가드`. 정제는 **재추출 없이 후처리로 3초 재계산**(오탐 패턴 가드만 추가).

## 검증(정밀도/재현율)

- N=300 **층화 라벨링** → 정밀도·재현율·Cohen's κ.
- 부분 자동화: **LLM 보조 라벨(Haiku 등) + 사람 스팟체크 하이브리드**.
