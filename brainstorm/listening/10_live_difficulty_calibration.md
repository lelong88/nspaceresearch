# Live Difficulty Calibration

Across all listening activities, AI continuously adjusts speech rate, vocabulary density, sentence complexity, and background noise level based on real-time comprehension scores — keeping the learner in the optimal challenge zone.

## Why it's novel
Most apps offer discrete difficulty levels (beginner, intermediate, advanced). This is a continuous, multi-dimensional adjustment happening in real time within a single session, across multiple parameters simultaneously.

## Why it's effective
Krashen's i+1 hypothesis and flow theory both point to the same principle: learning is maximized when challenge slightly exceeds current ability. Continuous calibration maintains this zone far more precisely than coarse difficulty levels, preventing both boredom and frustration.

## How AI enables it
- System maintains a multi-dimensional learner model (speech rate tolerance, vocabulary level, syntactic complexity threshold, noise tolerance)
- Each listening interaction updates the model based on comprehension performance
- TTS and LLM adjust generation parameters in real time: speed, word choice, sentence length, and even ambient noise mixing
- This operates as a cross-cutting concern across all other listening features, not a standalone activity

## Progress Tracking & Assessment

The calibration parameters themselves are the progress data. As the learner improves, the system raises each parameter — and the learner can see it.

### 1. Multi-Dimensional Learner Profile

The system maintains a radar chart of the learner's current tolerance levels across all parameters.

**Example** (Arabic speaker learning English, media curriculum):

Current profile:
> - Speech rate tolerance: 72% of native English speed
> - Vocabulary density: B1 level (can handle ~2 unknown words per minute)
> - Sentence complexity: compound sentences, not yet complex/nested
> - Noise tolerance: clean audio only (drops 40% accuracy with background noise)

4 weeks later:
> - Speech rate tolerance: 72% → 85% of native speed
> - Vocabulary density: B1 → B1+ (handles ~3 unknown words per minute)
> - Sentence complexity: compound → complex with relative clauses
> - Noise tolerance: clean → mild café noise (15% accuracy drop)

The learner sees: "Your English listening profile has improved in all 4 dimensions. Biggest gain: speech rate (+13%). Smallest gain: noise tolerance (+10%)."

### 2. Comfort Zone vs. Challenge Zone Ratio

The system tracks what percentage of each session the learner spends in their comfort zone vs. challenge zone (where errors occur but learning happens).

**Example:**

> Session on March 5: 80% comfort zone, 20% challenge zone — "This session was too easy. Raising parameters."
> Session on March 7: 45% comfort zone, 55% challenge zone — "Good balance. Optimal learning conditions."
> Session on March 9: 20% comfort zone, 80% challenge zone — "Overloaded. Pulling parameters back slightly."

"Your last 10 sessions averaged 50/50 comfort-to-challenge. This is the target zone."

### 3. Cross-Feature Difficulty Snapshot

Since this system operates across all features, it provides a unified view of where difficulty stands in each one.

**Example:**

> | Feature | Current Difficulty Level | Trend |
> |---|---|---|
> | Shadowing | 0.8x speed, short phrases | ↑ Rising |
> | Listening Cloze | Tier 2, medium predictability | → Stable |
> | Micro-Podcasts | 25% L1 / 75% English | ↑ Rising |
> | Scene Reconstruction | 60-second scenes, 2 characters | → Stable |
> | Dictation | Level 3, compound sentences | ↓ Pulled back |

"Dictation difficulty was pulled back this week after a spike in consonant cluster errors. All other features are progressing or stable."
