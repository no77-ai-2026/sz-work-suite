---
name: sample-log
description: |
  샘플 관리·재고실사(리스크 매니지먼트) — 기존 샘플 대장 기반 관리 + 실사 사진의 식별번호 판독·파일명 변경·대장 대조·폴더 분류·결과보고. 재촬영 의심 감지 포함. 트리거: "샘플 대장 정리해줘", "재고실사 사진 대조해줘", "실사 결과 보고서"
  EN: Sample ledger management and stocktaking photo reconciliation (Risk Management) — extract IDs from photos, rename files, match against ledger, sort into folders, report. Triggers: "reconcile stocktaking photos", "sample ledger update", "stock audit report"
version: 1.1.2
---

# sz:sample-log — 샘플 관리·재고실사 (리스크 매니지먼트)

## 언어 규칙
요청 언어(KO/EN/RU/UZ)로 응답.

## 모드 A — 대장 관리
1. **기존 샘플 대장(사내 양식 xlsx) 업로드를 먼저 요청한다.** 표준 컬럼을 이 스킬이 강제하지 않는다 — 대장의 컬럼 구조를 읽고 **식별번호 컬럼만 사용자에게 확인**한다.
2. 상태 업데이트, 회수 기한 초과 하이라이트, 발송·회수 요청 문서 초안(`sz:doc-formats` 골격).

## 모드 B — 재고실사 사진 대조 (핵심)
입력: 샘플 대장(xlsx) + 실사 사진 폴더. 판독·매칭·분류 규칙 정본: `references/photo-id-match.md`

절차:
1. 사진별 식별번호 판독(추측 금지, 형식 대조). 재촬영(스크린 촬영) 단서 동시 점검.
2. 정상 판독 사진의 파일명을 식별번호로 변경(중복 `_2` 규칙).
3. 대장 대조 → `01_매칭/` `02_불일치_사진만/` `03_판독불가/` `04_재촬영의심/` 분류. 대장에만 있는 항목은 **실사누락 리스트**.
4. 결과보고: 요약 집계 + 상세 표 + 육안 확인 대상(불일치·판독불가·재촬영 의심·실사누락) 명시.

## HARD
- 판독불가·재촬영 의심·불일치를 스킬이 임의 판정하지 않는다 — 최종 판정은 사용자 육안 확인.
- 실사 결과 수치(매칭률 등)는 반드시 분류 폴더 실측 개수와 일치해야 한다(보고 전 재검산).

## 체인
세관 반출입 이슈 → `sz:trade-logistics` / 리스크 등급화 → `sz:risk-radar`

## English Summary
Mode A: manage the existing sample ledger (ask the user to upload it; never impose columns; confirm the ID column). Mode B: stocktaking photo reconciliation — extract IDs from photos (no guessing; screen-recapture cues checked), rename files to IDs, match against the ledger, sort into 01_matched / 02_photo_only / 03_unreadable / 04_recapture_suspected, list ledger-only items as missing, and report. Final judgment always belongs to the user. Engine: references/photo-id-match.md.
