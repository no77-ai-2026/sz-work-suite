# sz v2.1.0 (2026-09-16) — issue-report 편입

- New **`issue-report`**: SEUZ 총괄 주간현안 1페이지 상세보고서(.docx). 독립 플러그인 `sz-repo`를 플러그인 내부 스킬로 편입 — 스킬 ID `sz:issue-report`
  - 계열 4종(A 재무·여신·보험 / B1 규제·법령 / B2 대외·관계기관 / B3 출장·사건)으로 세분, 계열별 규칙 강도표
  - CFO 확정본 3건(W36 채권 Top-up 보험 헷징 · W37 우즈벡 기업 규제 완화 · W37 주우 한국 대사관 CSR)에서 역산한 문체 규칙을 `references/cfo-review-log.md`에 축적
  - `scripts/lint_report.py` 신규 — 문체 린터. ERROR(확정본 전수 교정) / WARN(계열별 상이) / INFO(1회 관찰, 승격 대기) 3단계
  - `scripts/diff_review.py` 신규 — 초안·확정본 대조로 블록 구조·줄 단위·주석·용어 치환쌍 추출
  - `scripts/build_report.py` — `title_notes`(제목 주석) 지원 추가, 줄넘침·주석넘침·분량초과 3종 자동 점검
  - 승격 절차: diff → cfo-review-log 사례 기록 → **같은 지적 2회 반복 시** style-guide 규칙 승격 + 린터 검사 항목 추가
- 트리거 충돌 차단: 편입 전 `sz-repo`의 광역 문구 4종("주간 보고 정리해줘" / "1페이지 보고서" / "이 내용 보고서 양식으로" / "총괄 보고서 만들어줘") 제거 — `weekly-report`·`executive-summary`·`docx-generator`·`status-reporter`와의 오발동 차단. description 말미에 `※` 배제 안내 추가
- `doc-formats`: 삼성 법인 1페이지 주간현안은 `sz:issue-report`로 위임하도록 서두·사용 절차 1단계에 분기 명시
- 버전: plugin.json · marketplace.json · 전 SKILL.md 68개 모두 2.1.0으로 일치
- 스킬 67 → **68**

# sz v2.0.0 (2026-09-12) — lean edition, GIL v2.3.1 rebase, risk-center, wiki

- Rebased on GIL v2.3.1 (Apache-2.0): credential wiring via plugin.json `userConfig` + `${user_config.KEY}`, sz:work re-ported from gil:project v2.3.1 (8-lens interview, no-reply≠refusal, evolution log SSOT), QA chain order ai-slop → spell-check → humanize, `user-invocable` removed
- Scope cut 213 → **67 skills** for daily work (core 28 · team 33 · UZ channels 3 · html-slide · design-system-library · wiki); 92+ personal/marketing/commerce skills dropped; refs to dropped skills marked "(미포함)"
- Agents auto-pruned 21 → **6** (kept when ≥70% of referenced skills exist): core-text-qa · data-analysis · finance-report-assembler · hiring · legal-review · operations
- MCP 5 → **2** (korean-law with userConfig KOREAN_LAW_OC, kordoc); dart/archhub/korean-stats removed
- **RM alignment**: `risk-radar` now uses the 10-category risk register (Communication · Competitive/Market Disruption · Finance · Geo/Humanitarian · Human Capital · Legal · Operation · Product/Service · Security · Supply Chain) + 6-part delta briefing; new **`risk-center`** (init / update / report / doctor) with data-stripped dashboard template (per-category samples, `MODULES` switches), data schema, weekly sweep axes A–D with RU/EN auxiliary terms, report outline, verification-log format, RM AGENTS.md preset
- New **`wiki`** (LLM-Wiki): compile / ingest / lint / init, operations constitution, page template, project wiring question in sz:work project setup
- Build system: `sz-build/` manifest allowlist + `build-sz.py` one-command pipeline + `custom/` intake (template, 8-item checklist) + `masking.json` + `tools/strip-dashboard.py`; Windows runner `BUILD-SZ-v2.bat`
- Gates PASS: dir==name · kebab · reserved · version 2.0.0 all points · missing refs 0 · gil/legacy refs 0 · forbidden terms 0 · non-ASCII paths 0 · zip 398 entries

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

# sz v1.1.0 (2026-08-15)
- Harness layer: sz:work entry orchestrator (routing map + output grade system draft/working/final) + references/common-rules.md (SSOT)
- 21 coordinator agents ported from GIL (5 skipped: skills not present in sz) — namespace sz:, dangling refs cleaned
- QA chain wiring: "final/submit/report" keywords trigger ai-slop-reviewer > humanize-korean > korean-spell-check + recalculation
- 213 skills, all versions 1.1.0

# sz v1.1.1 (2026-08-15)
- Approval gate (HARD): file deliverables / multi-step chains require plan + explicit user approval before execution; no unsolicited deliverables
- Project instruction files: read & obey AGENTS.md/CLAUDE.md first; propose evolution-log entry after each deliverable (opt-in); lightweight project setup mode (4-question interview -> AGENTS.md skeleton)
- Language rule extended to KO/EN/RU/UZ across sz:work, common-rules and 6 SZ-specific skills; Korean-only QA steps skipped with notice for non-Korean outputs

# sz v1.1.2 (2026-08-18)
- Fix: project setup now ALWAYS creates CLAUDE.md pointer (@AGENTS.md) alongside AGENTS.md — empty CLAUDE.md silently broke auto-loading of project rules in new sessions
- Templates embedded: work/references/templates/AGENTS.md.tmpl + CLAUDE.md.tmpl (verbatim copy, no-backtick warning)
- Doctor check: detect empty/broken CLAUDE.md pointer and propose repair (opt-in)

# sz v1.1.3 (2026-08-18)
- Audit fixes: legacy .gil/ paths -> .sz/ (3 skills); YAML description marker unified; optional .sz/refs guidance in project setup
- README: Getting started (first-run guide, KO/EN) + Known limitations section

# sz v1.2.0 (2026-08-18)
- sz:work upgraded to FULL gil:project port (individual-use mode): Socratic interview init, AGENTS.md(<=100 lines)+CLAUDE.md pointer+.sz/ scaffold+.claude/agents custom agents, approval-based self-improvement (/work evolve), /work update sync, /work doctor diagnostics (incl. empty-pointer repair), legacy CLAUDE.md migration, 13 core protocol refs + templates
- SZ extensions preserved: KO/EN/RU/UZ language rule, SZ-specific 6-skill routing table, output grade system (core common-rules SSOT)
