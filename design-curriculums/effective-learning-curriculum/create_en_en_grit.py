"""
Create en-en Grit podcast curriculum.
Angela Duckworth's "Grit: The Power of Passion and Perseverance" TED Talk.
Language: en-en (English speakers learning English vocabulary)
Description tone: bold_declaration
Farewell tone: warm accountability
"""

import sys
import json
import requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
BASE_URL = "https://helloapi.step.is"

# --- Vocabulary ---
# Group 1 (Session 1): perseverance, stamina, tenacity, resilience, diligence, fortitude
# Group 2 (Session 2): passion, aptitude, deliberate, consistency, endurance, determination
# Group 3 (Session 3): grit, predictor, achievement, talent, potential, mindset

VOCAB_GROUP_1 = ["perseverance", "stamina", "tenacity", "resilience", "diligence", "fortitude"]
VOCAB_GROUP_2 = ["passion", "aptitude", "deliberate", "consistency", "endurance", "determination"]
VOCAB_GROUP_3 = ["grit", "predictor", "achievement", "talent", "potential", "mindset"]
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
        "title": "Introduction to Grit",
        "description": "An overview of Angela Duckworth's research on grit and why passion plus perseverance matters more than talent.",
        "data": {
            "text": "Welcome to Grit: The Power of Passion and Perseverance. In this curriculum, you will explore one of the most important ideas in modern psychology — the concept of grit. Angela Duckworth, a psychologist and former teacher, spent years studying what separates high achievers from everyone else. Her conclusion was surprising and powerful: it is not talent, not IQ, not social intelligence that predicts success. It is grit — the combination of passion and perseverance for long-term goals. Duckworth discovered this pattern everywhere she looked. At West Point Military Academy, the cadets who survived the grueling first summer of training were not the strongest or the smartest. They were the grittiest. In the National Spelling Bee, the children who advanced to the final rounds were not necessarily the ones with the highest verbal IQ scores. They were the ones who practiced the hardest and the longest. In her TED Talk, Duckworth shares her journey from management consulting to teaching seventh-grade math in New York City public schools. She noticed that her best students were not always the ones with the most natural ability. The students who thrived were the ones who worked hard, stayed committed, and did not give up when things got difficult. This observation launched her into a career studying the psychology of achievement. Over the next five sessions, you will learn eighteen vocabulary words that capture the essence of Duckworth's research. These words will help you talk about effort, persistence, and the qualities that drive long-term success. Today, in Session One, we will focus on six words that describe the inner qualities of gritty people: perseverance, stamina, tenacity, resilience, diligence, and fortitude. Let us begin."
        }
    }

    s1_intro_vocab = {
        "type": "introAudio",
        "title": "Vocabulary: The Inner Qualities of Grit",
        "description": "Learn six words that describe the inner qualities of gritty people: perseverance, stamina, tenacity, resilience, diligence, and fortitude.",
        "data": {
            "text": "In this session, you will learn six words that describe the inner qualities of people who demonstrate grit. These are the traits Angela Duckworth found again and again in high achievers — not brilliance, not luck, but deep personal qualities that sustain effort over time. Let us walk through each word carefully. The first word is perseverance. Perseverance is a noun that means continued effort and determination despite difficulties, failure, or delay. When Duckworth studied cadets at West Point, she found that perseverance was the single best predictor of who would survive the brutal first summer of training known as Beast Barracks. The cadets who made it through were not the fastest or the strongest. They were the ones who kept going when every part of them wanted to quit. Perseverance is the refusal to stop, even when the path is painful. The second word is stamina. Stamina is a noun meaning the physical or mental strength to sustain prolonged effort. Duckworth emphasizes that grit is not a sprint — it is a marathon. You need stamina to pursue a goal for years, not just weeks. The spelling bee champions she studied did not just practice the night before the competition. They practiced for months and years, building the stamina to endure thousands of hours of repetitive study. Stamina is what keeps you standing when the work stretches on far longer than you expected. The third word is tenacity. Tenacity is a noun that means the quality of holding firmly to something — a purpose, a belief, a course of action. It comes from the Latin word tenax, meaning holding fast. Tenacity is what you see in a student who fails a math test, studies harder, fails again, and still comes back for more. It is the grip that refuses to loosen. Duckworth describes gritty individuals as people who hold on to their goals with a tenacity that others find almost unreasonable. The fourth word is resilience. Resilience is a noun meaning the ability to recover quickly from setbacks, difficulties, or failure. Resilience is not about avoiding failure — it is about bouncing back from it. Duckworth found that gritty people experience just as many setbacks as everyone else. The difference is that they treat failure as a temporary condition, not a permanent identity. A resilient person falls down and gets back up. They do not interpret a bad result as proof that they are not good enough. They interpret it as information about what to do differently next time. The fifth word is diligence. Diligence is a noun meaning careful, persistent effort and hard work. While perseverance emphasizes not giving up, diligence emphasizes the quality of the effort itself. A diligent student does not just put in hours — they put in focused, thoughtful hours. Duckworth's research shows that gritty people are not just persistent; they are deliberately persistent. They pay attention to what they are doing, seek feedback, and refine their approach. Diligence is perseverance with precision. The sixth and final word for this session is fortitude. Fortitude is a noun meaning courage and strength in the face of pain, adversity, or danger. Fortitude is the emotional backbone of grit. It is what allows someone to endure not just physical hardship but emotional difficulty — the loneliness of working toward a goal that nobody else understands, the frustration of slow progress, the fear that the effort might not pay off. Duckworth argues that fortitude is what separates people who dream big from people who actually achieve big. Dreams are easy. Fortitude is what makes them real. Let us review all six words one more time: perseverance, the refusal to stop despite difficulty; stamina, the strength to sustain prolonged effort; tenacity, the firm grip on your goals; resilience, the ability to bounce back from failure; diligence, careful and persistent hard work; and fortitude, courage in the face of adversity. You will encounter all six of these words in the reading passage that follows. Pay attention to how they appear in context, and think about how they connect to Duckworth's research on grit."
        }
    }

    s1_view_flashcards = {
        "type": "viewFlashcards",
        "title": "Flashcards: Inner Qualities of Grit",
        "description": "Learn 6 words: perseverance, stamina, tenacity, resilience, diligence, fortitude.",
        "vocabList": VOCAB_GROUP_1
    }

    s1_speak_flashcards = {
        "type": "speakFlashcards",
        "title": "Flashcards: Speak the Words",
        "description": "Practice pronouncing: perseverance, stamina, tenacity, resilience, diligence, fortitude.",
        "vocabList": VOCAB_GROUP_1
    }

    s1_vocab_level1 = {
        "type": "vocabLevel1",
        "title": "Flashcards: Vocabulary Level 1",
        "description": "Test your knowledge of: perseverance, stamina, tenacity, resilience, diligence, fortitude.",
        "vocabList": VOCAB_GROUP_1
    }

    s1_vocab_level2 = {
        "type": "vocabLevel2",
        "title": "Flashcards: Vocabulary Level 2",
        "description": "Advanced practice with: perseverance, stamina, tenacity, resilience, diligence, fortitude.",
        "vocabList": VOCAB_GROUP_1
    }

    s1_reading_text = "Angela Duckworth did not set out to study grit. She started her career in management consulting, a world that rewards quick thinking and fast results. But something nagged at her. She left consulting, became a math teacher in New York City public schools, and noticed something that changed the direction of her life: the students who succeeded were not always the ones with the most natural ability. They were the ones with perseverance — the ones who kept working through confusion and frustration long after their peers had given up.\n\nThis observation sent Duckworth into the world of psychology research, where she began studying what she would eventually call grit. Her research took her to West Point Military Academy, where thousands of cadets arrive each summer for a punishing initiation known as Beast Barracks. The physical and mental demands are extreme. Every year, a significant number of cadets drop out. Duckworth wanted to know who would survive and who would quit. She found that the best predictor was not physical stamina alone, though stamina certainly mattered. It was a combination of stamina and something deeper — a tenacity that kept cadets pushing forward even when their bodies and minds screamed at them to stop.\n\nDuckworth saw the same pattern in the National Spelling Bee. The children who reached the final rounds were not necessarily the ones with the highest IQ scores. They were the ones who demonstrated extraordinary resilience in the face of failure. They misspelled words, went home, studied harder, and came back the next year. Their diligence was remarkable — not just the number of hours they practiced, but the quality of those hours. They sought out the hardest words, the ones most likely to trip them up, and drilled them relentlessly.\n\nWhat struck Duckworth most was the emotional dimension of grit. It was not enough to be physically tough or intellectually sharp. The grittiest people she studied possessed a kind of fortitude that went beyond mere toughness. They had the courage to keep believing in their goals when everyone around them had doubts. They endured loneliness, boredom, and the slow grind of incremental progress without losing sight of why they started. Fortitude, Duckworth realized, was the emotional engine that powered everything else."

    s1_reading = {
        "type": "reading",
        "title": "Read: The Discovery of Grit",
        "description": "Angela Duckworth did not set out to study grit. She started her career in management consulting...",
        "data": {"text": s1_reading_text}
    }

    s1_speak_reading = {
        "type": "speakReading",
        "title": "Read: Speak the Passage Aloud",
        "description": "Angela Duckworth did not set out to study grit. She started her career in management consulting...",
        "data": {"text": s1_reading_text}
    }

    s1_read_along = {
        "type": "readAlong",
        "title": "Listen: The Discovery of Grit",
        "description": "Listen to the passage and follow along.",
        "data": {"text": s1_reading_text}
    }

    s1_writing_sentence_1 = {
        "type": "writingSentence",
        "title": "Write: Using 'perseverance'",
        "description": "Write a sentence using the word perseverance.",
        "data": {
            "prompt": "Use the word 'perseverance' in a sentence about someone who refused to give up on a long-term goal. Example: Her perseverance through three years of failed experiments finally led to a breakthrough that changed the field.",
            "vocabWord": "perseverance"
        }
    }

    s1_writing_sentence_2 = {
        "type": "writingSentence",
        "title": "Write: Using 'resilience'",
        "description": "Write a sentence using the word resilience.",
        "data": {
            "prompt": "Use the word 'resilience' in a sentence about recovering from a difficult experience. Example: The team's resilience after losing the championship game impressed their coach, who watched them return to practice the very next morning with renewed focus.",
            "vocabWord": "resilience"
        }
    }

    s1_writing_paragraph = {
        "type": "writingParagraph",
        "title": "Write: Reflecting on Inner Strength",
        "description": "Write a paragraph about the inner qualities that help people persist through challenges.",
        "data": {
            "prompt": "Think about a time when you or someone you know faced a significant challenge that required sustained effort over weeks or months. Write a paragraph describing that experience using at least four of the following words: perseverance, stamina, tenacity, resilience, diligence, fortitude. Explain what made the challenge difficult and what inner qualities helped the person push through.",
            "vocabList": VOCAB_GROUP_1
        }
    }

    session_1 = {
        "title": "Session 1: The Inner Qualities of Grit",
        "activities": [
            s1_intro_topic, s1_intro_vocab, s1_view_flashcards, s1_speak_flashcards,
            s1_vocab_level1, s1_vocab_level2, s1_reading, s1_speak_reading,
            s1_read_along, s1_writing_sentence_1, s1_writing_sentence_2, s1_writing_paragraph
        ]
    }

    # ---- Session 2: Group 2 vocabulary ----
    s2_intro_topic = {
        "type": "introAudio",
        "title": "The Fuel Behind Grit",
        "description": "Exploring how passion, deliberate practice, and determination drive long-term achievement.",
        "data": {
            "text": "Welcome back. In Session One, you learned six words that describe the inner qualities of gritty people — perseverance, stamina, tenacity, resilience, diligence, and fortitude. These are the traits that keep someone going when the work gets hard. But Duckworth's research reveals something equally important: grit is not just about toughness. It is also about direction. The grittiest people she studied were not just persistent — they were passionate. They had found something that mattered deeply to them, and they pursued it with a consistency that lasted years, sometimes decades. In this session, you will learn six new words that capture the fuel behind grit: passion, aptitude, deliberate, consistency, endurance, and determination. These words describe not just the effort, but the purpose and strategy behind it. Let us begin."
        }
    }

    s2_intro_vocab = {
        "type": "introAudio",
        "title": "Vocabulary: The Fuel Behind Grit",
        "description": "Learn six words about the driving forces of grit: passion, aptitude, deliberate, consistency, endurance, and determination.",
        "data": {
            "text": "In Session One, you learned about the inner qualities that sustain gritty people — perseverance, stamina, tenacity, resilience, diligence, and fortitude. Now, in Session Two, we turn to the forces that drive grit forward. These six words describe the purpose, strategy, and sustained energy behind long-term achievement. Let us explore each one. The first word is passion. Passion is a noun meaning a strong, barely controllable emotion or an intense enthusiasm for something. In the context of grit, Duckworth uses passion in a very specific way. She does not mean a fleeting burst of excitement. She means a deep, enduring commitment to a particular interest or goal. The grittiest people she studied had found their passion early and stuck with it for years. A passionate musician does not just enjoy playing — they organize their entire life around getting better at it. Passion is the compass that gives grit its direction. The second word is aptitude. Aptitude is a noun meaning a natural ability or talent for learning something. Duckworth's research challenges the common belief that aptitude is the most important factor in success. She found that people with high aptitude but low grit often underperformed compared to people with moderate aptitude but high grit. Aptitude gives you a head start, but it does not carry you to the finish line. A student with a natural aptitude for mathematics still needs to practice, study, and push through difficult problems. Aptitude opens the door, but effort is what walks you through it. The third word is deliberate. Deliberate is an adjective meaning done consciously and intentionally, with careful thought. Duckworth emphasizes the importance of deliberate practice — a concept developed by psychologist Anders Ericsson. Deliberate practice is not just doing something over and over. It is focused, structured effort aimed at improving specific weaknesses. A deliberate learner does not just read a chapter and move on. They identify what they do not understand, seek feedback, and practice the hardest parts until they improve. Deliberate effort is what separates productive practice from mindless repetition. The fourth word is consistency. Consistency is a noun meaning the quality of always behaving or performing in a similar way, or of always happening in a similar way. Duckworth found that consistency of effort over time was one of the strongest markers of grit. It is not about having one great day of work. It is about showing up every day, even when motivation is low. A consistent runner does not just train when they feel inspired — they train on the days when they would rather stay in bed. Consistency is the quiet, unglamorous backbone of every great achievement. The fifth word is endurance. Endurance is a noun meaning the ability to withstand hardship, adversity, or stress over a prolonged period. While stamina often refers to physical or mental energy, endurance emphasizes the ability to last through difficulty. Duckworth's research shows that gritty people have remarkable endurance — they can sustain effort through years of slow progress, setbacks, and uncertainty. Endurance is what keeps a doctoral student working on their dissertation for five years, or an entrepreneur rebuilding after a failed business. It is the long game, played with patience. The sixth and final word for this session is determination. Determination is a noun meaning firmness of purpose or the resolve to achieve a goal. Determination is closely related to perseverance, but with an important distinction: determination emphasizes the decision to pursue a goal, while perseverance emphasizes the act of continuing despite obstacles. A determined person has made a conscious choice about what they want and has committed to pursuing it. Duckworth describes determination as the moment when grit crystallizes — when a person stops dabbling and starts committing. Let us review all six words together: passion, the deep commitment that gives grit its direction; aptitude, natural ability that provides a starting point but not a guarantee; deliberate, the intentional and focused approach to practice and improvement; consistency, the quality of showing up and performing day after day; endurance, the ability to withstand prolonged difficulty; and determination, the firmness of purpose that turns interest into commitment. You will see all six of these words in the reading passage ahead. Notice how they connect to the ideas from Session One and deepen your understanding of what grit really means."
        }
    }

    s2_view_flashcards = {
        "type": "viewFlashcards",
        "title": "Flashcards: The Fuel Behind Grit",
        "description": "Learn 6 words: passion, aptitude, deliberate, consistency, endurance, determination.",
        "vocabList": VOCAB_GROUP_2
    }

    s2_speak_flashcards = {
        "type": "speakFlashcards",
        "title": "Flashcards: Speak the Words",
        "description": "Practice pronouncing: passion, aptitude, deliberate, consistency, endurance, determination.",
        "vocabList": VOCAB_GROUP_2
    }

    s2_vocab_level1 = {
        "type": "vocabLevel1",
        "title": "Flashcards: Vocabulary Level 1",
        "description": "Test your knowledge of: passion, aptitude, deliberate, consistency, endurance, determination.",
        "vocabList": VOCAB_GROUP_2
    }

    s2_vocab_level2 = {
        "type": "vocabLevel2",
        "title": "Flashcards: Vocabulary Level 2",
        "description": "Advanced practice with: passion, aptitude, deliberate, consistency, endurance, determination.",
        "vocabList": VOCAB_GROUP_2
    }

    s2_reading_text = "Angela Duckworth's research forced her to confront an uncomfortable truth about how society thinks about success. We celebrate talent. We admire natural aptitude. We tell stories about prodigies who seem to achieve greatness effortlessly. But Duckworth's data told a different story. Aptitude, she found, was a poor predictor of long-term success. What mattered far more was what people did with their abilities — and how long they kept doing it.\n\nAt the heart of Duckworth's framework is a simple but powerful idea: effort counts twice. Talent multiplied by effort produces skill. Skill multiplied by effort produces achievement. This means that someone with moderate aptitude but extraordinary effort will, over time, outperform someone with extraordinary aptitude but moderate effort. The math is clear, but the implications are profound. It means that the most important variable in the equation of success is not what you are born with — it is what you choose to do, day after day, with deliberate intention.\n\nDuckworth found that the grittiest people she studied shared a common trait: passion. But not the kind of passion that burns hot and fades fast. She means a sustained, enduring passion — a deep interest that organizes a person's life for years or even decades. The spelling bee champions did not just enjoy words for a season. They were fascinated by language in a way that lasted. The West Point cadets who survived Beast Barracks were not just tough for a summer. They had a passion for military service that gave their suffering meaning.\n\nThis passion was paired with consistency. The gritty individuals in Duckworth's studies did not work in bursts of inspiration followed by long periods of inactivity. They showed up every day. They practiced with consistency that others found boring or even obsessive. But for them, it was not obsession — it was commitment. They had made a determination about what mattered to them, and they honored that determination through daily action.\n\nDuckworth also emphasizes the role of deliberate practice. Drawing on the work of psychologist Anders Ericsson, she argues that gritty people do not just practice more — they practice better. Their practice is deliberate: focused on specific weaknesses, guided by feedback, and designed to push them just beyond their current ability. This kind of practice requires endurance, because it is inherently uncomfortable. Deliberate practice means spending time on the things you are worst at, not the things you enjoy most. It means seeking out criticism rather than praise. It means enduring the frustration of slow improvement because you trust that the process works.\n\nThe combination of passion, deliberate practice, consistency, and endurance is what Duckworth calls the engine of grit. Aptitude may determine where you start, but determination — the firm resolve to keep going — determines where you finish."

    s2_reading = {
        "type": "reading",
        "title": "Read: The Engine of Grit",
        "description": "Angela Duckworth's research forced her to confront an uncomfortable truth about how society thinks...",
        "data": {"text": s2_reading_text}
    }

    s2_speak_reading = {
        "type": "speakReading",
        "title": "Read: Speak the Passage Aloud",
        "description": "Angela Duckworth's research forced her to confront an uncomfortable truth about how society thinks...",
        "data": {"text": s2_reading_text}
    }

    s2_read_along = {
        "type": "readAlong",
        "title": "Listen: The Engine of Grit",
        "description": "Listen to the passage and follow along.",
        "data": {"text": s2_reading_text}
    }

    s2_writing_sentence_1 = {
        "type": "writingSentence",
        "title": "Write: Using 'deliberate'",
        "description": "Write a sentence using the word deliberate.",
        "data": {
            "prompt": "Use the word 'deliberate' in a sentence about someone who practices or studies with focused intention. Example: His deliberate approach to learning the piano — targeting his weakest passages first — helped him improve faster than students who simply played their favorite songs.",
            "vocabWord": "deliberate"
        }
    }

    s2_writing_sentence_2 = {
        "type": "writingSentence",
        "title": "Write: Using 'consistency'",
        "description": "Write a sentence using the word consistency.",
        "data": {
            "prompt": "Use the word 'consistency' in a sentence about the importance of regular effort over time. Example: It was not any single brilliant performance that earned her the promotion, but the consistency of her work over three years that convinced her managers she was ready.",
            "vocabWord": "consistency"
        }
    }

    s2_writing_paragraph = {
        "type": "writingParagraph",
        "title": "Write: Reflecting on Effort and Direction",
        "description": "Write a paragraph about how passion and deliberate effort drive achievement.",
        "data": {
            "prompt": "Duckworth argues that effort counts twice: talent times effort equals skill, and skill times effort equals achievement. Think about a skill you have developed over time — it could be academic, athletic, artistic, or professional. Write a paragraph describing how passion, deliberate practice, consistency, or determination played a role in your development. Use at least four of the session vocabulary words.",
            "vocabList": VOCAB_GROUP_2
        }
    }

    session_2 = {
        "title": "Session 2: The Fuel Behind Grit",
        "activities": [
            s2_intro_topic, s2_intro_vocab, s2_view_flashcards, s2_speak_flashcards,
            s2_vocab_level1, s2_vocab_level2, s2_reading, s2_speak_reading,
            s2_read_along, s2_writing_sentence_1, s2_writing_sentence_2, s2_writing_paragraph
        ]
    }

    # ---- Session 3: Group 3 vocabulary ----
    s3_intro_topic = {
        "type": "introAudio",
        "title": "Grit, Talent, and the Growth Mindset",
        "description": "Exploring the relationship between grit, talent, achievement, and the mindset that makes long-term success possible.",
        "data": {
            "text": "Welcome to Session Three. Over the past two sessions, you have built a powerful vocabulary for talking about grit. In Session One, you learned about the inner qualities — perseverance, stamina, tenacity, resilience, diligence, and fortitude. In Session Two, you explored the driving forces — passion, aptitude, deliberate practice, consistency, endurance, and determination. Now, in this final teaching session, we bring it all together. You will learn six words that capture the big picture of Duckworth's research: grit itself, the concept of predictors, the nature of achievement, the role of talent, the idea of potential, and the power of mindset. These words will help you discuss not just what grit is, but why it matters — and how it connects to the broader science of human performance. Let us begin."
        }
    }

    s3_intro_vocab = {
        "type": "introAudio",
        "title": "Vocabulary: The Big Picture of Grit",
        "description": "Learn six words about the broader framework of grit: grit, predictor, achievement, talent, potential, and mindset.",
        "data": {
            "text": "You have already learned twelve words across two sessions. In Session One, you explored the inner qualities of gritty people: perseverance, stamina, tenacity, resilience, diligence, and fortitude. In Session Two, you studied the driving forces behind grit: passion, aptitude, deliberate practice, consistency, endurance, and determination. Now, in Session Three, you will learn six words that frame the big picture of Duckworth's research — the concepts that tie everything together. The first word is grit. Grit is a noun meaning courage, resolve, and strength of character — specifically, the combination of passion and perseverance for long-term goals. Duckworth defines grit as the tendency to sustain interest in and effort toward very long-term goals. It is not about being tough in a single moment. It is about being tough across years. Grit is what keeps a medical student going through a decade of training. It is what keeps an entrepreneur rebuilding after multiple failures. In Duckworth's framework, grit is the master trait — the quality that encompasses perseverance, passion, consistency, and all the other words you have learned. The second word is predictor. A predictor is a noun meaning a factor or variable that can be used to forecast an outcome. In Duckworth's research, she tested many potential predictors of success: IQ, physical fitness, social intelligence, leadership ability. But the strongest predictor, again and again, was grit. At West Point, grit scores predicted who would complete Beast Barracks better than any other measure. In the spelling bee, grit predicted who would advance to the final rounds. A predictor is not a guarantee — it is a statistical pattern. But the consistency of grit as a predictor across such different domains is what makes Duckworth's findings so compelling. The third word is achievement. Achievement is a noun meaning a thing accomplished through effort, skill, or courage. Duckworth draws a careful distinction between talent and achievement. Talent is what you can do naturally. Achievement is what you actually accomplish through sustained effort. Her formula — talent times effort equals skill, skill times effort equals achievement — shows that effort enters the equation twice. Achievement is not handed to you. It is built, brick by brick, through the daily application of effort to skill. The fourth word is talent. Talent is a noun meaning a natural aptitude or skill. Duckworth does not dismiss talent. She acknowledges that some people have natural advantages in certain areas. But she argues forcefully that our culture overvalues talent and undervalues effort. We are drawn to stories of natural genius because they are exciting and romantic. But the data shows that talent without effort is just unmet potential. A talented musician who never practices will be outperformed by a less talented musician who practices every day with deliberate focus. Talent matters, but it is not destiny. The fifth word is potential. Potential is a noun meaning latent qualities or abilities that may be developed and lead to future success. Duckworth's work suggests that everyone has more potential than they realize. The limiting factor is rarely ability — it is effort, persistence, and the willingness to endure discomfort. Potential is what exists before effort transforms it into achievement. A student with potential has the raw material for success, but without grit, that potential remains unrealized. Duckworth's message is hopeful: if grit can be developed, then potential can be unlocked at any stage of life. The sixth and final word is mindset. Mindset is a noun meaning a person's way of thinking and their established set of attitudes. Duckworth draws heavily on the work of Carol Dweck, who identified two types of mindset: fixed and growth. A fixed mindset believes that abilities are set in stone — you are either smart or you are not. A growth mindset believes that abilities can be developed through effort and learning. Duckworth argues that a growth mindset is essential to grit. If you believe your abilities are fixed, there is no reason to persist through difficulty. But if you believe you can grow, then every challenge becomes an opportunity. Mindset is the lens through which gritty people see the world. Let us review all six words: grit, the master trait combining passion and perseverance; predictor, a factor that forecasts outcomes; achievement, what is accomplished through sustained effort; talent, natural ability that is necessary but not sufficient; potential, the latent capacity waiting to be developed; and mindset, the way of thinking that determines whether you persist or give up. These six words complete your vocabulary for understanding Duckworth's research. In the reading passage ahead, you will see how they all connect."
        }
    }

    s3_view_flashcards = {
        "type": "viewFlashcards",
        "title": "Flashcards: The Big Picture of Grit",
        "description": "Learn 6 words: grit, predictor, achievement, talent, potential, mindset.",
        "vocabList": VOCAB_GROUP_3
    }

    s3_speak_flashcards = {
        "type": "speakFlashcards",
        "title": "Flashcards: Speak the Words",
        "description": "Practice pronouncing: grit, predictor, achievement, talent, potential, mindset.",
        "vocabList": VOCAB_GROUP_3
    }

    s3_vocab_level1 = {
        "type": "vocabLevel1",
        "title": "Flashcards: Vocabulary Level 1",
        "description": "Test your knowledge of: grit, predictor, achievement, talent, potential, mindset.",
        "vocabList": VOCAB_GROUP_3
    }

    s3_vocab_level2 = {
        "type": "vocabLevel2",
        "title": "Flashcards: Vocabulary Level 2",
        "description": "Advanced practice with: grit, predictor, achievement, talent, potential, mindset.",
        "vocabList": VOCAB_GROUP_3
    }

    s3_reading_text = "When Angela Duckworth stepped onto the TED stage in 2013, she carried with her a simple but radical message: the quality that matters most for success is not talent. It is grit. Her six-minute talk would go on to become one of the most-watched TED Talks in history, viewed over twenty million times. The reason is not hard to understand. Duckworth was challenging one of our deepest cultural assumptions — that achievement is primarily a product of talent.\n\nDuckworth's journey to this insight began in the classroom. As a seventh-grade math teacher, she noticed that her highest-performing students were not always the ones with the greatest natural talent. Some students with obvious aptitude coasted through easy problems but crumbled when the work got hard. Meanwhile, other students with more modest abilities worked with a determination that was almost fierce. They asked questions, sought help, practiced relentlessly, and gradually overtook their more talented peers. This pattern fascinated Duckworth and eventually led her to graduate school in psychology.\n\nHer research confirmed what she had observed in the classroom. Across every domain she studied — military training, spelling competitions, sales, teaching — grit was a stronger predictor of success than talent, IQ, or any other single factor. This finding was both encouraging and unsettling. Encouraging because it meant that achievement was not reserved for the naturally gifted. Unsettling because it meant that our cultural obsession with talent was not just wrong — it was actively harmful. By celebrating talent above effort, we send the message that if something does not come easily, you are probably not cut out for it. This mindset, Duckworth argues, is the enemy of grit.\n\nDuckworth connects her work to Carol Dweck's research on mindset. Dweck found that people with a growth mindset — those who believe abilities can be developed — are more likely to embrace challenges, persist through setbacks, and ultimately achieve more than people with a fixed mindset. Duckworth sees growth mindset as the psychological foundation of grit. If you believe your potential is fixed, there is no reason to push through difficulty. But if you believe your potential can expand with effort, then every obstacle becomes a chance to grow.\n\nThe implications of Duckworth's research extend far beyond individual achievement. She argues that schools, workplaces, and families can all cultivate grit by creating environments that reward effort over talent, that normalize struggle, and that help people find and develop their passions. The potential for change is enormous. If grit can be taught and developed — and Duckworth believes it can — then the gap between who we are and who we could become is not a matter of talent. It is a matter of effort, sustained over time, guided by passion, and supported by the right mindset."

    s3_reading = {
        "type": "reading",
        "title": "Read: Why Grit Matters More Than Talent",
        "description": "When Angela Duckworth stepped onto the TED stage in 2013, she carried with her a simple but radical...",
        "data": {"text": s3_reading_text}
    }

    s3_speak_reading = {
        "type": "speakReading",
        "title": "Read: Speak the Passage Aloud",
        "description": "When Angela Duckworth stepped onto the TED stage in 2013, she carried with her a simple but radical...",
        "data": {"text": s3_reading_text}
    }

    s3_read_along = {
        "type": "readAlong",
        "title": "Listen: Why Grit Matters More Than Talent",
        "description": "Listen to the passage and follow along.",
        "data": {"text": s3_reading_text}
    }

    s3_writing_sentence_1 = {
        "type": "writingSentence",
        "title": "Write: Using 'mindset'",
        "description": "Write a sentence using the word mindset.",
        "data": {
            "prompt": "Use the word 'mindset' in a sentence about how a person's beliefs affect their ability to learn or grow. Example: Adopting a growth mindset transformed her approach to failure — instead of seeing mistakes as proof of her limitations, she began treating them as essential steps in the learning process.",
            "vocabWord": "mindset"
        }
    }

    s3_writing_sentence_2 = {
        "type": "writingSentence",
        "title": "Write: Using 'achievement'",
        "description": "Write a sentence using the word achievement.",
        "data": {
            "prompt": "Use the word 'achievement' in a sentence about something that was accomplished through sustained effort rather than natural ability. Example: His greatest achievement was not winning the award itself, but the five years of disciplined practice that made it possible.",
            "vocabWord": "achievement"
        }
    }

    s3_writing_paragraph = {
        "type": "writingParagraph",
        "title": "Write: Reflecting on Talent vs. Effort",
        "description": "Write a paragraph about the relationship between talent, effort, and achievement.",
        "data": {
            "prompt": "Duckworth argues that our culture overvalues talent and undervalues effort. Do you agree? Think about an area of your life where you have seen someone with less natural talent outperform someone with more talent through sheer effort and persistence. Write a paragraph exploring this idea, using at least four of the following words: grit, predictor, achievement, talent, potential, mindset.",
            "vocabList": VOCAB_GROUP_3
        }
    }

    session_3 = {
        "title": "Session 3: Grit, Talent, and the Growth Mindset",
        "activities": [
            s3_intro_topic, s3_intro_vocab, s3_view_flashcards, s3_speak_flashcards,
            s3_vocab_level1, s3_vocab_level2, s3_reading, s3_speak_reading,
            s3_read_along, s3_writing_sentence_1, s3_writing_sentence_2, s3_writing_paragraph
        ]
    }

    # ---- Session 4: Review (full article) ----
    s4_reading_text = "There is a moment in Angela Duckworth's TED Talk that captures the essence of her entire body of work. She describes standing in front of a classroom of seventh graders, watching some students thrive while others — students with every apparent advantage — slowly disengage. The students who succeeded were not the ones with the most talent or the highest aptitude. They were the ones with perseverance. They were the ones who treated difficulty not as a signal to stop, but as a signal to push harder.\n\nThis observation became the foundation of a research career that would challenge how we think about achievement. Duckworth left teaching to pursue a doctorate in psychology, driven by a single question: what predicts success? She studied cadets at West Point Military Academy, where she found that grit — not physical stamina, not leadership scores, not academic grades — was the strongest predictor of who would complete the punishing first summer of training. She studied competitors in the National Spelling Bee, where she found that the children who advanced furthest were not the ones with the highest IQ scores but the ones who practiced with the most diligence and tenacity. She studied salespeople, teachers, and students across dozens of settings, and the pattern held: grit predicted achievement better than any other single variable.\n\nBut what exactly is grit? Duckworth defines it as the combination of passion and perseverance for long-term goals. It is not just about working hard in the moment. It is about maintaining effort and interest over years — sometimes decades. The grittiest people Duckworth studied had found something they cared about deeply, and they pursued it with a consistency that bordered on obsession. Their passion was not a fleeting enthusiasm. It was a sustained commitment that organized their daily lives.\n\nThis passion was paired with deliberate effort. Duckworth draws on the work of Anders Ericsson to argue that gritty people do not just practice more — they practice with intention. Their practice is deliberate, focused on specific weaknesses, and designed to push them beyond their comfort zone. This kind of practice requires extraordinary endurance, because it is inherently uncomfortable. You are spending your time on the things you are worst at, not the things you enjoy most. But gritty people embrace this discomfort because they understand that it is the price of improvement.\n\nDuckworth's research also reveals the critical role of mindset. Drawing on Carol Dweck's work, she argues that a growth mindset — the belief that abilities can be developed through effort — is essential to grit. People with a fixed mindset see difficulty as evidence of their limitations. People with a growth mindset see difficulty as an opportunity to grow. This difference in mindset has profound consequences for resilience. When a growth-minded person fails, they do not conclude that they lack talent. They conclude that they need to try a different approach, work harder, or seek better guidance.\n\nPerhaps the most powerful implication of Duckworth's work is that grit can be developed. It is not a fixed trait that you either have or you do not. Duckworth identifies four psychological assets that contribute to grit: interest, practice, purpose, and hope. Interest means finding something that fascinates you. Practice means committing to deliberate improvement. Purpose means believing that your work matters to others. And hope means maintaining the determination to keep going even when progress is slow.\n\nThe potential of this framework is enormous. If grit can be cultivated — through parenting, teaching, coaching, and personal effort — then the gap between where we are and where we could be is not determined by talent. It is determined by the fortitude to keep working, the resilience to recover from setbacks, and the endurance to sustain effort across the long arc of a meaningful life. Duckworth's message is both a challenge and an invitation: the most important thing about you is not how talented you are. It is how hard you are willing to work, and for how long."

    s4_intro = {
        "type": "introAudio",
        "title": "Review: The Complete Picture of Grit",
        "description": "A review session bringing together all 18 vocabulary words in a comprehensive article about grit.",
        "data": {
            "text": "Welcome to Session Four. Over the past three sessions, you have learned eighteen vocabulary words that capture the science of grit. In Session One, you explored the inner qualities: perseverance, stamina, tenacity, resilience, diligence, and fortitude. In Session Two, you studied the driving forces: passion, aptitude, deliberate, consistency, endurance, and determination. In Session Three, you examined the big picture: grit, predictor, achievement, talent, potential, and mindset. Now it is time to see all eighteen words working together in a single, comprehensive article about Angela Duckworth's research. This article weaves together everything you have learned. As you read, notice how the words connect to each other and to the broader themes of Duckworth's TED Talk. Let us begin."
        }
    }

    s4_reading = {
        "type": "reading",
        "title": "Read: The Science of Grit — A Complete Overview",
        "description": "There is a moment in Angela Duckworth's TED Talk that captures the essence of her entire body of...",
        "data": {"text": s4_reading_text}
    }

    s4_speak_reading = {
        "type": "speakReading",
        "title": "Read: Speak the Full Article Aloud",
        "description": "There is a moment in Angela Duckworth's TED Talk that captures the essence of her entire body of...",
        "data": {"text": s4_reading_text}
    }

    s4_read_along = {
        "type": "readAlong",
        "title": "Listen: The Science of Grit — A Complete Overview",
        "description": "Listen to the passage and follow along.",
        "data": {"text": s4_reading_text}
    }

    session_4 = {
        "title": "Session 4: Review — The Complete Picture",
        "activities": [s4_intro, s4_reading, s4_speak_reading, s4_read_along]
    }

    # ---- Session 5: Final reading + farewell ----
    s5_reading_text = "In the years since Angela Duckworth delivered her TED Talk on grit, the concept has sparked both enthusiasm and debate. Critics have questioned whether grit is truly distinct from conscientiousness, whether it can be reliably measured, and whether emphasizing grit places too much burden on individuals while ignoring systemic barriers. These are important questions, and Duckworth herself has acknowledged many of them. But the core insight of her research remains powerful: sustained effort toward long-term goals is one of the most reliable predictors of achievement across virtually every domain of human endeavor.\n\nConsider what Duckworth's research tells us about the relationship between talent and effort. Our culture is saturated with stories of natural genius — the prodigy who picks up a violin at age three and plays like a master, the entrepreneur who drops out of college and builds a billion-dollar company. These stories are compelling, but they are misleading. They suggest that aptitude is destiny, that the most talented people inevitably rise to the top. Duckworth's data tells a different story. Talent matters, but it is not the strongest predictor of who will succeed. The strongest predictor is grit — the willingness to work with perseverance and passion over extended periods of time.\n\nThis finding has profound implications for education. If grit is more important than talent, then schools should be designed not just to identify and nurture aptitude, but to build the qualities that sustain effort: resilience, diligence, fortitude, and a growth mindset. Duckworth argues that we need to teach children that struggle is not a sign of weakness — it is a sign of learning. When a student encounters a problem they cannot solve, the appropriate response is not to conclude that they lack talent. It is to dig in with tenacity, seek help, and try again. This requires a fundamental shift in mindset, from one that sees ability as fixed to one that sees ability as something that grows through deliberate effort.\n\nThe implications extend beyond education. In the workplace, Duckworth's research suggests that hiring for grit — not just for credentials or aptitude — may produce better long-term outcomes. In athletics, coaches who emphasize consistency and endurance over raw talent may develop more successful teams. In personal life, understanding grit can help us make better decisions about which goals to pursue and how to pursue them. The key insight is that determination — the firm resolve to keep going — is not a personality trait that some people have and others do not. It is a skill that can be developed through practice, supported by the right environment, and strengthened by a sense of purpose.\n\nDuckworth's most hopeful message is about potential. She believes that most people have far more potential than they realize, and that the primary barrier to unlocking that potential is not a lack of talent but a lack of sustained effort. The stamina to keep working when progress is slow, the endurance to push through years of difficulty, the fortitude to maintain belief in yourself when others have doubts — these are the qualities that transform potential into achievement.\n\nThe science of grit is still evolving. Researchers continue to study how grit develops, how it interacts with other personality traits, and how it can be cultivated in different contexts. But the central message of Duckworth's work is clear and enduring: what you achieve in life depends less on how talented you are and more on how hard you are willing to work, how long you are willing to persist, and whether you have the mindset to see every setback as a stepping stone rather than a dead end. Grit is not glamorous. It is not exciting. But it is, according to the data, the single most important quality you can develop if you want to achieve something meaningful with your life."

    s5_intro = {
        "type": "introAudio",
        "title": "Final Reading: Grit Beyond the TED Talk",
        "description": "Introducing the final reading that explores the broader implications and ongoing debate around grit.",
        "data": {
            "text": "Welcome to Session Five — your final session. You have come a long way. You have learned eighteen words that capture the science of grit, read three passages exploring different dimensions of Duckworth's research, and practiced using these words in your own writing. In this session, you will read one more article — this one looking at the broader implications of grit research, including its impact on education, the workplace, and personal development. You will encounter all eighteen vocabulary words in context. After the reading, we will close with a farewell that reviews the most important words and challenges you to carry what you have learned into your daily life. Let us begin."
        }
    }

    s5_reading = {
        "type": "reading",
        "title": "Read: Grit Beyond the TED Talk",
        "description": "In the years since Angela Duckworth delivered her TED Talk on grit, the concept has sparked both...",
        "data": {"text": s5_reading_text}
    }

    s5_speak_reading = {
        "type": "speakReading",
        "title": "Read: Speak the Final Article Aloud",
        "description": "In the years since Angela Duckworth delivered her TED Talk on grit, the concept has sparked both...",
        "data": {"text": s5_reading_text}
    }

    s5_read_along = {
        "type": "readAlong",
        "title": "Listen: Grit Beyond the TED Talk",
        "description": "Listen to the passage and follow along.",
        "data": {"text": s5_reading_text}
    }

    s5_farewell = {
        "type": "introAudio",
        "title": "Farewell: Your Grit Vocabulary",
        "description": "A warm farewell reviewing key vocabulary words and challenging you to apply what you have learned.",
        "data": {
            "text": "You made it. Five sessions, eighteen words, and a deep dive into one of the most important ideas in modern psychology. Before we part ways, let us revisit some of the words that matter most — not just as vocabulary, but as tools for thinking about your own life.\n\nPerseverance means continued effort despite difficulty. Here is a fresh example: The novelist spent eleven years writing and rewriting her first book before a publisher finally said yes. That is perseverance — not talent, not luck, but the stubborn refusal to quit.\n\nResilience is the ability to recover from setbacks. Think of it this way: After his startup failed and he lost everything, he took six months to regroup, then launched a new company that succeeded beyond anything he had imagined. Resilience is not about avoiding failure. It is about what you do after you fail.\n\nDeliberate means done with conscious intention and focus. A deliberate learner does not just go through the motions. She identifies her weakest areas, targets them specifically, and measures her progress. The next time you sit down to study or practice, ask yourself: am I being deliberate, or am I just putting in time?\n\nConsistency is the quality of showing up and performing day after day. The marathon runner who trains every morning, rain or shine, for two years before race day — that is consistency. It is not glamorous, but it is the foundation of every lasting achievement.\n\nMindset is your way of thinking about your own abilities. Do you believe you can grow, or do you believe your abilities are fixed? The answer to that question shapes everything — how you respond to criticism, how you handle failure, and whether you persist when the work gets hard. Choose a growth mindset. It is the single most important decision you can make for your own development.\n\nGrit is the combination of passion and perseverance for long-term goals. It is the master trait — the quality that ties together everything you have learned in this curriculum. Grit is not about being tough in a single moment. It is about being tough across years, across setbacks, across the long, slow grind of meaningful work.\n\nNow here is my challenge to you. Do not let these words stay on a flashcard. Take them into your life. The next time you face a difficult project at work, ask yourself: do I have the fortitude to see this through? The next time you feel like giving up on a goal, ask yourself: is this a moment that requires tenacity, or is it a moment to change direction? The next time someone tells you that you are not talented enough, remember Duckworth's formula: effort counts twice. Talent is where you start. Effort is what determines where you finish.\n\nYou have the vocabulary now. You have the framework. The only question left is: what will you do with it? I believe you have more potential than you realize. The research says so. The data says so. And if you bring the same diligence and determination to your goals that you brought to completing this curriculum, I have no doubt you will surprise yourself.\n\nThank you for learning with me. Now go be gritty."
        }
    }

    session_5 = {
        "title": "Session 5: Final Reading and Farewell",
        "activities": [s5_intro, s5_reading, s5_speak_reading, s5_read_along, s5_farewell]
    }

    # ---- Assemble content ----
    content = {
        "title": "Grit: The Power of Passion and Perseverance",
        "description": "SUCCESS IS NOT ABOUT TALENT. IT NEVER WAS.\n\nYou have watched people with half your ability climb past you — not because they were smarter, not because they had better connections, but because they simply refused to stop. The colleague who got promoted after years of quiet, relentless work. The friend who finished a marathon despite having no athletic background. The student who failed the exam twice and passed on the third try with the highest score in the class.\n\nWhat they had was not a secret. It was grit — the fierce combination of passion and perseverance that Angela Duckworth identified as the single strongest predictor of achievement across every domain she studied. Grit is the engine that turns potential into reality, the force that makes effort count twice in the equation of success.\n\nImagine understanding exactly why some people persist while others quit. Imagine having the vocabulary to describe the inner mechanics of long-term achievement — not in vague, motivational terms, but with the precision of a psychologist who has spent her career studying what actually works.\n\nLearn 18 powerful words drawn from Duckworth's groundbreaking TED Talk. From perseverance and resilience to mindset and deliberate practice, these words will sharpen both your English and your understanding of what it takes to achieve anything worth achieving.",
        "preview": {
            "text": "What if the most important quality for success is not talent, intelligence, or luck — but something far grittier? Angela Duckworth's research reveals that the combination of passion and perseverance predicts achievement better than any other factor. In this curriculum, you will master 18 upper-intermediate English words — perseverance, stamina, tenacity, resilience, diligence, fortitude, passion, aptitude, deliberate, consistency, endurance, determination, grit, predictor, achievement, talent, potential, and mindset — through five immersive sessions built around Duckworth's famous TED Talk. You will read original passages exploring the science of grit, practice speaking and writing with precision, and build a vocabulary that lets you discuss effort, persistence, and human potential with the confidence of someone who truly understands the research. By the end, you will not just know these words — you will think with them."
        },
        "contentTypeTags": ["podcast"],
        "youtubeUrl": "https://www.youtube.com/watch?v=H14bBuluwB8",
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

    # Property 4: Podcast content type tags — youtubeUrl present, contentTypeTags == ["podcast"]
    assert "youtubeUrl" in content, "Missing youtubeUrl for podcast curriculum"
    assert content["youtubeUrl"] == "https://www.youtube.com/watch?v=H14bBuluwB8", "Wrong youtubeUrl"
    assert content["contentTypeTags"] == ["podcast"], f"contentTypeTags should be ['podcast'], got {content['contentTypeTags']}"

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
    print(f"WHERE content->>'title' = 'Grit: The Power of Passion and Perseverance'")
    print(f"  AND uid = '{UID}' ORDER BY created_at;")
    return curriculum_id


if __name__ == "__main__":
    create()
