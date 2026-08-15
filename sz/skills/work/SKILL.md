---
name: work
description: |
  SZ Work Suite 진입 오케스트레이터 — 요청을 팀·스킬 체인·코디네이터로 라우팅, 산출물 등급제(⚡초안/◐작업본/◆최종본)와 승인 게이트 적용, 프로젝트 지침(AGENTS.md) 준수·갱신. 트리거: "이 업무 어떻게 처리해", "프로젝트 세팅해줘", "최종본으로 만들어줘", "/work"
  EN: Entry orchestrator for SZ Work Suite — routes requests to team skill chains and coordinators, applies output grades (draft/working/final), approval gates, and project instruction files (AGENTS.md). Triggers: "how should I handle this task", "set up this project", "make it final quality", "/work"
version: 1.1.1
---

# sz:work — SZ Work Suite 진입 오케스트레이터

공통 규칙 정본: `references/common-rules.md` (등급제·승인 게이트·QA 체인·조사 규칙·언어 규칙)

## 언어 규칙 (HARD)
**요청 언어로 대화·산출한다 — 한국어/영어/러시아어/우즈벡어(KO/EN/RU/UZ).** 사용자가 러시아어로 물으면 러시아어로 진행한다. 공식 문서는 요청 시 KO/EN 또는 KO/RU 병기. 한국어 전용 QA 단계(humanize-korean·korean-spell-check)는 비한국어 산출물에서 생략하고 1줄 고지하며, ai-slop-reviewer와 수치 재검산은 전 언어에 적용한다.

## 승인 게이트 (HARD)
- **파일 산출물·다단계 체인·대량 작업은 착수 전에 계획을 제시하고 사용자 명시 승인 후 시작한다.** 계획에는 산출물 목록·단계·(변경 작업이면) 전/후 비교를 담는다.
- 예외: 단순 질문 답변, 1회성 텍스트 초안, 사용자가 이미 형식·내용을 특정한 소규모 요청.
- 임의 선제작 금지 — 요청받지 않은 보고서·문서를 미리 만들지 않는다.

## 산출물 등급제 (HARD)
| 등급 | 트리거 | 처리 |
|---|---|---|
| ⚡ 초안 | 기본값 | 검수 체인 없음 |
| ◐ 작업본 | "다듬어줘" | `sz:ai-slop-reviewer` 1회 |
| ◆ 최종본 | "최종", "납품", "제출", "보고용", "발행" | `sz:ai-slop-reviewer` → (한국어) `sz:humanize-korean` → `sz:korean-spell-check` + 수치 재검산 |

## 프로젝트 지침 준수·갱신 (HARD)
1. 프로젝트 폴더에 `AGENTS.md` 또는 `CLAUDE.md`가 있으면 **먼저 읽고 그 규칙을 본 스킬 기본값보다 우선** 적용한다.
2. 산출물 완료 시 지침 파일 말미의 evolution log에 1줄(날짜·산출물·변경 요지) 추가를 **제안**한다 — 승인형: 사용자가 동의한 경우에만 파일을 수정하고, 무단 수정하지 않는다.
3. 지침 파일이 없고 반복 작업이 예상되면 프로젝트 세팅(아래)을 1회 제안한다.

## 프로젝트 세팅 모드
"프로젝트 세팅해줘" → ① 목적 ② 담당 팀·주 사용자 ③ 주요 산출물 유형 ④ 특수 규칙(익명화·양식 등) 4문항 인터뷰 → `AGENTS.md` 골격 생성: 프로젝트 목적 / HARD 규칙 / 산출물별 워크플로(라우팅 맵 오버라이드) / 등급제 재정의(필요 시) / evolution log 섹션. 생성 전 초안을 보여주고 승인받는다.

## 라우팅 맵 (요청 → 1차 목적지)
| 요청 유형 | 목적지 |
|---|---|
| 전략·사업계획·IR | business-plan-coordinator |
| 텍스트 최종 검수 | core-text-qa-coordinator |
| 데이터 분석·시각화·리포트 | data-analysis-coordinator |
| 결산·재무제표·변동분석 | finance-report-assembler |
| 채용·온보딩·인사 | hiring-coordinator |
| 계약·NDA·법적 리스크 | legal-review-coordinator |
| 프로세스·벤더·회의→보고 | operations-coordinator |
| 제안서 작성·마감 | sales-proposal-coordinator |
| 고객 문의 분류·응대 | support-ticket-triage-batch |
| 교육·연수 설계 | education-course-builder |
| UX·제품 기획 | product-ux-audit-coordinator |
| 마케팅 캠페인·감사·콘텐츠 | marketing-campaign-coordinator / marketing-audit-coordinator / content-publishing-pipeline |
| 커머스 런칭·성장·상세페이지 | commerce-launch-coordinator / commerce-growth-analyst / commerce-detail-page-builder |
| UZ 조사·검증 | sz:uz-research |
| 리스크 센싱·브리핑 | sz:risk-radar |
| 공문·품의·보고 양식 | sz:doc-formats |
| 통관·보세·수출입 | sz:trade-logistics |
| 재고실사 사진 대조 | sz:sample-log |
| ISA 판매 검증·인센티브 | sz:sales-verify |
단일 스킬로 끝나는 요청은 코디네이터 없이 해당 스킬 직행.

## 실행 원칙 (HARD)
1. 8분 초과 예상 작업은 착수 전 소요·모드(⚡/◐/◆) 1회 고지 후 사용자 선택.
2. 조사와 문서화는 2단 분리(조사 확정 → 문서화 승인).
3. 다단계 체인은 계획 승인 후 진행하며, 단계 완료마다 간결히 보고.
