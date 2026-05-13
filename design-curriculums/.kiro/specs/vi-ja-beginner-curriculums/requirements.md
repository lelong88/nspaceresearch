# Requirements Document

## Introduction

Create 20 Japanese-learning curriculums specifically designed for Vietnamese-speaking adults at the beginner level. Language pair: userLanguage="vi", language="ja". All 20 curriculums are beginner level, covering diverse topics appropriate for Vietnamese adults beginning their Japanese language journey.

This is the first vi-ja curriculum set. No existing Vietnamese-Japanese content exists on the platform. These 20 curriculums establish the foundation for Japanese learning by covering essential daily life, travel, culture, work, social, nature, technology, and health topics — all areas where Vietnamese adults commonly need Japanese vocabulary.

### What This Spec Covers

- 20 individually crafted curriculums for Vietnamese adults learning Japanese at beginner level
- Diverse topics covering daily life, travel, culture, work, social situations, nature, technology, and health
- Japanese vocabulary in hiragana/katakana with romaji pronunciation guidance
- Vietnamese marketing text (titles, descriptions, previews) for beginner-level content
- Collection and series organization for the vi-ja beginner curriculum line
- Pricing per the beginner guidelines (mini = 9, short = 19)
- Creation workflow, validation, and documentation

### What This Spec Does NOT Cover

- Changes to existing curriculums in other language pairs
- Intermediate or advanced Japanese curriculums
- Kanji-focused content (beginners focus on hiragana/katakana)
- Content generation pipeline (audio, illustrations) — curriculums are created private
- Grammar-focused curriculums (these are vocabulary-based)

## Glossary

- **Beginner_Curriculum**: A curriculum designed for Vietnamese adults learning Japanese at beginner level. Uses bilingual text (Vietnamese + Japanese). Vocabulary words are Japanese in hiragana/katakana. Marketing text is in Vietnamese.
- **Curriculum_Creator**: The system of standalone Python scripts that generate curriculum JSON content and upload it via the REST API.
- **Content_Validator**: Validation logic that checks curriculum JSON against the Content Corruption Detection Rules before upload.
- **Collection_Organizer**: The orchestrator script that creates collections, series, wires them together, and sets display orders via the REST API.
- **Tone_Assigner**: The logic that assigns description tones and farewell tones to each curriculum and series, ensuring variety constraints are met.
- **Language_Pair**: userLanguage="vi", language="ja" — Vietnamese speakers learning Japanese.
- **Persuasive_Copy**: The required writing style for marketing text — emotional sales copy with bold headline, concrete examples, vivid metaphor, transformation promise, and personal growth tie-in. Written in Vietnamese for beginner-level content.
- **Tone_Palette**: The 6 rhetorical opener types: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led.
- **Farewell_Palette**: The 5 emotional registers for farewell introAudio scripts: introspective_guide, warm_accountability, team_building_energy, quiet_awe, practical_momentum.
- **Strip_Keys**: Auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never be included in new curriculum content.
- **Mini_Curriculum**: A single-session curriculum with 3-5 vocabulary words, priced at 9 credits (beginner).
- **Short_Curriculum**: A 4-session curriculum with 8-10 vocabulary words, priced at 19 credits (beginner).
- **Hiragana**: The basic Japanese phonetic script used for native Japanese words. Beginners learn this first.
- **Katakana**: The Japanese phonetic script used for foreign loanwords and emphasis. Beginners learn this alongside hiragana.
- **Romaji**: Romanized Japanese — Latin alphabet representation of Japanese pronunciation, used as pronunciation guidance for Vietnamese learners.

## Requirements

### Requirement 1: Beginner Curriculum Format and Structure

**User Story:** As a platform owner, I want 20 Japanese-learning curriculums designed for Vietnamese adults at beginner level, so that learners have diverse, accessible content to begin their Japanese language journey.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce exactly 20 Beginner_Curriculums for the vi-ja Language_Pair.
2. THE Curriculum_Creator SHALL create 8 beginner mini curriculums and 12 beginner short curriculums.
3. WHEN a beginner mini Beginner_Curriculum is created, THE curriculum SHALL contain exactly 1 learning session with 3-5 vocabulary words.
4. WHEN a beginner short Beginner_Curriculum is created, THE curriculum SHALL contain 4 learning sessions with 8-10 vocabulary words divided into 2 groups.
5. THE Beginner_Curriculum SHALL include `contentTypeTags: []` at the top level of the content JSON (topic-based).
6. THE Beginner_Curriculum SHALL never include Strip_Keys in the content JSON.
7. THE Curriculum_Creator SHALL set `language: "ja"` and `userLanguage: "vi"` as top-level body parameters in the `curriculum/create` API call.

### Requirement 2: Topic Plan for 20 Beginner Curriculums

**User Story:** As a platform owner, I want diverse topics that cover essential Japanese vocabulary for Vietnamese adults, so that learners can immediately apply what they learn in real-life situations — from daily greetings to travel, work, and cultural experiences.

#### Acceptance Criteria

1. THE 20 Beginner_Curriculums SHALL cover the following topics, each individually crafted:

   **Beginner Mini (3-5 words, 1 session, 9 credits) — 8 curriculums:**
   - Curriculum 1: "Chào Hỏi Cơ Bản" (Basic Greetings) — essential greetings: こんにちは/konnichiwa (hello), ありがとう/arigatou (thank you), すみません/sumimasen (excuse me), おはよう/ohayou (good morning), さようなら/sayounara (goodbye). vocabList: ["こんにちは", "ありがとう", "すみません", "おはよう", "さようなら"]
   - Curriculum 2: "Đếm Số Tiếng Nhật" (Japanese Numbers) — numbers 1-5: いち/ichi (one), に/ni (two), さん/san (three), し/shi (four), ご/go (five). vocabList: ["いち", "に", "さん", "し", "ご"]
   - Curriculum 3: "Gia Đình Thân Yêu" (Beloved Family) — family members: おかあさん/okaasan (mother), おとうさん/otousan (father), あに/ani (older brother), あね/ane (older sister), いもうと/imouto (younger sister). vocabList: ["おかあさん", "おとうさん", "あに", "あね", "いもうと"]
   - Curriculum 4: "Màu Sắc Quanh Ta" (Colors Around Us) — basic colors: あか/aka (red), あお/ao (blue), しろ/shiro (white), くろ/kuro (black), きいろ/kiiro (yellow). vocabList: ["あか", "あお", "しろ", "くろ", "きいろ"]
   - Curriculum 5: "Thời Tiết Hôm Nay" (Today's Weather) — weather words: てんき/tenki (weather), あめ/ame (rain), はれ/hare (sunny), くもり/kumori (cloudy), かぜ/kaze (wind). vocabList: ["てんき", "あめ", "はれ", "くもり", "かぜ"]
   - Curriculum 6: "Đồ Uống Yêu Thích" (Favorite Drinks) — common drinks: みず/mizu (water), おちゃ/ocha (tea), コーヒー/koohii (coffee), ぎゅうにゅう/gyuunyuu (milk), ジュース/juusu (juice). vocabList: ["みず", "おちゃ", "コーヒー", "ぎゅうにゅう", "ジュース"]
   - Curriculum 7: "Ngày Trong Tuần" (Days of the Week) — days: げつようび/getsuyoubi (Monday), かようび/kayoubi (Tuesday), すいようび/suiyoubi (Wednesday), もくようび/mokuyoubi (Thursday), きんようび/kinyoubi (Friday). vocabList: ["げつようび", "かようび", "すいようび", "もくようび", "きんようび"]
   - Curriculum 8: "Cảm Xúc Mỗi Ngày" (Daily Emotions) — feelings: うれしい/ureshii (happy), かなしい/kanashii (sad), たのしい/tanoshii (fun/enjoyable), つかれた/tsukareta (tired), げんき/genki (energetic/well). vocabList: ["うれしい", "かなしい", "たのしい", "つかれた", "げんき"]

   **Beginner Short (8-10 words, 4 sessions, 19 credits) — 12 curriculums:**
   - Curriculum 9: "Ẩm Thực Nhật Bản" (Japanese Cuisine) — food vocabulary: ごはん/gohan (rice), さかな/sakana (fish), にく/niku (meat), やさい/yasai (vegetables), たまご/tamago (egg), みそしる/misoshiru (miso soup), すし/sushi (sushi), ラーメン/raamen (ramen), おいしい/oishii (delicious), いただきます/itadakimasu (bon appétit). vocabList: ["ごはん", "さかな", "にく", "やさい", "たまご", "みそしる", "すし", "ラーメン", "おいしい", "いただきます"]
   - Curriculum 10: "Mua Sắm Ở Nhật" (Shopping in Japan) — shopping words: みせ/mise (shop), いくら/ikura (how much), たかい/takai (expensive), やすい/yasui (cheap), かう/kau (to buy), おかね/okane (money), レジ/reji (cash register), ふくろ/fukuro (bag), きれい/kirei (pretty/clean), おおきい/ookii (big). vocabList: ["みせ", "いくら", "たかい", "やすい", "かう", "おかね", "レジ", "ふくろ", "きれい", "おおきい"]
   - Curriculum 11: "Di Chuyển Ở Nhật" (Getting Around Japan) — transportation: でんしゃ/densha (train), バス/basu (bus), えき/eki (station), きっぷ/kippu (ticket), ちかてつ/chikatetsu (subway), タクシー/takushii (taxi), ひだり/hidari (left), みぎ/migi (right), まっすぐ/massugu (straight), とまる/tomaru (to stop). vocabList: ["でんしゃ", "バス", "えき", "きっぷ", "ちかてつ", "タクシー", "ひだり", "みぎ", "まっすぐ", "とまる"]
   - Curriculum 12: "Khách Sạn Và Lưu Trú" (Hotels and Accommodation) — hotel vocabulary: ホテル/hoteru (hotel), へや/heya (room), よやく/yoyaku (reservation), チェックイン/chekkuin (check-in), かぎ/kagi (key), おふろ/ofuro (bath), あさごはん/asagohan (breakfast), いっぱく/ippaku (one night stay), フロント/furonto (front desk), にもつ/nimotsu (luggage). vocabList: ["ホテル", "へや", "よやく", "チェックイン", "かぎ", "おふろ", "あさごはん", "いっぱく", "フロント", "にもつ"]
   - Curriculum 13: "Văn Phòng Nhật Bản" (Japanese Office) — work vocabulary: しごと/shigoto (work/job), かいしゃ/kaisha (company), かいぎ/kaigi (meeting), でんわ/denwa (telephone), メール/meeru (email), じかん/jikan (time), やすみ/yasumi (day off/break), しゃちょう/shachou (company president), どうりょう/douryou (colleague), おつかれさま/otsukaresama (good work/thank you for your effort). vocabList: ["しごと", "かいしゃ", "かいぎ", "でんわ", "メール", "じかん", "やすみ", "しゃちょう", "どうりょう", "おつかれさま"]
   - Curriculum 14: "Bốn Mùa Nhật Bản" (Four Seasons of Japan) — seasons and nature: はる/haru (spring), なつ/natsu (summer), あき/aki (autumn), ふゆ/fuyu (winter), さくら/sakura (cherry blossom), もみじ/momiji (autumn leaves), ゆき/yuki (snow), うみ/umi (sea), やま/yama (mountain), はな/hana (flower). vocabList: ["はる", "なつ", "あき", "ふゆ", "さくら", "もみじ", "ゆき", "うみ", "やま", "はな"]
   - Curriculum 15: "Sở Thích Và Giải Trí" (Hobbies and Entertainment) — hobbies: しゅみ/shumi (hobby), えいが/eiga (movie), おんがく/ongaku (music), りょこう/ryokou (travel), どくしょ/dokusho (reading), スポーツ/supootsu (sports), りょうり/ryouri (cooking), さんぽ/sanpo (walk/stroll), しゃしん/shashin (photo), カラオケ/karaoke (karaoke). vocabList: ["しゅみ", "えいが", "おんがく", "りょこう", "どくしょ", "スポーツ", "りょうり", "さんぽ", "しゃしん", "カラオケ"]
   - Curriculum 16: "Sức Khỏe Và Cơ Thể" (Health and Body) — health vocabulary: あたま/atama (head), おなか/onaka (stomach), びょういん/byouin (hospital), くすり/kusuri (medicine), いたい/itai (painful), ねつ/netsu (fever), やすむ/yasumu (to rest), からだ/karada (body), けんこう/kenkou (health), いしゃ/isha (doctor). vocabList: ["あたま", "おなか", "びょういん", "くすり", "いたい", "ねつ", "やすむ", "からだ", "けんこう", "いしゃ"]
   - Curriculum 17: "Nhà Ở Nhật Bản" (Japanese Housing) — home vocabulary: いえ/ie (house), へや/heya (room), だいどころ/daidokoro (kitchen), トイレ/toire (toilet), おふろ/ofuro (bathroom), まど/mado (window), ドア/doa (door), でんき/denki (electricity/light), たたみ/tatami (tatami mat), ふとん/futon (futon). vocabList: ["いえ", "だいどころ", "トイレ", "まど", "ドア", "でんき", "たたみ", "ふとん", "にわ", "かいだん"]
   - Curriculum 18: "Lễ Hội Nhật Bản" (Japanese Festivals) — festival vocabulary: まつり/matsuri (festival), はなび/hanabi (fireworks), ゆかた/yukata (summer kimono), おみこし/omikoshi (portable shrine), たいこ/taiko (drum), やたい/yatai (food stall), おまもり/omamori (charm/amulet), じんじゃ/jinja (shrine), おてら/otera (temple), おぼん/obon (Obon festival). vocabList: ["まつり", "はなび", "ゆかた", "おみこし", "たいこ", "やたい", "おまもり", "じんじゃ", "おてら", "おぼん"]
   - Curriculum 19: "Công Nghệ Đời Thường" (Everyday Technology) — technology words: でんしゃ/densha (train), スマホ/sumaho (smartphone), インターネット/intaanetto (internet), パソコン/pasokon (computer), アプリ/apuri (app), でんし/denshi (electronic), コンビニ/konbini (convenience store), じどうはんばいき/jidouhanbaiki (vending machine), カード/kaado (card), Wi-Fi/waifai (Wi-Fi). vocabList: ["スマホ", "インターネット", "パソコン", "アプリ", "コンビニ", "じどうはんばいき", "カード", "ワイファイ", "でんし", "アニメ"]
   - Curriculum 20: "Thể Thao Và Vận Động" (Sports and Exercise) — sports vocabulary: サッカー/sakkaa (soccer), やきゅう/yakyuu (baseball), すいえい/suiei (swimming), はしる/hashiru (to run), あるく/aruku (to walk), じてんしゃ/jitensha (bicycle), たいいく/taiiku (physical education), しあい/shiai (match/game), かつ/katsu (to win), れんしゅう/renshuu (practice). vocabList: ["サッカー", "やきゅう", "すいえい", "はしる", "あるく", "じてんしゃ", "たいいく", "しあい", "かつ", "れんしゅう"]

2. THE Curriculum_Creator SHALL select vocabulary words that are high-frequency, practical, and immediately useful for Vietnamese adults in Japan or interacting with Japanese culture.
3. THE Curriculum_Creator SHALL ensure no two curriculums have overlapping vocabulary lists (vocabList arrays must be unique across all 20 curriculums).
4. WHEN creating reading passages, THE Curriculum_Creator SHALL use simple Japanese sentences (under 10 words average) written primarily in hiragana/katakana, present tense primarily, and vocabulary that Vietnamese adults can relate to in daily life situations.
5. THE vocabList arrays SHALL use Japanese words in hiragana or katakana (as appropriate for the word), all in their standard written form.

### Requirement 3: Beginner-Level Content Design

**User Story:** As a content quality owner, I want all learner-facing content designed for adult beginners learning Japanese, so that learners feel supported with clear Vietnamese explanations while building confidence in Japanese.

#### Acceptance Criteria

1. WHEN learner-facing content is created for introAudio scripts, THE scripts SHALL use a warm, encouraging tone in Vietnamese, introducing each Japanese word with: the Japanese word (in hiragana/katakana), romaji pronunciation, Vietnamese meaning, a simple example sentence in Japanese, and a cultural note or memory hook where relevant.
2. WHEN reading passages are created, THE passages SHALL be written in simple Japanese (hiragana/katakana only, no kanji) using only vocabulary from the curriculum's vocabList and basic connector particles. Passages SHALL feature relatable adult scenarios: ordering food, asking directions, workplace greetings, shopping, seasonal activities.
3. WHEN writingSentence prompts are created, THE prompts SHALL provide clear scaffolding: Vietnamese instructions, a complete Japanese example sentence (with romaji and Vietnamese translation), and a clear word-substitution pattern requiring only 1 word change.
4. THE Beginner_Curriculum SHALL NOT include `writingParagraph` activities (too complex for beginner Japanese learners who are still learning the writing system).
5. THE Beginner_Curriculum SHALL NOT include `vocabLevel3` activities (to keep cognitive load manageable for beginners learning a new script).
6. WHEN a beginner mini Beginner_Curriculum is created, THE curriculum SHALL NOT include `vocabLevel1` or `vocabLevel2` activities (mini format focuses on flashcards, reading, and speaking).
7. THE introAudio scripts SHALL provide romaji pronunciation guidance for every Japanese word, since Vietnamese learners are unfamiliar with Japanese phonetics.

### Requirement 4: Activity Templates for Beginner Curriculums

**User Story:** As a platform owner, I want activity sequences that build Japanese reading and speaking skills progressively, so that beginners gain confidence through structured repetition and practice.

#### Acceptance Criteria

1. WHEN a beginner mini Beginner_Curriculum is created, THE session SHALL include activities in this order: introAudio (welcome + teach all words with romaji, Vietnamese meaning, and cultural context), viewFlashcards, speakFlashcards, reading (short Japanese passage in hiragana/katakana, 40-60 characters), speakReading, readAlong, introAudio (farewell with vocab review and encouragement).

2. WHEN a beginner short Beginner_Curriculum is created, THE 4 sessions SHALL follow this structure:
   - Session 1: introAudio (welcome + teach words group 1 with romaji and Vietnamese meaning), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), reading (short Japanese passage using group 1 words, 60-80 characters), readAlong, introAudio (session wrap-up)
   - Session 2: introAudio (recap group 1 + teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), reading (short Japanese passage using group 2 words, 60-80 characters), readAlong, introAudio (session wrap-up)
   - Session 3 (Review): introAudio (review intro), viewFlashcards (all words), speakFlashcards (all words), vocabLevel1 (all words), vocabLevel2 (all words), writingSentence (3-4 items), introAudio (review wrap-up)
   - Session 4 (Final): introAudio (final reading intro), reading (combined Japanese passage using all words, 100-140 characters), speakReading, readAlong, writingSentence (2-3 items), introAudio (farewell with full vocab review and celebration)

### Requirement 5: Vietnamese Marketing Copy

**User Story:** As a content quality owner, I want all marketing text (title, description, preview) written in Vietnamese for beginner-level content, so that Vietnamese learners can easily understand what they will learn and feel motivated to start.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL write curriculum descriptions as Persuasive_Copy following the 5-beat structure, addressing adult learner aspirations: career opportunities with Japanese companies, travel to Japan, understanding anime/manga/Japanese culture, personal growth through language learning.
2. THE Curriculum_Creator SHALL write curriculum previews (~100-150 words) as Persuasive_Copy with vivid hooks about the learner's Japanese journey, vocabulary word listing (Japanese + romaji + Vietnamese meaning), and what the learner will be able to do after completing the curriculum.
3. THE Curriculum_Creator SHALL write all titles, descriptions, and preview text in Vietnamese (as required for beginner vi-ja curriculums where userLanguage="vi").
4. THE Tone_Assigner SHALL assign one of the 6 Tone_Palette types to every curriculum description headline.
5. WHILE assigning tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Tone_Palette type.
6. THE Tone_Assigner SHALL ensure no single Tone_Palette type exceeds 30% of the 20 curriculum descriptions (max 6 uses per tone).
7. THE Persuasive_Copy SHALL emphasize the practical value of Japanese for Vietnamese adults: career advancement with Japanese companies operating in Vietnam, travel experiences in Japan, understanding Japanese pop culture, and the intellectual satisfaction of mastering a new writing system.

### Requirement 6: introAudio Quality

**User Story:** As a content quality owner, I want introAudio scripts that effectively teach Japanese pronunciation and meaning to Vietnamese speakers, so that learners build correct pronunciation habits from the start.

#### Acceptance Criteria

1. WHEN a welcome introAudio is created for a mini curriculum, THE script (200-350 words) SHALL greet the learner warmly in Vietnamese, introduce the topic with a motivating hook, list all vocabulary words, and teach each word with: the Japanese word (hiragana/katakana), romaji pronunciation with Vietnamese phonetic approximation where helpful, Vietnamese meaning, a simple example sentence in Japanese with Vietnamese translation, and a cultural note or memory association.
2. WHEN a welcome introAudio is created for a short curriculum, THE script (300-500 words) SHALL follow the same pattern as criterion 1 but with more words and additional cultural context (e.g., explaining Japanese customs, etiquette, or cultural significance of vocabulary).
3. WHEN a session recap introAudio is created (sessions 2+), THE script SHALL briefly recap previous Japanese words with romaji before introducing new ones — using phrases like "Bạn còn nhớ không?" (Do you remember?).
4. WHEN a farewell introAudio is created, THE script (200-400 words) SHALL review key vocabulary words with fresh Japanese example sentences (with romaji and Vietnamese translation), celebrate the learner's progress, and encourage daily practice.
5. THE introAudio scripts SHALL be primarily in Vietnamese with Japanese words/phrases introduced with romaji pronunciation and Vietnamese meaning.
6. THE Curriculum_Creator SHALL individually craft every introAudio script for its specific curriculum topic, without using template functions or string interpolation.
7. THE Tone_Assigner SHALL assign one of the 5 Farewell_Palette registers to every farewell introAudio.
8. WHILE assigning farewell tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Farewell_Palette register.

### Requirement 7: Pricing

**User Story:** As a platform owner, I want beginner curriculums priced according to the standard pricing guidelines, so that pricing is consistent with the rest of the catalog.

#### Acceptance Criteria

1. WHEN a beginner mini Beginner_Curriculum (1 session) is created, THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 9`.
2. WHEN a beginner short Beginner_Curriculum (4 sessions) is created, THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 19`.
3. THE Curriculum_Creator SHALL set the price after the curriculum is successfully created and added to its series.

### Requirement 8: Collection and Series Organization

**User Story:** As a platform owner, I want the 20 beginner curriculums organized into a dedicated vi-ja collection and series, so that learners can easily find and browse all beginner Japanese content in a logical progression.

#### Acceptance Criteria

1. THE Collection_Organizer SHALL create 1 NEW collection titled "Tiếng Nhật Cho Người Mới Bắt Đầu" (Japanese for Beginners) with a neutral, informative Vietnamese description explaining this is a collection of Japanese curriculums designed for Vietnamese adults starting their Japanese learning journey.
2. THE Collection_Organizer SHALL organize the 20 curriculums into 3 series:
   - Series 1: "Những Bước Đầu Tiên" (First Steps) — containing the 8 beginner mini curriculums. Description ≤255 chars using a Tone_Palette type. Covers essential basics: greetings, numbers, family, colors, weather, drinks, days, emotions.
   - Series 2: "Khám Phá Cuộc Sống" (Exploring Life) — containing 6 beginner short curriculums (Curriculums 9-14: food, shopping, transportation, hotel, office, seasons). Description ≤255 chars using a different Tone_Palette type.
   - Series 3: "Mở Rộng Thế Giới" (Expanding Your World) — containing 6 beginner short curriculums (Curriculums 15-20: hobbies, health, housing, festivals, technology, sports). Description ≤255 chars using a different Tone_Palette type.
3. THE Collection_Organizer SHALL wire each series to the collection via `curriculum-collection/addSeriesToCollection`.
4. THE Collection_Organizer SHALL set display orders for all 3 series within the collection via `curriculum-series/setDisplayOrder`.
5. THE Collection_Organizer SHALL set display orders for all curriculums within each series via `curriculum/setDisplayOrder`.
6. THE Collection_Organizer SHALL ensure all curriculums within each series share `language: "ja"` and `userLanguage: "vi"`.
7. WHILE assigning series description tones, THE Tone_Assigner SHALL ensure all 3 series use different Tone_Palette types.

### Requirement 9: Activity Schema Compliance

**User Story:** As a platform developer, I want every activity to comply with the platform's content schema, so that the content pipeline processes Japanese curriculums without errors.

#### Acceptance Criteria

1. Each Activity SHALL include `activityType`, `title`, `description`, and `data` fields.
2. THE `activityType` field SHALL use one of the valid values: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence.
3. THE `vocabList` field SHALL be an array of lowercase strings (Japanese words in hiragana/katakana), using the field name `vocabList` (never `words`).
4. WHEN viewFlashcards and speakFlashcards appear in the same session, THE two activities SHALL have identical `vocabList` arrays.
5. All content data SHALL be inside the `data` object, not inline on the activity object.
6. WHEN a writingSentence activity is created, THE activity SHALL have `data.vocabList`, `data.items` (non-empty array), and each item SHALL have `prompt` (Vietnamese instructions with Japanese example sentence, romaji, Vietnamese translation, and substitution pattern) and `targetVocab` fields.
7. THE Curriculum_Creator SHALL follow the activity title/description conventions: viewFlashcards/speakFlashcards/vocabLevel* use "Flashcards: <topic>"; reading/speakReading use "Đọc: <topic>"; readAlong uses "Nghe: <topic>"; introAudio uses descriptive labels; writingSentence uses "Viết: <topic>".

### Requirement 10: Content Validation

**User Story:** As a platform developer, I want every beginner curriculum validated before upload, so that no corrupted content enters the database.

#### Acceptance Criteria

1. THE Content_Validator SHALL verify that every Beginner_Curriculum content JSON has non-null, non-empty `title`, `description`, and `preview.text` fields.
2. THE Content_Validator SHALL verify that `learningSessions` is a non-empty array, with each session having a non-empty `title` and `activities` array.
3. THE Content_Validator SHALL verify that every activity has `activityType` (not `type`), `title`, `description`, and `data` fields, with content fields inside `data`.
4. THE Content_Validator SHALL verify that `activityType` values are valid.
5. THE Content_Validator SHALL verify that vocabList fields contain arrays of strings using the field name `vocabList`.
6. THE Content_Validator SHALL verify that viewFlashcards and speakFlashcards in the same session have identical vocabList arrays.
7. THE Content_Validator SHALL verify writingSentence data structures (vocabList, items with prompt and targetVocab).
8. THE Content_Validator SHALL verify that no Strip_Keys appear anywhere in the content JSON.
9. THE Content_Validator SHALL verify that no `writingParagraph` or `vocabLevel3` activities exist in any Beginner_Curriculum.
10. IF any validation check fails, THEN THE Content_Validator SHALL abort the upload and print the specific rule violation.

### Requirement 11: Script Architecture and Workflow

**User Story:** As a developer, I want a clear, repeatable workflow for creating 20 beginner curriculums, so that the process is manageable and traceable.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce one standalone Python script per curriculum (20 scripts total).
2. THE Curriculum_Creator SHALL produce one orchestrator script that creates the collection, 3 series, wires them together, and sets display orders.
3. THE Curriculum_Creator SHALL organize scripts into a directory `vi-ja-beginner-curriculums/`.
4. THE Curriculum_Creator SHALL authenticate all API calls using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
5. THE Curriculum_Creator SHALL use `https://helloapi.step.is` as the API base URL.
6. THE Curriculum_Creator SHALL individually craft every piece of learner-facing text for its specific curriculum topic, without using template functions, string interpolation, or generic fill-in-the-blank patterns.
7. THE Curriculum_Creator MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.
8. IF a curriculum creation API call fails, THEN THE Curriculum_Creator SHALL log the error with the curriculum title and continue with the next curriculum.

### Requirement 12: Newly Created Curriculums Must Be Private

**User Story:** As a platform owner, I want all newly created Japanese curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created Beginner_Curriculum.

### Requirement 13: Curriculum Titles

**User Story:** As a content quality owner, I want curriculum titles to be minimal, engaging, and in Vietnamese, so that they work well within the series/collection context.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL keep curriculum titles minimal — never repeating series/collection name, content type prefix, skill-focus label, difficulty level, or audience suffix.
2. THE Curriculum_Creator SHALL write curriculum titles in Vietnamese.
3. THE curriculum titles SHALL NOT include difficulty level indicators (e.g., "beginner", "sơ cấp", "初級").
4. THE curriculum titles SHALL be engaging and descriptive — using clear, motivating language that tells the learner what topic they will explore.

### Requirement 14: Documentation and Cleanup

**User Story:** As a developer, I want proper documentation after all curriculums are created, so that the content is traceable and reproducible.

#### Acceptance Criteria

1. WHEN all 20 curriculums are created and verified, THE Curriculum_Creator SHALL create a README.md documenting: collection ID, all series IDs, all curriculum IDs with titles and display orders, vocabulary lists per curriculum, tone assignments (description and farewell for all 20), pricing, and SQL verification queries.
2. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted, leaving only the README.
3. THE Curriculum_Creator SHALL run a duplicate check query for each curriculum title after creation and resolve any duplicates (keep earliest, delete extras).

### Requirement 15: Execution Order

**User Story:** As a developer, I want a phased execution plan, so that I can create the infrastructure first and then add curriculums incrementally.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL execute creation in this order: (1) create collection and 3 series via orchestrator, (2) create beginner mini curriculums (8 scripts), (3) create beginner short curriculums for Series 2 (6 scripts), (4) create beginner short curriculums for Series 3 (6 scripts).
2. WHEN each curriculum is created, THE Curriculum_Creator SHALL immediately add it to the appropriate series, set its display order, and set its price.
3. WHEN all 20 curriculums are created, THE Curriculum_Creator SHALL verify the complete set by querying the database to confirm all curriculums exist with correct display orders, language values, prices, and non-empty content.
4. IF verification reveals missing or malformed curriculums, THEN THE Curriculum_Creator SHALL recreate the affected curriculums before finalizing documentation.
