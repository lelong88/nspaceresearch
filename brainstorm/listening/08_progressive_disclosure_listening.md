# Progressive Disclosure Listening

The same audio clip is played multiple times. First pass: learner answers gist questions. Second pass: detail questions. Third pass: linguistic analysis (why did the speaker use that tense?). Mirrors how listening proficiency actually develops.

## Why it's novel
Traditional exercises play audio once or twice with all questions presented together. This structures repeated listening with escalating cognitive demands, turning a single clip into a multi-layered learning sequence.

## Why it's effective
Mirrors the natural progression of listening skill development: gist before detail, detail before analysis. Each pass builds on the previous one, deepening processing without overwhelming the learner. The linguistic analysis pass builds metalinguistic awareness that accelerates future comprehension.

## How AI enables it
- LLM generates or selects content rich enough to support three layers of questioning
- LLM produces questions at each tier (gist, detail, linguistic analysis) calibrated to the learner's level
- LLM evaluates responses at each tier and adjusts subsequent questions based on what the learner demonstrated understanding of
- System decides whether additional passes are needed or if the learner can move on

## Progress Tracking & Assessment

Progress is measured by how deep the learner can go in fewer passes, and which tier is their ceiling.

### 1. Pass Efficiency Tracking

The system records how many passes the learner needs before answering correctly at each tier.

**Example** (Italian speaker learning English, art history curriculum):

An English clip about the restoration of a Renaissance fresco.

> Pass 1 (gist): "What is the clip about?" — Learner: "Restoring an old painting in a church." ✓ First pass.
> Pass 2 (detail): "What technique did the restorer say was most controversial?" — Learner: "I'm not sure, something about cleaning chemicals?" ✗ Partial.
> Pass 3 (detail retry): Same question — Learner: "Using solvents to remove the dark varnish layer." ✓ Second pass.
> Pass 4 (linguistic): "The restorer said 'had it not been for the donors, the project would have collapsed.' Why did she use 'had it not been' instead of 'if it wasn't'?" — Learner: "It's more formal, and it's talking about something unreal — a hypothetical past." ✓ First pass.

Score: Gist 1 pass, Detail 2 passes, Linguistic 1 pass.

Over time: "Your average passes needed: Gist 1.0 → 1.0 (stable). Detail 2.4 → 1.6 (improving). Linguistic 1.8 → 1.4 (improving)."

### 2. Tier Ceiling Progression

The system tracks the highest tier the learner can answer on first listen.

**Example:**

> Month 1: Reliably answers gist on first listen. Detail requires 2-3 passes. Cannot attempt linguistic tier.
> Month 3: Answers gist + detail on first listen. Linguistic tier requires 2 passes.
> Month 5: Answers all three tiers on first listen for familiar topics. Still needs 2 passes on linguistic tier for unfamiliar topics.

"Your tier ceiling: Detail (first listen). Linguistic tier on first listen is your next milestone."

### 3. Topic-Dependent Performance

The system identifies which topics the learner comprehends deeply vs. superficially.

**Example:**

> Art history clips: Gist 100%, Detail 85%, Linguistic 60%
> Architecture clips: Gist 100%, Detail 70%, Linguistic 30%
> Music theory clips: Gist 90%, Detail 45%, Linguistic 10%

"Your detail comprehension drops significantly on music theory. This suggests missing domain vocabulary — adding music terminology to your flashcard queue."
