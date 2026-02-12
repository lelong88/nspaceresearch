# Listening Features — Summary Matrix

| # | Feature | Beginner | Technical Complexity | Per-Session AI Cost | TTS Quality Dep. | STT Quality Dep. | User Engagement | Learning Effectiveness | Novelty vs Competitors | Language Universality |
|---|---------|----------|---------------------|---------------------|-------------------|-------------------|-----------------|----------------------|----------------------|----------------------|
| 03 | Personalized Bilingual Micro-Podcasts | 🟢 | 🟡 | 🔴 | 🔴 | 🟢 | 🟢 | 🟡 | 🟢 | 🟢 |
| 08 | Progressive Disclosure Listening | 🟢 | 🟢 | 🟢 | 🟡 | 🟢 | 🟡 | 🟢 | 🟡 | 🟢 |
| 09 | Sound-Meaning Mapping | 🟢 | 🔴 | 🟡 | 🔴 | 🟡 | 🔴 | 🟢 | 🟡 | 🔴 |
| 10 | Live Difficulty Calibration | 🟢 | 🔴 | 🟢 | 🟡 | 🟡 | 🟢 | 🟢 | 🟢 | 🟢 |
| 01 | Adaptive Speed Shadowing | 🟡 | 🔴 | 🟡 | 🔴 | 🔴 | 🟡 | 🟢 | 🟢 | 🟢 |
| 02 | Contextual Listening Cloze | 🟡 | 🟡 | 🟡 | 🟡 | 🟢 | 🟡 | 🟢 | 🟡 | 🟢 |
| 06 | Dictation with Intelligent Feedback | 🟡 | 🔴 | 🟡 | 🟡 | 🔴 | 🟡 | 🟢 | 🟡 | 🟢 |
| 04 | Scene Reconstruction | 🔴 | 🟡 | 🟡 | 🟡 | 🔴 | 🟢 | 🟢 | 🟡 | 🟢 |
| 05 | Accent & Register Variation | 🔴 | 🔴 | 🔴 | 🔴 | 🟢 | 🟡 | 🟢 | 🟢 | 🟡 |
| 07 | Conversation Eavesdrop | 🔴 | 🟡 | 🔴 | 🔴 | 🟢 | 🟢 | 🟢 | 🟢 | 🟢 |

## Dimension Definitions

- **Technical Complexity**: Engineering effort to build — models, pipelines, tracking systems
- **Per-Session AI Cost**: LLM/TTS/STT inference spend per user session
- **TTS Quality Dependency**: How much the feature's value degrades with mediocre TTS (accent control, speed granularity, naturalness)
- **STT Quality Dependency**: How much the feature relies on accurate speech recognition from the learner
- **User Engagement**: How enjoyable/sticky the feature is — willingness to return
- **Learning Effectiveness**: Pedagogical impact backed by language acquisition research
- **Novelty vs Competitors**: Differentiation from Duolingo, Babbel, Pimsleur, etc.
- **Language Universality**: Whether the feature works well across all language pairs (Low = tied to specific language properties like tones or specific phonemic gaps)
- **Suitable for Beginner**: Whether the feature is accessible and valuable at A0–A1 level (Low = requires intermediate+ proficiency to be usable)

## Quick Reads

**Lowest barrier to ship**: #08 Progressive Disclosure Listening — low complexity, low cost, high effectiveness

**Highest engagement**: #03 Micro-Podcasts, #04 Scene Reconstruction, #07 Eavesdrop — narrative/passive formats users gravitate toward

**Most differentiated**: #01 Adaptive Speed Shadowing, #05 Accent Variation, #07 Eavesdrop, #10 Live Calibration — hard to replicate without generative AI

**Infrastructure investment**: #10 Live Difficulty Calibration is high complexity but pays dividends across all other features as a cross-cutting system

**Language-specific considerations**: #09 Sound-Meaning Mapping is most valuable for tonal languages and distant L1-L2 pairs; #05 Accent Variation depends on TTS accent coverage per language
