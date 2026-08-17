---
name: sales-verify
description: |
  ISA 판매 검증·세일즈 인센티브(세일즈서포트) — 판매이력 엑셀과 필드포스 IMEI/시리얼 사진 대조, Luhn 검증, 재촬영·중복 IMEI 부정 방지 플래그, 필드포스별 지급 근거 산출. 트리거: "ISA 판매 검증해줘", "세일즈 인센티브 정산", "IMEI 사진 대조"
  EN: ISA sales verification and sales incentive (Sales Support) — match sales history vs field-force IMEI/serial photos, Luhn check, screen-recapture and duplicate-IMEI fraud flags, per-field-force payout basis. Triggers: "verify ISA sales", "sales incentive settlement", "match IMEI photos"
version: 1.1.2
---

# sz:sales-verify — ISA 판매 검증·세일즈 인센티브 (세일즈서포트)

> ISA = 사내 판매관리 앱 (internal sales application, 가칭)

필드포스가 판매 시 촬영·업로드한 IMEI/시리얼 사진과 ISA 판매이력을 대조해 세일즈 보너스(세일즈 인센티브) 지급 근거를 만든다. 판독·매칭 규칙 정본: `references/photo-id-match.md` (sz:sample-log와 공유 — 수정 시 동기화)

## 언어 규칙
요청 언어(KO/EN/RU/UZ)로 응답.

## 입력 (사용자에게 요청)
1. ISA 관리자화면에서 다운로드한 **판매이력 엑셀** — 컬럼 구조를 가정하지 않고 파일을 읽어 **IMEI/시리얼·필드포스·모델·판매일 컬럼을 사용자에게 확인**한다.
2. 필드포스 업로드 **사진 폴더**.
3. (선택) 모델별 지급 단가표 — 있으면 금액 자동 계산.

## 절차
1. **판독**: 사진별 IMEI/시리얼 추출. IMEI는 15자리+Luhn 체크섬 검증(실패=판독불가). 재촬영(스크린 촬영) 단서 동시 점검 — 실물이 아닌 화면 재촬영은 리젝 사유였던 실제 사례가 있으므로 중점 확인.
2. **파일명 변경**: 정상 판독 사진을 식별번호로 rename(중복 `_2` 규칙, 원본명은 보고서에 기록).
3. **대조·부정 방지 플래그**:
   - 매칭: 판매이력 ↔ 사진 IMEI 일치
   - 🚩 동일 IMEI 복수 판매 건(이중 청구 의심) / 🚩 이력만 있고 사진 없음 / 🚩 사진만 있고 이력 없음 / 🚩 재촬영 의심(사유 명기)
4. **집계**: 필드포스별 매칭 건수(모델별 분해) → 지급 근거 표. 단가표 제공 시 금액 계산(계산식 표기).
5. **보고**: 요약(총 건·매칭·플래그별 건수) + 필드포스별 지급 근거 xlsx + 육안 확인 대상 목록. 폴더 분류는 `01_매칭/` `02_불일치_사진만/` `03_판독불가/` `04_재촬영의심/`.

## HARD
- 지급·리젝의 최종 판정은 사용자 — 스킬은 근거와 플래그만 제공한다.
- 플래그 건은 지급 근거 표에서 제외하고 별도 목록으로(가지급 방지).
- 집계 수치는 폴더 실측·이력 건수와 재검산 후 보고.

## 체인
지급 문서·품의 → `sz:doc-formats` / 필드포스 정책 리스크 → `sz:risk-radar`

## English Summary
Inputs: ISA sales-history Excel (confirm IMEI/field-force/model columns with the user) + field-force photos (+ optional payout rate table). Extract IMEI/serial (15-digit Luhn check; failures = unreadable), flag fraud signals (duplicate IMEI across sales, history-without-photo, photo-without-history, screen recapture with stated reasons), aggregate matches per field force into a payout-basis table. Flagged items are excluded from payout and listed for human review. Engine: references/photo-id-match.md (shared with sz:sample-log).
