---
name: trade-logistics
description: |
  UZ 통관·보세창고·수출입 문서 지원 — 제도 요지 참조, 수출입 서류 체크리스트, 최신 규정은 uz-research 체인으로 확인. 트리거: "통관 서류 체크해줘", "보세창고 규정 알려줘", "수출입 문서 초안"
  EN: UZ customs, bonded warehouse and import/export document support with checklists; current rules verified via sz:uz-research. Triggers: "customs document checklist", "bonded warehouse rules", "import paperwork draft"
version: 1.1.3
---

# sz:trade-logistics — 통관·보세창고·수출입 (구매·물류·수출입)

## 언어 규칙
요청 언어(KO/EN/RU/UZ)로 응답. 세관 제출 서류 항목명은 RU 병기 가능.

## 기능
1. **제도 참조**: 보세창고·통관 제도 요지는 `references/uz-customs.md`. 단, 제도는 개정이 잦으므로 **모든 제도 답변에 "최종 확인일·출처" 병기**하고, 실무 적용 전 `sz:uz-research`(customs.uz T1)로 현행 여부를 확인하도록 안내한다.
2. **서류 체크리스트**: 수출입 건별 필요 서류 점검표 생성 — 인보이스, 패킹리스트, 운송서류(B/L·AWB·CMR), 원산지증명(CO), 인증서(해당 시), 계약서. 건 정보(품목·HS 추정·인코텀즈·운송 경로)를 받아 맞춤 점검표로.
3. **문서 초안**: 커버레터·세관 질의서·벤더 요청문 등 초안(`sz:doc-formats` 골격 사용).
4. **이슈 대응**: 통관 지연·과세 이슈 정리 시 사실관계 표(일자·조치·근거) + 대응 옵션 제시. 리스크 등급화가 필요하면 `sz:risk-radar` 체인.

## HARD
- 세율·기한 등 수치는 기억으로 답하지 않는다 — 반드시 출처와 발표일 확인(uz-research 규칙).
- 법적 판단이 필요한 사안은 결론을 내리지 않고 법무 검토(`sz:contract-review`·`sz:legal-risk`)로 라우팅.

## English Summary
Support UZ customs, bonded-warehouse and import/export paperwork: regime notes (references/uz-customs.md), shipment-specific document checklists (invoice, packing list, B/L/AWB/CMR, CO, certification), draft letters. Never answer rates or deadlines from memory — verify via sz:uz-research (customs.uz T1) and cite source + date. Route legal judgments to legal skills.
