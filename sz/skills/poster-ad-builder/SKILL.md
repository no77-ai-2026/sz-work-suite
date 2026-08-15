---
name: poster-ad-builder
description: |
  [한·UZ 듀얼 · gil-creative] 크리에이티브 설계(CreativeSpec)를 단일 광고 비주얼(포스터·SNS 광고·배너)로 조립하는 포맷 빌더입니다. 감정 여정에서 핵심 단계(히어로·특장점·오퍼·확신)만 1컷으로 압축하고, 1:1·4:5·9:16 등 채널 규격에 맞춰 배경 이미지 + 후조판 카피 레이어를 구성합니다.
  다음과 같은 요청 시 사용하세요:
  - "포스터 만들어줘"
  - "인스타 광고 비주얼 1컷"
  - "9:16 스토리 광고 만들어줘"
  - "배너 광고 시안"
  - "reklama afishasi" (광고 포스터, UZ)
  sz:creative-architect 설계를 입력으로 받아 image-bridge(미포함)로 배경을 렌더하고, 카피 오버레이 레이아웃을 산출합니다. 카드뉴스는 sz:card-news, 상세페이지는 sz:detail-page-image로 갈라집니다.
user-invocable: true
version: 1.1.1
---

# 포스터/광고 빌더 (Poster & Ad Builder)

> **역할** CreativeSpec을 **단일 비주얼 1컷**으로 압축·조립한다. 포스터·SNS 광고·배너 등.

---

## 1. 입력
- sz:creative-architect의 CreativeSpec(섹션·카피·renderMode·imgPrompt).
- 브랜드킷 토큰(sz:design-system-prep), 프리셋(무드), 시장 프로필(sz:market-profile-engine).

## 2. 압축 규칙
- 감정 여정 8단계 중 **①히어로 · ④특장점 1개 · ⑥오퍼 · ⑧확신** 을 1컷 위계로 압축.
- 위계: 가장 큰 약속(히어로 헤드라인) → 핵심 혜택 1줄 → CTA/오퍼 배지.
- 반복 금지·베네핏 헤드라인·기능→변화 번역 규칙 유지(방법론 #3·#4·#5).

## 3. 캔버스 규격 (RGB)

| 용도 | 비율 | 픽셀 |
|---|---|---|
| 정사각(피드) | 1:1 | 1080×1080 |
| 세로(피드) | 4:5 | 1080×1350 |
| 스토리/릴스 | 9:16 | 1080×1920 |
| 가로 배너 | 16:9 | 1920×1080 |

## 4. 조립 (통이미지 vs 후조판)
- **flat**: 라틴·짧은 카피 → image-bridge(미포함) `--mode flat`로 카피 포함 생성.
- **overlay**(CIS 기본): image-bridge(미포함) `--mode overlay`로 배경만 생성 → 카피/배지/아이콘을 HTML/디자인 레이어로 후조판.
- 산출: 배경 PNG + 카피 오버레이 스펙(위치·서체 위계·색=브랜드킷 토큰) + (선택) 편집 HTML.

## 5. 산출물
- 기본 `.md`(레이아웃 스펙 + 카피) + 배경 이미지. 편집 HTML은 요청 시.
- 파일명 `[포스터]_[제품·주제]_[YYYYMMDD]`.

## 6. 체이닝
| 목적 | 스킬 |
|---|---|
| 설계 입력 | `sz:creative-architect` |
| 배경 렌더 | `image-bridge(미포함)` (+ 프롬프트 빌더) |
| 브랜드킷 토큰 | `sz:design-system-prep` |
| SNS 카피·해시태그 | `sz:sns-content`·`sz:copywriting` |
| 텍스트 마감 | `sz:ai-slop-reviewer`→`sz:humanize-korean`→`sz:korean-spell-check` |
| 규제 | `commerce-marketing-compliance-kr(미포함)` |

> UZ/CIS 채널 규격·후조판은 `references/uz-poster-ad-builder.md`.
