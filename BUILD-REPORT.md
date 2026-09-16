# sz build report — v2.1.0

- base: v2.0.0 (67 skills) + custom intake 1
- custom skills: 1 ['issue-report'] — 독립 플러그인 `sz-repo`에서 편입, 폴더 구조(references/ scripts/ assets/) 무변경
- skills total: **68**
- agents: 6 (변동 없음) — core-text-qa · data-analysis · finance-report-assembler · hiring · legal-review · operations
- mcp: ['korean-law', 'kordoc'] (변동 없음) | userConfig: ['KOREAN_LAW_OC']
- version parity: plugin.json 2.1.0 · marketplace.json(metadata·plugins) 2.1.0 · SKILL.md 68/68 2.1.0
- 수동 게이트 (샌드박스 미가동으로 스크립트 대신 수동 검사)
  - dir==name: PASS (`skills/issue-report` ↔ `name: issue-report`)
  - kebab-case: PASS
  - reserved word: PASS
  - 끊긴 스킬 참조: PASS — issue-report가 참조하는 sz:weekly-report · sz:status-reporter · sz:executive-summary · sz:docx-generator 4종 모두 존재
  - 잔존 `sz-repo` 참조: 0건 (전 트리 grep)
  - 비ASCII 경로: PASS
- **미수행 (GIL PC에서 실행 필요)**
  - 회귀 테스트: `lint_report.py assets/example-w36-cfo.json` → "문체 점검 이상 없음"
  - 회귀 테스트: `build_report.py assets/example-w36-cfo.json /tmp/t.docx --md /dev/null` → "점검 사항 없음"
  - zip 재패키징: `releases/sz.plugin` (예상 엔트리 398 → 407)

---

# sz build report — v2.0.0

- GIL skills merged: 58
- sz:work ported from gil:project (+SZ extension)
- overlay skills: 3 ['risk-center', 'risk-radar', 'wiki']
- carried from prev: 5 ['uz-research', 'doc-formats', 'trade-logistics', 'sample-log', 'sales-verify']
- custom skills: 0 []
- skill refs to excluded skills marked (미포함): 50 ['audio-gen', 'blog', 'campaign-planner', 'card-news', 'commerce-influencer-collab', 'commerce-market-research', 'commerce-morning-brief', 'commerce-voc-triage', 'conflict-handler', 'copywriting', 'design-iteration-loop', 'design-prompt-builder', 'design-slop-check', 'design-system-prep', 'detail-page-copy', 'detail-page-image', 'devil-review', 'escalation-manager', 'feedback-loop', 'gemini-3-image-prompt', 'gpt-image-2-prompt', 'higgsfield-image', 'higgsfield-video', 'interview-coach', 'investor-relations', 'kb-article', 'landing-page', 'lead-triage', 'market-profile-engine', 'mcp-connector-setup', 'negotiation-1on1', 'newsletter', 'notebooklm-slide-prompt', 'people-operations', 'performance-report', 'product-detail', 'project', 'public-data', 'research-methodology', 'roadmap-manager', 'sbiz365-analyst', 'seo-audit', 'sns-content', 'startup-launchpad', 'story-project', 'tax-helper', 'ticket-triage', 'travel-planner', 'tutor-research', 'wellness-coach']
- agents kept 6: ['core-text-qa-coordinator(4/4)', 'data-analysis-coordinator(3/4)', 'finance-report-assembler(5/5)', 'hiring-coordinator(6/7)', 'legal-review-coordinator(7/7)', 'operations-coordinator(7/8)']
- agents dropped 20: ['business-plan-coordinator(8/12)', 'career-job-search-coordinator(2/6)', 'commerce-compliance-coordinator(1/4)', 'commerce-detail-page-builder(2/9)', 'commerce-growth-analyst(1/10)', 'commerce-launch-coordinator(2/14)', 'content-publishing-pipeline(2/7)', 'design-handoff-coordinator(0/5)', 'education-course-builder(2/6)', 'marketing-audit-coordinator(1/4)', 'marketing-campaign-coordinator(2/10)', 'media-production-pipeline(1/6)', 'product-ux-audit-coordinator(1/5)', 'productivity-planning-coordinator(2/6)', 'public-data-research-coordinator(1/5)', 'research-scout-coordinator(4/9)', 'sales-proposal-coordinator(2/3)', 'story-production-pipeline(2/13)', 'support-ticket-triage-batch(3/6)', 'wealth-roadmap-coordinator(1/7)']
- mcp kept: ['korean-law', 'kordoc'] | userConfig: ['KOREAN_LAW_OC']
- skills total: 67
- gates: PASS
- zip: sz.plugin (398 entries)
