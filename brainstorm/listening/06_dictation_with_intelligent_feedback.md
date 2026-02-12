# Dictation with Intelligent Feedback

AI plays a sentence; learner types or speaks it back. Instead of binary right/wrong, AI identifies the specific phonemic confusion (e.g., confusing /l/ and /r/, missing liaison in French) and generates follow-up drills targeting that exact gap.

## Why it's novel
Traditional dictation gives a score. This diagnoses the underlying perceptual error and immediately generates remediation. It turns a testing exercise into a diagnostic-and-treatment loop.

## Why it's effective
Dictation itself is a proven technique for developing listening accuracy. Adding phonemic diagnosis and targeted follow-up drills closes the feedback loop — the learner doesn't just know they got it wrong, they understand why and get immediate practice on the specific weak point.

## How AI enables it
- TTS generates sentences with controlled phonemic targets
- STT captures the learner's reproduction
- LLM performs error analysis: distinguishes spelling errors from phonemic confusions from grammar gaps
- LLM generates targeted minimal-pair or phonemic drills on the fly based on diagnosed errors

## Progress Tracking & Assessment

Every dictation attempt produces a classified error. Progress is tracked as error patterns being resolved over time.

### 1. Error Category Tracking

Errors are classified into categories. The system tracks each category's frequency across sessions.

**Example** (Mandarin speaker learning English, general curriculum):

Session 1 error breakdown (20 sentences):
> - Consonant confusion: 14 (e.g., wrote "sink" when audio said "think," wrote "rice" when audio said "lice")
> - Final consonant deletion: 4 (e.g., wrote "worl" for "world," "han" for "hand")
> - Vowel confusion: 2 (e.g., wrote "ship" when audio said "sheep")

Session 10 error breakdown (20 sentences):
> - Consonant confusion: 6
> - Final consonant deletion: 1
> - Vowel confusion: 3 (increased because sentence complexity introduced more minimal pairs)

"th/s distinction: 30% → 70%. Final consonants: 80% → 95%. New focus: vowel length distinction."

### 2. Phonemic Confusion Pairs

The system builds a personal confusion matrix — which specific sounds the learner mixes up.

**Example:**

> l/r confusion: 12 errors across 8 sessions → 2 errors in last 3 sessions ✓ Resolving
> th/s confusion: 8 errors across 8 sessions → 7 errors in last 3 sessions ✗ Persistent
> v/w confusion: 22 errors across 8 sessions → 18 errors in last 3 sessions ✗ Persistent

"Your l/r distinction is nearly resolved. th/s and v/w remain active issues. Today's drills will focus on these."

### 3. Sentence Complexity Ladder

As error rates drop, sentence length and speed increase. The system tracks what complexity level the learner can dictate accurately.

**Example:**

> Level 1: 3-word phrases at 0.7x speed — 92% accuracy ✓
> Level 2: Simple sentences (5-7 words) at 0.8x speed — 85% accuracy ✓
> Level 3: Compound sentences (10-12 words) at 0.9x speed — 64% accuracy ← current
> Level 4: Complex sentences (15+ words) at native speed — locked

"You're on Level 3. Hit 80% accuracy to unlock Level 4."
