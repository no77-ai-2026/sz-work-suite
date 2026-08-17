---
name: uz-research
description: |
  우즈베키스탄 법규·정책·경제지표·시장 조사의 SZ 표준 엔진 — T1/T2/T3 소스 신뢰도, 인용 4분류, 원문 접근 상한, 조사 심도 3모드. 트리거: "우즈벡 규정 조사해줘", "UZ 시장 동향 확인", "이 정책 사실 확인"
  EN: SZ standard engine for researching Uzbekistan laws, policies, economy and markets — source tiers T1/T2/T3, 4-level citation tags, depth modes. Triggers: "research UZ regulation", "check this UZ policy", "UZ market trend"
version: 1.1.2
---

# sz:uz-research — 우즈베키스탄 조사 엔진 (SZ 정본)

SZ의 모든 UZ 관련 조사·검증의 표준 절차. `sz:risk-radar`·`sz:trade-logistics`·`sz:contract-review` 등이 UZ 근거 조사가 필요할 때 본 스킬 규칙을 따른다.

## 언어 규칙
사용자 요청 언어(한국어/영어)로 응답한다. 검색은 러시아어 원문을 병행한다(공식 발표는 RU가 1차인 경우가 많음).

## 조사 심도 3모드 (착수 전 확인)
| 모드 | 소요 | 범위 |
|---|---|---|
| ⚡ Quick | 3~5분 | T1 1~2곳 + T2 교차 1곳, 핵심 사실만 |
| ◐ Standard | 8~12분 | T1 우선 + T2/T3 교차검증, 표 정리 (기본값) |
| ◆ Deep | 20분+ | 전 티어 교차 + 원문 인용, 이력 추적 |
예상 소요가 8분을 초과하면 착수 전 1회 소요를 고지하고 사용자가 모드를 선택하게 한다. 무인·예약 실행은 Standard.

## 소스 신뢰도 (T1 우선, 하위 티어는 교차검증용)
상세 목록: `references/uz-sources.md`
- **T1(공식)**: cbu.uz, lex.uz, stat.uz, my.gov.uz, soliq.uz, customs.uz, WTO, USTR
- **T2(현지 매체)**: kun.uz, gazeta.uz, daryo.uz, uz.kursiv.media, uzdaily.uz, tashkenttimes.uz
- **T3(국제기구·외신)**: IMF, World Bank, EBRD, OECD, Reuters, Bloomberg, FT, Big4 리포트

## 인용 4분류 (모든 항목에 태그)
상세 규칙: `references/research-rules.md`
- `VERIFIED` — 1차 원문 확인
- `SECONDARY` — 2차 출처 확인, "⚠ 원문 재확인 필요" 병기 (Deep 모드에서는 불허)
- `NOT_FOUND` — 확인 실패(추정 서술 금지)
- `MISMATCH` — 출처 간 불일치(양쪽 값·출처 병기)

## HARD 규칙
1. **원문 접근 상한**: 원문 확보 시도는 정보원 3곳·총 5회까지. lex.uz는 JS 렌더링으로 자동 수집이 자주 실패하므로 상한 도달 시 SECONDARY로 전환하고 명시한다.
2. **날짜는 1차 출처의 공식 발표일** 기준. 2차 매체가 늦게 보도해도 발표일로 표기하고 출처명은 "발표주체 (매체 보도)" 형식.
3. 임의 URL 생성 금지, 접속일을 발표일로 쓰지 않는다.
4. 조사와 문서화(보고서 산출)는 2단 분리 — 조사 결과 확정 후 문서화 여부를 별도 확인.

## 산출물
조사 결과 표: 항목 | 내용 | 출처(URL) | 발표일 | 검증등급. 말미에 미확인 항목과 후속 확인 방법 명시.

## English Summary
Respond in the user's language (KO/EN/RU/UZ). Follow source tiers (T1 official: cbu.uz, lex.uz, stat.uz, soliq.uz, customs.uz; T2 local media; T3 international), tag every item VERIFIED / SECONDARY / NOT_FOUND / MISMATCH, cap primary-source retries at 3 sources / 5 attempts, announce estimated time before tasks over 8 minutes, use official announcement dates, and separate research from report writing. Details: references/research-rules.md, references/uz-sources.md.
