# Implementation Plan: Vietnamese-Korean Preintermediate/Intermediate Curriculums

## Overview

Create 20 Korean-learning curriculums for Vietnamese-speaking adults at preintermediate and intermediate levels, organized into 1 collection ("Tiếng Hàn Trung Cấp") and 5 series of 4 curriculums each. Language pair: `userLanguage="vi"`, `language="ko"`.

Implementation uses Python scripts in `vi-ko-preintermediate-curriculums/`. Two curriculum formats: preintermediate (5 sessions, 18 words in 3 groups of 6, no writingParagraph/vocabLevel3, price 49) and intermediate (5 sessions, 18 words in 3 groups of 6, vocabLevel3 in Session 4, writingParagraph in Session 5, price 49). Each curriculum gets its own standalone script with hand-crafted content including Hangul with Revised Romanization. A preintermediate/intermediate-specific `validate_content.py` enforces format rules before upload. The shared root-level `api_helpers.py` handles all API calls.

Execution order: (1) content validator + property tests, (2) orchestrator for collection/series, (3) preintermediate scripts ×12, (4) intermediate scripts ×8, (5) README + cleanup.

## Tasks

- [x] 1. Create preintermediate/intermediate content validator
  - [x] 1.1 Create `vi-ko-preintermediate-curriculums/validate_content.py` with format-aware `validate(content, format)` function
    - `format` parameter: `"preintermediate"` or `"intermediate"`
    - Format-specific checks: session count = exactly 5 for both formats; vocab count = exactly 18 (3 groups of 6) for both formats
    - Preintermediate forbidden activities: `writingParagraph` and `vocabLevel3` forbidden in ALL sessions
    - Intermediate required activities: `vocabLevel3` ONLY in Session 4; `writingParagraph` ONLY in Session 5; raise error if missing from required session or present in wrong session
    - Shared checks: top-level structure (title, description, preview.text, contentTypeTags: [], learningSessions), session structure (title, non-empty activities), activity structure (activityType not type, valid values, title, description, data as dict), vocabList format (array of strings, field name vocabList not words — NO lowercase enforcement for Korean Hangul has no case), flashcard consistency (viewFlashcards/speakFlashcards identical vocabList in same session), writingSentence structure (data.vocabList, data.items with prompt and targetVocab), writingParagraph structure (data.vocabList, data.instructions, data.prompts array with >=2 items), strip-keys exclusion (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId)
    - Total unique vocab count = 18 across all sessions
    - Raise `ValueError` with specific violation message identifying the rule, location (session/activity index), format, and expected vs actual value
    - _Requirements: 1.3, 1.4, 1.5, 1.6, 1.8, 1.9, 1.10, 1.11, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 11.10, 11.11, 11.12_

  - [x] 1.2 Write property test: Valid content passes validation (Property 1)
    - **Property 1: Valid content passes validation**
    - Use `hypothesis` to generate well-formed curriculum content dicts matching each of the 2 formats (exactly 5 sessions, 18 vocab words in 3 groups of 6, all required fields, no forbidden activities for preintermediate, correct placement of required activities for intermediate, no strip keys, vocabList as arrays of Korean strings from Hangul Syllables block U+AC00-U+D7AF) and verify `validate(content, format)` returns without exception
    - **Validates: Requirements 1.3, 1.4, 1.5, 11.1, 11.2, 11.3, 11.4**

  - [x] 1.3 Write property test: Forbidden activities rejected for preintermediate (Property 2)
    - **Property 2: Forbidden activities are rejected for preintermediate format**
    - Use `hypothesis` to inject `writingParagraph` or `vocabLevel3` into any session of a valid preintermediate curriculum and verify `validate(content, "preintermediate")` raises ValueError identifying the forbidden activity
    - **Validates: Requirements 1.8, 1.9, 4.2, 11.10**

  - [x] 1.4 Write property test: Intermediate activity placement enforced (Property 3)
    - **Property 3: Intermediate activity placement is enforced**
    - Use `hypothesis` to test: (a) vocabLevel3 in wrong session raises ValueError, (b) writingParagraph in wrong session raises ValueError, (c) vocabLevel3 missing from Session 4 raises ValueError, (d) writingParagraph missing from Session 5 raises ValueError
    - **Validates: Requirements 1.10, 1.11, 5.2, 5.3, 11.11**

  - [x] 1.5 Write property test: Strip keys rejected anywhere in JSON tree (Property 4)
    - **Property 4: Strip keys are rejected anywhere in the JSON tree**
    - Use `hypothesis` to inject strip keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) at random depths in curriculum JSON and verify rejection with message mentioning the strip key
    - **Validates: Requirements 1.6, 11.9**

  - [x] 1.6 Write property test: Activities missing required fields rejected (Property 5)
    - **Property 5: Activities missing required fields are rejected**
    - Use `hypothesis` to generate activities missing `activityType`, `title`, `description`, or `data`, or with `data` not being a dict, and verify rejection identifying the missing field and its location
    - **Validates: Requirements 10.1, 10.5, 11.3**

  - [x] 1.7 Write property test: Invalid activityType values rejected (Property 6)
    - **Property 6: Invalid activityType values are rejected**
    - Use `hypothesis` to generate activities with `activityType` values not in the valid set (introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence, writingParagraph) and verify rejection
    - **Validates: Requirements 10.2, 11.4**

  - [x] 1.8 Write property test: vocabList format enforced (Property 7)
    - **Property 7: vocabList format is enforced**
    - Use `hypothesis` to generate vocab activities with non-array vocabList, empty vocabList, non-string elements, or field name `words` instead of `vocabList`, and verify rejection. Note: lowercase is NOT enforced for Korean vocabulary (Hangul has no case)
    - **Validates: Requirements 10.3, 11.5**

  - [x] 1.9 Write property test: Flashcard vocabList consistency (Property 8)
    - **Property 8: Flashcard vocabList consistency within sessions**
    - Use `hypothesis` to generate sessions with mismatched viewFlashcards/speakFlashcards vocabList arrays and verify rejection
    - **Validates: Requirements 10.4, 11.6**

  - [x] 1.10 Write property test: Writing activity structure enforced (Property 9)
    - **Property 9: Writing activity structure is enforced**
    - Use `hypothesis` to generate: (a) writingSentence activities with missing data.vocabList, missing/empty data.items, or items lacking prompt/targetVocab and verify rejection; (b) writingParagraph activities with missing data.vocabList, missing/empty data.instructions, or data.prompts with fewer than 2 items and verify rejection
    - **Validates: Requirements 10.6, 10.7, 11.7, 11.8**

- [x] 2. Checkpoint — Content validator ready
  - Ensure all tests pass, ask the user if questions arise.

- [x] 3. Create orchestrator and collection/series infrastructure
  - [x] 3.1 Create `vi-ko-preintermediate-curriculums/orchestrator.py`
    - Create 1 collection: "Tiếng Hàn Trung Cấp" with neutral informative Vietnamese description about advancing beyond beginner level
    - Create 5 series with descriptions ≤255 chars each using different Tone_Palette types:
      - Series 1: "Sự Nghiệp Tại Hàn Quốc" (tone: `bold_declaration`)
      - Series 2: "Khám Phá Hàn Quốc" (tone: `vivid_scenario`)
      - Series 3: "Đời Sống Và Xã Hội" (tone: `empathetic_observation`)
      - Series 4: "Văn Hóa Và Giải Trí" (tone: `surprising_fact`)
      - Series 5: "Thế Giới Hiện Đại" (tone: `provocative_question`)
    - Wire all 5 series to the collection via `add_series_to_collection`
    - Set display orders for all 5 series via `set_series_display_order`
    - Hard-code the tone assignment table from the design (all 20 curriculum description tones and farewell tones) and print it for reference
    - Log collection ID and all 5 series IDs to stdout
    - Uses root-level `api_helpers.py` via sys.path: `create_collection`, `create_series`, `add_series_to_collection`, `set_series_display_order`
    - _Requirements: 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 12.2, 12.3, 12.4, 12.5, 16.1_


- [x] 4. Create preintermediate curriculum scripts — Series 1: "Sự Nghiệp Tại Hàn Quốc"
  - [x] 4.1 Create `vi-ko-preintermediate-curriculums/create_job_interview.py` — "Phỏng Vấn Xin Việc" (Series 1, display order 1)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["이력서", "면접", "지원동기", "경력", "연봉", "정규직", "야근", "상사", "부하", "승진", "퇴사", "지원하다", "채용", "연수", "출퇴근", "유급휴가", "이직", "명함"]
    - Session structure per design: S1-S3 (learning with introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, introAudio grammar, reading 150-250 chars in Hangul, speakReading, readAlong, writingSentence ×3), S4 (review with all 18 words, vocabLevel1+2, writingSentence ×4-5), S5 (final reading 400-600 chars, farewell introAudio)
    - Description tone: `provocative_question`, farewell tone: `warm_accountability`
    - All text hand-crafted: Vietnamese marketing copy, Korean reading passages in Hangul, introAudio scripts teaching each word with Revised Romanization/Vietnamese meaning/example sentences
    - Validate with `validate(content, "preintermediate")` before upload
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 4.2 Create `vi-ko-preintermediate-curriculums/create_renting.py` — "Thuê Nhà Ở Hàn Quốc" (Series 1, display order 2)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["월세", "전세", "보증금", "부동산", "원룸", "자취", "이사", "계약", "보증인", "관리비", "역세권", "신축", "채광", "방음", "분리수거", "집주인", "갱신", "퇴거"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for renting/housing topic
    - Description tone: `vivid_scenario`, farewell tone: `quiet_awe`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 4.3 Create `vi-ko-preintermediate-curriculums/create_phone_communication.py` — "Giao Tiếp Qua Điện Thoại" (Series 1, display order 3)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["전화하다", "자동응답", "수신", "발신", "다시 걸다", "메시지", "내선", "외선", "통화", "끊다", "연결되다", "통화 중", "번호", "등록", "연락처", "부재중", "문자", "돌려주다"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for phone communication topic
    - Description tone: `empathetic_observation`, farewell tone: `practical_momentum`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

- [x] 5. Create preintermediate curriculum scripts — Series 2: "Khám Phá Hàn Quốc"
  - [x] 5.1 Create `vi-ko-preintermediate-curriculums/create_booking_planning.py` — "Đặt Vé Và Lên Kế Hoạch" (Series 2, display order 1)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["예매", "편도", "왕복", "출발", "도착", "환승", "공항", "탑승", "여권", "관광", "여행사", "일정", "짐 싸기", "환전", "면세", "안내", "지도", "기념품"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for travel planning topic
    - Description tone: `surprising_fact`, farewell tone: `team_building_energy`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 5.2 Create `vi-ko-preintermediate-curriculums/create_street_food.py` — "Ẩm Thực Đường Phố Hàn Quốc" (Series 2, display order 2)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["포장마차", "떡볶이", "순대", "호떡", "주문하다", "포장", "먹방", "줄서다", "일회용", "맛", "매운", "달콤한", "굽다", "튀기다", "찌다", "속", "양념", "고명"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for Korean street food culture topic
    - Description tone: `metaphor_led`, farewell tone: `warm_accountability`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 5.3 Create `vi-ko-preintermediate-curriculums/create_medical_visit.py` — "Khám Bệnh Ở Hàn Quốc" (Series 2, display order 3)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["진찰", "증상", "처방전", "건강보험", "접수", "대기실", "내과", "외과", "검사", "주사", "입원", "퇴원", "약국", "알레르기", "예방접종", "진단", "소견서", "응급실"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for medical visit topic
    - Description tone: `bold_declaration`, farewell tone: `quiet_awe`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

- [x] 6. Create preintermediate curriculum scripts — Series 3: "Đời Sống Và Xã Hội"
  - [x] 6.1 Create `vi-ko-preintermediate-curriculums/create_social_relationships.py` — "Mối Quan Hệ Xã Hội" (Series 3, display order 1)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["친구", "지인", "사귀다", "헤어지다", "신뢰", "약속", "상담", "소개", "초대하다", "거절하다", "사과하다", "용서하다", "다투다", "화해하다", "배려", "속마음", "눈치", "체면"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for social relationships topic
    - Description tone: `provocative_question`, farewell tone: `introspective_guide`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 6.2 Create `vi-ko-preintermediate-curriculums/create_online_shopping.py` — "Mua Sắm Trực Tuyến" (Series 3, display order 2)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["인터넷 쇼핑", "장바구니", "배송비", "배달되다", "반품", "교환", "후기", "평점", "재고", "할인", "적립금", "쿠폰", "택배", "대금", "계좌이체", "카드결제", "영수증", "문의"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for online shopping topic
    - Description tone: `empathetic_observation`, farewell tone: `team_building_energy`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 6.3 Create `vi-ko-preintermediate-curriculums/create_banking_finance.py` — "Ngân Hàng Và Tài Chính" (Series 3, display order 3)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["은행", "계좌", "송금", "환율", "대출", "이자", "저축", "입금", "출금", "수수료", "신용카드", "체크카드", "잔액", "자동이체", "통장", "비밀번호", "외화", "금리"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for banking/finance topic
    - Description tone: `bold_declaration`, farewell tone: `warm_accountability`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

- [x] 7. Create preintermediate curriculum scripts — Series 4: "Văn Hóa Và Giải Trí"
  - [x] 7.1 Create `vi-ko-preintermediate-curriculums/create_kdrama_entertainment.py` — "K-Drama Và Giải Trí" (Series 4, display order 1)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["드라마", "배우", "촬영", "대본", "시청률", "방영", "팬", "팬미팅", "연예인", "오디션", "예능", "출연", "제작", "감독", "각본", "시즌", "결말", "명장면"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for K-drama/entertainment topic
    - Description tone: `metaphor_led`, farewell tone: `practical_momentum`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 7.2 Create `vi-ko-preintermediate-curriculums/create_kpop_music.py` — "K-Pop Và Âm Nhạc" (Series 4, display order 2)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["가수", "아이돌", "앨범", "음원", "차트", "컴백", "뮤직비디오", "안무", "팬덤", "응원봉", "콘서트", "데뷔", "작곡", "작사", "음악방송", "총판매량", "스트리밍", "팬카페"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for K-pop/music topic
    - Description tone: `vivid_scenario`, farewell tone: `introspective_guide`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

- [x] 8. Create preintermediate curriculum scripts — Series 5: "Thế Giới Hiện Đại"
  - [x] 8.1 Create `vi-ko-preintermediate-curriculums/create_natural_disasters.py` — "Thiên Tai Và An Toàn" (Series 5, display order 1)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["지진", "태풍", "홍수", "대피", "방재", "비상구", "대피소", "경보", "여진", "정전", "단수", "비축", "소화기", "구조", "안부확인", "방재용품", "내진", "긴급재난문자"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for natural disasters/safety topic
    - Description tone: `bold_declaration`, farewell tone: `quiet_awe`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

- [x] 9. Checkpoint — All 12 preintermediate curriculums done
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 12 preintermediate curriculums created with correct series assignments
  - Verify all prices set to 49
  - Verify no writingParagraph or vocabLevel3 in any preintermediate curriculum
  - Verify language pair: all have `language="ko"`, `userLanguage="vi"`


- [x] 10. Create intermediate curriculum scripts — Series 1: "Sự Nghiệp Tại Hàn Quốc"
  - [x] 10.1 Create `vi-ko-preintermediate-curriculums/create_office_culture.py` — "Văn Hóa Công Sở Hàn Quốc" (Series 1, display order 4)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["존댓말", "보고", "연락", "상담", "회식", "송년회", "환영회", "송별회", "연공서열", "워라밸", "연차", "출장", "회의록", "발표", "마감", "결재", "사내문화", "팀워크"]
    - Session structure per design: S1-S3 (learning with introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, introAudio grammar, reading 200-350 chars in Hangul at TOPIK II level, speakReading, readAlong, writingSentence ×3), S4 (review with all 18 words, vocabLevel1+2+3, writingSentence ×4-5), S5 (final reading 500-800 chars, writingParagraph using 6+ vocab words, farewell introAudio)
    - Description tone: `bold_declaration`, farewell tone: `introspective_guide`
    - All text hand-crafted: Vietnamese marketing copy, Korean reading passages in Hangul (TOPIK II level), introAudio scripts teaching each word with Revised Romanization/Vietnamese meaning/example sentences, writingParagraph with Vietnamese instructions and >=2 guiding questions
    - Validate with `validate(content, "intermediate")` before upload
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

- [x] 11. Create intermediate curriculum scripts — Series 2: "Khám Phá Hàn Quốc"
  - [x] 11.1 Create `vi-ko-preintermediate-curriculums/create_rural_tourism.py` — "Du Lịch Nông Thôn Hàn Quốc" (Series 2, display order 4)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["시골", "온천", "한옥", "민박", "농촌체험", "수확", "논", "밭", "어촌", "고택", "마을", "계단식 논", "특산물", "사투리", "축제", "향토음식", "자연", "풍경"]
    - Same 5-session intermediate structure as 10.1 but all content hand-crafted for Korean rural tourism topic
    - Description tone: `vivid_scenario`, farewell tone: `practical_momentum`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

- [x] 12. Create intermediate curriculum scripts — Series 3: "Đời Sống Và Xã Hội"
  - [x] 12.1 Create `vi-ko-preintermediate-curriculums/create_psychology_emotions.py` — "Tâm Lý Và Cảm Xúc" (Series 3, display order 4)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["감정", "불안", "스트레스", "우울", "자신감", "열등감", "공감", "외로움", "성취감", "좌절", "성장", "자존감", "기분전환", "힐링", "명상", "상담", "의존", "회복"]
    - Same 5-session intermediate structure as 10.1 but all content hand-crafted for psychology/emotions topic
    - Description tone: `surprising_fact`, farewell tone: `quiet_awe`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

- [x] 13. Create intermediate curriculum scripts — Series 4: "Văn Hóa Và Giải Trí"
  - [x] 13.1 Create `vi-ko-preintermediate-curriculums/create_news_events.py` — "Tin Tức Và Thời Sự" (Series 4, display order 3)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["보도", "기자", "취재", "여론", "선거", "정책", "경제", "경기", "실업", "물가", "증세", "저출산", "고령화", "환경문제", "국제", "조약", "정상회담", "외교"]
    - Same 5-session intermediate structure as 10.1 but all content hand-crafted for news/current events topic
    - Description tone: `provocative_question`, farewell tone: `team_building_energy`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 13.2 Create `vi-ko-preintermediate-curriculums/create_education.py` — "Giáo Dục Ở Hàn Quốc" (Series 4, display order 4)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["입학", "졸업", "수능", "학원", "장학금", "학점", "논문", "연구", "교수", "강의", "등록금", "유학", "동아리", "축제", "성적", "진로", "취업준비", "대학원"]
    - Same 5-session intermediate structure as 10.1 but all content hand-crafted for Korean education system topic
    - Description tone: `empathetic_observation`, farewell tone: `warm_accountability`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

- [x] 14. Create intermediate curriculum scripts — Series 5: "Thế Giới Hiện Đại"
  - [x] 14.1 Create `vi-ko-preintermediate-curriculums/create_technology_ai.py` — "Công Nghệ Và AI" (Series 5, display order 2)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["인공지능", "자동화", "로봇", "데이터", "알고리즘", "프로그래밍", "보안", "개인정보", "SNS", "악플", "가짜뉴스", "가상현실", "전자결제", "구독", "클라우드", "알림", "업데이트", "해킹"]
    - Same 5-session intermediate structure as 10.1 but all content hand-crafted for technology/AI topic
    - Description tone: `surprising_fact`, farewell tone: `practical_momentum`
    - Note: Requirements description mentions SNS/eseuenesseu — use "SNS" in vocabList as it appears in the requirements description (loanword used as-is in Korean)
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 14.2 Create `vi-ko-preintermediate-curriculums/create_law_rules.py` — "Pháp Luật Và Quy Tắc" (Series 5, display order 3)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["법률", "규칙", "위반", "벌금", "신고", "허가", "의무", "권리", "계약", "보증", "배상", "재판", "변호사", "증거", "피해", "범죄", "방범", "비자"]
    - Same 5-session intermediate structure as 10.1 but all content hand-crafted for law/rules topic
    - Description tone: `metaphor_led`, farewell tone: `introspective_guide`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 14.3 Create `vi-ko-preintermediate-curriculums/create_environment.py` — "Môi Trường Và Phát Triển Bền Vững" (Series 5, display order 4)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["환경", "재활용", "분리수거", "재생에너지", "에너지", "온난화", "배출", "감축", "지속가능", "친환경", "절약", "태양광", "풍력", "오염", "생태계", "멸종위기", "산림파괴", "탄소중립"]
    - Same 5-session intermediate structure as 10.1 but all content hand-crafted for environment/sustainability topic
    - Description tone: `vivid_scenario`, farewell tone: `team_building_energy`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

- [x] 15. Checkpoint — All 20 curriculums created
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 12 preintermediate curriculums: no writingParagraph/vocabLevel3
  - Verify 8 intermediate curriculums: vocabLevel3 in Session 4, writingParagraph in Session 5
  - Verify all 20 prices set to 49
  - Verify language pair: all have `language="ko"`, `userLanguage="vi"`
  - Verify series membership: 4 curriculums per series, correct display orders
  - Run duplicate check queries for all 20 curriculum titles

- [x] 16. Documentation and cleanup
  - [x] 16.1 Create `vi-ko-preintermediate-curriculums/README.md`
    - Document: collection ID, all 5 series IDs, all 20 curriculum IDs with titles and display orders
    - Document: vocabulary lists per curriculum (all 20 × 18 words)
    - Document: tone assignments (description and farewell for all 20 curriculums)
    - Document: pricing (49 for all), language pair (vi-ko), format (preintermediate vs intermediate)
    - Include SQL verification queries: count curriculums, verify language pair, verify prices, verify series membership and display orders, verify no duplicates, verify collection → series wiring, verify level gap within series
    - Include recreation instructions
    - _Requirements: 15.1_

  - [x] 16.2 Delete all creation scripts after verification
    - Delete `orchestrator.py`, all 20 `create_*.py` scripts, `validate_content.py`, and `test_validate.py` from `vi-ko-preintermediate-curriculums/`
    - Only `README.md` remains in the directory
    - _Requirements: 15.2_

  - [x] 16.3 Run duplicate check and resolve
    - Run duplicate check query for each of the 20 curriculum titles
    - If duplicates found: keep earliest, remove from series first, then delete extras
    - _Requirements: 15.3_

- [x] 17. Final checkpoint — All tasks complete
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 20 curriculums total: 12 preintermediate + 8 intermediate
  - Verify collection and series structure is correct (1 collection, 5 series, 4 curriculums each)
  - Verify README.md is in place and all creation scripts are deleted
  - Verify no `setPublic` calls were made (all curriculums remain private)

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation between phases
- Property tests validate the preintermediate/intermediate-specific content validator (Properties 1-9) from the design
- The `validate_content.py` supports two formats: `preintermediate` (forbids writingParagraph/vocabLevel3) and `intermediate` (requires vocabLevel3 in S4, writingParagraph in S5)
- Root-level `api_helpers.py` is reused as-is — no changes needed
- All curriculum content must be hand-crafted — no template-based generation for learner-facing text
- Two formats: preintermediate (5 sessions, 18 words, no writingParagraph/vocabLevel3, price 49) and intermediate (5 sessions, 18 words, vocabLevel3 in S4, writingParagraph in S5, price 49)
- Korean vocabulary in Hangul with Revised Romanization pronunciation guidance in introAudio scripts
- No lowercase enforcement for vocabList — Korean Hangul has no letter case
- Series grouping: Series 1 (Career: curriculums 1,4,7,13), Series 2 (Discovering Korea: 2,3,5,17), Series 3 (Life/Society: 6,8,12,16), Series 4 (Culture/Entertainment: 9,10,14,15), Series 5 (Modern World: 11,18,19,20)
