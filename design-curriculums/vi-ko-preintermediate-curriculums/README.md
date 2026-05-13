# vi-ko Preintermediate → Intermediate Curriculums

Recovery manual for the 20 hand-crafted Vietnamese-for-Korean-learners curriculums created from this folder. After task 16.2, all `create_*.py` scripts and helper modules are deleted from this directory; the canonical source of truth is the production database. This README documents the IDs, structure, and verification queries needed to inspect, audit, or recreate the data.

## Overview

- **Audience**: Vietnamese speakers (`userLanguage="vi"`) learning Korean (`language="ko"`).
- **Levels covered**: 12 preintermediate + 8 intermediate (one collection bridging both).
- **Structure**: 1 collection → 5 series → 4 curriculums per series → 5 sessions per curriculum.
- **Vocabulary**: 18 Korean words per curriculum, split into 3 groups of 6 across viewFlashcards activities.
- **Pricing**: All 20 curriculums priced at `49` (won).
- **Visibility**: All curriculums are private (`is_public = false`). Generated content (audio, illustrations, segments) is added by the platform after creation; do not flip them public until that completes.
- **Owner UID**: `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.

## Collection

| Field | Value |
|---|---|
| ID | `pnhvrvxl` |
| Title | Tiếng Hàn Trung Cấp |

## Series

| Display order | ID | Title | Description tone |
|---|---|---|---|
| 1 | `w9l50fl3` | Sự Nghiệp Tại Hàn Quốc | `bold_declaration` |
| 2 | `bdggh18v` | Khám Phá Hàn Quốc | `vivid_scenario` |
| 3 | `bfbzoa1d` | Đời Sống Và Xã Hội | `empathetic_observation` |
| 4 | `yj551kdn` | Văn Hóa Và Giải Trí | `surprising_fact` |
| 5 | `w55q2rm9` | Thế Giới Hiện Đại | `provocative_question` |

The collection wires all 5 series via `curriculum_collection_series`. Each series holds exactly 4 curriculums.

## Curriculum format

| Aspect | Preintermediate (12 of 20) | Intermediate (8 of 20) |
|---|---|---|
| Sessions | 5 | 5 |
| Vocab count | 18 (3 groups of 6) | 18 (3 groups of 6) |
| `vocabLevel3` activity | not present | present in Session 4 |
| `writingParagraph` activity | not present | present in Session 5 |
| Reading passage difficulty | preintermediate Hangul | TOPIK II level |
| `contentTypeTags` | `[]` (or topical, per content rules) | `[]` (or topical) |
| Bilingual text (vi + ko) | yes | yes |

Both levels include hand-crafted Vietnamese marketing copy (`title`, `description`, `preview.text`), hand-crafted Korean reading passages, and hand-crafted introAudio scripts that teach each Korean word with Revised Romanization, Vietnamese meaning, and example sentences. Intermediate curriculums additionally include `writingParagraph` prompts in Vietnamese with at least two guiding questions.

## Curriculums

All curriculums share `language="ko"`, `userLanguage="vi"`, `price=49`, `is_public=false`. Tone columns are: `description tone / farewell introAudio tone`.

### Series 1 — Sự Nghiệp Tại Hàn Quốc (`w9l50fl3`)

| DO | ID | Title | Level | Tones | Vocabulary (18) |
|---|---|---|---|---|---|
| 1 | `SOTbtiM995Hz4LRo` | Phỏng Vấn Xin Việc | preintermediate | `provocative_question` / `warm_accountability` | 이력서, 면접, 지원동기, 경력, 연봉, 정규직, 야근, 상사, 부하, 승진, 퇴사, 지원하다, 채용, 연수, 출퇴근, 유급휴가, 이직, 명함 |
| 2 | `cLsn6yjAV0xzDRsc` | Thuê Nhà Ở Hàn Quốc | preintermediate | `vivid_scenario` / `quiet_awe` | 월세, 전세, 보증금, 부동산, 원룸, 자취, 이사, 계약, 보증인, 관리비, 역세권, 신축, 채광, 방음, 분리수거, 집주인, 갱신, 퇴거 |
| 3 | `q30SQA1IfiBvCfxG` | Giao Tiếp Qua Điện Thoại | preintermediate | `empathetic_observation` / `practical_momentum` | 전화하다, 자동응답, 수신, 발신, 다시 걸다, 메시지, 내선, 외선, 통화, 끊다, 연결되다, 통화 중, 번호, 등록, 연락처, 부재중, 문자, 돌려주다 |
| 4 | `nNNyUyVQAqF5eesA` | Văn Hóa Công Sở Hàn Quốc | intermediate | `bold_declaration` / `introspective_guide` | 존댓말, 보고, 연락, 상담, 회식, 송년회, 환영회, 송별회, 연공서열, 워라밸, 연차, 출장, 회의록, 발표, 마감, 결재, 사내문화, 팀워크 |

### Series 2 — Khám Phá Hàn Quốc (`bdggh18v`)

| DO | ID | Title | Level | Tones | Vocabulary (18) |
|---|---|---|---|---|---|
| 1 | `pR4EjhVH3Inu45O6` | Đặt Vé Và Lên Kế Hoạch | preintermediate | `surprising_fact` / `team_building_energy` | 예매, 편도, 왕복, 출발, 도착, 환승, 공항, 탑승, 여권, 관광, 여행사, 일정, 짐 싸기, 환전, 면세, 안내, 지도, 기념품 |
| 2 | `wUNI2uvWd3v1POGS` | Ẩm Thực Đường Phố Hàn Quốc | preintermediate | `metaphor_led` / `warm_accountability` | 포장마차, 떡볶이, 순대, 호떡, 주문하다, 포장, 먹방, 줄서다, 일회용, 맛, 매운, 달콤한, 굽다, 튀기다, 찌다, 속, 양념, 고명 |
| 3 | `dmTt9RcVwhQLHtm0` | Khám Bệnh Ở Hàn Quốc | preintermediate | `bold_declaration` / `quiet_awe` | 진찰, 증상, 처방전, 건강보험, 접수, 대기실, 내과, 외과, 검사, 주사, 입원, 퇴원, 약국, 알레르기, 예방접종, 진단, 소견서, 응급실 |
| 4 | `TRYBxNtap8Q54Gku` | Du Lịch Nông Thôn Hàn Quốc | intermediate | `vivid_scenario` / `practical_momentum` | 시골, 온천, 한옥, 민박, 농촌체험, 수확, 논, 밭, 어촌, 고택, 마을, 계단식 논, 특산물, 사투리, 축제, 향토음식, 자연, 풍경 |

### Series 3 — Đời Sống Và Xã Hội (`bfbzoa1d`)

| DO | ID | Title | Level | Tones | Vocabulary (18) |
|---|---|---|---|---|---|
| 1 | `vDrl5GzLH7lWu7hJ` | Mối Quan Hệ Xã Hội | preintermediate | `provocative_question` / `introspective_guide` | 친구, 지인, 사귀다, 헤어지다, 신뢰, 약속, 상담, 소개, 초대하다, 거절하다, 사과하다, 용서하다, 다투다, 화해하다, 배려, 속마음, 눈치, 체면 |
| 2 | `LZj8148VLUktEIQP` | Mua Sắm Trực Tuyến | preintermediate | `empathetic_observation` / `team_building_energy` | 인터넷 쇼핑, 장바구니, 배송비, 배달되다, 반품, 교환, 후기, 평점, 재고, 할인, 적립금, 쿠폰, 택배, 대금, 계좌이체, 카드결제, 영수증, 문의 |
| 3 | `1aYjBJIkb4649s9N` | Ngân Hàng Và Tài Chính | preintermediate | `bold_declaration` / `warm_accountability` | 은행, 계좌, 송금, 환율, 대출, 이자, 저축, 입금, 출금, 수수료, 신용카드, 체크카드, 잔액, 자동이체, 통장, 비밀번호, 외화, 금리 |
| 4 | `NmFT6O46nbm8Zm8o` | Tâm Lý Và Cảm Xúc | intermediate | `surprising_fact` / `quiet_awe` | 감정, 불안, 스트레스, 우울, 자신감, 열등감, 공감, 외로움, 성취감, 좌절, 성장, 자존감, 기분전환, 힐링, 명상, 상담, 의존, 회복 |

### Series 4 — Văn Hóa Và Giải Trí (`yj551kdn`)

| DO | ID | Title | Level | Tones | Vocabulary (18) |
|---|---|---|---|---|---|
| 1 | `3LgoIPUOslFhf19N` | K-Drama Và Giải Trí | preintermediate | `metaphor_led` / `practical_momentum` | 드라마, 배우, 촬영, 대본, 시청률, 방영, 팬, 팬미팅, 연예인, 오디션, 예능, 출연, 제작, 감독, 각본, 시즌, 결말, 명장면 |
| 2 | `YqHibTxAGVU0yz4S` | K-Pop Và Âm Nhạc | preintermediate | `vivid_scenario` / `introspective_guide` | 가수, 아이돌, 앨범, 음원, 차트, 컴백, 뮤직비디오, 안무, 팬덤, 응원봉, 콘서트, 데뷔, 작곡, 작사, 음악방송, 총판매량, 스트리밍, 팬카페 |
| 3 | `WaAPmU9Ew1B3qle3` | Tin Tức Và Thời Sự | intermediate | `provocative_question` / `team_building_energy` | 보도, 기자, 취재, 여론, 선거, 정책, 경제, 경기, 실업, 물가, 증세, 저출산, 고령화, 환경문제, 국제, 조약, 정상회담, 외교 |
| 4 | `HrFg9DXj1ZBZ4hfc` | Giáo Dục Ở Hàn Quốc | intermediate | `empathetic_observation` / `warm_accountability` | 입학, 졸업, 수능, 학원, 장학금, 학점, 논문, 연구, 교수, 강의, 등록금, 유학, 동아리, 축제, 성적, 진로, 취업준비, 대학원 |

### Series 5 — Thế Giới Hiện Đại (`w55q2rm9`)

| DO | ID | Title | Level | Tones | Vocabulary (18) |
|---|---|---|---|---|---|
| 1 | `RLI3brt9ObfHUyn8` | Thiên Tai Và An Toàn | preintermediate | `bold_declaration` / `quiet_awe` | 지진, 태풍, 홍수, 대피, 방재, 비상구, 대피소, 경보, 여진, 정전, 단수, 비축, 소화기, 구조, 안부확인, 방재용품, 내진, 긴급재난문자 |
| 2 | `NmotU5kLQQVxs7SW` | Công Nghệ Và AI | intermediate | `surprising_fact` / `practical_momentum` | 인공지능, 자동화, 로봇, 데이터, 알고리즘, 프로그래밍, 보안, 개인정보, SNS, 악플, 가짜뉴스, 가상현실, 전자결제, 구독, 클라우드, 알림, 업데이트, 해킹 |
| 3 | `S468QGQ6I6QDgk7N` | Pháp Luật Và Quy Tắc | intermediate | `metaphor_led` / `introspective_guide` | 법률, 규칙, 위반, 벌금, 신고, 허가, 의무, 권리, 계약, 보증, 배상, 재판, 변호사, 증거, 피해, 범죄, 방범, 비자 |
| 4 | `HzJbwrM4JopER3G6` | Môi Trường Và Phát Triển Bền Vững | intermediate | `vivid_scenario` / `team_building_energy` | 환경, 재활용, 분리수거, 재생에너지, 에너지, 온난화, 배출, 감축, 지속가능, 친환경, 절약, 태양광, 풍력, 오염, 생태계, 멸종위기, 산림파괴, 탄소중립 |

## SQL verification queries

Run via MCP postgres. The "spec id set" placeholder is the 20 curriculum IDs from the tables above.

```sql
-- 1. Count non-deleted curriculums for this spec.
-- Expected: 20.
SELECT COUNT(*)
FROM curriculum
WHERE id IN (
  'SOTbtiM995Hz4LRo','cLsn6yjAV0xzDRsc','q30SQA1IfiBvCfxG','nNNyUyVQAqF5eesA',
  'pR4EjhVH3Inu45O6','wUNI2uvWd3v1POGS','dmTt9RcVwhQLHtm0','TRYBxNtap8Q54Gku',
  'vDrl5GzLH7lWu7hJ','LZj8148VLUktEIQP','1aYjBJIkb4649s9N','NmFT6O46nbm8Zm8o',
  '3LgoIPUOslFhf19N','YqHibTxAGVU0yz4S','WaAPmU9Ew1B3qle3','HrFg9DXj1ZBZ4hfc',
  'RLI3brt9ObfHUyn8','NmotU5kLQQVxs7SW','S468QGQ6I6QDgk7N','HzJbwrM4JopER3G6'
)
  AND uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
  AND uid NOT LIKE '%_deleted';
```

```sql
-- 2. Verify language pair (all 20 should be language=ko, user_language=vi).
SELECT language, user_language, COUNT(*)
FROM curriculum
WHERE id IN (/* spec id set */)
GROUP BY language, user_language;
-- Expected single row: ('ko','vi',20)
```

```sql
-- 3. Verify all prices set to 49.
SELECT COUNT(*)
FROM curriculum
WHERE id IN (/* spec id set */) AND price = 49;
-- Expected: 20
```

```sql
-- 4. Verify all is_public=false (newly created, awaiting generation).
SELECT is_public, COUNT(*)
FROM curriculum
WHERE id IN (/* spec id set */)
GROUP BY is_public;
-- Expected single row: (false, 20)
```

```sql
-- 5. Verify series memberships and display orders (4 per series, display order 1..4).
SELECT cs.curriculum_series_id,
       cs.curriculum_id,
       c.display_order,
       c.content::jsonb->>'title' AS title
FROM curriculum_series_curriculum cs
JOIN curriculum c ON c.id = cs.curriculum_id
WHERE cs.curriculum_series_id IN ('w9l50fl3','bdggh18v','bfbzoa1d','yj551kdn','w55q2rm9')
ORDER BY cs.curriculum_series_id, c.display_order;
-- Expected: 20 rows, exactly 4 per series, display_order 1..4 within each series.
```

```sql
-- 6. Duplicate-title check (titles must be unique within this batch).
SELECT content::jsonb->>'title' AS title, COUNT(*)
FROM curriculum
WHERE id IN (/* spec id set */)
GROUP BY content::jsonb->>'title'
HAVING COUNT(*) > 1;
-- Expected: 0 rows.
```

```sql
-- 7. Verify collection → series wiring.
SELECT curriculum_collection_id, curriculum_series_id
FROM curriculum_collection_series
WHERE curriculum_collection_id = 'pnhvrvxl'
ORDER BY curriculum_series_id;
-- Expected: 5 rows, one per series id (w9l50fl3, bdggh18v, bfbzoa1d, yj551kdn, w55q2rm9).
```

```sql
-- 8. Confirm homogeneous language pair per series and per collection.
SELECT * FROM curriculum_series_language_list
WHERE curriculum_series_id IN ('w9l50fl3','bdggh18v','bfbzoa1d','yj551kdn','w55q2rm9');

SELECT * FROM curriculum_collections_language_list
WHERE curriculum_collection_id = 'pnhvrvxl';
-- Expected: each row shows language=ko, user_language=vi only (no mixed pairs).
```

```sql
-- 9. Confirm max 1-level gap within each series and within the collection.
SELECT * FROM curriculum_series_level_gap
WHERE curriculum_series_id IN ('w9l50fl3','bdggh18v','bfbzoa1d','yj551kdn','w55q2rm9');

SELECT * FROM curriculum_collections_level_gap
WHERE curriculum_collection_id = 'pnhvrvxl';
-- Expected: gap <= 1 across all rows. The collection bridges preintermediate↔intermediate (gap=1) which is allowed.
```

```sql
-- 10. Spot-check format split: 12 preintermediate + 8 intermediate.
SELECT (content::jsonb->>'level') AS level, COUNT(*)
FROM curriculum
WHERE id IN (/* spec id set */)
GROUP BY (content::jsonb->>'level');
-- Expected: ('preintermediate',12), ('intermediate',8)
```

## Recreation instructions

Per task 16.2, the `orchestrator.py`, all `create_*.py` scripts, `validate_content.py`, and `test_validate.py` are deleted from this directory after the data is verified in the database. Only this `README.md` remains.

The canonical source of truth for the curriculum data is now the production database. Inspect any individual curriculum via:

- API: `POST https://helloapi.step.is/curriculum/getOne` with `{ "id": "<curriculum_id>", "uid": "zs5AMpVfqkcfDf8CJ9qrXdH58d73" }` (no auth required for `getOne`).
- MCP postgres: `SELECT content FROM curriculum WHERE id = '<curriculum_id>';`

If the rows must be rebuilt from scratch (e.g., catastrophic data loss):

1. Re-author the content. The hand-crafted Vietnamese marketing copy, Korean reading passages, and bilingual session scripts must be re-authored from the spec materials in `.kiro/specs/vi-ko-preintermediate-curriculums/` (`requirements.md`, `design.md`, `tasks.md`). The 18-word vocab lists in this README are stable inputs; the surrounding prose is not stored elsewhere and must be re-written following `CURRICULUM_QUALITY_STANDARDS.md` and `CURRICULUM_CREATION_RULES.md`.
2. Validate every payload before upload using the rules previously implemented in `validate_content.py` (preintermediate vs intermediate session/activity shape, vocab counts, tone variety, no `mp3Url`/`illustrationSet`/`segments`/etc., bilingual fields populated, `contentTypeTags` present).
3. Recreate the collection and the 5 series via `curriculum-collection/create` and `curriculum-series/create`. Note the API generates fresh IDs — to keep the IDs in this README stable, recreate them by direct DB insert, otherwise update this README with new IDs.
4. Recreate each curriculum via `curriculum/create` (top-level `language="ko"`, `userLanguage="vi"`, plus the `content` JSON string). Wire to its series via `curriculum-series/addCurriculum`, set per-series `displayOrder` via `curriculum/setDisplayOrder`, and set `price=49` via `curriculum/setPrice`. Wire each series into the collection via `curriculum-collection/addSeriesToCollection` and set series display order via `curriculum-series/setDisplayOrder`.
5. Leave `is_public=false` until the platform finishes generating audio/illustrations.
6. Re-run the verification queries above to confirm 20 rows, correct language pair, prices, series memberships, display orders, and homogeneous language and level-gap views.
