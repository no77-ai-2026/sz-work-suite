# SZ Work Suite (`sz`) — v2.0.0

Claude Cowork plugin for SZ business & management support teams — **67 skills, 6 coordinator agents, 2 MCP servers**, one harness.
Lean by design: the everyday toolbox every team shares, plus the harness that keeps every session on the same rules. Team-specific workflows are added later as custom skills (see *Adding your own skills*).

> Based on GIL v2.3.1 bundles (Apache-2.0 + MIT). Attributions preserved in `NOTICE.md`, `LICENSE`, `LICENSE.MIT`.

## Install

**Marketplace (recommended)** — Claude desktop app → Settings → Plugins → *Add marketplace* → `no77-ai-2026/sz-work-suite` → install **sz**.
**File** — upload `releases/sz.plugin` in the plugin settings.

On first use the app asks for one optional key: `KOREAN_LAW_OC` (free, law.go.kr) — only needed for Korean statute lookups. Everything else works without it.

## Getting started (first run)

1. Ask in plain language — **Korean, English, Russian or Uzbek**. Skills answer in your language.
   - "이번 주 주간보고 만들어줘" · "Draft the meeting minutes" · "Проверь этот контракт"
2. `/sz:work` — the orchestrator. Say what you need; it routes to the right skill chain and applies output grades:
   default **draft** → "다듬어줘" **working** → "최종본으로" / "final" **full QA chain**.
3. Recurring project? Say **"프로젝트 세팅해줘"** once in that folder. After a short interview it writes `AGENTS.md` (rules) + `CLAUDE.md` (loader pointer); every later session in that folder follows them. `/sz:work doctor` checks the setup, `/sz:work evolve` proposes improvements (approval-gated).
4. Anything that changes files, runs multi-step chains or costs more than ~8 minutes shows a plan first and waits for your OK.

## What's inside

| Area | Skills |
|---|---|
| Harness | `work` (orchestrator, project scaffold, self-improvement, doctor) |
| **SZ-specific** | `uz-research` · `risk-radar` · **`risk-center`** · `doc-formats` · `trade-logistics` · `sample-log` · `sales-verify` · **`wiki`** |
| Documents | docx · pptx · xlsx · hwpx · pdf · html-report · **html-slide** · doc-reader · **design-system-library** |
| Text QA | ai-slop-reviewer · humanize-korean · korean-spell-check |
| Reporting | weekly-report · executive-summary · meeting-facilitator · report-speak · stakeholder-update · status-reporter |
| Research | research-verify · problem-solving · daily-briefing · language-tutor |
| Finance | financial-statements · close-management · journal-entry · reconciliation · variance-analysis · audit-support |
| Legal | contract-review · nda-triage · legal-risk · compliance-check · legal-response |
| HR / GA | employment-manager · resume-screener · interview-prep · draft-offer · policy-lookup · performance-review · process-manager · vendor-manager · vendor-check · event-planner |
| Sales support | call-summary · draft-response · pipeline-review · sales-forecast |
| Data | data-explorer · data-visualizer · statistical-analysis · validate-data · build-dashboard |
| Strategy | strategy-planner · market-analyst · consulting-brief |
| UZ channels | marketplace-uzum · yandex-market · telegram-commerce |

Agents: core-text-qa · data-analysis · finance-report-assembler · hiring · legal-review · operations coordinators.

### Risk Management: `sz:risk-center`
Rebuilds and runs the single-file HTML **risk-sensing dashboard** (Home / 10-category risk register / WTO / Bonded warehouse / Report archive).
- `init` — folders, data-stripped template (per-category sample items, `MODULES` switches), RM-specific `AGENTS.md`
- `update` — weekly full sweep (axes A–D, RU/EN auxiliary terms, primary-channel checks) → regrade via `risk-radar` → new versioned HTML → URL verification → QA → verification log → 6-part delta briefing
- `report` — approved deep-dive DOCX in the standard outline, summary embedded into the archive (no file links)
- `doctor` — snapshot/version/i18n/archive consistency
Data schema for skills that feed the dashboard: `sz/skills/risk-center/references/data-schema.md`.

### Knowledge: `sz:wiki`
Personal LLM-Wiki kept apart from working folders — `compile` (chat → frontmatter page in `_inbox/`), `ingest` (placement/promotion proposals, approval-gated), `lint`, `init`. Projects can point at a wiki domain ("위키 기준으로") and skills offer to compile reusable lessons.

## Adding your own skills

Drop a folder `custom/<skill-name>/SKILL.md` into the build tree (`sz-build/custom/`), tick the 8-item `INTAKE-CHECKLIST.md`, run `BUILD-SZ-v2.bat`. The build script merges, namespaces, masks, prunes agents, runs gates and zips in one step; the manifest `sz-manifest.json` is the single source of truth.

## Known limitations
- No external image/video/audio generation, no SNS auto-publishing, no DART/ARCHHUB MCPs in this edition — mentions inside some skills are marked "(미포함)" and simply skipped.
- `kordoc` MCP (HWP parsing) needs Node.js on the machine.

## 한국어 요약
업무·경영지원 파트용 얇은 공용 도구함 67스킬 + 하네스. 설치 후 한국어로 요청하면 됩니다. 반복 프로젝트는 "프로젝트 세팅해줘" 1회, 리스크 대시보드는 "리스크 대시보드 프로젝트 세팅", 지식 축적은 "위키로 컴파일". 팀별 개별 스킬은 `sz-build/custom/`에 넣고 빌드하면 자동 포함됩니다.

## License
Apache-2.0 (with MIT components). See `NOTICE.md`.
