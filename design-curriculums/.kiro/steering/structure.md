# Project Structure

```
.
├── firebase_token.py              # Shared auth helper — generates Firebase ID tokens for API calls
├── firebase_serviceAccountKey.json # Firebase service account credentials (do not commit secrets)
├── strip-keys.py                  # Utility to remove specified keys from all JSON files recursively
├── strip-keys.json                # List of keys to strip (mp3Url, illustrationSet, segments, etc.)
├── sample.json                    # Sample full curriculum JSON (Vietnamese "Disagree and Commit")
│
├── hugo/                          # Curriculums for Hugo (a learner)
│   ├── PROMPT.md                  # Original prompt/instructions used to generate curriculums
│   ├── create_20.py               # Generates 20 curriculums from inline topic definitions, uploads via API
│   ├── create_20_curriculums.py   # Alternative/expanded curriculum builder with per-session builders
│   ├── update_curriculums.py      # Patches existing curriculums with rewritten quality content from curriculums/
│   └── curriculums/               # One Python file per curriculum, each exports a CONTENT dict
│       ├── README.md              # Quality bar documentation and content structure spec
│       ├── sleep.py               # Example: "The Invisible Architecture of Sleep"
│       ├── attention.py           # Each file: CONTENT = { curriculum_id, title, preview, s1_intro, ... }
│       └── ...                    # 20 files total, named by topic slug
│
├── original-novels/               # Novel-based bilingual curriculum creation
│   └── the-last-light-of-alder-house/
│       ├── chapters/              # Plain text chapter files (1.txt through 20.txt)
│       └── create_chapter*_vi.py  # Per-chapter scripts that build Vietnamese-English curriculums
│
├── huyen/                         # Curriculums for Huyen (a learner)
│   ├── background.md              # Learner profile (small business owner, healthy meals)
│   └── opportunity-cost.json      # Full curriculum JSON tailored to learner's context
│
└── server                         # (binary/script — purpose unclear)
```

## Conventions

- Curriculum content files live in `hugo/curriculums/` as Python modules exporting a `CONTENT` dict
- Module names use snake_case topic slugs (e.g. `ocean_floor.py`, `ai_ethics.py`)
- Novel chapter scripts follow the pattern `create_chapter{N}_vi.py`
- JSON curriculum content uses Vietnamese for user-facing text (`title`, `description`, `preview.text`) and English for reading passages
- `strip_keys()` is a recurring utility pattern — defined inline in multiple scripts to remove generated/transient keys from curriculum JSON before upload
- API calls always go through `firebase_token.get_firebase_id_token(UID)` for auth
- The UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73` is used across all scripts as the authenticated user
