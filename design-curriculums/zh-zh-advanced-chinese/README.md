# 中文进阶 — ZH-ZH Advanced Chinese Curriculums

Chinese-for-Chinese-speakers (zh-zh) curriculums covering advanced vocabulary across intellectually rich topics. Mirrors the EN-EN "Power English" model: native speakers learning advanced vocabulary in their own language through topic-based content with 成语, 书面语, and specialized domain terminology.

Collection ID: `lqhx014h` — 中文进阶
Language pair: `zh-zh` (Chinese speaker learning advanced Chinese)

## Structure

1 collection → 2 series → 4 curriculums each → 8 curriculums total
Each curriculum: 10 vocab words, 4 sessions (S1: 5 words, S2: 5 words, S3: review all 10, S4: full article + farewell), 80 unique words total across the collection.

## Series 1: 思维与认知 (Thinking & Cognition)

Series ID: `mkxbcpty` (display_order: 100)

| Order | Curriculum ID | Title | Vocabulary |
|---|---|---|---|
| 0 | `gqfr8ddT9fyJ0a4e` | 认知偏差的隐形陷阱 | 锚定效应, 确认偏误, 从众心理, 后见之明, 沉没成本, 框架效应, 可得性启发, 光环效应, 禀赋效应, 达克效应 |
| 1 | `EthSjYjyqjqyIVTg` | 决策的艺术与科学 | 博弈论, 机会成本, 边际效用, 风险规避, 囚徒困境, 纳什均衡, 逆向选择, 道德风险, 有限理性, 前景理论 |
| 2 | `2fsjGmBTt20U7TKd` | 记忆的建筑学 | 海马体, 突触可塑性, 程序性记忆, 情景记忆, 工作记忆, 记忆宫殿, 遗忘曲线, 间隔重复, 虚假记忆, 闪光灯记忆 |
| 3 | `luRDFiVxu8fFIq1i` | 注意力经济学 | 注意力经济, 信息茧房, 多巴胺回路, 深度工作, 认知负荷, 心流状态, 注意力残留, 数字极简主义, 默认模式网络, 元认知 |

## Series 2: 社会与文明 (Society & Civilization)

Series ID: `qm9pj07x` (display_order: 200)

| Order | Curriculum ID | Title | Vocabulary |
|---|---|---|---|
| 0 | `x5UGuIAARA9fmCq3` | 语言如何塑造思维 | 萨丕尔-沃尔夫假说, 语言相对论, 语义场, 隐喻认知, 语码转换, 语言濒危, 认知语言学, 概念隐喻, 语用学, 言语行为理论 |
| 1 | `lAGsVxNRKKGfz87w` | 城市的隐秘逻辑 | 城市肌理, 绅士化, 公共空间, 城市热岛效应, 步行指数, 混合用途开发, 城市蔓延, 韧性城市, 社区营造, 城市针灸 |
| 2 | `tag5bapRyxin7cHA` | 信任的崩塌与重建 | 社会资本, 制度信任, 人际信任, 信任半径, 声誉机制, 囚徒博弈, 公地悲剧, 社会契约, 透明度悖论, 信任修复 |
| 3 | `nq9oSCkUV8GFbk5m` | 算法时代的伦理困境 | 算法偏见, 数据主权, 监控资本主义, 算法黑箱, 数字鸿沟, 技术伦理, 隐私悖论, 算法问责, 深度伪造, 技术中立论 |

## How They Were Created

- 8 standalone Python scripts (one per curriculum) built complete curriculum content JSON inline with hand-written Chinese text — all introAudio scripts, reading passages, descriptions, previews, and writing prompts individually crafted per topic
- Each script called `curriculum/create` with `language:"zh"`, `userLanguage:"zh"`, verified the result via `curriculum/getOne` (checking language fields, 4 sessions, activity counts [11,11,6,6], activity type sequences, vocab counts, Chinese-only text, no strip-keys, reading excerpt ⊂ article), and checked for duplicates
- An orchestrator script created the collection and 2 series, added curriculums to series, added series to collection, and set all display orders
- All 9 Python scripts were deleted after successful creation and verification, per workspace conventions

## To Recreate

1. Write 8 creation scripts following the 4-session EN-EN "Power English" pattern (Sessions 1–2: 11 activities each teaching 5 words; Session 3: 6 activities reviewing all 10; Session 4: 6 activities with full article + farewell)
2. Each curriculum needs: Chinese persuasive copy description/preview, 10 advanced vocab words with definitions and example sentences, introAudio teaching scripts (500–800 chars), reading excerpts and full article (800–1200 chars), writingSentence prompts (5 per session), writingParagraph prompts
3. Upload via `curriculum/create` with `language:"zh"`, `userLanguage:"zh"`, content as JSON string
4. Organize via orchestrator: create collection + series, add curriculums, set display orders
5. Full content is recoverable from the DB via `curriculum/getOne` for any curriculum ID listed above

## SQL Queries

Find all curriculums in the collection:

```sql
SELECT c.id, c.content->>'title' as title, c.display_order, c.language, c.user_language
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
JOIN curriculum_series cs ON csi.curriculum_series_id = cs.id
JOIN curriculum_collection_series ccs ON cs.id = ccs.curriculum_series_id
WHERE ccs.curriculum_collection_id = 'lqhx014h'
ORDER BY cs.display_order, c.display_order;
```

Find curriculums in Series 1 (思维与认知):

```sql
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'mkxbcpty'
ORDER BY c.display_order;
```

Find curriculums in Series 2 (社会与文明):

```sql
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON c.id = csi.curriculum_id
WHERE csi.curriculum_series_id = 'qm9pj07x'
ORDER BY c.display_order;
```

Find the collection and its series:

```sql
SELECT cc.id as collection_id, cc.title as collection_title,
       cs.id as series_id, cs.title as series_title, cs.display_order as series_order
FROM curriculum_collections cc
JOIN curriculum_collection_series ccs ON cc.id = ccs.curriculum_collection_id
JOIN curriculum_series cs ON ccs.curriculum_series_id = cs.id
WHERE cc.id = 'lqhx014h'
ORDER BY cs.display_order;
```
