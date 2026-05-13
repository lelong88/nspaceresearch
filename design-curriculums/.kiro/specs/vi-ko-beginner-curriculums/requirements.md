# Requirements Document

## Introduction

Create 20 Korean-learning curriculums specifically designed for Vietnamese-speaking adults at the beginner level. Language pair: userLanguage="vi", language="ko". All 20 curriculums are beginner level, covering diverse topics appropriate for Vietnamese adults beginning their Korean language journey.

This is the first vi-ko curriculum set. No existing Vietnamese-Korean content exists on the platform. These 20 curriculums establish the foundation for Korean learning by covering essential daily life, travel, culture, work, social, nature, technology, and health topics — all areas where Vietnamese adults commonly need Korean vocabulary (many Vietnamese work in Korean companies, watch K-dramas, and listen to K-pop).

### What This Spec Covers

- 20 individually crafted curriculums for Vietnamese adults learning Korean at beginner level
- Diverse topics covering daily life, travel, culture, work, social situations, nature, technology, and health
- Korean vocabulary in Hangul with Revised Romanization pronunciation guidance
- Vietnamese marketing text (titles, descriptions, previews) for beginner-level content
- Collection and series organization for the vi-ko beginner curriculum line
- Pricing per the beginner guidelines (mini = 9, short = 19)
- Creation workflow, validation, and documentation

### What This Spec Does NOT Cover

- Changes to existing curriculums in other language pairs
- Intermediate or advanced Korean curriculums
- Hanja (Chinese characters used in Korean) — beginners focus on Hangul only
- Content generation pipeline (audio, illustrations) — curriculums are created private
- Grammar-focused curriculums (these are vocabulary-based)

## Glossary

- **Beginner_Curriculum**: A curriculum designed for Vietnamese adults learning Korean at beginner level. Uses bilingual text (Vietnamese + Korean). Vocabulary words are Korean in Hangul. Marketing text is in Vietnamese.
- **Curriculum_Creator**: The system of standalone Python scripts that generate curriculum JSON content and upload it via the REST API.
- **Content_Validator**: Validation logic that checks curriculum JSON against the Content Corruption Detection Rules before upload.
- **Collection_Organizer**: The orchestrator script that creates collections, series, wires them together, and sets display orders via the REST API.
- **Tone_Assigner**: The logic that assigns description tones and farewell tones to each curriculum and series, ensuring variety constraints are met.
- **Language_Pair**: userLanguage="vi", language="ko" — Vietnamese speakers learning Korean.
- **Persuasive_Copy**: The required writing style for marketing text — emotional sales copy with bold headline, concrete examples, vivid metaphor, transformation promise, and personal growth tie-in. Written in Vietnamese for beginner-level content.
- **Tone_Palette**: The 6 rhetorical opener types: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led.
- **Farewell_Palette**: The 5 emotional registers for farewell introAudio scripts: introspective_guide, warm_accountability, team_building_energy, quiet_awe, practical_momentum.
- **Strip_Keys**: Auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never be included in new curriculum content.
- **Mini_Curriculum**: A single-session curriculum with 3-5 vocabulary words, priced at 9 credits (beginner).
- **Short_Curriculum**: A 4-session curriculum with 8-10 vocabulary words, priced at 19 credits (beginner).
- **Hangul**: The Korean alphabet script. All Korean vocabulary for beginners is written in Hangul.
- **Revised_Romanization**: The official romanization system for Korean (e.g., 안녕하세요 = annyeonghaseyo). Used as pronunciation guidance for Vietnamese learners.
- **Speech_Levels**: Korean has multiple politeness levels. Beginners learn 합니다체 (formal polite) and 해요체 (informal polite) forms.

## Requirements

### Requirement 1: Beginner Curriculum Format and Structure

**User Story:** As a platform owner, I want 20 Korean-learning curriculums designed for Vietnamese adults at beginner level, so that learners have diverse, accessible content to begin their Korean language journey.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce exactly 20 Beginner_Curriculums for the vi-ko Language_Pair.
2. THE Curriculum_Creator SHALL create 8 beginner mini curriculums and 12 beginner short curriculums.
3. WHEN a beginner mini Beginner_Curriculum is created, THE curriculum SHALL contain exactly 1 learning session with 3-5 vocabulary words.
4. WHEN a beginner short Beginner_Curriculum is created, THE curriculum SHALL contain 4 learning sessions with 8-10 vocabulary words divided into 2 groups.
5. THE Beginner_Curriculum SHALL include `contentTypeTags: []` at the top level of the content JSON (topic-based).
6. THE Beginner_Curriculum SHALL never include Strip_Keys in the content JSON.
7. THE Curriculum_Creator SHALL set `language: "ko"` and `userLanguage: "vi"` as top-level body parameters in the `curriculum/create` API call.

### Requirement 2: Topic Plan for 20 Beginner Curriculums

**User Story:** As a platform owner, I want diverse topics that cover essential Korean vocabulary for Vietnamese adults, so that learners can immediately apply what they learn in real-life situations — from daily greetings to travel, work, and cultural experiences.

#### Acceptance Criteria

1. THE 20 Beginner_Curriculums SHALL cover the following topics, each individually crafted:

   **Beginner Mini (3-5 words, 1 session, 9 credits) — 8 curriculums:**
   - Curriculum 1: "Chào Hỏi Cơ Bản" (Basic Greetings) — essential Korean greetings: 안녕하세요/annyeonghaseyo (hello), 감사합니다/gamsahamnida (thank you), 죄송합니다/joesonghamnida (sorry), 안녕히 가세요/annyeonghi gaseyo (goodbye - to person leaving), 네/ne (yes). vocabList: ["안녕하세요", "감사합니다", "죄송합니다", "안녕히 가세요", "네"]
   - Curriculum 2: "Đếm Số Tiếng Hàn" (Korean Numbers) — Sino-Korean numbers 1-5: 일/il (one), 이/i (two), 삼/sam (three), 사/sa (four), 오/o (five). vocabList: ["일", "이", "삼", "사", "오"]
   - Curriculum 3: "Gia Đình Thân Yêu" (Beloved Family) — family members: 어머니/eomeoni (mother), 아버지/abeoji (father), 형/hyeong (older brother - male speaker), 언니/eonni (older sister - female speaker), 동생/dongsaeng (younger sibling). vocabList: ["어머니", "아버지", "형", "언니", "동생"]
   - Curriculum 4: "Màu Sắc Quanh Ta" (Colors Around Us) — basic colors: 빨간색/ppalgansaek (red), 파란색/paransaek (blue), 하얀색/hayansaek (white), 검은색/geomeunsaek (black), 노란색/noransaek (yellow). vocabList: ["빨간색", "파란색", "하얀색", "검은색", "노란색"]
   - Curriculum 5: "Thời Tiết Hôm Nay" (Today's Weather) — weather words: 날씨/nalssi (weather), 비/bi (rain), 맑음/malgeum (sunny/clear), 흐림/heurim (cloudy), 바람/baram (wind). vocabList: ["날씨", "비", "맑음", "흐림", "바람"]
   - Curriculum 6: "Đồ Uống Yêu Thích" (Favorite Drinks) — common drinks: 물/mul (water), 차/cha (tea), 커피/keopi (coffee), 우유/uyu (milk), 주스/juseu (juice). vocabList: ["물", "차", "커피", "우유", "주스"]
   - Curriculum 7: "Ngày Trong Tuần" (Days of the Week) — days: 월요일/woryoil (Monday), 화요일/hwayoil (Tuesday), 수요일/suyoil (Wednesday), 목요일/mogyoil (Thursday), 금요일/geumyoil (Friday). vocabList: ["월요일", "화요일", "수요일", "목요일", "금요일"]
   - Curriculum 8: "Cảm Xúc Mỗi Ngày" (Daily Emotions) — feelings: 행복하다/haengbokhada (happy), 슬프다/seulpeuda (sad), 즐겁다/jeulgeopda (fun/enjoyable), 피곤하다/pigonhada (tired), 좋다/jota (good/nice). vocabList: ["행복하다", "슬프다", "즐겁다", "피곤하다", "좋다"]

   **Beginner Short (8-10 words, 4 sessions, 19 credits) — 12 curriculums:**
   - Curriculum 9: "Ẩm Thực Hàn Quốc" (Korean Cuisine) — food vocabulary: 밥/bap (rice/meal), 김치/gimchi (kimchi), 고기/gogi (meat), 야채/yachae (vegetables), 계란/gyeran (egg), 된장찌개/doenjang-jjigae (soybean paste stew), 비빔밥/bibimbap (bibimbap), 라면/ramyeon (ramen), 맛있다/masitda (delicious), 잘 먹겠습니다/jal meokgesseumnida (bon appétit). vocabList: ["밥", "김치", "고기", "야채", "계란", "된장찌개", "비빔밥", "라면", "맛있다", "잘 먹겠습니다"]
   - Curriculum 10: "Mua Sắm Ở Hàn Quốc" (Shopping in Korea) — shopping words: 가게/gage (shop), 얼마예요/eolmayeyo (how much), 비싸다/bissada (expensive), 싸다/ssada (cheap), 사다/sada (to buy), 돈/don (money), 카드/kadeu (card), 봉투/bongtu (bag), 예쁘다/yeppeuda (pretty), 크다/keuda (big). vocabList: ["가게", "얼마예요", "비싸다", "싸다", "사다", "돈", "카드", "봉투", "예쁘다", "크다"]
   - Curriculum 11: "Di Chuyển Ở Hàn Quốc" (Getting Around Korea) — transportation: 지하철/jihacheol (subway), 버스/beoseu (bus), 역/yeok (station), 표/pyo (ticket), 택시/taeksi (taxi), 공항/gonghang (airport), 왼쪽/oenjjok (left), 오른쪽/oreunjjok (right), 직진/jikjin (straight), 내리다/naerida (to get off). vocabList: ["지하철", "버스", "역", "표", "택시", "공항", "왼쪽", "오른쪽", "직진", "내리다"]
   - Curriculum 12: "Khách Sạn Và Lưu Trú" (Hotels and Accommodation) — hotel vocabulary: 호텔/hotel (hotel), 방/bang (room), 예약/yeyak (reservation), 체크인/chekeu-in (check-in), 열쇠/yeolsoe (key), 화장실/hwajangsil (bathroom), 아침 식사/achim siksa (breakfast), 하루/haru (one day), 프런트/peuronteu (front desk), 짐/jim (luggage). vocabList: ["호텔", "방", "예약", "체크인", "열쇠", "화장실", "아침 식사", "하루", "프런트", "짐"]
   - Curriculum 13: "Văn Phòng Hàn Quốc" (Korean Office) — work vocabulary: 일/il (work), 회사/hoesa (company), 회의/hoeui (meeting), 전화/jeonhwa (telephone), 이메일/imeil (email), 시간/sigan (time), 휴가/hyuga (vacation/day off), 사장님/sajangnim (boss/CEO), 동료/dongnyo (colleague), 수고하셨습니다/sugohasyeosseumnida (good work/thank you for your effort). vocabList: ["일", "회사", "회의", "전화", "이메일", "시간", "휴가", "사장님", "동료", "수고하셨습니다"]
   - Curriculum 14: "Bốn Mùa Hàn Quốc" (Four Seasons of Korea) — seasons and nature: 봄/bom (spring), 여름/yeoreum (summer), 가을/gaeul (autumn), 겨울/gyeoul (winter), 벚꽃/beotkkot (cherry blossom), 단풍/danpung (autumn leaves), 눈/nun (snow), 바다/bada (sea), 산/san (mountain), 꽃/kkot (flower). vocabList: ["봄", "여름", "가을", "겨울", "벚꽃", "단풍", "눈", "바다", "산", "꽃"]
   - Curriculum 15: "Sở Thích Và Giải Trí" (Hobbies and Entertainment) — hobbies: 취미/chwimi (hobby), 영화/yeonghwa (movie), 음악/eumak (music), 여행/yeohaeng (travel), 독서/dokseo (reading), 운동/undong (exercise/sports), 요리/yori (cooking), 산책/sanchaek (walk/stroll), 사진/sajin (photo), 노래방/noraebang (karaoke room). vocabList: ["취미", "영화", "음악", "여행", "독서", "운동", "요리", "산책", "사진", "노래방"]
   - Curriculum 16: "Sức Khỏe Và Cơ Thể" (Health and Body) — health vocabulary: 머리/meori (head), 배/bae (stomach), 병원/byeongwon (hospital), 약/yak (medicine), 아프다/apeuda (painful/sick), 열/yeol (fever), 쉬다/swida (to rest), 몸/mom (body), 건강/geongang (health), 의사/uisa (doctor). vocabList: ["머리", "배", "병원", "약", "아프다", "열", "쉬다", "몸", "건강", "의사"]
   - Curriculum 17: "Nhà Ở Hàn Quốc" (Korean Housing) — home vocabulary: 집/jip (house), 방/bang (room), 부엌/bueok (kitchen), 화장실/hwajangsil (bathroom), 거실/geosil (living room), 창문/changmun (window), 문/mun (door), 에어컨/eeokon (air conditioner), 온돌/ondol (heated floor), 이사/isa (moving house). vocabList: ["집", "부엌", "거실", "창문", "문", "에어컨", "온돌", "이사", "냉장고", "세탁기"]
   - Curriculum 18: "Văn Hóa Hàn Quốc" (Korean Culture & Traditions) — culture vocabulary: 한복/hanbok (traditional Korean clothing), 설날/seollal (Lunar New Year), 추석/chuseok (Korean Thanksgiving), 김장/gimjang (kimchi-making season), 노래방/noraebang (karaoke room), 찜질방/jjimjilbang (Korean spa/sauna), 소주/soju (soju), 삼겹살/samgyeopsal (pork belly BBQ), 한류/hallyu (Korean Wave), 드라마/deurama (K-drama). vocabList: ["한복", "설날", "추석", "김장", "찜질방", "소주", "삼겹살", "한류", "드라마", "케이팝"]
   - Curriculum 19: "Công Nghệ Đời Thường" (Everyday Technology) — technology words: 핸드폰/haendeupon (cellphone), 인터넷/inteonet (internet), 컴퓨터/keompyuteo (computer), 앱/aep (app), 편의점/pyeonuijeom (convenience store), 배달/baedal (delivery), 카카오톡/kakao-tok (KakaoTalk messenger), 와이파이/waipai (Wi-Fi), 충전/chungjeon (charging), 검색/geomsaek (search). vocabList: ["핸드폰", "인터넷", "컴퓨터", "앱", "편의점", "배달", "카카오톡", "와이파이", "충전", "검색"]
   - Curriculum 20: "Thể Thao Và Vận Động" (Sports and Exercise) — sports vocabulary: 축구/chukgu (soccer), 야구/yagu (baseball), 수영/suyeong (swimming), 달리기/dalligi (running), 걷기/geotgi (walking), 자전거/jajeongeo (bicycle), 태권도/taekwondo (taekwondo), 경기/gyeonggi (match/game), 이기다/igida (to win), 연습/yeonseup (practice). vocabList: ["축구", "야구", "수영", "달리기", "걷기", "자전거", "태권도", "경기", "이기다", "연습"]

2. THE Curriculum_Creator SHALL select vocabulary words that are high-frequency, practical, and immediately useful for Vietnamese adults in Korea or interacting with Korean culture (K-drama, K-pop, Korean companies in Vietnam).
3. THE Curriculum_Creator SHALL ensure no two curriculums have overlapping vocabulary lists (vocabList arrays must be unique across all 20 curriculums).
4. WHEN creating reading passages, THE Curriculum_Creator SHALL use simple Korean sentences (under 10 words average) written in Hangul, using polite speech level (해요체), and vocabulary that Vietnamese adults can relate to in daily life situations.
5. THE vocabList arrays SHALL use Korean words in Hangul in their standard dictionary or polite form.

### Requirement 3: Beginner-Level Content Design

**User Story:** As a content quality owner, I want all learner-facing content designed for adult beginners learning Korean, so that learners feel supported with clear Vietnamese explanations while building confidence in Korean.

#### Acceptance Criteria

1. WHEN learner-facing content is created for introAudio scripts, THE scripts SHALL use a warm, encouraging tone in Vietnamese, introducing each Korean word with: the Korean word (in Hangul), Revised Romanization pronunciation, Vietnamese meaning, a simple example sentence in Korean, and a cultural note or memory hook where relevant.
2. WHEN reading passages are created, THE passages SHALL be written in simple Korean (Hangul only) using only vocabulary from the curriculum's vocabList and basic connector particles. Passages SHALL feature relatable adult scenarios: ordering food, asking directions, workplace greetings, shopping, seasonal activities. Passages SHALL use polite speech level (해요체) appropriate for beginners.
3. WHEN writingSentence prompts are created, THE prompts SHALL provide clear scaffolding: Vietnamese instructions, a complete Korean example sentence (with romanization and Vietnamese translation), and a clear word-substitution pattern requiring only 1 word change.
4. THE Beginner_Curriculum SHALL NOT include `writingParagraph` activities (too complex for beginner Korean learners who are still learning Hangul reading fluency).
5. THE Beginner_Curriculum SHALL NOT include `vocabLevel3` activities (to keep cognitive load manageable for beginners learning a new script).
6. WHEN a beginner mini Beginner_Curriculum is created, THE curriculum SHALL NOT include `vocabLevel1` or `vocabLevel2` activities (mini format focuses on flashcards, reading, and speaking).
7. THE introAudio scripts SHALL provide Revised Romanization pronunciation guidance for every Korean word, with Vietnamese phonetic approximations where helpful (e.g., explaining that ㅓ sounds similar to Vietnamese "ơ"), since Vietnamese learners are unfamiliar with Korean phonetics.

### Requirement 4: Activity Templates for Beginner Curriculums

**User Story:** As a platform owner, I want activity sequences that build Korean reading and speaking skills progressively, so that beginners gain confidence through structured repetition and practice.

#### Acceptance Criteria

1. WHEN a beginner mini Beginner_Curriculum is created, THE session SHALL include activities in this order: introAudio (welcome + teach all words with romanization, Vietnamese meaning, and cultural context), viewFlashcards, speakFlashcards, reading (short Korean passage in Hangul, 40-60 characters), speakReading, readAlong, introAudio (farewell with vocab review and encouragement).

2. WHEN a beginner short Beginner_Curriculum is created, THE 4 sessions SHALL follow this structure:
   - Session 1: introAudio (welcome + teach words group 1 with romanization and Vietnamese meaning), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), reading (short Korean passage using group 1 words, 60-80 characters), readAlong, introAudio (session wrap-up)
   - Session 2: introAudio (recap group 1 + teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), reading (short Korean passage using group 2 words, 60-80 characters), readAlong, introAudio (session wrap-up)
   - Session 3 (Review): introAudio (review intro), viewFlashcards (all words), speakFlashcards (all words), vocabLevel1 (all words), vocabLevel2 (all words), writingSentence (3-4 items), introAudio (review wrap-up)
   - Session 4 (Final): introAudio (final reading intro), reading (combined Korean passage using all words, 100-140 characters), speakReading, readAlong, writingSentence (2-3 items), introAudio (farewell with full vocab review and celebration)

### Requirement 5: Vietnamese Marketing Copy

**User Story:** As a content quality owner, I want all marketing text (title, description, preview) written in Vietnamese for beginner-level content, so that Vietnamese learners can easily understand what they will learn and feel motivated to start.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL write curriculum descriptions as Persuasive_Copy following the 5-beat structure, addressing adult learner aspirations: career opportunities with Korean companies (Samsung, LG, Hyundai), travel to Korea, understanding K-drama/K-pop culture, personal growth through language learning.
2. THE Curriculum_Creator SHALL write curriculum previews (~100-150 words) as Persuasive_Copy with vivid hooks about the learner's Korean journey, vocabulary word listing (Korean + romanization + Vietnamese meaning), and what the learner will be able to do after completing the curriculum.
3. THE Curriculum_Creator SHALL write all titles, descriptions, and preview text in Vietnamese (as required for beginner vi-ko curriculums where userLanguage="vi").
4. THE Tone_Assigner SHALL assign one of the 6 Tone_Palette types to every curriculum description headline.
5. WHILE assigning tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Tone_Palette type.
6. THE Tone_Assigner SHALL ensure no single Tone_Palette type exceeds 30% of the 20 curriculum descriptions (max 6 uses per tone).
7. THE Persuasive_Copy SHALL emphasize the practical value of Korean for Vietnamese adults: career advancement with Korean companies operating in Vietnam (Samsung, LG, Hyundai, Lotte), travel experiences in Korea, understanding K-drama and K-pop culture, and the intellectual satisfaction of mastering Hangul.

### Requirement 6: introAudio Quality

**User Story:** As a content quality owner, I want introAudio scripts that effectively teach Korean pronunciation and meaning to Vietnamese speakers, so that learners build correct pronunciation habits from the start.

#### Acceptance Criteria

1. WHEN a welcome introAudio is created for a mini curriculum, THE script (200-350 words) SHALL greet the learner warmly in Vietnamese, introduce the topic with a motivating hook, list all vocabulary words, and teach each word with: the Korean word (Hangul), Revised Romanization pronunciation with Vietnamese phonetic approximation where helpful, Vietnamese meaning, a simple example sentence in Korean with Vietnamese translation, and a cultural note or memory association.
2. WHEN a welcome introAudio is created for a short curriculum, THE script (300-500 words) SHALL follow the same pattern as criterion 1 but with more words and additional cultural context (e.g., explaining Korean customs, speech levels, or cultural significance of vocabulary).
3. WHEN a session recap introAudio is created (sessions 2+), THE script SHALL briefly recap previous Korean words with romanization before introducing new ones — using phrases like "Bạn còn nhớ không?" (Do you remember?).
4. WHEN a farewell introAudio is created, THE script (200-400 words) SHALL review key vocabulary words with fresh Korean example sentences (with romanization and Vietnamese translation), celebrate the learner's progress, and encourage daily practice.
5. THE introAudio scripts SHALL be primarily in Vietnamese with Korean words/phrases introduced with Revised Romanization pronunciation and Vietnamese meaning.
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

**User Story:** As a platform owner, I want the 20 beginner curriculums organized into a dedicated vi-ko collection and series, so that learners can easily find and browse all beginner Korean content in a logical progression.

#### Acceptance Criteria

1. THE Collection_Organizer SHALL create 1 NEW collection titled "Tiếng Hàn Cho Người Mới Bắt Đầu" (Korean for Beginners) with a neutral, informative Vietnamese description explaining this is a collection of Korean curriculums designed for Vietnamese adults starting their Korean learning journey.
2. THE Collection_Organizer SHALL organize the 20 curriculums into 3 series:
   - Series 1: "Những Bước Đầu Tiên" (First Steps) — containing the 8 beginner mini curriculums. Description ≤255 chars using a Tone_Palette type. Covers essential basics: greetings, numbers, family, colors, weather, drinks, days, emotions.
   - Series 2: "Khám Phá Cuộc Sống" (Exploring Life) — containing 6 beginner short curriculums (Curriculums 9-14: food, shopping, transportation, hotel, office, seasons). Description ≤255 chars using a different Tone_Palette type.
   - Series 3: "Mở Rộng Thế Giới" (Expanding Your World) — containing 6 beginner short curriculums (Curriculums 15-20: hobbies, health, housing, culture, technology, sports). Description ≤255 chars using a different Tone_Palette type.
3. THE Collection_Organizer SHALL wire each series to the collection via `curriculum-collection/addSeriesToCollection`.
4. THE Collection_Organizer SHALL set display orders for all 3 series within the collection via `curriculum-series/setDisplayOrder`.
5. THE Collection_Organizer SHALL set display orders for all curriculums within each series via `curriculum/setDisplayOrder`.
6. THE Collection_Organizer SHALL ensure all curriculums within each series share `language: "ko"` and `userLanguage: "vi"`.
7. WHILE assigning series description tones, THE Tone_Assigner SHALL ensure all 3 series use different Tone_Palette types.

### Requirement 9: Activity Schema Compliance

**User Story:** As a platform developer, I want every activity to comply with the platform's content schema, so that the content pipeline processes Korean curriculums without errors.

#### Acceptance Criteria

1. Each Activity SHALL include `activityType`, `title`, `description`, and `data` fields.
2. THE `activityType` field SHALL use one of the valid values: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence.
3. THE `vocabList` field SHALL be an array of lowercase strings (Korean words in Hangul), using the field name `vocabList` (never `words`).
4. WHEN viewFlashcards and speakFlashcards appear in the same session, THE two activities SHALL have identical `vocabList` arrays.
5. All content data SHALL be inside the `data` object, not inline on the activity object.
6. WHEN a writingSentence activity is created, THE activity SHALL have `data.vocabList`, `data.items` (non-empty array), and each item SHALL have `prompt` (Vietnamese instructions with Korean example sentence, romanization, Vietnamese translation, and substitution pattern) and `targetVocab` fields.
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
3. THE Curriculum_Creator SHALL organize scripts into a directory `vi-ko-beginner-curriculums/`.
4. THE Curriculum_Creator SHALL authenticate all API calls using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
5. THE Curriculum_Creator SHALL use `https://helloapi.step.is` as the API base URL.
6. THE Curriculum_Creator SHALL individually craft every piece of learner-facing text for its specific curriculum topic, without using template functions, string interpolation, or generic fill-in-the-blank patterns.
7. THE Curriculum_Creator MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.
8. IF a curriculum creation API call fails, THEN THE Curriculum_Creator SHALL log the error with the curriculum title and continue with the next curriculum.

### Requirement 12: Newly Created Curriculums Must Be Private

**User Story:** As a platform owner, I want all newly created Korean curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created Beginner_Curriculum.

### Requirement 13: Curriculum Titles

**User Story:** As a content quality owner, I want curriculum titles to be minimal, engaging, and in Vietnamese, so that they work well within the series/collection context.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL keep curriculum titles minimal — never repeating series/collection name, content type prefix, skill-focus label, difficulty level, or audience suffix.
2. THE Curriculum_Creator SHALL write curriculum titles in Vietnamese.
3. THE curriculum titles SHALL NOT include difficulty level indicators (e.g., "beginner", "sơ cấp", "초급").
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
