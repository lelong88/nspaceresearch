# Implementation Plan: JA-JA Advanced Curriculums

## Overview

Create 20 advanced Japanese-language curriculums for native Japanese speakers expanding their formal, academic, and specialized vocabulary. Organized into 1 collection ("日本語上級語彙マスター") and 5 series (4 curriculums each).

Implementation uses Python scripts in `ja-ja-advanced-curriculums/`. Language pair: `language="ja"`, `userLanguage="ja"` (single-language — all text in Japanese). Each curriculum has 5 sessions with 11 activities per session in fixed order, 30+ vocabulary words (6+ per session), 800-1200+ character reading passages. Each script contains all hand-crafted content inline with `build_content()`, inline `validate_content()`, and `main()` functions. The shared root-level `api_helpers.py` handles all API calls. No pricing, no setPublic calls.

Execution order: (1) property tests for validate_content(), (2) orchestrator for collection/5 series, (3) Series A scripts ×4, (4) Series B scripts ×4, (5) Series C scripts ×4, (6) Series D scripts ×4, (7) Series E scripts ×4, (8) README + cleanup.

## Tasks

- [ ] 1. Write property-based tests for validate_content()
  - [ ] 1.1 Create `ja-ja-advanced-curriculums/test_validate.py` with Hypothesis strategies and 11 property tests
    - Implement generator strategies: `valid_curriculum()` (5 sessions, 11 activities each, correct order, valid vocabLists with 6+ lowercase hiragana strings, 800+ char reading text, proper writingSentence/writingParagraph structure), `random_activity(activity_type)`, `random_vocab_list(n)`, `random_japanese_text(min_chars)`, `random_strip_key()`, `random_json_path()`
    - Import `validate_content` from a reference curriculum script (create a minimal one for testing, or define validate_content in the test file itself for testing purposes)
    - Minimum 100 iterations per property test (`@settings(max_examples=100)`)
    - _Requirements: 14.1, 14.2, 14.3_

  - [ ]* 1.2 Write property test: Top-level structure validity (Property 1)
    - **Property 1: Top-level structure validity**
    - # Feature: ja-ja-advanced-curriculums, Property 1: Top-level structure validity
    - Generate valid content, then mutate: remove title, empty description, remove preview.text, set contentTypeTags to non-empty, change learningSessions length != 5. Verify `validate_content()` raises ValueError for each mutation.
    - **Validates: Requirements 2.4, 13.1**

  - [ ]* 1.3 Write property test: Session structure completeness (Property 2)
    - **Property 2: Session structure completeness**
    - # Feature: ja-ja-advanced-curriculums, Property 2: Session structure completeness
    - Generate valid content, then mutate: wrong session title (not "セッションN"), wrong activity count (!= 11), wrong activity order. Verify `validate_content()` raises ValueError.
    - **Validates: Requirements 2.1, 2.2, 2.8, 4.7**

  - [ ]* 1.4 Write property test: VocabList structural validity (Property 3)
    - **Property 3: VocabList structural validity**
    - # Feature: ja-ja-advanced-curriculums, Property 3: VocabList structural validity
    - Generate valid content, then mutate vocab activities: make vocabList non-lowercase, use field name `words` instead of `vocabList`, reduce to <6 items, make non-array. Verify `validate_content()` raises ValueError.
    - **Validates: Requirements 3.1, 3.2, 3.3, 3.4**

  - [ ]* 1.5 Write property test: Flashcard vocabList consistency (Property 4)
    - **Property 4: Flashcard vocabList consistency**
    - # Feature: ja-ja-advanced-curriculums, Property 4: Flashcard vocabList consistency
    - Generate valid content, then make viewFlashcards and speakFlashcards in the same session have different vocabList arrays. Verify `validate_content()` raises ValueError.
    - **Validates: Requirements 3.5**

  - [ ]* 1.6 Write property test: Activity metadata completeness (Property 5)
    - **Property 5: Activity metadata completeness**
    - # Feature: ja-ja-advanced-curriculums, Property 5: Activity metadata completeness
    - Generate valid content, then remove required fields (activityType, title, description, data) or use `type` instead of `activityType`, or use invalid activityType value. Verify `validate_content()` raises ValueError.
    - **Validates: Requirements 4.1, 13.2, 13.3, 13.4**

  - [ ]* 1.7 Write property test: Title format conventions (Property 6)
    - **Property 6: Title format conventions**
    - # Feature: ja-ja-advanced-curriculums, Property 6: Title format conventions
    - Generate valid content, then change title prefixes: vocab activities not starting with "フラッシュカード：", reading/speakReading not starting with "読む：", readAlong not starting with "聴く：", writingSentence/writingParagraph not starting with "書く：". Verify `validate_content()` raises ValueError.
    - **Validates: Requirements 4.2, 4.3, 4.4, 4.6**

  - [ ]* 1.8 Write property test: Reading/audio text presence and minimum length (Property 7)
    - **Property 7: Reading/audio text presence and minimum length**
    - # Feature: ja-ja-advanced-curriculums, Property 7: Reading/audio text presence and minimum length
    - Generate valid content, then mutate: shorten reading text below 800 characters, remove data.text from reading/speakReading/readAlong/introAudio. Verify `validate_content()` raises ValueError.
    - **Validates: Requirements 7.1, 7.2, 7.3**

  - [ ]* 1.9 Write property test: Reading text consistency within session (Property 8)
    - **Property 8: Reading text consistency within session**
    - # Feature: ja-ja-advanced-curriculums, Property 8: Reading text consistency within session
    - Generate valid content, then make reading, speakReading, and readAlong in the same session have different data.text values. Verify `validate_content()` raises ValueError.
    - **Validates: Requirements 7.4**

  - [ ]* 1.10 Write property test: Forbidden keys rejection (Property 9)
    - **Property 9: Forbidden keys rejection**
    - # Feature: ja-ja-advanced-curriculums, Property 9: Forbidden keys rejection
    - Inject strip keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) and `youtubeUrl` at random depths in valid content. Verify `validate_content()` raises ValueError.
    - **Validates: Requirements 2.5, 8.1**

  - [ ]* 1.11 Write property test: WritingSentence data structure validity (Property 10)
    - **Property 10: WritingSentence data structure validity**
    - # Feature: ja-ja-advanced-curriculums, Property 10: WritingSentence data structure validity
    - Generate valid content, then mutate writingSentence: remove data.vocabList, remove data.items, make items empty, remove prompt/targetVocab from items. Verify `validate_content()` raises ValueError.
    - **Validates: Requirements 6.1**

  - [ ]* 1.12 Write property test: WritingParagraph data structure validity (Property 11)
    - **Property 11: WritingParagraph data structure validity**
    - # Feature: ja-ja-advanced-curriculums, Property 11: WritingParagraph data structure validity
    - Generate valid content, then mutate writingParagraph: remove data.vocabList, remove data.instructions, make instructions empty, remove data.prompts, make prompts length < 2. Verify `validate_content()` raises ValueError.
    - **Validates: Requirements 6.2**

- [ ] 2. Checkpoint — Property tests ready
  - Ensure all property tests pass, ask the user if questions arise.

- [ ] 3. Create orchestrator and collection/series infrastructure
  - [ ] 3.1 Create `ja-ja-advanced-curriculums/orchestrator.py`
    - Create 1 collection: "日本語上級語彙マスター" with neutral informative Japanese description
    - Create 5 series with Japanese titles and descriptions (≤255 chars each):
      - Series 1: "ビジネス・専門日本語" (tone: `bold_declaration`)
      - Series 2: "学術・知的探究" (tone: `provocative_question`)
      - Series 3: "文化・芸術" (tone: `vivid_scenario`)
      - Series 4: "社会・心理" (tone: `empathetic_observation`)
      - Series 5: "科学・技術・健康" (tone: `surprising_fact`)
    - Wire all 5 series to the collection via `add_series_to_collection`
    - Set display orders for all 5 series (1-5) via `set_series_display_order`
    - Print collection ID, all 5 series IDs, and the full tone assignment table (20 curriculums with description tone + farewell tone)
    - Uses root-level `api_helpers.py` via sys.path: `create_collection`, `create_series`, `add_series_to_collection`, `set_series_display_order`
    - No `set_price` or `setPublic` calls
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7_

- [ ] 4. Create Series A: ビジネス・専門日本語 (4 curriculum scripts)
  - [ ] 4.1 Create `ja-ja-advanced-curriculums/create_negotiation.py` — 交渉術
    - Hand-write complete curriculum content for negotiation (ja-ja, advanced, concept-based)
    - Title: "交渉術", description tone: `provocative_question`, farewell tone: `warm_accountability`
    - 30+ vocabulary words across 5 sessions (6+ per session), all hiragana/katakana lowercase in vocabList
    - Session topics: 交渉の基本原則, 利害調整, 説得技法, 合意形成, 国際交渉
    - 5 sessions × 11 activities: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading (800+ chars), speakReading, readAlong, writingSentence (4-6 items), writingParagraph (instructions + 2-3 prompts), introAudio (farewell in session 5)
    - Inline `validate_content()` function (identical structure across all 20 scripts)
    - `build_content()` returns fully literal dict — no templates, no string interpolation for learner-facing text
    - Uses root-level `api_helpers.py`: `create_curriculum`, `add_to_series`, `set_display_order`
    - Display order: 1 in Series A
    - Prints duplicate check SQL after creation
    - `contentTypeTags: []`, no `youtubeUrl`, no strip keys, no `set_price`, no `setPublic`
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.1, 15.2, 16.1, 16.2, 16.3, 16.4_

  - [ ] 4.2 Create `ja-ja-advanced-curriculums/create_organizational_theory.py` — 組織論
    - Hand-write complete curriculum content for organizational theory (ja-ja, advanced)
    - Title: "組織論", description tone: `metaphor_led`, farewell tone: `quiet_awe`
    - 30+ vocabulary words across 5 sessions (6+ per session), NO overlap with 交渉術
    - Session topics: 組織構造, リーダーシップ, 意思決定, 組織文化, 変革管理
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 2 in Series A
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.2, 16.1, 16.2, 16.3, 16.4_

  - [ ] 4.3 Create `ja-ja-advanced-curriculums/create_management_strategy.py` — 経営戦略
    - Hand-write complete curriculum content for management strategy (ja-ja, advanced)
    - Title: "経営戦略", description tone: `surprising_fact`, farewell tone: `practical_momentum`
    - 30+ vocabulary words across 5 sessions (6+ per session), NO overlap with 交渉術 or 組織論
    - Session topics: 競争優位, 市場分析, イノベーション, 事業計画, グローバル戦略
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 3 in Series A
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.2, 16.1, 16.2, 16.3, 16.4_

  - [ ] 4.4 Create `ja-ja-advanced-curriculums/create_corporate_ethics.py` — 企業倫理
    - Hand-write complete curriculum content for corporate ethics (ja-ja, advanced)
    - Title: "企業倫理", description tone: `empathetic_observation`, farewell tone: `introspective_guide`
    - 30+ vocabulary words across 5 sessions (6+ per session), NO overlap with other Series A curriculums
    - Session topics: 倫理的判断, コンプライアンス, CSR, ガバナンス, 持続可能性
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 4 in Series A
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.2, 16.1, 16.2, 16.3, 16.4_

- [ ] 5. Checkpoint — Series A complete
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 4 curriculums exist in Series A with display orders 1-4
  - Verify no vocabulary overlap across the 4 Series A curriculums
  - Verify `language="ja"`, `userLanguage="ja"` on all 4 curriculums

- [ ] 6. Create Series B: 学術・知的探究 (4 curriculum scripts)
  - [ ] 6.1 Create `ja-ja-advanced-curriculums/create_epistemology.py` — 認識論
    - Hand-write complete curriculum content for epistemology (ja-ja, advanced)
    - Title: "認識論", description tone: `bold_declaration`, farewell tone: `team_building_energy`
    - 30+ vocabulary words across 5 sessions (6+ per session), all hiragana/katakana lowercase
    - Session topics: 知識の本質, 真理と正当化, 懐疑主義, 経験と理性, 現代認識論
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 1 in Series B
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.1, 15.2, 16.1, 16.2, 16.3, 16.4_

  - [ ] 6.2 Create `ja-ja-advanced-curriculums/create_economic_thought.py` — 経済思想
    - Hand-write complete curriculum content for economic thought (ja-ja, advanced)
    - Title: "経済思想", description tone: `vivid_scenario`, farewell tone: `warm_accountability`
    - 30+ vocabulary words across 5 sessions (6+ per session), NO overlap with 認識論
    - Session topics: 古典派経済学, マルクス経済学, ケインズ理論, 新自由主義, 行動経済学
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 2 in Series B
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.2, 16.1, 16.2, 16.3, 16.4_

  - [ ] 6.3 Create `ja-ja-advanced-curriculums/create_philosophy_of_language.py` — 言語哲学
    - Hand-write complete curriculum content for philosophy of language (ja-ja, advanced)
    - Title: "言語哲学", description tone: `provocative_question`, farewell tone: `quiet_awe`
    - 30+ vocabulary words across 5 sessions (6+ per session), NO overlap with other Series B curriculums
    - Session topics: 意味と指示, 言語行為論, 言語と思考, 記号論, 語用論
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 3 in Series B
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.2, 16.1, 16.2, 16.3, 16.4_

  - [ ] 6.4 Create `ja-ja-advanced-curriculums/create_scientific_methodology.py` — 科学方法論
    - Hand-write complete curriculum content for scientific methodology (ja-ja, advanced)
    - Title: "科学方法論", description tone: `surprising_fact`, farewell tone: `practical_momentum`
    - 30+ vocabulary words across 5 sessions (6+ per session), NO overlap with other Series B curriculums
    - Session topics: 仮説演繹法, 実験計画, 統計的推論, パラダイム論, 科学と倫理
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 4 in Series B
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.2, 16.1, 16.2, 16.3, 16.4_

- [ ] 7. Checkpoint — Series B complete
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 4 curriculums exist in Series B with display orders 1-4
  - Verify no vocabulary overlap across the 4 Series B curriculums

- [ ] 8. Create Series C: 文化・芸術 (4 curriculum scripts)
  - [ ] 8.1 Create `ja-ja-advanced-curriculums/create_literary_criticism.py` — 文学批評
    - Hand-write complete curriculum content for literary criticism (ja-ja, advanced)
    - Title: "文学批評", description tone: `empathetic_observation`, farewell tone: `introspective_guide`
    - 30+ vocabulary words across 5 sessions (6+ per session), all hiragana/katakana lowercase
    - Session topics: 構造主義批評, ポスト構造主義, フェミニズム批評, 読者反応理論, 比較文学
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 1 in Series C
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.1, 15.2, 16.1, 16.2, 16.3, 16.4_

  - [ ] 8.2 Create `ja-ja-advanced-curriculums/create_aesthetics.py` — 美学と芸術論
    - Hand-write complete curriculum content for aesthetics and art theory (ja-ja, advanced)
    - Title: "美学と芸術論", description tone: `metaphor_led`, farewell tone: `team_building_energy`
    - 30+ vocabulary words across 5 sessions (6+ per session), NO overlap with 文学批評
    - Session topics: 美の概念, 芸術と模倣, 崇高と美, 現代美学, 芸術と社会
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 2 in Series C
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.2, 16.1, 16.2, 16.3, 16.4_

  - [ ] 8.3 Create `ja-ja-advanced-curriculums/create_media_theory.py` — 現代メディア論
    - Hand-write complete curriculum content for contemporary media theory (ja-ja, advanced)
    - Title: "現代メディア論", description tone: `bold_declaration`, farewell tone: `warm_accountability`
    - 30+ vocabulary words across 5 sessions (6+ per session), NO overlap with other Series C curriculums
    - Session topics: メディアリテラシー, デジタル社会, 情報倫理, 公共圏, メディア批評
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 3 in Series C
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.2, 16.1, 16.2, 16.3, 16.4_

  - [ ] 8.4 Create `ja-ja-advanced-curriculums/create_traditional_arts.py` — 伝統芸能
    - Hand-write complete curriculum content for traditional performing arts (ja-ja, advanced)
    - Title: "伝統芸能", description tone: `vivid_scenario`, farewell tone: `quiet_awe`
    - 30+ vocabulary words across 5 sessions (6+ per session), NO overlap with other Series C curriculums
    - Session topics: 能楽, 歌舞伎, 文楽, 茶道と華道, 伝統の継承
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 4 in Series C
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.2, 16.1, 16.2, 16.3, 16.4_

- [ ] 9. Checkpoint — Series C complete
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 4 curriculums exist in Series C with display orders 1-4
  - Verify no vocabulary overlap across the 4 Series C curriculums

- [ ] 10. Create Series D: 社会・心理 (4 curriculum scripts)
  - [ ] 10.1 Create `ja-ja-advanced-curriculums/create_social_psychology.py` — 社会心理学
    - Hand-write complete curriculum content for social psychology (ja-ja, advanced)
    - Title: "社会心理学", description tone: `provocative_question`, farewell tone: `practical_momentum`
    - 30+ vocabulary words across 5 sessions (6+ per session), all hiragana/katakana lowercase
    - Session topics: 集団心理, 同調と服従, 偏見と差別, 対人認知, 社会的影響
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 1 in Series D
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.1, 15.2, 16.1, 16.2, 16.3, 16.4_

  - [ ] 10.2 Create `ja-ja-advanced-curriculums/create_self_development.py` — 自己啓発と内省
    - Hand-write complete curriculum content for self-development and introspection (ja-ja, advanced)
    - Title: "自己啓発と内省", description tone: `empathetic_observation`, farewell tone: `introspective_guide`
    - 30+ vocabulary words across 5 sessions (6+ per session), NO overlap with 社会心理学
    - Session topics: 自己認識, 動機づけ, レジリエンス, マインドフルネス, 自己実現
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 2 in Series D
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.2, 16.1, 16.2, 16.3, 16.4_

  - [ ] 10.3 Create `ja-ja-advanced-curriculums/create_urban_sociology.py` — 都市社会学
    - Hand-write complete curriculum content for urban sociology (ja-ja, advanced)
    - Title: "都市社会学", description tone: `surprising_fact`, farewell tone: `team_building_energy`
    - 30+ vocabulary words across 5 sessions (6+ per session), NO overlap with other Series D curriculums
    - Session topics: 都市化, コミュニティ, 格差と分断, 公共空間, 都市再生
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 3 in Series D
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.2, 16.1, 16.2, 16.3, 16.4_

  - [ ] 10.4 Create `ja-ja-advanced-curriculums/create_intercultural_communication.py` — 異文化コミュニケーション
    - Hand-write complete curriculum content for intercultural communication (ja-ja, advanced)
    - Title: "異文化コミュニケーション", description tone: `bold_declaration`, farewell tone: `warm_accountability`
    - 30+ vocabulary words across 5 sessions (6+ per session), NO overlap with other Series D curriculums
    - Session topics: 文化的価値観, 非言語コミュニケーション, 異文化適応, ステレオタイプ, 多文化共生
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 4 in Series D
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.2, 16.1, 16.2, 16.3, 16.4_

- [ ] 11. Checkpoint — Series D complete
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 4 curriculums exist in Series D with display orders 1-4
  - Verify no vocabulary overlap across the 4 Series D curriculums

- [ ] 12. Create Series E: 科学・技術・健康 (4 curriculum scripts)
  - [ ] 12.1 Create `ja-ja-advanced-curriculums/create_ai_ethics.py` — 人工知能と倫理
    - Hand-write complete curriculum content for AI and ethics (ja-ja, advanced)
    - Title: "人工知能と倫理", description tone: `metaphor_led`, farewell tone: `quiet_awe`
    - 30+ vocabulary words across 5 sessions (6+ per session), all hiragana/katakana lowercase
    - Session topics: 機械学習の基礎, AIバイアス, 自律性と責任, プライバシー, AI共存社会
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 1 in Series E
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.1, 15.2, 16.1, 16.2, 16.3, 16.4_

  - [ ] 12.2 Create `ja-ja-advanced-curriculums/create_environmental_science.py` — 環境科学
    - Hand-write complete curriculum content for environmental science (ja-ja, advanced)
    - Title: "環境科学", description tone: `provocative_question`, farewell tone: `practical_momentum`
    - 30+ vocabulary words across 5 sessions (6+ per session), NO overlap with 人工知能と倫理
    - Session topics: 気候変動, 生態系, 資源管理, 環境政策, 持続可能な開発
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 2 in Series E
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.2, 16.1, 16.2, 16.3, 16.4_

  - [ ] 12.3 Create `ja-ja-advanced-curriculums/create_neuroscience.py` — 脳科学と認知
    - Hand-write complete curriculum content for neuroscience and cognition (ja-ja, advanced)
    - Title: "脳科学と認知", description tone: `vivid_scenario`, farewell tone: `introspective_guide`
    - 30+ vocabulary words across 5 sessions (6+ per session), NO overlap with other Series E curriculums
    - Session topics: 神経可塑性, 記憶と学習, 意識の科学, 感情と脳, 認知バイアス
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 3 in Series E
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.2, 16.1, 16.2, 16.3, 16.4_

  - [ ] 12.4 Create `ja-ja-advanced-curriculums/create_preventive_medicine.py` — 予防医学
    - Hand-write complete curriculum content for preventive medicine (ja-ja, advanced)
    - Title: "予防医学", description tone: `bold_declaration`, farewell tone: `team_building_energy`
    - 30+ vocabulary words across 5 sessions (6+ per session), NO overlap with other Series E curriculums
    - Session topics: 疫学, 生活習慣病, 公衆衛生, 免疫と予防接種, 健康格差
    - Same 5×11 activity structure, inline `validate_content()`, `build_content()` with hand-crafted content
    - Display order: 4 in Series E
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 5.2, 5.3, 5.4, 5.5, 5.7, 6.1, 6.2, 6.3, 6.4, 7.1, 7.2, 7.3, 7.4, 8.1, 9.1, 9.2, 10.1, 10.2, 11.1, 11.2, 11.3, 11.4, 12.1, 13.1, 13.2, 13.3, 13.4, 14.1, 14.2, 14.3, 15.2, 16.1, 16.2, 16.3, 16.4_

- [ ] 13. Checkpoint — Series E complete, all 20 curriculums created
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 4 curriculums exist in Series E with display orders 1-4
  - Verify no vocabulary overlap across the 4 Series E curriculums
  - Verify all 20 curriculums have `language="ja"`, `userLanguage="ja"`
  - Verify `is_public = false` on all 20 curriculums
  - Run duplicate check queries for all 20 curriculum titles

- [ ] 14. Documentation and cleanup
  - [ ] 14.1 Create `ja-ja-advanced-curriculums/README.md`
    - Document: collection ID, all 5 series IDs, all 20 curriculum IDs with titles and display orders
    - Document: vocabulary lists per curriculum (30+ words each), tone assignments (description tone + farewell tone for all 20)
    - Document: language pair (ja-ja), no pricing, no setPublic
    - Document: series structure (5 series × 4 curriculums each)
    - Include SQL verification queries: count curriculums, verify language pair, verify series membership and display orders, verify no duplicates, verify is_public = false
    - Include recreation instructions
    - _Requirements: 10.5_

  - [ ] 14.2 Delete all creation scripts after verification
    - Delete `orchestrator.py`, all 20 `create_*.py` scripts, and `test_validate.py` from `ja-ja-advanced-curriculums/`
    - Only `README.md` remains in the directory
    - _Requirements: 10.5_

  - [ ] 14.3 Run duplicate check and resolve
    - Run duplicate check query for each of the 20 curriculum titles
    - If duplicates found: keep earliest, remove from series first, then delete extras
    - _Requirements: 12.1, 12.2_

- [ ] 15. Final checkpoint — All tasks complete
  - Ensure all tests pass, ask the user if questions arise.
  - Verify 20 curriculums total across 5 series (4 per series)
  - Verify collection and series structure is correct (1 collection → 5 series → 20 curriculums)
  - Verify README.md is in place and all creation scripts are deleted
  - Verify no `setPublic` calls were made (all curriculums remain private)
  - Verify no `set_price` calls were made
  - Verify description tone distribution: no single tone exceeds 30% of 20 descriptions
  - Verify no adjacent tone duplicates within any series

## Notes

- Tasks marked with `*` are optional and can be skipped for faster MVP
- Each task references specific requirements for traceability
- Checkpoints ensure incremental validation between series
- Property tests validate the inline `validate_content()` function (Properties 1-11) from the design
- The `validate_content()` function is defined identically inline in all 20 scripts — no separate validator module
- Root-level `api_helpers.py` is reused as-is — no changes needed
- All curriculum content must be hand-crafted — no template-based generation
- Single format: 5 sessions × 11 activities, 30+ vocab words, 800+ char reading passages
- All text in Japanese (single-language advanced level for native speakers)
- Japanese vocabList format: lowercase hiragana/katakana strings (e.g., ["こうしょう", "だきょう"])
- Character-based length validation (800+ characters) instead of word count
- No vocabulary overlap within the same series
- No pricing (no set_price calls), no setPublic calls
- Tone distribution across 20 descriptions: provocative_question ×4, bold_declaration ×4, vivid_scenario ×3, empathetic_observation ×3, surprising_fact ×3, metaphor_led ×3 — max 20%, all ≤30% ✓
- Farewell tone distribution: warm_accountability ×4, quiet_awe ×4, practical_momentum ×4, introspective_guide ×4, team_building_energy ×4 — evenly distributed ✓
- No adjacent tone duplicates within any series ✓
