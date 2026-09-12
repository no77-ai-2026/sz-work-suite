# 대시보드 데이터 스키마 정본 (SSOT) — 개별 스킬이 데이터를 산출할 때 이 형식을 따른다

모든 문자열은 KO/EN 쌍. 날짜는 `YYYY-MM-DD`. HTML 태그(`<b>` 등)를 포함하는 문자열은 렌더러가 innerHTML로 주입하므로 안전한 태그(b·i·br·a)만 사용.

## 1. KPIS — 홈 KPI 스트립 (배열)
```js
{ id:"uzs_usd",                      // 고유 키(snake_case)
  label:{ko:"UZS / USD", en:"UZS / USD"},
  val:"11,820",                      // 표시값(문자열)
  delta:"CBU 고시 9/2 적용 · …",     // 변동 요약 1줄(KO, 짧게)
  trend:"flat",                      // "up" | "down" | "flat"
  note:{ko:"…<b>강조</b>…", en:"…"}, // 해설(HTML 허용)
  src:{name:{ko:"CBU 공시 (YYYY-MM-DD)", en:"…"}, url:"https://…"} }
```
기본 6종: `uzs_usd` · `uzs_krw` · `cb_rate` · `inflation` · `gdp` · `sovereign`. 추가 시 id 충돌 금지.

## 2. RISK_DATA — 운영 리스크 레지스터 (카테고리 배열 → items)
```js
{ id:"finance", no:"③",              // 레지스터 10카테고리 id·번호 (sz:risk-radar 정본)
  name:{ko:"Finance", en:"Finance"},
  items:[
    { no:1,                          // 카테고리 내 일련번호(정수)
      status:"watch",                // "crisis" | "watch" | "normal"
      last:"2026-08-14",             // 최신 1차 발표일 — 최근 3주 배지 판정에 사용
      title:{ko:"…", en:"…"},
      summary:{ko:"2~3문장 요지", en:"…"},
      detail:{ko:"상세 분석(사실→함의, [추정] 태그)", en:"…"},
      response:{ko:"대응·모니터링 계획", en:"…"},
      sources:[ {title:{ko:"발표주체 (매체 보도) (YYYY-MM-DD)", en:"…"}, url:"https://…", date:"YYYY-MM-DD"} ],
      decisions:[]                   // 의사결정 이력 [{date, ko, en}] — 등급 변경·해제 시 1줄
    } ] }
```
카테고리 id 고정값: `comm`·`compete`·`finance`·`geo`·`hc`·`legal`·`ops`·`product`·`sec`·`supply`. 샘플 항목은 `title.ko`가 `SAMPLE-`로 시작하며 첫 update에서 제거.

## 3. WTO_EVENTS — 홈 타임라인 WTO 이벤트 (셸, 배열)
```js
{ date:"2026-07-27", ko:"제13차 Working Party 개최 …", en:"13th Working Party …", url:"https://…" }
```
WTO 뷰 본문은 `#view-wto` 정적 마크업(`data-ko`/`data-en`) — 갱신 시 이벤트 배열과 정적 마크업 둘 다 손본다.

## 4. window.REPORTS — 보고서 아카이브 요약 내장 (객체, 키 rN)
```js
r12:{ t:"urgent",                    // "urgent" | "regular" | "deep"
      ko:"제목", en:"Title", date:"YYYY-MM-DD",
      dko:"<p>요약 2~3문장</p><div class=\"gsp-lbl\">핵심 진단</div><div class=\"gsp-detail\"><p>· …</p></div><div class=\"gsp-lbl\">우선 권고</div><ol class=\"gsp-ol\"><li>…</li></ol>",
      den:"<p>English summary …</p>" }
```
아카이브 표 행: `<tr data-rep="r12" style="cursor:pointer">` + 작성일·유형 태그·제목(`span.rep-t`, `data-ko`/`data-en`). **파일 링크(`<a href>`) 금지.** 홈 카드 "아카이브 N건" 동기화.

## 5. 보세창고 뷰(BW) — `SOURCES`(객체)·`EVIDENCE`(배열)
```js
SOURCES.key = { tag:"tag-policy|tag-comp|tag-market|tag-news",
  type:{ko,en}, title:{ko,en}, meta:{ko:"출처 · 날짜", en:"…"},
  quote:{ko,en},                     // 선택
  detail:{ko:"<p>…</p>", en:"<p>…</p>"}, url:"https://…", btnLabel:{ko:"원문", en:"Open"} }
EVIDENCE[] = { cat:"policy|market|comp|news", label:{ko,en}, title:{ko,en}, date:"YYYY-MM-DD",
  conf:"●●●●○",                       // 5점 신뢰도
  src:"key" }                        // SOURCES 키 참조
```
BW I18N 콘텐츠 키(auditNote·rec1~3·stat*·footer)는 주간 갱신 시 함께 갱신되는 **분석 문구**다 — 라벨 키와 구분해 관리.

## 6. 셸 상수
`SNAPSHOT_DATE`(최근 3주 배지 기준일, 갱신 시 필수 동기화) · `RECENT_DAYS`(21) · `MODULES`(뷰 on/off) · 우상단 버전·날짜 · 각 뷰 스냅샷 날짜.

## 개별 스킬 연동 규약
- 대시보드에 넣을 항목을 만드는 스킬은 §2 항목 객체(JSON) 그대로 산출하고 카테고리 id를 명시한다.
- 등급(`status`)은 `sz:risk-radar` 3요소 판정을 거친 값만 사용.
- URL은 실존 확인된 것만, `date`는 1차 발표일. 미확인이면 항목에 넣지 말고 "원문 재확인 필요" 목록으로 보고.
