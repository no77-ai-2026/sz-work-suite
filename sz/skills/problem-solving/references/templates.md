# 산출물 템플릿 (templates)

## 1. ⚡초안 — 1페이지 문제정의서

```markdown
# 문제정의서: [과제명]

**핵심 메시지**: (1문장 — 무엇이 문제이고 무엇을 결정해야 하는가)

## SCQ
| 요소 | 내용 | 비고 |
|---|---|---|
| Situation | (검증 가능한 사실만) | 출처/근거 |
| Complication | (안정 상태를 깨는 GAP) | 출처/근거 |
| Question | (파생되는 Key Question) | |

※ 리프레이밍 점검: 이 Question이 옳은 문제인가? 대안 프레임: (있으면 1줄)

## 이슈 후보 3안 + 3-Test
| # | Issue Statement | Fact | Fork | Action | 미달 사유 |
|---|---|---|---|---|---|
| 1 | [문제적 사실]인 상황에서, [A vs B]? | ✓/✗ | ✓/✗ | ✓/✗ | (미달 시 1줄) |
| 2 | | | | | |
| 3 | | | | | |

**권고안**: N안 (사유 1줄) — 최종 선택은 사용자 확인
**[추정] 항목 검증 목록**: (sz:research-verify 이관 대상)
```

## 2. Issue Statement 4행 표 (이슈화 작업용)

| 단계 | 내용 |
|---|---|
| Key Question | (원 질문) |
| Problematic Fact | (검증된 사실. 미확인 시 [추정]) |
| Actionable Direction | (대안 A vs B) |
| **Issue** | "[문제적 사실]인 상황에서, [A를 해야 하는가 / A vs B]?" |

## 3. ◐작업본 — 로직트리 + 가설·Evidence

```markdown
## 로직트리 ([유형] Tree — 선택 사유 1줄)
(트리 텍스트/도식. 레벨당 3~5개, 최대 7개. 가지치기 항목과 사유 병기)

### 게이트 점검
- MECE: (중복/누락 검사 결과)
- Actionable·Relevant: (미달 노드와 조치)
- So What/Why So: (레벨 간 비약 검사 결과)

## 가설·Evidence 목록
| Sub-Issue | 가설 (Yes/No + because) | QDT ①전제 | QDT ②반증 요인 | 필요 Evidence |
|---|---|---|---|---|
```

## 4. ◆최종본 — Work Plan 6컬럼

| Issue | 가설 | 분석 | Source | 책임자/일정 | 결과물 |
|---|---|---|---|---|---|
| (트리 말단) | Yes/No + because | (증명/부정 분석) | (정보 소재·획득 방법) | (담당·기한) | (Blank Chart·산출물) |

+ 스토리라인: Key Question ≫ Issue → Sub-Issue → 가설 → Evidence → 과업 흐름을 피라미드 구조(핵심 메시지 → 근거)로 서술.

## 5. 출력 공통 규칙

- 산출물 최상단에 핵심 메시지 1문장
- 표로 정리 가능한 내용은 서술 대신 표
- 미확인 사실은 [추정], 검증 필요 항목은 별도 목록화
- 말미에 검증 3원칙 고지 (SKILL.md 참조)
