---
name: doc-formats
description: |
  SZ 문서 양식 레이어 — 공문·품의서·회의록·주간보고·출장보고의 표준 골격과 필수 항목을 규정하고 파일 생성은 docx/pptx/xlsx 스킬에 위임. 트리거: "품의서 써줘", "공문 양식으로", "출장보고서 만들어줘"
  EN: SZ document format layer — official letters, approval requests, minutes, weekly and trip reports; delegates file creation to docx/pptx/xlsx. Triggers: "draft an approval request", "official letter format", "trip report"
version: 1.1.1
---

# sz:doc-formats — SZ 문서 양식 레이어

사내 문서의 구조·톤·필수 항목을 규정하는 얇은 레이어. 실제 파일 생성은 내장 docx/pptx/xlsx 스킬 또는 `sz:docx-generator`·`sz:pptx-designer`에 위임한다.

## 사용 절차
1. 문서 유형 판별(공문/품의/회의록/주간보고/출장보고).
2. **사내 실제 양식 파일이 있으면 먼저 업로드를 요청**하고 그 구조를 그대로 따른다. 없으면 `references/formats.md`의 표준 골격 사용.
3. 초안 작성 → 필수 항목 누락 체크리스트 확인 → 산출.

## 언어 규칙
KO 기본. 요청 시 KO/EN 병기(문단 병렬 또는 2단 표). 영어 사용자의 요청이면 EN 단독.

## 톤 규칙
- 결론·요청사항 먼저(두괄식), 경위는 뒤에.
- 수치·날짜·금액은 표로. 추정치는 "(추정)" 명기.
- 품의·공문의 요청사항은 승인권자가 예/아니오로 판단 가능한 문장으로.

## 필수 항목 체크(산출 전 자동 확인)
공문: 수신·참조·제목·발신일·발신자 / 품의: 목적·경위·내용(금액·기간)·요청사항·첨부 / 회의록: 일시·참석·안건·결정사항·액션아이템(담당·기한) / 출장보고: 기간·목적·활동·결과·후속조치·경비 요약

## English Summary
Thin layer defining SZ document skeletons (official letter, approval request, minutes, weekly report, trip report). Ask for the internal template file first; otherwise use references/formats.md. Conclusion-first tone, mandatory-field checklist before output, KO/EN bilingual on request. File generation is delegated to docx/pptx/xlsx skills.
