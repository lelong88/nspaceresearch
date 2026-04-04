# Giới Hạn Của Ngôn Ngữ (vi-en)

Simplified vi-en version of "The Limits of Language" (en-en advanced, ID `BuUXrnuaTxXI0wmS`).

## Curriculum

| Field | Value |
|---|---|
| ID | `VPkJNTNQ3C7WxpYO` |
| Language | en |
| User Language | vi |
| Level | intermediate |
| Sessions | 3 |
| Vocab | 8 words (vocabulary, dialect, fluent, express, vague, indirect, reserved, wordy) |

## Structure

- **Phần 1: Ngôn ngữ và Ý nghĩa** — vocabulary, dialect, fluent, express
- **Phần 2: Giao tiếp và Im lặng** — vague, indirect, reserved, wordy
- **Phần 3: Ôn tập & Đọc toàn bài** — all 8 words, full article, comprehensive writing

## SQL Queries

```sql
-- Find this curriculum
SELECT id, content->>'title' as title, language, user_language
FROM curriculum WHERE id = 'VPkJNTNQ3C7WxpYO';

-- Find the original en-en version
SELECT id, content->>'title' as title, language, user_language
FROM curriculum WHERE id = 'BuUXrnuaTxXI0wmS';
```

## Recreation

Based on the en-en "The Limits of Language" curriculum but simplified:
- 8 intermediate words instead of 10 advanced GRE words
- 3 sessions instead of 4
- All user-facing text in Vietnamese
- Same theme: how language shapes thought, language as power
- Reading passages written at intermediate level
