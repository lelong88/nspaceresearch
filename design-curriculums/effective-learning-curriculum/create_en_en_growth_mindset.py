"""
Create en-en Growth Mindset concept curriculum.
Carol Dweck's Growth Mindset research.
Language: en-en (English speakers learning English vocabulary)
Description tone: provocative_question
Farewell tone: introspective guide
"""

import sys
import json
import requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
BASE_URL = "https://helloapi.step.is"

# --- Vocabulary ---
# Group 1 (Session 1): neuroplasticity, cognition, adaptability, persevere, incremental, cultivate
# Group 2 (Session 2): feedback, setback, embrace, evolve, mastery, trajectory
# Group 3 (Session 3): fixed, innate, malleable, flourish, threshold, paradigm

VOCAB_GROUP_1 = ["neuroplasticity", "cognition", "adaptability", "persevere", "incremental", "cultivate"]
VOCAB_GROUP_2 = ["feedback", "setback", "embrace", "evolve", "mastery", "trajectory"]
VOCAB_GROUP_3 = ["fixed", "innate", "malleable", "flourish", "threshold", "paradigm"]
ALL_VOCAB = VOCAB_GROUP_1 + VOCAB_GROUP_2 + VOCAB_GROUP_3

STRIP_KEYS = {
    "mp3Url", "illustrationSet", "chapterBookmarks", "segments",
    "whiteboardItems", "userReadingId", "lessonUniqueId", "curriculumTags",
    "taskId", "imageId", "practiceMinutes", "practiceTime",
    "difficultyTags", "skillFocusTags"
}


def strip_keys(obj):
    if isinstance(obj, dict):
        return {k: strip_keys(v) for k, v in obj.items() if k not in STRIP_KEYS}
    elif isinstance(obj, list):
        return [strip_keys(item) for item in obj]
    return obj


def build_content():
    # ---- Session 1: Group 1 vocabulary ----
    s1_intro_topic = {
        "type": "introAudio",
        "title": "Introduction to Growth Mindset",
        "description": "An overview of Carol Dweck's research on growth mindset and why your beliefs about intelligence shape everything.",
        "data": {
            "text": "Welcome to Growth Mindset: The Science of Becoming. In this curriculum, you will explore one of the most transformative ideas in modern psychology — the discovery that your beliefs about your own intelligence and abilities fundamentally shape how you learn, how you respond to failure, and how much you ultimately achieve. Carol Dweck, a psychologist at Stanford University, spent decades studying why some people thrive in the face of challenge while others collapse. Her answer was deceptively simple: it comes down to mindset. People who believe their abilities are fixed — that intelligence is something you are born with and cannot change — behave very differently from people who believe their abilities can grow through effort and learning. Dweck calls these two orientations the fixed mindset and the growth mindset. Her research shows that students praised for being smart tend to avoid challenges, because failure threatens their identity. But students praised for working hard seek out challenges, because struggle is where growth happens. This pattern holds across ages, cultures, and domains — from elementary school classrooms to corporate boardrooms. The implications are staggering. If the way you think about your own brain determines how far you go, then changing your mindset is not just a nice idea — it is the single most powerful lever you have for improving your life. Over the next five sessions, you will learn eighteen vocabulary words that capture the science behind Dweck's research. These words will help you talk about the brain, learning, effort, and the beliefs that either limit or liberate human potential. Today, in Session One, we focus on six words that describe the biological and psychological foundations of growth: neuroplasticity, cognition, adaptability, persevere, incremental, and cultivate. Let us begin."
        }
    }

    s1_intro_vocab = {
        "type": "introAudio",
        "title": "Vocabulary: The Foundations of Growth",
        "description": "Learn six words that describe the biological and psychological foundations of growth: neuroplasticity, cognition, adaptability, persevere, incremental, and cultivate.",
        "data": {
            "text": "In this session, you will learn six words that describe the biological and psychological foundations of the growth mindset. These are the concepts that explain why growth is possible — not as a motivational slogan, but as a scientific reality rooted in how the brain actually works. Let us walk through each word carefully. The first word is neuroplasticity. Neuroplasticity is a noun that refers to the brain's ability to reorganize itself by forming new neural connections throughout life. This is the biological foundation of the growth mindset. For most of human history, scientists believed the brain was essentially fixed after childhood — that you were born with a certain amount of intelligence and that was that. Dweck's work gained enormous power when neuroscience confirmed the opposite: the brain is plastic. It changes in response to experience, effort, and learning. Every time you struggle with a difficult problem and push through, your brain literally rewires itself. Neuroplasticity is the reason growth mindset is not just a feel-good philosophy — it is grounded in biology. The second word is cognition. Cognition is a noun meaning the mental processes involved in gaining knowledge and understanding, including thinking, reasoning, remembering, and problem-solving. Dweck's research is fundamentally about cognition — about how people think about thinking. When a student with a fixed mindset encounters a hard math problem, their cognition follows a predictable pattern: this is hard, I must not be smart enough, I should stop trying. When a student with a growth mindset encounters the same problem, their cognition takes a different path: this is hard, I must be learning something, I should keep going. The difference is not in ability. It is in the cognitive framework through which they interpret difficulty. The third word is adaptability. Adaptability is a noun meaning the quality of being able to adjust to new conditions or circumstances. Dweck's research shows that people with a growth mindset demonstrate far greater adaptability than those with a fixed mindset. When the rules change, when a strategy fails, when the environment shifts, growth-minded individuals adjust. They do not cling to a single approach because their identity is not tied to being right — it is tied to learning. Adaptability is what allows a person to fail at one approach and pivot to another without losing confidence or motivation. The fourth word is persevere. Persevere is a verb meaning to continue in a course of action despite difficulty or delay in achieving success. Dweck found that the single most important behavioral difference between fixed and growth mindset individuals is their response to difficulty. Fixed mindset people tend to give up when things get hard, interpreting struggle as evidence of inadequacy. Growth mindset people persevere, interpreting struggle as evidence of learning. A student who perseveres through a challenging chapter, a musician who perseveres through months of frustrating practice, an athlete who perseveres through a losing season — these are people whose mindset allows them to see difficulty as temporary and surmountable. The fifth word is incremental. Incremental is an adjective meaning relating to or denoting an increase or addition, especially one of a series on a fixed scale. Dweck often describes the growth mindset as an incremental theory of intelligence — the belief that intelligence grows in small, steady steps through effort and practice. This is the opposite of the entity theory, which holds that intelligence is a fixed quantity. The power of the incremental view is that it makes every small effort meaningful. You do not need a dramatic breakthrough to grow. You need consistent, incremental progress — one problem at a time, one lesson at a time, one day at a time. The sixth and final word for this session is cultivate. Cultivate is a verb meaning to try to develop or improve something through careful attention and effort. Dweck argues that a growth mindset is not something you either have or do not have. It is something you cultivate — deliberately, over time, through conscious choices about how you respond to challenge, failure, and criticism. A teacher cultivates growth mindset in students by praising effort rather than ability. A parent cultivates it by modeling curiosity and persistence. An individual cultivates it by catching themselves in fixed-mindset thinking and choosing a different response. Let us review all six words one more time: neuroplasticity, the brain's ability to rewire itself through experience; cognition, the mental processes of thinking and understanding; adaptability, the ability to adjust to new conditions; persevere, to continue despite difficulty; incremental, growing in small steady steps; and cultivate, to develop something through careful effort. You will encounter all six of these words in the reading passage that follows. Pay attention to how they appear in context, and think about how they connect to Dweck's research on growth mindset."
        }
    }

    s1_view_flashcards = {
        "type": "viewFlashcards",
        "title": "Flashcards: Foundations of Growth",
        "description": "Learn 6 words: neuroplasticity, cognition, adaptability, persevere, incremental, cultivate.",
        "vocabList": VOCAB_GROUP_1
    }

    s1_speak_flashcards = {
        "type": "speakFlashcards",
        "title": "Flashcards: Speak the Words",
        "description": "Practice pronouncing: neuroplasticity, cognition, adaptability, persevere, incremental, cultivate.",
        "vocabList": VOCAB_GROUP_1
    }

    s1_vocab_level1 = {
        "type": "vocabLevel1",
        "title": "Flashcards: Vocabulary Level 1",
        "description": "Test your knowledge of: neuroplasticity, cognition, adaptability, persevere, incremental, cultivate.",
        "vocabList": VOCAB_GROUP_1
    }

    s1_vocab_level2 = {
        "type": "vocabLevel2",
        "title": "Flashcards: Vocabulary Level 2",
        "description": "Advanced practice with: neuroplasticity, cognition, adaptability, persevere, incremental, cultivate.",
        "vocabList": VOCAB_GROUP_1
    }

    s1_reading_text = "For decades, the prevailing view in psychology was that intelligence was largely fixed at birth. You were either smart or you were not, and no amount of effort could fundamentally change the hand you were dealt. Carol Dweck did not set out to overturn this assumption. She started by studying how children respond to failure — and what she found changed the direction of her career and, eventually, the way millions of people think about learning.\n\nIn one of her earliest experiments, Dweck gave elementary school students a series of puzzles. The first few were easy. Then the puzzles became impossibly hard. What fascinated Dweck was not who solved the hard puzzles — almost nobody did. What fascinated her was how the children responded to failure. Some children crumbled. They said things like 'I'm not smart enough' and 'I give up.' But other children did something remarkable. They leaned forward, rubbed their hands together, and said things like 'I love a challenge' and 'I was hoping this would be informative.' These children did not just tolerate difficulty — they welcomed it. Dweck realized she was witnessing two fundamentally different cognitive frameworks in action.\n\nThe children who gave up were operating under what Dweck would later call a fixed mindset — the belief that intelligence and ability are static traits. For them, failure was not a learning opportunity. It was a verdict. If you fail, it means you are not smart, and since smartness is fixed, there is nothing you can do about it. The children who embraced the challenge were operating under a growth mindset — the belief that abilities can be developed through effort, strategy, and perseverance. For them, failure was information, not identity.\n\nWhat makes Dweck's work so powerful is that it is not just a theory about attitudes. It is grounded in the science of neuroplasticity — the brain's proven ability to form new neural connections in response to learning and experience. Every time you persevere through a difficult problem, your brain physically changes. New pathways are strengthened. Old limitations are overwritten. The incremental gains may be invisible day to day, but over months and years, they compound into dramatic cognitive growth.\n\nDweck's research also revealed that mindset is not destiny. It can be cultivated. In study after study, she showed that simple interventions — teaching students about neuroplasticity, praising effort instead of ability, reframing failure as a natural part of learning — could shift students from a fixed mindset to a growth mindset. The results were striking. Students who learned about the brain's adaptability showed measurable improvements in motivation, engagement, and academic performance. Their cognition literally changed: they began interpreting difficulty as a signal to try harder rather than a signal to give up.\n\nThe implications extend far beyond the classroom. Dweck's framework suggests that the single most important factor in long-term achievement is not talent, not resources, not even opportunity — it is the belief that you can grow. And that belief, like any skill, can be developed through incremental effort and deliberate practice. The question is not whether you are smart enough. The question is whether you are willing to cultivate the mindset that makes growth possible."

    s1_reading = {
        "type": "reading",
        "title": "Read: The Discovery of Growth Mindset",
        "description": "For decades, the prevailing view in psychology was that intelligence was largely fixed at birth...",
        "data": {"text": s1_reading_text}
    }

    s1_speak_reading = {
        "type": "speakReading",
        "title": "Read: Speak the Passage Aloud",
        "description": "For decades, the prevailing view in psychology was that intelligence was largely fixed at birth...",
        "data": {"text": s1_reading_text}
    }

    s1_read_along = {
        "type": "readAlong",
        "title": "Listen: The Discovery of Growth Mindset",
        "description": "Listen to the passage and follow along.",
        "data": {"text": s1_reading_text}
    }

    s1_writing_sentence_1 = {
        "type": "writingSentence",
        "title": "Write: Using 'neuroplasticity'",
        "description": "Write a sentence using the word neuroplasticity.",
        "data": {
            "prompt": "Use the word 'neuroplasticity' in a sentence about how the brain changes through learning. Example: Recent research on neuroplasticity has shown that learning a second language in adulthood physically alters the structure of the brain, creating new neural pathways that did not exist before.",
            "vocabWord": "neuroplasticity"
        }
    }

    s1_writing_sentence_2 = {
        "type": "writingSentence",
        "title": "Write: Using 'cultivate'",
        "description": "Write a sentence using the word cultivate.",
        "data": {
            "prompt": "Use the word 'cultivate' in a sentence about deliberately developing a skill or quality over time. Example: She made a conscious decision to cultivate patience by meditating for ten minutes every morning, and within six months, her colleagues noticed a dramatic change in how she handled stressful meetings.",
            "vocabWord": "cultivate"
        }
    }

    s1_writing_paragraph = {
        "type": "writingParagraph",
        "title": "Write: Reflecting on the Foundations of Growth",
        "description": "Write a paragraph about the biological and psychological foundations that make personal growth possible.",
        "data": {
            "prompt": "Think about a time when you struggled to learn something new — a language, a skill, a subject in school. At the time, did you believe your ability was fixed, or did you believe you could improve with effort? Write a paragraph describing that experience and how your beliefs affected your behavior. Use at least four of the following words: neuroplasticity, cognition, adaptability, persevere, incremental, cultivate.",
            "vocabList": VOCAB_GROUP_1
        }
    }

    session_1 = {
        "title": "Session 1: The Foundations of Growth",
        "activities": [
            s1_intro_topic, s1_intro_vocab, s1_view_flashcards, s1_speak_flashcards,
            s1_vocab_level1, s1_vocab_level2, s1_reading, s1_speak_reading,
            s1_read_along, s1_writing_sentence_1, s1_writing_sentence_2, s1_writing_paragraph
        ]
    }

    # ---- Session 2: Group 2 vocabulary ----
    s2_intro_topic = {
        "type": "introAudio",
        "title": "The Dynamics of Learning",
        "description": "Exploring how feedback, setbacks, and the pursuit of mastery shape the trajectory of growth.",
        "data": {
            "text": "Welcome back. In Session One, you learned six words that describe the biological and psychological foundations of growth — neuroplasticity, cognition, adaptability, persevere, incremental, and cultivate. These words explain why growth is possible. Now, in Session Two, we turn to the dynamics of growth — the messy, nonlinear process of actually learning and improving. Growth does not happen in a straight line. It happens through cycles of effort, feedback, failure, and adjustment. The people who grow the most are not the ones who avoid mistakes. They are the ones who learn from them. In this session, you will learn six new words that capture the dynamics of learning: feedback, setback, embrace, evolve, mastery, and trajectory. These words describe not just what happens when you learn, but how you respond to the inevitable difficulties along the way. Let us begin."
        }
    }

    s2_intro_vocab = {
        "type": "introAudio",
        "title": "Vocabulary: The Dynamics of Learning",
        "description": "Learn six words about the process of learning and growth: feedback, setback, embrace, evolve, mastery, and trajectory.",
        "data": {
            "text": "In Session One, you learned about the foundations of growth: neuroplasticity, cognition, adaptability, persevere, incremental, and cultivate. Now, in Session Two, we explore the dynamics of learning — the forces that shape how growth actually unfolds in real life. Let us explore each word. The first word is feedback. Feedback is a noun meaning information about reactions to a product, a person's performance, or a behavior, used as a basis for improvement. In Dweck's research, the role of feedback is central. She found that the type of feedback people receive dramatically shapes their mindset. When teachers tell students 'You are so smart,' they inadvertently reinforce a fixed mindset — the student begins to believe that their worth comes from an innate quality rather than from effort. But when teachers say 'You worked really hard on this,' they reinforce a growth mindset. The student learns that effort is what matters. Feedback is not just information. It is a signal that shapes how people think about themselves and their abilities. The second word is setback. A setback is a noun meaning a reversal or check in progress. Dweck's research reveals that how people interpret setbacks is one of the clearest markers of their mindset. A person with a fixed mindset sees a setback as proof of their limitations — a failed exam means they are not smart enough, a rejected job application means they are not good enough. A person with a growth mindset sees a setback as a temporary obstacle — a failed exam means they need to study differently, a rejection means they need to improve their approach. The difference is not in the setback itself but in the meaning assigned to it. The third word is embrace. Embrace is a verb meaning to accept or support something willingly and enthusiastically. Dweck found that growth-minded individuals do not merely tolerate challenges — they embrace them. They actively seek out situations that stretch their abilities because they understand that discomfort is where learning happens. A student who embraces a difficult course instead of avoiding it, a professional who embraces critical feedback instead of deflecting it, a musician who embraces a piece that is beyond their current skill — these are people whose mindset transforms difficulty from a threat into an opportunity. The fourth word is evolve. Evolve is a verb meaning to develop gradually, especially from a simple to a more complex or advanced form. Dweck's framework suggests that human abilities are not static — they evolve over time in response to effort, experience, and learning. A writer's style evolves through years of practice and revision. A leader's judgment evolves through decades of making decisions, some good and some bad. The growth mindset is fundamentally a belief in evolution — the conviction that who you are today is not who you have to be tomorrow. The fifth word is mastery. Mastery is a noun meaning comprehensive knowledge or skill in a subject or accomplishment. Dweck distinguishes between two orientations toward achievement: performance goals and mastery goals. People with performance goals want to look smart. People with mastery goals want to actually become competent. This distinction has enormous consequences. Performance-oriented students choose easy tasks that make them look good. Mastery-oriented students choose challenging tasks that help them learn. Over time, the mastery-oriented students develop deeper knowledge, greater resilience, and more genuine confidence — because their confidence is built on real competence, not on the appearance of competence. The sixth and final word for this session is trajectory. Trajectory is a noun meaning the path followed by a moving object, or more broadly, the general direction of something's development. Dweck's research suggests that mindset does not just affect individual moments — it shapes your entire trajectory. A student who adopts a growth mindset in elementary school follows a fundamentally different trajectory than one who adopts a fixed mindset. The growth-minded student takes harder courses, seeks more feedback, recovers faster from failures, and accumulates advantages that compound over years and decades. Trajectory is the long-term consequence of the daily choices your mindset produces. Let us review all six words together: feedback, information used as a basis for improvement; setback, a reversal in progress; embrace, to accept willingly and enthusiastically; evolve, to develop gradually over time; mastery, comprehensive knowledge or skill; and trajectory, the path of development over time. You will see all six of these words in the reading passage ahead. Notice how they connect to the ideas from Session One and deepen your understanding of how growth actually happens."
        }
    }

    s2_view_flashcards = {
        "type": "viewFlashcards",
        "title": "Flashcards: The Dynamics of Learning",
        "description": "Learn 6 words: feedback, setback, embrace, evolve, mastery, trajectory.",
        "vocabList": VOCAB_GROUP_2
    }

    s2_speak_flashcards = {
        "type": "speakFlashcards",
        "title": "Flashcards: Speak the Words",
        "description": "Practice pronouncing: feedback, setback, embrace, evolve, mastery, trajectory.",
        "vocabList": VOCAB_GROUP_2
    }

    s2_vocab_level1 = {
        "type": "vocabLevel1",
        "title": "Flashcards: Vocabulary Level 1",
        "description": "Test your knowledge of: feedback, setback, embrace, evolve, mastery, trajectory.",
        "vocabList": VOCAB_GROUP_2
    }

    s2_vocab_level2 = {
        "type": "vocabLevel2",
        "title": "Flashcards: Vocabulary Level 2",
        "description": "Advanced practice with: feedback, setback, embrace, evolve, mastery, trajectory.",
        "vocabList": VOCAB_GROUP_2
    }

    s2_reading_text = "Carol Dweck's research on mindset did not stop at identifying two ways of thinking about intelligence. She wanted to understand the mechanisms — the specific behaviors and responses that separate growth-minded people from fixed-minded people in real-world situations. What she found was that the difference shows up most clearly in how people handle three things: feedback, setbacks, and the pursuit of mastery.\n\nConsider feedback first. In a series of studies, Dweck and her colleagues gave students a test and then offered them one of two types of feedback. Some students were told, 'You must be smart at this.' Others were told, 'You must have worked really hard.' The results were dramatic. Students praised for intelligence chose easier tasks on the next round — they wanted to protect their reputation for being smart. Students praised for effort chose harder tasks — they wanted to keep learning. When both groups later encountered a difficult test and performed poorly, the intelligence-praised students lost confidence and their performance declined. The effort-praised students maintained their confidence and their performance improved. The feedback had reshaped their entire approach to learning.\n\nSetbacks revealed an even starker divide. Dweck found that fixed-mindset individuals treat setbacks as defining moments — a bad grade, a failed project, a lost competition becomes evidence of a permanent limitation. They do not just feel disappointed. They feel diminished. Growth-mindset individuals treat the same setbacks as data points. A bad grade means the study strategy needs to change. A failed project means the approach needs refinement. A lost competition means there is more to learn. They do not embrace failure for its own sake — nobody enjoys failing. But they embrace the information that failure provides, and they use it to evolve.\n\nThis difference in response to setbacks has profound consequences for the trajectory of a person's development. Dweck tracked students over years and found that those with a growth mindset showed a consistently upward trajectory in academic performance, even when they started at the same level as their fixed-mindset peers. The reason was not that they were smarter. It was that they responded to difficulty by working harder and trying new strategies, while their fixed-mindset peers responded by withdrawing effort and avoiding challenges.\n\nThe pursuit of mastery is where the growth mindset produces its most impressive results. Dweck distinguishes between performance goals — wanting to look competent — and mastery goals — wanting to actually become competent. Students oriented toward mastery embrace challenges that stretch their abilities. They seek out feedback, even when it is critical, because they understand that honest feedback is the fastest path to improvement. They do not measure their worth by how they compare to others. They measure it by how much they have evolved from where they started.\n\nDweck's research suggests that mastery is not a destination but a trajectory — an ongoing process of growth that never truly ends. The growth mindset does not promise that you will master everything you attempt. It promises something more valuable: that every effort you make, every setback you endure, and every piece of feedback you absorb will move you further along the path. The question is not whether you will reach perfection. The question is whether you are willing to embrace the process of getting better."

    s2_reading = {
        "type": "reading",
        "title": "Read: How Growth Happens",
        "description": "Carol Dweck's research on mindset did not stop at identifying two ways of thinking about intelligence...",
        "data": {"text": s2_reading_text}
    }

    s2_speak_reading = {
        "type": "speakReading",
        "title": "Read: Speak the Passage Aloud",
        "description": "Carol Dweck's research on mindset did not stop at identifying two ways of thinking about intelligence...",
        "data": {"text": s2_reading_text}
    }

    s2_read_along = {
        "type": "readAlong",
        "title": "Listen: How Growth Happens",
        "description": "Listen to the passage and follow along.",
        "data": {"text": s2_reading_text}
    }

    s2_writing_sentence_1 = {
        "type": "writingSentence",
        "title": "Write: Using 'embrace'",
        "description": "Write a sentence using the word embrace.",
        "data": {
            "prompt": "Use the word 'embrace' in a sentence about willingly accepting a challenge or difficult situation. Example: Rather than avoiding the advanced calculus course, she decided to embrace the challenge, knowing that the struggle itself would make her a stronger mathematician.",
            "vocabWord": "embrace"
        }
    }

    s2_writing_sentence_2 = {
        "type": "writingSentence",
        "title": "Write: Using 'trajectory'",
        "description": "Write a sentence using the word trajectory.",
        "data": {
            "prompt": "Use the word 'trajectory' in a sentence about the long-term direction of someone's development or career. Example: A single decision to switch from performance goals to mastery goals altered the entire trajectory of his career, transforming him from a cautious employee into an innovative leader.",
            "vocabWord": "trajectory"
        }
    }

    s2_writing_paragraph = {
        "type": "writingParagraph",
        "title": "Write: Reflecting on Feedback and Setbacks",
        "description": "Write a paragraph about how feedback and setbacks shape the learning process.",
        "data": {
            "prompt": "Think about a time when you received critical feedback or experienced a significant setback. How did you respond? Did you treat it as a verdict on your abilities, or as information you could use to improve? Write a paragraph describing that experience and what it taught you about learning. Use at least four of the following words: feedback, setback, embrace, evolve, mastery, trajectory.",
            "vocabList": VOCAB_GROUP_2
        }
    }

    session_2 = {
        "title": "Session 2: The Dynamics of Learning",
        "activities": [
            s2_intro_topic, s2_intro_vocab, s2_view_flashcards, s2_speak_flashcards,
            s2_vocab_level1, s2_vocab_level2, s2_reading, s2_speak_reading,
            s2_read_along, s2_writing_sentence_1, s2_writing_sentence_2, s2_writing_paragraph
        ]
    }

    # ---- Session 3: Group 3 vocabulary ----
    s3_intro_topic = {
        "type": "introAudio",
        "title": "Fixed vs. Growth: The Mindset Divide",
        "description": "Exploring the contrast between fixed and growth mindsets and the paradigm shift that makes flourishing possible.",
        "data": {
            "text": "Welcome to Session Three. Over the past two sessions, you have built a powerful vocabulary for talking about growth mindset. In Session One, you learned about the foundations — neuroplasticity, cognition, adaptability, persevere, incremental, and cultivate. In Session Two, you explored the dynamics — feedback, setback, embrace, evolve, mastery, and trajectory. Now, in this final teaching session, we bring it all together. You will learn six words that capture the core tension in Dweck's research: the contrast between fixed and growth orientations, and the paradigm shift required to move from one to the other. These words will help you discuss not just what growth mindset is, but what it replaces — and what becomes possible when you make the shift. Let us begin."
        }
    }

    s3_intro_vocab = {
        "type": "introAudio",
        "title": "Vocabulary: The Mindset Divide",
        "description": "Learn six words about the contrast between fixed and growth orientations: fixed, innate, malleable, flourish, threshold, and paradigm.",
        "data": {
            "text": "You have already learned twelve words across two sessions. In Session One, you explored the foundations of growth: neuroplasticity, cognition, adaptability, persevere, incremental, and cultivate. In Session Two, you studied the dynamics of learning: feedback, setback, embrace, evolve, mastery, and trajectory. Now, in Session Three, you will learn six words that frame the central tension in Dweck's work — the divide between believing abilities are fixed and believing they can grow. The first word is fixed. Fixed is an adjective meaning fastened securely in position, or not subject to change or fluctuation. In Dweck's framework, a fixed mindset is the belief that your intelligence, talent, and abilities are static traits — you have a certain amount and that is that. People with a fixed mindset see effort as a sign of weakness. If you were truly talented, they believe, things would come easily. This belief creates a fragile psychology: every test becomes a judgment, every failure becomes a sentence, and every challenge becomes a threat to your identity. The fixed mindset is not just wrong — it is paralyzing. The second word is innate. Innate is an adjective meaning inborn, natural, existing from birth rather than acquired. The fixed mindset rests on the assumption that the qualities that matter most — intelligence, creativity, leadership — are innate. You either have them or you do not. Dweck's research directly challenges this assumption. While certain baseline capacities may be innate, the degree to which they develop depends enormously on effort, environment, and mindset. A child may have an innate curiosity about numbers, but whether that curiosity develops into mathematical expertise depends on years of practice, teaching, and perseverance. Innate potential is a starting point, not a ceiling. The third word is malleable. Malleable is an adjective meaning able to be hammered or pressed into shape without breaking, or more broadly, easily influenced or changed. This is the growth mindset's core claim about human ability: it is malleable. Intelligence is not a fixed quantity sealed at birth. It is a malleable quality that responds to effort, strategy, and learning. Dweck's research, supported by neuroscience, shows that the brain itself is malleable — it physically changes in response to experience. When you learn something new, neurons form new connections. When you practice a skill, those connections strengthen. Malleability is not a metaphor. It is a biological fact. The fourth word is flourish. Flourish is a verb meaning to grow or develop in a healthy or vigorous way, especially as the result of a particularly favorable environment. Dweck's research shows that people with a growth mindset do not just survive challenges — they flourish because of them. A growth-minded student placed in a challenging academic environment does not wilt under pressure. They flourish, because the difficulty activates their belief that effort leads to improvement. Flourishing is what happens when a malleable mindset meets a demanding environment. The conditions that would crush a fixed-minded person become the conditions that allow a growth-minded person to thrive. The fifth word is threshold. Threshold is a noun meaning the point at which something begins or changes, or the level at which something starts to take effect. Dweck's work suggests that there is a critical threshold in mindset development — a point at which a person's beliefs about their own abilities shift from fixed to growth. Crossing this threshold does not happen overnight. It requires repeated experiences of effort leading to improvement, supported by the right kind of feedback and environment. But once crossed, the threshold marks a fundamental change in how a person relates to challenge, failure, and learning. The sixth and final word for this session is paradigm. Paradigm is a noun meaning a typical example or pattern of something, or a fundamental model or framework for understanding. Dweck's growth mindset represents a paradigm shift in how we think about human potential. The old paradigm said: talent is destiny. The new paradigm says: effort is destiny. This is not just a change in emphasis. It is a complete reframing of what it means to be intelligent, successful, and capable. A paradigm shift changes not just what you believe but how you see the world — and Dweck's research has triggered exactly that kind of shift in education, business, and personal development worldwide. Let us review all six words: fixed, not subject to change; innate, existing from birth; malleable, able to be shaped and changed; flourish, to grow vigorously; threshold, the point at which something changes; and paradigm, a fundamental framework for understanding. You will encounter all six of these words in the reading passage that follows."
        }
    }

    s3_view_flashcards = {
        "type": "viewFlashcards",
        "title": "Flashcards: The Mindset Divide",
        "description": "Learn 6 words: fixed, innate, malleable, flourish, threshold, paradigm.",
        "vocabList": VOCAB_GROUP_3
    }

    s3_speak_flashcards = {
        "type": "speakFlashcards",
        "title": "Flashcards: Speak the Words",
        "description": "Practice pronouncing: fixed, innate, malleable, flourish, threshold, paradigm.",
        "vocabList": VOCAB_GROUP_3
    }

    s3_vocab_level1 = {
        "type": "vocabLevel1",
        "title": "Flashcards: Vocabulary Level 1",
        "description": "Test your knowledge of: fixed, innate, malleable, flourish, threshold, paradigm.",
        "vocabList": VOCAB_GROUP_3
    }

    s3_vocab_level2 = {
        "type": "vocabLevel2",
        "title": "Flashcards: Vocabulary Level 2",
        "description": "Advanced practice with: fixed, innate, malleable, flourish, threshold, paradigm.",
        "vocabList": VOCAB_GROUP_3
    }

    s3_reading_text = "The most provocative claim in Carol Dweck's research is not that effort matters. Most people already believe that, at least in the abstract. The provocative claim is that our culture's obsession with innate talent is actively harmful — that the fixed mindset is not just incorrect but destructive, and that replacing it with a growth mindset requires nothing less than a paradigm shift in how we think about human potential.\n\nConsider how deeply the fixed mindset is embedded in everyday language. We say someone is 'a natural' or 'born to do this.' We describe children as 'gifted' — a word that literally implies their abilities were given to them, not earned. We celebrate prodigies and geniuses while paying far less attention to the years of deliberate practice that produced their expertise. This language reinforces the belief that the qualities that matter most are innate — that you either have them or you do not. Dweck argues that this belief creates a culture in which people are afraid to try, afraid to fail, and afraid to be seen struggling, because struggle is interpreted as evidence that you lack the innate ability to succeed.\n\nThe growth mindset offers a fundamentally different paradigm. In this framework, abilities are not fixed traits but malleable qualities that develop through effort, strategy, and learning. Intelligence is not a gift you unwrap at birth. It is a muscle you build over a lifetime. This shift in paradigm changes everything — how teachers teach, how parents praise, how managers evaluate, and how individuals relate to their own potential.\n\nDweck's research shows that when people cross the threshold from a fixed mindset to a growth mindset, their behavior changes in measurable ways. They take on harder challenges. They persist longer in the face of difficulty. They seek out feedback instead of avoiding it. And perhaps most importantly, they flourish in environments that would have previously intimidated them. A student who once avoided advanced courses because she feared looking stupid begins to embrace them because she understands that difficulty is where learning happens. An employee who once hid his mistakes begins to share them openly because he recognizes that transparency accelerates improvement.\n\nBut Dweck is careful to note that the threshold between fixed and growth mindset is not a single moment of revelation. It is a gradual process, shaped by experience, environment, and the kind of feedback a person receives. A child who is consistently praised for being smart may develop a deeply entrenched fixed mindset that takes years to shift. A child who is consistently praised for effort and strategy may develop a growth mindset that allows them to flourish across many domains.\n\nThe implications of this research are profound. If human abilities are truly malleable — and the science of neuroplasticity confirms that they are — then the most important thing any society can do is create environments where people are encouraged to grow rather than pressured to prove themselves. Schools that reward curiosity over correctness. Workplaces that value learning over performance. Families that celebrate effort over innate talent. In such environments, people do not just survive. They flourish. And the collective potential of an entire community begins to expand in ways that the old, fixed paradigm could never have imagined."

    s3_reading = {
        "type": "reading",
        "title": "Read: The Paradigm Shift",
        "description": "The most provocative claim in Carol Dweck's research is not that effort matters...",
        "data": {"text": s3_reading_text}
    }

    s3_speak_reading = {
        "type": "speakReading",
        "title": "Read: Speak the Passage Aloud",
        "description": "The most provocative claim in Carol Dweck's research is not that effort matters...",
        "data": {"text": s3_reading_text}
    }

    s3_read_along = {
        "type": "readAlong",
        "title": "Listen: The Paradigm Shift",
        "description": "Listen to the passage and follow along.",
        "data": {"text": s3_reading_text}
    }

    s3_writing_sentence_1 = {
        "type": "writingSentence",
        "title": "Write: Using 'malleable'",
        "description": "Write a sentence using the word malleable.",
        "data": {
            "prompt": "Use the word 'malleable' in a sentence about the capacity for change or development. Example: The research demonstrated that even adults in their sixties have malleable cognitive abilities, capable of significant improvement through consistent mental exercise and new learning experiences.",
            "vocabWord": "malleable"
        }
    }

    s3_writing_sentence_2 = {
        "type": "writingSentence",
        "title": "Write: Using 'paradigm'",
        "description": "Write a sentence using the word paradigm.",
        "data": {
            "prompt": "Use the word 'paradigm' in a sentence about a fundamental shift in how people think about something. Example: The discovery that praising effort produces better outcomes than praising intelligence represented a paradigm shift in educational psychology, overturning decades of conventional wisdom about how to motivate students.",
            "vocabWord": "paradigm"
        }
    }

    s3_writing_paragraph = {
        "type": "writingParagraph",
        "title": "Write: Reflecting on Fixed vs. Growth",
        "description": "Write a paragraph about the contrast between fixed and growth mindsets.",
        "data": {
            "prompt": "Dweck argues that our culture's celebration of innate talent creates a fixed mindset that prevents people from reaching their potential. Do you agree? Think about an area of your life where you have held either a fixed or growth belief about your abilities. Write a paragraph exploring how that belief affected your behavior and outcomes, using at least four of the following words: fixed, innate, malleable, flourish, threshold, paradigm.",
            "vocabList": VOCAB_GROUP_3
        }
    }

    session_3 = {
        "title": "Session 3: Fixed vs. Growth — The Mindset Divide",
        "activities": [
            s3_intro_topic, s3_intro_vocab, s3_view_flashcards, s3_speak_flashcards,
            s3_vocab_level1, s3_vocab_level2, s3_reading, s3_speak_reading,
            s3_read_along, s3_writing_sentence_1, s3_writing_sentence_2, s3_writing_paragraph
        ]
    }


    # ---- Session 4: Review (full article) ----
    s4_reading_text = "Carol Dweck's growth mindset research began with a simple observation in a laboratory: some children respond to failure by shutting down, while others respond by leaning in. That observation, made in the early 1980s, launched a research program that would fundamentally reshape how psychologists, educators, and business leaders think about human potential. The core finding is elegant in its simplicity: what you believe about your own abilities determines how you behave, and how you behave determines what you achieve.\n\nThe science behind this finding is grounded in neuroplasticity — the brain's capacity to reorganize itself by forming new neural connections throughout life. For centuries, the dominant view was that the brain was essentially fixed after a critical period in childhood. You were born with a certain cognitive architecture, and that was your lot. Modern neuroscience has demolished this view. Brain imaging studies show that learning physically changes the structure of the brain. When a person perseveres through a difficult mathematical problem, the neural pathways involved in mathematical reasoning literally strengthen. When a musician practices a challenging passage for the hundredth time, the connections between motor cortex and auditory cortex become denser and more efficient. The brain is not a fixed organ. It is a malleable one, constantly being reshaped by experience.\n\nThis biological reality is the foundation of Dweck's psychological framework. If the brain can change, then abilities can change. If abilities can change, then the belief that they cannot — the fixed mindset — is not just pessimistic. It is factually wrong. And yet, Dweck found that the fixed mindset is remarkably common. In study after study, she encountered people who believed their intelligence was innate and unchangeable. These individuals avoided challenges, gave up easily in the face of setbacks, and interpreted effort as a sign of inadequacy. Their cognition followed a predictable pattern: difficulty means I am not smart enough, and since smartness is fixed, there is no point in trying harder.\n\nThe growth mindset produces the opposite pattern. People who believe their abilities are malleable embrace challenges as opportunities to learn. They treat setbacks not as verdicts but as feedback — information about what to do differently next time. They persevere through difficulty because they understand that struggle is not a sign of failure but a sign of growth. Their trajectory is fundamentally different: where fixed-mindset individuals plateau early and stagnate, growth-mindset individuals show continuous, incremental improvement over time.\n\nDweck's research has revealed that mindset is not just an individual trait — it is shaped by environment, culture, and the specific kind of feedback people receive. When teachers praise students for being smart, they inadvertently cultivate a fixed mindset. When they praise students for effort and strategy, they cultivate a growth mindset. This finding has enormous implications for education. It suggests that the way we talk to children about their abilities can either limit or liberate their potential.\n\nThe concept of mastery is central to the growth mindset framework. Dweck distinguishes between performance orientation — wanting to look competent — and mastery orientation — wanting to actually become competent. Growth-minded individuals pursue mastery not because it is easy but because the process of evolving from novice to expert is inherently meaningful to them. They understand that mastery is not a destination but a trajectory — an ongoing journey of improvement that never truly ends.\n\nPerhaps the most important insight from Dweck's work is that mindset is not destiny. A person with a deeply entrenched fixed mindset can cross the threshold into growth-minded thinking through deliberate effort and the right kind of support. The paradigm shift from fixed to growth is not easy — it requires confronting deeply held beliefs about talent, intelligence, and self-worth. But it is possible. And when it happens, people do not just improve. They flourish. They discover reserves of adaptability and resilience they never knew they had. They begin to see every challenge not as a threat to their identity but as an invitation to become something more than they were yesterday."

    s4_intro = {
        "type": "introAudio",
        "title": "Review: The Complete Picture of Growth Mindset",
        "description": "A review session bringing together all 18 vocabulary words in a comprehensive article about growth mindset.",
        "data": {
            "text": "Welcome to Session Four. Over the past three sessions, you have learned eighteen vocabulary words that capture the science of growth mindset. In Session One, you explored the foundations: neuroplasticity, cognition, adaptability, persevere, incremental, and cultivate. In Session Two, you studied the dynamics: feedback, setback, embrace, evolve, mastery, and trajectory. In Session Three, you examined the mindset divide: fixed, innate, malleable, flourish, threshold, and paradigm. Now it is time to see all eighteen words working together in a single, comprehensive article about Carol Dweck's research. This article weaves together everything you have learned. As you read, notice how the words connect to each other and to the broader themes of growth mindset. Let us begin."
        }
    }

    s4_reading = {
        "type": "reading",
        "title": "Read: The Science of Growth Mindset — A Complete Overview",
        "description": "Carol Dweck's growth mindset research began with a simple observation in a laboratory...",
        "data": {"text": s4_reading_text}
    }

    s4_speak_reading = {
        "type": "speakReading",
        "title": "Read: Speak the Full Article Aloud",
        "description": "Carol Dweck's growth mindset research began with a simple observation in a laboratory...",
        "data": {"text": s4_reading_text}
    }

    s4_read_along = {
        "type": "readAlong",
        "title": "Listen: The Science of Growth Mindset — A Complete Overview",
        "description": "Listen to the passage and follow along.",
        "data": {"text": s4_reading_text}
    }

    session_4 = {
        "title": "Session 4: Review — The Complete Picture",
        "activities": [s4_intro, s4_reading, s4_speak_reading, s4_read_along]
    }

    # ---- Session 5: Final reading + farewell ----
    s5_reading_text = "In the decades since Carol Dweck first published her research on mindset, the concept has traveled far beyond the psychology laboratory. Growth mindset has become one of the most widely discussed ideas in education, corporate training, parenting, and personal development. It has also attracted criticism — some of it valid, some of it based on misunderstanding. Engaging with both the promise and the limitations of growth mindset research is essential for anyone who wants to apply it thoughtfully.\n\nThe most common criticism is that growth mindset has been oversimplified into a feel-good slogan: just believe in yourself and you can do anything. Dweck herself has pushed back against this interpretation. She emphasizes that growth mindset is not about blind optimism or empty praise. It is about a specific, evidence-based understanding of how the brain works. Neuroplasticity is real, but it does not mean that anyone can become anything with enough effort. It means that abilities are malleable within a range, and that the range is far wider than most people assume. A person with no innate musical ability will not become a concert pianist through effort alone. But a person with moderate musical ability who perseveres through years of deliberate practice will develop far beyond what a fixed mindset would predict.\n\nAnother criticism concerns the role of systemic barriers. Critics argue that emphasizing individual mindset can distract from structural inequalities — poverty, discrimination, lack of access to quality education — that limit people's opportunities regardless of their beliefs. This is a fair point, and Dweck has acknowledged it. Growth mindset is not a substitute for systemic change. But it is a powerful complement to it. A student in an under-resourced school who develops a growth mindset will not magically overcome every barrier. But they will be better equipped to take advantage of whatever opportunities do exist, to persevere through setbacks that would derail a fixed-minded peer, and to cultivate the adaptability needed to navigate a world that is not always fair.\n\nThe most exciting frontier of growth mindset research is in understanding how environments can be designed to help people flourish. Dweck and her colleagues have shown that relatively simple interventions — teaching students about neuroplasticity, training teachers to give process-focused feedback, creating classroom cultures that normalize struggle — can produce measurable improvements in motivation and achievement. These interventions work not by changing what students know but by changing how they think about their own cognition. When a student understands that their brain is malleable, that intelligence is not innate and fixed but something that evolves through effort, they cross a threshold. They begin to embrace challenges instead of avoiding them. They begin to see setbacks as information rather than identity. They begin to pursue mastery for its own sake rather than performing for approval.\n\nThe paradigm shift that Dweck's research represents is still unfolding. In education, it is challenging the centuries-old practice of sorting students by perceived ability. In business, it is reshaping how organizations think about talent development and leadership. In personal life, it is giving millions of people a new framework for understanding their own potential — a framework that says your trajectory is not determined by where you start but by how you respond to the incremental challenges along the way.\n\nThe growth mindset is not a magic formula. It does not eliminate difficulty or guarantee success. What it does is change your relationship with difficulty. It transforms struggle from a threat into a signal — a signal that your brain is working, that new neural connections are forming, that you are in the process of becoming something you were not before. And that transformation, Dweck's research suggests, is available to anyone willing to cultivate it. The question is not whether you were born with enough talent. The question is whether you are willing to flourish in the space between who you are and who you could become."

    s5_intro = {
        "type": "introAudio",
        "title": "Final Reading: Growth Mindset in the Real World",
        "description": "Introducing the final reading that explores the broader implications, criticisms, and future of growth mindset research.",
        "data": {
            "text": "Welcome to Session Five — your final session. You have come a long way. You have learned eighteen words that capture the science of growth mindset, read three passages exploring different dimensions of Dweck's research, and practiced using these words in your own writing. In this session, you will read one more article — this one looking at the broader implications of growth mindset research, including its impact on education, the criticisms it has faced, and the exciting frontiers of new research. You will encounter all eighteen vocabulary words in context. After the reading, we will close with a farewell that invites you to look inward and reflect on what these ideas mean for your own life. Let us begin."
        }
    }

    s5_reading = {
        "type": "reading",
        "title": "Read: Growth Mindset in the Real World",
        "description": "In the decades since Carol Dweck first published her research on mindset, the concept has traveled...",
        "data": {"text": s5_reading_text}
    }

    s5_speak_reading = {
        "type": "speakReading",
        "title": "Read: Speak the Final Article Aloud",
        "description": "In the decades since Carol Dweck first published her research on mindset, the concept has traveled...",
        "data": {"text": s5_reading_text}
    }

    s5_read_along = {
        "type": "readAlong",
        "title": "Listen: Growth Mindset in the Real World",
        "description": "Listen to the passage and follow along.",
        "data": {"text": s5_reading_text}
    }

    s5_farewell = {
        "type": "introAudio",
        "title": "Farewell: Your Growth Mindset Vocabulary",
        "description": "A reflective farewell reviewing key vocabulary words and inviting you to look inward.",
        "data": {
            "text": "You have reached the end of this curriculum, but I want to suggest that you are not at the end of anything. You are at a beginning. The eighteen words you have learned are not just vocabulary. They are lenses — ways of seeing yourself, your struggles, and your potential that you did not have before. Let me leave you with a few of them to carry forward.\n\nNeuroplasticity is the brain's ability to rewire itself through experience. Here is what that means for you, personally: every difficult conversation you have, every challenging book you read, every moment you spend struggling with something you do not yet understand — your brain is physically changing in response. The discomfort you feel when learning something hard is not a sign that you are failing. It is the sensation of new neural pathways being built. Sit with that for a moment. The struggle is the growth.\n\nMalleable means able to be shaped and changed. Ask yourself honestly: do you believe your abilities are malleable? Not in the abstract — everyone says yes in the abstract. But in the moments that matter. When you get critical feedback at work, do you feel your abilities are malleable, or do you feel attacked? When you fail at something you care about, do you believe you can change, or do you quietly conclude that this is just who you are? The answer to those questions reveals your real mindset, not the one you claim to have.\n\nEmbrace means to accept willingly and enthusiastically. Dweck's research shows that growth-minded people do not just tolerate difficulty — they embrace it. But here is the uncomfortable truth: embracing difficulty is not natural. It is a choice you make against every instinct that tells you to protect yourself, to play it safe, to avoid the risk of looking foolish. The next time you feel the urge to avoid something hard, notice that urge. Name it. And then ask yourself: what would it look like to embrace this instead?\n\nCultivate means to develop something through careful attention and effort. A growth mindset is not something you achieve once and then possess forever. It is something you cultivate, day by day, choice by choice. You cultivate it when you choose to see a setback as feedback rather than a verdict. You cultivate it when you praise your own effort rather than your own talent. You cultivate it when you catch yourself thinking 'I cannot do this' and add the word 'yet.'\n\nFlourish means to grow vigorously, especially in a favorable environment. Here is my question for you: are you in an environment that helps you flourish? And if not, what can you change? Sometimes flourishing requires changing your circumstances. But more often, it requires changing how you interpret your circumstances — seeing the difficulty not as a barrier but as the very condition that makes growth possible.\n\nParadigm means a fundamental framework for understanding. You have spent five sessions learning a new paradigm — a new way of thinking about intelligence, effort, and human potential. The old paradigm says you are what you were born with. The new paradigm says you are what you choose to become. Which paradigm will you carry forward?\n\nI will not end with a motivational speech. Instead, I will end with a question — the same question that sits at the heart of everything Carol Dweck has spent her career studying. It is not: how smart are you? It is not: how talented are you? The question is: what are you willing to become? The answer is not something you say. It is something you live, one incremental choice at a time. Thank you for learning with me. Now go look inward — and then forward."
        }
    }

    session_5 = {
        "title": "Session 5: Final Reading and Farewell",
        "activities": [s5_intro, s5_reading, s5_speak_reading, s5_read_along, s5_farewell]
    }

    # ---- Assemble content ----
    content = {
        "title": "Growth Mindset: The Science of Becoming",
        "description": "WHAT IF EVERYTHING YOU BELIEVE ABOUT YOUR OWN INTELLIGENCE IS WRONG?\n\nYou have been told you are smart — or not smart enough. You have watched yourself avoid challenges because failing would mean something terrible about who you are. You have seen a colleague get promoted and thought, 'They are just naturally better at this.' You have stared at a blank page and whispered, 'I am not a writer,' as if that were a fact written into your DNA.\n\nBut what if intelligence is not a fixed trait you are born with? What if it is more like a muscle — something that grows stronger every time you push it past its comfort zone? Carol Dweck's research on growth mindset reveals that your beliefs about your own brain are the single most powerful predictor of how much you will learn, how far you will go, and whether you will crumble or flourish when things get hard.\n\nImagine rewiring the voice in your head that says 'I cannot do this' into one that says 'I cannot do this yet.' That single word — yet — is the hinge on which Dweck's entire paradigm turns. It transforms failure from a verdict into a waypoint, struggle from a threat into a signal that your brain is literally building new connections.\n\nLearn 18 powerful words drawn from the science of growth mindset. From neuroplasticity and cognition to paradigm and flourish, these words will sharpen both your English and your understanding of what it truly means to grow.",
        "preview": {
            "text": "What if the most important factor in your success is not your talent, your IQ, or your circumstances — but what you believe about your own brain? Carol Dweck's groundbreaking research on growth mindset reveals that people who believe their abilities can develop through effort consistently outperform those who believe their abilities are fixed. In this curriculum, you will master 18 upper-intermediate English words — neuroplasticity, cognition, adaptability, persevere, incremental, cultivate, feedback, setback, embrace, evolve, mastery, trajectory, fixed, innate, malleable, flourish, threshold, and paradigm — through five immersive sessions built around Dweck's transformative research. You will read original passages exploring the science of how the brain changes, practice speaking and writing with precision, and build a vocabulary that lets you discuss intelligence, effort, and human potential with the confidence of someone who truly understands the research. By the end, you will not just know these words — you will think with them."
        },
        "contentTypeTags": [],
        "sessions": [session_1, session_2, session_3, session_4, session_5]
    }

    return content


def validate(content):
    """Validate all correctness properties applicable to a single curriculum."""

    # Property 1: Vocabulary count and grouping — 18 unique words across 3 groups of 6
    all_words = []
    for i in range(3):
        session = content["sessions"][i]
        vocab_activities = [a for a in session["activities"]
                           if a["type"] in ("viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2")]
        assert len(vocab_activities) == 4, f"Session {i+1} should have 4 vocab activities, got {len(vocab_activities)}"
        words = vocab_activities[0]["vocabList"]
        assert len(words) == 6, f"Session {i+1} vocabList has {len(words)} words, expected 6"
        # All 4 vocab activities in the session must have the same vocabList
        for va in vocab_activities:
            assert va["vocabList"] == words, f"Session {i+1} vocab activities have mismatched vocabLists"
        all_words.extend(words)
    assert len(all_words) == 18, f"Expected 18 total vocab words, got {len(all_words)}"
    assert len(set(all_words)) == 18, f"Expected 18 unique vocab words, got {len(set(all_words))} unique"

    # Property 2: Session and activity counts — 5 sessions with [12, 12, 12, 4, 5]
    assert len(content["sessions"]) == 5, f"Expected 5 sessions, got {len(content['sessions'])}"
    expected_counts = [12, 12, 12, 4, 5]
    for i, session in enumerate(content["sessions"]):
        actual = len(session["activities"])
        assert actual == expected_counts[i], f"Session {i+1} has {actual} activities, expected {expected_counts[i]}"

    # Property 3: Activity type sequences
    s123_types = ["introAudio", "introAudio", "viewFlashcards", "speakFlashcards",
                  "vocabLevel1", "vocabLevel2", "reading", "speakReading",
                  "readAlong", "writingSentence", "writingSentence", "writingParagraph"]
    s4_types = ["introAudio", "reading", "speakReading", "readAlong"]
    s5_types = ["introAudio", "reading", "speakReading", "readAlong", "introAudio"]

    for i in range(3):
        actual = [a["type"] for a in content["sessions"][i]["activities"]]
        assert actual == s123_types, f"Session {i+1} activity types mismatch: {actual}"
    actual_s4 = [a["type"] for a in content["sessions"][3]["activities"]]
    assert actual_s4 == s4_types, f"Session 4 activity types mismatch: {actual_s4}"
    actual_s5 = [a["type"] for a in content["sessions"][4]["activities"]]
    assert actual_s5 == s5_types, f"Session 5 activity types mismatch: {actual_s5}"

    # Property 4: Concept content type tags — no youtubeUrl, contentTypeTags == []
    assert "youtubeUrl" not in content, "Concept curriculum should not have youtubeUrl"
    assert content["contentTypeTags"] == [], f"contentTypeTags should be [], got {content['contentTypeTags']}"

    # Property 5: vocabList correctness on vocab activities
    vocab_types = {"viewFlashcards", "speakFlashcards", "vocabLevel1", "vocabLevel2"}
    for si, session in enumerate(content["sessions"]):
        for ai, a in enumerate(session["activities"]):
            if a["type"] in vocab_types:
                assert "vocabList" in a, f"Session {si+1} activity {ai} ({a['type']}) missing vocabList"
                assert "words" not in a, f"Session {si+1} activity {ai} ({a['type']}) has 'words' key — should be 'vocabList'"
                assert len(a["vocabList"]) == 6, f"Session {si+1} activity {ai} vocabList has {len(a['vocabList'])} items, expected 6"
                assert all(isinstance(w, str) and w == w.lower() for w in a["vocabList"]), \
                    f"Session {si+1} activity {ai} vocabList contains non-lowercase or non-string items"

    # Property 6: Activity and session metadata completeness
    for si, session in enumerate(content["sessions"]):
        assert "title" in session and isinstance(session["title"], str) and session["title"].strip(), \
            f"Session {si+1} missing or empty title"
        for ai, a in enumerate(session["activities"]):
            assert "title" in a and isinstance(a["title"], str) and a["title"].strip(), \
                f"Session {si+1} activity {ai} missing or empty title"
            assert "description" in a and isinstance(a["description"], str) and a["description"].strip(), \
                f"Session {si+1} activity {ai} missing or empty description"

    # Property 7: Strip keys absence
    def check_no_strip_keys(obj, path=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                assert k not in STRIP_KEYS, f"Strip key '{k}' found at {path}.{k}"
                check_no_strip_keys(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                check_no_strip_keys(item, f"{path}[{i}]")
    check_no_strip_keys(content)

    # Property 8: Vocab teaching script word count (500-800 words) — index 1 in sessions 1-3
    for i in range(3):
        text = content["sessions"][i]["activities"][1]["data"]["text"]
        word_count = len(text.split())
        assert 500 <= word_count <= 800, \
            f"Session {i+1} vocab teaching introAudio has {word_count} words, expected 500-800"

    print("All validations passed.")


def create():
    """Build content, validate, and create curriculum via API."""
    token = get_firebase_id_token(UID)
    content = build_content()
    content = strip_keys(content)
    validate(content)

    response = requests.post(f"{BASE_URL}/curriculum/create", json={
        "firebaseIdToken": token,
        "language": "en",
        "userLanguage": "en",
        "content": json.dumps(content)
    })
    response.raise_for_status()
    result = response.json()
    curriculum_id = result["id"]
    print(f"Created curriculum: {curriculum_id}")
    print(f"\n-- Duplicate check SQL:")
    print(f"SELECT id, content->>'title' as title, created_at FROM curriculum")
    print(f"WHERE content->>'title' = 'Growth Mindset: The Science of Becoming'")
    print(f"  AND uid = '{UID}' ORDER BY created_at;")
    return curriculum_id


if __name__ == "__main__":
    create()
