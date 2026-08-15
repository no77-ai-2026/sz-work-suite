---
name: risk-radar
description: |
  UZ 사업 리스크 센싱·등급 판정·브리핑 — 10카테고리 프레임, 상태 3등급(위기/주의/정상), 임원 보고 산출. 트리거: "리스크 점검해줘", "이 이슈 리스크 등급은", "리스크 브리핑 만들어줘"
  EN: UZ business risk sensing and grading — 10 risk categories, 3 status levels (Crisis/Watch/Normal), executive briefing. Triggers: "check risk level", "risk briefing", "assess this issue"
version: 1.0.0
---

# sz:risk-radar — UZ 사업 리스크 센싱 (리스크 매니지먼트)

이슈를 리스크 카테고리로 분류하고 상태 등급을 판정해 모니터링·브리핑 산출물을 만든다. 근거 조사는 `sz:uz-research` 규칙(소스 티어·인용 4분류·발표일 기준)을 따른다.

## 언어 규칙
요청 언어(KO/EN)로 응답. 임원 브리핑은 요청 시 KO/EN 병기.

## 10 리스크 카테고리
상세 정의·판정 기준: `references/risk-framework.md`
① 환율·통화 ② 세제·재정 ③ 통관·무역(보세 포함) ④ 산업 규제·인허가 ⑤ 노무·인사 ⑥ 에너지·유틸리티 ⑦ 물류·공급망 ⑧ 시장·경쟁 ⑨ 지정학·대외관계 ⑩ 컴플라이언스·법률

## 상태 3등급 (HARD 기준)
| 등급 | 기준 |
|---|---|
| 🔴 위기 (Crisis) | 손익 직접 충격 + 6개월 내 발효 + 회피 옵션 부재 (3조건 모두) |
| 🟡 주의 (Watch) | 발효 ≥6개월 또는 영향 ±3% 미만 또는 회피 옵션 존재 |
| 🟢 정상 (Normal) | 시그널만 존재, 즉시 영향 없음 |

등급 판정 시 3요소(손익 영향·발효 시점·회피 옵션)를 각각 근거와 함께 명시한다.

## 표기 규칙
- 자사는 "당사" 또는 "현지 법인(LE)"으로 표기(문서 내 법인 약어 사용은 사용자 지시에 따름).
- 모든 항목에 출처 URL + 공식 발표일 + 검증등급.

## 산출물
1. **리스크 표**: 항목 | 카테고리 | 상태 | 근거(손익/발효/회피) | 출처 | 발표일 | 검증등급
2. **델타 브리핑**(정기 점검 시): 신규 항목 / 등급 변화 / 해제 항목 / 다음 주기 우선순위 1~3
3. **임원 브리핑 1페이지**(요청 시): 결론 우선 — `sz:executive-summary` 화법, 파일 산출은 docx/pptx 스킬 위임

## English Summary
Classify issues into 10 risk categories and grade them: Crisis (direct P&L impact + effective within 6 months + no mitigation, all three required), Watch, or Normal. Every item needs source URL, official date and citation tag (via sz:uz-research). Outputs: risk table, delta briefing, one-page executive brief. Refer to the company as 'the local entity (LE)'. Details: references/risk-framework.md.
