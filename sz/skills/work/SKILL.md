---
name: work
description: |
  SZ Work Suite 진입 오케스트레이터 — 요청을 팀·스킬 체인·코디네이터로 라우팅하고 산출물 등급제(⚡초안/◐작업본/◆최종본)를 적용. 트리거: "이 업무 어떻게 처리해", "뭐부터 시작할까", "최종본으로 만들어줘", "/work"
  EN: Entry orchestrator for SZ Work Suite — routes requests to team skill chains and coordinators, applies the output grade system (draft/working/final). Triggers: "how should I handle this task", "make it final quality", "/work"
version: 1.1.0
---

# sz:work — SZ Work Suite 진입 오케스트레이터

사용자 요청을 해석해 ① 적합한 스킬/체인/코디네이터로 라우팅하고 ② 산출물 등급을 적용한다.
공통 규칙 정본: `references/common-rules.md` (등급제·QA 체인·조사 규칙·언어 규칙)

## 산출물 등급제 (HARD)
| 등급 | 트리거 | 처리 |
|---|---|---|
| ⚡ 초안 | 기본값 | 검수 체인 없음 — 빠른 산출 |
| ◐ 작업본 | "다듬어줘" | `sz:ai-slop-reviewer` 1회 |
| ◆ 최종본 | "최종", "납품", "제출", "보고용", "발행" | `sz:ai-slop-reviewer` → `sz:humanize-korean` → `sz:korean-spell-check` + 수치 재검산 |
영문 산출물의 ◆최종본은 humanize-korean·korean-spell-check를 생략하고 ai-slop-reviewer + 재검산만 적용.

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
| **UZ 조사·검증** | sz:uz-research (조사 규칙 정본) |
| **리스크 센싱·브리핑** | sz:risk-radar |
| **공문·품의·보고 양식** | sz:doc-formats |
| **통관·보세·수출입** | sz:trade-logistics |
| **재고실사 사진 대조** | sz:sample-log |
| **ISA 판매 검증·인센티브** | sz:sales-verify |
단일 스킬로 끝나는 요청은 코디네이터를 거치지 않고 해당 스킬 직행(비용 절약).

## 실행 원칙 (HARD)
1. 8분 초과 예상 작업은 착수 전 소요·모드(⚡/◐/◆) 1회 고지 후 사용자 선택.
2. 조사와 문서화는 2단 분리(조사 확정 → 문서화 승인).
3. 다단계 체인 시작 전 계획(단계·산출물)을 1줄씩 보여주고 진행.
4. 언어: 요청 언어(KO/EN)로 응답.
