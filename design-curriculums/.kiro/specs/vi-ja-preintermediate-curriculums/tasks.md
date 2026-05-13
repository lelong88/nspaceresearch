# Implementation Plan: Vietnamese-Japanese Preintermediate/Intermediate Curriculums

## Overview

Create 20 Japanese-learning curriculums for Vietnamese-speaking adults at preintermediate and intermediate levels, organized into 1 collection ("Tiếng Nhật Trung Cấp") and 5 series of 4 curriculums each. Language pair: `userLanguage="vi"`, `language="ja"`.

Implementation uses Python scripts in `vi-ja-preintermediate-curriculums/`. Two curriculum formats: preintermediate (5 sessions, 18 words in 3 groups of 6, no writingParagraph/vocabLevel3, price 49) and intermediate (5 sessions, 18 words in 3 groups of 6, vocabLevel3 in Session 4, writingParagraph in Session 5, price 49). Each curriculum gets its own standalone script with hand-crafted content including kanji with furigana. A preintermediate/intermediate-specific `validate_content.py` enforces format rules before upload. The shared root-level `api_helpers.py` handles all API calls.

Execution order: (1) content validator + property tests, (2) orchestrator for collection/series, (3) preintermediate scripts ×10, (4) intermediate scripts ×10, (5) README + cleanup.

## Tasks

- [ ] 1. Create preintermediate/intermediate content validator
  - [ ] 1.1 Create `vi-ja-preintermediate-curriculums/validate_content.py` with format-aware `validate(content, format)` function
    - `format` parameter: `"preintermediate"` or `"intermediate"`
    - Format-specific checks: session count = exactly 5 for both formats; vocab count = exactly 18 (3 groups of 6) for both formats
    - Preintermediate forbidden activities: `writingParagraph` and `vocabLevel3` forbidden in ALL sessions
    - Intermediate required activities: `vocabLevel3` ONLY in Session 4; `writingParagraph` ONLY in Session 5; raise error if missing from required session or present in wrong session
    - Shared checks: top-level structure (title, description, preview.text, contentTypeTags: [], learningSessions), session structure (title, non-empty activities), activity structure (activityType not type, valid values, title, description, data as dict), vocabList format (array of strings, field name vocabList not words — NO lowercase enforcement for Japanese hiragana/katakana/kanji), flashcard consistency (viewFlashcards/speakFlashcards identical vocabList in same session), writingSentence structure (data.vocabList, data.items with prompt and targetVocab), writingParagraph structure (data.vocabList, data.instructions, data.prompts array with >=2 items), strip-keys exclusion (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId)
    - Total unique vocab count = 18 across all sessions
    - Raise `ValueError` with specific violation message identifying the rule, location (session/activity index), format, and expected vs actual value
    - _Requirements: 1.3, 1.4, 1.5, 1.6, 1.8, 1.9, 1.10, 1.11, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 11.10, 11.11, 11.12_

  - [ ] 1.2 Write property test: Valid content passes validation (Property 1)
    - **Property 1: Valid content passes validation**
    - Use `hypothesis` to generate well-formed curriculum content dicts matching each of the 2 formats (exactly 5 sessions, 18 vocab words in 3 groups of 6, all required fields, no forbidden activities for preintermediate, correct placement of required activities for intermediate, no strip keys, vocabList as arrays of Japanese strings) and verify `validate(content, format)` returns without exception
    - **Validates: Requirements 1.3, 1.4, 1.5, 11.1, 11.2, 11.3, 11.4**

  - [ ] 1.3 Write property test: Forbidden activities rejected for preintermediate (Property 2)
    - **Property 2: Forbidden activities are rejected for preintermediate format**
    - Use `hypothesis` to inject `writingParagraph` or `vocabLevel3` into any session of a valid preintermediate curriculum and verify `validate(content, "preintermediate")` raises ValueError identifying the forbidden activity
    - **Validates: Requirements 1.8, 1.9, 4.2, 11.10**

  - [ ] 1.4 Write property test: Intermediate activity placement enforced (Property 3)
    - **Property 3: Intermediate activity placement is enforced**
    - Use `hypothesis` to test: (a) vocabLevel3 in wrong session raises ValueError, (b) writingParagraph in wrong session raises ValueError, (c) vocabLevel3 missing from Session 4 raises ValueError, (d) writingParagraph missing from Session 5 raises ValueError
    - **Validates: Requirements 1.10, 1.11, 5.2, 5.3, 11.11**

  - [ ] 1.5 Write property test: Strip keys rejected anywhere in JSON tree (Property 4)
    - **Property 4: Strip keys are rejected anywhere in the JSON tree**
    - Use `hypothesis` to inject strip keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) at random depths in curriculum JSON and verify rejection with message mentioning the strip key
    - **Validates: Requirements 1.6, 11.9**

  - [ ] 1.6 Write property test: Activities missing required fields rejected (Property 5)
    - **Property 5: Activities missing required fields are rejected**
    - Use `hypothesis` to generate activities missing `activityType`, `title`, `description`, or `data`, or with `data` not being a dict, and verify rejection identifying the missing field and its location
    - **Validates: Requirements 10.1, 10.5, 11.3**

  - [ ] 1.7 Write property test: Invalid activityType values rejected (Property 6)
    - **Property 6: Invalid activityType values are rejected**
    - Use `hypothesis` to generate activities with `activityType` values not in the valid set (introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence, writingParagraph) and verify rejection
    - **Validates: Requirements 10.2, 11.4**

  - [ ] 1.8 Write property test: vocabList format enforced (Property 7)
    - **Property 7: vocabList format is enforced**
    - Use `hypothesis` to generate vocab activities with non-array vocabList, empty vocabList, non-string elements, or field name `words` instead of `vocabList`, and verify rejection. Note: lowercase is NOT enforced for Japanese vocabulary (kanji/hiragana/katakana have no case)
    - **Validates: Requirements 10.3, 11.5**

  - [ ] 1.9 Write property test: Flashcard vocabList consistency (Property 8)
    - **Property 8: Flashcard vocabList consistency within sessions**
    - Use `hypothesis` to generate sessions with mismatched viewFlashcards/speakFlashcards vocabList arrays and verify rejection
    - **Validates: Requirements 10.4, 11.6**

  - [ ] 1.10 Write property test: Writing activity structure enforced (Property 9)
    - **Property 9: Writing activity structure is enforced**
    - Use `hypothesis` to generate: (a) writingSentence activities with missing data.vocabList, missing/empty data.items, or items lacking prompt/targetVocab and verify rejection; (b) writingParagraph activities with missing data.vocabList, missing/empty data.instructions, or data.prompts with fewer than 2 items and verify rejection
    - **Validates: Requirements 10.6, 10.7, 11.7, 11.8**

- [ ] 2. Checkpoint — Content validator ready
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 3. Create orchestrator and collection/series infrastructure
  - [ ] 3.1 Create `vi-ja-preintermediate-curriculums/orchestrator.py`
    - Create 1 collection: "Tiếng Nhật Trung Cấp" with neutral informative Vietnamese description about advancing beyond beginner level
    - Create 5 series with descriptions ≤255 chars each using different Tone_Palette types:
      - Series 1: "Sự Nghiệp Tại Nhật" (tone: `bold_declaration`)
      - Series 2: "Khám Phá Nhật Bản" (tone: `vivid_scenario`)
      - Series 3: "Đời Sống Và Xã Hội" (tone: `empathetic_observation`)
      - Series 4: "Văn Hóa Và Nghệ Thuật" (tone: `surprising_fact`)
      - Series 5: "Thế Giới Hiện Đại" (tone: `provocative_question`)
    - Wire all 5 series to the collection via `add_series_to_collection`
    - Set display orders for all 5 series via `set_series_display_order`
    - Hard-code the tone assignment table from the design (all 20 curriculum description tones and farewell tones) and print it for reference
    - Log collection ID and all 5 series IDs to stdout
    - Uses root-level `api_helpers.py` via sys.path: `create_collection`, `create_series`, `add_series_to_collection`, `set_series_display_order`
    - _Requirements: 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 12.2, 12.3, 12.4, 12.5, 16.1_


- [ ] 4. Create preintermediate curriculum scripts (10 scripts)
  - [ ] 4.1 Create `vi-ja-preintermediate-curriculums/create_job_interview.py` — "Phỏng Vấn Xin Việc" (Series 1, display order 1)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["履歴書", "面接", "志望動機", "経験", "給料", "正社員", "残業", "上司", "部下", "昇進", "退職", "応募", "採用", "研修", "通勤", "有給", "転職", "名刺"]
    - Session structure per design: S1-S3 (learning with introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, introAudio grammar, reading 150-250 chars with furigana, speakReading, readAlong, writingSentence ×3), S4 (review with all 18 words, vocabLevel1+2, writingSentence ×4-5), S5 (final reading 400-600 chars, farewell introAudio)
    - Description tone: `provocative_question`, farewell tone: `warm_accountability`
    - All text hand-crafted: Vietnamese marketing copy, Japanese reading passages with kanji+furigana, introAudio scripts teaching each word with furigana/Vietnamese meaning/example sentences
    - Validate with `validate(content, "preintermediate")` before upload
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [ ] 4.2 Create `vi-ja-preintermediate-curriculums/create_booking_planning.py` — "Đặt Phòng Và Lên Kế Hoạch" (Series 2, display order 1)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["予約", "片道", "往復", "出発", "到着", "乗り換え", "空港", "搭乗", "パスポート", "観光", "旅行代理店", "日程", "荷造り", "両替", "免税", "案内", "地図", "土産"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for travel planning topic
    - Description tone: `surprising_fact`, farewell tone: `team_building_energy`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [ ] 4.3 Create `vi-ja-preintermediate-curriculums/create_street_food.py` — "Ẩm Thực Đường Phố" (Series 2, display order 2)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["屋台", "焼き鳥", "たこ焼き", "お好み焼き", "注文", "持ち帰り", "食べ歩き", "行列", "割り箸", "味", "辛い", "甘い", "焼く", "揚げる", "蒸す", "具", "ソース", "薬味"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for street food culture topic
    - Description tone: `metaphor_led`, farewell tone: `warm_accountability`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [ ] 4.4 Create `vi-ja-preintermediate-curriculums/create_renting.py` — "Thuê Nhà Ở Nhật" (Series 1, display order 2)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["賃貸", "家賃", "敷金", "礼金", "不動産", "間取り", "一人暮らし", "引っ越し", "契約", "保証人", "管理費", "駅近", "築年数", "日当たり", "防音", "ゴミ出し", "大家", "更新"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for renting/housing topic
    - Description tone: `vivid_scenario`, farewell tone: `quiet_awe`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [ ] 4.5 Create `vi-ja-preintermediate-curriculums/create_medical_visit.py` — "Khám Bệnh Ở Nhật" (Series 3, display order 1)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["診察", "症状", "処方箋", "保険証", "受付", "待合室", "内科", "外科", "検査", "注射", "入院", "退院", "薬局", "アレルギー", "予防接種", "診断", "紹介状", "救急"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for medical visit topic
    - Description tone: `provocative_question`, farewell tone: `introspective_guide`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [ ] 4.6 Create `vi-ja-preintermediate-curriculums/create_social_relationships.py` — "Mối Quan Hệ Xã Hội" (Series 3, display order 2)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["友達", "知り合い", "付き合う", "別れる", "信頼", "約束", "相談", "紹介", "誘う", "断る", "謝る", "許す", "喧嘩", "仲直り", "気遣い", "本音", "建前", "空気を読む"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for social relationships topic
    - Description tone: `empathetic_observation`, farewell tone: `team_building_energy`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [ ] 4.7 Create `vi-ja-preintermediate-curriculums/create_natural_disasters.py` — "Thiên Tai Và An Toàn" (Series 3, display order 3)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["地震", "台風", "津波", "避難", "防災", "非常口", "避難所", "警報", "余震", "停電", "断水", "備蓄", "消火器", "救助", "安否確認", "防災グッズ", "耐震", "緊急地震速報"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for natural disasters/safety topic
    - Description tone: `bold_declaration`, farewell tone: `warm_accountability`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [ ] 4.8 Create `vi-ja-preintermediate-curriculums/create_phone_communication.py` — "Giao Tiếp Qua Điện Thoại" (Series 1, display order 3)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["電話", "留守番電話", "着信", "発信", "折り返し", "伝言", "内線", "外線", "通話", "切る", "かけ直す", "繋がる", "話し中", "番号", "登録", "連絡先", "不在", "取り次ぐ"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for phone communication topic
    - Description tone: `empathetic_observation`, farewell tone: `practical_momentum`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [ ] 4.9 Create `vi-ja-preintermediate-curriculums/create_online_shopping.py` — "Mua Sắm Trực Tuyến" (Series 5, display order 1)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["通販", "カート", "送料", "届く", "返品", "交換", "レビュー", "評価", "在庫", "割引", "ポイント", "クーポン", "配送", "代引き", "振込", "クレジットカード", "領収書", "問い合わせ"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for online shopping topic
    - Description tone: `bold_declaration`, farewell tone: `quiet_awe`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [ ] 4.10 Create `vi-ja-preintermediate-curriculums/create_sports_cheering.py` — "Thể Thao Và Cổ Vũ" (Series 5, display order 2)
    - Preintermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["応援", "試合", "選手", "優勝", "決勝", "予選", "観戦", "チケット", "スタジアム", "得点", "反則", "審判", "延長", "引き分け", "記録", "ファン", "声援", "実況"]
    - Same 5-session preintermediate structure as 4.1 but all content hand-crafted for sports/cheering topic
    - Description tone: `surprising_fact`, farewell tone: `practical_momentum`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.6, 3.7, 4.1, 4.2, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

- [ ] 5. Checkpoint — Preintermediate curriculums done
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 10 preintermediate curriculums created with correct series assignments
  - Verify all prices set to 49
  - Verify no writingParagraph or vocabLevel3 in any preintermediate curriculum
  - Verify language pair: all have `language="ja"`, `userLanguage="vi"`


- [ ] 6. Create intermediate curriculum scripts (10 scripts)
  - [ ] 6.1 Create `vi-ja-preintermediate-curriculums/create_office_culture.py` — "Văn Hóa Công Sở" (Series 1, display order 4)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["敬語", "報告", "連絡", "相談", "根回し", "飲み会", "忘年会", "歓迎会", "送別会", "年功序列", "終身雇用", "有給休暇", "出張", "議事録", "プレゼン", "締め切り", "稟議", "社風"]
    - Session structure per design: S1-S3 (learning with introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, introAudio grammar, reading 200-350 chars with kanji+furigana, speakReading, readAlong, writingSentence ×3), S4 (review with all 18 words, vocabLevel1+2+3, writingSentence ×4-5), S5 (final reading 500-800 chars, writingParagraph using 6+ vocab words, farewell introAudio)
    - Description tone: `bold_declaration`, farewell tone: `introspective_guide`
    - All text hand-crafted: Vietnamese marketing copy, Japanese reading passages with kanji (N4-N3 level) + furigana, introAudio scripts teaching each word with furigana/Vietnamese meaning/example sentences, writingParagraph with Vietnamese instructions and >=2 guiding questions
    - Validate with `validate(content, "intermediate")` before upload
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [ ] 6.2 Create `vi-ja-preintermediate-curriculums/create_traditional_arts.py` — "Nghệ Thuật Truyền Thống" (Series 4, display order 1)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["茶道", "華道", "書道", "着物", "歌舞伎", "能", "落語", "浮世絵", "陶芸", "漆器", "折り紙", "盆栽", "和紙", "藍染め", "師匠", "弟子", "稽古", "流派"]
    - Same 5-session intermediate structure as 6.1 but all content hand-crafted for traditional arts topic
    - Description tone: `metaphor_led`, farewell tone: `practical_momentum`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [ ] 6.3 Create `vi-ja-preintermediate-curriculums/create_news_events.py` — "Tin Tức Và Thời Sự" (Series 4, display order 2)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["報道", "記者", "取材", "世論", "選挙", "政策", "経済", "景気", "失業", "物価", "増税", "少子化", "高齢化", "環境問題", "国際", "条約", "首脳", "外交"]
    - Same 5-session intermediate structure as 6.1 but all content hand-crafted for news/current events topic
    - Description tone: `provocative_question`, farewell tone: `introspective_guide`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [ ] 6.4 Create `vi-ja-preintermediate-curriculums/create_education.py` — "Giáo Dục Ở Nhật" (Series 4, display order 3)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["入学", "卒業", "受験", "塾", "偏差値", "奨学金", "単位", "論文", "研究", "教授", "講義", "学費", "留学", "部活", "学園祭", "成績", "進路", "就職活動"]
    - Same 5-session intermediate structure as 6.1 but all content hand-crafted for education topic
    - Description tone: `vivid_scenario`, farewell tone: `team_building_energy`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [ ] 6.5 Create `vi-ja-preintermediate-curriculums/create_fine_dining.py` — "Ẩm Thực Cao Cấp" (Series 2, display order 3)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["懐石", "割烹", "板前", "旬", "盛り付け", "器", "出汁", "発酵", "熟成", "食材", "産地", "予約制", "おまかせ", "コース", "日本酒", "銘柄", "食感", "香り"]
    - Same 5-session intermediate structure as 6.1 but all content hand-crafted for fine dining topic
    - Description tone: `bold_declaration`, farewell tone: `quiet_awe`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [ ] 6.6 Create `vi-ja-preintermediate-curriculums/create_psychology_emotions.py` — "Tâm Lý Và Cảm Xúc" (Series 3, display order 4)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["感情", "不安", "ストレス", "鬱", "自信", "劣等感", "共感", "孤独", "達成感", "挫折", "成長", "自己肯定感", "気分転換", "癒し", "瞑想", "カウンセリング", "依存", "回復"]
    - Same 5-session intermediate structure as 6.1 but all content hand-crafted for psychology/emotions topic
    - Description tone: `surprising_fact`, farewell tone: `quiet_awe`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [ ] 6.7 Create `vi-ja-preintermediate-curriculums/create_rural_tourism.py` — "Du Lịch Nông Thôn" (Series 2, display order 4)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["田舎", "温泉", "旅館", "民宿", "農業体験", "収穫", "田んぼ", "畑", "漁村", "古民家", "里山", "棚田", "地元", "方言", "祭り", "郷土料理", "自然", "景色"]
    - Same 5-session intermediate structure as 6.1 but all content hand-crafted for rural tourism topic
    - Description tone: `vivid_scenario`, farewell tone: `practical_momentum`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [ ] 6.8 Create `vi-ja-preintermediate-curriculums/create_technology_ai.py` — "Công Nghệ Và AI" (Series 5, display order 3)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["人工知能", "自動化", "ロボット", "データ", "アルゴリズム", "プログラミング", "セキュリティ", "個人情報", "SNS", "炎上", "フェイクニュース", "仮想現実", "電子決済", "サブスク", "クラウド", "通知", "更新", "バグ"]
    - Same 5-session intermediate structure as 6.1 but all content hand-crafted for technology/AI topic
    - Description tone: `metaphor_led`, farewell tone: `introspective_guide`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [ ] 6.9 Create `vi-ja-preintermediate-curriculums/create_law_rules.py` — "Pháp Luật Và Quy Tắc" (Series 4, display order 4)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["法律", "規則", "違反", "罰金", "届出", "許可", "届け出る", "義務", "権利", "契約", "保証", "賠償", "裁判", "弁護士", "証拠", "被害", "犯罪", "防犯"]
    - Same 5-session intermediate structure as 6.1 but all content hand-crafted for law/rules topic
    - Description tone: `empathetic_observation`, farewell tone: `warm_accountability`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [ ] 6.10 Create `vi-ja-preintermediate-curriculums/create_environment.py` — "Môi Trường Và Bền Vững" (Series 5, display order 4)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["環境", "リサイクル", "分別", "再生可能", "エネルギー", "温暖化", "排出", "削減", "持続可能", "エコ", "省エネ", "太陽光", "風力", "汚染", "生態系", "絶滅危惧", "森林伐採", "脱炭素"]
    - Same 5-session intermediate structure as 6.1 but all content hand-crafted for environment/sustainability topic
    - Description tone: `vivid_scenario`, farewell tone: `team_building_energy`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.6, 3.7, 5.1, 5.2, 5.3, 6.1, 6.2, 6.3, 6.4, 6.5, 6.7, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

- [ ] 7. Checkpoint — All 20 curriculums created
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 10 preintermediate curriculums: no writingParagraph/vocabLevel3
  - Verify 10 intermediate curriculums: vocabLevel3 in Session 4, writingParagraph in Session 5
  - Verify all 20 prices set to 49
  - Verify language pair: all have `language="ja"`, `userLanguage="vi"`
  - Verify series membership: 4 curriculums per series, correct display orders
  - Run duplicate check queries for all 20 curriculum titles

- [ ] 8. Documentation and cleanup
  - [ ] 8.1 Create `vi-ja-preintermediate-curriculums/README.md`
    - Document: collection ID, all 5 series IDs, all 20 curriculum IDs with titles and display orders
    - Document: vocabulary lists per curriculum (all 20 × 18 words)
    - Document: tone assignments (description and farewell for all 20 curriculums)
    - Document: pricing (49 for all), language pair (vi-ja), format (preintermediate vs intermediate)
    - Include SQL verification queries: count curriculums, verify language pair, verify prices, verify series membership and display orders, verify no duplicates, verify collection → series wiring, verify level gap within series
    - Include recreation instructions
    - _Requirements: 15.1_

  - [ ] 8.2 Delete all creation scripts after verification
    - Delete `orchestrator.py`, all 20 `create_*.py` scripts, `validate_content.py`, and `test_validate.py` from `vi-ja-preintermediate-curriculums/`
    - Only `README.md` remains in the directory
    - _Requirements: 15.2_

  - [ ] 8.3 Run duplicate check and resolve
    - Run duplicate check query for each of the 20 curriculum titles
    - If duplicates found: keep earliest, remove from series first, then delete extras
    - _Requirements: 15.3_

- [ ] 9. Final checkpoint — All tasks complete
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 20 curriculums total: 10 preintermediate + 10 intermediate
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
- Two formats: preintermediate (5 sessions, 18 words, no writingParagraph/vocabLevel3, price 49), intermediate (5 sessions, 18 words, vocabLevel3 in S4, writingParagraph in S5, price 49)
- Vietnamese session titles: "Phần 1", "Phần 2", "Phần 3", "Ôn tập", "Đọc tổng hợp"
- All marketing text (title, description, preview) in Vietnamese targeting adult learners
- All learner-facing content bilingual: Vietnamese explanations with Japanese vocabulary including kanji + furigana
- No vocabulary overlap across the 20 curriculums or with the 20 beginner vi-ja curriculums
- Japanese vocabulary includes kanji (JLPT N5-N4 for preintermediate, N4-N3 for intermediate) with furigana readings
- Reading passage lengths: preintermediate 150-250 chars per session / 400-600 chars final; intermediate 200-350 chars per session / 500-800 chars final
- Tone distribution across 20 descriptions: provocative_question ×3, bold_declaration ×4, vivid_scenario ×4, empathetic_observation ×3, surprising_fact ×3, metaphor_led ×3 — max 20%, all ≤30% ✓
- No adjacent tone duplicates within any of the 5 series ✓
- Farewell tone distribution: warm_accountability ×4, quiet_awe ×4, practical_momentum ×4, introspective_guide ×4, team_building_energy ×4 — evenly distributed (20% each) ✓
- Series composition: Series 1 (Curriculums 1,4,8,11), Series 2 (2,3,15,17), Series 3 (5,6,7,16), Series 4 (12,13,14,19), Series 5 (9,10,18,20)
