# SZ 공통 규칙 정본 (SSOT) — v1.1.1

## 1. 언어 (HARD)
- 요청 언어로 대화·산출: **KO / EN / RU / UZ**. 언어를 임의로 바꾸지 않는다.
- 공식 문서는 요청 시 KO/EN 또는 KO/RU 병기.
- 한국어 전용 QA(humanize-korean·korean-spell-check)는 비한국어 산출물에서 생략 + 1줄 고지. ai-slop-reviewer·수치 재검산은 전 언어 적용.

## 2. 승인 게이트 (HARD)
- 파일 산출물·다단계 체인·대량 작업: 계획(산출물·단계·전/후 비교) 제시 → 명시 승인 → 착수.
- 임의 선제작 금지. 예외: 단순 답변·1회성 소규모 초안.

## 3. 산출물 등급제
- ⚡ 초안(기본): 검수 없음.
- ◐ 작업본("다듬어줘"): ai-slop-reviewer 1회.
- ◆ 최종본("최종·납품·제출·보고용·발행" 명시 시만): ai-slop-reviewer → (한국어) humanize-korean → korean-spell-check + 수치·집계 재검산. 머리에 "◆최종본 QA 완료" 1줄.

## 4. 프로젝트 지침 파일
- AGENTS.md/CLAUDE.md 존재 시 그 규칙이 본 정본보다 우선.
- 산출물 완료 후 evolution log 1줄 추가를 제안(승인형 — 무단 수정 금지).
- 반복 업무 프로젝트에는 sz:work 프로젝트 세팅 모드로 AGENTS.md(정본)+CLAUDE.md(@AGENTS.md 포인터, 빈 파일 금지)를 함께 생성(승인 후).

## 5. 조사 규칙 (정본: sz:uz-research references)
- 인용 4분류 VERIFIED/SECONDARY/NOT_FOUND/MISMATCH · 원문 접근 상한 3곳·5회 · 심도 3모드(8분 초과 사전 고지) · 1차 출처 발표일 기준.

## 6. 문서·판정 원칙
- 사내 양식 우선 요청(sz:doc-formats). 결론 우선. 실데이터·개인정보를 예시로 남기지 않음.
- 사진 판독 추측 금지·재촬영 의심 자동 리젝 금지, 법적 판단·지급 결정·위기 판정은 근거만 제시 — 최종 판정은 사용자.
