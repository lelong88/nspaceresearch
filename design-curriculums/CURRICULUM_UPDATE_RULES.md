# Curriculum Update Rules

Rules that apply specifically when editing/rewriting existing curriculums (via `curriculum/update`).

## CRITICAL — Never strip keys via `curriculum/update`

NEVER fetch an existing curriculum's content, strip keys, and push it back via `curriculum/update`. This destroys all generated metadata (`taskId`, `illustrationSet`, `curriculumTags`, `mp3Url`, `segments`, `lessonUniqueId`, `imageId`, `userReadingId`, etc.) that was produced by the content generation pipeline — requiring a full re-generation of audio, illustrations, and other assets.

When updating specific fields on an existing curriculum (e.g., rewriting `introAudio` text, fixing a `description`), only modify the targeted fields and preserve all other keys intact. Use `curriculum/removeGeneratedContent` if you intentionally need to trigger re-generation for specific activities.

## What to strip when rewriting content
When rewriting text fields, strip `mp3Url` from: `preview`, `introAudio` activities, `writingSentence` items, `writingParagraph` — so audio can be regenerated.

## What NOT to change when rewriting
- Activity structure (types, order, count)
- Vocabulary lists
- Reading passages
- Activity types that aren't introAudio/writingSentence/writingParagraph
