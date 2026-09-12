# 심층 보고서 규격 + 검증 로그 양식 + 아카이브 내장 (정본 — report 모드에서 지연 로드)

## 1. 보고서 표준 목차 (DOCX)
표지 → **Executive Summary**(결론·등급·요청 결정 1페이지) → **Key Findings**(번호 목록, 각 항목에 출처·발표일) → 상세 분석(사실 → 함의, [추정] 태그) → **시나리오**(Best / Base / Worst — 트리거·확률·손익 영향·대응) → **재무영향**(KRW·USD·UZS 병기, 산식 명시) → **Action**(우선순위·담당 부서·납기·KPI) → 부록 A 데이터 → **부록 B 출처 검증 로그**(인용 4분류 표) + 참고문헌(APA·클릭형 하이퍼링크).

유형 태그: `urgent`(긴급 리스크분석, 5~8p) · `regular`(정기 모니터링, 8~12p) · `deep`(종합 리포트, 15p+). 파일명: `[YYYY-MM-DD] UZ {주제} {유형}.docx` 또는 프로젝트 관행.

## 2. 산출 절차 (HARD)
1. **승인 확인**: 주제·유형·심도(⚡/◐/◆)·납기. 임의 선제작 금지.
2. 조사 확정(`sz:uz-research`) → 사용자 확인 → 문서화(2단 분리).
3. `sz:docx-generator`로 작성. ◆최종본이면 `sz:work` QA 체인(ai-slop-reviewer → korean-spell-check → humanize-korean) + 수치·환산 재검산.
4. `02_보고서/` 저장 → **동시에** 아카이브 내장(§4) → 검증 로그에 기록.

## 3. 검증 로그 양식 (`03_검증로그/{대시보드명}_{주간갱신|보고서}_{YYYY-MM-DD}_verification.md`)
```
# 검증 로그 — {갱신 유형} {YYYY-MM-DD} (v{semver})
## 스냅샷 구간: {직전} → {이번}
## 축별 스윕 기록
| 축 | 쿼리(요지) | 결과(신규/변경/저변동) | 근거 URL |
## 신규·변경 항목 검증
| 카테고리 | 항목 | 출처 | 발표일 | 검증등급(VERIFIED/SECONDARY/NOT_FOUND/MISMATCH) | 비고 |
## KPI 대조 (cbu.uz·stat.uz 1차 페이지)
## 등급 변화 | 잠정 강등 항목 | 원문 재확인 필요 항목
## 대시보드 반영 확인: 파일명·버전·SNAPSHOT_DATE·뷰 날짜·REPORTS 건수 ✔/✘
```

## 4. 아카이브 요약 내장 (HARD · 배포용 단일 파일 원칙)
새 보고서마다 **동시에** 대시보드 아카이브에 반영. 파일 링크를 쓰지 않는다 — HTML 하나만 배포해도 전부 동작해야 한다.
1. `window.REPORTS`에 항목 추가(`data-schema.md` §4): `t`·`ko/en` 제목·`date`·`dko`(요약 2~3문장 → 핵심 진단 → 우선 권고 `gsp-ol`)·`den`. Executive Summary·Key Findings에서 추출.
2. 아카이브 표에 행 추가: `<tr data-rep="rN" style="cursor:pointer">` + 작성일·유형 태그·제목(`span.rep-t`, `data-ko/data-en`).
3. 원문 안내는 패널 자동 표기("`02_보고서/` 보관 · 리스크관리팀 요청") — 별도 작업 불요.
4. 홈 카드 아카이브 건수 갱신.
