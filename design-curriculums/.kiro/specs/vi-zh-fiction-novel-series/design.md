# Design Document: vi-zh Fiction Novel Series

## Overview

This feature creates a 10-chapter Chinese fiction novel curriculum series for Vietnamese-Chinese (vi-zh) preintermediate learners. The workflow mirrors the existing vi-en "The Little Bookshop by the Sea" series (n4y9zm3v) but targets Chinese (zh) instead of English, with an entirely different original story.

The pipeline is:
1. Write an original simplified Chinese novel (10 chapters, HSK2-3 vocabulary)
2. Structure each chapter as a Python content module exporting a curriculum dict
3. Validate all content against correctness properties
4. Upload via per-chapter creation scripts calling the curriculum API
5. Organize into a new vi-zh Fiction collection and series
6. Delete source materials, retain README

The simplified session structure (viewFlashcards + reading + readAlong only) is intentional — this series focuses on immersive reading practice with familiar vocabulary, not new vocabulary acquisition. This contrasts with the heavier vi-zh textbook series (dqce6wbh) which uses introAudio, speakFlashcards, vocabLevel1/2, grammar, speakReading, etc.

## Architecture

```mermaid
graph TD
    A[Novel Text<br/>10 chapters in Chinese] --> B[Content Modules<br/>chapter{N}_content.py]
    B --> C[Validation Script<br/>validate_content.py]
    C --> D[Creation Scripts<br/>create_chapter{N}_vi.py]
    D --> E[Curriculum API<br/>POST /curriculum/create]
    E --> F[Organization Script<br/>organize_series.py]
    F --> G1[POST /curriculum-series/create]
    F --> G2[POST /curriculum-series/addCurriculum]
    F --> G3[POST /curriculum-collection/create]
    F --> G4[POST /curriculum-collection/addSeriesToCollection]
    F --> G5[POST /curriculum/setDisplayOrder]
    G1 & G2 & G3 & G4 & G5 --> H[Cleanup: delete source, keep README]
```

The architecture is a linear pipeline with no runtime components. All scripts are standalone Python files that run once and are deleted after successful import.

### Key Design Decisions

1. **Separate content modules from creation scripts**: Each `chapter{N}_content.py` exports a pure data dict. The `create_chapter{N}_vi.py` script imports it and handles API calls. This separates content authoring from API mechanics, making validation possible before upload.

2. **New vi-zh Fiction collection**: The existing "Truyện (Fiction)" collection (97cee550) contains vi-en content. Adding vi-zh content would violate the language homogeneity rule. A new collection "Truyện (小说)" is created with `language: "zh"` and `userLanguage: "vi"`.

3. **Runtime collection existence check**: The organize script checks whether a vi-zh Fiction collection already exists before creating one, preventing duplicates if the script is re-run or if another vi-zh series is added later.

4. **Simple session structure**: Sessions use only viewFlashcards, reading, and readAlong — no introAudio, speakFlashcards, vocabLevel1/2, grammar, or speakReading. This matches the vi-en novel pattern and keeps the focus on reading immersion.

## Components and Interfaces

### 1. Content Modules (`chapter{N}_content.py`, N=1..10)

Each module exports a single function or dict containing the full curriculum content for one chapter.

```python
# chapter1_content.py
def get_content():
    return {
        "title": "...",          # Bilingual vi-zh title
        "description": "...",    # Vietnamese description
        "preview": { "text": "..." },  # Vietnamese preview (~150 words)
        "learningSessions": [...]       # 6 sessions
    }
```

### 2. Validation Script (`validate_content.py`)

Imports all 10 content modules and checks correctness properties:
- Session count, activity types, activity order
- Vocab counts (3 per session 1-5, 15 total in session 6)
- Reading passage presence and length
- Session 6 concatenation correctness
- Strip-keys absence
- Cross-chapter vocab overlap limits
- Bilingual title format

```python
def validate_chapter(content: dict, chapter_num: int) -> list[str]:
    """Returns list of error messages. Empty = valid."""
```

### 3. Creation Scripts (`create_chapter{N}_vi.py`, N=1..10)

Each script:
1. Imports `firebase_token` via sys.path
2. Imports `chapter{N}_content`
3. Calls POST `/curriculum/create` with `{ firebaseIdToken, uid, language: "zh", userLanguage: "vi", content: JSON.stringify(content) }`
4. Prints created curriculum ID and title

```python
import sys, json, requests
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

from chapter1_content import get_content

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

token = get_firebase_id_token(UID)
content = get_content()
resp = requests.post(f"{API_BASE}/curriculum/create", json={
    "firebaseIdToken": token,
    "uid": UID,
    "language": "zh",
    "userLanguage": "vi",
    "content": json.dumps(content)
})
resp.raise_for_status()
result = resp.json()
print(f"Created: {result['id']} — {content['title']}")
```

### 4. Organization Script (`organize_series.py`)

Handles all post-creation organization:
1. Creates series with bilingual title
2. Adds all 10 curriculums to series (looks up by title pattern)
3. Checks if vi-zh Fiction collection exists; creates if not
4. Adds series to collection
5. Sets display orders 1-10

All IDs are looked up at runtime by title — no hardcoded IDs.

### 5. README (`README.md`)

Post-cleanup documentation containing:
- How content was created
- Series ID, Collection ID
- SQL queries to find curriculums
- Novel summary for recreation context

## Data Models

### Curriculum Content Structure

```json
{
  "title": "[Vietnamese Title] ([Chinese Title]) — Chương 1: [Vi Chapter Title] ([Zh Chapter Title])",
  "description": "Vietnamese description of chapter content and learning objectives",
  "preview": {
    "text": "Vietnamese preview text (~150 words) with vivid hooks..."
  },
  "learningSessions": [
    {
      "activities": [
        {
          "type": "viewFlashcards",
          "vocabList": ["词1", "词2", "词3"],
          "audioSpeed": -0.2
        },
        {
          "type": "reading",
          "text": "Chinese reading passage (~100-150 chars)...",
          "audioSpeed": -0.2
        },
        {
          "type": "readAlong",
          "text": "Same Chinese reading passage as above..."
        }
      ]
    }
  ]
}
```

### Session Structure Summary

| Session | Activities | Vocab Count | Reading Content |
|---------|-----------|-------------|-----------------|
| 1-5 | viewFlashcards → reading → readAlong | 3 words each | ~100-150 chars passage |
| 6 | viewFlashcards → readAlong | 15 words (all) | Full chapter (all 5 passages concatenated) |

### API Request Bodies

**Create Curriculum:**
```json
{
  "firebaseIdToken": "<token>",
  "uid": "zs5AMpVfqkcfDf8CJ9qrXdH58d73",
  "language": "zh",
  "userLanguage": "vi",
  "content": "<JSON string of curriculum content>"
}
```

**Create Series:**
```json
{
  "firebaseIdToken": "<token>",
  "title": "Bilingual series title",
  "description": "Vietnamese series description",
  "isPublic": true
}
```

**Create Collection:**
```json
{
  "firebaseIdToken": "<token>",
  "title": "Truyện (小说)",
  "isPublic": true
}
```

**Add Curriculum to Series:**
```json
{
  "firebaseIdToken": "<token>",
  "curriculumSeriesId": "<series_id>",
  "curriculumId": "<curriculum_id>"
}
```

**Add Series to Collection:**
```json
{
  "firebaseIdToken": "<token>",
  "curriculumCollectionId": "<collection_id>",
  "curriculumSeriesId": "<series_id>"
}
```

**Set Display Order:**
```json
{
  "firebaseIdToken": "<token>",
  "curriculumId": "<curriculum_id>",
  "displayOrder": 1
}
```

### Strip Keys (must NOT appear in content)

`mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`



## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system — essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: Curriculum session structure

*For any* chapter content dict, it must contain exactly 6 learning sessions; sessions 1-5 must each have exactly 3 activities in order [viewFlashcards, reading, readAlong]; session 6 must have exactly 2 activities in order [viewFlashcards, readAlong].

**Validates: Requirements 2.1, 2.2, 2.3**

### Property 2: Activity field presence and audioSpeed

*For any* viewFlashcards activity in any chapter, it must have a `vocabList` array and `audioSpeed` equal to -0.2. *For any* reading activity in any chapter, it must have a non-empty `text` field and `audioSpeed` equal to -0.2. *For any* readAlong activity, it must have a non-empty `text` field.

**Validates: Requirements 2.4, 2.5**

### Property 3: Vocabulary count per chapter and per session

*For any* chapter, the total number of unique vocabulary words across sessions 1-5 must equal exactly 15, and each session's viewFlashcards must contain exactly 3 words.

**Validates: Requirements 1.3, 4.1, 4.3**

### Property 4: ReadAlong-Reading text equality

*For any* chapter and *for any* session 1-5, the readAlong activity's text must be identical to the reading activity's text in the same session.

**Validates: Requirements 2.6**

### Property 5: Session 6 readAlong is full chapter concatenation

*For any* chapter, session 6's readAlong text must equal the concatenation of the reading texts from sessions 1-5 (in order).

**Validates: Requirements 2.7**

### Property 6: Session 6 viewFlashcards is vocab union

*For any* chapter, session 6's viewFlashcards vocabList must contain exactly the union of all vocabList words from sessions 1-5 (all 15 words, no duplicates, no extras).

**Validates: Requirements 2.8**

### Property 7: Cross-chapter vocabulary overlap limit

*For any* pair of chapters, the intersection of their vocabulary lists must have at most 2 words.

**Validates: Requirements 1.5, 4.5**

### Property 8: Reading passage length

*For any* chapter and *for any* session 1-5, the reading passage must be between 80 and 180 Chinese characters (allowing some flexibility around the 100-150 target).

**Validates: Requirements 1.8, 5.4**

### Property 9: Vocabulary words appear in reading passages

*For any* chapter and *for any* session 1-5, every word in that session's viewFlashcards vocabList must appear as a substring in the corresponding reading passage text.

**Validates: Requirements 5.3**

### Property 10: Title format and no level descriptor

*For any* chapter N, the curriculum title must contain "Chương N:" and must NOT contain any of the strings: "preintermediate", "sơ trung cấp", "初级", "中级", "beginner", "intermediate", "advanced".

**Validates: Requirements 3.1, 3.6**

### Property 11: Preview word count

*For any* chapter, the preview text must exist and contain between 100 and 200 words (allowing flexibility around the ~150 target).

**Validates: Requirements 3.3**

### Property 12: No strip keys in content

*For any* chapter content dict, recursively searching the entire structure must find zero occurrences of any strip key: mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId.

**Validates: Requirements 6.1**

## Error Handling

### Content Validation Errors
- `validate_content.py` collects all errors per chapter and prints a summary. It does NOT stop at the first error — all chapters are validated and all errors reported.
- Exit code 1 if any errors found, 0 if all pass.

### API Errors
- Creation scripts call `resp.raise_for_status()` after each API call. HTTP errors (401, 403, 500) will raise exceptions with status code and response body.
- If a creation script fails mid-way, the curriculum may or may not have been created. The organize script looks up curriculums by title, so re-running is safe.

### Duplicate Collection Prevention
- `organize_series.py` queries existing collections before creating a new one. If a vi-zh Fiction collection already exists, it reuses it instead of creating a duplicate.

### Auth Token Expiry
- Firebase ID tokens expire after 1 hour. If running all 10 creation scripts sequentially, each script generates a fresh token. The organize script also generates a fresh token at startup.

## Testing Strategy

### Validation Script (`validate_content.py`)

The validation script implements all 12 correctness properties as checks against the 10 content modules. This is the primary quality gate before upload.

Since there is no test framework in this project (no pytest, no CI), the validation script IS the test suite. It runs all checks and reports pass/fail.

### Property-Based Testing Approach

The content modules are static data (not generated at runtime), so traditional property-based testing with random input generation doesn't apply directly. Instead, the validation script treats the 10 chapters as the input space and verifies each property holds across all of them.

Each check in `validate_content.py` is tagged with a comment referencing the design property:

```python
# Feature: vi-zh-fiction-novel-series, Property 1: Curriculum session structure
def check_session_structure(content, chapter_num):
    ...
```

### Dual Testing Approach

- **Property checks** (Properties 1-12): Verified across all 10 chapters by `validate_content.py`
- **Example checks**: Title format regex match for specific chapter numbers, preview text spot checks
- **Edge cases**: Session 6 concatenation with varying passage lengths, vocab overlap at the boundary (exactly 2 shared words)

### Test Execution

```bash
# Run all validation checks before uploading
python validate_content.py
# Expected output: "All 10 chapters passed validation" or list of errors
```

### Minimum Coverage

Each of the 12 properties is checked against all 10 chapters = 120 property checks minimum. Cross-chapter properties (Property 7: vocab overlap) check all 45 chapter pairs (10 choose 2).
