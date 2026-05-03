# Implementation Plan: Vietnamese-Chinese Children's Curriculum

## Overview

Create 22 Chinese-learning curriculums for Vietnamese children aged 6-10, organized into 1 NEW collection "Tieng Trung Cho Be 6-10 Tuoi" and 3 series. Scripts go in `vi-zh-children-curriculum/`. Reuses root-level `api_helpers.py`.

Three formats: beginner_mini (1 session, 3-5 words, price 9), beginner_short (4 sessions, 8-10 words, price 19), preintermediate_short (4 sessions, 10-12 words, price 49). Language pair: userLanguage="vi", language="zh".

Execution order: (1) create validator, (2) run orchestrator to create collection + 3 series, (3) beginner mini scripts x6, (4) beginner short scripts x8, (5) preintermediate short scripts x8, (6) documentation + cleanup.

## Tasks

- [x] 1. Create children-specific content validator
  - [x] 1.1 Create `vi-zh-children-curriculum/validate_content.py` with format-aware `validate(content, format)` function
    - `format` parameter: `"beginner_mini"`, `"beginner_short"`, or `"preintermediate_short"`
    - Format-specific checks: session count (1 for mini, 4 for short/preintermediate), vocab count range (3-5 for mini, 8-10 for beginner_short, 10-12 for preintermediate_short)
    - Forbidden activities: `writingParagraph` and `vocabLevel3` forbidden in ALL children's formats; `vocabLevel1` and `vocabLevel2` additionally forbidden in `beginner_mini`
    - Shared checks: top-level structure (title, description, preview.text, contentTypeTags: [], learningSessions), session structure, activity structure (activityType/title/description/data), vocabList format (array of lowercase strings), flashcard consistency, writingSentence structure, strip-keys exclusion
    - Raise `ValueError` with specific violation message identifying the rule, location, and expected vs actual value
    - _Requirements: 10.1, 10.2, 10.3, 10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 10.10_

- [x] 2. Create orchestrator script
  - [x] 2.1 Create `vi-zh-children-curriculum/orchestrator.py`
    - Create 1 collection: "Tieng Trung Cho Be 6-10 Tuoi" with neutral Vietnamese description
    - Create 3 series: "Buoc Dau Tien" (bold_declaration tone), "Xay Nen Vung Chac" (vivid_scenario tone), "Kham Pha Them" (empathetic_observation tone)
    - Series descriptions: <=255 chars, each using a different Tone_Palette type
    - Wire all 3 series to the collection via `add_series_to_collection`
    - Set series display orders: Series 1 = 1, Series 2 = 2, Series 3 = 3
    - Print collection_id and all 3 series_ids for use in curriculum scripts
    - Uses root-level `api_helpers.py` (create_collection, create_series, add_series_to_collection, set_series_display_order)
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5, 8.6, 8.7, 11.2, 11.4, 11.5, 11.9_

- [x] 3. Checkpoint — Infrastructure ready
  - Run orchestrator, verify collection and 3 series exist in DB
  - Record collection_id and series_ids for curriculum scripts

- [x] 4. Create beginner mini curriculum scripts (6 scripts, Series 1: "Buoc Dau Tien")
  - [x] 4.1 Create `vi-zh-children-curriculum/create_colors.py` — "The Gioi Mau Sac"
    - Beginner mini format: 1 session, 5 words (hong, lan, lv, huang, bai), price 9
    - Activity sequence: introAudio (welcome, 200-350 words, teach 红/蓝/绿/黄/白 with pinyin + Vietnamese) -> viewFlashcards -> speakFlashcards -> reading (30-50 Chinese characters only) -> speakReading -> readAlong -> introAudio (farewell, 200-400 words)
    - Description tone: `provocative_question`, farewell tone: `introspective_guide`
    - Series 1, display order: 1
    - introAudio: primarily Vietnamese, Chinese words as character + pinyin + Vietnamese meaning
    - Reading passage: Chinese characters only (no pinyin in reading text)
    - Validate with `validate(content, "beginner_mini")` before upload
    - _Requirements: 1.1, 1.3, 1.6, 1.7, 1.8, 2.1, 3.1, 3.2, 3.4, 3.5, 3.6, 3.7, 4.1, 5.1, 5.2, 5.3, 5.4, 5.7, 6.1, 6.4, 6.5, 6.6, 6.7, 7.1, 9.1-9.7, 11.1, 11.6, 11.9, 12.1, 13.1-13.4, 14.1, 14.2, 14.3, 14.5, 17.1, 17.2_

  - [x] 4.2 Create `vi-zh-children-curriculum/create_numbers.py` — "Dem Tu 1 Den 10"
    - Beginner mini format: 1 session, 5 words (yi, er, san, si, wu), price 9
    - Same activity sequence as 4.1 but all content hand-crafted for numbers topic
    - Description tone: `bold_declaration`, farewell tone: `warm_accountability`
    - Series 1, display order: 2
    - _Requirements: same as 4.1_

  - [x] 4.3 Create `vi-zh-children-curriculum/create_family.py` — "Gia Dinh Yeu Thuong"
    - Beginner mini format: 1 session, 5 words (mama, baba, gege, jiejie, didi), price 9
    - Same activity sequence as 4.1 but all content hand-crafted for family topic
    - Description tone: `vivid_scenario`, farewell tone: `team_building_energy`
    - Series 1, display order: 3
    - _Requirements: same as 4.1_

  - [x] 4.4 Create `vi-zh-children-curriculum/create_fruits.py` — "Trai Cay Ngon Lanh"
    - Beginner mini format: 1 session, 5 words (pingguo, xiangjiao, xigua, putao, chengzi), price 9
    - Same activity sequence as 4.1 but all content hand-crafted for fruits topic
    - Description tone: `empathetic_observation`, farewell tone: `quiet_awe`
    - Series 1, display order: 4
    - _Requirements: same as 4.1_

  - [x] 4.5 Create `vi-zh-children-curriculum/create_pets.py` — "Ban Thu Cung"
    - Beginner mini format: 1 session, 5 words (xiao gou, mao, yu, niao, tuzi), price 9
    - Same activity sequence as 4.1 but all content hand-crafted for pets topic
    - Description tone: `surprising_fact`, farewell tone: `practical_momentum`
    - Series 1, display order: 5
    - _Requirements: same as 4.1_

  - [x] 4.6 Create `vi-zh-children-curriculum/create_greetings.py` — "Chao Hoi Vui Ve"
    - Beginner mini format: 1 session, 5 words (ni hao, xie xie, zai jian, dui bu qi, mei guan xi), price 9
    - Same activity sequence as 4.1 but all content hand-crafted for greetings topic
    - Description tone: `metaphor_led`, farewell tone: `introspective_guide`
    - Series 1, display order: 6
    - _Requirements: same as 4.1_

- [x] 5. Checkpoint — All beginner mini curriculums created
  - Verify 6 curriculums exist in Series 1 with display orders 1-6
  - Verify prices: all 6 at price 9
  - Verify language pair: all have `language="zh"`, `userLanguage="vi"`
  - Run duplicate check for all 6 titles

- [x] 6. Create beginner short curriculum scripts (8 scripts, Series 2: "Xay Nen Vung Chac")
  - [x] 6.1 Create `vi-zh-children-curriculum/create_school.py` — "Mot Ngay O Truong"
    - Beginner short format: 4 sessions, 10 words (laoshi, tongxue, shu, bi, zhuozi, shang ke, xia ke, zuoye, jiaoshi, shubao), price 19
    - Session 1: introAudio -> viewFlashcards (group 1) -> speakFlashcards (group 1) -> vocabLevel1 (group 1) -> reading (50-70 chars) -> readAlong -> introAudio
    - Session 2: introAudio -> viewFlashcards (group 2) -> speakFlashcards (group 2) -> vocabLevel1 (group 2) -> reading (50-70 chars) -> readAlong -> introAudio
    - Session 3: introAudio -> viewFlashcards (all) -> speakFlashcards (all) -> vocabLevel1 (all) -> vocabLevel2 (all) -> writingSentence (3-4 items) -> introAudio
    - Session 4: introAudio -> reading (80-110 chars) -> speakReading -> readAlong -> writingSentence (2-3 items) -> introAudio (farewell)
    - Description tone: `bold_declaration`, farewell tone: `warm_accountability`
    - Series 2, display order: 1
    - introAudio: primarily Vietnamese with Chinese character + pinyin + Vietnamese meaning
    - Reading passages: Chinese characters only
    - writingSentence: Vietnamese instructions with Chinese example (character + pinyin + translation) + substitution pattern
    - _Requirements: 1.1, 1.4, 1.6, 1.7, 1.8, 2.1, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 4.2, 5.1, 5.2, 5.3, 5.4, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 7.2, 9.1-9.7, 11.1, 11.6, 11.9, 12.1, 13.1-13.4, 14.1, 14.2, 14.3, 14.5, 17.1, 17.2_

  - [x] 6.2 Create `vi-zh-children-curriculum/create_chinese_food.py` — "Do An Trung Hoa"
    - Beginner short format: 4 sessions, 10 words (mifan, miantiao, jiaozi, baozi, tang, cha, kuaizi, hao chi, e, bao), price 19
    - Same 4-session structure as 6.1 but all content hand-crafted for Chinese food topic
    - Description tone: `vivid_scenario`, farewell tone: `team_building_energy`
    - Series 2, display order: 2
    - Include cultural context about Chinese food (chopsticks, dumplings, tea culture)
    - _Requirements: same as 6.1 + 14.4_

  - [x] 6.3 Create `vi-zh-children-curriculum/create_playground.py` — "San Choi Vui Nhon"
    - Beginner short format: 4 sessions, 10 words (pao, tiao, wan, xiao, chang ge, hua hua, pengyou, kai xin, yi qi, you xi), price 19
    - Same 4-session structure as 6.1 but all content hand-crafted for playground topic
    - Description tone: `provocative_question`, farewell tone: `quiet_awe`
    - Series 2, display order: 3
    - _Requirements: same as 6.1_

  - [x] 6.4 Create `vi-zh-children-curriculum/create_body.py` — "Co The Cua Em"
    - Beginner short format: 4 sessions, 10 words (tou, shou, jiao, yanjing, erduo, zuiba, bizi, duzi, toufa, yachi), price 19
    - Same 4-session structure as 6.1 but all content hand-crafted for body parts topic
    - Description tone: `surprising_fact`, farewell tone: `practical_momentum`
    - Series 2, display order: 4
    - _Requirements: same as 6.1_

  - [x] 6.5 Create `vi-zh-children-curriculum/create_weather.py` — "Thoi Tiet Hom Nay"
    - Beginner short format: 4 sessions, 10 words (taiyang, xia yu, gua feng, leng, re, xue, yun, tianqi, nuanhuo, liangkuai), price 19
    - Same 4-session structure as 6.1 but all content hand-crafted for weather topic
    - Description tone: `empathetic_observation`, farewell tone: `introspective_guide`
    - Series 2, display order: 5
    - _Requirements: same as 6.1_

  - [x] 6.6 Create `vi-zh-children-curriculum/create_wardrobe.py` — "Tu Quan Ao"
    - Beginner short format: 4 sessions, 10 words (yifu, kuzi, qunzi, xiezi, maozi, wazi, waitao, chuan, piaoliang, xin), price 19
    - Same 4-session structure as 6.1 but all content hand-crafted for clothing topic
    - Description tone: `metaphor_led`, farewell tone: `warm_accountability`
    - Series 2, display order: 6
    - _Requirements: same as 6.1_

  - [x] 6.7 Create `vi-zh-children-curriculum/create_vehicles.py` — "Xe Co Quanh Em"
    - Beginner short format: 4 sessions, 10 words (qiche, gonggong qiche, huoche, feiji, zixingche, xiao chuan, ditie, kuai, man, zuo), price 19
    - Same 4-session structure as 6.1 but all content hand-crafted for vehicles topic
    - Description tone: `bold_declaration`, farewell tone: `team_building_energy`
    - Series 2, display order: 7
    - _Requirements: same as 6.1_

  - [x] 6.8 Create `vi-zh-children-curriculum/create_animals.py` — "Con Vat Dang Yeu"
    - Beginner short format: 4 sessions, 10 words (daxiang, xiongmao, laohu, changjinglu, qi e, shizi, hema, eyu, daishu, kongque), price 19
    - Same 4-session structure as 6.1 but all content hand-crafted for zoo animals topic
    - Description tone: `vivid_scenario`, farewell tone: `quiet_awe`
    - Series 2, display order: 8
    - Include cultural context about pandas being China's national treasure
    - _Requirements: same as 6.1 + 14.4_

- [x] 7. Checkpoint — All beginner short curriculums created
  - Verify 8 curriculums exist in Series 2 with display orders 1-8
  - Verify prices: all 8 at price 19
  - Verify language pair: all have `language="zh"`, `userLanguage="vi"`
  - Run duplicate check for all 8 titles

- [x] 8. Create preintermediate short curriculum scripts (8 scripts, Series 3: "Kham Pha Them")
  - [x] 8.1 Create `vi-zh-children-curriculum/create_lunar_new_year.py` — "Tet Nguyen Dan"
    - Preintermediate short format: 4 sessions, 12 words (chun jie, hong bao, bian pao, deng long, bai nian, tuan yuan, nian ye fan, wu long, fu, chun lian, ya sui qian, fang jia), price 49
    - Session 1: introAudio -> viewFlashcards (group 1) -> speakFlashcards (group 1) -> vocabLevel1 (group 1) -> vocabLevel2 (group 1) -> reading (70-90 chars) -> speakReading -> readAlong -> introAudio
    - Session 2: introAudio -> viewFlashcards (group 2) -> speakFlashcards (group 2) -> vocabLevel1 (group 2) -> vocabLevel2 (group 2) -> reading (70-90 chars) -> speakReading -> readAlong -> introAudio
    - Session 3: introAudio -> viewFlashcards (all) -> speakFlashcards (all) -> vocabLevel1 (all) -> vocabLevel2 (all) -> writingSentence (4-5 items) -> introAudio
    - Session 4: introAudio -> reading (120-160 chars) -> speakReading -> readAlong -> writingSentence (3-4 items) -> introAudio (farewell)
    - Description tone: `surprising_fact`, farewell tone: `practical_momentum`
    - Series 3, display order: 1
    - Include cultural context connecting Chinese and Vietnamese Lunar New Year traditions
    - _Requirements: 1.1, 1.5, 1.6, 1.7, 1.8, 2.1, 3.1, 3.2, 3.3, 3.4, 3.5, 3.7, 4.3, 5.1, 5.2, 5.3, 5.4, 5.7, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 7.3, 9.1-9.7, 11.1, 11.6, 11.9, 12.1, 13.1-13.4, 14.1, 14.2, 14.3, 14.4, 14.5, 17.1, 17.2_

  - [x] 8.2 Create `vi-zh-children-curriculum/create_zodiac.py` — "Muoi Hai Con Giap"
    - Preintermediate short format: 4 sessions, 12 words (lao shu, niu, hu, tu, long, she, ma, yang, hou, ji, gou, zhu), price 49
    - Same 4-session structure as 8.1 but all content hand-crafted for zodiac topic
    - Description tone: `metaphor_led`, farewell tone: `introspective_guide`
    - Series 3, display order: 2
    - Include cultural context about Chinese zodiac and how Vietnamese zodiac is similar
    - _Requirements: same as 8.1_

  - [x] 8.3 Create `vi-zh-children-curriculum/create_nature.py` — "Kham Pha Thien Nhien"
    - Preintermediate short format: 4 sessions, 12 words (shan, he, da shu, hua, cao, tiankong, xingxing, yueliang, hai, feng, yezi, zhongzi), price 49
    - Same 4-session structure as 8.1 but all content hand-crafted for nature topic
    - Description tone: `empathetic_observation`, farewell tone: `warm_accountability`
    - Series 3, display order: 3
    - _Requirements: same as 8.1_

  - [x] 8.4 Create `vi-zh-children-curriculum/create_shopping.py` — "Di Cho Cung Me"
    - Preintermediate short format: 4 sessions, 12 words (mai3, mai4, qian, duo shao qian, gui, pian yi, shui guo, shu cai, chao shi, fu qian, zhao qian, dai zi), price 49
    - Same 4-session structure as 8.1 but all content hand-crafted for shopping topic
    - Description tone: `provocative_question`, farewell tone: `team_building_energy`
    - Series 3, display order: 4
    - Note: mai3/mai4 disambiguates buy/sell homophones
    - _Requirements: same as 8.1 + 14.6_

  - [x] 8.5 Create `vi-zh-children-curriculum/create_seasons.py` — "Bon Mua Trong Nam"
    - Preintermediate short format: 4 sessions, 12 words (chun tian, xia tian, qiu tian, dong tian, you yong, hua xue, fang feng zheng, shang hua, luo ye, dui xue ren, shu jia, han jia), price 49
    - Same 4-session structure as 8.1 but all content hand-crafted for seasons topic
    - Description tone: `bold_declaration`, farewell tone: `quiet_awe`
    - Series 3, display order: 5
    - _Requirements: same as 8.1_

  - [x] 8.6 Create `vi-zh-children-curriculum/create_daily_routines.py` — "Sinh Hoat Hang Ngay"
    - Preintermediate short format: 4 sessions, 12 words (qi chuang, shua ya, xi lian, chi zao fan, shang xue, hui jia, zuo zuo ye, xi zao, shui jiao, kan shu, kan dian shi, zao shang hao), price 49
    - Same 4-session structure as 8.1 but all content hand-crafted for daily routines topic
    - Description tone: `vivid_scenario`, farewell tone: `practical_momentum`
    - Series 3, display order: 6
    - _Requirements: same as 8.1_

  - [x] 8.7 Create `vi-zh-children-curriculum/create_mid_autumn.py` — "Le Hoi Trung Thu"
    - Preintermediate short format: 4 sessions, 12 words (zhong qiu jie, yue bing, shang yue, chang e, yu tu, jia ren, hua deng, cai mi, yuan, si nian, gu shi, kuai le), price 49
    - Same 4-session structure as 8.1 but all content hand-crafted for Mid-Autumn Festival topic
    - Description tone: `surprising_fact`, farewell tone: `introspective_guide`
    - Series 3, display order: 7
    - Include cultural context connecting Chinese and Vietnamese Mid-Autumn Festival traditions
    - _Requirements: same as 8.1_

  - [x] 8.8 Create `vi-zh-children-curriculum/create_characters.py` — "Net But Dau Tien"
    - Preintermediate short format: 4 sessions, 12 words (bi hua, heng, shu bi, pie, na, dian, xie zi, han zi, lian xi, ben zi, mao bi, mo), price 49
    - Same 4-session structure as 8.1 but all content hand-crafted for Chinese characters/strokes topic
    - Description tone: `metaphor_led`, farewell tone: `warm_accountability`
    - Series 3, display order: 8
    - Include cultural context about the beauty and history of Chinese calligraphy
    - _Requirements: same as 8.1 + 14.4_

- [x] 9. Checkpoint — All 22 curriculums created
  - Verify 6 curriculums in Series 1 with display orders 1-6
  - Verify 8 curriculums in Series 2 with display orders 1-8
  - Verify 8 curriculums in Series 3 with display orders 1-8
  - Verify prices: 6 mini at 9, 8 short at 19, 8 preintermediate at 49
  - Verify language pair: all have `language="zh"`, `userLanguage="vi"`
  - Run duplicate check for all 22 titles
  - Verify zero vocabulary overlap between all 22 curriculums

- [x] 10. Documentation and cleanup
  - [x] 10.1 Create `vi-zh-children-curriculum/README.md` with full documentation
    - Collection ID, all 3 series IDs
    - All 22 curriculum IDs with titles, display orders, vocabulary lists (characters + pinyin + Vietnamese meaning), tone assignments, pricing
    - SQL verification queries
    - _Requirements: 15.1_

  - [x] 10.2 Delete all creation scripts after verification
    - Delete all 22 `create_*.py` scripts and `orchestrator.py` from `vi-zh-children-curriculum/`
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
  - Verify validator file remains at `vi-zh-children-curriculum/validate_content.py`

## Notes

- This is the FIRST vi-zh children's batch — orchestrator creates new collection and 3 series
- Collection: "Tieng Trung Cho Be 6-10 Tuoi" (Chinese for Kids 6-10)
- Series 1: "Buoc Dau Tien" (First Steps) — 6 beginner mini curriculums
- Series 2: "Xay Nen Vung Chac" (Building Strong Foundations) — 8 beginner short curriculums
- Series 3: "Kham Pha Them" (Explore More) — 8 preintermediate short curriculums
- Root-level `api_helpers.py` is reused as-is — no changes needed
- All curriculum content must be hand-crafted — no template-based generation for learner-facing text
- Vietnamese session titles: "Phan 1" (mini), "Phan 1"/"Phan 2"/"On tap"/"Doc tong hop" (short/preintermediate)
- All marketing text (title, description, preview) in Vietnamese targeting parents
- All learner-facing content: introAudio primarily in Vietnamese with Chinese words as character + pinyin + Vietnamese meaning
- Reading passages: Chinese characters only (no pinyin in reading text)
- vocabList: lowercase ASCII pinyin without tone marks, spaces between syllables of multi-syllable words
- Zero vocabulary overlap between all 22 curriculums
- Tone assignments pre-planned in Requirement 17 — no adjacent duplicates, no tone >30%
- Farewell tones evenly distributed: 4-5 uses each across 5 registers
- Chinese-specific: explain tones in child-friendly Vietnamese, include cultural context where relevant
- writingSentence prompts: Vietnamese instructions + Chinese example (character + pinyin + translation) + substitution pattern
- No writingParagraph or vocabLevel3 in any curriculum
- Beginner mini also excludes vocabLevel1 and vocabLevel2
- Pinyin homophone disambiguation: mai3/mai4 for buy/sell, "da shu" for big tree vs "shu" for book, "shu bi" for vertical stroke