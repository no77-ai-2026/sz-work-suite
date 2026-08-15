---
name: creative-wizard
description: |
  [한·UZ 듀얼 · gil-creative 코디네이터] 글로벌 광고 크리에이티브 마법사의 전체 흐름을 오케스트레이션하는 진입점입니다. 하나의 브리프에서 상세페이지·카드뉴스·포스터·인쇄물을 멀티 포맷·멀티 마켓으로 제작합니다. 브리프 인터뷰 → 시장 프로필 → 자료·후기 분석 → 히어로 톤 앵커링(승인 게이트) → 크리에이티브 설계 → 이미지 → 포맷 빌더 → QA 순으로 하위 스킬을 라우팅합니다.
  다음과 같은 요청 시 사용하세요:
  - "광고 크리에이티브 마법사 시작"
  - "상세페이지/카드뉴스/포스터 만들어줘 (제품·시장 있음)"
  - "우즈벡 시장용 광고 크리에이티브 통째로"
  - "브리프 받아서 멀티 포맷으로 만들어줘"
  - "reklama kreativ sehrgari" (광고 크리에이티브 마법사, UZ)
  텍스트 지능(카피·구성·현지화·후기분석)은 Claude가 직접 수행하고, 이미지 생성만 image-bridge(미포함)(OpenAI/Gemini BYOK)로 붙입니다. 설계는 sz:creative-architect, 현지화는 sz:market-profile-engine, 자료는 sz:material-analyzer로 위임합니다.
user-invocable: true
version: 1.1.1
---

# 크리에이티브 마법사 (Creative Wizard) — 코디네이터

> **역할** 글로벌 광고 크리에이티브 마법사의 오케스트레이터. 사용자와 대화하며 브리프를 모으고, 하위 스킬을 순서대로 호출해 멀티 포맷 산출까지 끌고 간다.
> **원칙** 텍스트=Claude 내재, 이미지=외부 API(BYOK).
> **한·UZ 듀얼** 한국 표준 + UZ/CIS. 시장 고정 없이 확장.

---

## 0. 역할 분담 (핵심 원칙)
- **텍스트 두뇌 = Claude(내재)**: 카피·구성·후기분석·현지화. 외부 텍스트 API 없음.
- **이미지만 외부**: OpenAI gpt-image / Google Gemini image, BYOK (image-bridge(미포함)).
- **기본 산출 = Markdown(.md)**. 무거운 포맷은 사용자 명시 요청 시에만.

---

## 1. 워크플로우 (데이터 플로우 10단계)

굵은 단계는 Claude 직접 수행, ⑦만 외부 API.

| # | 단계 | 담당 |
|---|---|---|
| 1 | **브리프 인터뷰** (§2) | 이 스킬 (Claude) |
| 2 | **시장 프로필 로드/생성** | `sz:market-profile-engine` |
| 3 | **자료·후기 분석 + 벤치마크 흐름** | `sz:material-analyzer` (+ `sz:commerce-voc-triage`) |
| 4 | **히어로 톤 앵커링** (승인 게이트) | `sz:creative-architect` §3 |
| 5 | **크리에이티브 설계**(앵커 상속·8단계·10종) | `sz:creative-architect` |
| 6 | **이미지 프롬프트 생성** | `sz:creative-architect` (+ `sz:gpt-image-2-prompt`·`sz:gemini-3-image-prompt`) |
| 7 | 이미지 생성 (외부, BYOK) | `image-bridge(미포함)` |
| 8 | **포맷 빌더** | 포맷별(§4) |
| 9 | **QA** (슬롭·윤문·규제) | `sz:ai-slop-reviewer`→`sz:humanize-korean`→규제 |
| 10 | **전달** | 카테고리 폴더 저장·링크 |

---

## 2. 브리프 인터뷰 (수집 항목)

사용자에게 아래를 대화로 수집한다. 이미 주어진 값은 건너뛰고, 부족한 것만 묻는다(한 번에 하나씩).

| 범주 | 항목 |
|---|---|
| product | 상품명·카테고리·USP·가격·자료(사진·스펙) |
| market | 국가·주언어/병기언어·산업 |
| channel | Uzum·Yandex·OLX·Telegram·쿠팡·스마트스토어 등 |
| formats | 상세페이지 / 카드뉴스 / 포스터·광고 / 인쇄물 (복수 선택) |
| tone | 무드 프리셋(프리미엄·모던·테크·미니멀·팝아트·인스타감성·레트로) |
| reviews | 후기 파일(엑셀·텍스트) 첨부 여부 |
| benchmarks | 기존 상세/경쟁사 자료 첨부 여부 |
| brandkit | 브랜드킷(로고·색·서체) 유무 → 없으면 sz:design-system-prep로 소싱 |

> 브리프 스키마: `product·market·channel·formats·tone·reviews·benchmarks`.

---

## 3. 승인 게이트 (히어로 우선)

- 전체를 한 번에 뽑지 않는다. **히어로 1장 먼저** 확정 → 사용자 승인 → 나머지 일괄.
- 승인 전에는 image-bridge(미포함) 대량 호출을 하지 않는다(비용·일관성 보호).
- 승인 후 앵커(톤·컬러·구도)를 상속해 전 섹션·전 포맷 생성.

---

## 4. 포맷별 빌더 라우팅

| 포맷 | 빌더 (조합) |
|---|---|
| 상세페이지 | `sz:detail-page-planner` → `sz:detail-page-copy` → `sz:detail-page-image` / 코드형은 `sz:landing-page`·`sz:product-detail` |
| 카드뉴스 | `sz:card-news` |
| 포스터/광고 | `sz:poster-ad-builder` (+ `image-bridge(미포함)`) |
| 인쇄물 | `sz:print-creative-builder` (+ `sz:pdf-writer`) |

> 하나의 CreativeSpec(sz:creative-architect 산출)을 각 빌더가 포맷 특성에 맞게 압축·확장한다.

---

## 5. QA 파이프라인 (종료 필수)

| 단계 | 도구 |
|---|---|
| AI 슬롭 제거 → 언어별 윤문 | `sz:ai-slop-reviewer` → `sz:humanize-korean` |
| 한국어 맞춤법 | `sz:korean-spell-check` |
| 광고 규제(과장·최상급·의학효능·표시의무) | `commerce-marketing-compliance-kr(미포함)` + 시장 프로필 규제 항목 |
| 이미지 검수(일관성·가독성·금기색) | Claude 육안 |

> 원칙: 코드·JSON·순수 표를 제외한 모든 텍스트 산출물은 슬롭 검수로 종료.

---

## 6. 전체 체이닝 맵

```
creative-wizard(코디네이터)
├─ market-profile-engine ──(시장 오버레이)──┐
├─ material-analyzer ──(자료·벤치마크·후기)─┤
│    └─ commerce-voc-triage (후기)          │
├─ design-system-prep ──(브랜드킷 토큰)─────┤
├─ creative-architect ◄────────────────────┘  (설계: 8단계·방법론 10종·CreativeSpec)
│    └─ 승인 게이트(히어로)
├─ image-bridge (OpenAI/Gemini BYOK) ◄ gpt-image-2-prompt / gemini-3-image-prompt
├─ 포맷 빌더: detail-page-* / card-news / poster-ad-builder / print-creative-builder
└─ QA: ai-slop-reviewer → humanize-korean → korean-spell-check → commerce-marketing-compliance-kr
```

---

## 7. 워크플로우 예시 (우즈벡 뷰티 수분크림 상세페이지)
1. 브리프: 수분크림 / 우즈벡(RU+UZ) / Uzum / 상세페이지 / 후기+벤치마크 첨부
2. `sz:market-profile-engine` 로드: 정품·인증 신뢰, Payme·Click·Uzum Nasiya, BTS
3. `sz:material-analyzer`: 후기에서 '보습 지속·저자극' 소구 추출 + 벤치마크 흐름 파악
4. `sz:creative-architect`: 히어로 앵커링(승인) → 8단계 + RU/UZ 카피 + 레이아웃, renderMode=overlay
5. `image-bridge(미포함)`: 1080 세로 배경만 생성(비라틴 후조판)
6. 빌더: 세로 합성 상세 + 편집 HTML(카피 오버레이)
7. QA: RU/UZ 슬롭·윤문 + 광고 규제
8. `.md` 우선 저장 → 링크 공유

> 실행 옵션·BYOK·UZ 세부는 `references/uz-creative-wizard.md` 참조.

---

## 8. 2단계 진화
- **Phase 1** (현재): Cowork 스킬 묶음. 상세페이지 우선 → 4포맷 확장.
- **Phase 2**: 웹서비스(Next.js+Vercel, 서버 프록시, 계정·결제). 프롬프트·규칙을 이전.
