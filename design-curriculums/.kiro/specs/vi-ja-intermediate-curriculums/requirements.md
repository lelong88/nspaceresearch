# Requirements Document

## Introduction

Create 20 Japanese-learning curriculums for Vietnamese-speaking adults at the intermediate and upper-intermediate levels. Language pair: userLanguage="vi", language="ja". This is the third vi-ja curriculum set, building on the existing 20 beginner curriculums and 20 preintermediate/intermediate curriculums.

These 20 curriculums target learners who have completed the preintermediate set and are ready for more sophisticated vocabulary, complex sentence structures, nuanced cultural understanding, and professional-level communication. At this level, learners are comfortable with basic kanji (JLPT N4) and are expanding into N3-N2 territory. Reading passages use kanji freely with selective furigana (only for N2+ kanji). Topics cover diverse life domains: business strategy, media literacy, personal development, social issues, creative arts, science, philosophy, and cross-cultural communication — areas where Vietnamese adults at this level need deeper Japanese vocabulary to function professionally and intellectually.

### What This Spec Covers

- 20 individually crafted curriculums for Vietnamese adults learning Japanese at intermediate and upper-intermediate levels
- 18 vocabulary words per curriculum divided into 3 groups of 6
- 5 sessions per curriculum: 3 learning sessions, 1 review session, 1 final reading session
- Diverse topics covering business, media, personal development, society, arts, science, philosophy, and cross-cultural domains
- Japanese vocabulary includes kanji with furigana for N2+ level kanji
- Vietnamese marketing text for intermediate; bilingual or Vietnamese for upper-intermediate
- Collection and series organization
- Pricing at 49 credits per curriculum (standard for intermediate/upper-intermediate with 5 sessions)

### What This Spec Does NOT Cover

- Changes to the existing 20 beginner or 20 preintermediate vi-ja curriculums
- Advanced-level Japanese curriculums
- Overlap with beginner topics (greetings, numbers, family, colors, weather, drinks, days, emotions, food, shopping, transport, hotel, office, seasons, hobbies, health, housing, festivals, technology, sports) or preintermediate topics (job interview, booking/planning, street food, renting, medical visit, social relationships, natural disasters, phone communication, online shopping, sports cheering, office culture, traditional arts, news/current events, education, fine dining, psychology/emotions, rural tourism, technology/AI, law/rules, environment/sustainability)
- Content generation pipeline (audio, illustrations) — curriculums are created private
- Grammar-focused curriculums (these are vocabulary-based balanced_skills)

## Glossary

- **Intermediate_Curriculum**: A curriculum for Vietnamese adults learning Japanese at intermediate level. Uses bilingual text (Vietnamese + Japanese). Vocabulary includes kanji (JLPT N3 level). 18 words across 5 sessions. Includes vocabLevel3 in review session. Includes writingParagraph in final session. All marketing text in Vietnamese.
- **Upper_Intermediate_Curriculum**: A curriculum for Vietnamese adults learning Japanese at upper-intermediate level. May use bilingual or single-language content per platform policy. Vocabulary includes kanji (JLPT N3-N2 level). 18 words across 5 sessions. Includes vocabLevel3 in review session. Includes writingParagraph in final session. Marketing text may be bilingual or Vietnamese.
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
- **Furigana**: Hiragana reading annotations placed above kanji characters to indicate pronunciation. At intermediate/upper-intermediate level, furigana is provided selectively — only for N2+ kanji that learners may not yet know.
- **Kanji**: Chinese characters used in Japanese writing. At intermediate level, learners handle N3 kanji comfortably. At upper-intermediate, learners encounter N3-N2 kanji with selective furigana support.

## Requirements

### Requirement 1: Intermediate/Upper-Intermediate Curriculum Format and Structure

**User Story:** As a platform owner, I want 20 Japanese-learning curriculums at intermediate and upper-intermediate levels for Vietnamese adults, so that learners who completed the preintermediate set have a clear next step toward professional-level Japanese.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce exactly 20 curriculums for the vi-ja Language_Pair at intermediate and upper-intermediate levels.
2. THE Curriculum_Creator SHALL create 10 intermediate curriculums and 10 upper-intermediate curriculums.
3. WHEN an intermediate or upper-intermediate curriculum is created, THE curriculum SHALL contain exactly 18 vocabulary words divided into 3 groups of 6.
4. WHEN an intermediate or upper-intermediate curriculum is created, THE curriculum SHALL contain exactly 5 sessions: 3 learning sessions, 1 review session, and 1 final reading session.
5. THE curriculum SHALL include `contentTypeTags: []` at the top level of the content JSON (topic-based).
6. THE curriculum SHALL never include Strip_Keys in the content JSON.
7. THE Curriculum_Creator SHALL set `language: "ja"` and `userLanguage: "vi"` as top-level body parameters in the `curriculum/create` API call.
8. WHEN an intermediate curriculum is created, THE curriculum SHALL include `vocabLevel3` in the review session.
9. WHEN an intermediate curriculum is created, THE curriculum SHALL include `writingParagraph` in the final reading session.
10. WHEN an upper-intermediate curriculum is created, THE curriculum SHALL include `vocabLevel3` in the review session.
11. WHEN an upper-intermediate curriculum is created, THE curriculum SHALL include `writingParagraph` in the final reading session.

### Requirement 2: Topic Plan for 20 Intermediate/Upper-Intermediate Curriculums

**User Story:** As a platform owner, I want diverse topics that challenge learners with sophisticated vocabulary across business, media, personal development, society, arts, science, and cross-cultural domains, so that learners can function professionally and intellectually in Japanese.

#### Acceptance Criteria

1. THE 20 curriculums SHALL cover the following topics, each individually crafted. No topic SHALL overlap with the 20 beginner curriculums or the 20 preintermediate curriculums.

   **Intermediate (18 words, 5 sessions, 49 credits) — 10 curriculums:**
   - Curriculum 1: "Đàm Phán Kinh Doanh" (Business Negotiation) — negotiation and deal-making vocabulary: 交渉/こうしょう (negotiation), 提案/ていあん (proposal), 妥協/だきょう (compromise), 条件/じょうけん (conditions), 合意/ごうい (agreement), 利益/りえき (profit/benefit), 競合/きょうごう (competition), 戦略/せんりゃく (strategy), 見積もり/みつもり (estimate/quote), 契約書/けいやくしょ (contract document), 納期/のうき (delivery deadline), 取引先/とりひきさき (business partner), 値下げ/ねさげ (price reduction), 決裁/けっさい (approval/authorization), 商談/しょうだん (business talk), 譲歩/じょうほ (concession), 双方/そうほう (both parties), 成約/せいやく (closing a deal)
   - Curriculum 2: "Truyền Thông Và Quảng Cáo" (Media and Advertising) — media/marketing vocabulary: 広告/こうこく (advertisement), 宣伝/せんでん (publicity/promotion), ブランド (brand), ターゲット (target audience), キャンペーン (campaign), 消費者/しょうひしゃ (consumer), 影響力/えいきょうりょく (influence), 口コミ/くちこみ (word of mouth), インフルエンサー (influencer), 視聴率/しちょうりつ (viewership rating), メディア (media), 炎上/えんじょう (online backlash), 印象/いんしょう (impression), 訴求/そきゅう (appeal), 差別化/さべつか (differentiation), コンテンツ (content), 拡散/かくさん (viral spread), 認知度/にんちど (brand awareness)
   - Curriculum 3: "Tài Chính Cá Nhân" (Personal Finance) — money management vocabulary: 貯金/ちょきん (savings), 投資/とうし (investment), 株/かぶ (stocks), 利息/りそく (interest), 借金/しゃっきん (debt), 返済/へんさい (repayment), 家計/かけい (household budget), 節約/せつやく (economizing), 資産/しさん (assets), 年金/ねんきん (pension), 保険/ほけん (insurance), 税金/ぜいきん (tax), 確定申告/かくていしんこく (tax return), ローン (loan), 金利/きんり (interest rate), 収支/しゅうし (income and expenses), 老後/ろうご (old age/retirement), 運用/うんよう (asset management)
   - Curriculum 4: "Hôn Nhân Và Gia Đình Hiện Đại" (Modern Marriage and Family) — family dynamics vocabulary: 結婚/けっこん (marriage), 離婚/りこん (divorce), 共働き/ともばたらき (dual income), 育児/いくじ (childcare), 家事分担/かじぶんたん (sharing housework), 嫁姑/よめしゅうとめ (wife-mother-in-law), 晩婚/ばんこん (late marriage), 少子化/しょうしか (declining birthrate), 核家族/かくかぞく (nuclear family), 介護/かいご (elderly care), 世代間/せだいかん (intergenerational), 価値観/かちかん (values), 同棲/どうせい (cohabitation), 養育費/よういくひ (child support), 親権/しんけん (custody), 扶養/ふよう (financial support/dependents), 相続/そうぞく (inheritance), 家族構成/かぞくこうせい (family structure)
   - Curriculum 5: "Phát Triển Bản Thân" (Self-Development) — personal growth vocabulary: 目標/もくひょう (goal), 習慣/しゅうかん (habit), 自己啓発/じこけいはつ (self-improvement), 時間管理/じかんかんり (time management), 優先順位/ゆうせんじゅんい (priority), 集中力/しゅうちゅうりょく (concentration), 生産性/せいさんせい (productivity), モチベーション (motivation), 振り返り/ふりかえり (reflection), 挑戦/ちょうせん (challenge), 失敗/しっぱい (failure), 克服/こくふく (overcoming), 継続/けいぞく (continuation/persistence), 成果/せいか (results/achievements), 計画/けいかく (plan), 実行/じっこう (execution), 改善/かいぜん (improvement/kaizen), 意志力/いしりょく (willpower)
   - Curriculum 6: "Văn Hóa Manga Và Anime" (Manga and Anime Culture) — otaku culture vocabulary: 漫画/まんが (manga), アニメ (anime), 声優/せいゆう (voice actor), 連載/れんさい (serialization), 単行本/たんこうぼん (collected volume), 同人誌/どうじんし (doujinshi/fan work), コスプレ (cosplay), 聖地巡礼/せいちじゅんれい (anime pilgrimage), 原作/げんさく (original work), 作画/さくが (animation/drawing), 伏線/ふくせん (foreshadowing), 展開/てんかい (plot development), ジャンル (genre), 主人公/しゅじんこう (protagonist), 世界観/せかいかん (worldview/setting), 名場面/めいばめん (iconic scene), 完結/かんけつ (completion/finale), ファン層/ふぁんそう (fanbase)
   - Curriculum 7: "Y Học Và Sức Khỏe Tinh Thần" (Medicine and Mental Health) — mental health vocabulary: 精神科/せいしんか (psychiatry), 心療内科/しんりょうないか (psychosomatic medicine), 適応障害/てきおうしょうがい (adjustment disorder), 燃え尽き/もえつき (burnout), 過労/かろう (overwork), 休職/きゅうしょく (leave of absence), 復職/ふくしょく (return to work), 治療/ちりょう (treatment), 薬物療法/やくぶつりょうほう (pharmacotherapy), 認知行動療法/にんちこうどうりょうほう (CBT), 偏見/へんけん (prejudice/stigma), 理解/りかい (understanding), 支援/しえん (support), 相談窓口/そうだんまどぐち (consultation desk), 早期発見/そうきはっけん (early detection), 予防/よぼう (prevention), 回復/かいふく (recovery), 社会復帰/しゃかいふっき (social reintegration)
   - Curriculum 8: "Bất Động Sản Và Đầu Tư" (Real Estate and Investment) — property/investment vocabulary: 不動産投資/ふどうさんとうし (real estate investment), 物件/ぶっけん (property), 利回り/りまわり (yield/return), 頭金/あたまきん (down payment), 住宅ローン/じゅうたくローン (mortgage), 固定資産税/こていしさんぜい (property tax), 管理会社/かんりがいしゃ (management company), 空室/くうしつ (vacancy), 入居者/にゅうきょしゃ (tenant), 修繕/しゅうぜん (repair/renovation), 築年数/ちくねんすう (building age), 立地/りっち (location), 相場/そうば (market price), 査定/さてい (appraisal), 仲介/ちゅうかい (brokerage), 登記/とうき (registration), 融資/ゆうし (financing), 収益/しゅうえき (revenue/income)
   - Curriculum 9: "Ẩm Thực Thế Giới Tại Nhật" (World Cuisine in Japan) — international food culture vocabulary: 多国籍料理/たこくせきりょうり (multinational cuisine), 食文化/しょくぶんか (food culture), 本場/ほんば (authentic/original place), 調理法/ちょうりほう (cooking method), 食材/しょくざい (ingredients), 香辛料/こうしんりょう (spices), 食感/しょっかん (texture), 盛り付け/もりつけ (plating), 食べ放題/たべほうだい (all-you-can-eat), 予約必須/よやくひっす (reservation required), 行列店/ぎょうれつてん (popular restaurant with queues), 食レポ/しょくれぽ (food review), グルメ (gourmet), ミシュラン (Michelin), 隠れ家/かくれが (hidden gem restaurant), 食通/しょくつう (foodie/connoisseur), 創作料理/そうさくりょうり (creative cuisine), 食べログ/たべろぐ (food review site)
   - Curriculum 10: "Giao Thông Và Đô Thị" (Transportation and Urban Life) — urban planning vocabulary: 都市計画/としけいかく (urban planning), 再開発/さいかいはつ (redevelopment), 人口密度/じんこうみつど (population density), 通勤ラッシュ/つうきんラッシュ (commuter rush), 渋滞/じゅうたい (traffic jam), 公共交通/こうきょうこうつう (public transport), 路線図/ろせんず (route map), 乗車率/じょうしゃりつ (occupancy rate), 終電/しゅうでん (last train), 始発/しはつ (first train), 定期券/ていきけん (commuter pass), 混雑/こんざつ (congestion), 時差出勤/じさしゅっきん (staggered commuting), テレワーク (telework), 郊外/こうがい (suburbs), 都心/としん (city center), インフラ (infrastructure), バリアフリー (barrier-free/accessibility)

   **Upper-Intermediate (18 words, 5 sessions, 49 credits) — 10 curriculums:**
   - Curriculum 11: "Triết Học Sống Của Người Nhật" (Japanese Philosophy of Living) — life philosophy vocabulary: 生きがい/いきがい (ikigai/reason for living), 侘び寂び/わびさび (wabi-sabi), 無常/むじょう (impermanence), 一期一会/いちごいちえ (once-in-a-lifetime encounter), 本音/ほんね (true feelings), 建前/たてまえ (public facade), 義理/ぎり (social obligation), 恩/おん (debt of gratitude), 和/わ (harmony), 空気/くうき (atmosphere/social pressure), 甘え/あまえ (dependence/indulgence), 我慢/がまん (endurance/patience), 反省/はんせい (self-reflection), 謙虚/けんきょ (humility), 思いやり/おもいやり (consideration/empathy), 潔い/いさぎよい (graceful acceptance), 道/みち (the way/path), 修行/しゅぎょう (ascetic training/discipline)
   - Curriculum 12: "Chính Trị Và Xã Hội Nhật Bản" (Japanese Politics and Society) — political/social vocabulary: 民主主義/みんしゅしゅぎ (democracy), 国会/こっかい (parliament/Diet), 与党/よとう (ruling party), 野党/やとう (opposition party), 憲法/けんぽう (constitution), 改正/かいせい (amendment/revision), 世論調査/せろんちょうさ (opinion poll), 投票率/とうひょうりつ (voter turnout), 格差/かくさ (disparity/gap), 福祉/ふくし (welfare), 移民/いみん (immigration), 多様性/たようせい (diversity), 差別/さべつ (discrimination), 人権/じんけん (human rights), 市民運動/しみんうんどう (civic movement), 規制緩和/きせいかんわ (deregulation), 官僚/かんりょう (bureaucrat), 地方自治/ちほうじち (local autonomy)
   - Curriculum 13: "Khoa Học Và Khám Phá" (Science and Discovery) — scientific vocabulary: 研究者/けんきゅうしゃ (researcher), 論文/ろんぶん (academic paper), 仮説/かせつ (hypothesis), 実験/じっけん (experiment), 発見/はっけん (discovery), 証明/しょうめい (proof), 理論/りろん (theory), 応用/おうよう (application), 学会/がっかい (academic conference), ノーベル賞/ノーベルしょう (Nobel Prize), 特許/とっきょ (patent), 革新/かくしん (innovation), 量子/りょうし (quantum), 遺伝子/いでんし (gene), 人工知能/じんこうちのう (artificial intelligence), 宇宙/うちゅう (space/universe), 再生医療/さいせいいりょう (regenerative medicine), 持続可能/じぞくかのう (sustainable)
   - Curriculum 14: "Văn Học Nhật Bản" (Japanese Literature) — literary vocabulary: 文学/ぶんがく (literature), 小説/しょうせつ (novel), 短編/たんぺん (short story), 随筆/ずいひつ (essay), 俳句/はいく (haiku), 作家/さっか (author/writer), 芥川賞/あくたがわしょう (Akutagawa Prize), 直木賞/なおきしょう (Naoki Prize), 純文学/じゅんぶんがく (literary fiction), 大衆文学/たいしゅうぶんがく (popular fiction), 翻訳/ほんやく (translation), 出版/しゅっぱん (publishing), 書評/しょひょう (book review), 描写/びょうしゃ (description/depiction), 比喩/ひゆ (metaphor), 主題/しゅだい (theme), 文体/ぶんたい (writing style), 読書感想文/どくしょかんそうぶん (book report)
   - Curriculum 15: "Khởi Nghiệp Tại Nhật" (Entrepreneurship in Japan) — startup vocabulary: 起業/きぎょう (starting a business), 創業者/そうぎょうしゃ (founder), ベンチャー (venture), 資金調達/しきんちょうたつ (fundraising), 事業計画/じぎょうけいかく (business plan), 投資家/とうしか (investor), 株式公開/かぶしきこうかい (IPO), 黒字/くろじ (profit/in the black), 赤字/あかじ (loss/in the red), 市場調査/しじょうちょうさ (market research), 差別化/さべつか (differentiation), 顧客/こきゃく (customer), 売上/うりあげ (sales/revenue), 撤退/てったい (withdrawal/exit), 失敗/しっぱい (failure), 再挑戦/さいちょうせん (retry/second attempt), 人脈/じんみゃく (network/connections), ピッチ (pitch)
   - Curriculum 16: "Thiên Nhiên Và Sinh Thái" (Nature and Ecology) — ecology vocabulary: 生態系/せいたいけい (ecosystem), 生物多様性/せいぶつたようせい (biodiversity), 絶滅危惧種/ぜつめつきぐしゅ (endangered species), 食物連鎖/しょくもつれんさ (food chain), 光合成/こうごうせい (photosynthesis), 共生/きょうせい (symbiosis), 外来種/がいらいしゅ (invasive species), 固有種/こゆうしゅ (endemic species), 保護区/ほごく (protected area), 森林/しんりん (forest), 湿地/しっち (wetland), 干潟/ひがた (tidal flat), 珊瑚礁/さんごしょう (coral reef), 渡り鳥/わたりどり (migratory bird), 生息地/せいそくち (habitat), 環境保全/かんきょうほぜん (environmental conservation), 自然遺産/しぜんいさん (natural heritage), 里山/さとやま (satoyama landscape)
   - Curriculum 17: "Tội Phạm Và Công Lý" (Crime and Justice) — criminal justice vocabulary: 犯罪/はんざい (crime), 捜査/そうさ (investigation), 逮捕/たいほ (arrest), 容疑者/ようぎしゃ (suspect), 裁判/さいばん (trial), 判決/はんけつ (verdict/sentence), 無罪/むざい (not guilty), 有罪/ゆうざい (guilty), 刑務所/けいむしょ (prison), 仮釈放/かりしゃくほう (parole), 再犯/さいはん (recidivism), 被害者/ひがいしゃ (victim), 加害者/かがいしゃ (perpetrator), 冤罪/えんざい (wrongful conviction), 死刑/しけい (death penalty), 更生/こうせい (rehabilitation), 司法/しほう (judiciary), 陪審員/ばいしんいん (juror)
   - Curriculum 18: "Trí Tuệ Nhân Tạo Và Tương Lai" (AI and the Future) — advanced AI vocabulary: 機械学習/きかいがくしゅう (machine learning), 深層学習/しんそうがくしゅう (deep learning), 自然言語処理/しぜんげんごしょり (natural language processing), 画像認識/がぞうにんしき (image recognition), 自動運転/じどううんてん (autonomous driving), 倫理/りんり (ethics), 雇用/こよう (employment), 代替/だいたい (replacement/substitution), 共存/きょうぞん (coexistence), 創造性/そうぞうせい (creativity), 判断/はんだん (judgment), 責任/せきにん (responsibility), 規制/きせい (regulation), 透明性/とうめいせい (transparency), 偏り/かたより (bias), 進化/しんか (evolution), 特異点/とくいてん (singularity), 汎用/はんよう (general-purpose)
   - Curriculum 19: "Giải Trí Và Truyền Hình" (Entertainment and Television) — entertainment industry vocabulary: 番組/ばんぐみ (TV program), バラエティ (variety show), ドラマ (drama/TV series), 視聴者/しちょうしゃ (viewer), 脚本/きゃくほん (screenplay), 演出/えんしゅつ (direction/production), 出演/しゅつえん (appearance/performance), 芸能人/げいのうじん (celebrity), お笑い/おわらい (comedy), 漫才/まんざい (manzai comedy), コント (skit/comedy sketch), 司会/しかい (host/MC), 生放送/なまほうそう (live broadcast), 収録/しゅうろく (recording), 配信/はいしん (streaming/distribution), 動画/どうが (video), チャンネル登録/ちゃんねるとうろく (channel subscription), 再生回数/さいせいかいすう (view count)
   - Curriculum 20: "Ngoại Giao Và Quan Hệ Quốc Tế" (Diplomacy and International Relations) — diplomatic vocabulary: 外交/がいこう (diplomacy), 大使館/たいしかん (embassy), 首脳会談/しゅのうかいだん (summit meeting), 条約/じょうやく (treaty), 制裁/せいさい (sanctions), 安全保障/あんぜんほしょう (security), 同盟/どうめい (alliance), 紛争/ふんそう (conflict/dispute), 和平/わへい (peace), 難民/なんみん (refugee), 国連/こくれん (United Nations), 決議/けつぎ (resolution), 主権/しゅけん (sovereignty), 領土/りょうど (territory), 貿易摩擦/ぼうえきまさつ (trade friction), 経済制裁/けいざいせいさい (economic sanctions), 多国間/たこくかん (multilateral), 覇権/はけん (hegemony)

2. THE Curriculum_Creator SHALL select vocabulary words that are high-frequency at the JLPT N3-N2 level, practical, and relevant to Vietnamese adults working in or engaging deeply with Japanese society.
3. THE Curriculum_Creator SHALL ensure no two curriculums have overlapping vocabulary lists (vocabList arrays must be unique across all 20 curriculums).
4. THE Curriculum_Creator SHALL ensure no vocabulary overlaps with the 20 beginner or 20 preintermediate vi-ja curriculums.
5. WHEN creating reading passages, THE Curriculum_Creator SHALL use Japanese sentences of 15-30 words, incorporating kanji with selective furigana (only for N2+ kanji), and scenarios appropriate for adults engaging with professional, intellectual, and cultural topics in Japan.


### Requirement 3: Intermediate Content Design

**User Story:** As a content quality owner, I want intermediate-level content designed for adults who can handle complex Japanese with kanji, so that learners are appropriately challenged while still receiving Vietnamese support for instructions.

#### Acceptance Criteria

1. WHEN learner-facing content is created for introAudio scripts at intermediate level, THE scripts SHALL use Vietnamese as the primary language, introducing each Japanese word with: the Japanese word (kanji + furigana for N2+ kanji only), Vietnamese meaning, part of speech, an example sentence in Japanese (15-25 words with natural kanji usage), Vietnamese translation of the example, and contextual usage notes including formality level.
2. WHEN reading passages are created for intermediate curriculums, THE passages SHALL be written in Japanese using kanji at JLPT N3 level freely (no furigana) with selective furigana for N2+ kanji. Passages SHALL be 250-400 characters and feature scenarios such as business discussions, cultural analysis, personal development reflections, and social commentary.
3. WHEN reading passages are created for upper-intermediate curriculums, THE passages SHALL be written in Japanese using kanji at JLPT N3-N2 level freely with selective furigana only for rare or specialized kanji. Passages SHALL be 350-500 characters and feature complex scenarios such as philosophical discussions, political analysis, scientific explanations, and literary criticism.
4. WHEN writingSentence prompts are created, THE prompts SHALL provide Vietnamese instructions, a complete Japanese example sentence (with selective furigana and Vietnamese translation), and a substitution pattern requiring the learner to use the target vocabulary word in a new, contextually appropriate sentence.
5. WHEN writingParagraph prompts are created, THE prompts SHALL require the learner to write 4-6 Japanese sentences using multiple vocabulary words from the curriculum, with Vietnamese instructions and guiding questions that demand analytical or argumentative responses.
6. THE introAudio scripts SHALL provide furigana readings only for N2+ kanji vocabulary, assuming learners can read N3 and below independently.
7. ALL user-facing text for intermediate curriculums (titles, descriptions, previews, introAudio, writing prompts) SHALL be bilingual: Vietnamese for instructions/marketing, Japanese for reading passages and example sentences.
8. WHEN an upper-intermediate curriculum is created, THE user-facing text MAY be bilingual (Vietnamese + Japanese) or use Vietnamese for marketing with Japanese for content, per platform policy.

### Requirement 4: Activity Structure for Intermediate Curriculums

**User Story:** As a platform owner, I want intermediate curriculums to include vocabLevel3 and writingParagraph to push learners toward greater fluency and production.

#### Acceptance Criteria

1. WHEN an intermediate curriculum is created, THE 5 sessions SHALL follow this structure:
   - Session 1 (Learning): introAudio (welcome + topic intro), introAudio (teach words group 1 with kanji, selective furigana, Vietnamese meaning, example sentences), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), vocabLevel2 (group 1), introAudio (grammar/usage notes), reading (passage using group 1 words, 250-400 chars), speakReading, readAlong, writingSentence (3 items using group 1 words)
   - Session 2 (Learning): introAudio (recap group 1 + intro), introAudio (teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), vocabLevel2 (group 2), introAudio (grammar/usage notes), reading (passage using group 2 words, 250-400 chars), speakReading, readAlong, writingSentence (3 items using group 2 words)
   - Session 3 (Learning): introAudio (recap groups 1-2 + intro), introAudio (teach words group 3), viewFlashcards (group 3), speakFlashcards (group 3), vocabLevel1 (group 3), vocabLevel2 (group 3), introAudio (grammar/usage notes), reading (passage using group 3 words, 250-400 chars), speakReading, readAlong, writingSentence (3 items using group 3 words)
   - Session 4 (Review): introAudio (review intro), viewFlashcards (all 18 words), speakFlashcards (all 18 words), vocabLevel1 (all 18 words), vocabLevel2 (all 18 words), vocabLevel3 (all 18 words), writingSentence (4-5 items mixing all groups)
   - Session 5 (Final Reading): introAudio (full reading intro), reading (full article using all 18 words, 600-900 chars), speakReading, readAlong, writingParagraph (using 6+ vocabulary words), introAudio (farewell with vocab review)

2. THE intermediate curriculum SHALL include vocabLevel3 in the review session (Session 4) only.
3. THE intermediate curriculum SHALL include writingParagraph in the final reading session (Session 5) only.

### Requirement 5: Activity Structure for Upper-Intermediate Curriculums

**User Story:** As a platform owner, I want upper-intermediate curriculums to challenge learners with longer passages, more complex writing tasks, and reduced scaffolding, so that learners build toward near-native reading and writing ability.

#### Acceptance Criteria

1. WHEN an upper-intermediate curriculum is created, THE 5 sessions SHALL follow this structure:
   - Session 1 (Learning): introAudio (welcome + topic intro), introAudio (teach words group 1 with kanji, minimal furigana, Vietnamese meaning, example sentences), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), vocabLevel2 (group 1), introAudio (grammar/usage notes), reading (passage using group 1 words, 350-500 chars), speakReading, readAlong, writingSentence (3 items using group 1 words)
   - Session 2 (Learning): introAudio (recap group 1 + intro), introAudio (teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), vocabLevel2 (group 2), introAudio (grammar/usage notes), reading (passage using group 2 words, 350-500 chars), speakReading, readAlong, writingSentence (3 items using group 2 words)
   - Session 3 (Learning): introAudio (recap groups 1-2 + intro), introAudio (teach words group 3), viewFlashcards (group 3), speakFlashcards (group 3), vocabLevel1 (group 3), vocabLevel2 (group 3), introAudio (grammar/usage notes), reading (passage using group 3 words, 350-500 chars), speakReading, readAlong, writingSentence (3 items using group 3 words)
   - Session 4 (Review): introAudio (review intro), viewFlashcards (all 18 words), speakFlashcards (all 18 words), vocabLevel1 (all 18 words), vocabLevel2 (all 18 words), vocabLevel3 (all 18 words), writingSentence (4-5 items mixing all groups)
   - Session 5 (Final Reading): introAudio (full reading intro), reading (full article using all 18 words, 800-1200 chars), speakReading, readAlong, writingParagraph (using 6+ vocabulary words, analytical/argumentative), introAudio (farewell with vocab review)

2. THE upper-intermediate curriculum SHALL include vocabLevel3 in the review session (Session 4) only.
3. THE upper-intermediate curriculum SHALL include writingParagraph in the final reading session (Session 5) only.
4. THE writingParagraph prompts for upper-intermediate curriculums SHALL require analytical or argumentative responses — not simple summaries or descriptions.

### Requirement 6: Vietnamese Marketing Copy

**User Story:** As a content quality owner, I want all marketing text written in Vietnamese with persuasive copy standards, so that Vietnamese learners feel motivated to advance their Japanese to professional and intellectual levels.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL write curriculum descriptions as Persuasive_Copy following the 5-beat structure, addressing adult learner aspirations: professional advancement in Japanese companies, intellectual engagement with Japanese society, cultural fluency beyond tourist-level, and personal transformation through mastering complex Japanese.
2. THE Curriculum_Creator SHALL write curriculum previews (~150 words) as Persuasive_Copy with vivid hooks about the learner's Japanese journey at this advanced stage, vocabulary word listing (Japanese + furigana where applicable + Vietnamese meaning), and what the learner will be able to do after completing the curriculum.
3. THE Curriculum_Creator SHALL write all titles, descriptions, and preview text in Vietnamese for intermediate curriculums (as required for intermediate vi-ja curriculums where userLanguage="vi").
4. WHEN an upper-intermediate curriculum is created, THE marketing text (title, description, preview) MAY be in Vietnamese or bilingual, per platform policy.
5. THE Tone_Assigner SHALL assign one of the 6 Tone_Palette types to every curriculum description headline.
6. WHILE assigning tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Tone_Palette type.
7. THE Tone_Assigner SHALL ensure no single Tone_Palette type exceeds 30% of the 20 curriculum descriptions (max 6 uses per tone).
8. THE Persuasive_Copy SHALL emphasize the practical value of intermediate/upper-intermediate Japanese for Vietnamese adults: leading business negotiations, understanding Japanese media and politics, engaging in intellectual discussions, navigating complex social situations, and building deep cross-cultural relationships.

### Requirement 7: introAudio Quality

**User Story:** As a content quality owner, I want introAudio scripts that effectively teach sophisticated Japanese vocabulary with nuanced usage guidance to Vietnamese speakers, so that learners build professional-level communication skills.

#### Acceptance Criteria

1. WHEN a welcome introAudio is created, THE script (600-900 words) SHALL greet the learner warmly in Vietnamese, introduce the topic with a motivating hook relevant to their professional/intellectual growth, list all 6 vocabulary words for the session, and teach each word with: the Japanese word (kanji + selective furigana), Vietnamese meaning, part of speech, a contextual example sentence in Japanese with Vietnamese translation, formality level notes (casual/polite/keigo), and usage nuances or common collocations.
2. WHEN a vocabulary-teaching introAudio is created, THE script SHALL explain how each word is used in real Japanese contexts, noting register differences, common mistakes by Vietnamese speakers, and connections to words learned in previous levels.
3. WHEN a session recap introAudio is created (sessions 2-3), THE script SHALL briefly recap previous session words before introducing new ones — using phrases like "前回学んだ言葉を覚えていますか？" alongside Vietnamese explanations.
4. WHEN a grammar/usage introAudio is created, THE script SHALL explain 1-2 grammar patterns relevant to the session's vocabulary, with Vietnamese explanations and Japanese example sentences demonstrating formal and informal usage.
5. WHEN a farewell introAudio is created, THE script (400-600 words) SHALL review 5-6 key vocabulary words with definitions and fresh Japanese example sentences (with Vietnamese translation), summarize the learning journey, connect the vocabulary to real-world application, and close with a warm personal sign-off.
6. THE Curriculum_Creator SHALL individually craft every introAudio script for its specific curriculum topic, without using template functions or string interpolation.
7. THE Tone_Assigner SHALL assign one of the 5 Farewell_Palette registers to every farewell introAudio.
8. WHILE assigning farewell tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Farewell_Palette register.

### Requirement 8: Pricing

**User Story:** As a platform owner, I want intermediate/upper-intermediate curriculums priced at the standard rate, so that pricing is consistent with the rest of the catalog.

#### Acceptance Criteria

1. WHEN an intermediate or upper-intermediate curriculum (5 sessions) is created, THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 49`.
2. THE Curriculum_Creator SHALL set the price after the curriculum is successfully created and added to its series.

### Requirement 9: Collection and Series Organization

**User Story:** As a platform owner, I want the 20 intermediate/upper-intermediate curriculums organized into a dedicated collection with thematic series, so that learners can browse content by interest area and find a clear progression from the preintermediate collection.

#### Acceptance Criteria

1. THE Collection_Organizer SHALL create 1 NEW collection titled "Tiếng Nhật Nâng Cao" (Advanced Japanese) with a neutral, informative Vietnamese description explaining this is a collection of Japanese curriculums for Vietnamese adults at intermediate and upper-intermediate levels, covering business, culture, society, science, and personal development topics.
2. THE Collection_Organizer SHALL organize the 20 curriculums into 5 series of 4 curriculums each:
   - Series 1: "Kinh Doanh Và Tài Chính" (Business and Finance) — containing Curriculums 1, 3, 8, 15 (business negotiation, personal finance, real estate/investment, entrepreneurship). Description ≤255 chars using a Tone_Palette type.
   - Series 2: "Truyền Thông Và Giải Trí" (Media and Entertainment) — containing Curriculums 2, 6, 9, 19 (media/advertising, manga/anime culture, world cuisine, entertainment/TV). Description ≤255 chars using a different Tone_Palette type.
   - Series 3: "Xã Hội Và Con Người" (Society and People) — containing Curriculums 4, 5, 7, 12 (modern marriage/family, self-development, mental health, politics/society). Description ≤255 chars using a different Tone_Palette type.
   - Series 4: "Khoa Học Và Tương Lai" (Science and the Future) — containing Curriculums 10, 13, 16, 18 (transportation/urban, science/discovery, nature/ecology, AI/future). Description ≤255 chars using a different Tone_Palette type.
   - Series 5: "Văn Hóa Và Tư Tưởng" (Culture and Thought) — containing Curriculums 11, 14, 17, 20 (Japanese philosophy, literature, crime/justice, diplomacy/international relations). Description ≤255 chars using a different Tone_Palette type.
3. THE Collection_Organizer SHALL wire each series to the collection via `curriculum-collection/addSeriesToCollection`.
4. THE Collection_Organizer SHALL set display orders for all 5 series within the collection via `curriculum-series/setDisplayOrder`.
5. THE Collection_Organizer SHALL set display orders for all curriculums within each series via `curriculum/setDisplayOrder`.
6. THE Collection_Organizer SHALL ensure all curriculums within each series share `language: "ja"` and `userLanguage: "vi"`.
7. WHILE assigning series description tones, THE Tone_Assigner SHALL ensure all 5 series use different Tone_Palette types.
8. WITHIN each series, THE maximum difficulty level gap SHALL be 1 level (intermediate + upper-intermediate is acceptable).

### Requirement 10: Activity Schema Compliance

**User Story:** As a platform developer, I want every activity to comply with the platform's content schema, so that the content pipeline processes Japanese curriculums without errors.

#### Acceptance Criteria

1. Each Activity SHALL include `activityType`, `title`, `description`, and `data` fields.
2. THE `activityType` field SHALL use one of the valid values: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3, reading, speakReading, readAlong, writingSentence, writingParagraph.
3. THE `vocabList` field SHALL be an array of lowercase strings (Japanese words in their standard written form including kanji), using the field name `vocabList` (never `words`).
4. WHEN viewFlashcards and speakFlashcards appear in the same session, THE two activities SHALL have identical `vocabList` arrays.
5. All content data SHALL be inside the `data` object, not inline on the activity object.
6. WHEN a writingSentence activity is created, THE activity SHALL have `data.vocabList`, `data.items` (non-empty array), and each item SHALL have `prompt` (Vietnamese instructions with Japanese example sentence, selective furigana, Vietnamese translation, and substitution pattern) and `targetVocab` fields.
7. WHEN a writingParagraph activity is created, THE activity SHALL have `data.vocabList`, `data.instructions` (Vietnamese), and `data.prompts` (array of at least 2 guiding questions in Vietnamese requiring analytical/argumentative responses).
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
8. THE Content_Validator SHALL verify writingParagraph data structures (vocabList, instructions, prompts array with ≥2 items).
9. THE Content_Validator SHALL verify that no Strip_Keys appear anywhere in the content JSON.
10. THE Content_Validator SHALL verify that all curriculums contain vocabLevel3 only in Session 4 and writingParagraph only in Session 5.
11. IF any validation check fails, THEN THE Content_Validator SHALL abort the upload and print the specific rule violation.

### Requirement 12: Script Architecture and Workflow

**User Story:** As a developer, I want a clear, repeatable workflow for creating 20 intermediate/upper-intermediate curriculums, so that the process is manageable and traceable.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce one standalone Python script per curriculum (20 scripts total).
2. THE Curriculum_Creator SHALL produce one orchestrator script that creates the collection, 5 series, wires them together, and sets display orders.
3. THE Curriculum_Creator SHALL organize scripts into a directory `vi-ja-intermediate-curriculums/`.
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
3. THE curriculum titles SHALL NOT include difficulty level indicators (e.g., "intermediate", "upper-intermediate", "trung cấp", "中級").
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

1. THE Curriculum_Creator SHALL execute creation in this order: (1) create collection and 5 series via orchestrator, (2) create intermediate curriculums (10 scripts), (3) create upper-intermediate curriculums (10 scripts).
2. WHEN each curriculum is created, THE Curriculum_Creator SHALL immediately add it to the appropriate series, set its display order, and set its price.
3. WHEN all 20 curriculums are created, THE Curriculum_Creator SHALL verify the complete set by querying the database to confirm all curriculums exist with correct display orders, language values, prices, and non-empty content.
4. IF verification reveals missing or malformed curriculums, THEN THE Curriculum_Creator SHALL recreate the affected curriculums before finalizing documentation.
