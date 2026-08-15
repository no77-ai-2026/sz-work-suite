# sz v1.0.0 (2026-08-14)

## 최초 릴리스 — SZ Work Suite
- 기반: GIL v2.2.0 3번들(gil 148 · gil-creative 96 · gil-commerce 54, Apache-2.0+MIT)
- 이식 206스킬 (제외 92: 개인·비업무 74 + BYOK/인증 11 + SNS 발행 5 + 한국 광고법규 2 → EXCLUDED-SKILLS-v1.0.0.txt)
- SZ 특화 신규 6: uz-research(조사 엔진: T1/T2/T3·인용 4분류·심도 3모드) · risk-radar(10카테고리·상태 3등급) ·
  doc-formats(문서 양식 레이어) · trade-logistics(통관·보세창고) · sample-log(재고실사 사진 대조) ·
  sales-verify(ISA 판매 검증·세일즈 인센티브, IMEI Luhn·재촬영 감지·중복 플래그)
- 공용 판독 엔진 정본: sample-log/references/photo-id-match.md (sales-verify와 동기화 사본)
- 네임스페이스: gil*: → sz: 평탄화 1,409건, 미포함 스킬 참조 98건 "(미포함)" 처리
- MCP 5종(무키): dart · korean-law · korean-stats · archhub · kordoc / 에이전트: v1.0 미포함
- 게이트: dir==name·kebab·예약어·버전 전 지점 1.0.0·끊긴 참조 0·gil/moai 잔존 0·비ASCII 0 — 전수 PASS
- 라이선스: Apache-2.0 (LICENSE·LICENSE.MIT·NOTICE.md 보존 + 사내판 고지)
- 확인 대기: problem-solving·research-verify 원자료(사내 교육자료) 이용 조건 — 배포 전 사용자 확인
