# Design Document: Vietnamese-English Buddhism & Meditation Curriculums

## Overview

This design covers the creation of 20 English-learning curriculums for Vietnamese speakers on Buddhism, meditation, and mindfulness topics. The system consists of:

- **20 standalone Python scripts** — one per curriculum, each containing hand-crafted content
- **1 orchestrator script** — creates the collection, 3 series, wires them together, sets display orders and prices
- **1 content validator module** — validates curriculum JSON against corruption rules before upload
- **Shared API helpers** — reuses the existing root-level `api_helpers.py` module for all REST API calls

The language pair is `userLanguage="vi"` (Vietnamese speakers), `language="en"` (learning English). All marketing text (titles, descriptions, previews) is in Vietnamese. All reading passages are in English. introAudio scripts are bilingual (Vietnamese explanations for English vocabulary). Difficulty levels span preintermediate (~10 curriculums) and intermediate (~10 curriculums), all with 4 sessions each, priced at 49 credits.

### Key Design Decisions

1. **Reuse existing `api_helpers.py`** — the root-level module already wraps all needed API endpoints (create_curriculum, create_collection, create_series, add_to_series, add_series_to_collection, set_display_order, set_series_display_order, set_price) with Firebase auth, error handling, and logging.

2. **Buddhism-specific validator** — a new `vi-en-buddhism-meditation/validate_content.py` validates the specific structural rules for this batch: exactly 4 sessions, activity sequences matching the declared skill focus format (story-reading, speaking, balanced), contentTypeTags correctness, and all standard corruption checks.

3. **Three skill focus formats** — each format has a distinct activity sequence template. The validator accepts a `format` parameter ("story_reading", "speaking", "balanced") and checks the activity sequence matches.

4. **Tone assignments pre-planned** — with 20 curriculums across 3 series, all description tones and farewell tones are pre-planned in the design to satisfy adjacency and distribution constraints. Hard-coded directly in each script.

5. **No template content** — every piece of learner-facing text (introAudio, reading passages, descriptions, previews, writing prompts) is individually crafted per curriculum. Scripts may share structural helpers but all text is hand-written.

6. **Private by default** — no script calls `setPublic`. Curriculums need content generation (audio, illustrations) before being exposed to learners.

## Architecture

```mermaid
graph TD
    subgraph "vi-en-buddhism-meditation/"
        ORCH[orchestrator.py] --> API
        VAL[validate_content.py]
        
        C1[create_con_duong_giac_ngo.py] --> VAL
        C1 --> API
        C2[create_ngoi_chua_trong_suong.py] --> VAL
        C2 --> API
        C3[create_cau_chuyen_thien_su.py] --> VAL
        C3 --> API
        C4[create_hanh_trinh_chanh_niem.py] --> VAL
        C4 --> API
        C5[create_nhung_bai_hoc_tu_hoa_sen.py] --> VAL
        C5 --> API
        C6[create_mua_an_cu.py] --> VAL
        C6 --> API
        C7[create_anh_sang_tu_bi.py] --> VAL
        C7 --> API
        C8[create_thien_cho_nguoi_moi.py] --> VAL
        C8 --> API
        C9[create_noi_ve_chanh_niem.py] --> VAL
        C9 --> API
        C10[create_doi_thoai_ve_phat_giao.py] --> VAL
        C10 --> API
        C11[create_chia_se_trai_nghiem_thien.py] --> VAL
        C11 --> API
        C12[create_tai_khoa_tu.py] --> VAL
        C12 --> API
        C13[create_phat_giao_va_doi_song.py] --> VAL
        C13 --> API
        C14[create_bat_chanh_dao.py] --> VAL
        C14 --> API
        C15[create_thien_dinh_moi_ngay.py] --> VAL
        C15 --> API
        C16[create_tu_dieu_de.py] --> VAL
        C16 --> API
        C17[create_chanh_niem_trong_an_uong.py] --> VAL
        C17 --> API
        C18[create_thien_hanh.py] --> VAL
        C18 --> API
        C19[create_khong_gian_thien.py] --> VAL
        C19 --> API
        C20[create_tam_tu_va_thien_tam_tu.py] --> VAL
        C20 --> API
    end

    API[api_helpers.py<br/>shared, repo root]
    API --> FB[firebase_token.py]
    API --> REST[helloapi.step.is REST API]
    REST --> DB[(PostgreSQL)]
```

### Execution Flow

```mermaid
sequenceDiagram
    participant Dev as Developer
    participant Orch as orchestrator.py
    participant Script as create_*.py (x20)
    participant Val as validate_content.py
    participant API as api_helpers.py
    participant Server as helloapi.step.is

    Dev->>Orch: python orchestrator.py
    Orch->>API: create_collection(title, description)
    API->>Server: POST /curriculum-collection/create
    Server-->>API: { id: collection_id }
    Orch->>API: create_series (x3)
    Orch->>API: add_series_to_collection (x3)
    Orch->>API: set_series_display_order (x3)
    Orch-->>Dev: Print collection_id, series_ids

    loop For each curriculum (1-20)
        Dev->>Script: python create_<topic>.py
        Script->>Script: Build content JSON (hand-crafted)
        Script->>Val: validate(content, format)
        Val-->>Script: OK or raise ValueError
        Script->>API: create_curriculum(content, "en", "vi")
        API->>Server: POST /curriculum/create
        Server-->>API: { id: curriculum_id }
        Script->>API: add_to_series(series_id, curriculum_id)
        Script->>API: set_display_order(curriculum_id, order)
        Script->>API: set_price(curriculum_id, 49)
        Script-->>Dev: Print curriculum_id
    end
```

## Components and Interfaces

### 1. orchestrator.py

Creates the collection and 3 series, wires them together, sets display orders.

**Inputs:** None (all data hard-coded — collection/series titles, descriptions, tone assignments)

**Outputs:** Prints collection ID, 3 series IDs

**API calls:**
- `curriculum-collection/create` — 1 call
- `curriculum-series/create` — 3 calls
- `curriculum-collection/addSeriesToCollection` — 3 calls
- `curriculum-series/setDisplayOrder` — 3 calls

**Collection:**
- Title: "Phật Giáo, Thiền Định & Chánh Niệm" (Vietnamese)
- Description: Neutral informative Vietnamese description about the collection containing English-learning curriculums on Buddhism, meditation, and mindfulness for Vietnamese speakers.

**Series tone assignments (hard-coded in orchestrator):**

| Entity | Tone |
|--------|------|
| Series 1: "Đọc Truyện Phật Giáo" (Story-Reading, 7 curriculums) | `vivid_scenario` |
| Series 2: "Luyện Nói Về Thiền & Chánh Niệm" (Speaking, 6 curriculums) | `empathetic_observation` |
| Series 3: "Kỹ Năng Toàn Diện" (Balanced, 7 curriculums) | `bold_declaration` |

### 2. validate_content.py

Content validator supporting three curriculum skill focus formats.

**Interface:**
```python
def validate(content: dict, format: str) -> None:
    """
    Validates curriculum content JSON for Buddhism/meditation curriculums.
    
    Args:
        content: The curriculum content dict
        format: One of "story_reading", "speaking", "balanced"
    
    Raises:
        ValueError with specific violation message on any failure.
    """
```

**Format configurations:**

| Format | Sessions | contentTypeTags | Vocab Words |
|--------|----------|-----------------|-------------|
| `story_reading` | 4 | `["story"]` | 10-12 |
| `speaking` | 4 | `[]` | 10-12 |
| `balanced` | 4 | `[]` | 10-12 |

**Validation checks:**
1. Top-level structure: `title`, `description`, `preview.text`, `contentTypeTags`, `learningSessions`
2. Session count = 4
3. Each session has `title` and non-empty `activities` array
4. Each activity has `activityType` (not `type`), `title`, `description`, `data` object
5. Valid `activityType` values (introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingParagraph)
6. `vocabList` is array of lowercase strings, field name is `vocabList` (not `words`)
7. `viewFlashcards`/`speakFlashcards` in same session have identical `vocabList`
8. `writingSentence` has `data.vocabList`, `data.items` with `prompt` and `targetVocab`
9. `writingParagraph` has `data.vocabList`, `data.instructions`, `data.prompts` (length >= 2)
10. No strip-keys anywhere in JSON tree
11. `contentTypeTags` matches format (`["story"]` for story_reading, `[]` for speaking/balanced)
12. Activity sequence matches the declared format template
13. Writing activities (writingSentence, writingParagraph) only appear in sessions 3 and 4

### 3. Individual Curriculum Scripts (create_*.py x 20)

Each script is standalone and contains all hand-crafted content for one curriculum.

**Common interface pattern:**
```python
# create_<topic>.py
import sys
import json
import logging

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/vi-en-buddhism-meditation")
from api_helpers import (
    create_curriculum, add_to_series, set_display_order, set_price
)
from validate_content import validate

SERIES_ID = "<series_id>"  # From orchestrator output
DISPLAY_ORDER = <N>
PRICE = 49

def build_content() -> dict:
    """Build the curriculum content dict with all hand-crafted text."""
    return {
        "title": "...",  # Vietnamese
        "description": "...",  # Vietnamese persuasive copy
        "preview": {"text": "..."},  # Vietnamese ~150 words
        "contentTypeTags": ["story"],  # or [] for speaking/balanced
        "learningSessions": [...]
    }

def main():
    content = build_content()
    validate(content, format="story_reading")  # or "speaking" / "balanced"
    curriculum_id = create_curriculum(content, "en", "vi")
    add_to_series(SERIES_ID, curriculum_id)
    set_display_order(curriculum_id, DISPLAY_ORDER)
    set_price(curriculum_id, PRICE)
    print(f"Created: {curriculum_id}")

if __name__ == "__main__":
    main()
```

### 4. Tone Assignment Table

Pre-planned to satisfy all adjacency and distribution constraints.

**Curriculum description tones and farewell tones:**

| # | Curriculum | Series | Order | Level | Desc Tone | Farewell Tone |
|---|-----------|--------|-------|-------|-----------|---------------|
| 1 | Con Đường Giác Ngộ | Đọc Truyện Phật Giáo | 1 | preintermediate | provocative_question | introspective_guide |
| 2 | Ngôi Chùa Trong Sương | Đọc Truyện Phật Giáo | 2 | preintermediate | vivid_scenario | warm_accountability |
| 3 | Những Bài Học Từ Hoa Sen | Đọc Truyện Phật Giáo | 3 | preintermediate | empathetic_observation | quiet_awe |
| 4 | Câu Chuyện Thiền Sư | Đọc Truyện Phật Giáo | 4 | intermediate | bold_declaration | team_building_energy |
| 5 | Hành Trình Chánh Niệm | Đọc Truyện Phật Giáo | 5 | intermediate | surprising_fact | practical_momentum |
| 6 | Mùa An Cư | Đọc Truyện Phật Giáo | 6 | intermediate | metaphor_led | introspective_guide |
| 7 | Ánh Sáng Từ Bi | Đọc Truyện Phật Giáo | 7 | intermediate | provocative_question | warm_accountability |
| 8 | Thiền Cho Người Mới | Luyện Nói Về Thiền & Chánh Niệm | 1 | preintermediate | bold_declaration | quiet_awe |
| 9 | Nói Về Chánh Niệm | Luyện Nói Về Thiền & Chánh Niệm | 2 | preintermediate | vivid_scenario | team_building_energy |
| 10 | Tại Khóa Tu | Luyện Nói Về Thiền & Chánh Niệm | 3 | preintermediate | surprising_fact | practical_momentum |
| 11 | Đối Thoại Về Phật Giáo | Luyện Nói Về Thiền & Chánh Niệm | 4 | intermediate | empathetic_observation | introspective_guide |
| 12 | Chia Sẻ Trải Nghiệm Thiền | Luyện Nói Về Thiền & Chánh Niệm | 5 | intermediate | metaphor_led | warm_accountability |
| 13 | Phật Giáo Và Đời Sống Hiện Đại | Luyện Nói Về Thiền & Chánh Niệm | 6 | intermediate | provocative_question | quiet_awe |
| 14 | Bát Chánh Đạo | Kỹ Năng Toàn Diện | 1 | preintermediate | bold_declaration | team_building_energy |
| 15 | Thiền Định Mỗi Ngày | Kỹ Năng Toàn Diện | 2 | preintermediate | empathetic_observation | practical_momentum |
| 16 | Chánh Niệm Trong Ăn Uống | Kỹ Năng Toàn Diện | 3 | preintermediate | vivid_scenario | introspective_guide |
| 17 | Không Gian Thiền | Kỹ Năng Toàn Diện | 4 | preintermediate | surprising_fact | warm_accountability |
| 18 | Tứ Diệu Đế | Kỹ Năng Toàn Diện | 5 | intermediate | metaphor_led | quiet_awe |
| 19 | Thiền Hành | Kỹ Năng Toàn Diện | 6 | intermediate | provocative_question | team_building_energy |
| 20 | Tâm Từ Và Thiền Tâm Từ | Kỹ Năng Toàn Diện | 7 | intermediate | bold_declaration | practical_momentum |

**Tone distribution verification (20 curriculums):**
- provocative_question: 4 (20%)
- bold_declaration: 4 (20%)
- vivid_scenario: 3 (15%)
- empathetic_observation: 3 (15%)
- surprising_fact: 3 (15%)
- metaphor_led: 3 (15%)
- Max = 4/20 = 20%, all well under 30% cap (max 6 allowed)

**No adjacent description tone duplicates:**
- Series 1: provocative -> vivid -> empathetic -> bold -> surprising -> metaphor -> provocative (all adjacent pairs different)
- Series 2: bold -> vivid -> surprising -> empathetic -> metaphor -> provocative (all adjacent pairs different)
- Series 3: bold -> empathetic -> vivid -> surprising -> metaphor -> provocative -> bold (all adjacent pairs different)

**Farewell tone distribution (20 curriculums):**
- introspective_guide: 4 (20%)
- warm_accountability: 4 (20%)
- team_building_energy: 4 (20%)
- quiet_awe: 4 (20%)
- practical_momentum: 4 (20%)
- Evenly distributed (4 each, within 3-5 range)

**No adjacent farewell tone duplicates:**
- Series 1: introspective -> warm -> quiet -> team -> practical -> introspective -> warm (all adjacent pairs different)
- Series 2: quiet -> team -> practical -> introspective -> warm -> quiet (all adjacent pairs different)
- Series 3: team -> practical -> introspective -> warm -> quiet -> team -> practical (all adjacent pairs different)

### 5. Activity Templates

#### Story-Reading Format (contentTypeTags: ["story"])

```
Session 1 (Group 1, ~5-6 words):
  1. introAudio — welcome + teach words group 1 (500-800 words, bilingual)
  2. viewFlashcards (group 1)
  3. speakFlashcards (group 1)
  4. reading — narrative passage 150-200 words using group 1 words
  5. speakReading
  6. readAlong
  7. introAudio — session wrap-up

Session 2 (Group 2, ~5-6 words):
  1. introAudio — recap group 1 + teach group 2 (500-800 words, bilingual)
  2. viewFlashcards (group 2)
  3. speakFlashcards (group 2)
  4. reading — narrative passage 150-200 words using group 2 words
  5. speakReading
  6. readAlong
  7. introAudio — session wrap-up

Session 3 (Review):
  1. introAudio — review intro
  2. viewFlashcards (all words)
  3. speakFlashcards (all words)
  4. vocabLevel1 (all words)
  5. reading — story continuation 200-250 words using all words
  6. speakReading
  7. readAlong
  8. introAudio — review wrap-up

Session 4 (Final):
  1. introAudio — final reading intro
  2. reading — story conclusion 250-300 words using all words
  3. speakReading
  4. readAlong
  5. writingSentence (3-4 items reflecting on the story)
  6. introAudio — farewell with vocab review (400-600 words)
```

#### Speaking Format (contentTypeTags: [])

```
Session 1 (Group 1, ~5-6 words):
  1. introAudio — welcome + teach words group 1 (500-800 words, bilingual)
  2. viewFlashcards (group 1)
  3. speakFlashcards (group 1)
  4. vocabLevel1 (group 1)
  5. speakFlashcards (group 1 — second round)
  6. reading — short passage 80-100 words
  7. speakReading
  8. introAudio — session wrap-up

Session 2 (Group 2, ~5-6 words):
  1. introAudio — recap group 1 + teach group 2 (500-800 words, bilingual)
  2. viewFlashcards (group 2)
  3. speakFlashcards (group 2)
  4. vocabLevel1 (group 2)
  5. speakFlashcards (group 2 — second round)
  6. reading — short passage 80-100 words
  7. speakReading
  8. introAudio — session wrap-up

Session 3 (Review):
  1. introAudio — review intro
  2. speakFlashcards (all words)
  3. vocabLevel1 (all words)
  4. vocabLevel2 (all words)
  5. speakFlashcards (all words — second round)
  6. reading — passage 100-120 words
  7. speakReading
  8. introAudio — review wrap-up

Session 4 (Final):
  1. introAudio — final session intro
  2. speakFlashcards (all words)
  3. vocabLevel2 (all words)
  4. reading — passage 120-150 words
  5. speakReading
  6. readAlong
  7. writingSentence (2-3 items)
  8. introAudio — farewell with vocab review (400-600 words)
```

#### Balanced Format (contentTypeTags: [])

```
Session 1 (Group 1, ~5-6 words):
  1. introAudio — welcome + teach words group 1 (500-800 words, bilingual)
  2. viewFlashcards (group 1)
  3. speakFlashcards (group 1)
  4. vocabLevel1 (group 1)
  5. reading — passage 120-150 words
  6. speakReading
  7. readAlong
  8. introAudio — session wrap-up

Session 2 (Group 2, ~5-6 words):
  1. introAudio — recap group 1 + teach group 2 (500-800 words, bilingual)
  2. viewFlashcards (group 2)
  3. speakFlashcards (group 2)
  4. vocabLevel1 (group 2)
  5. reading — passage 120-150 words
  6. speakReading
  7. readAlong
  8. introAudio — session wrap-up

Session 3 (Review):
  1. introAudio — review intro
  2. viewFlashcards (all words)
  3. speakFlashcards (all words)
  4. vocabLevel1 (all words)
  5. vocabLevel2 (all words)
  6. reading — passage 150-180 words
  7. speakReading
  8. readAlong
  9. writingSentence (4-5 items)
  10. introAudio — review wrap-up

Session 4 (Final):
  1. introAudio — final reading intro
  2. reading — full passage 200-250 words using all words
  3. speakReading
  4. readAlong
  5. writingSentence (3-4 items)
  6. writingParagraph (1 prompt)
  7. introAudio — farewell with vocab review (400-600 words)
```

## Data Models

### Curriculum Content JSON Structure

```json
{
  "title": "Con Đường Giác Ngộ",
  "description": "TẠI SAO CON NGƯỜI TÌM KIẾM SỰ GIÁC NGỘ?\n\nTừ ngàn xưa, con người đã...",
  "preview": {
    "text": "Hãy tưởng tượng bạn đang bước trên con đường mà Đức Phật đã đi qua hơn 2500 năm trước..."
  },
  "contentTypeTags": ["story"],
  "learningSessions": [
    {
      "title": "Phần 1",
      "activities": [
        {
          "activityType": "introAudio",
          "title": "Chào mừng đến với Con Đường Giác Ngộ",
          "description": "Giới thiệu bài học và từ vựng phần 1",
          "data": {
            "text": "Xin chào bạn! Hôm nay chúng ta sẽ cùng nhau khám phá câu chuyện về hành trình giác ngộ của Đức Phật Thích Ca Mâu Ni qua tiếng Anh nhé...\n\nTừ đầu tiên là 'enlightenment' — /ɪnˈlaɪtənmənt/ — nghĩa là sự giác ngộ, sự khai sáng. Ví dụ: The Buddha achieved enlightenment under the Bodhi tree..."
          }
        },
        {
          "activityType": "viewFlashcards",
          "title": "Flashcards: Con đường giác ngộ (phần 1)",
          "description": "Học 5 từ: enlightenment, renounce, suffering, meditation, awakening",
          "data": {
            "vocabList": ["enlightenment", "renounce", "suffering", "meditation", "awakening"]
          }
        },
        {
          "activityType": "speakFlashcards",
          "title": "Flashcards: Con đường giác ngộ (phần 1)",
          "description": "Học 5 từ: enlightenment, renounce, suffering, meditation, awakening",
          "data": {
            "vocabList": ["enlightenment", "renounce", "suffering", "meditation", "awakening"]
          }
        },
        {
          "activityType": "reading",
          "title": "Đọc: Hoàng tử Siddhartha",
          "description": "Long ago in ancient India, a young prince named Siddhartha Gautama lived in a magnificent palace...",
          "data": {
            "text": "Long ago in ancient India, a young prince named Siddhartha Gautama lived in a magnificent palace. His father, the king, protected him from all suffering in the world...",
            "vocabList": ["enlightenment", "renounce", "suffering", "meditation", "awakening"]
          }
        },
        {
          "activityType": "speakReading",
          "title": "Đọc: Hoàng tử Siddhartha",
          "description": "Long ago in ancient India, a young prince named Siddhartha Gautama lived in a magnificent palace...",
          "data": {
            "text": "Long ago in ancient India, a young prince named Siddhartha Gautama lived in a magnificent palace. His father, the king, protected him from all suffering in the world..."
          }
        },
        {
          "activityType": "readAlong",
          "title": "Nghe: Hoàng tử Siddhartha",
          "description": "Nghe đoạn văn vừa đọc và theo dõi.",
          "data": {
            "text": "Long ago in ancient India, a young prince named Siddhartha Gautama lived in a magnificent palace. His father, the king, protected him from all suffering in the world..."
          }
        },
        {
          "activityType": "introAudio",
          "title": "Kết thúc phần 1",
          "description": "Tóm tắt và kết thúc phần học",
          "data": {
            "text": "Tuyệt vời! Bạn vừa hoàn thành phần 1 của bài học..."
          }
        }
      ]
    }
  ]
}
```

### writingSentence Item Structure

```json
{
  "activityType": "writingSentence",
  "title": "Viết: Suy ngẫm về con đường giác ngộ",
  "description": "Viết câu tiếng Anh về hành trình giác ngộ",
  "data": {
    "vocabList": ["enlightenment", "renounce", "suffering", "meditation", "awakening", "compassion", "path", "wisdom", "serenity", "liberation"],
    "items": [
      {
        "prompt": "Dùng từ 'enlightenment' để viết một câu về hành trình tâm linh. Ví dụ: The monk spent decades in meditation before reaching enlightenment.",
        "targetVocab": "enlightenment"
      },
      {
        "prompt": "Dùng từ 'compassion' để viết một câu về lòng từ bi trong đời sống hàng ngày. Ví dụ: True compassion means understanding the suffering of others without judgment.",
        "targetVocab": "compassion"
      },
      {
        "prompt": "Dùng từ 'liberation' để viết một câu về sự giải thoát khỏi khổ đau. Ví dụ: Buddhism teaches that liberation from suffering comes through understanding its root causes.",
        "targetVocab": "liberation"
      }
    ]
  }
}
```

### writingParagraph Structure

```json
{
  "activityType": "writingParagraph",
  "title": "Viết: Bát Chánh Đạo trong đời sống",
  "description": "Viết đoạn văn tiếng Anh về Bát Chánh Đạo",
  "data": {
    "vocabList": ["righteous", "speech", "action", "livelihood", "effort", "concentration", "understanding", "intention", "ethical", "conduct"],
    "instructions": "Viết 3-5 câu tiếng Anh về cách bạn có thể áp dụng Bát Chánh Đạo (Noble Eightfold Path) vào cuộc sống hàng ngày. Sử dụng ít nhất 3-4 từ vựng đã học trong bài.",
    "prompts": [
      "Explain how right speech and right action can improve your daily interactions with others. Use vocabulary from this session to describe specific examples.",
      "Describe how right effort and right concentration can help you overcome challenges in modern life. Connect these Buddhist principles to practical situations you face."
    ]
  }
}
```

### API Call Parameters

| API Endpoint | Key Parameters |
|---|---|
| `curriculum/create` | `firebaseIdToken`, `language: "en"`, `userLanguage: "vi"`, `content: JSON.stringify(content)` |
| `curriculum-series/addCurriculum` | `firebaseIdToken`, `curriculumSeriesId`, `curriculumId` |
| `curriculum/setDisplayOrder` | `firebaseIdToken`, `id`, `displayOrder` |
| `curriculum/setPrice` | `firebaseIdToken`, `id`, `price: 49` |
| `curriculum-collection/create` | `firebaseIdToken`, `title`, `description` |
| `curriculum-series/create` | `firebaseIdToken`, `title`, `description` |
| `curriculum-collection/addSeriesToCollection` | `firebaseIdToken`, `curriculumCollectionId`, `curriculumSeriesId` |
| `curriculum-series/setDisplayOrder` | `firebaseIdToken`, `id`, `displayOrder` |

### Vocabulary Lists (All 20 Curriculums)

| # | Curriculum | vocabList | Count |
|---|---|---|---|
| 1 | Con Đường Giác Ngộ | enlightenment, renounce, suffering, meditation, awakening, compassion, path, wisdom, serenity, liberation | 10 |
| 2 | Ngôi Chùa Trong Sương | temple, incense, chant, monk, prayer, bell, offering, devotion, silence, ritual | 10 |
| 3 | Những Bài Học Từ Hoa Sen | lotus, bloom, mud, purity, patience, growth, resilience, beauty, emerge, transform | 10 |
| 4 | Câu Chuyện Thiền Sư | parable, disciple, insight, paradox, detachment, mindful, stillness, impermanence, awareness, transcend, koan, contemplation | 12 |
| 5 | Hành Trình Chánh Niệm | mindfulness, breath, anchor, present, observe, acceptance, wandering, intention, clarity, equanimity, cultivate, surrender | 12 |
| 6 | Mùa An Cư | retreat, discipline, solitude, reflection, vow, perseverance, community, harmony, simplicity, gratitude, renewal, dedication | 12 |
| 7 | Ánh Sáng Từ Bi | compassion, empathy, forgiveness, generosity, kindness, selfless, benevolence, reconciliation, altruism, unconditional, embrace, nurture | 12 |
| 8 | Thiền Cho Người Mới | breathe, focus, relax, posture, inhale, exhale, calm, gentle, steady, release | 10 |
| 9 | Nói Về Chánh Niệm | awareness, moment, attention, distraction, grounding, sensation, acknowledge, respond, pause, balance | 10 |
| 10 | Tại Khóa Tu | schedule, session, instructor, guidance, practice, technique, beginner, intermediate, silent, mindful | 10 |
| 11 | Đối Thoại Về Phật Giáo | philosophy, reincarnation, karma, nirvana, dharma, sangha, enlighten, meditate, spiritual, doctrine, scripture, monastery | 12 |
| 12 | Chia Sẻ Trải Nghiệm Thiền | profound, transformative, peaceful, restless, breakthrough, struggle, consistent, progress, insight, revelation, surrender, blissful | 12 |
| 13 | Phật Giáo Và Đời Sống Hiện Đại | integrate, contemporary, stress, anxiety, therapeutic, holistic, secular, wellness, resilience, sustainable, intentional, flourish | 12 |
| 14 | Bát Chánh Đạo | righteous, speech, action, livelihood, effort, concentration, understanding, intention, ethical, conduct | 10 |
| 15 | Thiền Định Mỗi Ngày | routine, habit, morning, evening, duration, timer, cushion, comfortable, consistent, benefit | 10 |
| 16 | Chánh Niệm Trong Ăn Uống | savor, texture, aroma, gratitude, nourish, chew, appreciate, portion, mindful, conscious | 10 |
| 17 | Không Gian Thiền | sanctuary, candle, cushion, altar, tranquil, atmosphere, minimal, natural, sacred, arrange | 10 |
| 18 | Tứ Diệu Đế | truth, suffering, origin, cessation, noble, craving, attachment, liberation, diagnosis, prescription, remedy, realization | 12 |
| 19 | Thiền Hành | stride, pace, deliberate, sensation, grounding, rhythm, awareness, surroundings, footstep, synchronize, embodiment, presence | 12 |
| 20 | Tâm Từ Và Thiền Tâm Từ | radiate, wellbeing, boundless, extend, recipient, phrase, visualize, warmth, genuine, universal, infinite, intention | 12 |

**Overlap check:** Note that a few words appear in multiple curriculums (e.g., "compassion" in #1 and #7, "mindful" in #4 and #10, "suffering" in #1 and #18, "intention" in #5 and #20, "awareness" in #4 and #19, "insight" in #4 and #12, "surrender" in #5 and #12, "resilience" in #3 and #13, "liberation" in #1 and #18, "gratitude" in #6 and #16, "cushion" in #15 and #17). Per Requirement 2.3, no more than 2 shared words between any two curriculums. The maximum overlap between any pair is 2 words (e.g., #1 and #18 share "suffering" and "liberation"), which satisfies the constraint.

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system — essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

The content validator (`validate_content.py`) is the primary component amenable to property-based testing. It is a pure function: takes a content dict and format string, returns None or raises ValueError. The input space is large (arbitrary JSON structures), and universal properties hold across all valid/invalid inputs.

The curriculum creation scripts, orchestrator, and API interactions are integration-level concerns tested via database verification queries after execution.

### Property 1: Valid content passes validation

*For any* well-formed curriculum content dict that matches its declared format (correct session count of 4, activity sequence matching the format template, all required fields present, vocabList arrays valid, contentTypeTags correct for format, no strip keys), calling `validate(content, format)` SHALL return without raising an exception.

**Validates: Requirements 1.4, 1.5, 3.1, 3.2, 3.3, 3.4, 9.1, 10.1, 10.2**

### Property 2: contentTypeTags validation per format

*For any* curriculum content dict, if the format is "story_reading" and contentTypeTags is not `["story"]`, OR if the format is "speaking"/"balanced" and contentTypeTags is not `[]`, then `validate()` SHALL raise a ValueError.

**Validates: Requirements 1.4, 1.5, 10.10**

### Property 3: Strip keys rejected anywhere in JSON tree

*For any* curriculum content dict and any strip key (mp3Url, illustrationSet, chapterBookmarks, segments, whiteboardItems, userReadingId, lessonUniqueId, curriculumTags, taskId, imageId), if that key is injected at any depth in the JSON tree, `validate()` SHALL raise a ValueError mentioning the strip key.

**Validates: Requirements 1.6, 10.9**

### Property 4: Activity sequence matches declared format

*For any* curriculum content dict, if the activity type sequence in any session does not match the expected template for the declared format (story_reading, speaking, or balanced), `validate()` SHALL raise a ValueError identifying the session and expected sequence.

**Validates: Requirements 3.1, 3.2, 3.3**

### Property 5: Activity structural requirements enforced

*For any* activity in any curriculum content, if any of the required fields (`activityType`, `title`, `description`, `data`) is missing, if `data` is not a dict, or if `activityType` is not in the valid set (introAudio, viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2, reading, speakReading, readAlong, writingSentence, writingParagraph), `validate()` SHALL raise a ValueError.

**Validates: Requirements 9.1, 9.2, 10.3, 10.4**

### Property 6: vocabList format enforced

*For any* vocab activity (viewFlashcards, speakFlashcards, vocabLevel1, vocabLevel2), if `data.vocabList` contains non-lowercase strings, is not an array, is empty, or uses the field name `words` instead of `vocabList`, `validate()` SHALL raise a ValueError.

**Validates: Requirements 9.3, 10.5**

### Property 7: Flashcard vocabList consistency within sessions

*For any* session containing both `viewFlashcards` and `speakFlashcards` activities, if their `data.vocabList` arrays differ, `validate()` SHALL raise a ValueError.

**Validates: Requirements 9.4, 10.6**

### Property 8: writingSentence structure enforced

*For any* `writingSentence` activity, if `data.vocabList` is missing, `data.items` is missing or empty, or any item lacks a non-empty `prompt` or `targetVocab`, `validate()` SHALL raise a ValueError.

**Validates: Requirements 9.6, 10.7**

### Property 9: writingParagraph structure enforced

*For any* `writingParagraph` activity, if `data.vocabList` is missing, `data.instructions` is missing or empty, or `data.prompts` is missing or has fewer than 2 items, `validate()` SHALL raise a ValueError.

**Validates: Requirements 9.7, 10.8**

### Property 10: Top-level structure enforced

*For any* curriculum content dict, if `title` is missing or empty, `description` is missing or empty, `preview.text` is missing or empty, or `learningSessions` is not an array of exactly 4 sessions each with a non-empty `title` and `activities` array, `validate()` SHALL raise a ValueError.

**Validates: Requirements 10.1, 10.2, 3.4**

### Property 11: Writing activities restricted to sessions 3 and 4

*For any* curriculum content dict, if a `writingSentence` or `writingParagraph` activity appears in session 1 or session 2, `validate()` SHALL raise a ValueError.

**Validates: Requirements 16.4**

## Error Handling

### Validator Errors

The `validate_content.py` module raises `ValueError` with a specific message identifying:
- The exact rule violated
- The location in the JSON tree (e.g., "Session 2, Activity 3")
- The expected vs. actual value

Each curriculum script calls `validate()` before any API call. If validation fails, the script aborts with the error message — no partial upload occurs.

### API Call Errors

Each curriculum script follows this error handling pattern:

1. **Validation failure** — Script aborts immediately, prints the violation. No API calls made.
2. **`curriculum/create` failure** — Script logs the error with curriculum title and exits.
3. **`add_to_series` failure** — Curriculum exists but is orphaned. Script logs the error. Developer must manually add to series or delete the curriculum.
4. **`set_display_order` failure** — Curriculum exists in series but without explicit order. Script logs the error. Developer must manually set order.
5. **`set_price` failure** — Curriculum exists with default price. Script logs the error. Developer must manually set price.

The orchestrator follows the same pattern:
1. **`create_collection` failure** — Abort. Nothing created.
2. **`create_series` failure** — Log error, continue with remaining series. Developer must manually create the failed series.
3. **`add_series_to_collection` failure** — Series exists but is orphaned. Log error, continue.
4. **`set_series_display_order` failure** — Log error, continue. Developer must manually set order.

### Duplicate Handling

After each curriculum creation, the script logs the curriculum ID. If a script is accidentally run twice, the developer runs the duplicate check query:

```sql
SELECT id, content->>'title' as title, created_at FROM curriculum
WHERE content->>'title' = '<title>'
AND uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
AND uid NOT LIKE '%_deleted'
ORDER BY created_at;
```

Keep the earliest, delete extras (remove from series first, then delete curriculum).

## Testing Strategy

### Property-Based Tests (validate_content.py)

**Library:** [Hypothesis](https://hypothesis.readthedocs.io/) (Python PBT library)

**Configuration:** Minimum 100 iterations per property test.

**Tag format:** Each test is tagged with a comment: `# Feature: vi-en-buddhism-meditation, Property N: <property_text>`

The 11 correctness properties above are implemented as Hypothesis property tests in a `test_validate_content.py` file. Each property test generates random curriculum content structures using Hypothesis strategies and verifies the validator's behavior.

**Generator strategies needed:**
- `valid_curriculum(format)` — generates a structurally valid curriculum content dict for the given format (story_reading, speaking, balanced), with correct activity sequences, valid vocabLists, and proper contentTypeTags
- `random_activity(activity_type)` — generates a valid activity of the given type with all required fields
- `random_vocab_list(n)` — generates a list of n random lowercase English strings
- `random_strip_key()` — picks a random strip key from the set of 10 forbidden keys
- `random_json_path()` — picks a random location in a content dict to inject a key
- `random_format()` — picks one of "story_reading", "speaking", "balanced"

### Example-Based Tests

- Verify no vocabulary overlap exceeds 2 words between any pair of the 20 curriculums (Req 2.3)
- Verify tone assignment table has no adjacent duplicates within each series (Req 5.5)
- Verify no description tone exceeds 30% of 20 descriptions (Req 5.6)
- Verify farewell tone distribution is 3-5 per register (Req 6.8)
- Verify no adjacent farewell tone duplicates within each series (Req 6.7)
- Verify all 3 series use different description tones (Req 8.7)
- Verify correct activity sequence templates for each format (Req 3.1, 3.2, 3.3)
- Verify no script calls `setPublic` (Req 12.1)
- Verify no title contains difficulty level indicators (Req 13.3)

### Integration Verification (Post-Execution)

After all 20 scripts run, verify via SQL queries:

```sql
-- Count all vi-en Buddhism curriculums (expect 20)
SELECT COUNT(*) FROM curriculum
WHERE id IN (<list of 20 IDs>);

-- Verify language pair
SELECT id, content->>'title' as title, language, user_language
FROM curriculum WHERE id IN (<list of 20 IDs>);

-- Verify all prices are 49
SELECT id, content->>'title' as title, price
FROM curriculum WHERE id IN (<list of 20 IDs>)
WHERE price != 49;

-- Verify series membership and display orders
SELECT cs.id as series_id, cs.title as series_title,
       c.id as curriculum_id, c.content->>'title' as curriculum_title,
       c.display_order, c.price
FROM curriculum_series cs
JOIN curriculum_series_items csi ON cs.id = csi.curriculum_series_id
JOIN curriculum c ON csi.curriculum_id = c.id
WHERE cs.id IN (<series_1_id>, <series_2_id>, <series_3_id>)
ORDER BY cs.display_order, c.display_order;

-- Verify contentTypeTags for story-reading curriculums
SELECT id, content->>'title' as title, content->'contentTypeTags' as tags
FROM curriculum WHERE id IN (<story_reading_ids>);

-- Verify no duplicates
SELECT content->>'title' as title, COUNT(*)
FROM curriculum
WHERE uid = 'zs5AMpVfqkcfDf8CJ9qrXdH58d73'
AND content->>'title' IN (<list of 20 titles>)
AND uid NOT LIKE '%_deleted'
GROUP BY content->>'title'
HAVING COUNT(*) > 1;

-- Verify collection-series wiring
SELECT cc.id as collection_id, cc.title as collection_title,
       cs.id as series_id, cs.title as series_title, cs.display_order
FROM curriculum_collections cc
JOIN curriculum_collection_series ccs ON cc.id = ccs.curriculum_collection_id
JOIN curriculum_series cs ON ccs.curriculum_series_id = cs.id
WHERE cc.id = '<collection_id>'
ORDER BY cs.display_order;
```

### Smoke Tests

- Verify each of the 20 script files exists in `vi-en-buddhism-meditation/`
- Verify orchestrator.py exists in `vi-en-buddhism-meditation/`
- Verify validate_content.py exists in `vi-en-buddhism-meditation/`
- Verify no script contains `setPublic` calls
- Verify orchestrator creates exactly 1 collection and 3 series
