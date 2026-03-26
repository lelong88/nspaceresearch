# En-Zh Textbook: Standard Chinese — Elementary 2

Collection: **Elementary 2 (初级二)** (`<COLLECTION_ID>`) — shared with Wisdom series
Series: **Standard Chinese — Elementary 2** (`<SERIES_ID>`)
Language pair: en-zh | 25 lessons | Level: elementary (HSK2-HSK3)

## Curriculums in series

| # | En-Zh ID | Vi-Zh Source ID | Chinese Lesson Title |
|---|---|---|---|
| 1 | `<TBD>` | `04lOR1Iu5GyOaBUw` | 入乡随俗 |
| 2 | `<TBD>` | `6TnsAlQdyw6xx6j6` | 儿子要回家 |
| 3 | `<TBD>` | `bzMQCJ3ODqTyxvcV` | 卖辣椒的女孩子 |
| 4 | `<TBD>` | `3tIKKfVXUwww4KBB` | 我和中国有个约会 |
| 5 | `<TBD>` | `6fRciqUGdeS39m0K` | 为什么我一个人站着吃 |
| 6 | `<TBD>` | `iv3p0NFL9cyF3EWf` | 我这里一切都好 |
| 7 | `<TBD>` | `dGmm3KJ3wd2Xk3Nq` | 我要去埃及 |
| 8 | `<TBD>` | `eWWS8wx2dK5navFR` | 旧梦 |
| 9 | `<TBD>` | `UpQJ6qlRmT5yhhmm` | 爱的教育 |
| 10 | `<TBD>` | `u7tQyss5mINeIlb7` | 快乐其实很简单 |
| 11 | `<TBD>` | `Sp0sb06QkTkL0oQF` | 书本里的蚂蚁 |
| 12 | `<TBD>` | `yJW8SV8SlQbJFx95` | 是枕头不是针头 |
| 13 | `<TBD>` | `0FpGky16VkzBwc7k` | 中国来信改变了我的生活 |
| 14 | `<TBD>` | `51NO0BdwwGbPAqDP` | 善良的故事 |
| 15 | `<TBD>` | `HxsWBc4i3Ie6X8Qt` | 飞回来的信鸽 |
| 16 | `<TBD>` | `rquilJXtJVThwV2U` | 把表拨快三分钟 |
| 17 | `<TBD>` | `4ugX5vWM4Bwzt9BQ` | 情人节的故事 |
| 18 | `<TBD>` | `WDbSfoEVOr2gnDTh` | 给盲人的电影 |
| 19 | `<TBD>` | `hECHbCbj79pVkOOp` | 笔友 |
| 20 | `<TBD>` | `nrdO48JrgloCPZ4w` | 第一人格 |
| 21 | `<TBD>` | `854X10xTGjg0M0eY` | 愚公移山 |
| 22 | `<TBD>` | `ABzPkpADwRRs4bWj` | 卡 |
| 23 | `<TBD>` | `qzqSoSAItNpDN9Ls` | 我的低碳生活 |
| 24 | `<TBD>` | `AO78wULDqE4eXwJP` | 父子长城 |
| 25 | `<TBD>` | `tqcNssMIdyl1hOXO` | 打车去柏林 |

## Vi-Zh Source

- Collection: `64fb68f8` — "Sơ Cấp 2 (初级二)"
- Series: `dqce6wbh` — "Hán Ngữ Phổ Thông - Sơ cấp 2"
- Display orders: 1–25

## How content was created

Each en-zh lesson curriculum was derived from its vi-zh source via a standalone Python script:

1. **Fetch** the vi-zh source curriculum via `curriculum/getOne`
2. **Strip** auto-generated keys (`mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`) using `strip_keys()`
3. **Transform** all Vietnamese user-facing text to hand-written English — titles, descriptions (with pedagogical framing for English speakers), previews, introAudio scripts, writing prompts, activity titles/descriptions, session titles, vocabulary definitions
4. **Upload** via `curriculum/create` with `language="zh"`, `userLanguage="en"`

The orchestrator script (`create_en_zh_textbook_series.py`) created the en-zh Elementary 2 collection and the Standard Chinese — Elementary 2 series, wired them together, added all 25 lesson curriculums to the series, and set display orders 1–25. Series display order: 0 (matching vi-zh source).

The Elementary 2 collection (`<COLLECTION_ID>`) is shared with the Wisdom in Chinese Characters series.

Structure per lesson curriculum:
- Vocabulary drawn from the textbook lesson, HSK2-HSK3 level
- Multiple sessions: learning sessions + review + full reading with farewell
- Textbook reading passages in simplified Chinese
- introAudio scripts include pinyin when teaching vocabulary
- Writing prompts include pinyin in parentheses and Chinese example sentences
- `language="zh"`, `userLanguage="en"` as top-level API params
- All curriculums are private (`is_public = false`)

All creation scripts were deleted after successful creation and verification. Content is fully recoverable via `curriculum/getOne` with each curriculum ID.

## SQL queries

```sql
-- Find en-zh Elementary 2 collection (shared with wisdom series)
SELECT * FROM curriculum_collections WHERE id = '<COLLECTION_ID>';

-- Find en-zh series in Elementary 2 collection
SELECT cs.*
FROM curriculum_series cs
JOIN curriculum_collection_series ccs ON ccs.curriculum_series_id = cs.id
WHERE ccs.curriculum_collection_id = '<COLLECTION_ID>';

-- Find en-zh textbook lessons
SELECT c.id, c.content->>'title' as title, c.display_order
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id = '<SERIES_ID>'
ORDER BY c.display_order;

-- Check language homogeneity
SELECT * FROM curriculum_series_language_list WHERE id = '<SERIES_ID>';

-- Compare with vi-zh source series
SELECT c.id, c.content->>'title' as title, c.display_order, c.language, c.user_language
FROM curriculum c
JOIN curriculum_series_items csi ON csi.curriculum_id = c.id
WHERE csi.curriculum_series_id = 'dqce6wbh'
ORDER BY c.display_order;
```
