---
name: risk-center
description: |
  UZ 리스크 센싱 통합 대시보드(단일 HTML · 5뷰 홈/운영리스크/WTO/보세창고/보고서 아카이브) 운영 — init(프로젝트 세팅·템플릿 배치) / update(주간 전수 스윕·갱신·검증 로그·델타 브리핑) / report(심층 보고서·아카이브 내장) / doctor(정합 점검). 트리거: "리스크 대시보드 프로젝트 세팅", "대시보드 업데이트해줘", "환율 리스크 보고서", "대시보드 점검해줘"
  EN: Single-file HTML risk-sensing dashboard operations — init / weekly update (full sweep, verification log, delta briefing) / deep-dive report with archive embedding / doctor. Triggers: "set up the risk dashboard project", "update the dashboard", "risk report on ...", "check the dashboard"
version: 2.1.0
---

# sz:risk-center — 리스크 센싱 통합 대시보드 운영 (리스크 매니지먼트)

C레벨 대상 UZ 리스크 센싱을 **단일 HTML 대시보드 1개**로 운영하는 표준 절차. 판정 엔진은 `sz:risk-radar`, 조사 규칙은 `sz:uz-research`, 공통 규칙(등급제·승인 게이트·언어)은 `sz:work`를 따른다.

## 언어 규칙
요청 언어(KO/EN/RU/UZ)로 대화. **대시보드 텍스트는 KO/EN 동등 품질 병기(HARD)**, 보고서는 KO 기본(요청 시 EN).

## 참조 (지연 로드 — 해당 모드에서만 읽기)
| 파일 | 내용 | 읽는 시점 |
|---|---|---|
| `references/data-schema.md` | KPIS·RISK_DATA·WTO_EVENTS·REPORTS·BW(SOURCES/EVIDENCE)·I18N 필드 정의 | update·report·개별 스킬 연동 |
| `references/weekly-sweep.md` | 전수 스윕 축 A~D·보조 검색어·검증·체크리스트·최근 3주 배지·i18n 규칙 | update |
| `references/report-format.md` | 심층 보고서 표준 목차·검증 로그 양식·아카이브 요약 내장 절차 | report |
| `references/dashboard-tech.md` | 셸·뷰 모듈·MODULES 플래그·CSS 스코프·Chart.js 폴백 | init·HTML 수정 |
| `references/research-depth.md` | 인용 4분류·접근 상한·심도 3모드·2단 분리 | 조사 전반 |
| `references/templates/AGENTS-risk-center.md.tmpl` | RM 프로젝트 AGENTS.md 프리셋 | init |
| `references/template/risk-center.template.html` | 데이터 비운 대시보드 템플릿(카테고리별 가상 샘플 1건) | init |

## 공통 HARD 규칙 (프로젝트 AGENTS.md가 덮어쓸 수 있음)
1. **금칙어·익명화**: 대시보드 파일명·내용에 법인 약어·'본사'·'당 법인' 금지, 자사="당사/현지 법인(LE)". 경쟁사 익명화 매핑은 프로젝트 AGENTS.md에서 지정(플러그인은 매핑을 갖지 않음).
2. **출처 무결성·발표일 기준**: 모든 항목에 실존 공개 URL + 1차 출처 공식 발표일(2차 매체가 늦게 보도해도 발표일, 출처명 "발표주체 (매체 보도)"). 접속일 사용·임의 URL 생성 금지.
3. **단일 HTML**: 메뉴 전환형 1파일. 파일 링크 금지(보고서는 요약 내장). 디자인 토큰은 `sz:design-system-library` 프리셋 `sz-corporate`와 동일 계열.
4. **버전·파일명**: `uz-risk-center_v{semver}_{YYYY-MM-DD}.html`, 갱신 시 patch 증가 + 파일명 날짜 갱신 + 우상단 표기 동기화, **구버전 보존**.
5. **보고서는 승인 후 제작**: 임의 선제작 금지.
6. **KO/EN 페어링**·**아카이브 요약 내장**·**SNAPSHOT_DATE 동기화**·**i18n 렌더링(innerHTML/textContent)** — 상세는 refs.
7. **갱신 후 한국어 델타 브리핑 6항목**(`sz:risk-radar`).

## 모드

### init — 리스크 대시보드 프로젝트 세팅
1. 인터뷰 4문항: ① 대상 법인·시장(기본 UZ) ② 금칙어·익명화 매핑 ③ 활성 모듈(`MODULES`: ops·wto·bw·archive, 기본 전부 on) ④ 갱신 주기(기본 주간·월요일)
2. 계획 제시 → **승인 후** 생성: 폴더 `01_대시보드/`·`02_보고서/`·`03_검증로그/`·`inputs/` + 템플릿 HTML을 `01_대시보드/uz-risk-center_v1.0.0_{오늘}.html`로 배치(MODULES 반영) + `AGENTS.md`(프리셋 치환) + `CLAUDE.md`(`@AGENTS.md` 포인터, 빈 파일 금지) + `.sz/refs/`에 refs 5종 사본
3. 샘플 항목(카테고리별 1건, `SAMPLE-` id) 유지 여부 확인 — 첫 update에서 자동 제거
4. 기존 대시보드 폴더를 가져오는 경우(이전): 파일 복사 후 `sz:work doctor`로 `gil:`→`sz:`·`.sz/`→`.sz/` 이관, 템플릿 재생성 금지

### update — 주간 갱신
착수 전: 예상 소요(◐ 표준 20~40분) 1회 고지. 절차(`weekly-sweep.md`):
1. `_반영준비_*` 문서 확인 → 2. **전수 스윕 축 A~D**(날짜 한정 쿼리·보조 검색어·1차 공표 채널 직접 확인, 부분 조사 금지) → 3. 카테고리 큐레이션·`sz:risk-radar` 등급 판정 → 4. **새 파일명**으로 HTML 갱신: `RISK_DATA`·`KPIS`·`WTO_EVENTS`·BW 데이터·`SNAPSHOT_DATE`·각 뷰 스냅샷 날짜·우상단 버전 → 5. 신규·변경 URL **개별 WebFetch 전수검증**(실패=잠정 강등) → 6. `sz:validate-data` QA + 치환 오염 검증(헤더·타 뷰 날짜 오염) + 렌더링 검증(항목 수·EN 전환·배지) → 7. 검증 로그 `03_검증로그/` 발행 → 8. **델타 브리핑 6항목**

### report — 주제별 심층 보고서
1. **승인 확인**(주제·심도·납기) → 2. `sz:uz-research`(2단 분리: 조사 확정 후 문서화) → 3. `sz:docx-generator`로 표준 목차(`report-format.md`) 작성 → 4. 등급별 검수(◆최종본이면 `sz:work` QA 체인) → 5. `02_보고서/` 저장 → 6. **동시에** 대시보드 `window.REPORTS` 요약 내장 + 아카이브 표 행 + 홈 아카이브 건수 갱신(파일 링크 금지) → 7. 검증 로그에 반영 기록

### doctor — 정합 점검
`SNAPSHOT_DATE` = 최신 갱신 기준일 · 파일명↔우상단 버전·날짜 일치 · 각 뷰 스냅샷 날짜 일치 · `REPORTS` 건수 = 홈 카드 건수 = `02_보고서/` 파일 수 · i18n: HTML 태그 포함 문자열은 `data-i18n-html`/innerHTML · 금칙어 스캔 · 항목 `last`/`sources[].date` 형식(YYYY-MM-DD) · CDN 차단 시 CSS 폴백 동작 · 샘플(`SAMPLE-`) 잔존 여부. 결과는 표로, 수리는 승인 후.

## 체인
`sz:uz-research`(조사) · `sz:risk-radar`(판정·델타) · `sz:validate-data`(QA) · `sz:docx-generator`/`sz:pptx-designer`/`sz:html-slide`(산출) · `sz:trade-logistics`(보세창고 축 제도 참조) · `sz:design-system-library`(디자인 토큰) · `sz:wiki`(risk-mgmt 도메인 배경 지식 우선 참조, 갱신 교훈은 compile 제안)

## English Summary
Operate a single-file HTML risk-sensing dashboard (Home / Operational Risk register / WTO / Bonded Warehouse / Report Archive). **init** scaffolds folders, the data-stripped template (per-category sample items), an RM-specific AGENTS.md and a CLAUDE.md pointer after approval. **update** runs the full weekly sweep (axes A–D, date-bounded queries, auxiliary RU/EN terms, primary-channel checks), regrades items via `sz:risk-radar`, writes a new versioned HTML (RISK_DATA, KPIS, WTO_EVENTS, SNAPSHOT_DATE), verifies every new URL, runs QA, publishes a verification log and a 6-part delta briefing. **report** produces an approved deep-dive DOCX in the standard outline and embeds its summary into `window.REPORTS` (no file links). **doctor** checks date/version/i18n/archive consistency. Dashboard text is always KO/EN paired; the company is referred to as "the local entity (LE)".
