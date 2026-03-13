# Project Structure

```
.
├── firebase_token.py              # Shared auth helper — generates Firebase ID tokens for API calls
├── firebase_serviceAccountKey.json # Firebase service account credentials (do not commit secrets)
├── strip-keys.py                  # Utility to remove specified keys from all JSON files recursively
├── strip-keys.json                # List of keys to strip (mp3Url, illustrationSet, segments, etc.)
│
├── learners/
│   ├── hugo/                      # Curriculums for Hugo (en-en, intermediate, series db5930f6)
│   │   └── README.md              # Tracking: creation method, SQL queries, recreation instructions
│   │
│   └── huyen/                     # Curriculums for Huyen (vi-en, coaching)
│       └── README.md              # Tracking: learner profile, curriculum ID, recreation instructions
│
├── original-novels/               # Novel-based bilingual curriculum creation
│   └── the-last-light-of-alder-house/
│       └── README.md              # Tracking: series ID 70b5bb22, SQL queries, recreation instructions
│
└── server                         # Symlink to ../../nspacenest (NestJS helloapi server code)
```

## Conventions

- Source materials (content files, JSON, chapter texts, etc.) are deleted after successful import to DB
- Each source folder keeps a README with: how content was created, SQL queries to find it in DB, enough context to recreate if needed
- Quality bar is documented in the project-level steering (product.md), not in individual folders
- Full content is always recoverable from the DB via `curriculum/getOne` or MCP postgres
- JSON curriculum content uses Vietnamese for user-facing text (`title`, `description`, `preview.text`) and English for reading passages
- `strip_keys()` is a recurring utility pattern — defined inline in scripts to remove generated/transient keys from curriculum JSON before upload
- API calls always go through `firebase_token.get_firebase_id_token(UID)` for auth
- The UID `zs5AMpVfqkcfDf8CJ9qrXdH58d73` is used across all scripts as the authenticated user
