# Requirements Document

## Introduction

Create 20 Japanese-learning curriculums for Vietnamese-speaking adults at the preintermediate and intermediate levels. Language pair: userLanguage="vi", language="ja". This is the second vi-ja curriculum set, building on the existing 20 beginner curriculums that cover basic topics (greetings, numbers, family, colors, weather, drinks, days, emotions, food, shopping, transport, hotel, office, seasons, hobbies, health, housing, festivals, technology, sports).

These 20 curriculums target learners who have completed the beginner set and are ready for more complex vocabulary, longer sentences, and richer cultural/professional scenarios. At this level, learners know hiragana and katakana and are beginning to encounter basic kanji. Reading passages can include basic kanji with furigana guidance. Topics are more sophisticated: workplace communication, travel planning, cultural deep-dives, relationships, current events, arts, and daily life at a higher complexity level.

### What This Spec Covers

- 20 individually crafted curriculums for Vietnamese adults learning Japanese at preintermediate and intermediate levels
- 18 vocabulary words per curriculum divided into 3 groups of 6
- 5 sessions per curriculum: 3 learning sessions, 1 review session, 1 final reading session
- Diverse topics covering workplace, travel, culture, relationships, technology, arts, daily life, and society
- Japanese vocabulary in standard written form (hiragana, katakana, and basic kanji as appropriate)
- Vietnamese marketing text (titles, descriptions, previews)
- Collection and series organization
- Pricing at 49 credits per curriculum (standard for preintermediate/intermediate with 5 sessions)

### What This Spec Does NOT Cover

- Changes to the existing 20 beginner vi-ja curriculums
- Upper-intermediate or advanced Japanese curriculums
- Overlap with beginner topics already covered
- Content generation pipeline (audio, illustrations) — curriculums are created private
- Grammar-focused curriculums (these are vocabulary-based balanced_skills)

## Glossary

- **Preintermediate_Curriculum**: A curriculum for Vietnamese adults learning Japanese at preintermediate level. Uses bilingual text (Vietnamese + Japanese). Vocabulary includes hiragana, katakana, and basic kanji. 18 words across 5 sessions. Does NOT include writingParagraph or vocabLevel3.
- **Intermediate_Curriculum**: A curriculum for Vietnamese adults learning Japanese at intermediate level. Uses bilingual text (Vietnamese + Japanese). Vocabulary includes hiragana, katakana, and kanji. 18 words across 5 sessions. Includes writingParagraph in the final session. Includes vocabLevel3 in review session.
- **Curriculum_Creator**: The system of standalone Python scripts that generate curriculum JSON content and upload it via the REST API.
- **Content_Validator**: Validation logic that checks curriculum JSON against the Content Corruption Detection Rules before upload.
- **Collection_Organizer**: The orchestrator script that creates collections, series, wires them together, and sets display orders via the REST API.
- **Tone_Assigner**: The logic that assigns description tones and farewell tones to each curriculum and series, ensuring variety constraints are met.
- **Language_Pair**: userLanguage="vi", language="ja" — Vietnamese speakers learning Japanese.
- **Persuasive_Copy**: The required writing style for marketing text — emotional sales copy with bold headline, concrete examples, vivid metaphor, transformation promise, and personal growth tie-in. Written in Vietnamese.
- **Tone_Palette**: The 6 rhetorical opener types: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led.
- **Farewell_Palette**: The 5 emotional registers for farewell introAudio scripts: introspective_guide, warm_accountability, team_building_energy, quiet_awe, practical_momentum.
- **Strip_Keys**: Auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never be included in new curriculum content.
- **Balanced_Skills**: Curriculum type distributing time across reading, listening, speaking, and writing. Uses 18 words across 3 learning sessions + review + final reading.
- **Furigana**: Hiragana reading annotations placed above kanji characters to indicate pronunciation. Used at preintermediate/intermediate level to support learners encountering new kanji.
- **Kanji**: Chinese characters used in Japanese writing. At preintermediate/intermediate level, learners encounter basic kanji (JLPT N5-N4 level) with furigana support.

## Requirements

### Requirement 1: Preintermediate/Intermediate Curriculum Format and Structure

**User Story:** As a platform owner, I want 20 Japanese-learning curriculums at preintermediate and intermediate levels for Vietnamese adults, so that learners who completed the beginner set have a clear next step in their Japanese journey.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce exactly 20 curriculums for the vi-ja Language_Pair at preintermediate and intermediate levels.
2. THE Curriculum_Creator SHALL create 10 preintermediate curriculums and 10 intermediate curriculums.
3. WHEN a preintermediate or intermediate curriculum is created, THE curriculum SHALL contain exactly 18 vocabulary words divided into 3 groups of 6.
4. WHEN a preintermediate or intermediate curriculum is created, THE curriculum SHALL contain exactly 5 sessions: 3 learning sessions, 1 review session, and 1 final reading session.
5. THE curriculum SHALL include `contentTypeTags: []` at the top level of the content JSON (topic-based).
6. THE curriculum SHALL never include Strip_Keys in the content JSON.
7. THE Curriculum_Creator SHALL set `language: "ja"` and `userLanguage: "vi"` as top-level body parameters in the `curriculum/create` API call.
8. WHEN a preintermediate curriculum is created, THE curriculum SHALL NOT include `writingParagraph` activities.
9. WHEN a preintermediate curriculum is created, THE curriculum SHALL NOT include `vocabLevel3` activities.
10. WHEN an intermediate curriculum is created, THE curriculum SHALL include `writingParagraph` in the final reading session.
11. WHEN an intermediate curriculum is created, THE curriculum SHALL include `vocabLevel3` in the review session.


### Requirement 2: Topic Plan for 20 Preintermediate/Intermediate Curriculums

**User Story:** As a platform owner, I want diverse topics that build on the beginner foundation with more complex vocabulary and real-world scenarios, so that learners can handle workplace communication, travel planning, cultural discussions, and social situations in Japanese.

#### Acceptance Criteria

1. THE 20 curriculums SHALL cover the following topics, each individually crafted. No topic SHALL overlap with the 20 beginner curriculums (greetings, numbers, family, colors, weather, drinks, days, emotions, food, shopping, transport, hotel, office, seasons, hobbies, health, housing, festivals, technology, sports).

   **Preintermediate (18 words, 5 sessions, 49 credits) — 10 curriculums:**
   - Curriculum 1: "Phỏng Vấn Xin Việc" (Job Interview) — workplace vocabulary for job hunting: 履歴書/りれきしょ (resume), 面接/めんせつ (interview), 志望動機/しぼうどうき (motivation for applying), 経験/けいけん (experience), 給料/きゅうりょう (salary), 正社員/せいしゃいん (full-time employee), 残業/ざんぎょう (overtime), 上司/じょうし (boss/superior), 部下/ぶか (subordinate), 昇進/しょうしん (promotion), 退職/たいしょく (resignation), 応募/おうぼ (application), 採用/さいよう (hiring), 研修/けんしゅう (training), 通勤/つうきん (commuting), 有給/ゆうきゅう (paid leave), 転職/てんしょく (job change), 名刺/めいし (business card)
   - Curriculum 2: "Đặt Phòng Và Lên Kế Hoạch" (Booking and Planning) — travel planning vocabulary: 予約/よやく (reservation), 片道/かたみち (one-way), 往復/おうふく (round trip), 出発/しゅっぱつ (departure), 到着/とうちゃく (arrival), 乗り換え/のりかえ (transfer), 空港/くうこう (airport), 搭乗/とうじょう (boarding), パスポート (passport), 観光/かんこう (sightseeing), 旅行代理店/りょこうだいりてん (travel agency), 日程/にってい (schedule/itinerary), 荷造り/にづくり (packing), 両替/りょうがえ (currency exchange), 免税/めんぜい (tax-free), 案内/あんない (guidance/information), 地図/ちず (map), 土産/みやげ (souvenir)
   - Curriculum 3: "Ẩm Thực Đường Phố" (Street Food Culture) — food culture beyond basics: 屋台/やたい (food stall), 焼き鳥/やきとり (grilled chicken skewers), たこ焼き/たこやき (takoyaki), お好み焼き/おこのみやき (okonomiyaki), 注文/ちゅうもん (order), 持ち帰り/もちかえり (takeout), 食べ歩き/たべあるき (eating while walking), 行列/ぎょうれつ (queue/line), 割り箸/わりばし (disposable chopsticks), 味/あじ (flavor/taste), 辛い/からい (spicy), 甘い/あまい (sweet), 焼く/やく (to grill), 揚げる/あげる (to deep-fry), 蒸す/むす (to steam), 具/ぐ (ingredients/filling), ソース (sauce), 薬味/やくみ (condiments/garnish)
   - Curriculum 4: "Thuê Nhà Ở Nhật" (Renting in Japan) — housing/rental vocabulary: 賃貸/ちんたい (rental), 家賃/やちん (rent), 敷金/しききん (security deposit), 礼金/れいきん (key money), 不動産/ふどうさん (real estate), 間取り/まどり (floor plan), 一人暮らし/ひとりぐらし (living alone), 引っ越し/ひっこし (moving), 契約/けいやく (contract), 保証人/ほしょうにん (guarantor), 管理費/かんりひ (maintenance fee), 駅近/えきちか (near station), 築年数/ちくねんすう (building age), 日当たり/ひあたり (sunlight exposure), 防音/ぼうおん (soundproofing), ゴミ出し/ごみだし (garbage disposal), 大家/おおや (landlord), 更新/こうしん (renewal)
   - Curriculum 5: "Khám Bệnh Ở Nhật" (Medical Visit in Japan) — medical/healthcare vocabulary: 診察/しんさつ (medical examination), 症状/しょうじょう (symptoms), 処方箋/しょほうせん (prescription), 保険証/ほけんしょう (insurance card), 受付/うけつけ (reception), 待合室/まちあいしつ (waiting room), 内科/ないか (internal medicine), 外科/げか (surgery department), 検査/けんさ (test/examination), 注射/ちゅうしゃ (injection), 入院/にゅういん (hospitalization), 退院/たいいん (discharge), 薬局/やっきょく (pharmacy), アレルギー (allergy), 予防接種/よぼうせっしゅ (vaccination), 診断/しんだん (diagnosis), 紹介状/しょうかいじょう (referral letter), 救急/きゅうきゅう (emergency)
   - Curriculum 6: "Mối Quan Hệ Xã Hội" (Social Relationships) — relationship/social vocabulary: 友達/ともだち (friend), 知り合い/しりあい (acquaintance), 付き合う/つきあう (to date/associate), 別れる/わかれる (to break up/part), 信頼/しんらい (trust), 約束/やくそく (promise), 相談/そうだん (consultation), 紹介/しょうかい (introduction), 誘う/さそう (to invite), 断る/ことわる (to refuse), 謝る/あやまる (to apologize), 許す/ゆるす (to forgive), 喧嘩/けんか (quarrel), 仲直り/なかなおり (reconciliation), 気遣い/きづかい (consideration), 本音/ほんね (true feelings), 建前/たてまえ (public facade), 空気を読む/くうきをよむ (to read the room)
   - Curriculum 7: "Thiên Tai Và An Toàn" (Natural Disasters and Safety) — disaster preparedness vocabulary: 地震/じしん (earthquake), 台風/たいふう (typhoon), 津波/つなみ (tsunami), 避難/ひなん (evacuation), 防災/ぼうさい (disaster prevention), 非常口/ひじょうぐち (emergency exit), 避難所/ひなんじょ (evacuation shelter), 警報/けいほう (warning/alert), 余震/よしん (aftershock), 停電/ていでん (power outage), 断水/だんすい (water outage), 備蓄/びちく (stockpiling), 消火器/しょうかき (fire extinguisher), 救助/きゅうじょ (rescue), 安否確認/あんぴかくにん (safety confirmation), 防災グッズ/ぼうさいぐっず (disaster supplies), 耐震/たいしん (earthquake-resistant), 緊急地震速報/きんきゅうじしんそくほう (earthquake early warning)
   - Curriculum 8: "Giao Tiếp Qua Điện Thoại" (Phone Communication) — telephone/communication vocabulary: 電話/でんわ (telephone), 留守番電話/るすばんでんわ (answering machine), 着信/ちゃくしん (incoming call), 発信/はっしん (outgoing call), 折り返し/おりかえし (callback), 伝言/でんごん (message), 内線/ないせん (extension), 外線/がいせん (outside line), 通話/つうわ (phone conversation), 切る/きる (to hang up), かけ直す/かけなおす (to call back), 繋がる/つながる (to be connected), 話し中/はなしちゅう (line busy), 番号/ばんごう (number), 登録/とうろく (registration), 連絡先/れんらくさき (contact information), 不在/ふざい (absence), 取り次ぐ/とりつぐ (to transfer a call)
   - Curriculum 9: "Mua Sắm Trực Tuyến" (Online Shopping) — e-commerce vocabulary: 通販/つうはん (mail order/online shopping), カート (cart), 送料/そうりょう (shipping fee), 届く/とどく (to arrive/be delivered), 返品/へんぴん (return), 交換/こうかん (exchange), レビュー (review), 評価/ひょうか (rating/evaluation), 在庫/ざいこ (stock/inventory), 割引/わりびき (discount), ポイント (points), クーポン (coupon), 配送/はいそう (delivery), 代引き/だいびき (cash on delivery), 振込/ふりこみ (bank transfer), クレジットカード (credit card), 領収書/りょうしゅうしょ (receipt), 問い合わせ/といあわせ (inquiry)
   - Curriculum 10: "Thể Thao Và Cổ Vũ" (Sports and Cheering) — sports culture vocabulary: 応援/おうえん (cheering/support), 試合/しあい (match/game), 選手/せんしゅ (athlete/player), 優勝/ゆうしょう (championship), 決勝/けっしょう (finals), 予選/よせん (preliminary round), 観戦/かんせん (watching a game), チケット (ticket), スタジアム (stadium), 得点/とくてん (score/points), 反則/はんそく (foul), 審判/しんぱん (referee), 延長/えんちょう (extension/overtime), 引き分け/ひきわけ (draw/tie), 記録/きろく (record), ファン (fan), 声援/せいえん (cheering voice), 実況/じっきょう (live commentary)

   **Intermediate (18 words, 5 sessions, 49 credits) — 10 curriculums:**
   - Curriculum 11: "Văn Hóa Công Sở" (Office Culture) — Japanese workplace culture: 敬語/けいご (honorific language), 報告/ほうこく (report), 連絡/れんらく (contact/communication), 相談/そうだん (consultation), 根回し/ねまわし (consensus-building), 飲み会/のみかい (drinking party), 忘年会/ぼうねんかい (year-end party), 歓迎会/かんげいかい (welcome party), 送別会/そうべつかい (farewell party), 年功序列/ねんこうじょれつ (seniority system), 終身雇用/しゅうしんこよう (lifetime employment), 有給休暇/ゆうきゅうきゅうか (paid vacation), 出張/しゅっちょう (business trip), 議事録/ぎじろく (meeting minutes), プレゼン (presentation), 締め切り/しめきり (deadline), 稟議/りんぎ (approval process), 社風/しゃふう (company culture)
   - Curriculum 12: "Nghệ Thuật Truyền Thống" (Traditional Arts) — Japanese traditional arts: 茶道/さどう (tea ceremony), 華道/かどう (flower arrangement), 書道/しょどう (calligraphy), 着物/きもの (kimono), 歌舞伎/かぶき (kabuki), 能/のう (noh theater), 落語/らくご (rakugo/comic storytelling), 浮世絵/うきよえ (ukiyo-e woodblock prints), 陶芸/とうげい (pottery), 漆器/しっき (lacquerware), 折り紙/おりがみ (origami), 盆栽/ぼんさい (bonsai), 和紙/わし (Japanese paper), 藍染め/あいぞめ (indigo dyeing), 師匠/ししょう (master/teacher), 弟子/でし (disciple/apprentice), 稽古/けいこ (practice/training), 流派/りゅうは (school/style)
   - Curriculum 13: "Tin Tức Và Thời Sự" (News and Current Events) — media/news vocabulary: 報道/ほうどう (news report), 記者/きしゃ (journalist), 取材/しゅざい (news coverage), 世論/せろん (public opinion), 選挙/せんきょ (election), 政策/せいさく (policy), 経済/けいざい (economy), 景気/けいき (economic conditions), 失業/しつぎょう (unemployment), 物価/ぶっか (prices/cost of living), 増税/ぞうぜい (tax increase), 少子化/しょうしか (declining birthrate), 高齢化/こうれいか (aging population), 環境問題/かんきょうもんだい (environmental issues), 国際/こくさい (international), 条約/じょうやく (treaty), 首脳/しゅのう (head of state), 外交/がいこう (diplomacy)
   - Curriculum 14: "Giáo Dục Ở Nhật" (Education in Japan) — education system vocabulary: 入学/にゅうがく (enrollment), 卒業/そつぎょう (graduation), 受験/じゅけん (entrance exam), 塾/じゅく (cram school), 偏差値/へんさち (deviation score), 奨学金/しょうがくきん (scholarship), 単位/たんい (credit/unit), 論文/ろんぶん (thesis/paper), 研究/けんきゅう (research), 教授/きょうじゅ (professor), 講義/こうぎ (lecture), 学費/がくひ (tuition), 留学/りゅうがく (study abroad), 部活/ぶかつ (club activities), 学園祭/がくえんさい (school festival), 成績/せいせき (grades), 進路/しんろ (career path), 就職活動/しゅうしょくかつどう (job hunting)
   - Curriculum 15: "Ẩm Thực Cao Cấp" (Fine Dining) — high-end food/restaurant vocabulary: 懐石/かいせき (kaiseki cuisine), 割烹/かっぽう (Japanese fine dining), 板前/いたまえ (sushi chef), 旬/しゅん (seasonal ingredient), 盛り付け/もりつけ (plating/presentation), 器/うつわ (vessel/dish), 出汁/だし (dashi stock), 発酵/はっこう (fermentation), 熟成/じゅくせい (aging/maturing), 食材/しょくざい (ingredients), 産地/さんち (place of origin), 予約制/よやくせい (reservation-only), おまかせ (chef's choice), コース (course meal), 日本酒/にほんしゅ (sake), 銘柄/めいがら (brand/label), 食感/しょっかん (texture), 香り/かおり (aroma/fragrance)
   - Curriculum 16: "Tâm Lý Và Cảm Xúc" (Psychology and Emotions) — emotional/psychological vocabulary: 感情/かんじょう (emotion), 不安/ふあん (anxiety), ストレス (stress), 鬱/うつ (depression), 自信/じしん (self-confidence), 劣等感/れっとうかん (inferiority complex), 共感/きょうかん (empathy), 孤独/こどく (loneliness), 達成感/たっせいかん (sense of achievement), 挫折/ざせつ (setback/frustration), 成長/せいちょう (growth), 自己肯定感/じここうていかん (self-esteem), 気分転換/きぶんてんかん (change of mood), 癒し/いやし (healing/comfort), 瞑想/めいそう (meditation), カウンセリング (counseling), 依存/いぞん (dependence/addiction), 回復/かいふく (recovery)
   - Curriculum 17: "Du Lịch Nông Thôn" (Rural Tourism) — countryside/rural vocabulary: 田舎/いなか (countryside), 温泉/おんせん (hot spring), 旅館/りょかん (Japanese inn), 民宿/みんしゅく (guesthouse), 農業体験/のうぎょうたいけん (farming experience), 収穫/しゅうかく (harvest), 田んぼ/たんぼ (rice paddy), 畑/はたけ (field/farm), 漁村/ぎょそん (fishing village), 古民家/こみんか (traditional house), 里山/さとやま (satoyama/rural landscape), 棚田/たなだ (terraced rice fields), 地元/じもと (local area), 方言/ほうげん (dialect), 祭り/まつり (festival), 郷土料理/きょうどりょうり (local cuisine), 自然/しぜん (nature), 景色/けしき (scenery)
   - Curriculum 18: "Công Nghệ Và AI" (Technology and AI) — modern technology vocabulary: 人工知能/じんこうちのう (artificial intelligence), 自動化/じどうか (automation), ロボット (robot), データ (data), アルゴリズム (algorithm), プログラミング (programming), セキュリティ (security), 個人情報/こじんじょうほう (personal information), SNS/エスエヌエス (social media), 炎上/えんじょう (online flaming), フェイクニュース (fake news), 仮想現実/かそうげんじつ (virtual reality), 電子決済/でんしけっさい (electronic payment), サブスク (subscription), クラウド (cloud), 通知/つうち (notification), 更新/こうしん (update), バグ (bug)
   - Curriculum 19: "Pháp Luật Và Quy Tắc" (Law and Rules) — legal/rules vocabulary: 法律/ほうりつ (law), 規則/きそく (rules/regulations), 違反/いはん (violation), 罰金/ばっきん (fine/penalty), 届出/とどけで (notification/report), 許可/きょか (permission), 届け出る/とどけでる (to file/report), 義務/ぎむ (obligation/duty), 権利/けんり (right), 契約/けいやく (contract), 保証/ほしょう (guarantee), 賠償/ばいしょう (compensation), 裁判/さいばん (trial/court), 弁護士/べんごし (lawyer), 証拠/しょうこ (evidence), 被害/ひがい (damage/harm), 犯罪/はんざい (crime), 防犯/ぼうはん (crime prevention)
   - Curriculum 20: "Môi Trường Và Bền Vững" (Environment and Sustainability) — environmental vocabulary: 環境/かんきょう (environment), リサイクル (recycling), 分別/ぶんべつ (waste sorting), 再生可能/さいせいかのう (renewable), エネルギー (energy), 温暖化/おんだんか (global warming), 排出/はいしゅつ (emission), 削減/さくげん (reduction), 持続可能/じぞくかのう (sustainable), エコ (eco-friendly), 省エネ/しょうえね (energy saving), 太陽光/たいようこう (solar), 風力/ふうりょく (wind power), 汚染/おせん (pollution), 生態系/せいたいけい (ecosystem), 絶滅危惧/ぜつめつきぐ (endangered), 森林伐採/しんりんばっさい (deforestation), 脱炭素/だつたんそ (decarbonization)

2. THE Curriculum_Creator SHALL select vocabulary words that are high-frequency at the JLPT N4-N3 level, practical, and relevant to Vietnamese adults living in or interacting with Japan.
3. THE Curriculum_Creator SHALL ensure no two curriculums have overlapping vocabulary lists (vocabList arrays must be unique across all 20 curriculums).
4. THE Curriculum_Creator SHALL ensure no vocabulary overlaps with the 20 beginner vi-ja curriculums.
5. WHEN creating reading passages, THE Curriculum_Creator SHALL use Japanese sentences of 10-20 words, incorporating basic kanji with furigana guidance, and scenarios appropriate for adults navigating real-life situations in Japan.


### Requirement 3: Preintermediate/Intermediate Content Design

**User Story:** As a content quality owner, I want all learner-facing content designed for adults at preintermediate and intermediate levels, so that learners are appropriately challenged while still receiving Vietnamese support.

#### Acceptance Criteria

1. WHEN learner-facing content is created for introAudio scripts, THE scripts SHALL use Vietnamese as the primary language, introducing each Japanese word with: the Japanese word (in standard written form including kanji where appropriate), furigana reading, Vietnamese meaning, an example sentence in Japanese (10-20 words), and contextual usage notes.
2. WHEN reading passages are created for preintermediate curriculums, THE passages SHALL be written in Japanese using hiragana, katakana, and basic kanji (JLPT N5-N4 level) with furigana annotations for all kanji. Passages SHALL be 150-250 characters and feature scenarios such as workplace interactions, travel situations, and social conversations.
3. WHEN reading passages are created for intermediate curriculums, THE passages SHALL be written in Japanese using hiragana, katakana, and kanji (JLPT N4-N3 level) with furigana annotations for kanji above N5 level. Passages SHALL be 200-350 characters and feature more complex scenarios such as cultural analysis, news discussion, and professional situations.
4. WHEN writingSentence prompts are created, THE prompts SHALL provide Vietnamese instructions, a complete Japanese example sentence (with furigana and Vietnamese translation), and a clear substitution pattern requiring the learner to use the target vocabulary word in a new context.
5. WHEN writingParagraph prompts are created (intermediate only), THE prompts SHALL require the learner to write 3-5 Japanese sentences using multiple vocabulary words from the curriculum, with Vietnamese instructions and guiding questions.
6. THE introAudio scripts SHALL provide furigana readings for all kanji vocabulary and explain kanji components or memory hooks where helpful for Vietnamese learners.
7. ALL user-facing text (titles, descriptions, previews, introAudio, writing prompts) SHALL be bilingual: Vietnamese for instructions/marketing, Japanese for reading passages and example sentences.

### Requirement 4: Activity Structure for Preintermediate Curriculums

**User Story:** As a platform owner, I want preintermediate curriculums to follow the established 5-session balanced_skills structure without advanced activities, so that learners build confidence before encountering more demanding tasks.

#### Acceptance Criteria

1. WHEN a preintermediate curriculum is created, THE 5 sessions SHALL follow this structure:
   - Session 1 (Learning): introAudio (welcome + topic intro), introAudio (teach words group 1 with furigana, Vietnamese meaning, example sentences), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), vocabLevel2 (group 1), introAudio (grammar/usage notes), reading (passage using group 1 words, 150-250 chars), speakReading, readAlong, writingSentence (3 items using group 1 words)
   - Session 2 (Learning): introAudio (recap group 1 + intro), introAudio (teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), vocabLevel2 (group 2), introAudio (grammar/usage notes), reading (passage using group 2 words, 150-250 chars), speakReading, readAlong, writingSentence (3 items using group 2 words)
   - Session 3 (Learning): introAudio (recap groups 1-2 + intro), introAudio (teach words group 3), viewFlashcards (group 3), speakFlashcards (group 3), vocabLevel1 (group 3), vocabLevel2 (group 3), introAudio (grammar/usage notes), reading (passage using group 3 words, 150-250 chars), speakReading, readAlong, writingSentence (3 items using group 3 words)
   - Session 4 (Review): introAudio (review intro), viewFlashcards (all 18 words), speakFlashcards (all 18 words), vocabLevel1 (all 18 words), vocabLevel2 (all 18 words), writingSentence (4-5 items mixing all groups)
   - Session 5 (Final Reading): introAudio (full reading intro), reading (full article using all 18 words, 400-600 chars), speakReading, readAlong, introAudio (farewell with vocab review)

2. THE preintermediate curriculum SHALL NOT include vocabLevel3 or writingParagraph activities in any session.

### Requirement 5: Activity Structure for Intermediate Curriculums

**User Story:** As a platform owner, I want intermediate curriculums to include more demanding activities like writingParagraph and vocabLevel3, so that learners are pushed toward greater fluency and production.

#### Acceptance Criteria

1. WHEN an intermediate curriculum is created, THE 5 sessions SHALL follow this structure:
   - Session 1 (Learning): introAudio (welcome + topic intro), introAudio (teach words group 1 with furigana, Vietnamese meaning, example sentences), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), vocabLevel2 (group 1), introAudio (grammar/usage notes), reading (passage using group 1 words, 200-350 chars), speakReading, readAlong, writingSentence (3 items using group 1 words)
   - Session 2 (Learning): introAudio (recap group 1 + intro), introAudio (teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), vocabLevel2 (group 2), introAudio (grammar/usage notes), reading (passage using group 2 words, 200-350 chars), speakReading, readAlong, writingSentence (3 items using group 2 words)
   - Session 3 (Learning): introAudio (recap groups 1-2 + intro), introAudio (teach words group 3), viewFlashcards (group 3), speakFlashcards (group 3), vocabLevel1 (group 3), vocabLevel2 (group 3), introAudio (grammar/usage notes), reading (passage using group 3 words, 200-350 chars), speakReading, readAlong, writingSentence (3 items using group 3 words)
   - Session 4 (Review): introAudio (review intro), viewFlashcards (all 18 words), speakFlashcards (all 18 words), vocabLevel1 (all 18 words), vocabLevel2 (all 18 words), vocabLevel3 (all 18 words), writingSentence (4-5 items mixing all groups)
   - Session 5 (Final Reading): introAudio (full reading intro), reading (full article using all 18 words, 500-800 chars), speakReading, readAlong, writingParagraph (using 6+ vocabulary words), introAudio (farewell with vocab review)

2. THE intermediate curriculum SHALL include vocabLevel3 in the review session (Session 4) only.
3. THE intermediate curriculum SHALL include writingParagraph in the final reading session (Session 5) only.

### Requirement 6: Vietnamese Marketing Copy

**User Story:** As a content quality owner, I want all marketing text written in Vietnamese with persuasive copy standards, so that Vietnamese learners feel motivated to advance their Japanese skills.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL write curriculum descriptions as Persuasive_Copy following the 5-beat structure, addressing adult learner aspirations: career advancement with Japanese companies, deeper cultural understanding, confident travel in Japan, and intellectual growth through mastering kanji and complex grammar.
2. THE Curriculum_Creator SHALL write curriculum previews (~150 words) as Persuasive_Copy with vivid hooks about the learner's Japanese journey at this level, vocabulary word listing (Japanese + furigana + Vietnamese meaning), and what the learner will be able to do after completing the curriculum.
3. THE Curriculum_Creator SHALL write all titles, descriptions, and preview text in Vietnamese (as required for preintermediate/intermediate vi-ja curriculums where userLanguage="vi").
4. THE Tone_Assigner SHALL assign one of the 6 Tone_Palette types to every curriculum description headline.
5. WHILE assigning tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Tone_Palette type.
6. THE Tone_Assigner SHALL ensure no single Tone_Palette type exceeds 30% of the 20 curriculum descriptions (max 6 uses per tone).
7. THE Persuasive_Copy SHALL emphasize the practical value of intermediate Japanese for Vietnamese adults: navigating Japanese bureaucracy, building professional relationships, understanding media and news, and experiencing Japan beyond tourist-level interactions.

### Requirement 7: introAudio Quality

**User Story:** As a content quality owner, I want introAudio scripts that effectively teach Japanese vocabulary with kanji awareness to Vietnamese speakers, so that learners build reading skills alongside vocabulary.

#### Acceptance Criteria

1. WHEN a welcome introAudio is created, THE script (500-800 words) SHALL greet the learner warmly in Vietnamese, introduce the topic with a motivating hook, list all 6 vocabulary words for the session, and teach each word with: the Japanese word (kanji + furigana), Vietnamese meaning, part of speech, a contextual example sentence in Japanese with Vietnamese translation, and a kanji breakdown or memory hook where applicable.
2. WHEN a vocabulary-teaching introAudio is created, THE script SHALL explain how each word is used in real Japanese contexts, noting formality levels (casual vs. polite vs. keigo) where relevant.
3. WHEN a session recap introAudio is created (sessions 2-3), THE script SHALL briefly recap previous session words with furigana before introducing new ones — using phrases like "Bạn còn nhớ không?" and providing quick-review example sentences.
4. WHEN a grammar/usage introAudio is created, THE script SHALL explain 1-2 grammar patterns relevant to the session's vocabulary, with Vietnamese explanations and Japanese example sentences.
5. WHEN a farewell introAudio is created, THE script (400-600 words) SHALL review 5-6 key vocabulary words with definitions and fresh Japanese example sentences (with furigana and Vietnamese translation), summarize the learning journey, and close with a warm personal sign-off.
6. THE Curriculum_Creator SHALL individually craft every introAudio script for its specific curriculum topic, without using template functions or string interpolation.
7. THE Tone_Assigner SHALL assign one of the 5 Farewell_Palette registers to every farewell introAudio.
8. WHILE assigning farewell tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Farewell_Palette register.

### Requirement 8: Pricing

**User Story:** As a platform owner, I want preintermediate/intermediate curriculums priced at the standard rate, so that pricing is consistent with the rest of the catalog.

#### Acceptance Criteria

1. WHEN a preintermediate or intermediate curriculum (5 sessions) is created, THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 49`.
2. THE Curriculum_Creator SHALL set the price after the curriculum is successfully created and added to its series.

### Requirement 9: Collection and Series Organization

**User Story:** As a platform owner, I want the 20 preintermediate/intermediate curriculums organized into a dedicated collection with thematic series, so that learners can browse content by interest area and find a clear progression from the beginner collection.

#### Acceptance Criteria

1. THE Collection_Organizer SHALL create 1 NEW collection titled "Tiếng Nhật Trung Cấp" (Intermediate Japanese) with a neutral, informative Vietnamese description explaining this is a collection of Japanese curriculums for Vietnamese adults advancing beyond beginner level, covering workplace, culture, travel, and daily life topics.
2. THE Collection_Organizer SHALL organize the 20 curriculums into 5 series of 4 curriculums each:
   - Series 1: "Sự Nghiệp Tại Nhật" (Career in Japan) — containing Curriculums 1, 4, 8, 11 (job interview, renting, phone communication, office culture). Description ≤255 chars using a Tone_Palette type.
   - Series 2: "Khám Phá Nhật Bản" (Discovering Japan) — containing Curriculums 2, 3, 15, 17 (booking/planning, street food, fine dining, rural tourism). Description ≤255 chars using a different Tone_Palette type.
   - Series 3: "Đời Sống Và Xã Hội" (Life and Society) — containing Curriculums 5, 6, 7, 16 (medical visit, social relationships, natural disasters, psychology/emotions). Description ≤255 chars using a different Tone_Palette type.
   - Series 4: "Văn Hóa Và Nghệ Thuật" (Culture and Arts) — containing Curriculums 12, 13, 14, 19 (traditional arts, news/current events, education, law/rules). Description ≤255 chars using a different Tone_Palette type.
   - Series 5: "Thế Giới Hiện Đại" (The Modern World) — containing Curriculums 9, 10, 18, 20 (online shopping, sports/cheering, technology/AI, environment/sustainability). Description ≤255 chars using a different Tone_Palette type.
3. THE Collection_Organizer SHALL wire each series to the collection via `curriculum-collection/addSeriesToCollection`.
4. THE Collection_Organizer SHALL set display orders for all 5 series within the collection via `curriculum-series/setDisplayOrder`.
5. THE Collection_Organizer SHALL set display orders for all curriculums within each series via `curriculum/setDisplayOrder`.
6. THE Collection_Organizer SHALL ensure all curriculums within each series share `language: "ja"` and `userLanguage: "vi"`.
7. WHILE assigning series description tones, THE Tone_Assigner SHALL ensure all 5 series use different Tone_Palette types.
8. WITHIN each series, THE maximum difficulty level gap SHALL be 1 level (preintermediate + intermediate is acceptable).

### Requirement 10: Activity Schema Compliance

**User Story:** As a platform developer, I want every activity to comply with the platform's content schema, so that the content pipeline processes Japanese curriculums without errors.

#### Acceptance Criteria

1. Each Activity SHALL include `activityType`, `title`, `description`, and `data` fields.
2. THE `activityType` field SHALL use one of the valid values: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence, writingParagraph.
3. THE `vocabList` field SHALL be an array of lowercase strings (Japanese words in their standard written form), using the field name `vocabList` (never `words`).
4. WHEN viewFlashcards and speakFlashcards appear in the same session, THE two activities SHALL have identical `vocabList` arrays.
5. All content data SHALL be inside the `data` object, not inline on the activity object.
6. WHEN a writingSentence activity is created, THE activity SHALL have `data.vocabList`, `data.items` (non-empty array), and each item SHALL have `prompt` (Vietnamese instructions with Japanese example sentence, furigana, Vietnamese translation, and substitution pattern) and `targetVocab` fields.
7. WHEN a writingParagraph activity is created (intermediate only), THE activity SHALL have `data.vocabList`, `data.instructions` (Vietnamese), and `data.prompts` (array of at least 2 guiding questions in Vietnamese).
8. THE Curriculum_Creator SHALL follow the activity title/description conventions: viewFlashcards/speakFlashcards/vocabLevel* use "Flashcards: <topic>"; reading/speakReading use "Đọc: <topic>"; readAlong uses "Nghe: <topic>"; introAudio uses descriptive labels; writingSentence uses "Viết: <topic>"; writingParagraph uses "Viết đoạn: <topic>".

### Requirement 11: Content Validation

**User Story:** As a platform developer, I want every curriculum validated before upload, so that no corrupted content enters the database.

#### Acceptance Criteria

1. THE Content_Validator SHALL verify that every curriculum content JSON has non-null, non-empty `title`, `description`, and `preview.text` fields.
2. THE Content_Validator SHALL verify that `learningSessions` is a non-empty array with exactly 5 sessions, each having a non-empty `title` and `activities` array.
3. THE Content_Validator SHALL verify that every activity has `activityType` (not `type`), `title`, `description`, and `data` fields, with content fields inside `data`.
4. THE Content_Validator SHALL verify that `activityType` values are valid.
5. THE Content_Validator SHALL verify that vocabList fields contain arrays of strings using the field name `vocabList`.
6. THE Content_Validator SHALL verify that viewFlashcards and speakFlashcards in the same session have identical vocabList arrays.
7. THE Content_Validator SHALL verify writingSentence data structures (vocabList, items with prompt and targetVocab).
8. THE Content_Validator SHALL verify writingParagraph data structures for intermediate curriculums (vocabList, instructions, prompts array with ≥2 items).
9. THE Content_Validator SHALL verify that no Strip_Keys appear anywhere in the content JSON.
10. THE Content_Validator SHALL verify that preintermediate curriculums do NOT contain writingParagraph or vocabLevel3 activities.
11. THE Content_Validator SHALL verify that intermediate curriculums contain vocabLevel3 only in Session 4 and writingParagraph only in Session 5.
12. IF any validation check fails, THEN THE Content_Validator SHALL abort the upload and print the specific rule violation.

### Requirement 12: Script Architecture and Workflow

**User Story:** As a developer, I want a clear, repeatable workflow for creating 20 preintermediate/intermediate curriculums, so that the process is manageable and traceable.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce one standalone Python script per curriculum (20 scripts total).
2. THE Curriculum_Creator SHALL produce one orchestrator script that creates the collection, 5 series, wires them together, and sets display orders.
3. THE Curriculum_Creator SHALL organize scripts into a directory `vi-ja-preintermediate-curriculums/`.
4. THE Curriculum_Creator SHALL authenticate all API calls using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
5. THE Curriculum_Creator SHALL use `https://helloapi.step.is` as the API base URL.
6. THE Curriculum_Creator SHALL individually craft every piece of learner-facing text for its specific curriculum topic, without using template functions, string interpolation, or generic fill-in-the-blank patterns.
7. THE Curriculum_Creator MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.
8. IF a curriculum creation API call fails, THEN THE Curriculum_Creator SHALL log the error with the curriculum title and continue with the next curriculum.

### Requirement 13: Newly Created Curriculums Must Be Private

**User Story:** As a platform owner, I want all newly created Japanese curriculums to be private by default, so that they go through content generation (audio, illustrations) before being exposed to learners.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL NOT call `curriculum/setPublic` with `isPublic: true` on any newly created curriculum.

### Requirement 14: Curriculum Titles

**User Story:** As a content quality owner, I want curriculum titles to be minimal, engaging, and in Vietnamese, so that they work well within the series/collection context.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL keep curriculum titles minimal — never repeating series/collection name, content type prefix, skill-focus label, difficulty level, or audience suffix.
2. THE Curriculum_Creator SHALL write curriculum titles in Vietnamese.
3. THE curriculum titles SHALL NOT include difficulty level indicators (e.g., "preintermediate", "intermediate", "trung cấp", "中級").
4. THE curriculum titles SHALL be engaging and descriptive — using clear, motivating language that tells the learner what topic they will explore.

### Requirement 15: Documentation and Cleanup

**User Story:** As a developer, I want proper documentation after all curriculums are created, so that the content is traceable and reproducible.

#### Acceptance Criteria

1. WHEN all 20 curriculums are created and verified, THE Curriculum_Creator SHALL create a README.md documenting: collection ID, all series IDs, all curriculum IDs with titles and display orders, vocabulary lists per curriculum, tone assignments (description and farewell for all 20), pricing, and SQL verification queries.
2. WHEN all curriculums are verified in the database, THE source Python scripts SHALL be deleted, leaving only the README.
3. THE Curriculum_Creator SHALL run a duplicate check query for each curriculum title after creation and resolve any duplicates (keep earliest, delete extras).

### Requirement 16: Execution Order

**User Story:** As a developer, I want a phased execution plan, so that I can create the infrastructure first and then add curriculums incrementally.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL execute creation in this order: (1) create collection and 5 series via orchestrator, (2) create preintermediate curriculums (10 scripts), (3) create intermediate curriculums (10 scripts).
2. WHEN each curriculum is created, THE Curriculum_Creator SHALL immediately add it to the appropriate series, set its display order, and set its price.
3. WHEN all 20 curriculums are created, THE Curriculum_Creator SHALL verify the complete set by querying the database to confirm all curriculums exist with correct display orders, language values, prices, and non-empty content.
4. IF verification reveals missing or malformed curriculums, THEN THE Curriculum_Creator SHALL recreate the affected curriculums before finalizing documentation.