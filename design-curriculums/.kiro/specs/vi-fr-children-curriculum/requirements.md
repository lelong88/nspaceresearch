# Requirements Document

## Introduction

Create 22 French-learning curriculums specifically designed for Vietnamese-speaking children aged 6-10. Language pair: userLanguage="vi", language="fr". Difficulty levels: beginner (14 curriculums — 6 mini + 8 short) and preintermediate (8 curriculums).

This is the first vi-fr children's curriculum set. The existing vi-en children's catalog has 20 curriculums across 2 series, and the vi-zh children's catalog has 22 curriculums across 3 series, but there is no French-learning content for children. These 22 curriculums fill a critical gap by providing age-appropriate, child-friendly French learning experiences with topics that resonate with Vietnamese children — including both universal childhood topics and France-specific cultural content (French food, festivals, landmarks, daily life).

### What This Spec Covers

- 22 individually crafted curriculums for Vietnamese children aged 6-10 learning French
- Child-friendly topics including France-specific cultural content
- Age-appropriate persuasive copy (written for parents, since parents purchase)
- NEW collection and series organization for the vi-fr children's curriculum line
- Pricing per the beginner/preintermediate guidelines
- French vocabulary with Vietnamese explanations
- Creation workflow, validation, and documentation

### What This Spec Does NOT Cover

- Changes to existing vi-en or vi-zh children's curriculums
- Children's curriculums for other language pairs
- Content generation pipeline (audio, illustrations) — curriculums are created private
- Advanced or intermediate difficulty levels (not appropriate for ages 6-10)
- Existing vi-fr adult curriculums (if any)

## Glossary

- **Children_Curriculum**: A curriculum designed for Vietnamese children aged 6-10 learning French. Uses simpler vocabulary (3-5 words for mini, 8-10 words for short, 10-12 for preintermediate), shorter reading passages, playful tone, and age-appropriate topics. All user-facing marketing text targets parents (the purchasers). Vocabulary items are French words.
- **Curriculum_Creator**: The system of standalone Python scripts that generate curriculum JSON content and upload it via the REST API.
- **Content_Validator**: Validation logic that checks curriculum JSON against the Content Corruption Detection Rules before upload.
- **Collection_Organizer**: The orchestrator script that creates collections, series, wires them together, and sets display orders via the REST API.
- **Tone_Assigner**: The logic that assigns description tones and farewell tones to each curriculum and series, ensuring variety constraints are met.
- **Language_Pair**: userLanguage="vi", language="fr" — Vietnamese children learning French.
- **Parent_Copy**: Persuasive marketing text written for Vietnamese parents who are purchasing the curriculum for their child. Uses the standard 5-beat persuasive copy structure but addresses parental aspirations and concerns about their child's French education.
- **Child_Content**: Learner-facing content (introAudio scripts, reading passages, writing prompts) written in a warm, playful, encouraging tone appropriate for children aged 6-10. Uses simple Vietnamese explanations and child-friendly French vocabulary.
- **Persuasive_Copy**: The required writing style for marketing text — emotional sales copy with bold headline, concrete examples, vivid metaphor, transformation promise, and personal growth tie-in.
- **Tone_Palette**: The 6 rhetorical opener types: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led.
- **Farewell_Palette**: The 5 emotional registers for farewell introAudio scripts: introspective_guide, warm_accountability, team_building_energy, quiet_awe, practical_momentum.
- **Strip_Keys**: Auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never be included in new curriculum content.
- **Mini_Curriculum**: A single-session curriculum with 3-5 vocabulary words, priced at 9 credits (beginner).
- **Short_Curriculum**: A 4-session curriculum with 8-10 vocabulary words, priced at 19 credits (beginner) or 49 credits (preintermediate).

## Requirements

### Requirement 1: Children's Curriculum Format and Structure

**User Story:** As a platform owner, I want 22 French-learning curriculums designed specifically for Vietnamese children aged 6-10, so that young learners have age-appropriate content that makes learning French fun and engaging.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce exactly 22 Children_Curriculums for the vi-fr Language_Pair.
2. THE Curriculum_Creator SHALL create 6 beginner mini curriculums, 8 beginner short curriculums, and 8 preintermediate short curriculums.
3. WHEN a beginner mini Children_Curriculum is created, THE curriculum SHALL contain exactly 1 learning session with 3-5 vocabulary words.
4. WHEN a beginner short Children_Curriculum is created, THE curriculum SHALL contain 4 learning sessions with 8-10 vocabulary words divided into 2 groups.
5. WHEN a preintermediate Children_Curriculum is created, THE curriculum SHALL contain 4 learning sessions with 10-12 vocabulary words divided into 2-3 groups.
6. THE Children_Curriculum SHALL include `contentTypeTags: []` at the top level of the content JSON (topic-based).
7. THE Children_Curriculum SHALL never include Strip_Keys in the content JSON.
8. THE Curriculum_Creator SHALL set `language: "fr"` and `userLanguage: "vi"` as top-level body parameters in the `curriculum/create` API call.

### Requirement 2: Topic Plan for 22 Children's Curriculums

**User Story:** As a platform owner, I want child-friendly topics that resonate with Vietnamese children aged 6-10 learning French, so that young learners are excited to study French through familiar, fun subjects and France-specific cultural content.

#### Acceptance Criteria

1. THE 22 Children_Curriculums SHALL cover the following topics, each individually crafted:

   **Beginner Mini (3-5 words, 1 session, 9 credits) — 6 curriculums:**
   - Curriculum 1: "Thế Giới Màu Sắc" (World of Colors) — colors in French: rouge (red), bleu (blue), vert (green), jaune (yellow), blanc (white). vocabList: ["rouge", "bleu", "vert", "jaune", "blanc"]
   - Curriculum 2: "Đếm Từ 1 Đến 5" (Counting 1 to 5) — numbers: un (one), deux (two), trois (three), quatre (four), cinq (five). vocabList: ["un", "deux", "trois", "quatre", "cinq"]
   - Curriculum 3: "Gia Đình Yêu Thương" (Loving Family) — family members: maman (mom), papa (dad), frère (brother), soeur (sister), bébé (baby). vocabList: ["maman", "papa", "frère", "soeur", "bébé"]
   - Curriculum 4: "Trái Cây Ngon Lành" (Delicious Fruits) — fruits: pomme (apple), banane (banana), orange (orange), fraise (strawberry), raisin (grape). vocabList: ["pomme", "banane", "orange", "fraise", "raisin"]
   - Curriculum 5: "Bạn Thú Cưng" (Pet Friends) — common pets: chien (dog), chat (cat), poisson (fish), oiseau (bird), lapin (rabbit). vocabList: ["chien", "chat", "poisson", "oiseau", "lapin"]
   - Curriculum 6: "Chào Hỏi Vui Vẻ" (Happy Greetings) — greetings and manners: bonjour (hello), merci (thank you), au revoir (goodbye), pardon (sorry), oui (yes). vocabList: ["bonjour", "merci", "au revoir", "pardon", "oui"]

   **Beginner Short (8-10 words, 4 sessions, 19 credits) — 8 curriculums:**
   - Curriculum 7: "Một Ngày Ở Trường" (A Day at School) — school vocabulary: école (school), livre (book), crayon (pencil), table (desk), maître (teacher), classe (classroom), cahier (notebook), cartable (backpack), récréation (recess), devoirs (homework). vocabList: ["école", "livre", "crayon", "table", "maître", "classe", "cahier", "cartable", "récréation", "devoirs"]
   - Curriculum 8: "Món Ăn Pháp" (French Food) — food vocabulary: pain (bread), fromage (cheese), croissant (croissant), soupe (soup), lait (milk), poulet (chicken), gâteau (cake), salade (salad), eau (water), chocolat (chocolate). vocabList: ["pain", "fromage", "croissant", "soupe", "lait", "poulet", "gâteau", "salade", "eau", "chocolat"]
   - Curriculum 9: "Sân Chơi Vui Nhộn" (Fun Playground) — playground/action words: courir (run), sauter (jump), jouer (play), rire (laugh), chanter (sing), dessiner (draw), ami (friend), ballon (ball), toboggan (slide), balançoire (swing). vocabList: ["courir", "sauter", "jouer", "rire", "chanter", "dessiner", "ami", "ballon", "toboggan", "balançoire"]
   - Curriculum 10: "Cơ Thể Của Em" (My Body) — body parts: tête (head), main (hand), pied (foot), yeux (eyes), oreille (ear), bouche (mouth), nez (nose), ventre (belly), cheveux (hair), dent (tooth). vocabList: ["tête", "main", "pied", "yeux", "oreille", "bouche", "nez", "ventre", "cheveux", "dent"]
   - Curriculum 11: "Thời Tiết Hôm Nay" (Today's Weather) — weather: soleil (sun), pluie (rain), vent (wind), froid (cold), chaud (hot), neige (snow), nuage (cloud), orage (storm), arc-en-ciel (rainbow), parapluie (umbrella). vocabList: ["soleil", "pluie", "vent", "froid", "chaud", "neige", "nuage", "orage", "arc-en-ciel", "parapluie"]
   - Curriculum 12: "Tủ Quần Áo" (My Wardrobe) — clothing: chemise (shirt), pantalon (pants), robe (dress), chaussures (shoes), chapeau (hat), chaussettes (socks), manteau (coat), jupe (skirt), écharpe (scarf), gants (gloves). vocabList: ["chemise", "pantalon", "robe", "chaussures", "chapeau", "chaussettes", "manteau", "jupe", "écharpe", "gants"]
   - Curriculum 13: "Xe Cộ Quanh Em" (Vehicles Around Me) — vehicles: voiture (car), bus (bus), train (train), avion (airplane), vélo (bicycle), bateau (boat), métro (subway), moto (motorcycle), rapide (fast), lent (slow). vocabList: ["voiture", "bus", "train", "avion", "vélo", "bateau", "métro", "moto", "rapide", "lent"]
   - Curriculum 14: "Con Vật Đáng Yêu" (Adorable Animals) — zoo animals: éléphant (elephant), lion (lion), girafe (giraffe), singe (monkey), tigre (tiger), ours (bear), pingouin (penguin), serpent (snake), zèbre (zebra), perroquet (parrot). vocabList: ["éléphant", "lion", "girafe", "singe", "tigre", "ours", "pingouin", "serpent", "zèbre", "perroquet"]

   **Preintermediate Short (10-12 words, 4 sessions, 49 credits) — 8 curriculums:**
   - Curriculum 15: "Khám Phá Thiên Nhiên" (Exploring Nature) — nature vocabulary: forêt (forest), rivière (river), montagne (mountain), papillon (butterfly), fleur (flower), feuille (leaf), arbre (tree), ciel (sky), étoile (star), lune (moon), jardin (garden), herbe (grass). vocabList: ["forêt", "rivière", "montagne", "papillon", "fleur", "feuille", "arbre", "ciel", "étoile", "lune", "jardin", "herbe"]
   - Curriculum 16: "Bữa Ăn Gia Đình" (Family Meals) — mealtime vocabulary: petit-déjeuner (breakfast), déjeuner (lunch), dîner (dinner), assiette (plate), fourchette (fork), couteau (knife), cuillère (spoon), verre (glass), cuisine (kitchen), délicieux (delicious), manger (eat), boire (drink). vocabList: ["petit-déjeuner", "déjeuner", "dîner", "assiette", "fourchette", "couteau", "cuillère", "verre", "cuisine", "délicieux", "manger", "boire"]
   - Curriculum 17: "Bốn Mùa Trong Năm" (Four Seasons) — seasons and activities: printemps (spring), été (summer), automne (autumn), hiver (winter), nager (swim), ski (ski), plage (beach), feuilles (leaves), fleurir (bloom), bonhomme de neige (snowman), vacances (vacation), chaleur (heat). vocabList: ["printemps", "été", "automne", "hiver", "nager", "ski", "plage", "feuilles", "fleurir", "bonhomme de neige", "vacances", "chaleur"]
   - Curriculum 18: "Đi Chợ Cùng Mẹ" (Shopping with Mom) — market/shopping: acheter (buy), vendre (sell), argent (money), combien (how much), cher (expensive), marché (market), légumes (vegetables), fruits (fruits), sac (bag), payer (pay), magasin (store), prix (price). vocabList: ["acheter", "vendre", "argent", "combien", "cher", "marché", "légumes", "fruits", "sac", "payer", "magasin", "prix"]
   - Curriculum 19: "Sinh Hoạt Hàng Ngày" (Daily Routines) — daily activities: se réveiller (wake up), se brosser les dents (brush teeth), se laver (wash), matin (morning), dormir (sleep), après-midi (afternoon), rentrer (go home), lire (read), goûter (snack), soir (evening), nuit (night), bonne nuit (good night). vocabList: ["se réveiller", "se brosser les dents", "se laver", "matin", "dormir", "après-midi", "rentrer", "lire", "goûter", "soir", "nuit", "bonne nuit"]
   - Curriculum 20: "Ngôi Nhà Của Em" (My House) — house vocabulary: maison (house), chambre (bedroom), salon (living room), salle à manger (dining room), salle de bain (bathroom), porte (door), fenêtre (window), lit (bed), escalier (stairs), toit (roof), clé (key), mur (wall). vocabList: ["maison", "chambre", "salon", "salle à manger", "salle de bain", "porte", "fenêtre", "lit", "escalier", "toit", "clé", "mur"]
   - Curriculum 21: "Thể Thao Sôi Động" (Active Sports) — sports and exercise: football (soccer), natation (swimming), basket (basketball), tennis (tennis), danse (dance), grimper (climb), lancer (throw), attraper (catch), but (goal), gagner (win), équipe (team), champion (champion). vocabList: ["football", "natation", "basket", "tennis", "danse", "grimper", "lancer", "attraper", "but", "gagner", "équipe", "champion"]
   - Curriculum 22: "Đại Dương Xanh" (Blue Ocean) — ocean animals and sea life: baleine (whale), dauphin (dolphin), requin (shark), pieuvre (octopus), tortue (turtle), crabe (crab), méduse (jellyfish), coquillage (shell), corail (coral), vague (wave), plongée (diving), sable (sand). vocabList: ["baleine", "dauphin", "requin", "pieuvre", "tortue", "crabe", "méduse", "coquillage", "corail", "vague", "plongée", "sable"]

2. THE Curriculum_Creator SHALL select vocabulary words that are concrete, high-frequency, and visually representable for children aged 6-10.
3. THE Curriculum_Creator SHALL ensure no two curriculums have overlapping vocabulary lists (vocabList arrays must be unique across all 22 curriculums).
4. WHEN creating reading passages for children, THE Curriculum_Creator SHALL use simple French sentences (under 10 words average for beginner, under 12 words for preintermediate), present tense primarily, and vocabulary that a 6-10 year old Vietnamese child can relate to.
5. THE vocabList arrays SHALL use French words in their standard written form (including accents where applicable), all lowercase.

### Requirement 3: Age-Appropriate Content Design

**User Story:** As a content quality owner, I want all learner-facing content designed for children aged 6-10, so that young learners feel engaged, safe, and encouraged throughout the learning experience.

#### Acceptance Criteria

1. WHEN Child_Content is created for introAudio scripts, THE scripts SHALL use a warm, playful, encouraging tone — as if a friendly teacher is speaking to a child. Use simple Vietnamese sentences, enthusiastic language, and gentle encouragement. Each French word SHALL be introduced with: the French word, Vietnamese meaning, pronunciation guidance in simple Vietnamese terms, and a fun association or memory hook.
2. WHEN Child_Content is created for reading passages, THE passages SHALL be written in simple French using only vocabulary from the curriculum's vocabList and basic connector words. Passages SHALL feature child-relatable scenarios: playing with friends, going to school, eating food, exploring nature, family activities. No abstract concepts, no adult themes.
3. WHEN Child_Content is created for writingSentence prompts, THE prompts SHALL provide maximum scaffolding: full Vietnamese instructions written simply for a child, a complete French example sentence (with Vietnamese translation) the child can closely imitate, and a clear word-substitution pattern requiring only 1 word change.
4. THE Children_Curriculum SHALL NOT include `writingParagraph` activities (too complex for ages 6-10).
5. THE Children_Curriculum SHALL NOT include `vocabLevel3` activities (to reduce cognitive load for young learners).
6. WHEN a beginner mini Children_Curriculum is created, THE curriculum SHALL NOT include `vocabLevel1` or `vocabLevel2` activities (mini format focuses on flashcards, reading, and speaking).
7. THE introAudio farewell scripts SHALL use an especially warm, celebratory tone — praising the child's effort, using phrases like "con giỏi lắm!" (you did great!), and encouraging them to practice French with family or friends.

### Requirement 4: Activity Templates for Children's Curriculums

**User Story:** As a platform owner, I want activity sequences optimized for children's attention spans and learning patterns, so that young learners stay engaged throughout each session.

#### Acceptance Criteria

1. WHEN a beginner mini Children_Curriculum is created, THE session SHALL include activities in this order: introAudio (welcome + teach all words with playful context, pronunciation guide, and Vietnamese meaning), viewFlashcards, speakFlashcards, reading (short French passage, 40-60 words), speakReading, readAlong, introAudio (farewell with vocab review and praise).

2. WHEN a beginner short Children_Curriculum is created, THE 4 sessions SHALL follow this structure:
   - Session 1: introAudio (welcome + teach words group 1 with French pronunciation and Vietnamese meaning), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), reading (short French passage using group 1 words, 60-80 words), readAlong, introAudio (session wrap-up)
   - Session 2: introAudio (recap group 1 + teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), reading (short French passage using group 2 words, 60-80 words), readAlong, introAudio (session wrap-up)
   - Session 3 (Review): introAudio (review intro), viewFlashcards (all words), speakFlashcards (all words), vocabLevel1 (all words), vocabLevel2 (all words), writingSentence (3-4 items), introAudio (review wrap-up)
   - Session 4 (Final): introAudio (final reading intro), reading (combined French passage using all words, 100-120 words), speakReading, readAlong, writingSentence (2-3 items), introAudio (farewell with full vocab review and celebration)

3. WHEN a preintermediate short Children_Curriculum is created, THE 4 sessions SHALL follow this structure:
   - Session 1: introAudio (welcome + teach words group 1 with French pronunciation and Vietnamese meaning), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), vocabLevel2 (group 1), reading (French passage using group 1 words, 80-100 words), speakReading, readAlong, introAudio (session wrap-up)
   - Session 2: introAudio (recap group 1 + teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), vocabLevel2 (group 2), reading (French passage using group 2 words, 80-100 words), speakReading, readAlong, introAudio (session wrap-up)
   - Session 3 (Review): introAudio (review intro), viewFlashcards (all words), speakFlashcards (all words), vocabLevel1 (all words), vocabLevel2 (all words), writingSentence (4-5 items), introAudio (review wrap-up)
   - Session 4 (Final): introAudio (final reading intro), reading (combined French passage using all words, 150-180 words), speakReading, readAlong, writingSentence (3-4 items), introAudio (farewell with full vocab review and celebration)

### Requirement 5: Parent-Facing Marketing Copy

**User Story:** As a content quality owner, I want all marketing text (title, description, preview) to speak to Vietnamese parents, so that parents understand the value and feel confident purchasing these curriculums for their children.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL write curriculum descriptions as Parent_Copy following the Persuasive_Copy 5-beat structure, but addressing parental aspirations: their child's future, early French language advantage, confidence building, and fun learning. The copy SHALL emphasize the cultural prestige of French and its value as a global language.
2. THE Curriculum_Creator SHALL write curriculum previews (~100-150 words) as Parent_Copy with vivid hooks about the child's French learning journey, vocabulary word listing (French word + Vietnamese meaning), and what the child will be able to say/read in French after completing the curriculum.
3. THE Curriculum_Creator SHALL write all titles, descriptions, and preview text in Vietnamese (as required for beginner/preintermediate curriculums where userLanguage="vi").
4. THE Tone_Assigner SHALL assign one of the 6 Tone_Palette types to every curriculum description headline.
5. WHILE assigning tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Tone_Palette type.
6. THE Tone_Assigner SHALL ensure no single Tone_Palette type exceeds 30% of the 22 curriculum descriptions (max 6-7 uses per tone).
7. THE Parent_Copy SHALL NOT use fear-based marketing or shame-based language about children's abilities. The tone SHALL be aspirational, warm, and encouraging — celebrating the child's potential and the cultural richness of learning French.

### Requirement 6: introAudio Quality for Children

**User Story:** As a content quality owner, I want introAudio scripts crafted specifically for young learners of French, so that children feel welcomed, engaged, and celebrated throughout the learning experience.

#### Acceptance Criteria

1. WHEN a welcome introAudio is created for a mini curriculum, THE script (200-350 words) SHALL greet the child warmly in Vietnamese, introduce the topic with a fun hook (e.g., "Hôm nay chúng ta sẽ học đếm bằng tiếng Pháp nè!"), list all vocabulary words, and teach each word with: the French word, pronunciation guidance in simple Vietnamese terms, Vietnamese meaning, a simple example sentence in French, and a fun fact or memory association.
2. WHEN a welcome introAudio is created for a short/preintermediate curriculum, THE script (300-500 words) SHALL follow the same pattern as criterion 1 but with more words and slightly more context per word, including cultural context where relevant (e.g., explaining why French people eat croissants for breakfast).
3. WHEN a session recap introAudio is created (sessions 2+), THE script SHALL briefly and playfully recap previous French words before introducing new ones — using phrases like "Các bạn còn nhớ không? Hôm trước chúng ta học..." (Do you remember? Last time we learned...).
4. WHEN a farewell introAudio is created, THE script (200-400 words) SHALL review key vocabulary words with fresh child-friendly French example sentences (with Vietnamese translation), celebrate the child's achievement with enthusiastic praise, and encourage practicing French with family or friends.
5. THE introAudio scripts SHALL be primarily in Vietnamese with French words/phrases introduced with pronunciation guidance and Vietnamese meaning.
6. THE Curriculum_Creator SHALL individually craft every introAudio script for its specific curriculum topic, without using template functions or string interpolation.
7. THE Tone_Assigner SHALL assign one of the 5 Farewell_Palette registers to every farewell introAudio, adapted for a child audience (e.g., "warm accountability" becomes gentle encouragement to practice French words, "quiet awe" becomes wonder at the beauty of the French language).
8. WHILE assigning farewell tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Farewell_Palette register.

### Requirement 7: Pricing

**User Story:** As a platform owner, I want children's curriculums priced according to the standard pricing guidelines, so that pricing is consistent with the rest of the catalog.

#### Acceptance Criteria

1. WHEN a beginner mini Children_Curriculum (1 session) is created, THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 9`.
2. WHEN a beginner short Children_Curriculum (4 sessions) is created, THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 19`.
3. WHEN a preintermediate short Children_Curriculum (4 sessions) is created, THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 49`.
4. THE Curriculum_Creator SHALL set the price after the curriculum is successfully created and added to its series.

### Requirement 8: Collection and Series Organization

**User Story:** As a platform owner, I want the 22 children's curriculums organized into a dedicated vi-fr collection and series, so that parents can easily find and browse all children's French content.

#### Acceptance Criteria

1. THE Collection_Organizer SHALL create 1 NEW collection titled "Tiếng Pháp Cho Bé 6-10 Tuổi" (French for Kids 6-10) with a neutral, informative Vietnamese description explaining this is a collection of French curriculums designed for Vietnamese children aged 6-10.
2. THE Collection_Organizer SHALL organize the 22 curriculums into 3 series:
   - Series 1: "Bước Đầu Tiên" (First Steps) — containing the 6 beginner mini curriculums. Description ≤255 chars using a Tone_Palette type.
   - Series 2: "Xây Nền Vững Chắc" (Building Strong Foundations) — containing the 8 beginner short curriculums. Description ≤255 chars using a different Tone_Palette type.
   - Series 3: "Khám Phá Thêm" (Explore More) — containing the 8 preintermediate curriculums. Description ≤255 chars using a different Tone_Palette type.
3. THE Collection_Organizer SHALL wire each series to the collection via `curriculum-collection/addSeriesToCollection`.
4. THE Collection_Organizer SHALL set display orders for all 3 series within the collection via `curriculum-series/setDisplayOrder`.
5. THE Collection_Organizer SHALL set display orders for all curriculums within each series via `curriculum/setDisplayOrder`.
6. THE Collection_Organizer SHALL ensure all curriculums within each series share `language: "fr"` and `userLanguage: "vi"`.
7. WHILE assigning series description tones, THE Tone_Assigner SHALL ensure all 3 series use different Tone_Palette types.

### Requirement 9: Activity Schema Compliance

**User Story:** As a platform developer, I want every activity to comply with the platform's content schema, so that the content pipeline processes children's curriculums without errors.

#### Acceptance Criteria

1. Each Activity SHALL include `activityType`, `title`, `description`, and `data` fields.
2. THE `activityType` field SHALL use one of the valid values: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence.
3. THE `vocabList` field SHALL be an array of lowercase strings (French words with accents preserved), using the field name `vocabList` (never `words`).
4. WHEN viewFlashcards and speakFlashcards appear in the same session, THE two activities SHALL have identical `vocabList` arrays.
5. All content data SHALL be inside the `data` object, not inline on the activity object.
6. WHEN a writingSentence activity is created, THE activity SHALL have `data.vocabList`, `data.items` (non-empty array), and each item SHALL have `prompt` (Vietnamese instructions with French example sentence and Vietnamese translation, plus substitution pattern) and `targetVocab` fields.
7. THE Curriculum_Creator SHALL follow the activity title/description conventions: viewFlashcards/speakFlashcards/vocabLevel* use "Flashcards: <topic>"; reading/speakReading use "Đọc: <topic>"; readAlong uses "Nghe: <topic>"; introAudio uses descriptive labels; writingSentence uses "Viết: <topic>".

### Requirement 10: Content Validation

**User Story:** As a platform developer, I want every children's curriculum validated before upload, so that no corrupted content enters the database.

#### Acceptance Criteria

1. THE Content_Validator SHALL verify that every Children_Curriculum content JSON has non-null, non-empty `title`, `description`, and `preview.text` fields.
2. THE Content_Validator SHALL verify that `learningSessions` is a non-empty array, with each session having a non-empty `title` and `activities` array.
3. THE Content_Validator SHALL verify that every activity has `activityType` (not `type`), `title`, `description`, and `data` fields, with content fields inside `data`.
4. THE Content_Validator SHALL verify that `activityType` values are valid.
5. THE Content_Validator SHALL verify that vocabList fields contain arrays of lowercase strings using the field name `vocabList`.
6. THE Content_Validator SHALL verify that viewFlashcards and speakFlashcards in the same session have identical vocabList arrays.
7. THE Content_Validator SHALL verify writingSentence data structures (vocabList, items with prompt and targetVocab).
8. THE Content_Validator SHALL verify that no Strip_Keys appear anywhere in the content JSON.
9. THE Content_Validator SHALL verify that no `writingParagraph` or `vocabLevel3` activities exist in any Children_Curriculum.
10. IF any validation check fails, THEN THE Content_Validator SHALL abort the upload and print the specific rule violation.

### Requirement 11: Script Architecture and Workflow

**User Story:** As a developer, I want a clear, repeatable workflow for creating 22 children's curriculums, so that the process is manageable and traceable.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce one standalone Python script per curriculum (22 scripts total).
2. THE Curriculum_Creator SHALL produce one orchestrator script that creates the collection, 3 series, wires them together, sets display orders, and sets prices.
3. THE Curriculum_Creator SHALL organize scripts into a directory `vi-fr-children-curriculum/`.
4. THE Curriculum_Creator SHALL authenticate all API calls using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
5. THE Curriculum_Creator SHALL use `https://helloapi.step.is` as the API base URL.
6. THE Curriculum_Creator SHALL individually craft every piece of learner-facing text for its specific curriculum topic, without using template functions, string interpolation, or generic fill-in-the-blank patterns.
7. THE Curriculum_Creator MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.
8. IF a curriculum creation API call fails, THEN THE Curriculum_Creator SHALL log the error with the curriculum title and continue with the next curriculum.
9. THE Curriculum_Creator SHALL reuse the root-level `api_helpers.py` for all API calls (create_curriculum, add_to_series, set_display_order, set_price).
10. THE Curriculum_Creator SHALL create a `vi-fr-children-curriculum/validate_content.py` module for content validation specific to vi-fr children's curriculums.

### Requirement 12: Newly Created Curriculums Must Be Private

**User Story:** As a platform owner, I want all newly created children's curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created Children_Curriculum.

### Requirement 13: Curriculum Titles

**User Story:** As a content quality owner, I want curriculum titles to be minimal, child-friendly, and in Vietnamese, so that they work well within the series/collection context.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL keep curriculum titles minimal — never repeating series/collection name, content type prefix, skill-focus label, difficulty level, or audience suffix.
2. THE Curriculum_Creator SHALL write curriculum titles in Vietnamese.
3. THE curriculum titles SHALL NOT include difficulty level indicators (e.g., "beginner", "sơ cấp").
4. THE curriculum titles SHALL be engaging and child-friendly — using playful, imaginative language that appeals to both children and parents.

### Requirement 14: French-Specific Content Adaptations

**User Story:** As a content quality owner, I want the French learning content to properly handle French-specific elements (accents, pronunciation, gender), so that children learn French correctly from the start.

#### Acceptance Criteria

1. WHEN teaching vocabulary in introAudio scripts, THE Curriculum_Creator SHALL present each word in the format: French word → pronunciation guidance in simple Vietnamese → Vietnamese meaning → example sentence. Example: "rouge — đọc là 'ru-giơ' nhé — nghĩa là màu đỏ. Ví dụ: Le ballon est rouge — quả bóng màu đỏ."
2. THE reading passages SHALL be written entirely in French, appropriate for the target level.
3. THE introAudio scripts SHALL explain French pronunciation in child-friendly Vietnamese terms, especially sounds that don't exist in Vietnamese (e.g., the French "r", nasal vowels, the "u" sound). Use simple comparisons: "Âm 'r' trong tiếng Pháp giống như tiếng gừ nhẹ ở cổ họng nhé."
4. WHEN cultural context is relevant (French food, daily life, landmarks), THE introAudio scripts SHALL include brief, child-friendly cultural explanations in Vietnamese connecting French culture to Vietnamese culture where possible (e.g., both cultures value family meals, Vietnam has French colonial architectural heritage).
5. THE vocabList arrays SHALL use French words in their standard lowercase written form, preserving accents (é, è, ê, ë, à, â, ù, û, ô, î, ï, ç, œ, æ) as they are part of correct French spelling.
6. WHEN a French word contains special characters or accents, THE vocabList entry SHALL preserve those characters exactly as written in standard French (e.g., "éléphant", "forêt", "garçon").

### Requirement 15: Documentation and Cleanup

**User Story:** As a developer, I want proper documentation after all curriculums are created, so that the content is traceable and reproducible.

#### Acceptance Criteria

1. WHEN all 22 curriculums are created and verified, THE Curriculum_Creator SHALL create a README.md in `vi-fr-children-curriculum/` documenting: collection ID, all series IDs, all curriculum IDs with titles and display orders, vocabulary lists per curriculum (French word + Vietnamese meaning), tone assignments (description and farewell), pricing, and SQL verification queries.
2. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted, leaving only the README.md and validate_content.py.
3. THE Curriculum_Creator SHALL run a duplicate check query for each curriculum title after creation and resolve any duplicates (keep earliest, delete extras).

### Requirement 16: Execution Order

**User Story:** As a developer, I want a phased execution plan, so that I can create the infrastructure first and then add curriculums incrementally.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL execute creation in this order: (1) create collection and 3 series via orchestrator, (2) create beginner mini curriculums (6 scripts), (3) create beginner short curriculums (8 scripts), (4) create preintermediate short curriculums (8 scripts).
2. WHEN each curriculum is created, THE Curriculum_Creator SHALL immediately add it to the appropriate series, set its display order, and set its price.
3. WHEN all 22 curriculums are created, THE Curriculum_Creator SHALL verify the complete set by querying the database to confirm all curriculums exist with correct display orders, language values, prices, and non-empty content.
4. IF verification reveals missing or malformed curriculums, THEN THE Curriculum_Creator SHALL recreate the affected curriculums before finalizing documentation.

### Requirement 17: Tone Assignment Plan

**User Story:** As a content quality owner, I want a pre-planned tone assignment for all 22 curriculums, so that variety is guaranteed and adjacency rules are respected.

#### Acceptance Criteria

1. THE Tone_Assigner SHALL pre-assign description tones for all 22 curriculums before creation begins, following this distribution (max 30% = max 7 per tone across 22):

   **Series 1 — Bước Đầu Tiên (6 beginner mini):**
   - Curriculum 1 (Colors): provocative_question
   - Curriculum 2 (Numbers): bold_declaration
   - Curriculum 3 (Family): vivid_scenario
   - Curriculum 4 (Fruits): empathetic_observation
   - Curriculum 5 (Pets): surprising_fact
   - Curriculum 6 (Greetings): metaphor_led

   **Series 2 — Xây Nền Vững Chắc (8 beginner short):**
   - Curriculum 7 (School): bold_declaration
   - Curriculum 8 (French Food): vivid_scenario
   - Curriculum 9 (Playground): provocative_question
   - Curriculum 10 (Body): surprising_fact
   - Curriculum 11 (Weather): empathetic_observation
   - Curriculum 12 (Wardrobe): metaphor_led
   - Curriculum 13 (Vehicles): bold_declaration
   - Curriculum 14 (Animals): vivid_scenario

   **Series 3 — Khám Phá Thêm (8 preintermediate):**
   - Curriculum 15 (Nature): surprising_fact
   - Curriculum 16 (Family Meals): metaphor_led
   - Curriculum 17 (Seasons): empathetic_observation
   - Curriculum 18 (Shopping): provocative_question
   - Curriculum 19 (Daily Routines): bold_declaration
   - Curriculum 20 (House): vivid_scenario
   - Curriculum 21 (Sports): surprising_fact
   - Curriculum 22 (Ocean): metaphor_led

2. THE Tone_Assigner SHALL pre-assign farewell tones for all 22 curriculums, distributing evenly across the 5 registers (4-5 uses each across 22 curriculums):

   **Series 1:**
   - Curriculum 1: introspective_guide
   - Curriculum 2: warm_accountability
   - Curriculum 3: team_building_energy
   - Curriculum 4: quiet_awe
   - Curriculum 5: practical_momentum
   - Curriculum 6: introspective_guide

   **Series 2:**
   - Curriculum 7: warm_accountability
   - Curriculum 8: team_building_energy
   - Curriculum 9: quiet_awe
   - Curriculum 10: practical_momentum
   - Curriculum 11: introspective_guide
   - Curriculum 12: warm_accountability
   - Curriculum 13: team_building_energy
   - Curriculum 14: quiet_awe

   **Series 3:**
   - Curriculum 15: practical_momentum
   - Curriculum 16: introspective_guide
   - Curriculum 17: warm_accountability
   - Curriculum 18: team_building_energy
   - Curriculum 19: quiet_awe
   - Curriculum 20: practical_momentum
   - Curriculum 21: introspective_guide
   - Curriculum 22: warm_accountability

3. WHILE assigning tones, THE Tone_Assigner SHALL verify that no two adjacent curriculums within the same series share the same description tone or farewell tone.
4. THE Tone_Assigner SHALL verify that no single description tone exceeds 7 uses across all 22 curriculums (30% cap).
