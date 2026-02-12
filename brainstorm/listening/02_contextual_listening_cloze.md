# Contextual Listening Cloze

AI generates natural dialogues or monologues but strategically mutes target vocabulary or grammar patterns. The learner must identify the missing word purely from audio context. Difficulty scales by muting more predictable words first, then less predictable ones.

## Why it's novel
Traditional listening cloze is done on paper with written transcripts. This is purely auditory — the learner never sees text, forcing genuine listening comprehension rather than reading-assisted guessing.

## Why it's effective
Forces active prediction and deep processing of audio input. Predictability-based difficulty scaling aligns with how natural language processing works in the brain (high-frequency collocations are easier to predict than rare word choices).

## How AI enables it
- LLM generates contextually rich audio scripts with controlled vocabulary targets
- LLM scores each target word's predictability in context to sequence difficulty
- TTS produces audio with precise muting of target segments
- LLM evaluates learner's spoken or typed answers with tolerance for synonyms and near-matches

## Progress Tracking & Assessment

Every cloze answer is a data point. The system tracks accuracy across predictability levels to measure listening depth.

### 1. Predictability Tier Progression

Each muted word has a predictability score. Progress means accurately filling in less predictable words.

**Example** (Vietnamese speaker learning English, culinary curriculum):

Tier 1 — High predictability (collocations):
> Audio: "The chef added salt and ___" (pepper)
> Most learners get this — "salt and pepper" is a fixed pair.

Tier 2 — Medium predictability (contextual inference):
> Audio: "You need to let the sauce simmer for at least ___" (twenty minutes)
> Requires understanding the cooking context to guess a reasonable duration.

Tier 3 — Low predictability (precise recall):
> Audio: "The restaurant's signature dish is called ___" (The Golden Garden)
> Only gettable if the learner was closely tracking details from earlier in the audio.

The learner sees: "Tier 1: 95%. Tier 2: 68%. Tier 3: 30%. Focus area: contextual inference."

### 2. Vocabulary Domain Accuracy Map

The system tracks cloze accuracy broken down by vocabulary domain within the curriculum.

**Example:**

> Cooking verbs (simmer, dice, whisk): 80% accuracy
> Ingredients (shallot, chive, saffron): 55% accuracy
> Kitchen equipment (colander, skillet, rolling pin): 35% accuracy

The next session loads more equipment vocabulary into the cloze targets.

### 3. Speed-Accuracy Tradeoff

As the learner improves, the system shortens the response window. Progress is measured as maintaining accuracy under tighter time pressure.

**Example:**

> Week 1: 8-second response window, 70% accuracy
> Week 3: 5-second response window, 72% accuracy
> Week 6: 3-second response window, 68% accuracy

"Your response speed has improved 2.5x while maintaining accuracy. You're processing audio in near real-time."
