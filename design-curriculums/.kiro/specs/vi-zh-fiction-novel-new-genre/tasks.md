# Tasks

## Task 1: Write the original Chinese mystery novel (10 chapters)

- [x] 1.1 Choose a mystery novel concept, characters, and overarching plot arc — entirely different from "味道的记忆" (culinary) and "The Little Bookshop by the Sea" (coastal bookshop) and "The Silent Clocktower" (en-en mystery)
- [x] 1.2 Select 150 HSK2-3 vocabulary words (15 per chapter) with at most 2 shared words between any two chapters
- [x] 1.3 Write Chapter 1 text: 5 reading passages (~100-150 Chinese characters each), each passage using 3 of the chapter's vocab words
- [x] 1.4 Write Chapter 2 text following the same structure
- [x] 1.5 Write Chapter 3 text following the same structure
- [x] 1.6 Write Chapter 4 text following the same structure
- [x] 1.7 Write Chapter 5 text following the same structure
- [x] 1.8 Write Chapter 6 text following the same structure
- [x] 1.9 Write Chapter 7 text following the same structure
- [x] 1.10 Write Chapter 8 text following the same structure
- [x] 1.11 Write Chapter 9 text following the same structure
- [x] 1.12 Write Chapter 10 text following the same structure

## Task 2: Create content modules (`chapter{N}_content.py`)

- [x] 2.1 Create `original-novels/vi-zh-mystery-novel/chapter1_content.py` with bilingual title, Vietnamese description, Vietnamese preview (~150 words), and 6 learning sessions (sessions 1-5: viewFlashcards(3 words, audioSpeed -0.2) + reading(passage, audioSpeed -0.2) + readAlong(same passage); session 6: viewFlashcards(all 15 words, audioSpeed -0.2) + readAlong(full chapter text))
- [x] 2.2 Create `chapter2_content.py` following the same structure
- [x] 2.3 Create `chapter3_content.py` following the same structure
- [x] 2.4 Create `chapter4_content.py` following the same structure
- [x] 2.5 Create `chapter5_content.py` following the same structure
- [x] 2.6 Create `chapter6_content.py` following the same structure
- [x] 2.7 Create `chapter7_content.py` following the same structure
- [x] 2.8 Create `chapter8_content.py` following the same structure
- [x] 2.9 Create `chapter9_content.py` following the same structure
- [x] 2.10 Create `chapter10_content.py` following the same structure

## Task 3: Create validation script

- [x] 3.1 Create `original-novels/vi-zh-mystery-novel/validate_content.py` that imports all 10 content modules and checks all 12 correctness properties: (P1) session structure, (P2) activity fields/audioSpeed, (P3) vocab count 15/chapter and 3/session, (P4) readAlong==reading text, (P5) session 6 concatenation, (P6) session 6 vocab union, (P7) cross-chapter overlap ≤ 2, (P8) passage length 80-180 chars, (P9) vocab in passages, (P10) title format + no level, (P11) preview 100-200 words + Vietnamese metadata, (P12) no strip keys
- [x] 3.2 Run `validate_content.py` and fix any content errors until all 10 chapters pass

## Task 4: Create the creation and organization script

- [x] 4.1 Create `original-novels/vi-zh-mystery-novel/create_all_chapters.py` that: (a) authenticates via firebase_token with UID zs5AMpVfqkcfDf8CJ9qrXdH58d73, (b) imports and uploads all 10 chapters via POST /curriculum/create with language="zh", userLanguage="vi", (c) creates a series with bilingual vi-zh title via POST /curriculum-series/create, (d) adds all 10 curriculums to the series via POST /curriculum-series/addCurriculum, (e) checks that existing collection 7nf5wi1d is accessible via curriculum-collection/listAll — does NOT create a new collection, (f) adds series to existing collection via POST /curriculum-collection/addSeriesToCollection, (g) sets display orders 1-10 via POST /curriculum/setDisplayOrder

## Task 5: Upload and organize

- [ ] 5.1 Run `create_all_chapters.py` to upload all 10 chapter curriculums, create series, attach to existing collection, and set display orders
- [ ] 5.2 Verify all 10 curriculums appear correctly in the series with correct display orders

## Task 6: Cleanup and documentation

- [ ] 6.1 Create `README.md` in `original-novels/vi-zh-mystery-novel/` with: how content was created, Series ID, Collection ID (7nf5wi1d), SQL queries to find curriculums, novel summary for recreation
- [ ] 6.2 Delete all source material files (chapter content modules, creation script, validation script) — retain only README.md
