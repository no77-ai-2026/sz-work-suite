# SZ Work Suite (`sz`)

Internal Claude Cowork plugin for SZ business & management support teams. v1.1.0 adds a harness layer: `sz:work` orchestrator, 21 coordinator agents, and an output grade system (draft/working/final QA chain).
**212 skills** covering strategy & reporting, document production (Word/PPT/Excel/HWP/PDF), finance & accounting, legal & compliance, HR/GA, procurement & trade logistics, sales & CS, data analysis, research, marketing & design, and commerce operations — plus **6 SZ-specific skills**.

> Private, internal use. Based on GIL v2.2.0 bundles (Apache-2.0 + MIT). See NOTICE.md.

## Installation

**Option A — marketplace (recommended)**
1. In Claude (Cowork), run: `/plugin marketplace add no77-ai-2026/sz-work-suite`
2. Install the `sz` plugin from the marketplace list.

**Option B — file upload**
Download `releases/sz.plugin` and upload it via Cowork plugin settings.

## Getting started (first run)

1. **Install**: Claude desktop app > Settings > Plugins > *Add marketplace* > enter `no77-ai-2026/sz-work-suite` > install **sz**. (Or upload `releases/sz.plugin` directly.)
2. **Say what you need in plain language** — Korean, English, Russian or Uzbek. Examples:
   - "이번 주 주간보고 만들어줘" / "Draft this week's report"
   - "Проверь этот контракт" (contract review)
   - "재고실사 사진 대조해줘" (upload ledger + photos)
3. **Or start from the orchestrator**: type `/sz:work` or say "이 업무 어떻게 처리해?" — it routes your request to the right skill chain.
4. **Working on a recurring project?** Say "프로젝트 세팅해줘" once in that project folder. After a 4-question interview it creates `AGENTS.md` (project rules) + `CLAUDE.md` (loader pointer) — from then on every session in that project follows your rules automatically.
5. **Output quality levels**: default is a quick draft. Say "다듬어줘" for a polished working version, or "최종본으로" / "final" for the full QA chain (style review + spell check + number recheck).

### 처음 사용하는 분께 (KO)
설치 후 그냥 한국어로 업무를 요청하면 됩니다. 반복 업무가 있는 프로젝트 폴더에서는 "프로젝트 세팅해줘"를 한 번 실행해 두면 이후 세션이 규칙을 자동으로 따릅니다. "최종본으로"라고 하면 3중 검수를 거칩니다.

## Known limitations (v1.1)

- External image/video/audio generation (Higgsfield, image APIs), SNS auto-publishing (Instagram/Threads) and a few key-based connectors are **not included** — mentions of them inside some skills can be ignored; those steps are simply skipped.
- `korean-law` MCP works better with a personal OC id (`KOREAN_LAW_OC` env var, free from open.law.go.kr); without it some law lookups fall back to web search.
- Coordinator agents cover multi-step workflows; single-skill requests run directly without them.

## Language

All skills respond in **your language** — ask in English, get English; ask in Korean, get Korean. The 6 SZ-specific skills carry bilingual (KO/EN) documentation.

## SZ-specific skills

| Skill | Team | What it does |
|---|---|---|
| `sz:uz-research` | All | Uzbekistan law/policy/market research engine — source tiers (T1 official / T2 local media / T3 international), citation tags (VERIFIED/SECONDARY/NOT_FOUND/MISMATCH), retry caps, depth modes |
| `sz:risk-radar` | Risk Management | Risk sensing across 10 categories, 3 status grades (Crisis/Watch/Normal), executive briefings |
| `sz:doc-formats` | All | SZ document skeletons: official letter, approval request, minutes, weekly report, trip report (KO/EN) |
| `sz:trade-logistics` | Procurement/Logistics | UZ customs & bonded-warehouse notes, shipment document checklists |
| `sz:sample-log` | Risk Management | Stocktaking photo reconciliation: extract serial/ID from photos, rename files, match against the sample ledger, sort into matched/unmatched/unreadable/recapture-suspected folders, report |
| `sz:sales-verify` | Sales Support | ISA sales verification for sales incentive: match sales-history Excel vs field-force IMEI/serial photos, Luhn IMEI check, duplicate-IMEI and screen-recapture fraud flags, per-field-force payout basis |

Shared photo-ID matching engine (single source of truth): `sz/skills/sample-log/references/photo-id-match.md`.

## Typical everyday skills

`weekly-report`, `meeting-facilitator`, `executive-summary`, `docx-generator`, `pptx-designer`, `xlsx-creator`, `contract-review`, `nda-triage`, `financial-statements`, `variance-analysis`, `resume-screener`, `draft-offer`, `proposal-writer`, `ticket-triage`, `data-explorer`, `data-visualizer`, `ai-slop-reviewer`, `korean-spell-check`, and ~190 more. Ask Claude "what can the sz plugin do for <my task>?".

## 한국어 요약

SZ 업무·경영지원 파트 공유 플러그인입니다. 212스킬(GIL v2.2.0 기반 사내판 206 + SZ 특화 6). 설치는 위 Option A/B, 스킬은 요청 언어(한국어/영어)로 응답합니다.

## License

Apache-2.0 (with MIT components). Upstream attributions preserved in `NOTICE.md`, `LICENSE`, `LICENSE.MIT`. Internal distribution for SZ staff.
