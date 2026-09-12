# 대시보드 기술 메모 (정본 — init·HTML 수정 시 지연 로드)

## 구조
- **셸**(메뉴·홈·테마·언어 토글) + **뷰 모듈** 4종: `#view-ops`(운영 리스크, `window.OPS` IIFE: `KPIS`·`RISK_DATA`·`SNAPSHOT_DATE`·`RECENT_DAYS`·`isRecent()`·`latestSourceDate()`) · `#view-wto`(정적 마크업 `data-ko`/`data-en`) · `#view-bw`(보세창고, `window.BW` IIFE: `I18N`·`SOURCES`·`EVIDENCE`·시나리오·게이트) · `#view-reports`(아카이브, `window.REPORTS`).
- 홈 타임라인의 WTO 이벤트는 셸 `WTO_EVENTS` 배열.
- **`MODULES` 플래그**(셸 최상단): `{ops:1, wto:1, bw:1, archive:1}` — 0이면 해당 메뉴·뷰 숨김. 코드 삭제 없이 구성 변경. init 인터뷰 ③에서 결정.
- 각 뷰 CSS는 `#view-*`로 스코프. **전역 토큰만 수정하면 전체 테마 변경**.

## 디자인 토큰
Wanted Design System 계열 — 기본 `#3366FF`·Pretendard·라이트 기본/다크 토글. `sz:design-system-library` 프리셋 `sz-corporate`와 동일 값을 유지해 HTML 보고서·슬라이드와 룩을 통일.

## 외부 의존
- Chart.js CDN 로드, **오프라인·CDN 차단 시 CSS 막대 폴백 자동 동작**(doctor 점검 항목).
- 폰트 CDN 실패 시 시스템 폰트 폴백.

## 배포 원칙
- 단일 HTML. 보고서는 요약 내장(`window.REPORTS`), 파일 링크 금지 → 파일 하나만 보내도 전부 동작.
- 대시보드 파일은 `01_대시보드/` 안에 두고 이동하지 않는다(과거 상대경로 안내 문구 호환).
- 갱신마다 **새 파일명**(patch·날짜)으로 저장, 구버전 보존.

## i18n
- `LANG` 토글(ko/en). 라벨은 `data-i18n` → textContent, HTML 포함 문자열은 `data-i18n-html` → innerHTML(렌더러 예외 키: `latest_signal_val` 등).
- 데이터 객체의 `{ko, en}` 쌍은 렌더러가 현재 언어로 선택.

## 수정 시 주의
- 날짜·버전 일괄 치환은 뷰별로 범위를 한정(셸 헤더·타 뷰 오염 방지) → 치환 후 diff 검증.
- `RISK_DATA` 카테고리 `id`·`no`는 고정(레지스터 10분류). 항목 `no`는 카테고리 내 연속.
- 새 i18n 키 추가 시 ko/en 둘 다 등록(누락 시 영어 전환에서 공백).
