# Requirements Document

## Introduction

This feature adds two advanced-level English-only (en-en) curriculums on the topic of *Raising Boys*, drawn from Steve Biddulph's book of the same name, targeting parents who are advanced English learners (IELTS ≈ 7.5+). The curriculums cover the early-childhood window the user has scoped as "~4 to 7," which in Biddulph's own framework straddles the central pivot at age six between the *Tender Years* (birth–6, mother-led attachment) and the *Father Years* (6–14, father-led identity formation). To stay faithful to the book and to give each curriculum a clean developmental thesis, the spec splits the window into two curriculums that bracket that pivot:

- **Curriculum A — Ages 4–5 (Closing the Tender Years).** The language-explosion, big-feelings, imaginative-play tail end of Stage 1, where warmth, attunement, and emotional naming still dominate.
- **Curriculum B — Ages 6–7 (Opening the Father Years).** The "switching on" of masculine identity at the start of Stage 2, where fathers (or father figures) move to the foreground and a boy starts looking outward for who he might become.

A reference curriculum already exists in the database (`oIBdDjUpizHWtQTq`, vi-en, beginner, focused on a 1-year-old). It establishes the structural and tonal template — multi-session vocabulary arc, intro audio scripting style, whiteboard cueing, grammar mini-lessons, sectional readings rolling up to a final whole-text reading, farewell intro audio — and the new curriculums adopt that structure while shifting language tier (advanced, English-only), age band (4–5 and 6–7), and conceptual depth.

## Glossary

- **Source_Book**: *Raising Boys* by Steve Biddulph, including its three-stage developmental framework.
- **Tender_Years_Stage**: Biddulph's Stage 1, birth to age 6, characterised by attachment, warmth, and security primarily mediated by the mother or primary caregiver.
- **Father_Years_Stage**: Biddulph's Stage 2, age 6 to age 14, characterised by the father (or a male mentor) moving to the foreground for identity and modelling of masculinity.
- **Curriculum_A**: The first new curriculum, scoped to ages 4–5 within Tender_Years_Stage.
- **Curriculum_B**: The second new curriculum, scoped to ages 6–7 within Father_Years_Stage.
- **New_Curriculum**: Either Curriculum_A or Curriculum_B; statements about New_Curriculum apply to both.
- **Reference_Curriculum**: The existing vi-en curriculum with id `oIBdDjUpizHWtQTq`, used as a structural and tonal template.
- **Curriculum_Content_JSON**: The top-level JSON object stored in `curriculum.content` for a single curriculum, containing `title`, `preview`, `description`, `learningSessions`, `contentTypeTags`, and related fields.
- **Learning_Session**: One ordered group of activities inside `learningSessions`, with its own `title` and `activities` array.
- **Activity**: A single object inside a Learning_Session's `activities` array, identified by `activityType` (`introAudio`, `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, `vocabLevel2`, `reading`, `speakReading`, `readAlong`, `writingSentence`, `writingParagraph`).
- **Vocab_Item**: A single English word or short phrase taught and practised in a Learning_Session.
- **Description_Tone**: One of the six rhetorical tones defined in product steering — `provocative_question`, `bold_declaration`, `vivid_scenario`, `empathetic_observation`, `surprising_fact`, `metaphor_led`.
- **Strip_Keys_Set**: The set of auto-generated keys defined in `strip-keys.json` (`mp3Url`, `illustrationSet`, `chapterBookmarks`, `segments`, `whiteboardItems`, `userReadingId`, `lessonUniqueId`, `curriculumTags`, `taskId`, `imageId`).
- **Curriculum_Builder**: The Python script (or scripts) that constructs Curriculum_Content_JSON and POSTs it to `curriculum/create`.
- **Spec_Author**: The agent or human authoring this spec and its downstream design and tasks.
- **Database**: The platform PostgreSQL database, queryable via MCP postgres.

## Requirements

### Requirement 1: Two-curriculum scope and age-band split

**User Story:** As a content lead, I want this spec to produce exactly two en-en advanced curriculums whose age bands faithfully reflect Biddulph's stages around the age-six pivot, so that the resulting content is true to the Source_Book rather than to a generic "early childhood" framing.

#### Acceptance Criteria

1. THE Spec_Author SHALL deliver exactly two New_Curriculum artifacts: Curriculum_A and Curriculum_B.
2. THE Curriculum_A SHALL scope its content to boys aged 4 to 5 inclusive, positioned as the closing portion of Tender_Years_Stage.
3. THE Curriculum_B SHALL scope its content to boys aged 6 to 7 inclusive, positioned as the opening portion of Father_Years_Stage.
4. THE Curriculum_A `description` SHALL name the Tender_Years_Stage framing in plain prose at least once.
5. THE Curriculum_B `description` SHALL name the Father_Years_Stage framing in plain prose at least once.
6. WHERE the user later requests a single combined 4–7 curriculum instead of the split, THE Spec_Author SHALL flag the request as a deviation from this requirement and confirm before consolidating.

### Requirement 2: Language pair, level, and language-only-content rule

**User Story:** As a learner with IELTS ≈ 7.5+, I want every word of the curriculum's user-facing text in English only, so that the curriculum reads as native-level material and never falls into bilingual scaffolding.

#### Acceptance Criteria

1. THE Curriculum_A SHALL be created with `language = "en"` and `userLanguage = "en"` as top-level body params on `curriculum/create`.
2. THE Curriculum_B SHALL be created with `language = "en"` and `userLanguage = "en"` as top-level body params on `curriculum/create`.
3. THE Curriculum_Content_JSON `title`, `description`, and `preview.text` for each New_Curriculum SHALL be written exclusively in English with no Vietnamese (or other non-English) translations or glosses.
4. THE Curriculum_Content_JSON `difficultyTags` array for each New_Curriculum SHALL contain `"advanced"`, plus the matching skill-level tags `"vocab_advanced"`, `"reading_advanced"`, and `"writing_advanced"`.
5. THE Learning_Session content (intro audio scripts, flashcard glosses, vocab definitions, reading passages, grammar notes, writing prompts) for each New_Curriculum SHALL be written exclusively in English.
6. IF any user-facing string inside Curriculum_Content_JSON contains characters outside the ASCII letters, digits, standard punctuation, and English-context Unicode (smart quotes, em-dash, en-dash), THEN THE Spec_Author SHALL treat that string as a violation and rewrite it before the curriculum is created.
7. THE Curriculum_Content_JSON SHALL NOT include any field encoding a translated pair (for example, side-by-side English and non-English text within a single `text` or `subtitle` value), and the surviving English-only text in those fields SHALL itself satisfy AC2.3 and AC2.5.

### Requirement 3: Source fidelity to Steve Biddulph's *Raising Boys*

**User Story:** As a parent who has read the book, I want the curriculum content to reflect Biddulph's actual claims and tone for the relevant stage, so that I trust the material as a study companion rather than a generic parenting blog.

#### Acceptance Criteria

1. THE Curriculum_A core content SHALL be drawn from Source_Book themes that belong to Tender_Years_Stage at ages 4–5, including at minimum: language and emotional vocabulary growth, the role of warmth and physical affection, slower-than-girls language development as a non-deficit, imaginative play, and big feelings (tantrums, fears, exuberance).
2. THE Curriculum_B core content SHALL be drawn from Source_Book themes that belong to the Father_Years_Stage onset at ages 6–7, including at minimum: the "switching on" of interest in fathers and male role models, the start of a boy's outward-facing identity, structured rough-and-tumble play, the importance of mothers stepping back without disappearing, and the early shape of self-discipline.
3. THE Spec_Author SHALL attribute book-derived ideas to Biddulph by name at least once per New_Curriculum's `description`, and at least once inside any `introAudio` script that paraphrases a book claim.
4. THE Spec_Author SHALL NOT reproduce more than 30 consecutive words of verbatim text from Source_Book in any field of either New_Curriculum.
5. WHERE a Source_Book claim is contested, dated, or culturally specific, THE Spec_Author SHALL phrase the claim as Biddulph's view rather than as universal fact.

### Requirement 4: Reference-curriculum-as-template usage

**User Story:** As the Curriculum_Builder, I want to reuse the structural shape of the existing vi-en *Raising Boys* curriculum without inheriting its generated artefacts, so that the new curriculums look coherent with the platform's house style yet are clean inputs to `curriculum/create`.

#### Acceptance Criteria

1. WHEN the Curriculum_Builder uses Reference_Curriculum's content as a template, THE Curriculum_Builder SHALL strip every key in Strip_Keys_Set from the in-memory copy before composing the new Curriculum_Content_JSON.
2. THE Curriculum_Builder SHALL NOT include any field from Strip_Keys_Set in the Curriculum_Content_JSON sent to `curriculum/create` for either New_Curriculum.
3. THE Spec_Author SHALL preserve from Reference_Curriculum the multi-session arc shape: a sequence of vocabulary-introduction sessions each ending in a session-specific reading, followed by a review session, followed by a whole-text reading session that concatenates the prior session readings.
4. THE Spec_Author SHALL preserve from Reference_Curriculum the within-session activity ordering: an `introAudio` for the session theme, an `introAudio` for the vocabulary, then `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, `vocabLevel2`, then a grammar/usage `introAudio`, then `reading`, `speakReading`, `readAlong`.
5. WHERE Reference_Curriculum's beginner-tier choices conflict with advanced-level expectations (for example, six basic words per session, sub-100-word readings, single-clause sentences), THE Spec_Author SHALL upgrade those choices for each New_Curriculum rather than copy them verbatim.

### Requirement 5: Vocabulary tier appropriate for advanced learners

**User Story:** As an advanced learner, I want each session to teach vocabulary that genuinely extends my range rather than reviewing words I already own, so that the curriculum earns its "advanced" label.

#### Acceptance Criteria

1. THE Vocab_Item set across all Learning_Sessions of a New_Curriculum SHALL be sized between 30 and 48 distinct items, with each Learning_Session that introduces vocabulary teaching between 6 and 10 new Vocab_Items.
2. THE Vocab_Item set for each New_Curriculum SHALL be dominated by lower-frequency, register-rich English (parenting psychology, developmental science, emotional nuance, embodied behaviour) rather than CEFR A1–B1 staples; bare basics already at A1 such as `baby`, `love`, `safe`, `to hold`, `to cry` SHALL NOT appear as taught items.
3. THE Vocab_Item set for Curriculum_A SHALL emphasise emotional attunement, language-and-imagination scaffolding, and somatic regulation vocabulary fitted to ages 4–5.
4. THE Vocab_Item set for Curriculum_B SHALL emphasise identity, modelling, structured play, and early self-regulation vocabulary fitted to ages 6–7 and the onset of Father_Years_Stage.
5. WHEN a Vocab_Item is also present in Reference_Curriculum's 18-word beginner set, THE Spec_Author SHALL replace it with a more advanced near-synonym or upgrade.
6. THE definition gloss for each Vocab_Item in any `introAudio` script SHALL be written in English only, in one or two sentences, with at least one example sentence in English.

### Requirement 6: Reading passage complexity and length

**User Story:** As an advanced learner, I want the reading passages to be substantive parenting essays rather than primer-style sentences, so that I practise comprehension and pacing on real prose.

#### Acceptance Criteria

1. THE per-session `reading` activity for each New_Curriculum SHALL contain between 220 and 360 English words.
2. THE final whole-text `reading` activity for each New_Curriculum SHALL be the concatenation of the per-session readings, separated by paragraph breaks, with no rewriting that changes meaning.
3. THE `reading` activity text for each New_Curriculum SHALL use a mix of simple, compound, and complex sentences, with average sentence length between 14 and 22 words.
4. THE `reading` activity text for each New_Curriculum SHALL embed every Vocab_Item taught in that same Learning_Session at least once, in a context that supports inference of meaning.
5. THE `speakReading` activity for each Learning_Session SHALL use the exact same `text` value as the matching `reading` activity in that Learning_Session.
6. THE `readAlong` activity for each Learning_Session SHALL use the exact same `text` value as the matching `reading` activity in that Learning_Session.

### Requirement 7: Writing activities for advanced practice

**User Story:** As an advanced learner, I want explicit writing prompts that ask me to produce my own English output, so that the curriculum exercises productive skill and not just receptive skill.

#### Acceptance Criteria

1. THE Curriculum_Content_JSON for each New_Curriculum SHALL include at least one `writingSentence` Activity.
2. THE Curriculum_Content_JSON for each New_Curriculum SHALL include at least one `writingParagraph` Activity.
3. THE prompt text for every `writingSentence` and `writingParagraph` Activity SHALL be written in English only.
4. THE prompt text for every `writingSentence` and `writingParagraph` Activity SHALL reference at least two Vocab_Items taught earlier in the same New_Curriculum and SHALL ask the learner to apply a Source_Book idea to their own parenting situation.
5. THE `writingParagraph` prompt for each New_Curriculum SHALL request a paragraph between 80 and 150 words.

### Requirement 8: Activity ordering and session structure

**User Story:** As a learner moving through a session, I want the activity order to follow the platform's standard pedagogical arc, so that input precedes output and recognition precedes recall.

#### Acceptance Criteria

1. THE `learningSessions` array of each New_Curriculum SHALL contain between 4 and 6 Learning_Session entries.
2. THE first Learning_Session of each New_Curriculum SHALL begin with an `introAudio` Activity that frames the curriculum's developmental thesis.
3. THE final Learning_Session of each New_Curriculum SHALL end with a closing `introAudio` Activity that reviews 5 to 6 Vocab_Items with definitions and fresh example sentences (the "farewell" pattern).
4. THE penultimate Learning_Session (or its equivalent role) of each New_Curriculum SHALL be a review session that revisits the cumulative Vocab_Item set across `viewFlashcards`, `vocabLevel1`, and `vocabLevel2` Activities.
5. WITHIN each vocabulary-introducing Learning_Session, THE Activities SHALL appear in the order: theme `introAudio`, vocabulary `introAudio`, `viewFlashcards`, `speakFlashcards`, `vocabLevel1`, `vocabLevel2`, grammar/usage `introAudio`, `reading`, `speakReading`, `readAlong`.
6. WHERE `writingSentence` or `writingParagraph` Activities are placed inside a Learning_Session, THE Activities SHALL appear after the `reading` block of that session.

### Requirement 9: Title, preview, and description quality

**User Story:** As a learner browsing the catalogue, I want titles, previews, and descriptions that are honest, English-native, and rhetorically varied, so that the catalogue feels curated rather than templated.

#### Acceptance Criteria

1. THE `title` for each New_Curriculum SHALL be in English only, SHALL clearly signal the topic and age band, and SHALL NOT contain any difficulty-level word (`beginner`, `intermediate`, `advanced`, `upper-intermediate`).
2. THE `preview.text` for each New_Curriculum SHALL be in English only and SHALL be between 60 and 200 words.
3. THE `description` for each New_Curriculum SHALL open with a tone-assigned ALL-CAPS headline line that uses one of the six Description_Tone values defined in product steering.
4. THE Description_Tone chosen for Curriculum_A's headline SHALL differ from the Description_Tone chosen for Curriculum_B's headline.
5. THE `description` for each New_Curriculum SHALL run multi-paragraph and SHALL name Steve Biddulph and the Source_Book at least once.
6. THE `description` for each New_Curriculum SHALL NOT use vague intensifiers (`very`, `really`, `super`, `incredibly`) more than twice in total.

### Requirement 10: contentTypeTags presence and value

**User Story:** As the platform's curriculum-loading code, I want the `contentTypeTags` field to always exist on every new curriculum's JSON, so that I never have to defend against a missing key.

#### Acceptance Criteria

1. THE Curriculum_Content_JSON for each New_Curriculum SHALL include a top-level `contentTypeTags` field.
2. THE `contentTypeTags` field for each New_Curriculum SHALL be an array, and its value SHALL be one of `[]`, `["movie"]`, `["music"]`, `["podcast"]`, or `["story"]`.
3. THE Spec_Author SHALL choose the `contentTypeTags` value for each New_Curriculum independently of whether the curriculum has a narrative-fiction frame, treating tag and frame as independent properties.

### Requirement 11: Privacy and lifecycle of newly created curriculums

**User Story:** As a content operator, I want the new curriculums to start private and stay private until generation is complete, so that learners never see half-rendered material.

#### Acceptance Criteria

1. THE Curriculum_Builder SHALL NOT call `curriculum/setPublic` with `isPublic: true` for either New_Curriculum during this spec.
2. WHEN the Curriculum_Builder calls `curriculum/create` for a New_Curriculum, THE Curriculum_Builder SHALL pass `language`, `userLanguage`, and `content` as top-level body params.
3. WHEN the Curriculum_Builder finishes creating a New_Curriculum, THE Spec_Author SHALL verify the curriculum's existence in Database via `curriculum.id` lookup before considering the creation step complete.
4. THE Spec_Author SHALL NOT delete any `create_*.py` script for either New_Curriculum until the corresponding curriculum row is confirmed present and non-deleted in Database.
5. IF a `create_*.py` script for a New_Curriculum has not yet been confirmed against Database, THEN THE Spec_Author SHALL prohibit deletion of that script outright, with no override path inside this spec.

### Requirement 12: Series and collection placement

**User Story:** As a catalogue curator, I want the two new curriculums to be organised in a way that respects language homogeneity rules and either creates a new en-en home or stays unhomed pending a decision, so that I never mix bilingual and single-language content under one parent.

#### Acceptance Criteria

1. THE Spec_Author SHALL NOT add either New_Curriculum to any existing series whose `curriculum_series_language_list` row indicates a language pair other than `language=en, userLanguage=en`.
2. THE Spec_Author SHALL NOT add either New_Curriculum to any existing collection whose `curriculum_collections_language_list` row indicates a language pair other than `language=en, userLanguage=en`.
3. WHERE the Spec_Author creates a new curriculum series to host both New_Curriculums, THE new series SHALL hold only en-en advanced curriculums and its `description` SHALL be ≤ 255 characters and SHALL use a Description_Tone that differs from each individual New_Curriculum headline tone (which is sufficient even when the two New_Curriculum tones happen to coincide).
4. WHERE no en-en parenting series or collection is created in this spec, THE Spec_Author SHALL leave both New_Curriculums unattached to any series or collection rather than force a misaligned parent.
5. THE Spec_Author SHALL NOT set `displayOrder` on any collection in this spec.

### Requirement 13: Description tone variety enforcement

**User Story:** As the description tone palette, I want all persuasive copy produced by this spec to obey the variety rules, so that the catalogue does not drift toward a single rhetorical default.

#### Acceptance Criteria

1. THE `description` ALL-CAPS headline of Curriculum_A and the `description` ALL-CAPS headline of Curriculum_B SHALL be assigned distinct Description_Tone values.
2. WHERE this spec also produces a series-level `description`, that headline SHALL be assigned a Description_Tone distinct from the tones used by Curriculum_A and Curriculum_B headlines.
3. WHEN counted across all `description` fields produced in this spec (the two curriculums plus any series and collection descriptions added by this spec), no single Description_Tone SHALL account for more than 30% of the batch.

### Requirement 14: Output verifiability and post-creation checks

**User Story:** As a reviewer, I want to be able to confirm that the deliverables of this spec actually exist and obey the rules, by querying Database directly without relying on script side-effects, so that "done" is observable.

#### Acceptance Criteria

1. THE Spec_Author SHALL provide, in the spec's downstream design or tasks document, a SQL query that locates each New_Curriculum by `language`, `user_language`, and `content->>'title'` from the `curriculum` table while excluding rows whose `uid` ends in `_deleted`.
2. THE Spec_Author SHALL provide, in the spec's downstream design or tasks document, a SQL query or check procedure that verifies each New_Curriculum's `difficultyTags` contains `"advanced"` and its `contentTypeTags` is a present array.
3. WHEN Database confirms both New_Curriculums exist and pass the language, level, and `contentTypeTags` checks, THE creation phase of this spec SHALL be considered complete.
4. IF Database query returns zero rows for a New_Curriculum after the Curriculum_Builder reports success, THEN THE Spec_Author SHALL treat the run as failed and SHALL re-run the creation script rather than proceed to deletion or publication.
