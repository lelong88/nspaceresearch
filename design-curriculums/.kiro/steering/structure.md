# Project Structure

```
.
├── firebase_token.py              # Shared auth helper — generates Firebase ID tokens for API calls
├── firebase_serviceAccountKey.json # Firebase service account credentials (do not commit secrets)
├── strip-keys.py                  # Utility to remove specified keys from all JSON files recursively
├── strip-keys.json                # List of keys to strip (mp3Url, illustrationSet, segments, etc.)
│
├── learners/
│   ├── hugo/                      # Curriculums for Hugo (en-en, intermediate)
│   │   ├── README.md              # Tracking info: SQL query to find Hugo's curriculums in DB
│   │   ├── PROMPT.md              # Original prompt/instructions used to generate curriculums
│   │   ├── update_curriculums.py  # Patches existing curriculums with rewritten content from curriculums/
│   │   └── curriculums/           # One Python file per curriculum, each exports a CONTENT dict
│   │       ├── README.md          # Quality bar documentation and content structure spec
│   │       ├── sleep.py           # Example: "The Invisible Architecture of Sleep"
│   │       ├── attention.py       # Each file: CONTENT = { curriculum_id, title, preview, s1_intro, ... }
│   │       └── ...                # 20 files total, named by topic slug
│   │
│   └── huyen/                     # Curriculums for Huyen (vi-en, coaching)
│       ├── README.md              # Tracking info: curriculum ID and SQL query
│       ├── background.md          # Learner profile (small business owner, healthy meals)
│       └── opportunity-cost.json  # Full curriculum JSON tailored to learner's context
│
├── original-novels/               # Novel-based bilingual curriculum creation
│   └── the-last-light-of-alder-house/
│       ├── README.md              # Tracking info: series ID, SQL query for chapter-to-curriculum mapping
│       └── chapters/              # Plain text chapter files (1.txt through 20.txt) — original source material
│
└── server                         # Symlink to ../../nspacenest (NestJS helloapi server code)
```

## Conventions

- Curriculum content files live in `learners/hugo/curriculums/` as Python modules exporting a `CONTENT` dict
- Module names use snake_case topic slugs (e.g. `ocean_floor.py`, `ai_ethics.py`)
- Original source material (chapter text files, learner profiles, prompt docs, etc.) is always preserved
- Each source folder has a README explaining how to query the DB for corresponding curriculum IDs
- JSON curriculum content uses Vietnamese for user-facing text (`title`, `description`, `preview.text`) and English for reading passages
- `strip_keys()` is a recurring utility pattern — defined inline in multiple scripts to remove generated/transient keys from curriculum JSON before upload
- API calls always go through `firebase_token.get_firebase_id_token(UID)` for auth
- The UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73` is used across all scripts as the authenticated user
