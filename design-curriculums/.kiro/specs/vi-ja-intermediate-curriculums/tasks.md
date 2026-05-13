# Implementation Plan: Vietnamese-Japanese Intermediate/Upper-Intermediate Curriculums

## Overview

Create 20 Japanese-learning curriculums for Vietnamese-speaking adults at intermediate and upper-intermediate levels, organized into 1 collection ("Tiếng Nhật Nâng Cao") and 5 series of 4 curriculums each. Language pair: `userLanguage="vi"`, `language="ja"`.

Implementation uses Python scripts in `vi-ja-intermediate-curriculums/`. Two curriculum formats: intermediate (5 sessions, 18 words in 3 groups of 6, vocabLevel3 in Session 4, writingParagraph in Session 5, reading 250-400 chars/session + 600-900 final, price 49) and upper_intermediate (5 sessions, 18 words in 3 groups of 6, vocabLevel3 in Session 4, writingParagraph in Session 5, reading 350-500 chars/session + 800-1200 final, price 49). Each curriculum gets its own standalone script with hand-crafted content including kanji with selective furigana (N2+ only). A format-aware `validate_content.py` enforces rules before upload. The shared root-level `api_helpers.py` handles all API calls.

Execution order: (1) content validator + property tests, (2) orchestrator for collection/series, (3) intermediate scripts ×10, (4) upper-intermediate scripts ×10, (5) verification, (6) README + cleanup.

## Tasks

- [x] 1. Create intermediate/upper-intermediate content validator
  - [x] 1.1 Create `vi-ja-intermediate-curriculums/validate_content.py` with format-aware `validate(content, format)` function
    - `format` parameter: `"intermediate"` or `"upper_intermediate"`
    - Both formats require: session count = exactly 5; vocab count = exactly 18 (3 groups of 6); vocabLevel3 ONLY in Session 4 (required); writingParagraph ONLY in Session 5 (required)
    - Shared checks: top-level structure (title, description, preview.text, contentTypeTags: [], learningSessions), session structure (title, non-empty activities), activity structure (activityType not type, valid values, title, description, data as dict), vocabList format (array of strings, field name vocabList not words — NO lowercase enforcement for Japanese hiragana/katakana/kanji), flashcard consistency (viewFlashcards/speakFlashcards identical vocabList in same session), writingSentence structure (data.vocabList, data.items with prompt and targetVocab), writingParagraph structure (data.vocabList, data.instructions, data.prompts array with >=2 items), strip-keys exclusion (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId)
    - Total unique vocab count = 18 across all sessions
    - vocabLevel3 IS PRESENT in Session 4 (required, not just allowed)
    - writingParagraph IS PRESENT in Session 5 (required, not just allowed)
    - Raise `ValueError` with specific violation message identifying the rule, location (session/activity index), format, and expected vs actual value
    - _Requirements: 1.3, 1.4, 1.5, 1.6, 1.8, 1.9, 1.10, 1.11, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 11.10, 11.11_

  - [x] 1.2 Write property test: Valid content passes validation (Property 1)
    - **Property 1: Valid content passes validation**
    - Use `hypothesis` to generate well-formed curriculum content dicts matching each of the 2 formats (exactly 5 sessions, 18 vocab words in 3 groups of 6, all required fields, vocabLevel3 in Session 4, writingParagraph in Session 5, no strip keys, vocabList as arrays of Japanese strings) and verify `validate(content, format)` returns without exception
    - **Validates: Requirements 1.3, 1.4, 1.5, 1.8, 1.9, 1.10, 1.11, 11.1, 11.2, 11.3, 11.4**

  - [x] 1.3 Write property test: Strip keys rejected anywhere in JSON tree (Property 2)
    - **Property 2: Strip keys are rejected anywhere in the JSON tree**
    - Use `hypothesis` to inject strip keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) at random depths in curriculum JSON and verify rejection with message mentioning the strip key
    - **Validates: Requirements 1.6, 11.9**

  - [x] 1.4 Write property test: Activity placement enforced (Property 3)
    - **Property 3: Activity placement is enforced**
    - Use `hypothesis` to test: (a) vocabLevel3 in wrong session raises ValueError, (b) writingParagraph in wrong session raises ValueError, (c) vocabLevel3 missing from Session 4 raises ValueError, (d) writingParagraph missing from Session 5 raises ValueError
    - **Validates: Requirements 1.8, 1.9, 1.10, 1.11, 4.2, 4.3, 5.2, 5.3, 11.10**

  - [x] 1.5 Write property test: Activities missing required fields rejected (Property 4)
    - **Property 4: Activities missing required fields are rejected**
    - Use `hypothesis` to generate activities missing `activityType`, `title`, `description`, or `data`, or with `data` not being a dict, and verify rejection identifying the missing field and its location
    - **Validates: Requirements 10.1, 10.5, 11.3**

  - [x] 1.6 Write property test: Invalid activityType values rejected (Property 5)
    - **Property 5: Invalid activityType values are rejected**
    - Use `hypothesis` to generate activities with `activityType` values not in the valid set (introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence, writingParagraph) and verify rejection
    - **Validates: Requirements 10.2, 11.4**

  - [x] 1.7 Write property test: vocabList format enforced (Property 6)
    - **Property 6: vocabList format is enforced**
    - Use `hypothesis` to generate vocab activities with non-array vocabList, empty vocabList, non-string elements, or field name `words` instead of `vocabList`, and verify rejection. Note: lowercase is NOT enforced for Japanese vocabulary (kanji/hiragana/katakana have no case)
    - **Validates: Requirements 10.3, 11.5**

  - [x] 1.8 Write property test: Flashcard vocabList consistency (Property 7)
    - **Property 7: Flashcard vocabList consistency within sessions**
    - Use `hypothesis` to generate sessions with mismatched viewFlashcards/speakFlashcards vocabList arrays and verify rejection
    - **Validates: Requirements 10.4, 11.6**

  - [x] 1.9 Write property test: Writing activity structure enforced (Property 8)
    - **Property 8: Writing activity structure is enforced**
    - Use `hypothesis` to generate: (a) writingSentence activities with missing data.vocabList, missing/empty data.items, or items lacking prompt/targetVocab and verify rejection; (b) writingParagraph activities with missing data.vocabList, missing/empty data.instructions, or data.prompts with fewer than 2 items and verify rejection
    - **Validates: Requirements 10.6, 10.7, 11.7, 11.8**

- [x] 2. Checkpoint — Content validator ready
  - Ensure all tests pass, ask the user if questions arise.

- [x] 3. Create orchestrator and collection/series infrastructure
  - [x] 3.1 Create `vi-ja-intermediate-curriculums/orchestrator.py`
    - Create 1 collection: "Tiếng Nhật Nâng Cao" with neutral informative Vietnamese description about intermediate/upper-intermediate Japanese for Vietnamese adults covering business, culture, society, science, and personal development
    - Create 5 series with descriptions ≤255 chars each using different Tone_Palette types:
      - Series 1: "Kinh Doanh Và Tài Chính" (tone: `bold_declaration`) — Curriculums 1, 3, 8, 15
      - Series 2: "Truyền Thông Và Giải Trí" (tone: `vivid_scenario`) — Curriculums 2, 6, 9, 19
      - Series 3: "Xã Hội Và Con Người" (tone: `empathetic_observation`) — Curriculums 4, 5, 7, 12
      - Series 4: "Khoa Học Và Tương Lai" (tone: `surprising_fact`) — Curriculums 10, 13, 16, 18
      - Series 5: "Văn Hóa Và Tư Tưởng" (tone: `provocative_question`) — Curriculums 11, 14, 17, 20
    - Wire all 5 series to the collection via `add_series_to_collection`
    - Set display orders for all 5 series via `set_series_display_order`
    - Hard-code the tone assignment table from the design (all 20 curriculum description tones and farewell tones) and print it for reference
    - Log collection ID and all 5 series IDs to stdout
    - Uses root-level `api_helpers.py` via sys.path: `create_collection`, `create_series`, `add_series_to_collection`, `set_series_display_order`
    - _Requirements: 9.1, 9.2, 9.3, 9.4, 9.7, 12.2, 12.3, 12.4, 12.5, 16.1_

  - [x] 3.2 Run `orchestrator.py` and record collection/series IDs
    - Execute the orchestrator script
    - Record the collection ID and all 5 series IDs for use in curriculum scripts
    - Verify collection and series created successfully via database query
    - _Requirements: 9.1, 9.2, 9.3, 9.4, 16.1_

- [x] 4. Checkpoint — Infrastructure ready
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 1 collection and 5 series exist in database
  - Verify series are wired to collection with correct display orders


- [x] 5. Create intermediate curriculum scripts (10 scripts)
  - [x] 5.1 Create `vi-ja-intermediate-curriculums/create_business_negotiation.py` — "Đàm Phán Kinh Doanh" (Series 1: Kinh Doanh Và Tài Chính, display order 1)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["交渉", "提案", "妥協", "条件", "合意", "利益", "競合", "戦略", "見積もり", "契約書", "納期", "取引先", "値下げ", "決裁", "商談", "譲歩", "双方", "成約"]
    - Session structure: S1-S3 (learning with introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, introAudio grammar, reading 250-400 chars with N3 kanji freely + N2+ furigana, speakReading, readAlong, writingSentence ×3), S4 (review with all 18 words, vocabLevel1+2+3, writingSentence ×4-5), S5 (final reading 600-900 chars, writingParagraph using 6+ vocab words, farewell introAudio)
    - Description tone: `provocative_question`, farewell tone: `warm_accountability`
    - All text hand-crafted: Vietnamese persuasive marketing copy, Japanese reading passages with kanji (N3 freely, N2+ with furigana), introAudio scripts teaching each word with selective furigana/Vietnamese meaning/example sentences, writingParagraph with Vietnamese instructions and >=2 guiding questions
    - Validate with `validate(content, "intermediate")` before upload
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.5, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 5.2 Create `vi-ja-intermediate-curriculums/create_media_advertising.py` — "Truyền Thông Và Quảng Cáo" (Series 2: Truyền Thông Và Giải Trí, display order 1)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["広告", "宣伝", "ブランド", "ターゲット", "キャンペーン", "消費者", "影響力", "口コミ", "インフルエンサー", "視聴率", "メディア", "炎上", "印象", "訴求", "差別化", "コンテンツ", "拡散", "認知度"]
    - Same 5-session intermediate structure as 5.1 but all content hand-crafted for media/advertising topic
    - Description tone: `surprising_fact`, farewell tone: `team_building_energy`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.5, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 5.3 Create `vi-ja-intermediate-curriculums/create_personal_finance.py` — "Tài Chính Cá Nhân" (Series 1: Kinh Doanh Và Tài Chính, display order 2)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["貯金", "投資", "株", "利息", "借金", "返済", "家計", "節約", "資産", "年金", "保険", "税金", "確定申告", "ローン", "金利", "収支", "老後", "運用"]
    - Same 5-session intermediate structure as 5.1 but all content hand-crafted for personal finance topic
    - Description tone: `vivid_scenario`, farewell tone: `quiet_awe`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.5, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 5.4 Create `vi-ja-intermediate-curriculums/create_modern_marriage.py` — "Hôn Nhân Và Gia Đình Hiện Đại" (Series 3: Xã Hội Và Con Người, display order 1)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["結婚", "離婚", "共働き", "育児", "家事分担", "嫁姑", "晩婚", "少子化", "核家族", "介護", "世代間", "価値観", "同棲", "養育費", "親権", "扶養", "相続", "家族構成"]
    - Same 5-session intermediate structure as 5.1 but all content hand-crafted for modern marriage/family topic
    - Description tone: `empathetic_observation`, farewell tone: `introspective_guide`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.5, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 5.5 Create `vi-ja-intermediate-curriculums/create_self_development.py` — "Phát Triển Bản Thân" (Series 3: Xã Hội Và Con Người, display order 2)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["目標", "習慣", "自己啓発", "時間管理", "優先順位", "集中力", "生産性", "モチベーション", "振り返り", "挑戦", "失敗", "克服", "継続", "成果", "計画", "実行", "改善", "意志力"]
    - Same 5-session intermediate structure as 5.1 but all content hand-crafted for self-development topic
    - Description tone: `provocative_question`, farewell tone: `team_building_energy`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.5, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 5.6 Create `vi-ja-intermediate-curriculums/create_manga_anime.py` — "Văn Hóa Manga Và Anime" (Series 2: Truyền Thông Và Giải Trí, display order 2)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["漫画", "アニメ", "声優", "連載", "単行本", "同人誌", "コスプレ", "聖地巡礼", "原作", "作画", "伏線", "展開", "ジャンル", "主人公", "世界観", "名場面", "完結", "ファン層"]
    - Same 5-session intermediate structure as 5.1 but all content hand-crafted for manga/anime culture topic
    - Description tone: `metaphor_led`, farewell tone: `warm_accountability`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.5, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 5.7 Create `vi-ja-intermediate-curriculums/create_mental_health.py` — "Y Học Và Sức Khỏe Tinh Thần" (Series 3: Xã Hội Và Con Người, display order 3)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["精神科", "心療内科", "適応障害", "燃え尽き", "過労", "休職", "復職", "治療", "薬物療法", "認知行動療法", "偏見", "理解", "支援", "相談窓口", "早期発見", "予防", "回復", "社会復帰"]
    - Same 5-session intermediate structure as 5.1 but all content hand-crafted for mental health topic
    - Description tone: `bold_declaration`, farewell tone: `warm_accountability`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.5, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 5.8 Create `vi-ja-intermediate-curriculums/create_real_estate.py` — "Bất Động Sản Và Đầu Tư" (Series 1: Kinh Doanh Và Tài Chính, display order 3)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["不動産投資", "物件", "利回り", "頭金", "住宅ローン", "固定資産税", "管理会社", "空室", "入居者", "修繕", "築年数", "立地", "相場", "査定", "仲介", "登記", "融資", "収益"]
    - Same 5-session intermediate structure as 5.1 but all content hand-crafted for real estate/investment topic
    - Description tone: `empathetic_observation`, farewell tone: `practical_momentum`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.5, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 5.9 Create `vi-ja-intermediate-curriculums/create_world_cuisine.py` — "Ẩm Thực Thế Giới Tại Nhật" (Series 2: Truyền Thông Và Giải Trí, display order 3)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["多国籍料理", "食文化", "本場", "調理法", "食材", "香辛料", "食感", "盛り付け", "食べ放題", "予約必須", "行列店", "食レポ", "グルメ", "ミシュラン", "隠れ家", "食通", "創作料理", "食べログ"]
    - Same 5-session intermediate structure as 5.1 but all content hand-crafted for world cuisine topic
    - Description tone: `bold_declaration`, farewell tone: `quiet_awe`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.5, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 5.10 Create `vi-ja-intermediate-curriculums/create_transportation_urban.py` — "Giao Thông Và Đô Thị" (Series 4: Khoa Học Và Tương Lai, display order 1)
    - Intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["都市計画", "再開発", "人口密度", "通勤ラッシュ", "渋滞", "公共交通", "路線図", "乗車率", "終電", "始発", "定期券", "混雑", "時差出勤", "テレワーク", "郊外", "都心", "インフラ", "バリアフリー"]
    - Same 5-session intermediate structure as 5.1 but all content hand-crafted for transportation/urban life topic
    - Description tone: `metaphor_led`, farewell tone: `practical_momentum`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.4, 3.5, 3.7, 4.1, 4.2, 4.3, 6.1, 6.2, 6.3, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

- [x] 6. Run intermediate curriculum scripts
  - Execute all 10 intermediate curriculum scripts (5.1–5.10) against the API
  - Each script validates content, creates curriculum, adds to series, sets display order, sets price to 49
  - Record all 10 curriculum IDs
  - Verify no `setPublic` calls made
  - _Requirements: 8.1, 8.2, 9.5, 9.6, 13.1, 16.1, 16.2_

- [x] 7. Checkpoint — Intermediate curriculums done
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 10 intermediate curriculums created with correct series assignments
  - Verify all prices set to 49
  - Verify vocabLevel3 in Session 4 and writingParagraph in Session 5 for all 10
  - Verify language pair: all have `language="ja"`, `userLanguage="vi"`

- [x] 8. Create upper-intermediate curriculum scripts (10 scripts)
  - [x] 8.1 Create `vi-ja-intermediate-curriculums/create_japanese_philosophy.py` — "Triết Học Sống Của Người Nhật" (Series 5: Văn Hóa Và Tư Tưởng, display order 1)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["生きがい", "侘び寂び", "無常", "一期一会", "本音", "建前", "義理", "恩", "和", "空気", "甘え", "我慢", "反省", "謙虚", "思いやり", "潔い", "道", "修行"]
    - Session structure: S1-S3 (learning with introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, introAudio grammar, reading 350-500 chars with N3-N2 kanji freely + rare kanji furigana, speakReading, readAlong, writingSentence ×3), S4 (review with all 18 words, vocabLevel1+2+3, writingSentence ×4-5), S5 (final reading 800-1200 chars, writingParagraph using 6+ vocab words with analytical/argumentative prompts, farewell introAudio)
    - Description tone: `metaphor_led`, farewell tone: `quiet_awe`
    - All text hand-crafted: Vietnamese persuasive marketing copy, Japanese reading passages with kanji (N3-N2 freely, rare with furigana), introAudio scripts teaching each word with minimal furigana/Vietnamese meaning/example sentences, writingParagraph with Vietnamese instructions and >=2 analytical guiding questions
    - Validate with `validate(content, "upper_intermediate")` before upload
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.8, 4.1, 5.1, 5.2, 5.3, 5.4, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 7.7, 7.8, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 8.2 Create `vi-ja-intermediate-curriculums/create_politics_society.py` — "Chính Trị Và Xã Hội Nhật Bản" (Series 3: Xã Hội Và Con Người, display order 4)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["民主主義", "国会", "与党", "野党", "憲法", "改正", "世論調査", "投票率", "格差", "福祉", "移民", "多様性", "差別", "人権", "市民運動", "規制緩和", "官僚", "地方自治"]
    - Same 5-session upper-intermediate structure as 8.1 but all content hand-crafted for politics/society topic
    - Description tone: `surprising_fact`, farewell tone: `quiet_awe`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.8, 4.1, 5.1, 5.2, 5.3, 5.4, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 7.7, 7.8, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 8.3 Create `vi-ja-intermediate-curriculums/create_science_discovery.py` — "Khoa Học Và Khám Phá" (Series 4: Khoa Học Và Tương Lai, display order 2)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["研究者", "論文", "仮説", "実験", "発見", "証明", "理論", "応用", "学会", "ノーベル賞", "特許", "革新", "量子", "遺伝子", "人工知能", "宇宙", "再生医療", "持続可能"]
    - Same 5-session upper-intermediate structure as 8.1 but all content hand-crafted for science/discovery topic
    - Description tone: `provocative_question`, farewell tone: `introspective_guide`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.8, 4.1, 5.1, 5.2, 5.3, 5.4, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 7.7, 7.8, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 8.4 Create `vi-ja-intermediate-curriculums/create_japanese_literature.py` — "Văn Học Nhật Bản" (Series 5: Văn Hóa Và Tư Tưởng, display order 2)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["文学", "小説", "短編", "随筆", "俳句", "作家", "芥川賞", "直木賞", "純文学", "大衆文学", "翻訳", "出版", "書評", "描写", "比喩", "主題", "文体", "読書感想文"]
    - Same 5-session upper-intermediate structure as 8.1 but all content hand-crafted for Japanese literature topic
    - Description tone: `empathetic_observation`, farewell tone: `practical_momentum`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.8, 4.1, 5.1, 5.2, 5.3, 5.4, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 7.7, 7.8, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 8.5 Create `vi-ja-intermediate-curriculums/create_entrepreneurship.py` — "Khởi Nghiệp Tại Nhật" (Series 1: Kinh Doanh Và Tài Chính, display order 4)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["起業", "創業者", "ベンチャー", "資金調達", "事業計画", "投資家", "株式公開", "黒字", "赤字", "市場調査", "差別化", "顧客", "売上", "撤退", "失敗", "再挑戦", "人脈", "ピッチ"]
    - Same 5-session upper-intermediate structure as 8.1 but all content hand-crafted for entrepreneurship topic
    - Description tone: `bold_declaration`, farewell tone: `introspective_guide`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.8, 4.1, 5.1, 5.2, 5.3, 5.4, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 7.7, 7.8, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 8.6 Create `vi-ja-intermediate-curriculums/create_nature_ecology.py` — "Thiên Nhiên Và Sinh Thái" (Series 4: Khoa Học Và Tương Lai, display order 3)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["生態系", "生物多様性", "絶滅危惧種", "食物連鎖", "光合成", "共生", "外来種", "固有種", "保護区", "森林", "湿地", "干潟", "珊瑚礁", "渡り鳥", "生息地", "環境保全", "自然遺産", "里山"]
    - Same 5-session upper-intermediate structure as 8.1 but all content hand-crafted for nature/ecology topic
    - Description tone: `vivid_scenario`, farewell tone: `team_building_energy`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.8, 4.1, 5.1, 5.2, 5.3, 5.4, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 7.7, 7.8, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 8.7 Create `vi-ja-intermediate-curriculums/create_crime_justice.py` — "Tội Phạm Và Công Lý" (Series 5: Văn Hóa Và Tư Tưởng, display order 3)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["犯罪", "捜査", "逮捕", "容疑者", "裁判", "判決", "無罪", "有罪", "刑務所", "仮釈放", "再犯", "被害者", "加害者", "冤罪", "死刑", "更生", "司法", "陪審員"]
    - Same 5-session upper-intermediate structure as 8.1 but all content hand-crafted for crime/justice topic
    - Description tone: `bold_declaration`, farewell tone: `introspective_guide`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.8, 4.1, 5.1, 5.2, 5.3, 5.4, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 7.7, 7.8, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 8.8 Create `vi-ja-intermediate-curriculums/create_ai_future.py` — "Trí Tuệ Nhân Tạo Và Tương Lai" (Series 4: Khoa Học Và Tương Lai, display order 4)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["機械学習", "深層学習", "自然言語処理", "画像認識", "自動運転", "倫理", "雇用", "代替", "共存", "創造性", "判断", "責任", "規制", "透明性", "偏り", "進化", "特異点", "汎用"]
    - Same 5-session upper-intermediate structure as 8.1 but all content hand-crafted for AI/future topic
    - Description tone: `surprising_fact`, farewell tone: `warm_accountability`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.8, 4.1, 5.1, 5.2, 5.3, 5.4, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 7.7, 7.8, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 8.9 Create `vi-ja-intermediate-curriculums/create_entertainment_tv.py` — "Giải Trí Và Truyền Hình" (Series 2: Truyền Thông Và Giải Trí, display order 4)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["番組", "バラエティ", "ドラマ", "視聴者", "脚本", "演出", "出演", "芸能人", "お笑い", "漫才", "コント", "司会", "生放送", "収録", "配信", "動画", "チャンネル登録", "再生回数"]
    - Same 5-session upper-intermediate structure as 8.1 but all content hand-crafted for entertainment/TV topic
    - Description tone: `vivid_scenario`, farewell tone: `practical_momentum`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.8, 4.1, 5.1, 5.2, 5.3, 5.4, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 7.7, 7.8, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

  - [x] 8.10 Create `vi-ja-intermediate-curriculums/create_diplomacy.py` — "Ngoại Giao Và Quan Hệ Quốc Tế" (Series 5: Văn Hóa Và Tư Tưởng, display order 4)
    - Upper-intermediate format: 5 sessions, 18 words in 3 groups of 6, price 49
    - vocabList: ["外交", "大使館", "首脳会談", "条約", "制裁", "安全保障", "同盟", "紛争", "和平", "難民", "国連", "決議", "主権", "領土", "貿易摩擦", "経済制裁", "多国間", "覇権"]
    - Same 5-session upper-intermediate structure as 8.1 but all content hand-crafted for diplomacy/international relations topic
    - Description tone: `surprising_fact`, farewell tone: `team_building_energy`
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.10, 1.11, 2.1, 2.2, 2.3, 2.5, 3.1, 3.3, 3.4, 3.5, 3.8, 4.1, 5.1, 5.2, 5.3, 5.4, 6.1, 6.2, 6.4, 6.5, 6.6, 6.8, 7.1, 7.2, 7.4, 7.5, 7.6, 7.7, 7.8, 8.1, 8.2, 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 12.1, 12.4, 12.5, 12.6, 12.7, 13.1, 14.1, 14.2, 14.3, 14.4, 16.2_

- [x] 9. Run upper-intermediate curriculum scripts
  - Execute all 10 upper-intermediate curriculum scripts (8.1–8.10) against the API
  - Each script validates content, creates curriculum, adds to series, sets display order, sets price to 49
  - Record all 10 curriculum IDs
  - Verify no `setPublic` calls made
  - _Requirements: 8.1, 8.2, 9.5, 9.6, 13.1, 16.1, 16.2_

- [x] 10. Checkpoint — All 20 curriculums created
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 10 intermediate curriculums: vocabLevel3 in Session 4, writingParagraph in Session 5, reading 250-400 chars
  - Verify 10 upper-intermediate curriculums: vocabLevel3 in Session 4, writingParagraph in Session 5, reading 350-500 chars
  - Verify all 20 prices set to 49
  - Verify language pair: all have `language="ja"`, `userLanguage="vi"`
  - Verify series membership: 4 curriculums per series, correct display orders
  - Run duplicate check queries for all 20 curriculum titles

- [x] 11. Verify all curriculums in database
  - Query database to confirm all 20 curriculums exist with correct display orders, language values, prices, and non-empty content
  - Verify collection → series → curriculum wiring is complete
  - Verify no duplicates exist
  - If verification reveals missing or malformed curriculums, recreate affected ones
  - _Requirements: 16.3, 16.4_

- [x] 12. Documentation and cleanup
  - [x] 12.1 Create `vi-ja-intermediate-curriculums/README.md`
    - Document: collection ID, all 5 series IDs, all 20 curriculum IDs with titles and display orders
    - Document: vocabulary lists per curriculum (all 20 × 18 words)
    - Document: tone assignments (description and farewell for all 20 curriculums)
    - Document: pricing (49 for all), language pair (vi-ja), formats (intermediate vs upper_intermediate)
    - Include SQL verification queries: count curriculums, verify language pair, verify prices, verify series membership and display orders, verify no duplicates, verify collection → series wiring, verify level gap within series
    - Include recreation instructions
    - _Requirements: 15.1_

  - [x] 12.2 Delete all creation scripts after verification
    - Delete `orchestrator.py`, all 20 `create_*.py` scripts, `validate_content.py`, and `test_validate.py` from `vi-ja-intermediate-curriculums/`
    - Only `README.md` remains in the directory
    - _Requirements: 15.2_

  - [x] 12.3 Run duplicate check and resolve
    - Run duplicate check query for each of the 20 curriculum titles
    - If duplicates found: keep earliest, remove from series first, then delete extras
    - _Requirements: 15.3_

- [x] 13. Final checkpoint — All tasks complete
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 20 curriculums total: 10 intermediate + 10 upper-intermediate
  - Verify collection and series structure is correct (1 collection, 5 series, 4 curriculums each)
  - Verify README.md is in place and all creation scripts are deleted
  - Verify no `setPublic` calls were made (all curriculums remain private)

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation between phases
- Property tests validate the intermediate/upper-intermediate-specific content validator (Properties 1-8) from the design
- The `validate_content.py` supports two formats: `intermediate` (vocabLevel3 in S4, writingParagraph in S5, reading 250-400/600-900 chars) and `upper_intermediate` (vocabLevel3 in S4, writingParagraph in S5, reading 350-500/800-1200 chars)
- Root-level `api_helpers.py` is reused as-is — no changes needed
- All curriculum content must be hand-crafted — no template-based generation for learner-facing text
- Both formats share the same activity structure (vocabLevel3 in S4, writingParagraph in S5); the difference is content complexity (passage length, analytical depth, furigana density)
- No `setPublic` calls — all curriculums remain private until content generation (audio, illustrations) is complete
- Japanese vocabulary uses kanji with selective furigana (N2+ only for intermediate, rare/specialized only for upper-intermediate)
