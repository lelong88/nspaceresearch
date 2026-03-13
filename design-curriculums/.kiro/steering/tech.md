# Tech Stack

## Language & Runtime
- Python 3 (scripts are standalone, no package manager or virtual env in repo)

## Key Libraries
- `requests` — HTTP calls to the curriculum REST API
- `firebase-admin` — Firebase Auth for generating ID tokens
- `json` — Curriculum content is JSON (stored as JSON strings in the DB)
- `importlib` — Dynamic module loading for curriculum content files

## External Services
- **Curriculum API**: `https://helloapi.step.is/curriculum` (endpoints: `/create`, `/update`, `/getOne`, `/setDisplayOrder`)
- **Curriculum Collection API**: `https://helloapi.step.is/curriculum-collection` (endpoints: `/create`, `/update`, `/delete`, `/setIsPublic`, `/setDisplayOrder`, `/addCurriculum`, `/removeCurriculum`, `/addSeriesToCollection`, `/removeSeriesFromCollection`, `/addCurriculumToSeries`, `/removeCurriculumFromSeries`, `/listAll`, `/listPublicCollections`)
- **Curriculum Series API**: `https://helloapi.step.is/curriculum-series` (endpoints: `/create`, `/update`, `/delete`, `/setIsPublic`, `/setDisplayOrder`, `/addCurriculum`, `/removeCurriculum`, `/listAll`)
- **Firebase Auth**: Used to generate ID tokens for API authentication
- **PostgreSQL database**: Curriculum data is also queryable via MCP postgres

## Authentication Pattern
All API calls require a Firebase ID token. The shared helper `firebase_token.py` at the repo root:
1. Loads a service account from `firebase_serviceAccountKey.json`
2. Creates a custom token for a UID
3. Exchanges it for an ID token via the Firebase REST API

Scripts import this via `sys.path` manipulation:
```python
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token
```

## Common Commands
```bash
# Create 20 curriculums from topic definitions
python hugo/create_20.py

# Update curriculums with rewritten quality content
python hugo/update_curriculums.py

# Organize curriculums into collections and series
python organize_collections.py

# Strip unnecessary keys from JSON files
python strip-keys.py

# Create a novel chapter curriculum (run from repo root)
python original-novels/the-last-light-of-alder-house/create_chapter1_vi.py
```

## No Build/Test System
There is no build step, test suite, or CI pipeline. Scripts are run directly with `python`.
