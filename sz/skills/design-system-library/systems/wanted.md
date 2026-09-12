# wanted — Wanted Design System (WDS)

한국 채용 플랫폼 원티드(Wanted Lab)의 디자인 시스템. 클린한 화이트 캔버스 + 선명한 블루 프라이머리, Pretendard 타이포. 신뢰감 있는 한국형 비즈니스 문서에 적합.

> 출처: Wanted Design System (Figma Community, Beta) — 사용자 제공 캡처 기반.
> ⚠️ 색상 hex는 캡처 실측 **근사치**(공식 토큰 JSON 미보유). 공식 값 확보 시 갱신할 것.

## 색 (semantic → 근사 hex)

| 토큰 | 근사값 | 용도 |
|---|---|---|
| primary-normal (blue-60) | `#2A6FF3` | 버튼·링크·강조 |
| primary-strong (blue-55) | `#1F5EE0` | hover·강조 진함 |
| primary-heavy (blue-50) | `#164FC9` | pressed·헤더 강조 |
| static-white | `#FFFFFF` | 캔버스 |
| static-black | `#000000` | 순수 검정 |
| label-normal (coolNeutral-10) | `#171719` | 본문 텍스트 |
| label-strong | `#000000` | 제목 |
| label-neutral (coolNeutral-40) | `#5A5C63` | 보조 텍스트 |
| label-alternative (coolNeutral-60) | `#989BA2` | 캡션·비활성 |
| background-alternative | `#F7F7F8` | 섹션 배경·카드 |
| line-normal | `#E1E2E4` | 구분선·테이블 보더 |
| accent-orange | `#FF6B00` | 포인트(제한적) |

## 타이포그래피

- **글꼴: Pretendard** (원본은 Pretendard JP — 한·영·일 지원). 문서 폴백: Pretendard → 맑은 고딕/Apple SD Gothic Neo → sans-serif
- 위계: 7단계·18 하위 위계. 문서용 매핑(캡처 스케일 기반 확대):

| 위계 | 크기/행간 | 웨이트 |
|---|---|---|
| Display(표지 제목) | 36/46 | 700 |
| Title(장 제목) | 26/36 | 700 |
| Heading(절 제목) | 20/28 | 600 |
| Headline | 18/26 | 600 |
| Body 1 | 16/26 (reading) · 16/24 (normal) | 400 |
| Body 2 | 15/24 | 400 |
| Caption/Label | 13/18 | 400·500 |

## 무드·레이아웃 규칙

- 화이트 캔버스, 섹션 구분은 얇은 라인(#E1E2E4) 또는 연회색 블록(#F7F7F8)
- 라운드 12~16px 카드, 그림자 최소화(레이어드 대신 여백으로 위계)
- 강조는 블루 단색으로 절제 — 다색 사용 금지(포인트 오렌지는 배지·경고 정도)
- 표: 헤더 연회색 배경 + 라인 보더, 지브라 스트라이프 없음
- 좌측 정렬 기본, 제목-본문 사이 넉넉한 수직 여백

## 문서 형식별 번역 규칙

| 형식 | 적용 |
|---|---|
| HTML(report/slide) | 위 토큰을 CSS 변수/Tailwind config로 직접 적용, Pretendard CDN |
| DOCX | 제목=Pretendard(또는 맑은 고딕) 700 + label-strong, 본문 Body1, 강조·링크 primary-normal, 표 헤더 background-alternative |
| PPTX | 타이틀 슬라이드 Display, 본문 슬라이드 Title/Body, 액센트 도형 primary-normal, 배경 white |
| PDF | HTML 규칙 준용 후 렌더 |
