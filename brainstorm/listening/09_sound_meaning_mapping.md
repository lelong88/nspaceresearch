# Sound-Meaning Mapping Drills

For tonal languages or languages with sounds absent in L1, AI generates minimal-pair audio drills embedded in meaningful sentences — not isolated syllables. The learner must distinguish meaning from sound in context, which transfers better than lab-style pair drills.

## Why it's novel
Minimal-pair training traditionally uses isolated words or syllables in a lab setting. Embedding pairs in meaningful sentences forces the learner to use both acoustic and contextual cues together, which is how real listening works.

## Why it's effective
Research shows that phonemic perception training transfers better when done in context rather than in isolation. Meaningful sentences provide the semantic scaffold that helps the brain anchor new sound categories to actual communication rather than abstract auditory patterns.

## How AI enables it
- LLM generates sentence pairs where a single phonemic distinction changes the meaning, ensuring both sentences are natural and contextually plausible
- TTS produces audio with precise phonemic control
- LLM calibrates to the learner's L1-L2 pair, targeting the specific sound confusions known to affect that language combination
- System tracks which contrasts the learner has acquired and which remain difficult

## Progress Tracking & Assessment

Each drill is a binary signal: did the learner distinguish the contrast or not? Progress is tracked per phonemic contrast.

### 1. Contrast Acquisition Map

The system maintains a list of all target phonemic contrasts for the learner's L1-L2 pair and tracks mastery of each.

**Example** (Japanese speaker learning English, general curriculum):

English has phonemic contrasts absent in Japanese. Key contrasts for Japanese speakers:

> | Contrast | Accuracy | Status |
> |---|---|---|
> | /l/ vs. /r/ (light vs. right) | 78% | ◐ Developing |
> | /b/ vs. /v/ (berry vs. very) | 72% | ◐ Developing |
> | /s/ vs. /θ/ (sink vs. think) | 45% | ✗ Not acquired |
> | /æ/ vs. /ʌ/ (bat vs. but) | 40% | ✗ Not acquired |

"2 of 4 critical contrasts developing. 0 fully acquired. Focus today: /s/ vs. /θ/."

### 2. In-Context vs. Isolated Accuracy

The system tests the same contrast both in isolation and in sentences, revealing whether the learner can transfer.

**Example:**

> "light" vs. "right":
> - Isolated word pair: 85% accuracy
> - In sentence ("Turn on the ___ / Turn to the ___"): 55% accuracy

"You can hear the light/right contrast in isolation but lose it in running speech. Generating more sentence-level drills for this pair."

### 3. Acquisition Curve

The system plots accuracy over time for each contrast, showing the learning trajectory.

**Example:**

/s/ vs. /θ/ accuracy over 4 weeks:
> Week 1: 52% (near chance level for 2-choice)
> Week 2: 60%
> Week 3: 70%
> Week 4: 58% (regression after introducing new vocabulary like "thought" vs. "sought")

"This contrast is developing but not yet stable. The dip in week 4 is normal — new vocabulary temporarily competes for attention. Continuing drills."
