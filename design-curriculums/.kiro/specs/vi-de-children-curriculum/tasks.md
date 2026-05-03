# Implementation Plan: Vietnamese-German Children's Curriculum

## Overview

Create 22 German-learning curriculums for Vietnamese children aged 6-10, organized into 1 NEW collection "Tiếng Đức Cho Bé 6-10 Tuổi" and 3 series. Scripts go in `vi-de-children-curriculum/`. Reuses root-level `api_helpers.py`.

Three formats: beginner_mini (1 session, 3-5 words, price 9), beginner_short (4 sessions, 8-10 words, price 19), preintermediate_short (4 sessions, 10-12 words, price 49). Language pair: userLanguage="vi", language="de".

Execution order: (1) create validator, (2) run orchestrator to create collection + 3 series, (3) beginner mini scripts x6, (4) beginner short scripts x8, (5) preintermediate short scripts x8, (6) documentation + cleanup.

## Tasks

- [x] 1. Create children-specific content validator
  - [x] 1.1 Create `vi-de-children-curriculum/validate_content.py` with format-aware `validate(content, format)` function
    - `format` parameter: `"beginner_mini"`, `"beginner_short"`, or `"preintermediate_short"`
    - Format-specific checks: session count (1 for mini, 4 for short/preintermediate), vocab count range (3-5 for mini, 8-10 for beginner_short, 10-12 for preintermediate_short)
    - Forbidden activities: `writingParagraph` and `vocabLevel3` forbidden in ALL children's formats; `vocabLevel1` and `vocabLevel2` additionally forbidden in `beginner_mini`
    - Shared checks: top-level structure (title, description, preview.text, contentTypeTags: [], learningSessions), session structure, activity structure (activityType/title/description/data), vocabList format (array of lowercase strings), flashcard consistency, writingSentence structure, strip-keys exclusion
    - German-specific: Python `str.islower()` naturally supports umlauts (ä, ö, ü) and ß; multi-word entries with spaces/hyphens are valid (e.g., "wie viel", "zähne putzen", "nach hause gehen", "gute nacht")
    - Raise `ValueError` with specific violation message identifying the rule, location, and expected vs actual value
    - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 10.10_

  - [x] 1.2 Write property tests for validate_content.py
    - **Property 1: Valid content passes validation**
    - **Property 2: Forbidden activities are rejected per format**
    - **Property 3: Strip keys are rejected anywhere in the JSON tree**
    - **Property 4: Activities missing required fields are rejected**
    - **Property 5: Invalid activityType values are rejected**
    - **Property 6: vocabList format is enforced**
    - **Property 7: Flashcard vocabList consistency within sessions**
    - **Property 8: writingSentence structure is enforced**
    - Use Hypothesis library, minimum 100 iterations per property
    - Generate German-style strings with umlauts (ä, ö, ü), ß, and multi-word entries
    - **Validates: Requirements 10.1-10.9, 14.5, 14.6**

- [x] 2. Create orchestrator script
  - [x] 2.1 Create `vi-de-children-curriculum/orchestrator.py`
    - Create 1 collection: "Tiếng Đức Cho Bé 6-10 Tuổi" with neutral Vietnamese description
    - Create 3 series: "Bước Đầu Tiên" (bold_declaration tone), "Xây Nền Vững Chắc" (vivid_scenario tone), "Khám Phá Thêm" (empathetic_observation tone)
    - Series descriptions: <=255 chars, each using a different Tone_Palette type
    - Wire all 3 series to the collection via `add_series_to_collection`
    - Set series display orders: Series 1 = 1, Series 2 = 2, Series 3 = 3
    - Print collection_id and all 3 series_ids for use in curriculum scripts
    - Uses root-level `api_helpers.py` (create_collection, create_series, add_series_to_collection, set_series_display_order)
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 11.2, 11.4, 11.5, 11.9_

- [x] 3. Checkpoint — Infrastructure ready
  - Run orchestrator, verify collection and 3 series exist in DB
  - Record collection_id and series_ids for curriculum scripts

- [x] 4. Create beginner mini curriculum scripts (6 scripts, Series 1: "Bước Đầu Tiên")
  - [x] 4.1 Create `vi-de-children-curriculum/create_colors.py` — "Thế Giới Màu Sắc"
    - Beginner mini format: 1 session, 5 words, price 9
    - vocabList: ["rot", "blau", "grün", "gelb", "weiß"]
    - Activity sequence: introAudio (welcome, 200-350 words, teach rot/blau/grün/gelb/weiß with German pronunciation guidance + Vietnamese meaning) -> viewFlashcards -> speakFlashcards -> reading (short German passage, 40-60 words) -> speakReading -> readAlong -> introAudio (farewell, 200-400 words)
    - Description tone: `provocative_question`, farewell tone: `introspective_guide`
    - Series 1, display order: 1
    - introAudio: primarily Vietnamese, German words with pronunciation guidance in simple Vietnamese terms + Vietnamese meaning
    - Reading passage: entirely in German
    - No vocabLevel1, vocabLevel2, writingParagraph, or vocabLevel3
    - Validate with `validate(content, "beginner_mini")` before upload
    - _Requirements: 1.1, 1.3, 1.6, 1.7, 1.8, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 5.1, 5.2, 5.3, 5.4, 5.7, 6.1, 6.4, 6.5, 6.6, 6.7, 7.1, 9.1-9.7, 11.1, 11.6, 11.9, 12.1, 13.1-13.4, 14.1, 14.2, 14.3, 14.5, 17.1, 17.2_

  - [x] 4.2 Create `vi-de-children-curriculum/create_numbers.py` — "Đếm Từ 1 Đến 5"
    - Beginner mini format: 1 session, 5 words, price 9
    - vocabList: ["eins", "zwei", "drei", "vier", "fünf"]
    - Same activity sequence as 4.1 but all content hand-crafted for numbers topic
    - Description tone: `bold_declaration`, farewell tone: `warm_accountability`
    - Series 1, display order: 2
    - _Requirements: same as 4.1_

  - [x] 4.3 Create `vi-de-children-curriculum/create_family.py` — "Gia Đình Yêu Thương"
    - Beginner mini format: 1 session, 5 words, price 9
    - vocabList: ["mama", "papa", "bruder", "schwester", "baby"]
    - Same activity sequence as 4.1 but all content hand-crafted for family topic
    - Description tone: `vivid_scenario`, farewell tone: `team_building_energy`
    - Series 1, display order: 3
    - _Requirements: same as 4.1_

  - [x] 4.4 Create `vi-de-children-curriculum/create_fruits.py` — "Trái Cây Ngon Lành"
    - Beginner mini format: 1 session, 5 words, price 9
    - vocabList: ["apfel", "banane", "orange", "erdbeere", "traube"]
    - Same activity sequence as 4.1 but all content hand-crafted for fruits topic
    - Description tone: `empathetic_observation`, farewell tone: `quiet_awe`
    - Series 1, display order: 4
    - _Requirements: same as 4.1_

  - [x] 4.5 Create `vi-de-children-curriculum/create_pets.py` — "Bạn Thú Cưng"
    - Beginner mini format: 1 session, 5 words, price 9
    - vocabList: ["hund", "katze", "fisch", "vogel", "kaninchen"]
    - Same activity sequence as 4.1 but all content hand-crafted for pets topic
    - Description tone: `surprising_fact`, farewell tone: `practical_momentum`
    - Series 1, display order: 5
    - _Requirements: same as 4.1_

  - [x] 4.6 Create `vi-de-children-curriculum/create_greetings.py` — "Chào Hỏi Vui Vẻ"
    - Beginner mini format: 1 session, 5 words, price 9
    - vocabList: ["hallo", "danke", "tschüss", "bitte", "ja"]
    - Same activity sequence as 4.1 but all content hand-crafted for greetings topic
    - Description tone: `metaphor_led`, farewell tone: `introspective_guide`
    - Series 1, display order: 6
    - _Requirements: same as 4.1_

- [x] 5. Checkpoint — All beginner mini curriculums created
  - Verify 6 curriculums exist in Series 1 with display orders 1-6
  - Verify prices: all 6 at price 9
  - Verify language pair: all have `language="de"`, `userLanguage="vi"`
  - Run duplicate check for all 6 titles

- [x] 6. Create beginner short curriculum scripts (8 scripts, Series 2: "Xây Nền Vững Chắc")
  - [x] 6.1 Create `vi-de-children-curriculum/create_school.py` — "Một Ngày Ở Trường"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["schule", "buch", "stift", "tisch", "lehrer", "klasse", "heft", "tasche", "pause", "hausaufgabe"]
    - Session 1: introAudio -> viewFlashcards (group 1) -> speakFlashcards (group 1) -> vocabLevel1 (group 1) -> reading (German passage, 60-80 words) -> readAlong -> introAudio
    - Session 2: introAudio -> viewFlashcards (group 2) -> speakFlashcards (group 2) -> vocabLevel1 (group 2) -> reading (German passage, 60-80 words) -> readAlong -> introAudio
    - Session 3: introAudio -> viewFlashcards (all) -> speakFlashcards (all) -> vocabLevel1 (all) -> vocabLevel2 (all) -> writingSentence (3-4 items) -> introAudio
    - Session 4: introAudio -> reading (combined German passage, 100-120 words) -> speakReading -> readAlong -> writingSentence (2-3 items) -> introAudio (farewell)
    - Description tone: `bold_declaration`, farewell tone: `warm_accountability`
    - Series 2, display order: 1
    - introAudio: primarily Vietnamese with German word + pronunciation guidance + Vietnamese meaning
    - Reading passages: entirely in German
    - writingSentence: Vietnamese instructions with German example (+ Vietnamese translation) + substitution pattern
    - _Requirements: 1.1, 1.4, 1.6, 1.7, 1.8, 2.1, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 4.2, 5.1, 5.2, 5.3, 5.4, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 7.2, 9.1-9.7, 11.1, 11.6, 11.9, 12.1, 13.1-13.4, 14.1, 14.2, 14.3, 14.5, 17.1, 17.2_

  - [x] 6.2 Create `vi-de-children-curriculum/create_german_food.py` — "Món Ăn Đức"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["brot", "käse", "wurst", "suppe", "milch", "hähnchen", "kuchen", "salat", "wasser", "schokolade"]
    - Same 4-session structure as 6.1 but all content hand-crafted for German food topic
    - Description tone: `vivid_scenario`, farewell tone: `team_building_energy`
    - Series 2, display order: 2
    - Include cultural context about German food culture (Bratwurst, Wurst varieties, Bäckerei/bakery culture, Käse traditions)
    - _Requirements: same as 6.1 + 14.4_

  - [x] 6.3 Create `vi-de-children-curriculum/create_playground.py` — "Sân Chơi Vui Nhộn"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["laufen", "springen", "spielen", "lachen", "singen", "malen", "freund", "ball", "rutsche", "schaukel"]
    - Same 4-session structure as 6.1 but all content hand-crafted for playground topic
    - Description tone: `provocative_question`, farewell tone: `quiet_awe`
    - Series 2, display order: 3
    - _Requirements: same as 6.1_

  - [x] 6.4 Create `vi-de-children-curriculum/create_body.py` — "Cơ Thể Của Em"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["kopf", "hand", "fuß", "auge", "ohr", "mund", "nase", "bauch", "haar", "zahn"]
    - Same 4-session structure as 6.1 but all content hand-crafted for body parts topic
    - Description tone: `surprising_fact`, farewell tone: `practical_momentum`
    - Series 2, display order: 4
    - _Requirements: same as 6.1_

  - [x] 6.5 Create `vi-de-children-curriculum/create_weather.py` — "Thời Tiết Hôm Nay"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["sonne", "regen", "wind", "kalt", "heiß", "schnee", "wolke", "sturm", "regenbogen", "regenschirm"]
    - Same 4-session structure as 6.1 but all content hand-crafted for weather topic
    - Description tone: `empathetic_observation`, farewell tone: `introspective_guide`
    - Series 2, display order: 5
    - _Requirements: same as 6.1_

  - [x] 6.6 Create `vi-de-children-curriculum/create_wardrobe.py` — "Tủ Quần Áo"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["hemd", "hose", "kleid", "schuhe", "hut", "socken", "mantel", "rock", "schal", "handschuhe"]
    - Same 4-session structure as 6.1 but all content hand-crafted for clothing topic
    - Description tone: `metaphor_led`, farewell tone: `warm_accountability`
    - Series 2, display order: 6
    - _Requirements: same as 6.1_

  - [x] 6.7 Create `vi-de-children-curriculum/create_vehicles.py` — "Xe Cộ Quanh Em"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["auto", "bus", "zug", "flugzeug", "fahrrad", "schiff", "u-bahn", "motorrad", "schnell", "langsam"]
    - Same 4-session structure as 6.1 but all content hand-crafted for vehicles topic
    - Description tone: `bold_declaration`, farewell tone: `team_building_energy`
    - Series 2, display order: 7
    - _Requirements: same as 6.1_

  - [x] 6.8 Create `vi-de-children-curriculum/create_animals.py` — "Con Vật Đáng Yêu"
    - Beginner short format: 4 sessions, 10 words, price 19
    - vocabList: ["elefant", "löwe", "giraffe", "affe", "tiger", "bär", "pinguin", "schlange", "zebra", "papagei"]
    - Same 4-session structure as 6.1 but all content hand-crafted for zoo animals topic
    - Description tone: `vivid_scenario`, farewell tone: `quiet_awe`
    - Series 2, display order: 8
    - _Requirements: same as 6.1_

- [x] 7. Checkpoint — All beginner short curriculums created
  - Verify 8 curriculums exist in Series 2 with display orders 1-8
  - Verify prices: all 8 at price 19
  - Verify language pair: all have `language="de"`, `userLanguage="vi"`
  - Run duplicate check for all 8 titles

- [x] 8. Create preintermediate short curriculum scripts (8 scripts, Series 3: "Khám Phá Thêm")
  - [x] 8.1 Create `vi-de-children-curriculum/create_nature.py` — "Khám Phá Thiên Nhiên"
    - Preintermediate short format: 4 sessions, 12 words, price 49
    - vocabList: ["wald", "fluss", "berg", "schmetterling", "blume", "blatt", "baum", "himmel", "stern", "mond", "garten", "gras"]
    - Session 1: introAudio -> viewFlashcards (group 1) -> speakFlashcards (group 1) -> vocabLevel1 (group 1) -> vocabLevel2 (group 1) -> reading (German passage, 80-100 words) -> speakReading -> readAlong -> introAudio
    - Session 2: introAudio -> viewFlashcards (group 2) -> speakFlashcards (group 2) -> vocabLevel1 (group 2) -> vocabLevel2 (group 2) -> reading (German passage, 80-100 words) -> speakReading -> readAlong -> introAudio
    - Session 3: introAudio -> viewFlashcards (all) -> speakFlashcards (all) -> vocabLevel1 (all) -> vocabLevel2 (all) -> writingSentence (4-5 items) -> introAudio
    - Session 4: introAudio -> reading (combined German passage, 150-180 words) -> speakReading -> readAlong -> writingSentence (3-4 items) -> introAudio (farewell)
    - Description tone: `surprising_fact`, farewell tone: `practical_momentum`
    - Series 3, display order: 1
    - introAudio: primarily Vietnamese with German word + pronunciation guidance + Vietnamese meaning
    - Reading passages: entirely in German
    - writingSentence: Vietnamese instructions with German example (+ Vietnamese translation) + substitution pattern
    - _Requirements: 1.1, 1.5, 1.6, 1.7, 1.8, 2.1, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 4.3, 5.1, 5.2, 5.3, 5.4, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 7.3, 9.1-9.7, 11.1, 11.6, 11.9, 12.1, 13.1-13.4, 14.1, 14.2, 14.3, 14.5, 17.1, 17.2_

  - [x] 8.2 Create `vi-de-children-curriculum/create_family_meals.py` — "Bữa Ăn Gia Đình"
    - Preintermediate short format: 4 sessions, 12 words, price 49
    - vocabList: ["frühstück", "mittagessen", "abendessen", "teller", "gabel", "messer", "löffel", "glas", "küche", "lecker", "essen", "trinken"]
    - Same 4-session structure as 8.1 but all content hand-crafted for family meals topic
    - Description tone: `metaphor_led`, farewell tone: `introspective_guide`
    - Series 3, display order: 2
    - Include cultural context about German mealtime traditions (Frühstück with Brötchen, Mittagessen as main meal, Abendbrot)
    - _Requirements: same as 8.1 + 14.4_

  - [x] 8.3 Create `vi-de-children-curriculum/create_seasons.py` — "Bốn Mùa Trong Năm"
    - Preintermediate short format: 4 sessions, 12 words, price 49
    - vocabList: ["frühling", "sommer", "herbst", "winter", "schwimmen", "ski", "strand", "blätter", "blühen", "schneemann", "ferien", "hitze"]
    - Same 4-session structure as 8.1 but all content hand-crafted for seasons topic
    - Description tone: `empathetic_observation`, farewell tone: `warm_accountability`
    - Series 3, display order: 3
    - _Requirements: same as 8.1_

  - [x] 8.4 Create `vi-de-children-curriculum/create_shopping.py` — "Đi Chợ Cùng Mẹ"
    - Preintermediate short format: 4 sessions, 12 words, price 49
    - vocabList: ["kaufen", "verkaufen", "geld", "wie viel", "teuer", "markt", "gemüse", "obst", "tüte", "bezahlen", "geschäft", "preis"]
    - Same 4-session structure as 8.1 but all content hand-crafted for shopping topic
    - Description tone: `provocative_question`, farewell tone: `team_building_energy`
    - Series 3, display order: 4
    - _Requirements: same as 8.1_

  - [x] 8.5 Create `vi-de-children-curriculum/create_daily_routines.py` — "Sinh Hoạt Hàng Ngày"
    - Preintermediate short format: 4 sessions, 12 words, price 49
    - vocabList: ["aufwachen", "zähne putzen", "waschen", "morgen", "schlafen", "nachmittag", "nach hause gehen", "lesen", "snack", "abend", "nacht", "gute nacht"]
    - Same 4-session structure as 8.1 but all content hand-crafted for daily routines topic
    - Description tone: `bold_declaration`, farewell tone: `quiet_awe`
    - Series 3, display order: 5
    - _Requirements: same as 8.1_

  - [x] 8.6 Create `vi-de-children-curriculum/create_house.py` — "Ngôi Nhà Của Em"
    - Preintermediate short format: 4 sessions, 12 words, price 49
    - vocabList: ["haus", "schlafzimmer", "wohnzimmer", "esszimmer", "badezimmer", "tür", "fenster", "bett", "treppe", "dach", "schlüssel", "wand"]
    - Same 4-session structure as 8.1 but all content hand-crafted for house topic
    - Description tone: `vivid_scenario`, farewell tone: `practical_momentum`
    - Series 3, display order: 6
    - _Requirements: same as 8.1_

  - [x] 8.7 Create `vi-de-children-curriculum/create_sports.py` — "Thể Thao Sôi Động"
    - Preintermediate short format: 4 sessions, 12 words, price 49
    - vocabList: ["fußball", "turnen", "basketball", "tennis", "tanzen", "klettern", "werfen", "fangen", "tor", "gewinnen", "mannschaft", "meister"]
    - Same 4-session structure as 8.1 but all content hand-crafted for sports topic
    - Description tone: `surprising_fact`, farewell tone: `introspective_guide`
    - Series 3, display order: 7
    - _Requirements: same as 8.1_

  - [x] 8.8 Create `vi-de-children-curriculum/create_christmas_market.py` — "Chợ Giáng Sinh"
    - Preintermediate short format: 4 sessions, 12 words, price 49
    - vocabList: ["weihnachtsmarkt", "lebkuchen", "glühwein", "geschenk", "weihnachtsbaum", "kerze", "nikolaus", "adventskalender", "plätzchen", "glocke", "krippe", "fest"]
    - Same 4-session structure as 8.1 but all content hand-crafted for Christmas market topic
    - Description tone: `metaphor_led`, farewell tone: `warm_accountability`
    - Series 3, display order: 8
    - Include cultural context about German Weihnachtsmarkt tradition (Lebkuchen, Nikolaus, Adventskalender, comparing festive spirit to Vietnamese Tết markets)
    - _Requirements: same as 8.1 + 14.4_

- [x] 9. Checkpoint — All 22 curriculums created
  - Verify 6 curriculums in Series 1 with display orders 1-6
  - Verify 8 curriculums in Series 2 with display orders 1-8
  - Verify 8 curriculums in Series 3 with display orders 1-8
  - Verify prices: 6 mini at 9, 8 short at 19, 8 preintermediate at 49
  - Verify language pair: all have `language="de"`, `userLanguage="vi"`
  - Run duplicate check for all 22 titles
  - Verify zero vocabulary overlap between all 22 curriculums

- [x] 10. Documentation and cleanup
  - [x] 10.1 Create `vi-de-children-curriculum/README.md` with full documentation
    - Collection ID, all 3 series IDs
    - All 22 curriculum IDs with titles, display orders, vocabulary lists (German word + Vietnamese meaning), tone assignments, pricing
    - SQL verification queries
    - _Requirements: 15.1_

  - [x] 10.2 Delete all creation scripts after verification
    - Delete all 22 `create_*.py` scripts and `orchestrator.py` from `vi-de-children-curriculum/`
    - Only `README.md` and `validate_content.py` remain in the directory
    - _Requirements: 15.2_

  - [x] 10.3 Run duplicate check and resolve
    - Run duplicate check query for each of the 22 curriculum titles
    - If duplicates found: keep earliest, remove from series first, then delete extras
    - _Requirements: 15.3_

- [x] 11. Final checkpoint — All tasks complete
  - Verify 22 new curriculums total: 6 mini + 8 short + 8 preintermediate
  - Verify collection and series structure is correct (1 collection, 3 series, 22 curriculums)
  - Verify README.md is complete and all creation scripts are deleted
  - Verify no `setPublic` calls were made (all curriculums remain private)
  - Verify validator file remains at `vi-de-children-curriculum/validate_content.py`

## Notes

- This is the FIRST vi-de children's batch — orchestrator creates new collection and 3 series
- Collection: "Tiếng Đức Cho Bé 6-10 Tuổi" (German for Kids 6-10)
- Series 1: "Bước Đầu Tiên" (First Steps) — 6 beginner mini curriculums, series tone: bold_declaration
- Series 2: "Xây Nền Vững Chắc" (Building Strong Foundations) — 8 beginner short curriculums, series tone: vivid_scenario
- Series 3: "Khám Phá Thêm" (Explore More) — 8 preintermediate short curriculums, series tone: empathetic_observation
- Root-level `api_helpers.py` is reused as-is — no changes needed
- All curriculum content must be hand-crafted — no template-based generation for learner-facing text
- Vietnamese session titles: "Phần 1" (mini), "Phần 1"/"Phần 2"/"Ôn tập"/"Đọc tổng hợp" (short/preintermediate)
- All marketing text (title, description, preview) in Vietnamese targeting parents
- All learner-facing content: introAudio primarily in Vietnamese with German words + pronunciation guidance + Vietnamese meaning
- Reading passages: entirely in German
- vocabList: German words in standard lowercase form with umlauts (ä, ö, ü) and ß preserved
- Multi-word vocab items allowed (e.g., "wie viel", "zähne putzen", "nach hause gehen", "gute nacht", "u-bahn")
- Zero vocabulary overlap between all 22 curriculums
- Tone assignments pre-planned in Requirement 17 — no adjacent duplicates, no tone >30%
- Farewell tones evenly distributed: 4-5 uses each across 5 registers
- German-specific pronunciation guidance: explain umlauts (ä, ö, ü), ß, "sch", "ch" sounds in child-friendly Vietnamese terms
- German-specific cultural content: Bratwurst/Wurst, Weihnachtsmarkt, Lebkuchen, Nikolaus, Adventskalender
- writingSentence prompts: Vietnamese instructions + German example (+ Vietnamese translation) + substitution pattern
- No writingParagraph or vocabLevel3 in any curriculum
- Beginner mini also excludes vocabLevel1 and vocabLevel2
