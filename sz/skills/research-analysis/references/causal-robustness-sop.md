# 인과 식별 강건성 SOP + 정직한 재프레이밍 (Causal Robustness SOP)

> 준실험(quasi-experimental) 관찰데이터에서 **인과 주장**을 세우거나, 세우지 못할 때 **정직하게 연관으로 후퇴**하는 표준 절차. 반드시 이 순서로 자기검증한다. DiD·event-study·stacked·placebo 코드 포함.

## 핵심 명제

> **억지 인과 < 정직한 견고 연관.** Devil(Reviewer 2) 기준에선 후자가 통과한다. 사전추세·clean-ATT가 깨지면 "인과"를 철회하고 "기업FE 견고 연관"으로 재프레이밍하되, **은폐하지 말고 한계를 그대로 제시**해 심사자를 선제 방어한다.

## 강건성 3+2종세트 — 반드시 이 순서로

### 1. 기업FE 견고성 (첫 관문)
단순 상호작용이 **기업고정효과(내부변환)에서도** 유지되는가? 여기서 붕괴하면 사실상 기각 신호.

```python
import statsmodels.formula.api as smf
# 기업FE + 연도FE, 기업 클러스터 SE
m = smf.ols('dlnCost ~ dlnSales + dec_dlnSales + post_dec_dlnSales + C(firm) + C(year)', data=df)\
      .fit(cov_type='cluster', cov_kwds={'groups': df['firm']})
print(m.params[['dlnSales','dec_dlnSales','post_dec_dlnSales']])
```

### 2. Event-study (평행추세 검증)
처치 상대연도 더미 × 상호작용. **사전(t−2, t−3) 계수 ≈ 0이어야 평행추세 성립.**
사전 계수가 유의(예: t−2 +0.6***)하면 **평행추세 위반 → 인과 주장 불가.**

```python
# rel = 처치 상대연도(-3..+3, -1 기준 생략). 각 rel×핵심상호작용 더미를 회귀에 투입
# 사전(rel<=-2) 계수의 유의성·부호를 확인 → flat이어야 통과
```

### 3. Stacked DiD (Cengiz et al. 2019) — staggered 편의 제거
코호트별 clean 스택(treated + not-yet-treated) → 스택×기업 FE, 스택×연도 FE → Goodman-Bacon 편의 제거.
**ATT 유의 + 사전추세 flat**이면 인과 근거 강화.

### 4. 위약(placebo) 검정
비처치군에 **가짜 처치시점** 부여 → **무반응이어야** 정상. 반응이 나오면 설계 오염.

### 5. 판정·재프레이밍 게이트
- 사전추세·clean ATT **통과** → 인과 주장 가능(단, 저널 인과 요구수준 확인).
- **하나라도 붕괴** → **"인과" 철회 → "기업FE 견고 연관"으로 재프레이밍.** 게재는 가능하되:
  - **타깃 하향**(예: 인과 요구 SSCI Q1 → 연관 허용 Scopus Q2).
  - **한계 절(4.5절 등)에 event-study·stacked·placebo 결과를 그대로 제시**.

## 완전분리·희소사건 대비 (로짓/카운트)

| 증상 | 원인 | 해결 |
|---|---|---|
| Singular matrix | 산업더미 다수 + 희소사건 완전분리 | 사건 0건 산업 '기타' 병합, `method='bfgs'`, 클러스터 SE |
| `get_robustcov_results` 없음 | statsmodels Logit API | `.fit(cov_type='cluster', cov_kwds={'groups': df.firm})` |
| 효과크기 누락 | p만 보고 | OR/RR/SMD + 95% CI 병기, null도 효과크기+검정력 보고 |

## ABJ 원가경직성 상호작용 (재사용 엔진)

```
Δln원가 = β1·Δln매출 + β2·(Dec·Δln매출) + β3·(Post·Dec·Δln매출) + 기업FE + 연도FE
```
- `Dec` = 매출 감소 더미. β2<0 = 원가경직성(sticky costs).
- `Post` = 정책/처치 이후. **β3 > 0 = 처치가 경직성을 완화**(핵심 관심계수).
- 표준 산출: 표본선정·기술통계·주분석·이질성(계획기간 등)·강건성 표를 `make_tables.py`로 자동화.

## 자기검증 체크리스트

```
[ ] 기업FE에서 핵심계수 유지되는가
[ ] event-study 사전계수 flat인가 (평행추세)
[ ] stacked DiD ATT 유의 + 사전 flat인가
[ ] placebo 무반응인가
[ ] 위 중 붕괴 시 "연관"으로 재프레이밍 + 한계 명시 + 저널 하향했는가
[ ] 완전분리·클러스터SE 처리했는가
```
