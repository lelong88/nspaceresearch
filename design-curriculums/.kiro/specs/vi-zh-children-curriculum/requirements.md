# Requirements Document

## Introduction

Create 22 Chinese-learning curriculums specifically designed for Vietnamese-speaking children aged 6-10. Language pair: userLanguage="vi", language="zh". Difficulty levels: beginner (14 curriculums — 6 mini + 8 short) and preintermediate (8 curriculums).

This is the first vi-zh children's curriculum set. The existing vi-en children's catalog has 20 curriculums across 2 series, but there is no Chinese-learning content for children. These 22 curriculums fill a critical gap by providing age-appropriate, child-friendly Chinese learning experiences with topics that resonate with Vietnamese children — including both universal childhood topics and China-specific cultural content (Chinese food, festivals, zodiac animals, basic characters).

### What This Spec Covers

- 22 individually crafted curriculums for Vietnamese children aged 6-10 learning Chinese
- Child-friendly topics including China-specific cultural content
- Age-appropriate persuasive copy (written for parents, since parents purchase)
- NEW collection and series organization for the vi-zh children's curriculum line
- Pricing per the beginner/preintermediate guidelines
- Chinese-specific vocabulary (characters + pinyin) with Vietnamese explanations
- Creation workflow, validation, and documentation

### What This Spec Does NOT Cover

- Changes to existing vi-en children's curriculums
- Children's curriculums for other language pairs
- Content generation pipeline (audio, illustrations) — curriculums are created private
- Advanced or intermediate difficulty levels (not appropriate for ages 6-10)
- Existing vi-zh adult curriculums (fiction novels, movies, songs)

## Glossary

- **Children_Curriculum**: A curriculum designed for Vietnamese children aged 6-10 learning Chinese. Uses simpler vocabulary (3-5 words for mini, 8-10 words for short, 10-12 for preintermediate), shorter reading passages, playful tone, and age-appropriate topics. All user-facing marketing text targets parents (the purchasers). Vocabulary items are Chinese characters with pinyin.
- **Curriculum_Creator**: The system of standalone Python scripts that generate curriculum JSON content and upload it via the REST API.
- **Content_Validator**: Validation logic that checks curriculum JSON against the Content Corruption Detection Rules before upload.
- **Collection_Organizer**: The orchestrator script that creates collections, series, wires them together, and sets display orders via the REST API.
- **Tone_Assigner**: The logic that assigns description tones and farewell tones to each curriculum and series, ensuring variety constraints are met.
- **Language_Pair**: userLanguage="vi", language="zh" — Vietnamese children learning Chinese.
- **Parent_Copy**: Persuasive marketing text written for Vietnamese parents who are purchasing the curriculum for their child. Uses the standard 5-beat persuasive copy structure but addresses parental aspirations and concerns about their child's Chinese education.
- **Child_Content**: Learner-facing content (introAudio scripts, reading passages, writing prompts) written in a warm, playful, encouraging tone appropriate for children aged 6-10. Uses simple Vietnamese explanations and child-friendly Chinese vocabulary (characters + pinyin).
- **Persuasive_Copy**: The required writing style for marketing text — emotional sales copy with bold headline, concrete examples, vivid metaphor, transformation promise, and personal growth tie-in.
- **Tone_Palette**: The 6 rhetorical opener types: provocative_question, bold_declaration, vivid_scenario, empathetic_observation, surprising_fact, metaphor_led.
- **Farewell_Palette**: The 5 emotional registers for farewell introAudio scripts: introspective_guide, warm_accountability, team_building_energy, quiet_awe, practical_momentum.
- **Strip_Keys**: Auto-generated platform keys (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId) that must never be included in new curriculum content.
- **Mini_Curriculum**: A single-session curriculum with 3-5 vocabulary words, priced at 9 credits (beginner).
- **Short_Curriculum**: A 4-session curriculum with 8-10 vocabulary words, priced at 19 credits (beginner) or 49 credits (preintermediate).
- **Pinyin**: The romanization system for Chinese characters. Used in vocabList fields as lowercase strings (e.g., "nǐ hǎo" becomes "ni hao" in vocabList since the platform requires lowercase ASCII strings).
- **Chinese_Character**: The logographic writing system used in Chinese. Each vocabulary word is taught as character + pinyin + Vietnamese meaning.

## Requirements

### Requirement 1: Children's Curriculum Format and Structure

**User Story:** As a platform owner, I want 22 Chinese-learning curriculums designed specifically for Vietnamese children aged 6-10, so that young learners have age-appropriate content that makes learning Chinese fun and engaging.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL produce exactly 22 Children_Curriculums for the vi-zh Language_Pair.
2. THE Curriculum_Creator SHALL create 6 beginner mini curriculums, 8 beginner short curriculums, and 8 preintermediate short curriculums.
3. WHEN a beginner mini Children_Curriculum is created, THE curriculum SHALL contain exactly 1 learning session with 3-5 vocabulary words.
4. WHEN a beginner short Children_Curriculum is created, THE curriculum SHALL contain 4 learning sessions with 8-10 vocabulary words divided into 2 groups.
5. WHEN a preintermediate Children_Curriculum is created, THE curriculum SHALL contain 4 learning sessions with 10-12 vocabulary words divided into 2-3 groups.
6. THE Children_Curriculum SHALL include `contentTypeTags: []` at the top level of the content JSON (topic-based).
7. THE Children_Curriculum SHALL never include Strip_Keys in the content JSON.
8. THE Curriculum_Creator SHALL set `language: "zh"` and `userLanguage: "vi"` as top-level body parameters in the `curriculum/create` API call.

### Requirement 2: Topic Plan for 22 Children's Curriculums

**User Story:** As a platform owner, I want child-friendly topics that resonate with Vietnamese children aged 6-10 learning Chinese, so that young learners are excited to study Chinese through familiar, fun subjects and China-specific cultural content.

#### Acceptance Criteria

1. THE 22 Children_Curriculums SHALL cover the following topics, each individually crafted:

   **Beginner Mini (3-5 words, 1 session, 9 credits) — 6 curriculums:**
   - Curriculum 1: "Thế Giới Màu Sắc" (World of Colors) — colors in Chinese: 红/hóng (red), 蓝/lán (blue), 绿/lǜ (green), 黄/huáng (yellow), 白/bái (white). vocabList: ["hong", "lan", "lv", "huang", "bai"]
   - Curriculum 2: "Đếm Từ 1 Đến 10" (Counting 1 to 10) — numbers: 一/yī, 二/èr, 三/sān, 四/sì, 五/wǔ. vocabList: ["yi", "er", "san", "si", "wu"]
   - Curriculum 3: "Gia Đình Yêu Thương" (Loving Family) — family members: 妈妈/māma (mom), 爸爸/bàba (dad), 哥哥/gēge (older brother), 姐姐/jiějie (older sister), 弟弟/dìdi (younger brother). vocabList: ["mama", "baba", "gege", "jiejie", "didi"]
   - Curriculum 4: "Trái Cây Ngon Lành" (Delicious Fruits) — fruits: 苹果/píngguǒ (apple), 香蕉/xiāngjiāo (banana), 西瓜/xīguā (watermelon), 葡萄/pútao (grape), 橙子/chéngzi (orange). vocabList: ["pingguo", "xiangjiao", "xigua", "putao", "chengzi"]
   - Curriculum 5: "Bạn Thú Cưng" (Pet Friends) — common pets: 小狗/xiǎogǒu (puppy), 猫/māo (cat), 鱼/yú (fish), 鸟/niǎo (bird), 兔子/tùzi (rabbit). vocabList: ["xiao gou", "mao", "yu", "niao", "tuzi"]
   - Curriculum 6: "Chào Hỏi Vui Vẻ" (Happy Greetings) — greetings and manners: 你好/nǐhǎo (hello), 谢谢/xièxie (thank you), 再见/zàijiàn (goodbye), 对不起/duìbuqǐ (sorry), 没关系/méiguānxi (it's okay). vocabList: ["ni hao", "xie xie", "zai jian", "dui bu qi", "mei guan xi"]

   **Beginner Short (8-10 words, 4 sessions, 19 credits) — 8 curriculums:**
   - Curriculum 7: "Một Ngày Ở Trường" (A Day at School) — school vocabulary: 老师/lǎoshī (teacher), 同学/tóngxué (classmate), 书/shū (book), 笔/bǐ (pen), 桌子/zhuōzi (desk), 上课/shàngkè (attend class), 下课/xiàkè (finish class), 作业/zuòyè (homework), 教室/jiàoshì (classroom), 书包/shūbāo (backpack). vocabList: ["laoshi", "tongxue", "shu", "bi", "zhuozi", "shang ke", "xia ke", "zuoye", "jiaoshi", "shubao"]
   - Curriculum 8: "Đồ Ăn Trung Hoa" (Chinese Food) — food vocabulary: 米饭/mǐfàn (rice), 面条/miàntiáo (noodles), 饺子/jiǎozi (dumplings), 包子/bāozi (steamed buns), 汤/tāng (soup), 茶/chá (tea), 筷子/kuàizi (chopsticks), 好吃/hǎochī (delicious), 饿/è (hungry), 饱/bǎo (full). vocabList: ["mifan", "miantiao", "jiaozi", "baozi", "tang", "cha", "kuaizi", "hao chi", "e", "bao"]
   - Curriculum 9: "Sân Chơi Vui Nhộn" (Fun Playground) — playground/action words: 跑/pǎo (run), 跳/tiào (jump), 玩/wán (play), 笑/xiào (laugh), 唱歌/chànggē (sing), 画画/huàhuà (draw), 朋友/péngyou (friend), 开心/kāixīn (happy), 一起/yìqǐ (together), 游戏/yóuxì (game). vocabList: ["pao", "tiao", "wan", "xiao", "chang ge", "hua hua", "pengyou", "kai xin", "yi qi", "you xi"]
   - Curriculum 10: "Cơ Thể Của Em" (My Body) — body parts: 头/tóu (head), 手/shǒu (hand), 脚/jiǎo (foot), 眼睛/yǎnjing (eyes), 耳朵/ěrduo (ears), 嘴巴/zuǐba (mouth), 鼻子/bízi (nose), 肚子/dùzi (belly), 头发/tóufa (hair), 牙齿/yáchǐ (teeth). vocabList: ["tou", "shou", "jiao", "yanjing", "erduo", "zuiba", "bizi", "duzi", "toufa", "yachi"]
   - Curriculum 11: "Thời Tiết Hôm Nay" (Today's Weather) — weather: 太阳/tàiyáng (sun), 下雨/xiàyǔ (rain), 刮风/guāfēng (windy), 冷/lěng (cold), 热/rè (hot), 雪/xuě (snow), 云/yún (cloud), 天气/tiānqì (weather), 暖和/nuǎnhuo (warm), 凉快/liángkuai (cool). vocabList: ["taiyang", "xia yu", "gua feng", "leng", "re", "xue", "yun", "tianqi", "nuanhuo", "liangkuai"]
   - Curriculum 12: "Tủ Quần Áo" (My Wardrobe) — clothing: 衣服/yīfu (clothes), 裤子/kùzi (pants), 裙子/qúnzi (skirt/dress), 鞋子/xiézi (shoes), 帽子/màozi (hat), 袜子/wàzi (socks), 外套/wàitào (jacket), 穿/chuān (wear), 漂亮/piàoliang (pretty), 新/xīn (new). vocabList: ["yifu", "kuzi", "qunzi", "xiezi", "maozi", "wazi", "waitao", "chuan", "piaoliang", "xin"]
   - Curriculum 13: "Xe Cộ Quanh Em" (Vehicles Around Me) — vehicles: 汽车/qìchē (car), 公共汽车/gōnggòng qìchē (bus), 火车/huǒchē (train), 飞机/fēijī (airplane), 自行车/zìxíngchē (bicycle), 小船/xiǎochuán (small boat), 地铁/dìtiě (subway), 快/kuài (fast), 慢/màn (slow), 坐/zuò (ride/sit). vocabList: ["qiche", "gonggong qiche", "huoche", "feiji", "zixingche", "xiao chuan", "ditie", "kuai", "man", "zuo"]
   - Curriculum 14: "Con Vật Đáng Yêu" (Adorable Animals) — zoo animals: 大象/dàxiàng (elephant), 熊猫/xióngmāo (panda), 老虎/lǎohǔ (tiger), 长颈鹿/chángjǐnglù (giraffe), 企鹅/qǐ'é (penguin), 狮子/shīzi (lion), 河马/hémǎ (hippo), 鳄鱼/èyú (crocodile), 袋鼠/dàishǔ (kangaroo), 孔雀/kǒngquè (peacock). vocabList: ["daxiang", "xiongmao", "laohu", "changjinglu", "qi e", "shizi", "hema", "eyu", "daishu", "kongque"]

   **Preintermediate Short (10-12 words, 4 sessions, 49 credits) — 8 curriculums:**
   - Curriculum 15: "Tết Nguyên Đán" (Lunar New Year) — festival vocabulary: 春节/Chūnjié (Spring Festival), 红包/hóngbāo (red envelope), 鞭炮/biānpào (firecrackers), 灯笼/dēnglong (lantern), 拜年/bàinián (New Year greetings), 团圆/tuányuán (reunion), 年夜饭/niányèfàn (New Year's Eve dinner), 舞龙/wǔlóng (dragon dance), 福/fú (fortune/blessing), 春联/chūnlián (Spring couplets), 压岁钱/yāsuìqián (lucky money), 放假/fàngjià (holiday). vocabList: ["chun jie", "hong bao", "bian pao", "deng long", "bai nian", "tuan yuan", "nian ye fan", "wu long", "fu", "chun lian", "ya sui qian", "fang jia"]
   - Curriculum 16: "Mười Hai Con Giáp" (The 12 Zodiac Animals) — zodiac: 老鼠/lǎoshǔ (rat), 牛/niú (ox), 虎/hǔ (tiger), 兔/tù (rabbit), 龙/lóng (dragon), 蛇/shé (snake), 马/mǎ (horse), 羊/yáng (goat), 猴/hóu (monkey), 鸡/jī (rooster), 狗/gǒu (dog), 猪/zhū (pig). vocabList: ["lao shu", "niu", "hu", "tu", "long", "she", "ma", "yang", "hou", "ji", "gou", "zhu"]
   - Curriculum 17: "Khám Phá Thiên Nhiên" (Exploring Nature) — nature: 山/shān (mountain), 河/hé (river), 大树/dàshù (big tree), 花/huā (flower), 草/cǎo (grass), 天空/tiānkōng (sky), 星星/xīngxing (stars), 月亮/yuèliang (moon), 海/hǎi (sea), 风/fēng (wind), 叶子/yèzi (leaf), 种子/zhǒngzi (seed). vocabList: ["shan", "he", "da shu", "hua", "cao", "tiankong", "xingxing", "yueliang", "hai", "feng", "yezi", "zhongzi"]
   - Curriculum 18: "Đi Chợ Cùng Mẹ" (Shopping with Mom) — market/shopping: 买/mǎi (buy), 卖/mài (sell), 钱/qián (money), 多少钱/duōshao qián (how much), 贵/guì (expensive), 便宜/piányi (cheap), 水果/shuǐguǒ (fruit), 蔬菜/shūcài (vegetables), 超市/chāoshì (supermarket), 付钱/fùqián (pay), 找钱/zhǎoqián (give change), 袋子/dàizi (bag). vocabList: ["mai3", "mai4", "qian", "duo shao qian", "gui", "pian yi", "shui guo", "shu cai", "chao shi", "fu qian", "zhao qian", "dai zi"]
   - Curriculum 19: "Bốn Mùa Trong Năm" (Four Seasons) — seasons and activities: 春天/chūntiān (spring), 夏天/xiàtiān (summer), 秋天/qiūtiān (autumn), 冬天/dōngtiān (winter), 游泳/yóuyǒng (swim), 滑雪/huáxuě (ski), 放风筝/fàng fēngzhēng (fly kite), 赏花/shǎnghuā (enjoy flowers), 落叶/luòyè (falling leaves), 堆雪人/duī xuěrén (build snowman), 暑假/shǔjià (summer vacation), 寒假/hánjià (winter vacation). vocabList: ["chun tian", "xia tian", "qiu tian", "dong tian", "you yong", "hua xue", "fang feng zheng", "shang hua", "luo ye", "dui xue ren", "shu jia", "han jia"]
   - Curriculum 20: "Sinh Hoạt Hàng Ngày" (Daily Routines) — daily activities: 起床/qǐchuáng (wake up), 刷牙/shuāyá (brush teeth), 洗脸/xǐliǎn (wash face), 吃早饭/chī zǎofàn (eat breakfast), 上学/shàngxué (go to school), 回家/huíjiā (go home), 做作业/zuò zuòyè (do homework), 洗澡/xǐzǎo (take bath), 睡觉/shuìjiào (sleep), 看书/kànshū (read book), 看电视/kàn diànshì (watch TV), 早上好/zǎoshang hǎo (good morning). vocabList: ["qi chuang", "shua ya", "xi lian", "chi zao fan", "shang xue", "hui jia", "zuo zuo ye", "xi zao", "shui jiao", "kan shu", "kan dian shi", "zao shang hao"]
   - Curriculum 21: "Lễ Hội Trung Thu" (Mid-Autumn Festival) — festival vocabulary: 中秋节/Zhōngqiūjié (Mid-Autumn Festival), 月饼/yuèbǐng (mooncake), 赏月/shǎngyuè (admire the moon), 嫦娥/Cháng'é (Chang'e), 玉兔/yùtù (Jade Rabbit), 家人/jiārén (family), 花灯/huādēng (decorative lantern), 猜谜/cāimí (riddles), 圆/yuán (round), 思念/sīniàn (miss someone), 故事/gùshi (story), 快乐/kuàilè (happy). vocabList: ["zhong qiu jie", "yue bing", "shang yue", "chang e", "yu tu", "jia ren", "hua deng", "cai mi", "yuan", "si nian", "gu shi", "kuai le"]
   - Curriculum 22: "Nét Bút Đầu Tiên" (First Brush Strokes) — Chinese characters basics: 笔画/bǐhuà (stroke), 横/héng (horizontal stroke), 竖/shù (vertical stroke), 撇/piě (left-falling stroke), 捺/nà (right-falling stroke), 点/diǎn (dot stroke), 写字/xiězì (write characters), 汉字/hànzì (Chinese characters), 练习/liànxí (practice), 本子/běnzi (notebook), 毛笔/máobǐ (calligraphy brush), 墨/mò (ink). vocabList: ["bi hua", "heng", "shu bi", "pie", "na", "dian", "xie zi", "han zi", "lian xi", "ben zi", "mao bi", "mo"]

2. THE Curriculum_Creator SHALL select vocabulary words that are concrete, high-frequency, and visually representable for children aged 6-10.
3. THE Curriculum_Creator SHALL ensure no two curriculums have overlapping vocabulary lists (vocabList arrays must be unique across all 22 curriculums).
4. WHEN creating reading passages for children, THE Curriculum_Creator SHALL use simple Chinese sentences (under 8 characters average for beginner, under 12 characters for preintermediate), present tense primarily, and vocabulary that a 6-10 year old Vietnamese child can relate to.
5. THE Curriculum_Creator SHALL use lowercase pinyin (without tone marks, spaces separating syllables for multi-syllable words) in vocabList fields, since the platform requires lowercase ASCII strings.

### Requirement 3: Age-Appropriate Content Design

**User Story:** As a content quality owner, I want all learner-facing content designed for children aged 6-10, so that young learners feel engaged, safe, and encouraged throughout the learning experience.

#### Acceptance Criteria

1. WHEN Child_Content is created for introAudio scripts, THE scripts SHALL use a warm, playful, encouraging tone — as if a friendly teacher is speaking to a child. Use simple Vietnamese sentences, enthusiastic language, and gentle encouragement. Each Chinese word SHALL be introduced with: the Chinese character, pinyin pronunciation, Vietnamese meaning, and a fun association or memory hook.
2. WHEN Child_Content is created for reading passages, THE passages SHALL be written in simple Chinese using only vocabulary from the curriculum's vocabList and basic connector words. Passages SHALL feature child-relatable scenarios: playing with friends, going to school, eating food, celebrating festivals, exploring nature. No abstract concepts, no adult themes.
3. WHEN Child_Content is created for writingSentence prompts, THE prompts SHALL provide maximum scaffolding: full Vietnamese instructions written simply for a child, a complete Chinese example sentence (with pinyin and Vietnamese translation) the child can closely imitate, and a clear word-substitution pattern requiring only 1 word change.
4. THE Children_Curriculum SHALL NOT include `writingParagraph` activities (too complex for ages 6-10).
5. THE Children_Curriculum SHALL NOT include `vocabLevel3` activities (to reduce cognitive load for young learners).
6. WHEN a beginner mini Children_Curriculum is created, THE curriculum SHALL NOT include `vocabLevel1` or `vocabLevel2` activities (mini format focuses on flashcards, reading, and speaking).
7. THE introAudio farewell scripts SHALL use an especially warm, celebratory tone — praising the child's effort, using phrases like "con giỏi lắm!" (you did great!), and encouraging them to practice Chinese with family or friends.

### Requirement 4: Activity Templates for Children's Curriculums

**User Story:** As a platform owner, I want activity sequences optimized for children's attention spans and learning patterns, so that young learners stay engaged throughout each session.

#### Acceptance Criteria

1. WHEN a beginner mini Children_Curriculum is created, THE session SHALL include activities in this order: introAudio (welcome + teach all words with playful context, pinyin pronunciation guide, and Vietnamese meaning), viewFlashcards, speakFlashcards, reading (short Chinese passage, 30-50 characters), speakReading, readAlong, introAudio (farewell with vocab review and praise).

2. WHEN a beginner short Children_Curriculum is created, THE 4 sessions SHALL follow this structure:
   - Session 1: introAudio (welcome + teach words group 1 with characters, pinyin, Vietnamese meaning), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), reading (short Chinese passage using group 1 words, 50-70 characters), readAlong, introAudio (session wrap-up)
   - Session 2: introAudio (recap group 1 + teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), reading (short Chinese passage using group 2 words, 50-70 characters), readAlong, introAudio (session wrap-up)
   - Session 3 (Review): introAudio (review intro), viewFlashcards (all words), speakFlashcards (all words), vocabLevel1 (all words), vocabLevel2 (all words), writingSentence (3-4 items), introAudio (review wrap-up)
   - Session 4 (Final): introAudio (final reading intro), reading (combined Chinese passage using all words, 80-110 characters), speakReading, readAlong, writingSentence (2-3 items), introAudio (farewell with full vocab review and celebration)

3. WHEN a preintermediate short Children_Curriculum is created, THE 4 sessions SHALL follow this structure:
   - Session 1: introAudio (welcome + teach words group 1 with characters, pinyin, Vietnamese meaning), viewFlashcards (group 1), speakFlashcards (group 1), vocabLevel1 (group 1), vocabLevel2 (group 1), reading (Chinese passage using group 1 words, 70-90 characters), speakReading, readAlong, introAudio (session wrap-up)
   - Session 2: introAudio (recap group 1 + teach words group 2), viewFlashcards (group 2), speakFlashcards (group 2), vocabLevel1 (group 2), vocabLevel2 (group 2), reading (Chinese passage using group 2 words, 70-90 characters), speakReading, readAlong, introAudio (session wrap-up)
   - Session 3 (Review): introAudio (review intro), viewFlashcards (all words), speakFlashcards (all words), vocabLevel1 (all words), vocabLevel2 (all words), writingSentence (4-5 items), introAudio (review wrap-up)
   - Session 4 (Final): introAudio (final reading intro), reading (combined Chinese passage using all words, 120-160 characters), speakReading, readAlong, writingSentence (3-4 items), introAudio (farewell with full vocab review and celebration)

### Requirement 5: Parent-Facing Marketing Copy

**User Story:** As a content quality owner, I want all marketing text (title, description, preview) to speak to Vietnamese parents, so that parents understand the value and feel confident purchasing these curriculums for their children.

#### Acceptance Criteria

1. THE Curriculum_Creator SHALL write curriculum descriptions as Parent_Copy following the Persuasive_Copy 5-beat structure, but addressing parental aspirations: their child's future, early Chinese language advantage, confidence building, and fun learning. The copy SHALL emphasize the growing importance of Chinese in Vietnam and Southeast Asia.
2. THE Curriculum_Creator SHALL write curriculum previews (~100-150 words) as Parent_Copy with vivid hooks about the child's Chinese learning journey, vocabulary word listing (characters + pinyin + Vietnamese meaning), and what the child will be able to say/read in Chinese after completing the curriculum.
3. THE Curriculum_Creator SHALL write all titles, descriptions, and preview text in Vietnamese (as required for beginner/preintermediate curriculums where userLanguage="vi").
4. THE Tone_Assigner SHALL assign one of the 6 Tone_Palette types to every curriculum description headline.
5. WHILE assigning tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Tone_Palette type.
6. THE Tone_Assigner SHALL ensure no single Tone_Palette type exceeds 30% of the 22 curriculum descriptions (max 6-7 uses per tone).
7. THE Parent_Copy SHALL NOT use fear-based marketing or shame-based language about children's abilities. The tone SHALL be aspirational, warm, and encouraging — celebrating the child's potential and the cultural richness of learning Chinese.

### Requirement 6: introAudio Quality for Children

**User Story:** As a content quality owner, I want introAudio scripts crafted specifically for young learners of Chinese, so that children feel welcomed, engaged, and celebrated throughout the learning experience.

#### Acceptance Criteria

1. WHEN a welcome introAudio is created for a mini curriculum, THE script (200-350 words) SHALL greet the child warmly in Vietnamese, introduce the topic with a fun hook (e.g., "Hôm nay chúng ta sẽ học đếm bằng tiếng Trung nè!"), list all vocabulary words, and teach each word with: the Chinese character, pinyin pronunciation (with tone guidance in simple Vietnamese), Vietnamese meaning, a simple example sentence in Chinese, and a fun fact or memory association.
2. WHEN a welcome introAudio is created for a short/preintermediate curriculum, THE script (300-500 words) SHALL follow the same pattern as criterion 1 but with more words and slightly more context per word, including cultural context where relevant (e.g., explaining why Chinese people give red envelopes).
3. WHEN a session recap introAudio is created (sessions 2+), THE script SHALL briefly and playfully recap previous Chinese words before introducing new ones — using phrases like "Các bạn còn nhớ không? Hôm trước chúng ta học..." (Do you remember? Last time we learned...).
4. WHEN a farewell introAudio is created, THE script (200-400 words) SHALL review key vocabulary words with fresh child-friendly Chinese example sentences (with pinyin and Vietnamese translation), celebrate the child's achievement with enthusiastic praise, and encourage practicing Chinese with family or friends.
5. THE introAudio scripts SHALL be primarily in Vietnamese with Chinese words/phrases introduced using characters + pinyin + Vietnamese meaning format.
6. THE Curriculum_Creator SHALL individually craft every introAudio script for its specific curriculum topic, without using template functions or string interpolation.
7. THE Tone_Assigner SHALL assign one of the 5 Farewell_Palette registers to every farewell introAudio, adapted for a child audience (e.g., "warm accountability" becomes gentle encouragement to practice Chinese characters, "quiet awe" becomes wonder at the beauty of Chinese writing).
8. WHILE assigning farewell tones within a series, THE Tone_Assigner SHALL ensure no two adjacent curriculums use the same Farewell_Palette register.

### Requirement 7: Pricing

**User Story:** As a platform owner, I want children's curriculums priced according to the standard pricing guidelines, so that pricing is consistent with the rest of the catalog.

#### Acceptance Criteria

1. WHEN a beginner mini Children_Curriculum (1 session) is created, THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 9`.
2. WHEN a beginner short Children_Curriculum (4 sessions) is created, THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 19`.
3. WHEN a preintermediate short Children_Curriculum (4 sessions) is created, THE Curriculum_Creator SHALL call `curriculum/setPrice` with `price: 49`.
4. THE Curriculum_Creator SHALL set the price after the curriculum is successfully created and added to its series.

### Requirement 8: Collection and Series Organization

**User Story:** As a platform owner, I want the 22 children's curriculums organized into a dedicated vi-zh collection and series, so that parents can easily find and browse all children's Chinese content.

#### Acceptance Criteria

1. THE Collection_Organizer SHALL create 1 NEW collection titled "Tiếng Trung Cho Bé 6-10 Tuổi" (Chinese for Kids 6-10) with a neutral, informative Vietnamese description explaining this is a collection of Chinese curriculums designed for Vietnamese children aged 6-10.
2. THE Collection_Organizer SHALL organize the 22 curriculums into 3 series:
   - Series 1: "Bước Đầu Tiên" (First Steps) — containing the 6 beginner mini curriculums. Description ≤255 chars using a Tone_Palette type.
   - Series 2: "Xây Nền Vững Chắc" (Building Strong Foundations) — containing the 8 beginner short curriculums. Description ≤255 chars using a different Tone_Palette type.
   - Series 3: "Khám Phá Thêm" (Explore More) — containing the 8 preintermediate curriculums. Description ≤255 chars using a different Tone_Palette type.
3. THE Collection_Organizer SHALL wire each series to the collection via `curriculum-collection/addSeriesToCollection`.
4. THE Collection_Organizer SHALL set display orders for all 3 series within the collection via `curriculum-series/setDisplayOrder`.
5. THE Collection_Organizer SHALL set display orders for all curriculums within each series via `curriculum/setDisplayOrder`.
6. THE Collection_Organizer SHALL ensure all curriculums within each series share `language: "zh"` and `userLanguage: "vi"`.
7. WHILE assigning series description tones, THE Tone_Assigner SHALL ensure all 3 series use different Tone_Palette types.

### Requirement 9: Activity Schema Compliance

**User Story:** As a platform developer, I want every activity to comply with the platform's content schema, so that the content pipeline processes children's curriculums without errors.

#### Acceptance Criteria

1. Each Activity SHALL include `activityType`, `title`, `description`, and `data` fields.
2. THE `activityType` field SHALL use one of the valid values: introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence.
3. THE `vocabList` field SHALL be an array of lowercase strings (pinyin without tone marks), using the field name `vocabList` (never `words`).
4. WHEN viewFlashcards and speakFlashcards appear in the same session, THE two activities SHALL have identical `vocabList` arrays.
5. All content data SHALL be inside the `data` object, not inline on the activity object.
6. WHEN a writingSentence activity is created, THE activity SHALL have `data.vocabList`, `data.items` (non-empty array), and each item SHALL have `prompt` (Vietnamese instructions with Chinese example sentence including pinyin and translation, plus substitution pattern) and `targetVocab` fields.
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
3. THE Curriculum_Creator SHALL organize scripts into a directory `vi-zh-children-curriculum/`.
4. THE Curriculum_Creator SHALL authenticate all API calls using `firebase_token.get_firebase_id_token` with UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73`.
5. THE Curriculum_Creator SHALL use `https://helloapi.step.is` as the API base URL.
6. THE Curriculum_Creator SHALL individually craft every piece of learner-facing text for its specific curriculum topic, without using template functions, string interpolation, or generic fill-in-the-blank patterns.
7. THE Curriculum_Creator MAY use shared helper functions for activity structure (types, order, data schema) but SHALL hand-write all text content per curriculum.
8. IF a curriculum creation API call fails, THEN THE Curriculum_Creator SHALL log the error with the curriculum title and continue with the next curriculum.
9. THE Curriculum_Creator SHALL reuse the root-level `api_helpers.py` for all API calls (create_curriculum, add_to_series, set_display_order, set_price).
10. THE Curriculum_Creator SHALL create a `vi-zh-children-curriculum/validate_content.py` module for content validation specific to vi-zh children's curriculums.

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

### Requirement 14: Chinese-Specific Content Adaptations

**User Story:** As a content quality owner, I want the Chinese learning content to properly handle Chinese-specific elements (characters, pinyin, tones), so that children learn Chinese correctly from the start.

#### Acceptance Criteria

1. WHEN teaching vocabulary in introAudio scripts, THE Curriculum_Creator SHALL present each word in the format: Chinese character → pinyin (with tone description in simple Vietnamese) → Vietnamese meaning → example sentence. Example: "红 — đọc là 'hóng', thanh 2 nhé — nghĩa là màu đỏ. Ví dụ: 红色的花 — hoa màu đỏ."
2. THE reading passages SHALL be written entirely in Chinese characters (no pinyin in the reading text itself), appropriate for the target level.
3. THE introAudio scripts SHALL explain Chinese tones in child-friendly Vietnamese terms (e.g., "thanh 1 là giọng bằng phẳng như hát một nốt dài", "thanh 3 là giọng xuống rồi lên như khi bạn ngạc nhiên").
4. WHEN cultural context is relevant (festivals, food, zodiac), THE introAudio scripts SHALL include brief, child-friendly cultural explanations in Vietnamese connecting Chinese culture to Vietnamese culture where possible (e.g., both cultures celebrate Lunar New Year).
5. THE vocabList arrays SHALL use pinyin without tone marks, with spaces separating syllables of multi-syllable words (e.g., "ni hao", "xie xie", "chun jie"), all lowercase ASCII characters only.
6. WHEN a word has the same pinyin romanization (without tones) as another word in a different curriculum, THE Curriculum_Creator SHALL disambiguate the vocabList entry by using an extended form or context word. Known homophones requiring disambiguation: "shu" appears in Curriculum 7 (书/shū, book — use "shu" since it's the most common), Curriculum 17 (树/shù, tree — use "da shu" meaning big tree), and Curriculum 22 (竖/shù, vertical stroke — use "shu" in context of "bi hua" strokes, already listed as "shu" but distinguished by curriculum context). The Curriculum_Creator SHALL resolve all pinyin collisions by using extended compound forms where possible.

### Requirement 15: Documentation and Cleanup

**User Story:** As a developer, I want proper documentation after all curriculums are created, so that the content is traceable and reproducible.

#### Acceptance Criteria

1. WHEN all 22 curriculums are created and verified, THE Curriculum_Creator SHALL create a README.md in `vi-zh-children-curriculum/` documenting: collection ID, all series IDs, all curriculum IDs with titles and display orders, vocabulary lists per curriculum (characters + pinyin + Vietnamese meaning), tone assignments (description and farewell), pricing, and SQL verification queries.
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
   - Curriculum 8 (Chinese Food): vivid_scenario
   - Curriculum 9 (Playground): provocative_question
   - Curriculum 10 (Body): surprising_fact
   - Curriculum 11 (Weather): empathetic_observation
   - Curriculum 12 (Wardrobe): metaphor_led
   - Curriculum 13 (Vehicles): bold_declaration
   - Curriculum 14 (Animals): vivid_scenario

   **Series 3 — Khám Phá Thêm (8 preintermediate):**
   - Curriculum 15 (Lunar New Year): surprising_fact
   - Curriculum 16 (Zodiac): metaphor_led
   - Curriculum 17 (Nature): empathetic_observation
   - Curriculum 18 (Shopping): provocative_question
   - Curriculum 19 (Seasons): bold_declaration
   - Curriculum 20 (Daily Routines): vivid_scenario
   - Curriculum 21 (Mid-Autumn): surprising_fact
   - Curriculum 22 (Characters): metaphor_led

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
