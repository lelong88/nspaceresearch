# Luyện Thi IELTS: Từ Vựng Học Thuật

## Series
- ID: `bapehjcu`
- Title: Luyện Thi IELTS: Từ Vựng Học Thuật
- Language: vi-en, Level: intermediate
- Target: Vietnamese learners aiming for IELTS 4.5–5.5
- Public: yes
- Collection: Học Từ Vựng Theo Chủ Đề (`279d6843`)

## Curriculums (8 total, 18 vocab words each = 144 words)

| # | ID | Title | Vocab (Session 1 / 2 / 3) |
|---|---|---|---|
| 1 | `bLgmNfiE58a9sQ8h` | Education Systems – Hệ Thống Giáo Dục Toàn Cầu | curriculum, assessment, compulsory, literacy, enroll, tuition / scholarship, vocational, discipline, qualification, semester, lecture / graduate, pedagogy, dropout, standardized, extracurricular, inclusive |
| 2 | `mNxSkDJPLlU2HyTa` | Urbanization & City Life – Đô Thị Hóa | urbanization, infrastructure, congestion, suburb, population density, migrate / affordable, commute, pollution, zoning, renovation, municipal / sustainable, gentrification, pedestrian, public transit, slum, metropolitan |
| 3 | `P315PuGnubhSEQdC` | Health & Medicine – Sức Khỏe | diagnosis, symptom, chronic, immune system, prescription, therapy / mental health, obesity, vaccine, hygiene, nutrition, epidemic / life expectancy, preventive, rehabilitation, clinical trial, side effect, well-being |
| 4 | `8cxXMVyw9pKTWcj1` | Technology & Society – Công Nghệ | innovation, artificial intelligence, automation, digital, algorithm, data / privacy, cybersecurity, social media, screen time, misinformation, surveillance / bandwidth, obsolete, virtual reality, biotechnology, ethical, disruptive |
| 5 | `zuUTnQzx0eKxusAW` | Environment & Climate – Môi Trường | climate change, greenhouse gas, carbon footprint, fossil fuel, emission, global warming / renewable energy, deforestation, biodiversity, ecosystem, conservation, endangered / drought, flood, recycle, sustainable development, carbon neutral, habitat |
| 6 | `XJo0bOWZ1uGasKxG` | Work & Employment – Việc Làm | unemployment, salary, recruitment, resume, interview, career / freelance, remote work, minimum wage, labor market, promotion, retire / workforce, outsource, internship, job satisfaction, gender gap, trade union |
| 7 | `80toVXqfJFUjQgHX` | Tourism & Culture – Du Lịch | tourism, destination, heritage, souvenir, hospitality, itinerary / ecotourism, accommodation, customs, cuisine, landmark, visa / overtourism, cultural exchange, indigenous, preservation, pilgrim, backpacker |
| 8 | `Fo09rPMmLCnszOyF` | Food & Agriculture – Nông Nghiệp | agriculture, crop, harvest, irrigation, fertile, livestock / organic, pesticide, genetically modified, food security, famine, subsidy / aquaculture, supply chain, food waste, arable, monoculture, food sovereignty |

## Find in DB
```sql
-- Series
SELECT * FROM curriculum_series WHERE id = 'bapehjcu';

-- All curriculums in series
SELECT c.id, c.content->>'title' as title, c.display_order, cat.overall_level
FROM curriculum_series_items csi
JOIN curriculum c ON c.id = csi.curriculum_id
LEFT JOIN curriculum_all_tags cat ON c.id = cat.id
WHERE csi.curriculum_series_id = 'bapehjcu'
ORDER BY c.display_order;
```

## How it was created
Each curriculum follows the 5-session pattern (matching Health & Wellness series):
- Sessions 1-3: Learn 6 words each + grammar + short IELTS-style reading passage + writing
- Session 4: Review all 18 words (flashcards + vocab drills)
- Session 5: Full article reading + comprehensive farewell

Reading passages are written in IELTS Academic Reading style — factual, multi-paragraph, accessible at intermediate level. Vietnamese user-facing text, English reading passages. Content was generated via `ielts_vi_curriculum_*.py` scripts (deleted after import). Full content recoverable via `curriculum/getOne` or MCP postgres.
