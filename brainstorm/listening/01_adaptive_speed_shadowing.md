# Adaptive Speed Shadowing

AI generates native-speed audio, then creates a version that dynamically slows down only on segments the learner struggles with (detected via their speech-to-text responses). Over sessions, the slow segments gradually speed up as proficiency improves.

## Why it's novel
Traditional shadowing uses uniform speed control. This targets deceleration precisely where the learner needs it, creating a personalized speed profile per learner per content.

## Why it's effective
Shadowing is already an evidence-backed technique. Adaptive speed removes the frustration of uniform fast audio while avoiding the artificial feel of uniformly slow audio. The learner stays in the optimal challenge zone.

## How AI enables it
- TTS generates audio at arbitrary speeds per segment
- STT analyzes learner's reproduction to detect struggle points (mispronunciations, hesitations, omissions)
- Model tracks per-segment proficiency and adjusts speed curve over time

## Progress Tracking & Assessment

The system's speed adjustments are themselves the progress data. As the learner improves, fewer segments need deceleration.

### 1. Per-Segment Speed Profile

The system maintains a speed map for each phrase the learner shadows. Progress is visible as the map shifts toward native speed.

**Example** (Japanese speaker learning English, business curriculum):

The learner shadows a sentence: "We need to reschedule the quarterly review meeting."

Session 1 speed profile:
> - "We need to" — 100% speed (no issues)
> - "reschedule" — 55% speed (struggled with /ʃ/ cluster, said "re-sked-yool")
> - "the quarterly" — 60% speed (dropped the /r/ in quarterly, hesitated on "the")
> - "review meeting" — 80% speed (slight /v/ → /b/ substitution)

Session 5 speed profile:
> - "We need to" — 100% speed
> - "reschedule" — 80% speed (still slight hesitation on /sk/ → /ʃ/ transition)
> - "the quarterly" — 90% speed (improving)
> - "review meeting" — 100% speed

The learner sees: "Average shadowing speed: 74% → 93% of native. 2 of 4 segments at full speed."

### 2. Struggle Pattern Dashboard

The system aggregates struggle points across sessions to surface systemic weaknesses, not just per-sentence scores.

**Example:**

After 20 sessions, the system identifies:
> "You consistently slow down on words with consonant clusters: 'strengths,' 'schedule,' 'restructure.' Your accuracy on cluster words is 45% vs. 82% on other segments."

It then generates shadowing exercises specifically loaded with consonant-cluster-heavy business English phrases.

### 3. Native-Speed Graduation

A sentence is "graduated" when the learner shadows it at 95%+ native speed with acceptable pronunciation three sessions in a row.

**Example:**

> "Graduated phrases this week: 12. Total graduated: 87 of 120 in your Business English curriculum. Next milestone: 100 phrases."
