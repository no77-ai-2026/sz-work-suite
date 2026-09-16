---
name: risk-radar
description: |
  리스크 판정 엔진 — 리스크 레지스터 10카테고리(Communication·Competitive·Finance·Geo·Human Capital·Legal·Operation·Product·Security·Supply Chain) 분류, 상태 3등급(위기/주의/정상) 판정, 델타 브리핑 6항목, 임원 브리핑. 트리거: "이 이슈 리스크 등급 판정해줘", "리스크 브리핑 만들어줘", "이번 주 리스크 델타"
  EN: Risk grading engine — 10-category risk register classification, 3-level status (Crisis/Watch/Normal), 6-part delta briefing, executive brief. Triggers: "grade this risk", "risk briefing", "weekly risk delta"
version: 2.1.0
---

# sz:risk-radar — 리스크 판정 엔진 (리스크 매니지먼트)

이슈를 **리스크 레지스터 10카테고리**로 분류하고 상태 등급을 판정해 표·브리핑을 만든다. 대시보드 운영(세팅·주간 갱신·보고서·점검)은 `sz:risk-center`가 담당하고 본 스킬을 호출한다. 근거 조사는 `sz:uz-research` 규칙(소스 티어·인용 4분류·1차 발표일)을 따른다.

## 언어 규칙
요청 언어(KO/EN/RU/UZ)로 응답. 리스크 표·브리핑은 요청 시 KO/EN 병기.

## 리스크 레지스터 10카테고리 (분류 체계 — HARD)
정의·대표 항목·판정 절차: `references/risk-framework.md`

| # | id | 카테고리 |
|---|---|---|
| ① | comm | Communication — 뉴미디어·언론·평판 |
| ② | compete | Competitive / Market Disruption — 경쟁사·채널·가격·시장 구조 |
| ③ | finance | Finance — 환율·금리·세제·신용·자본통제 |
| ④ | geo | Geo / Humanitarian — 지정학·제재·정치·재난 |
| ⑤ | hc | Human Capital — 노무·인건비·채용·비자 |
| ⑥ | legal | Legal — 법령 개정·규제·인증·분쟁 |
| ⑦ | ops | Operation (Office) — 사무·인프라·에너지·행정 |
| ⑧ | product | Product / Service — 제품 규격·품질·A/S·소비자 이슈 |
| ⑨ | sec | Security — 물리·정보·사이버 보안 |
| ⑩ | supply | Supply Chain — 통관·물류·보세·공급 |

※ 이 10분류는 **레지스터(분류) 체계**다. 주간 조사에 쓰는 **검색 스윕 축**(환율·인플레·세제·지정학·공급망·경쟁·수요·규제·노무·자본통제)은 별개이며 `sz:risk-center/references/weekly-sweep.md`에 있다. 한 스윕 결과가 여러 레지스터 카테고리에 배정될 수 있다.

## 상태 3등급 (HARD)
| 등급 | 코드 | 기준 |
|---|---|---|
| 🔴 위기 (Crisis) | `crisis` | 손익 직접 충격 + 6개월 내 발효 + 회피 옵션 부재 (3조건 모두) |
| 🟡 주의 (Watch) | `watch` | 발효 ≥6개월 또는 영향 ±3% 미만 또는 회피 옵션 존재 |
| 🟢 정상 (Normal) | `normal` | 시그널만 존재, 즉시 영향 없음 |

판정 시 3요소(손익 영향·발효 시점·회피 옵션)를 각각 근거와 함께 명시한다. SECONDARY 출처만으로 위기 판정 금지(원문 확인 요청). 판정은 권고이며 최종 확정은 사용자.

## 항목 산출 형식
대시보드 스키마와 동일한 필드로 산출한다(`sz:risk-center/references/data-schema.md`): `no · status · last(YYYY-MM-DD) · title{ko,en} · summary{ko,en} · detail{ko,en} · response{ko,en} · sources[{title{ko,en}, url, date}] · decisions[]`. 표기: 자사="당사/현지 법인(LE)", 경쟁사 익명화는 프로젝트 AGENTS.md 지침을 따른다.

## 델타 브리핑 6항목 (정기 점검 후 HARD)
① 스냅샷 구간(직전→이번 기준일) ② 실질 신규 데이터(항목·출처·발표일) ③ KPI 변동 ④ 상태 등급 변화(상향/하향/해제) ⑤ 기타 갱신(문구·날짜 정합) ⑥ 다음 주기 우선순위 1~3개. 변동 없으면 "주요 변화 없음" 명시.

## 산출물
1. **리스크 표**: 항목 | 카테고리 | 상태 | 근거(손익/발효/회피) | 출처 | 발표일 | 검증등급
2. **델타 브리핑**(6항목)
3. **임원 브리핑 1페이지**(요청 시): 결론 우선 — 파일 산출은 `sz:docx-generator`·`sz:pptx-designer`·`sz:html-slide` 위임, 등급별 QA(`sz:work` 공통 규칙)

## English Summary
Classify issues into the 10-category risk register (Communication, Competitive/Market Disruption, Finance, Geo/Humanitarian, Human Capital, Legal, Operation, Product/Service, Security, Supply Chain) and grade them Crisis / Watch / Normal using three tests (direct P&L impact, effective within 6 months, no mitigation). Emit items in the dashboard data schema (`sz:risk-center`), a 6-part delta briefing, and optionally a one-page executive brief. Evidence follows `sz:uz-research` source tiers and citation tags; final judgment remains with the user.
