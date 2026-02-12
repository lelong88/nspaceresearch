# Listen & Answer with Image

AI generates a short audio segment (often bilingual) paired with a comprehension question. The correct answer is represented by an image, displayed alongside multiple distractor images. The learner taps the correct image. No text input, no speaking — pure listening comprehension with visual response.

This is a low-friction, exposure-first modality. It prioritizes enjoyment and repetition volume over deep skill-building. It complements higher-effort features like Dictation and Scene Reconstruction.

## Why it's novel
Most listening comprehension exercises require text output (typing an answer, selecting a text option). By replacing text with images, the feature removes L2 literacy as a barrier entirely. The learner's attention stays on audio processing, not on reading or spelling in L2.

## Why it's effective
- Removes production anxiety — no fear of mispronouncing or misspelling
- Dual coding (audio + image) strengthens vocabulary retention vs. audio alone
- High repetition volume — low effort per item means more items per session
- Accessible in contexts where speaking/typing isn't possible (commute, public spaces)
- Works especially well for beginners who lack the productive vocabulary to demonstrate comprehension through L2 output

## Limitations & Mitigations

### Shallow processing risk
The learner may latch onto a single keyword instead of processing the full utterance.

**Mitigation:** All distractor images must share the keyword's visual category. If the audio describes "a woman reading a newspaper on a bench," all four images should show a woman reading — but only one shows her on a bench with a newspaper. The discriminating detail must require understanding the full sentence.

### Limited to imageable content
Concrete nouns and actions are easy to depict. Abstract concepts (emotions, time relationships, conditional logic) are harder.

**Mitigation:** Use scene-based images that depict situations rather than isolated objects. "Disappointing" can be shown as a person opening an empty gift box. "Before the meeting" can be shown as a clock at 8:45 with people still arriving. This extends the feature into intermediate territory, though it has a natural ceiling.

### Inflated accuracy from guessing
With 4 images, random tapping scores 25%. Elimination strategies can push this higher without real comprehension.

**Mitigation:** Track response time alongside accuracy. A correct answer in <2 seconds with consistent patterns suggests comprehension. A correct answer after 8 seconds of hesitation suggests guessing. The system can also vary the number of options (3-6 images) to keep the guess rate unstable.

### Distractor quality is critical
Trivially different distractors (beach vs. calculator) make the task meaningless.

**Mitigation:** AI generates distractors that are semantically close to the correct answer. For "the children are playing soccer in the rain," distractors might be: children playing soccer in sunshine, children playing basketball in the rain, adults playing soccer in the rain. Each distractor matches part of the description but not all of it.

## How AI enables it
- LLM generates audio scripts with controlled vocabulary, ensuring the discriminating detail is distributed across the sentence (not front-loaded into one keyword)
- LLM generates distractor descriptions that overlap semantically with the correct answer, differing on exactly the detail being tested
- Image generation model produces the correct image and distractor images from these descriptions
- TTS produces bilingual audio calibrated to the learner's L1/L2 ratio
- LLM selects which vocabulary items and grammar structures to target based on the learner's curriculum

## Progress Tracking & Assessment

### 1. Keyword-vs-Full-Sentence Accuracy Split

The system tracks whether the learner is processing full sentences or just catching keywords, by comparing performance on keyword-sufficient vs. sentence-required items.

**Example** (Thai speaker learning English, travel curriculum):

Keyword-sufficient item:
> Audio: "Can you see the elephant?"
> Images: elephant, giraffe, lion, tiger.
> Learner picks elephant. Correct — but only required hearing one word.

Sentence-required item:
> Audio: "The woman in the blue jacket is waiting for the bus, not the train."
> Images: woman in blue jacket at bus stop, woman in red jacket at bus stop, woman in blue jacket at train platform, woman in blue jacket boarding a train.
> Learner must process color + location + negation.

The system reports both scores separately:
> "Keyword-level accuracy: 95%. Full-sentence accuracy: 58%. Your listening catches individual words well — now we're training you to process complete descriptions."

### 2. Vocabulary Exposure Tracker

Since this feature prioritizes exposure volume, the system tracks how many unique vocabulary items the learner has encountered and correctly associated with images.

**Example:**

> This week: 145 items attempted, 92 unique English words encountered.
> Correct on first exposure: 34%
> Correct after 3 exposures: 71%
> Correct after 5+ exposures: 89%

"You've been exposed to 420 unique English words through image listening. 312 are now recognized consistently."

### 3. Response Time Curve

As familiarity grows, response time should decrease. The system plots this per vocabulary item.

**Example:**

> "breakfast" — first encounter: 6.2s → latest: 1.1s ✓ Acquired
> "appointment" — first encounter: 7.8s → latest: 5.4s ◐ Developing
> "luggage" — first encounter: 8.1s → latest: 7.9s ✗ Not yet acquired

"3 words from your Travel English module still take over 5 seconds. Increasing their rotation frequency."

### 4. Comprehension Depth Progression

Over time, the system shifts the ratio from keyword-sufficient items to sentence-required items. The learner's ability to maintain accuracy as items get harder is the progress signal.

**Example:**

> Month 1: 80% keyword items, 20% sentence items. Overall accuracy: 85%.
> Month 2: 50% keyword, 50% sentence. Overall accuracy: 74%.
> Month 3: 30% keyword, 70% sentence. Overall accuracy: 72%.

"Your accuracy held steady even as we shifted to full-sentence items. You're processing more of the audio, not just catching keywords."
