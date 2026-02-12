# Accent & Register Variation Training

For the same content, AI generates audio in multiple accents, speeds, and registers (formal, casual, slang). The learner practices comprehension across variation, addressing a known weakness in traditional listening curricula that typically use one clean studio voice.

## Why it's novel
Language courses overwhelmingly use a single "standard" accent and formal register. Real-world listening requires handling variation. AI can generate the same semantic content across a matrix of accent/speed/register combinations — something impractical with human voice actors.

## Why it's effective
Variability in training input is a well-established principle in perceptual learning. Exposure to multiple accents and registers builds robust, transferable listening skills rather than brittle comprehension tied to one voice.

## How AI enables it
- TTS with voice/accent controls generates the same script in multiple variants
- LLM adapts scripts across registers (formal report vs. casual retelling vs. slang version) while preserving core meaning
- System tracks which variants the learner struggles with and increases exposure to those

## Progress Tracking & Assessment

The system tracks comprehension accuracy across a matrix of accents and registers, revealing blind spots.

### 1. Variation Matrix Heatmap

The system scores the learner's comprehension across each accent/register combination.

**Example** (Brazilian Portuguese speaker learning English, travel curriculum):

| | Formal | Casual | Slang |
|---|---|---|---|
| American (General) | 90% | 75% | 40% |
| British (RP) | 70% | 50% | 25% |
| Australian | 55% | 35% | 15% |
| Indian English | 60% | 40% | 20% |

The learner sees this as a color-coded heatmap. Red cells get more practice. "Your weakest combination: Australian casual. Generating targeted episodes."

### 2. Same-Content Comprehension Delta

The system plays the same semantic content in different variants and compares scores.

**Example:**

A hotel check-in dialogue is generated in three versions:
> - General American, formal register: Learner answers 5/5 comprehension questions.
> - British RP, casual register: Learner answers 3/5.
> - Australian accent, fast speed: Learner answers 1/5.

"You understood the same content at 100% in General American but only 20% in fast Australian. The gap is accent/speed, not vocabulary."

### 3. Robustness Score

A single metric that captures how much the learner's comprehension degrades when conditions change from "ideal" (standard accent, slow, formal) to "real-world" (varied accent, fast, casual).

**Example:**

> Week 1: Ideal conditions: 88%. Real-world conditions: 35%. Robustness gap: 53 points.
> Week 6: Ideal conditions: 90%. Real-world conditions: 62%. Robustness gap: 28 points.

"Your robustness gap shrank from 53 to 28 points. You're becoming less dependent on clean, slow audio."
