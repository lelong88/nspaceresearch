# Tech Stack

## Language & Runtime
- Python 3 (scripts are standalone, no package manager or virtual env in repo)

## Key Libraries
- `requests` — HTTP calls to the curriculum REST API
- `firebase-admin` — Firebase Auth for generating ID tokens
- `json` — Curriculum content is JSON (stored as JSON strings in the DB)
- `importlib` — Dynamic module loading for curriculum content files

## External Services
- **Firebase Auth**: Used to generate ID tokens for API authentication
- **PostgreSQL database**: Curriculum data is also queryable via MCP postgres

## API Base URL
`https://helloapi.step.is`

All endpoints are POST. All require `firebaseIdToken` in the JSON body (middleware converts it to `uid` before the controller sees it).

### Auth Levels
- **AuthGuard**: Any authenticated user. Endpoints: `curriculum/create`, `curriculum/update`, `curriculum/list`, `curriculum/listPurchased`, `curriculum/delete`, `curriculum/updateTitle`, `curriculum/setPublic`, `curriculum/markComplete`, `curriculum-collection/listAll`
- **SuperAuthGuard**: Admin-only (UID must be in the hardcoded allowlist). Endpoints: `curriculum/setDisplayOrder`, `curriculum/setPrice`, `curriculum/removeGeneratedContent`, all `curriculum-series/*`, all `curriculum-collection/*` except `listAll`, `listPublicCollections`, `getOne`
- **No auth**: `curriculum/getOne`, `curriculum/listPublic`, `curriculum-collection/listPublicCollections`, `curriculum-collection/getOne`

### Curriculum API (`/curriculum`)

| Endpoint | Body Params | Auth | Notes |
|---|---|---|---|
| `/create` | `language`, `userLanguage`, `content` (JSON string) | AuthGuard | `content` can be string or object (service handles both), but `language` and `userLanguage` MUST be top-level body params, not just inside content. Returns `{ id, ... }` |
| `/update` | `id`, `content` | AuthGuard | |
| `/updateTitle` | `id`, `title` | AuthGuard | |
| `/getOne` | `id`, `uid` | None | |
| `/delete` | `id` | AuthGuard | |
| `/list` | (none, uses uid from token) | AuthGuard | Lists curriculums owned by the authenticated user |
| `/listPublic` | `language`, `userLanguage` | None | |
| `/listPurchased` | (none, uses uid from token) | AuthGuard | |
| `/setPublic` | `id`, `isPublic` | AuthGuard | |
| `/setPrice` | `id`, `price` (number) | SuperAuth | |
| `/setDisplayOrder` | `id`, `displayOrder` (integer) | SuperAuth | |
| `/markComplete` | `curriculumId` | AuthGuard | Upserts a completion record for the user |
| `/removeGeneratedContent` | `id`, `activityIndices?` (number[]) | SuperAuth | Strips generated content from specific activities (or all if indices omitted) |

### Curriculum Series API (`/curriculum-series`)

All endpoints require SuperAuthGuard.

| Endpoint | Body Params | Notes |
|---|---|---|
| `/create` | `title`, `description?`, `thumbnail?`, `isPublic?` | Returns the created series. Note: does NOT accept `language`/`userLanguage` — those are inferred from the curriculums added to it |
| `/update` | `id`, `title?`, `description?`, `thumbnail?` | |
| `/delete` | `id` | |
| `/getOne` | `id` | |
| `/listAll` | (none) | Returns all series |
| `/setIsPublic` | `id`, `isPublic` | Field is `id`, NOT `curriculumSeriesId` |
| `/setDisplayOrder` | `id`, `displayOrder` (integer) | |
| `/addCurriculum` | `curriculumSeriesId`, `curriculumId` | Adds a curriculum to the series. Display order on the curriculum itself must be set separately via `curriculum/setDisplayOrder` |
| `/removeCurriculum` | `curriculumSeriesId`, `curriculumId` | |

### Curriculum Collection API (`/curriculum-collection`)

| Endpoint | Body Params | Auth | Notes |
|---|---|---|---|
| `/create` | `title`, `description?`, `thumbnail?`, `isPublic?` | SuperAuth | |
| `/update` | `id`, `title?`, `description?`, `thumbnail?` | SuperAuth | |
| `/delete` | `id` | SuperAuth | |
| `/getOne` | `id` | None | |
| `/listAll` | (none) | AuthGuard | Returns all collections (not just public) |
| `/listPublicCollections` | `userLanguage?`, `targetLanguage?` | None | Filters by language, includes series and curriculums. Main client-facing endpoint |
| `/setIsPublic` | `id`, `isPublic` | SuperAuth | |
| `/setDisplayOrder` | `id`, `displayOrder` (integer) | SuperAuth | |
| `/addCurriculum` | `curriculumCollectionId`, `curriculumId` | SuperAuth | Adds a curriculum directly to a collection (not via series) |
| `/removeCurriculum` | `curriculumCollectionId`, `curriculumId` | SuperAuth | |
| `/addSeriesToCollection` | `curriculumCollectionId`, `curriculumSeriesId` | SuperAuth | |
| `/removeSeriesFromCollection` | `curriculumCollectionId`, `curriculumSeriesId` | SuperAuth | |
| `/addCurriculumToSeries` | `curriculumSeriesId`, `curriculumId` | SuperAuth | Alternative to `curriculum-series/addCurriculum` |
| `/removeCurriculumFromSeries` | `curriculumSeriesId`, `curriculumId` | SuperAuth | Alternative to `curriculum-series/removeCurriculum` |

### Common Gotchas
- `curriculum/create` requires `language` and `userLanguage` as separate top-level body fields alongside `content`. Putting them only inside the content JSON causes a 500.
- `curriculum-series/setIsPublic` uses `id` as the param name, not `curriculumSeriesId`. Same for `curriculum-collection/setIsPublic`.
- `curriculum-series/addCurriculum` does NOT set `displayOrder` on the curriculum. You must call `curriculum/setDisplayOrder` separately for each curriculum after adding it to the series.
- `curriculum-series/create` does not accept `language`/`userLanguage`. The series inherits language info from its member curriculums.
- `content` in `curriculum/create` and `curriculum/update` can be either a JSON string or an object — the service normalizes it. But sending it as a string is the canonical approach.

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
# Strip unnecessary keys from JSON files
python strip-keys.py
```

## No Build/Test System
There is no build step, test suite, or CI pipeline. Scripts are run directly with `python`.

## Script Authoring — Write in Smaller Chunks

Large `fs_write` operations on Python scripts (especially curriculum-creation scripts with embedded JSON content) frequently fail or produce malformed output. To prevent this:

- **Initial creation**: use `fs_write` for only the script skeleton — imports, constants, helper functions, and a `main()` stub. Keep this under ~100 lines.
- **Adding content**: use `fs_append` to add one logical section at a time (e.g., one session's activities, one curriculum's content blob, one helper function). Aim for ~50-150 lines per append.
- **Editing existing content**: use `str_replace` for targeted edits rather than rewriting the whole file.
- **Embedded JSON**: when a script contains a large JSON content blob, build it incrementally with `fs_append` calls per session/activity rather than one mega-write. Verify the file parses (`python -c "import ast; ast.parse(open('script.py').read())"`) after each chunk.
- **Avoid heredocs and inline `python -c` for multi-line content** — they amplify quoting/escaping errors. Stick to `fs_write` + `fs_append` + `str_replace`.

This applies to all `create_*.py`, `update_*.py`, and similar scripts in `learners/`, `original-novels/`, and ad-hoc curriculum work.
