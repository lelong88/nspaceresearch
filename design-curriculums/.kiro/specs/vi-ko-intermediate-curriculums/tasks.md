# Implementation Plan: Vietnamese-Korean Intermediate/Upper-Intermediate Curriculums

## Overview

Create 20 Korean-learning curriculums for Vietnamese-speaking adults at intermediate and upper-intermediate levels, organized into 1 collection ("Tiếng Hàn Trung Cao Cấp") and 4 series. Language pair: `userLanguage="vi"`, `language="ko"`.

Implementation uses Python scripts in `vi-ko-intermediate-curriculums/`. Two curriculum formats: intermediate (5 sessions, 18 words in 3 groups of 6, vocabLevel3 in Session 4, writingParagraph in Session 5, reading 200-350 chars/session + 500-800 final, price 49) and upper_intermediate (5 sessions, 18 words in 3 groups of 6, vocabLevel3 in Session 4, writingParagraph in Session 5, reading 300-500 chars/session + 600-1000 final, price 49). Each curriculum gets its own standalone script with hand-crafted content including Hangul with Revised Romanization. A format-aware `validate_content.py` enforces rules before upload. The shared root-level `api_helpers.py` handles all API calls.

Execution order: (1) content validator + property tests, (2) orchestrator for collection/series, (3) intermediate scripts ×10, (4) upper-intermediate scripts ×10, (5) verification, (6) README + cleanup.

## Tasks

- [x] 1. Create intermediate/upper-intermediate content validator
  - [x] 1.1 Create `vi-ko-intermediate-curriculums/validate_content.py` with format-aware `validate(content, format)` function
    - `format` parameter: `"intermediate"` or `"upper_intermediate"`
    - Both formats require: session count = exactly 5; vocab count = exactly 18 (3 groups of 6); vocabLevel3 ONLY in Session 4 (required); writingParagraph ONLY in Session 5 (required)
    - Shared checks: top-level structure (title, description, preview.text, contentTypeTags: [], learningSessions), session structure (title, non-empty activities), activity structure (activityType not type, valid values, title, description, data as dict), vocabList format (array of strings, field name vocabList not words — NO lowercase enforcement for Korean Hangul), flashcard consistency (viewFlashcards/speakFlashcards identical vocabList in same session), writingSentence structure (data.vocabList, data.items with prompt and targetVocab), writingParagraph structure (data.vocabList, data.instructions, data.prompts array with >=2 items), strip-keys exclusion (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId)
    - Total unique vocab count = 18 across all sessions
    - vocabLevel3 IS PRESENT in Session 4 (required, not just allowed)
    - writingParagraph IS PRESENT in Session 5 (required, not just allowed)
    - Raise `ValueError` with specific violation message identifying the rule, location (session/activity index), format, and expected vs actual value
    - _Requirements: 1.3, 1.4, 1.5, 1.6, 1.8, 1.9, 1.10, 1.11, 9.6_

  - [x] 1.2 Write property test: Valid content passes validation (Property 1)
    - **Property 1: Valid content passes validation**
    - Use `hypothesis` to generate well-formed curriculum content dicts matching each of the 2 formats (exactly 5 sessions, 18 vocab words in 3 groups of 6, all required fields, vocabLevel3 in Session 4, writingParagraph in Session 5, no strip keys, vocabList as arrays of Korean strings) and verify `validate(content, format)` returns without exception
    - **Validates: Requirements 1.3, 1.4, 1.5, 1.8, 1.9, 1.10, 1.11**

  - [x] 1.3 Write property test: Strip keys rejected anywhere in JSON tree (Property 2)
    - **Property 2: Strip keys are rejected anywhere in the JSON tree**
    - Use `hypothesis` to inject strip keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) at random depths in curriculum JSON and verify rejection with message mentioning the strip key
    - **Validates: Requirements 1.6**

  - [x] 1.4 Write property test: Activity placement enforced (Property 3)
    - **Property 3: Activity placement is enforced**
    - Use `hypothesis` to test: (a) vocabLevel3 in wrong session raises ValueError, (b) writingParagraph in wrong session raises ValueError, (c) vocabLevel3 missing from Session 4 raises ValueError, (d) writingParagraph missing from Session 5 raises ValueError
    - **Validates: Requirements 1.8, 1.9, 1.10, 1.11, 4.2, 4.3, 5.2, 5.3**

  - [x] 1.5 Write property test: Activities missing required fields rejected (Property 4)
    - **Property 4: Activities missing required fields are rejected**
    - Use `hypothesis` to generate activities missing `activityType`, `title`, `description`, or `data`, or with `data` not being a dict, and verify rejection identifying the missing field and its location
    - **Validates: Requirements 9.6**

  - [x] 1.6 Write property test: Invalid activityType values rejected (Property 5)
    - **Property 5: Invalid activityType values are rejected**
    - Use `hypothesis` to generate activities with `activityType` values not in the valid set (introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence, writingParagraph) and verify rejection
    - **Validates: Requirements 9.6**

  - [x] 1.7 Write property test: vocabList format enforced (Property 6)
    - **Property 6: vocabList format is enforced**
    - Use `hypothesis` to generate vocab activities with non-array vocabList, empty vocabList, non-string elements, or field name `words` instead of `vocabList`, and verify rejection. Note: lowercase is NOT enforced for Korean vocabulary (Hangul has no case)
    - **Validates: Requirements 9.6**

  - [x] 1.8 Write property test: Flashcard vocabList consistency (Property 7)
    - **Property 7: Flashcard vocabList consistency within sessions**
    - Use `hypothesis` to generate sessions with mismatched viewFlashcards/speakFlashcards vocabList arrays and verify rejection
    - **Validates: Requirements 9.6**

  - [x] 1.9 Write property test: Writing activity structure enforced (Property 8)
    - **Property 8: Writing activity structure is enforced**
    - Use `hypothesis` to generate: (a) writingSentence activities with missing data.vocabList, missing/empty data.items, or items lacking prompt/targetVocab and verify rejection; (b) writingParagraph activities with missing data.vocabList, missing/empty data.instructions, or data.prompts with fewer than 2 items and verify rejection
    - **Validates: Requirements 9.6**

- [x] 2. Checkpoint — Content validator ready
  - Ensure all tests pass, ask the user if questions arise.

- [x] 3. Create orchestrator and collection/series infrastructure
  - [x] 3.1 Create `vi-ko-intermediate-curriculums/orchestrator.py`
    - Create 1 collection: "Tiếng Hàn Trung Cao Cấp" with neutral informative Vietnamese description about intermediate/upper-intermediate Korean for Vietnamese adults covering business, culture, society, lifestyle, and intellectual topics
    - Create 4 series with descriptions ≤255 chars each using different Tone_Palette types:
      - Series 1: "Kinh Doanh Và Sự Nghiệp" (tone: `bold_declaration`) — Curriculums 1, 8, 12
      - Series 2: "Văn Hóa Và Xã Hội" (tone: `empathetic_observation`) — Curriculums 2, 5, 6, 14, 17
      - Series 3: "Đời Sống Và Xu Hướng" (tone: `vivid_scenario`) — Curriculums 3, 4, 7, 9, 13, 16
      - Series 4: "Tri Thức Và Tư Tưởng" (tone: `provocative_question`) — Curriculums 10, 11, 15, 18, 19, 20
    - Wire all 4 series to the collection via `add_series_to_collection`
    - Set display orders for all 4 series via `set_series_display_order`
    - Hard-code the tone assignment table from the design (all 20 curriculum description tones and farewell tones) and print it for reference
    - Log collection ID and all 4 series IDs to stdout
    - Uses root-level `api_helpers.py` via sys.path: `create_collection`, `create_series`, `add_series_to_collection`, `set_series_display_order`
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7_

  - [x] 3.2 Run `orchestrator.py` and record collection/series IDs
    - Execute the orchestrator script
    - Record the collection ID and all 4 series IDs for use in curriculum scripts
    - Verify collection and series created successfully via database query
    - _Requirements: 8.1, 8.2, 8.3, 8.4_

- [x] 4. Checkpoint — Infrastructure ready
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 1 collection and 4 series exist in database
  - Verify series are wired to collection with correct display orders

- [x] 5. Create intermediate curriculum scripts (10 scripts)
  - [x] 5.1 Create `vi-ko-intermediate-curriculums/create_business_strategy.py` — "Đầu Tư Và Chiến Lược Kinh Doanh" (Series 1: Kinh Doanh Và Sự Nghiệp, display order 1)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["전략", "리더십", "의사결정", "시장점유율", "경쟁력", "혁신", "인수합병", "주주", "이사회", "실적", "수익성", "비전", "목표설정", "위기관리", "조직문화", "성장전략", "사업확장", "지속가능경영"]
    - Session structure: S1-S3 (learning with introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, introAudio grammar, reading 200-350 chars, speakReading, readAlong, writingSentence ×3), S4 (review with all 18 words, vocabLevel1+2+3, writingSentence ×4-5), S5 (final reading 500-800 chars, writingParagraph using 6+ vocab words, farewell introAudio)
    - Description tone: `provocative_question`, farewell tone: `warm_accountability`
    - All text hand-crafted: Vietnamese persuasive marketing copy, Korean reading passages in Hangul (TOPIK II level 3-4), introAudio scripts teaching each word with Revised Romanization/Vietnamese meaning/example sentences, writingParagraph with Vietnamese instructions and >=2 guiding questions
    - Validate with `validate(content, "intermediate")` before upload
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

  - [x] 5.2 Create `vi-ko-intermediate-curriculums/create_korean_history.py` — "Đại Hàn Và Lịch Sử" (Series 2: Văn Hóa Và Xã Hội, display order 1)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["왕조", "세종대왕", "한글창제", "임진왓란", "독립운동", "식민지", "광복", "전쟁", "휴전", "분단", "통일", "민주화", "유산", "문화재", "유네스코", "고궁", "사극", "역사적"]
    - Description tone: `surprising_fact`, farewell tone: `introspective_guide`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

  - [x] 5.3 Create `vi-ko-intermediate-curriculums/create_beauty_skincare.py` — "Làm Đẹp Và Skincare Hàn Quốc" (Series 3: Đời Sống Và Xu Hướng, display order 1)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["화장품", "스킨케어", "성분", "보습", "미백", "주름", "항산화", "자외선", "선크림", "세럼", "토너", "에센스", "피부과", "시술", "필러", "보톡스", "매출", "트렌드"]
    - Description tone: `bold_declaration`, farewell tone: `introspective_guide`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

  - [x] 5.4 Create `vi-ko-intermediate-curriculums/create_fine_dining.py` — "Ẩm Thực Cao Cấp Hàn Quốc" (Series 3: Đời Sống Và Xu Hướng, display order 2)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["한정식", "반찬", "발효", "숙성", "제철", "산지직송", "맛집", "미슐린", "셀프", "조리법", "담금질", "숙성도", "향신료", "식감", "플레이팅", "페어링", "식도락", "맛평가"]
    - Description tone: `vivid_scenario`, farewell tone: `team_building_energy`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

  - [x] 5.5 Create `vi-ko-intermediate-curriculums/create_social_issues.py` — "Xã Hội Hàn Quốc Hiện Đại" (Series 2: Văn Hóa Và Xã Hội, display order 2)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["고령화사회", "저출산", "성평등", "워라밸", "청년실업", "주거비", "격차", "다문화", "인권", "차별", "세대갈등", "사회복지", "빈부격차", "정신건강", "과로사회", "사회안전망", "공정성", "양극화"]
    - Description tone: `empathetic_observation`, farewell tone: `team_building_energy`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

  - [x] 5.6 Create `vi-ko-intermediate-curriculums/create_korean_arts.py` — "Nghệ Thuật Hàn Quốc" (Series 2: Văn Hóa Và Xã Hội, display order 3)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["전통음악", "판소리", "가야금", "한복", "수묵화", "도예", "영화제", "감독", "독립영화", "한류", "미술관", "전시회", "설치미술", "현대미술", "문화예술", "창작", "예술가", "미학"]
    - Description tone: `metaphor_led`, farewell tone: `warm_accountability`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

  - [x] 5.7 Create `vi-ko-intermediate-curriculums/create_education_system.py` — "Hệ Thống Giáo Dục Hàn Quốc" (Series 3: Đời Sống Và Xu Hướng, display order 3)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["입시", "수능", "사교육", "과외", "입시지옥", "성적지상주의", "입시전쟁", "야자", "재수", "학벌", "스펙", "취업률", "장학생", "유학생", "교육개혁", "창의력", "인성교육", "진로상담"]
    - Description tone: `empathetic_observation`, farewell tone: `warm_accountability`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

  - [x] 5.8 Create `vi-ko-intermediate-curriculums/create_real_estate.py` — "Bất Động Sản Và Đầu Tư Tại Hàn Quốc" (Series 1: Kinh Doanh Và Sự Nghiệp, display order 2)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["아파트", "재건축", "재개발", "투기", "규제", "대출규제", "양도세", "청약", "분양", "전세사기", "시세", "호가", "매매", "중개수수료", "등기", "담보대출", "갑투", "주택정책"]
    - Description tone: `vivid_scenario`, farewell tone: `quiet_awe`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

  - [x] 5.9 Create `vi-ko-intermediate-curriculums/create_media_journalism.py` — "Truyền Thông Và Báo Chí Hàn Quốc" (Series 3: Đời Sống Và Xu Hướng, display order 4)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["언론", "기사", "특종", "속보", "여론조작", "가짜뉴스", "언론의자유", "편향보도", "팔로워", "구독자", "유튜버", "인플루언서", "댓글", "알고리즘", "조회수", "매체", "신뢰도", "필력"]
    - Description tone: `surprising_fact`, farewell tone: `quiet_awe`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

  - [x] 5.10 Create `vi-ko-intermediate-curriculums/create_philosophy_confucianism.py` — "Triết Học Và Giá Trị Nho Giáo" (Series 4: Tri Thức Và Tư Tưởng, display order 1)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["유교", "효도", "예의", "충", "인", "의", "지", "신", "선비", "유교적", "위계질서", "존경", "겦손", "조화", "도덕", "양심", "수양", "선비정신"]
    - Description tone: `metaphor_led`, farewell tone: `team_building_energy`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

- [x] 6. Run intermediate curriculum scripts
  - Execute all 10 intermediate curriculum scripts (5.1–5.10) against the API
  - Each script validates content, creates curriculum, adds to series, sets display order, sets price to 49
  - Record all 10 curriculum IDs
  - Verify no `setPublic` calls made
  - _Requirements: 9.3, 9.4, 9.5, 9.6, 9.8, 10.1, 10.2_

- [x] 7. Checkpoint — Intermediate curriculums done
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 10 intermediate curriculums created with correct series assignments
  - Verify all prices set to 49
  - Verify vocabLevel3 in Session 4 and writingParagraph in Session 5 for all 10
  - Verify language pair: all have `language="ko"`, `userLanguage="vi"`

- [x] 8. Create upper-intermediate curriculum scripts (10 scripts)
  - [x] 8.1 Create `vi-ko-intermediate-curriculums/create_fashion_design.py` — "Thời Trang Và Thiết Kế Hàn Quốc" (Series 4: Tri Thức Và Tư Tưởng, display order 2)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["패션산업", "디자이너", "컨렉션", "패션위크", "브랜드", "럭셔리", "패스트패션", "지속가능패션", "트렌드", "스타일링", "모델", "런웨이", "텍스타일", "봄콜레션", "신진디자이너", "동대문", "한복디자인", "문화상품"]
    - Session structure: S1-S3 (learning with introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, introAudio grammar, reading 300-500 chars with TOPIK II level 4-5, speakReading, readAlong, writingSentence ×3), S4 (review with all 18 words, vocabLevel1+2+3, writingSentence ×4-5), S5 (final reading 600-1000 chars, writingParagraph using 8+ vocab words with analytical/argumentative prompts, farewell introAudio)
    - Description tone: `bold_declaration`, farewell tone: `warm_accountability`
    - All text hand-crafted: Vietnamese persuasive marketing copy, Korean reading passages in Hangul (TOPIK II level 4-5 with complex grammar and idiomatic expressions), introAudio scripts teaching each word with Revised Romanization/Vietnamese meaning/example sentences, writingParagraph with Vietnamese instructions and >=2 analytical guiding questions
    - Validate with `validate(content, "upper_intermediate")` before upload
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 3.1, 3.3, 3.4, 3.5, 3.6, 3.8, 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

  - [x] 8.2 Create `vi-ko-intermediate-curriculums/create_startup_ecosystem.py` — "Hệ Sinh Thái Startup Hàn Quốc" (Series 1: Kinh Doanh Và Sự Nghiệp, display order 3)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["창업", "유니콘", "투자유치", "벤처케피털", "엑셀러레이터", "사업계획서", "피벗팅", "스케일업", "엑시트", "기업공개", "판교", "스타트업생태계", "실패", "재도전", "기업가정신", "혁신기술", "인재영입", "시장조사"]
    - Description tone: `bold_declaration`, farewell tone: `practical_momentum`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 3.1, 3.3, 3.4, 3.5, 3.6, 3.8, 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

  - [x] 8.3 Create `vi-ko-intermediate-curriculums/create_sports_esports.py` — "Văn Hóa Thể Thao Và Esports" (Series 3: Đời Sống Và Xu Hướng, display order 5)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["야구", "축구", "이스포츠", "프로게이머", "리그", "우승", "팔들", "응원", "응원가", "스포츠정신", "스포츠산업", "중계", "선수생활", "은퇴", "훈련", "전술", "스포츠외교", "올림픽"]
    - Description tone: `metaphor_led`, farewell tone: `practical_momentum`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 3.1, 3.3, 3.4, 3.5, 3.6, 3.8, 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

  - [x] 8.4 Create `vi-ko-intermediate-curriculums/create_wedding_traditions.py` — "Hôn Nhân Và Truyền Thống Gia Đình" (Series 2: Văn Hóa Và Xã Hội, display order 4)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["결혼식", "폐백", "함", "예단", "신랑", "신부", "중매", "상견례", "혼수", "예식장", "주례", "축의금", "신혼여행", "제사", "차례", "효", "장남", "며느리"]
    - Description tone: `vivid_scenario`, farewell tone: `quiet_awe`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 3.1, 3.3, 3.4, 3.5, 3.6, 3.8, 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

  - [x] 8.5 Create `vi-ko-intermediate-curriculums/create_language_nuances.py` — "Sắc Thái Ngôn Ngữ Hàn Quốc" (Series 4: Tri Thức Và Tư Tưởng, display order 3)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["존댓말", "반말", "존칭", "경어", "겦양어", "신조어", "줄임말", "은어", "유행어", "사투리", "억양", "어미", "조사", "어감", "높임말", "낮춤말", "언어예절", "세대차이"]
    - Description tone: `surprising_fact`, farewell tone: `quiet_awe`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 3.1, 3.3, 3.4, 3.5, 3.6, 3.8, 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

  - [x] 8.6 Create `vi-ko-intermediate-curriculums/create_healthcare_system.py` — "Hệ Thống Y Tế Hàn Quốc" (Series 3: Đời Sống Và Xu Hướng, display order 6)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["건강보험", "국민건강보험", "의료시스템", "종합병원", "전문의", "진료비", "본인부담금", "의료관광", "성형외과", "원격진료", "응급의료", "의료분쟁", "의료사고", "환자권리", "의료윤리", "예방의학", "건강검진", "의료기술"]
    - Description tone: `provocative_question`, farewell tone: `introspective_guide`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 3.1, 3.3, 3.4, 3.5, 3.6, 3.8, 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

  - [x] 8.7 Create `vi-ko-intermediate-curriculums/create_immigration.py` — "Nhập Cư Và Xã Hội Đa Văn Hóa" (Series 2: Văn Hóa Và Xã Hội, display order 5)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["이민", "이주노동자", "다문화가정", "결혼이주여성", "영주권", "귀화", "외국인등록", "체류자격", "불법체류", "차별금지", "사회통합", "언어장벽", "문화충돌", "적응", "정체성", "공존", "포용", "외국인정책"]
    - Description tone: `provocative_question`, farewell tone: `practical_momentum`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 3.1, 3.3, 3.4, 3.5, 3.6, 3.8, 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

  - [x] 8.8 Create `vi-ko-intermediate-curriculums/create_architecture_urban.py` — "Kiến Trúc Và Đô Thị Hóa" (Series 4: Tri Thức Và Tư Tưởng, display order 4)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["건축", "도시개발", "재개발", "스마트도시", "친환경건축", "한옥보존", "공공디자인", "도시재생", "주거환경", "공원", "복합문화공간", "랜드마크", "스카이라인", "도시계획", "교통인프라", "보행자중심", "공간디자인", "지역활성화"]
    - Description tone: `vivid_scenario`, farewell tone: `practical_momentum`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 3.1, 3.3, 3.4, 3.5, 3.6, 3.8, 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

  - [x] 8.9 Create `vi-ko-intermediate-curriculums/create_korean_literature.py` — "Văn Học Hàn Quốc" (Series 4: Tri Thức Và Tư Tưởng, display order 5)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["문학", "소설", "시", "수필", "작가", "시인", "노벨문학상", "번역", "출판", "문학상", "서점", "독서", "서평", "묘사", "은유", "주제", "문체", "서사"]
    - Description tone: `empathetic_observation`, farewell tone: `introspective_guide`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 3.1, 3.3, 3.4, 3.5, 3.6, 3.8, 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

  - [x] 8.10 Create `vi-ko-intermediate-curriculums/create_traditional_medicine.py` — "Y Học Cổ Truyền Hàn Quốc" (Series 4: Tri Thức Và Tư Tưởng, display order 6)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["한의학", "한의사", "한약", "침", "뜻", "부항", "경락", "혈자리", "체질", "음양", "오행", "보약", "생약", "탕약", "인삼", "녹용", "양생", "체질개선"]
    - Description tone: `provocative_question`, farewell tone: `team_building_energy`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 3.1, 3.3, 3.4, 3.5, 3.6, 3.8, 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 9.1, 9.3, 9.4, 9.6, 9.8, 10.1_

- [x] 9. Run upper-intermediate curriculum scripts
  - Execute all 10 upper-intermediate curriculum scripts (8.1–8.10) against the API
  - Each script validates content, creates curriculum, adds to series, sets display order, sets price to 49
  - Record all 10 curriculum IDs
  - Verify no `setPublic` calls made
  - _Requirements: 9.3, 9.4, 9.5, 9.6, 9.8, 10.1, 10.2_

- [x] 10. Checkpoint — All 20 curriculums created
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 10 intermediate curriculums: vocabLevel3 in Session 4, writingParagraph in Session 5, reading 200-350 chars
  - Verify 10 upper-intermediate curriculums: vocabLevel3 in Session 4, writingParagraph in Session 5, reading 300-500 chars
  - Verify all 20 prices set to 49
  - Verify language pair: all have `language="ko"`, `userLanguage="vi"`
  - Verify series membership: correct display orders within each series
  - Run duplicate check queries for all 20 curriculum titles

- [x] 11. Verify all curriculums in database
  - Query database to confirm all 20 curriculums exist with correct display orders, language pair, and series membership
  - Verify collection has 4 series with correct display orders
  - Verify no duplicates exist
  - Run content corruption checks on all 20 curriculums
  - _Requirements: 1.1, 1.2, 8.1, 8.2, 8.3, 8.4, 9.7, 10.1, 10.2_

- [x] 12. Create README and cleanup
  - [x] 12.1 Create `vi-ko-intermediate-curriculums/README.md` documenting:
    - All 20 curriculum IDs with titles and levels
    - Collection ID and 4 series IDs
    - Series membership and display orders
    - Creation method (standalone Python scripts + orchestrator)
    - SQL queries for retrieval
    - Recreation context (requirements, vocab lists, tone assignments)
    - _Requirements: 9.7_

  - [x] 12.2 Delete all creation scripts after verification
    - Delete all 20 `create_*.py` scripts
    - Delete `orchestrator.py`
    - Delete `validate_content.py` and `test_validate.py`
    - Keep only `README.md` in the directory
    - _Requirements: 9.7_
