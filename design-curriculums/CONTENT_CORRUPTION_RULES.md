# Content JSON Corruption Detection Rules

Deterministic rules derived from all 377 curriculum rows. Excludes strip-keys (`difficultyTags`, `practiceTime`, `contentTypeTags`, `skillFocusTags`, and others in `strip-keys.json`) — their presence or absence is irrelevant.

## 1. Top-Level Structure

| Rule | Check |
|---|---|
| `content` is a JSON object | `jsonb_typeof(content) = 'object'` |
| Has `title` | non-null, non-empty string |
| Has `description` | non-null, non-empty string |
| Has `preview` | object with `text` (non-empty string) |
| Has `learningSessions` | array, length ≥ 1 |

## 2. Session Structure

| Rule | Check |
|---|---|
| Each session is an object | `jsonb_typeof = 'object'` |
| Has `title` | non-empty string |
| Has `activities` | array, length ≥ 1 |

## 3. Activity Structure (all types)

| Rule | Check |
|---|---|
| Each activity is an object | `jsonb_typeof = 'object'` |
| Has `activityType` | string. Must NOT use `type` (old schema — corrupted) |
| Valid activityType value | one of: `introAudio`, `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, `vocabLevel2`, `vocabLevel3`, `reading`, `speakReading`, `readAlong`, `writingSentence`, `writingParagraph` |
| Has `practiceMinutes` | number, > 0 |
| Has `title` | string |
| Has `description` | string |
| Has `data` field | object. Content fields must be inside `data`, NOT inline on the activity (inline = corrupted) |

## 4. Activity-Type-Specific Data Rules

### introAudio
| Rule | Check |
|---|---|
| `data.text` | non-empty string |

### reading, speakReading, readAlong
| Rule | Check |
|---|---|
| `data.text` | non-empty string |

### viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, vocabLevel3
| Rule | Check |
|---|---|
| `data.vocabList` | non-empty array of strings |
| Field name is `vocabList` | never `words` |

### writingSentence
| Rule | Check |
|---|---|
| `data.vocabList` | non-empty array of strings |
| `data.items` | non-empty array |
| Each item has `prompt` | non-empty string |
| Each item has `targetVocab` | non-empty string. Must NOT use `word` (old schema — corrupted) |

### writingParagraph
| Rule | Check |
|---|---|
| `data.vocabList` | array of strings |
| Has prompt content | either `data.prompts` or `data.prompt` present |

## 5. Cross-Field Consistency

| Rule | Check |
|---|---|
| `viewFlashcards` and `speakFlashcards` in the same session have identical `vocabList` | Mismatch means vocab was edited on one but not the other |

## 6. Not Corruption (false positives to avoid)

- Multiple `introAudio` per session is normal (1–4 is common: welcome, vocab intro, farewell)
- Short reading text is valid for song/music curriculums
- Any key in `strip-keys.json` being present or absent is irrelevant — those are auto-generated
