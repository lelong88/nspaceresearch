# Scene Reconstruction

AI plays a dialogue or narration, then asks the learner open-ended comprehension questions — not multiple choice, but "describe what happened" in L2. AI evaluates the response for both comprehension accuracy and language production.

## Why it's novel
Traditional listening comprehension uses multiple-choice or true/false, which can be gamed and only test recognition. This requires free production, testing both receptive and productive skills simultaneously.

## Why it's effective
Retelling activates deeper encoding than passive recognition. Evaluating both comprehension and production in one task is highly efficient. The open-ended format reveals specific gaps (did they miss a detail? or understand it but lack the vocabulary to express it?).

## How AI enables it
- LLM generates rich, narratively coherent scenes with clear factual content to verify comprehension
- TTS delivers the scene as natural audio
- STT captures the learner's retelling
- LLM evaluates the retelling on two axes: factual accuracy (comprehension) and linguistic quality (production), providing targeted feedback on each

## Progress Tracking & Assessment

Every retelling is evaluated on two independent axes — comprehension and production — making it easy to see which skill is lagging.

### 1. Dual-Axis Scoring

Each retelling gets two scores. Progress on each axis is tracked independently.

**Example** (Korean speaker learning English, daily life curriculum):

Scene: An English narration about a woman returning a defective laptop at an electronics store.

Learner's retelling (in English): "The woman go to store. Computer is break. She want money back. The worker say no, then say yes."

> Comprehension score: 4/5 — captured the main conflict and resolution, missed that the manager (not the employee) approved the refund.
> Production score: 2/5 — used basic sentence structures only, no connectors, missing past tense ("go" instead of "went," "is break" instead of "was broken"), avoided the word "refund" and used a workaround ("money back").

The learner sees: "Comprehension: ████░ 80%. Production: ██░░░ 40%."

### 2. Gap Diagnosis

The system distinguishes "understood but couldn't say it" from "didn't catch it at all."

**Example:**

After the retelling above, the system probes:
> "You didn't use the word 'refund.' Did you hear it in the audio but not know how to say it, or did you miss that part?"

If the learner says "I heard it but forgot the word" — it's a production gap. "Refund" goes into active vocabulary practice.

If the learner says "I didn't catch that part" — it's a comprehension gap. The next scene replays similar transactional vocabulary at slightly slower speed.

### 3. Complexity Progression

As comprehension scores stay high, scenes get longer and more complex. The system tracks what scene complexity the learner can handle.

**Example:**

> Month 1: 30-second scenes, 2 characters, 1 event. Avg comprehension: 85%.
> Month 2: 60-second scenes, 2 characters, 2-3 events. Avg comprehension: 78%.
> Month 3: 90-second scenes, 3 characters, subplot. Avg comprehension: 72%.

"Scene complexity level: 3 of 5. You're handling multi-event narratives with 70%+ comprehension."
