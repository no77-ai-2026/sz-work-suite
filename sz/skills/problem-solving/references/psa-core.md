# PSA 방법론 정본 (psa-core)

> 출처: 사내 PSA 교육자료(전정우, IQVIA, 2026-08) 재구성. 수치 예시는 교육용(Illustrative).

## 1. 전략 컨설턴트의 3대 핵심 역량

| 역량 | 성격 | 대표 툴 |
|---|---|---|
| Creative Thinking | 발산적 사고 — 기존 사고를 깨는 접근 | 브레인스토밍, SCAMPER, TRIZ |
| Logical Thinking | 수렴적 사고 — MECE 분해 후 소단위 증명 | Logic Tree, Issue Tree |
| Fact-Based Thinking | 주장·가정에 합리적 근거 | 리서치·데이터 분석 |

Logical Thinking = Thinking(사고 기법) + Approach(문제해결 접근법) + Communication(보고 스킬). 이를 체계화한 방법론이 PSA.

## 2. PSA 전체 4단계

| # | 단계 | 내용 |
|---|---|---|
| 1 | **Framing** (Problem Structuring) | 문제 범위 파악, 작은 단위로 분해, 초기가설 도출 |
| 2 | **Designing** (Analysis Structuring) | 가설 증명에 필요한 분석 규정 |
| 3 | **Gathering** (Research & Analysis) | 분석에 필요한 Fact 수집 → `sz:research-verify` 담당 |
| 4 | **Interpreting** (Structured Communication) | 가설 유효성 판단·해석·액션 결정 |

## 3. Framing·Designing 세부 5단계

| # | 단계 | 목적 | 핵심 |
|---|---|---|---|
| 1 | Key Question 도출 | 문제의 정의 | SCQ(A) 프레임워크 |
| 2 | Key Issues 도출 | KQ를 핵심 이슈로 변환 | Issue = Problematic Fact + Actionable Direction |
| 3 | Issue Break-down | 해결 가능한 수준으로 구조화 | Logic Tree, sub-issue = 개별 분석 작업 단위 |
| 4 | 가설 수립·필요근거 파악 | Evidence 수집 준비 | 가설 상정 + QDT 품질 평가 |
| 5 | Designing Analysis | 작업계획 수립 | 이슈트리 기반 Work Plan·WBS |

## 4. SCQ 프레임워크

| 요소 | 특징 | 작업 |
|---|---|---|
| Situation | 논란의 여지가 없는 사실. Historically true, easily verifiable | 현 상황 진단 |
| Complication | 안정 상태에 문제를 더하는 부분 — 프로젝트의 원인 | GAP 규명 |
| Question | 자연스럽게 파생되는 질문 | Key Question 도출 |

예시 (통신사): S=B기업 통신사업부는 항상 고수익 / C=지난 2년 수익성 감소, 향후도 감소 전망 / Q=수익성 감소의 원인이 무엇인가?
예시 (인수): S=온라인 다각화를 인수로 실행하기로 결정 / C=후보가 10개 / Q=어느 회사를 인수해야 하는가?
실무에서 SCQ는 제안서의 "프로젝트 배경 및 목적 + 수행 범위" 구조로 직결된다.

## 5. 이슈 정의

```
Issue = Problematic Fact + Specific, Actionable Direction
```

- 이슈 = "사실에 근거해, 선택지가 보이는 닫힌 질문". 이슈 정의는 프로젝트 전체 공수의 방향타
- "어떻게 건강해질까?"에는 브레인스토밍밖에 못 하지만, "약을 시작해야 하는가?"에는 검사(분석)로 답할 수 있다
- 표준 문형: **"[문제적 사실]인 상황에서, [대안 A를 해야 하는가 / A vs B]?"** — 경영진 의사결정으로 귀결
- Fact·항상 참인 질문·"왜?"형 열린 질문은 이슈가 아님. 상세 판정은 `issue-gates.md`

## 6. 로직트리 3대 구조 원칙

| 원칙 | 역할 |
|---|---|
| **MECE** | 수직 완전성 — 같은 레벨이 겹치지 않고(ME) 상위를 빠짐없이 포괄(CE). 단, 엄밀한 MECE보다 "상대에게 가치 있는 MECE"가 중요 |
| **Force at Work** | 통찰 — 트리 절단면이 비즈니스 실동인(원가구조·시장동학·의사결정 로직)을 포착. 1·2레벨 구분이 제일 중요 |
| **So What? / Why So?** | 수평 논리 검증 — 상위→하위(So What, 하향), 하위→상위(Why So, 상향)를 매 레벨 확인. So What 하면 반드시 Why So로 검증 |

## 7. 가설·Evidence

- Issue → Hypothesis(가장 현실적·실현 가능한 Solution, Yes/No + because) → Evidence(증명 또는 반박 자료)
- 80:20 법칙 — 결과에 막대한 영향을 미치는 핵심요소 위주로 분석
- QDT(Quick and Dirty Test): ① 가설이 참이 되려면 어떤 전제가 필요한가 ② 가설을 틀리게 할 요인은 무엇인가 — 전제가 약하면 나쁜 가설
- 예시: "새 기계가 더 잘 작동할 것" → 논거(생산성↑·내구성↑·유연성↑) → Evidence(단위시간당 생산량, 연간 정비 건수, 불량률)

## 8. Work Plan (6컬럼)

| 컬럼 | 정의 |
|---|---|
| Issue | 로직트리 말단에서 시작. Yes/No 응답 또는 구체적 행동이 제시되는 형태 |
| 가설 | Issue별 해결안. 팀 토의로 crystallize, 분석 우선순위 결정 |
| 분석 | 가설 증명/부정에 필요한 분석. 필요 수준(간단한 사례 vs 복잡한 증명) 결정 |
| Source | 정보의 종류·소재지·획득 방법 |
| 책임자/일정 | 획득·분석 책임자와 기한 |
| 결과물 | 예상 분석결과·산출물 (Blank Chart, Story-line) |

이슈트리가 그대로 WBS·간트차트로 전환된다. 전체 흐름: Key Question ≫ Issue → Sub-Issue → 가설 → Evidence → 과업 = 하나의 "Story Line".
