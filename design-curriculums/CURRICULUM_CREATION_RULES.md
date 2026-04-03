# Curriculum Creation Rules

Rules that apply specifically when creating new curriculums (via `curriculum/create`).

## Activity Schema Requirements

### practiceMinutes Required on Every Activity
Every activity must have a `practiceMinutes` field (integer). Default values by activity type:

| Activity Type | practiceMinutes |
|---|---|
| `introAudio` | 3 |
| `viewFlashcards` | 6 |
| `speakFlashcards` | 6 |
| `vocabLevel1` | 10 |
| `vocabLevel2` | 10 |
| `vocabLevel3` | 10 |
| `reading` | 5 |
| `speakReading` | 5 |
| `readAlong` | 3 |
| `writingSentence` | 10 |
| `writingParagraph` | 10 |

Adjust if the activity is unusually long or short (e.g., a short welcome introAudio can be 1 minute). Never create activities without `practiceMinutes`.

### vocabList Required on Vocab Activities
`speakFlashcards`, `viewFlashcards`, and `vocabLevel*` (`vocabLevel1`, `vocabLevel2`, `vocabLevel3`) activities must include a `vocabList` field — an array of lowercase strings listing the vocabulary words for that activity.

Rules:
- `vocabList` must be an array of strings — never objects, numbers, or other types
- All strings must be lowercase (e.g. `["resilience", "cognitive"]`, not `["Resilience", "Cognitive"]`)
- The field name must be `vocabList` — never `words`. Using `words` is a schema violation
- This applies everywhere `vocabList` appears: on activities (`viewFlashcards`, `speakFlashcards`, `vocabLevel1`, `vocabLevel2`, `vocabLevel3`, `reading`, `speakReading`) and on `writingParagraph` activities

### Activity Title and Description Required
Every activity must have a `title` and `description` field. Never create activities without them.
- `viewFlashcards`/`speakFlashcards`/`vocabLevel1`/`vocabLevel2`: title = "Flashcards: <topic>", description = "Học N từ: word1, word2, ..."
- `reading`/`speakReading`: title = "Đọc: <topic>", description = first ~80 chars of the reading text
- `readAlong`: title = "Nghe: <topic>", description = "Nghe đoạn văn vừa đọc và theo dõi."
- `introAudio`: title = descriptive label (e.g. "Giới thiệu bài học", "Giới thiệu từ vựng"), description = brief summary
- `writingSentence`/`writingParagraph`: title = "Viết: <topic>", description = brief summary of the writing task
- Review/final sessions: use "Ôn tập" in titles, "Toàn bộ câu chuyện" for full-chapter readAlongs
- Session objects also need a `title` field (e.g. "Phần 1", "Phần 2", "Ôn tập")

## Database Column Length Limits

| Table | Column | Max Length |
|---|---|---|
| `curriculum_series` | `title` | 255 |
| `curriculum_series` | `description` | 255 |
| `curriculum_collections` | `title` | 255 |

`curriculum.content` is `jsonb` (no varchar limit). Keep series descriptions concise (under 255 chars). Collection descriptions are `text` type (no limit).

## One Script Per Curriculum
When creating a series with multiple curriculums, write a separate Python script for each curriculum (e.g., `create_gre_1_altruism.py`, `create_gre_2_dissent.py`). A single "orchestrator" script or README can document the series-level setup.

## Story-Oriented Curriculums (original-novels)

Story-oriented curriculums (housed in `original-novels/`) are for **reading practice**, not vocabulary acquisition. The core rule:

- **Content must be mostly comprehensible at the target level.** The reading passages, vocabulary, and grammar should sit comfortably within what a learner at that level already knows.
- Vocabulary words are **familiar refreshers**, not new learning targets. They should be words the learner has likely encountered before at or below their level.
- The goal is extensive reading — building fluency, confidence, and enjoyment through volume of comprehensible input.
- Ask: "Would a learner at this level understand ~95% of this text without a dictionary?" If not, simplify.

The level tag on the curriculum reflects the reader it's written *for*, not the ceiling it's written *toward*.
