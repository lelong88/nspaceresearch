# Implementation Plan: Vietnamese-Korean Beginner Curriculums

## Overview

Create 20 Korean-learning curriculums for Vietnamese-speaking adults at the beginner level, organized into 1 collection ("Tiếng Hàn Cho Người Mới Bắt Đầu") and 3 series ("Những Bước Đầu Tiên" with 8 beginner mini curriculums, "Khám Phá Cuộc Sống" with 6 beginner short curriculums, "Mở Rộng Thế Giới" with 6 beginner short curriculums).

Implementation uses Python scripts in `vi-ko-beginner-curriculums/`. Language pair: `userLanguage="vi"`, `language="ko"`. Two curriculum formats: beginner_mini (1 session, 3-5 words, price 9), beginner_short (4 sessions, 8-10 words, price 19). Each curriculum gets its own standalone script with hand-crafted beginner Korean content. A beginner-specific `validate_content.py` enforces format rules before upload (NO lowercase enforcement for Korean Hangul). The shared root-level `api_helpers.py` handles all API calls.

Execution order: (1) content validator + property tests, (2) orchestrator for collection/series, (3) beginner mini scripts ×8, (4) beginner short scripts ×6 for Series 2, (5) beginner short scripts ×6 for Series 3, (6) README + cleanup.

## Tasks

- [x] 1. Create beginner-specific content validator
  - [x] 1.1 Create `vi-ko-beginner-curriculums/validate_content.py` with format-aware `validate(content, format)` function
    - `format` parameter: `"beginner_mini"` or `"beginner_short"`
    - Format-specific checks: session count (1 for mini, 4 for short), vocab count range (3-5 for mini, 8-10 for short)
    - Forbidden activities: `writingParagraph` and `vocabLevel3` forbidden in ALL beginner formats; `vocabLevel1` and `vocabLevel2` additionally forbidden in `beginner_mini`
    - Shared checks: top-level structure (title, description, preview.text, contentTypeTags, learningSessions), session structure (title, non-empty activities), activity structure (activityType not type, valid values, title, description, data as dict), vocabList format (array of strings, field name vocabList not words — NO lowercase enforcement for Korean Hangul), flashcard consistency (viewFlashcards/speakFlashcards identical vocabList in same session), writingSentence structure (data.vocabList, data.items with prompt and targetVocab), strip-keys exclusion (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId)
    - Raise `ValueError` with specific violation message identifying the rule, location (session/activity index), and expected vs actual value
    - _Requirements: 1.3, 1.4, 1.5, 1.6, 3.4, 3.5, 3.6, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 10.10_


  - [x] 1.2 Write property test: Valid content passes validation (Property 1)
    - **Property 1: Valid content passes validation**
    - Use `hypothesis` to generate well-formed curriculum content dicts matching each of the 2 formats (correct session count, vocab count within range, all required fields, no forbidden activities, no strip keys, vocabList as arrays of Korean Hangul strings) and verify `validate(content, format)` returns without exception
    - **Validates: Requirements 1.3, 1.4, 1.5, 10.1, 10.2, 10.3, 10.4**

  - [x] 1.3 Write property test: Forbidden activities rejected per format (Property 2)
    - **Property 2: Forbidden activities are rejected per format**
    - Use `hypothesis` to inject `writingParagraph` or `vocabLevel3` into any beginner curriculum and verify rejection; additionally inject `vocabLevel1`/`vocabLevel2` into `beginner_mini` format and verify rejection
    - **Validates: Requirements 3.4, 3.5, 3.6, 10.9**

  - [x] 1.4 Write property test: Strip keys rejected anywhere in JSON tree (Property 3)
    - **Property 3: Strip keys are rejected anywhere in the JSON tree**
    - Use `hypothesis` to inject strip keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) at random depths in curriculum JSON and verify rejection with message mentioning the strip key
    - **Validates: Requirements 1.6, 10.8**

  - [x] 1.5 Write property test: Activities missing required fields rejected (Property 4)
    - **Property 4: Activities missing required fields are rejected**
    - Use `hypothesis` to generate activities missing `activityType`, `title`, `description`, or `data`, or with `data` not being a dict, and verify rejection identifying the missing field
    - **Validates: Requirements 9.1, 9.5, 10.3**

  - [x] 1.6 Write property test: Invalid activityType values rejected (Property 5)
    - **Property 5: Invalid activityType values are rejected**
    - Use `hypothesis` to generate activities with `activityType` values not in the valid set (introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence) and verify rejection
    - **Validates: Requirements 9.2, 10.4**

  - [x] 1.7 Write property test: vocabList format enforced (Property 6)
    - **Property 6: vocabList format is enforced**
    - Use `hypothesis` to generate vocab activities with non-array vocabList, empty vocabList, non-string elements, or field name `words` instead of `vocabList`, and verify rejection. Note: lowercase is NOT enforced for Korean Hangul vocabulary
    - **Validates: Requirements 9.3, 10.5**

  - [x] 1.8 Write property test: Flashcard vocabList consistency (Property 7)
    - **Property 7: Flashcard vocabList consistency within sessions**
    - Use `hypothesis` to generate sessions with mismatched viewFlashcards/speakFlashcards vocabList arrays and verify rejection
    - **Validates: Requirements 9.4, 10.6**

  - [x] 1.9 Write property test: writingSentence structure enforced (Property 8)
    - **Property 8: writingSentence structure is enforced**
    - Use `hypothesis` to generate writingSentence activities with missing data.vocabList, missing/empty data.items, or items lacking prompt/targetVocab, and verify rejection
    - **Validates: Requirements 9.6, 10.7**

- [x] 2. Checkpoint — Content validator ready
  - Ensure all tests pass, ask the user if questions arise.

- [x] 3. Create orchestrator and collection/series infrastructure
  - [x] 3.1 Create `vi-ko-beginner-curriculums/orchestrator.py`
    - Create 1 collection: "Tiếng Hàn Cho Người Mới Bắt Đầu" with neutral informative Vietnamese description
    - Create 3 series: "Những Bước Đầu Tiên" (description tone: `bold_declaration`, ≤255 chars), "Khám Phá Cuộc Sống" (description tone: `empathetic_observation`, ≤255 chars), "Mở Rộng Thế Giới" (description tone: `vivid_scenario`, ≤255 chars)
    - Wire all 3 series to the collection via `add_series_to_collection`
    - Set display orders for all 3 series via `set_series_display_order`
    - Hard-code the tone assignment table from the design (all 20 curriculum description tones and farewell tones) and print it for reference
    - Log collection ID and all 3 series IDs to stdout
    - Uses root-level `api_helpers.py` via sys.path: `create_collection`, `create_series`, `add_series_to_collection`, `set_series_display_order`
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 11.2, 11.3, 11.4, 11.5, 15.1_


- [x] 4. Create beginner mini curriculum scripts (8 scripts, Series 1: "Những Bước Đầu Tiên")
  - [x] 4.1 Create `vi-ko-beginner-curriculums/create_greetings.py` — "Chào Hỏi Cơ Bản"
    - Beginner mini format: 1 session, 5 words, price 9
    - vocabList: ["안녕하세요", "감사합니다", "죄송합니다", "안녕히 가세요", "네"]
    - Activity sequence: introAudio (welcome + teach all 5 words with Revised Romanization, Vietnamese meaning, cultural context, 200-350 words) → viewFlashcards → speakFlashcards → reading (40-60 characters, simple Korean passage in Hangul) → speakReading → readAlong → introAudio (farewell with vocab review and encouragement, 200-400 words)
    - Description tone: `provocative_question`, farewell tone: `warm_accountability`
    - Preview: ~100-150 words Vietnamese Persuasive_Copy with vivid hooks about Korean greetings
    - All text hand-crafted, no templates. Vietnamese marketing text for adults, bilingual learner content with Revised Romanization
    - Validate with `validate(content, "beginner_mini")` before upload
    - Display order: 1 in series
    - _Requirements: 1.1, 1.3, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 5.1, 5.2, 5.3, 5.4, 5.7, 6.1, 6.4, 6.5, 6.6, 6.7, 7.1, 9.1, 9.2, 9.3, 9.4, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 4.2 Create `vi-ko-beginner-curriculums/create_numbers.py` — "Đếm Số Tiếng Hàn"
    - Beginner mini format: 1 session, 5 words, price 9
    - vocabList: ["일", "이", "삼", "사", "오"]
    - Same activity sequence as 4.1 but all content hand-crafted for numbers topic
    - Description tone: `vivid_scenario`, farewell tone: `quiet_awe`
    - Display order: 2 in series
    - _Requirements: 1.1, 1.3, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 5.1, 5.2, 5.3, 5.4, 5.7, 6.1, 6.4, 6.5, 6.6, 6.7, 7.1, 9.1, 9.2, 9.3, 9.4, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 4.3 Create `vi-ko-beginner-curriculums/create_family.py` — "Gia Đình Thân Yêu"
    - Beginner mini format: 1 session, 5 words, price 9
    - vocabList: ["어머니", "아버지", "형", "언니", "동생"]
    - Same activity sequence as 4.1 but all content hand-crafted for family topic
    - Description tone: `empathetic_observation`, farewell tone: `practical_momentum`
    - Display order: 3 in series
    - _Requirements: 1.1, 1.3, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 5.1, 5.2, 5.3, 5.4, 5.7, 6.1, 6.4, 6.5, 6.6, 6.7, 7.1, 9.1, 9.2, 9.3, 9.4, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 4.4 Create `vi-ko-beginner-curriculums/create_colors.py` — "Màu Sắc Quanh Ta"
    - Beginner mini format: 1 session, 5 words, price 9
    - vocabList: ["빨간색", "파란색", "하얀색", "검은색", "노란색"]
    - Same activity sequence as 4.1 but all content hand-crafted for colors topic
    - Description tone: `surprising_fact`, farewell tone: `introspective_guide`
    - Display order: 4 in series
    - _Requirements: 1.1, 1.3, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 5.1, 5.2, 5.3, 5.4, 5.7, 6.1, 6.4, 6.5, 6.6, 6.7, 7.1, 9.1, 9.2, 9.3, 9.4, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 4.5 Create `vi-ko-beginner-curriculums/create_weather.py` — "Thời Tiết Hôm Nay"
    - Beginner mini format: 1 session, 5 words, price 9
    - vocabList: ["날씨", "비", "맑음", "흐림", "바람"]
    - Same activity sequence as 4.1 but all content hand-crafted for weather topic
    - Description tone: `bold_declaration`, farewell tone: `team_building_energy`
    - Display order: 5 in series
    - _Requirements: 1.1, 1.3, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 5.1, 5.2, 5.3, 5.4, 5.7, 6.1, 6.4, 6.5, 6.6, 6.7, 7.1, 9.1, 9.2, 9.3, 9.4, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 4.6 Create `vi-ko-beginner-curriculums/create_drinks.py` — "Đồ Uống Yêu Thích"
    - Beginner mini format: 1 session, 5 words, price 9
    - vocabList: ["물", "차", "커피", "우유", "주스"]
    - Same activity sequence as 4.1 but all content hand-crafted for drinks topic
    - Description tone: `metaphor_led`, farewell tone: `warm_accountability`
    - Display order: 6 in series
    - _Requirements: 1.1, 1.3, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 5.1, 5.2, 5.3, 5.4, 5.7, 6.1, 6.4, 6.5, 6.6, 6.7, 7.1, 9.1, 9.2, 9.3, 9.4, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 4.7 Create `vi-ko-beginner-curriculums/create_days.py` — "Ngày Trong Tuần"
    - Beginner mini format: 1 session, 5 words, price 9
    - vocabList: ["월요일", "화요일", "수요일", "목요일", "금요일"]
    - Same activity sequence as 4.1 but all content hand-crafted for days of the week topic
    - Description tone: `provocative_question`, farewell tone: `quiet_awe`
    - Display order: 7 in series
    - _Requirements: 1.1, 1.3, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 5.1, 5.2, 5.3, 5.4, 5.7, 6.1, 6.4, 6.5, 6.6, 6.7, 7.1, 9.1, 9.2, 9.3, 9.4, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 4.8 Create `vi-ko-beginner-curriculums/create_emotions.py` — "Cảm Xúc Mỗi Ngày"
    - Beginner mini format: 1 session, 5 words, price 9
    - vocabList: ["행복하다", "슬프다", "즐겁다", "피곤하다", "좋다"]
    - Same activity sequence as 4.1 but all content hand-crafted for emotions topic
    - Description tone: `empathetic_observation`, farewell tone: `practical_momentum`
    - Display order: 8 in series
    - _Requirements: 1.1, 1.3, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 5.1, 5.2, 5.3, 5.4, 5.7, 6.1, 6.4, 6.5, 6.6, 6.7, 7.1, 9.1, 9.2, 9.3, 9.4, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_


- [x] 5. Create beginner short curriculum scripts (6 scripts, Series 2: "Khám Phá Cuộc Sống")
  - [x] 5.1 Create `vi-ko-beginner-curriculums/create_food.py` — "Ẩm Thực Hàn Quốc"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["밥", "김치", "고기", "야채", "계란", "된장찌개", "비빔밥", "라면", "맛있다", "잘 먹겠습니다"]
    - Session 1 ("Phần 1"): introAudio (welcome + teach group 1 with Revised Romanization and Vietnamese meaning) → viewFlashcards (group 1) → speakFlashcards (group 1) → vocabLevel1 (group 1) → reading (60-80 characters, Korean passage using group 1 words) → readAlong → introAudio (session wrap-up)
    - Session 2 ("Phần 2"): introAudio (recap group 1 + teach group 2) → viewFlashcards (group 2) → speakFlashcards (group 2) → vocabLevel1 (group 2) → reading (60-80 characters) → readAlong → introAudio (session wrap-up)
    - Session 3 ("Ôn tập"): introAudio → viewFlashcards (all) → speakFlashcards (all) → vocabLevel1 (all) → vocabLevel2 (all) → writingSentence (3-4 items with Vietnamese prompts, Korean example sentences with Revised Romanization, 1-word substitution pattern) → introAudio (review wrap-up)
    - Session 4 ("Đọc tổng hợp"): introAudio → reading (100-140 characters, combined passage) → speakReading → readAlong → writingSentence (2-3 items) → introAudio (farewell with full vocab review and celebration)
    - Description tone: `bold_declaration`, farewell tone: `introspective_guide`
    - All text hand-crafted. Vietnamese marketing text for adults, bilingual learner content with Revised Romanization
    - Validate with `validate(content, "beginner_short")` before upload
    - Display order: 1 in series
    - _Requirements: 1.1, 1.4, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.2, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 5.2 Create `vi-ko-beginner-curriculums/create_shopping.py` — "Mua Sắm Ở Hàn Quốc"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["가게", "얼마예요", "비싸다", "싸다", "사다", "돈", "카드", "봉투", "예쁘다", "크다"]
    - Same 4-session structure as 5.1 but all content hand-crafted for shopping topic
    - Description tone: `surprising_fact`, farewell tone: `team_building_energy`
    - Display order: 2 in series
    - _Requirements: 1.1, 1.4, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.2, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 5.3 Create `vi-ko-beginner-curriculums/create_transport.py` — "Di Chuyển Ở Hàn Quốc"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["지하철", "버스", "역", "표", "택시", "공항", "왼쪽", "오른쪽", "직진", "내리다"]
    - Same 4-session structure as 5.1 but all content hand-crafted for transportation topic
    - Description tone: `vivid_scenario`, farewell tone: `warm_accountability`
    - Display order: 3 in series
    - _Requirements: 1.1, 1.4, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.2, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 5.4 Create `vi-ko-beginner-curriculums/create_hotel.py` — "Khách Sạn Và Lưu Trú"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["호텔", "방", "예약", "체크인", "열쇠", "화장실", "아침 식사", "하루", "프런트", "짐"]
    - Same 4-session structure as 5.1 but all content hand-crafted for hotel/accommodation topic
    - Description tone: `provocative_question`, farewell tone: `quiet_awe`
    - Display order: 4 in series
    - _Requirements: 1.1, 1.4, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.2, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 5.5 Create `vi-ko-beginner-curriculums/create_office.py` — "Văn Phòng Hàn Quốc"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["일", "회사", "회의", "전화", "이메일", "시간", "휴가", "사장님", "동료", "수고하셨습니다"]
    - Same 4-session structure as 5.1 but all content hand-crafted for office/work topic
    - Description tone: `metaphor_led`, farewell tone: `practical_momentum`
    - Display order: 5 in series
    - _Requirements: 1.1, 1.4, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.2, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 5.6 Create `vi-ko-beginner-curriculums/create_seasons.py` — "Bốn Mùa Hàn Quốc"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["봄", "여름", "가을", "겨울", "벚꽃", "단풍", "눈", "바다", "산", "꽃"]
    - Same 4-session structure as 5.1 but all content hand-crafted for seasons/nature topic
    - Description tone: `empathetic_observation`, farewell tone: `introspective_guide`
    - Display order: 6 in series
    - _Requirements: 1.1, 1.4, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.2, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

- [x] 6. Checkpoint — Series 1 and Series 2 done
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 8 curriculums exist in Series 1 with correct display orders 1-8
  - Verify 6 curriculums exist in Series 2 with correct display orders 1-6
  - Verify prices: 8 mini at 9, 6 short at 19


- [x] 7. Create beginner short curriculum scripts (6 scripts, Series 3: "Mở Rộng Thế Giới")
  - [x] 7.1 Create `vi-ko-beginner-curriculums/create_hobbies.py` — "Sở Thích Và Giải Trí"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["취미", "영화", "음악", "여행", "독서", "운동", "요리", "산책", "사진", "노래방"]
    - Same 4-session structure as 5.1 but all content hand-crafted for hobbies/entertainment topic
    - Description tone: `surprising_fact`, farewell tone: `team_building_energy`
    - Display order: 1 in series
    - _Requirements: 1.1, 1.4, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.2, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 7.2 Create `vi-ko-beginner-curriculums/create_health.py` — "Sức Khỏe Và Cơ Thể"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["머리", "배", "병원", "약", "아프다", "열", "쉬다", "몸", "건강", "의사"]
    - Same 4-session structure as 5.1 but all content hand-crafted for health/body topic
    - Description tone: `bold_declaration`, farewell tone: `warm_accountability`
    - Display order: 2 in series
    - _Requirements: 1.1, 1.4, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.2, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 7.3 Create `vi-ko-beginner-curriculums/create_housing.py` — "Nhà Ở Hàn Quốc"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["집", "부엌", "거실", "창문", "문", "에어컨", "온돌", "이사", "냉장고", "세탁기"]
    - Same 4-session structure as 5.1 but all content hand-crafted for housing topic
    - Description tone: `vivid_scenario`, farewell tone: `quiet_awe`
    - Display order: 3 in series
    - _Requirements: 1.1, 1.4, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.2, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 7.4 Create `vi-ko-beginner-curriculums/create_culture.py` — "Văn Hóa Hàn Quốc"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["한복", "설날", "추석", "김장", "찜질방", "소주", "삼겹살", "한류", "드라마", "케이팝"]
    - Same 4-session structure as 5.1 but all content hand-crafted for Korean culture topic
    - Description tone: `provocative_question`, farewell tone: `practical_momentum`
    - Display order: 4 in series
    - _Requirements: 1.1, 1.4, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.2, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 7.5 Create `vi-ko-beginner-curriculums/create_technology.py` — "Công Nghệ Đời Thường"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["핸드폰", "인터넷", "컴퓨터", "앱", "편의점", "배달", "카카오톡", "와이파이", "충전", "검색"]
    - Same 4-session structure as 5.1 but all content hand-crafted for technology topic
    - Description tone: `empathetic_observation`, farewell tone: `introspective_guide`
    - Display order: 5 in series
    - _Requirements: 1.1, 1.4, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.2, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

  - [x] 7.6 Create `vi-ko-beginner-curriculums/create_sports.py` — "Thể Thao Và Vận Động"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["축구", "야구", "수영", "달리기", "걷기", "자전거", "태권도", "경기", "이기다", "연습"]
    - Same 4-session structure as 5.1 but all content hand-crafted for sports topic
    - Description tone: `metaphor_led`, farewell tone: `team_building_energy`
    - Display order: 6 in series
    - _Requirements: 1.1, 1.4, 2.1, 2.4, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 4.2, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 7.2, 9.1, 9.2, 9.3, 9.4, 9.6, 9.7, 11.1, 11.6, 12.1, 13.1, 13.2, 13.3, 13.4_

- [x] 8. Checkpoint — All 20 curriculums created
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 8 curriculums in Series 1 ("Những Bước Đầu Tiên") with display orders 1-8
  - Verify 6 curriculums in Series 2 ("Khám Phá Cuộc Sống") with display orders 1-6
  - Verify 6 curriculums in Series 3 ("Mở Rộng Thế Giới") with display orders 1-6
  - Verify prices: 8 mini at 9, 12 short at 19
  - Verify language pair: all curriculums have `language="ko"`, `userLanguage="vi"`
  - Run duplicate check queries for all 20 curriculum titles


- [x] 9. Documentation and cleanup
  - [x] 9.1 Create `vi-ko-beginner-curriculums/README.md`
    - Document: collection ID, series IDs, all 20 curriculum IDs with titles and display orders
    - Document: vocabulary lists per curriculum, tone assignments (description and farewell for all 20)
    - Document: pricing (9 for mini, 19 for short), language pair (vi-ko)
    - Include SQL verification queries: count curriculums, verify language pair, verify prices, verify series membership and display orders, verify no duplicates, verify collection → series wiring
    - Include recreation instructions
    - _Requirements: 14.1_

  - [x] 9.2 Delete all creation scripts after verification
    - Delete `orchestrator.py`, all 20 `create_*.py` scripts, and `validate_content.py` from `vi-ko-beginner-curriculums/`
    - Only `README.md` remains in the directory
    - _Requirements: 14.2_

  - [x] 9.3 Run duplicate check and resolve
    - Run duplicate check query for each of the 20 curriculum titles
    - If duplicates found: keep earliest, remove from series first, then delete extras
    - _Requirements: 14.3_

- [x] 10. Final checkpoint — All tasks complete
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 20 curriculums total: 8 mini + 12 short
  - Verify collection and series structure is correct (1 collection, 3 series)
  - Verify README.md is in place and all creation scripts are deleted
  - Verify no `setPublic` calls were made (all curriculums remain private)

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation between phases
- Property tests validate the beginner-specific content validator (Properties 1-8) from the design
- The `validate_content.py` is beginner-specific — key difference from children's validator: NO lowercase enforcement for vocabList since Korean Hangul has no case distinction
- Root-level `api_helpers.py` is reused as-is — no changes needed
- All curriculum content must be hand-crafted — no template-based generation
- Two formats: beginner_mini (1 session, 3-5 words, price 9), beginner_short (4 sessions, 8-10 words, price 19)
- Vietnamese session titles: "Phần 1", "Phần 2", "Ôn tập", "Đọc tổng hợp" (for short format)
- All marketing text (title, description, preview) in Vietnamese targeting adult learners
- All learner-facing content (introAudio, reading, writing prompts) bilingual with warm encouraging tone, Revised Romanization pronunciation guidance
- No vocabulary overlap across the 20 curriculums
- Korean vocabulary in Hangul only — no Hanja for beginners
- Reading passage length measured in characters (40-60 for mini, 60-80 per session for short, 100-140 for final session)
- Tone distribution across 20 descriptions: provocative_question ×4, vivid_scenario ×3, empathetic_observation ×4, surprising_fact ×3, bold_declaration ×3, metaphor_led ×3 — max 20%, all ≤30% ✓
- No adjacent tone duplicates within any of the 3 series ✓
- Farewell tone distribution: warm_accountability ×4, quiet_awe ×4, practical_momentum ×4, introspective_guide ×4, team_building_energy ×4 — evenly distributed (20% each) ✓
