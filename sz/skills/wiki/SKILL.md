---
name: wiki
description: |
  LLM-Wiki 중앙 지식 저장소 운영 — compile(현재 대화의 재사용 지식을 frontmatter 페이지로 증류해 _inbox에 저장) / ingest(인박스 배치·승격·중복·링크 제안 → 승인 후 실행) / lint(frontmatter·깨진 링크·고아·INDEX 점검) / init(위키 스캐폴드). 트리거: "위키로 컴파일", "이 대화 위키에 저장해줘", "인제스트 브리핑", "위키 정리", "위키 린트", "위키 세팅해줘"
  EN: Personal LLM-Wiki operations — compile chat knowledge into frontmatter pages (inbox), ingest briefing (placement/promotion proposals, approval-gated), lint, init scaffold. Triggers: "compile to wiki", "ingest briefing", "wiki lint", "set up my wiki"
version: 2.1.0
---

# sz:wiki — LLM-Wiki 중앙 지식 저장소 (개인 위키)

작업장(프로젝트 폴더)과 위키를 분리한다: **프로젝트 폴더는 어지러워도 되고, 위키는 깨끗해야 한다.** 위키에는 재사용할 검증 지식만 두고, 쌓는 행위(compile, 10초)와 배치 판단(ingest, 주 1회)을 분리해 기록 마찰을 없앤다. 운영 헌법: `references/operations.md`.

## 언어 규칙
요청 언어(KO/EN/RU/UZ)로 대화. 위키 페이지 본문은 사용자 주 언어(기본 KO). 위키 페이지는 ⚡초안으로 충분 — AI가 읽는 지식이지 발행물이 아니므로 QA 체인을 태우지 않는다.

## 위키 위치 찾기 (HARD)
1. 프로젝트 `AGENTS.md`의 위키 배선 줄(예: "`../_Wiki/wiki/<도메인>/INDEX.md` 우선 참조")에서 경로를 읽는다.
2. 없으면 프로젝트 폴더의 형제 폴더 `../_Wiki/`를 확인한다.
3. 둘 다 없으면 **임의 생성하지 않고** `init` 모드를 제안한다.

## 모드

### compile — 대화 → 위키 페이지 (`_inbox/` 전용)
1. **추출**: 대화에서 재사용 가치가 있는 지식 단위를 식별 — "다른 프로젝트에서도 쓰는가? 한 달 뒤에도 유효한가?" 일회성 산출물·잡담·작업 지시 자체는 제외.
2. **주제 분리**: 한 파일 = 한 주제(보통 1~3개).
3. **증류**: 대화 복사가 아니라 **결론·근거·조건을 재구성**. 대화체 흔적 제거, 서술형 30~80줄.
4. **frontmatter**(`references/page-template.md`): `title · maturity: idea(기본) · domain(추정, 확신 없으면 미정) · updated · source · links`.
5. 파일명 `_inbox/YYYYMMDD_주제.md`. "로그도" 요청 시 `_inbox/logs/YYYYMMDD_주제_log.md`에 시간순 요지 저장.
6. **보고**: 생성 파일·1줄 요약·추정 도메인 표. 배치·승격 제안은 하지 않는다(ingest 몫).
금지: 민감정보(신분증·계좌·비밀번호·건강) 파일화 금지(제외 후 고지) · 기존 위키 페이지 직접 수정 금지 · 대화 전문 복사 금지.

### ingest — 인제스트 브리핑 (승인형 HARD)
1. `_inbox` 신규 파일 목록화 → 2. 파일별 배치 제안(도메인·기존 페이지 병합 여부 — **중복 페이지 금지, 있으면 갱신**) → 3. 승격 후보(2회+ 재등장=concept, 실행 검증=process, 2개+ 프로젝트 재사용=framework) → 4. 중복·`links` 연결 제안 → 5. **제안 표(파일 | 제안 | 근거) 제시 → 사용자 승인 → 실행 → 도메인 INDEX.md·`00_INDEX.md` 갱신**.
분석·제안은 AI, **결정은 사람.** 무승인 자동 이동·병합·승격 금지. 삭제는 제안만 하고 사용자가 명시할 때만 실행. 배치 시 `_inbox` 파일명의 날짜를 제거해 주제명으로 개명.

### lint — 월간 점검
frontmatter 누락·필드 불량 · 깨진 `[[링크]]` · 어디서도 참조되지 않는 고아 파일 · INDEX와 실제 파일 불일치 · `_inbox` 30일+ 방치 파일 → 보고 표. 수리는 승인 후.

### init — 위키 스캐폴드 (승인 후)
인터뷰 2문항(① 도메인 목록 — 기본: uzbekistan·accounting·risk-mgmt·legal·hr·sales-support·logistics·ai-workflow, ② 조직 정체성 폴더 사용 여부) → 계획 제시 → 승인 → 생성: `_Wiki/AGENTS.md`(`references/templates/AGENTS-wiki.md.tmpl`) + `CLAUDE.md`(`@AGENTS.md` 포인터) + `OPERATIONS.md`(`references/operations.md` 사본) + `wiki/00_INDEX.md` + 도메인별 `INDEX.md` + `wiki/_inbox/logs/` + (선택) `brand/`·`contents/strategy/`·`contents/ops/`.

## 조회 규약 ("~에 대해 위키 기준으로")
해당 도메인 `INDEX.md` → 관련 페이지를 읽고 **내장 지식보다 우선** 근거로 답한다. 위키와 프로젝트 파일이 충돌하면 최신 `updated` 우선, 불확실하면 사용자에게 확인. 도메인이 모호하면 `wiki/00_INDEX.md`를 먼저 읽는다.

## 체인
- `sz:work` 프로젝트 세팅: 인터뷰 "위키 배선" 문항 → AGENTS.md에 참조 1줄 삽입. `sz:risk-center` 프리셋은 `risk-mgmt` 도메인 배선 기본 포함.
- 작업 중 재사용 지식이 확정되면 어떤 스킬이든 사용자에게 "위키로 컴파일" 여부를 **1줄로 제안**(자동 실행 금지).
- 조사 결과의 출처 등급(`sz:uz-research` 4분류)은 위키 페이지 본문에 그대로 보존한다.

## English Summary
A personal LLM-Wiki (Karpathy-style) kept separate from working folders. **compile** distills reusable knowledge from the current chat into frontmatter pages under `wiki/_inbox/` (never edits existing pages, never stores sensitive data). **ingest** proposes placement, merges, promotions (idea → concept → process → framework) and links as a table and executes only after approval. **lint** reports missing frontmatter, broken `[[links]]`, orphans, INDEX drift and stale inbox files. **init** scaffolds `_Wiki/` with AGENTS.md pointer pair, OPERATIONS.md and domain INDEX files after approval. Other skills read the wiki first when asked "based on the wiki".
