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
