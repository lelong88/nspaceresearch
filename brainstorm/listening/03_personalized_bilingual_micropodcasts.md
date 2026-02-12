# Personalized Bilingual Micro-Podcasts

AI generates short (2-5 min) podcast episodes that interleave L1 and L2, calibrated to the learner's level. Topics align with their curriculum domain (e.g., healthcare conversations, legal proceedings). Each episode introduces a controlled number of new items.

## Why it's novel
Existing bilingual podcasts are generic, pre-recorded, and not personalized. These are generated on-demand to match the learner's exact curriculum, level, domain, and vocabulary targets — a unique episode every time.

## Why it's effective
Bilingual interleaving provides built-in comprehension scaffolding without requiring the learner to pause and look things up. Domain alignment means the learner acquires vocabulary they'll actually use. Controlled new-item density prevents cognitive overload.

## How AI enables it
- LLM generates scripts that weave L1/L2 naturally, respecting the learner's current vocabulary and introducing new items at a controlled rate
- LLM tailors topic and register to the learner's curriculum domain
- TTS produces natural multi-voice audio with appropriate L1/L2 pronunciation
- Content is unique per generation — infinite variety, no repetition fatigue

## Progress Tracking & Assessment

Passive listening alone provides no feedback loop. The following mechanisms add assessment without destroying the low-friction podcast feel.

### 1. Inline Comprehension Checks

After each episode, 2-3 quick questions test whether key content landed. Accuracy drives the next episode's difficulty.

**Example** (Spanish speaker learning English, hospitality curriculum):

The episode is a 3-minute podcast about a guest complaining about their hotel room. After it ends:

- "What was wrong with the guest's room?" (open-ended, spoken in English)
- "The guest said 'the air conditioning is out of order' — what does 'out of order' mean?" (recognition)
- "How did the receptionist offer to fix it?" (inference)

Score 3/3: next episode introduces 5 new items. Score 1/3: next episode reuses 3 of the same items in a different scenario (a different guest, same vocabulary).

### 2. Gradual L1 Withdrawal

The system starts with heavy L1 scaffolding and progressively reduces it as the learner demonstrates comprehension. The L1/L2 ratio itself becomes the visible progress metric.

**Example:**

Week 1 episode (heavy L1 — Spanish):
> "El huésped llamó — called the front desk — para decir que su habitación — his room was too noisy. La recepcionista — the receptionist — le ofreció cambiarlo — offered to move him to a quieter floor."

Week 3 episode (reduced L1):
> "The guest called the front desk para decir que his room was too noisy. The receptionist offered to move him a un piso más tranquilo — a quieter floor."

Week 6 episode (near full L2 — English):
> "The guest called the front desk to complain that his room was too noisy. The receptionist offered to move him to a quieter floor on a higher level."

The learner sees their L1/L2 ratio on a simple progress bar: "You started at 70% Spanish. You're now at 15% Spanish."

### 3. Recall Prompts

Between episodes, the system resurfaces vocabulary from previous episodes using spaced repetition.

**Example:**

Tuesday's episode introduced "front desk," "out of order," and "air conditioning." On Thursday, before the new episode plays:

> "Before today's episode — quick check. What does 'front desk' mean?"
> (learner answers)
> "And what does 'out of order' mean?"
> (learner answers)

Got both: move on. Missed one: that item gets woven into today's episode again. Missed both: today's episode is a remix of Tuesday's content in a new scenario (a restaurant instead of a hotel, but same target vocabulary).

### 4. Comprehension-Gated Progression

New curriculum content only unlocks when the learner demonstrates they absorbed the previous episode.

**Example:**

The curriculum plan is:
- Episode 1-2: Check-in vocabulary
- Episode 3-4: Room complaint vocabulary
- Episode 5-6: Restaurant service vocabulary

The learner finishes Episode 2 but scores poorly on check-in vocab comprehension checks. Episode 3 does not advance to room complaints. Instead, the system generates Episode 2b — a different check-in scenario (a family arriving vs. a business traveler) reusing the same English target vocabulary:

> "Module: Check-in — 60% mastered (3 of 5 key phrases). Generating a new practice episode."

Only when they hit the threshold (e.g., 80%) does Episode 3 unlock.
