"""
Create en-en movie curriculum #3: The Pursuit of Happyness
Mirror of vi-en source XjJRTMHxnBXFiA31 — all Vietnamese UI text rewritten in English.

Source movie: The Pursuit of Happyness (2006)
YouTube: https://www.youtube.com/watch?v=bMfOMBGNfMo

18 vocabulary words in 3 groups of 6 (same as vi-en source):
  Group 1: average, dream, practice, probably, protect, spend
  Group 2: broker, chance, internship, opportunity, possibly, struggle
  Group 3: appreciate, happier, lucky, period, shirt, welcome

All user-facing text in English. Reading passages stay as-is (already English).
Vocabulary words stay as-is (already English).

Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 9.1, 9.2, 9.3, 9.4, 9.5
"""

import sys, json, requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"
SOURCE_ID = "XjJRTMHxnBXFiA31"

STRIP_KEYS = {
    "mp3Url", "illustrationSet", "chapterBookmarks", "segments",
    "whiteboardItems", "userReadingId", "lessonUniqueId",
    "curriculumTags", "taskId", "imageId",
}


def strip_keys(obj):
    if isinstance(obj, dict):
        return {k: strip_keys(v) for k, v in obj.items() if k not in STRIP_KEYS}
    if isinstance(obj, list):
        return [strip_keys(item) for item in obj]
    return obj


def validate(content):
    errors = []

    # 18 unique vocab words
    all_words = set()
    for session in content["learningSessions"][:3]:
        for act in session["activities"]:
            if act["activityType"] in ("viewFlashcards", "speakFlashcards",
                                       "vocabLevel1", "vocabLevel2", "vocabLevel3"):
                for w in act["data"].get("vocabList", []):
                    all_words.add(w)
    if len(all_words) != 18:
        errors.append(f"Expected 18 unique vocab words, got {len(all_words)}: {all_words}")

    # 5 sessions
    if len(content["learningSessions"]) != 5:
        errors.append(f"Expected 5 sessions, got {len(content['learningSessions'])}")

    # Activity counts: 12, 12, 12, 4, 5
    expected_counts = [12, 12, 12, 4, 5]
    for i, (session, exp) in enumerate(zip(content["learningSessions"], expected_counts)):
        actual = len(session["activities"])
        if actual != exp:
            errors.append(f"Session {i}: expected {exp} activities, got {actual}")

    # youtubeUrl present
    if not content.get("youtubeUrl"):
        errors.append("Missing youtubeUrl")

    # contentTypeTags
    if "movie" not in content.get("contentTypeTags", []):
        errors.append("Missing 'movie' in contentTypeTags")

    # Every activity has title, description
    for i, session in enumerate(content["learningSessions"]):
        if "title" not in session:
            errors.append(f"Session {i} missing title")
        for j, act in enumerate(session["activities"]):
            for field in ("title", "description"):
                if field not in act:
                    errors.append(f"Session {i}, Activity {j} ({act.get('activityType','?')}) missing '{field}'")

    # No strip keys remain
    def check_no_strip(obj, path="root"):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in STRIP_KEYS:
                    errors.append(f"Strip key '{k}' found at {path}.{k}")
                check_no_strip(v, f"{path}.{k}")
        elif isinstance(obj, list):
            for idx, item in enumerate(obj):
                check_no_strip(item, f"{path}[{idx}]")

    check_no_strip(content)

    if errors:
        print("VALIDATION ERRORS:")
        for e in errors:
            print(f"  - {e}")
        raise ValueError(f"{len(errors)} validation error(s)")
    print("Validation passed.")


def build_content():
    # 1. Fetch vi-en source
    resp = requests.post(f"{API_BASE}/curriculum/getOne",
                         json={"id": SOURCE_ID, "uid": UID})
    resp.raise_for_status()
    source_content = resp.json()["content"]
    if isinstance(source_content, str):
        source_content = json.loads(source_content)
    content = strip_keys(source_content)

    # 2. Transform top-level Vietnamese text → English
    content["title"] = "'The Pursuit of Happyness' — You Got a Dream, You Gotta Protect It"

    content["description"] = (
        "WHAT WOULD YOU DO IF THE WORLD TOLD YOU YOUR DREAM WAS IMPOSSIBLE?\n\n"
        "Picture this: you're sleeping on the floor of a subway bathroom with your five-year-old son "
        "because you have nowhere else to go. Your bank account is empty. Your wife has left. "
        "Every door you knock on either stays shut or slams in your face. And yet — you keep going. "
        "You keep showing up. You keep telling your son that anything is possible, even when "
        "every piece of evidence says otherwise.\n\n"
        "That's the true story of Chris Gardner, played by Will Smith in 'The Pursuit of Happyness.' "
        "It's a film about a man who refuses to let his circumstances define his future — "
        "who takes an unpaid internship at a brokerage firm while homeless, who sells bone-density "
        "scanners during the day and sleeps in shelters at night, who looks his son in the eye "
        "and says: 'Don't ever let somebody tell you you can't do something.'\n\n"
        "The scene on the basketball court is the one that breaks you. Chris watches his son shoot hoops "
        "and almost tells him not to dream too big — then catches himself. 'You got a dream, "
        "you gotta protect it,' he says. That single line has become a rallying cry for anyone "
        "who's ever been told they weren't good enough.\n\n"
        "18 vocabulary words drawn directly from the film's dialogue — words like 'struggle,' "
        "'opportunity,' 'protect,' and 'dream' — combined with a multi-sensory learning method "
        "so you sharpen your English while carrying Chris Gardner's relentless belief "
        "that tomorrow can be better than today."
    )

    content["preview"] = {
        "text": (
            "Remember the scene where Chris Gardner kneels on a basketball court, looks his son "
            "in the eye, and says: 'You got a dream, you gotta protect it'?\n\n"
            "18 English vocabulary words you'll learn: average, dream, practice, probably, protect, "
            "spend, broker, chance, internship, opportunity, possibly, struggle, appreciate, happier, "
            "lucky, period, shirt, welcome.\n\n"
            "Across 5 sessions you'll read Chris's actual dialogue, discover how a homeless father "
            "turned an unpaid internship into a Wall Street career — and how the simplest words "
            "carry the weight of an entire life's perseverance.\n\n"
            "Tap the link below to watch the original scene — after this course, "
            "you'll hear Chris tell his story and understand every single word naturally."
        )
    }

    content["contentTypeTags"] = ["movie"]
    content["is_public"] = False

    # ── Session 0: Group 1 — average, dream, practice, probably, protect, spend ──
    s0 = content["learningSessions"][0]
    s0["title"] = "Session 1: You Got a Dream, You Gotta Protect It"

    # Activity 0: introAudio — scene intro
    s0["activities"][0]["title"] = "Introduction to the Film Scene"
    s0["activities"][0]["description"] = "Setting the stage for the basketball court scene from The Pursuit of Happyness"
    s0["activities"][0]["data"]["text"] = (
        "Welcome to the vocabulary-through-cinema course! Today we begin with one of "
        "the most emotionally powerful scenes in modern Hollywood — the basketball court scene "
        "from 'The Pursuit of Happyness.' The 2006 film stars Will Smith as Chris Gardner, "
        "a real man who went from homelessness to becoming a millionaire stockbroker — "
        "and the film never lets you forget the cost of that journey.\n\n"
        "In this scene, Chris and his young son Christopher are shooting hoops on a public court. "
        "Chris, exhausted from selling bone-density scanners all day and sleeping in shelters at night, "
        "watches his son dream about playing in the NBA. For a moment, Chris almost tells him "
        "to be realistic — to not aim too high. But then he catches himself. He kneels down, "
        "looks his son in the eye, and delivers one of the most quoted lines in cinema: "
        "'Don't ever let somebody tell you you can't do something. Not even me. "
        "You got a dream, you gotta protect it.'\n\n"
        "In this first session, you'll learn 6 vocabulary words that appear in Chris Gardner's "
        "dialogue: average, dream, practice, probably, protect, and spend. Each word is woven "
        "into the fabric of the scene, and by the end of this session you'll hear them the way "
        "Chris means them — not just as dictionary entries, but as pieces of a father's desperate "
        "promise to his son that the future doesn't have to look like the present."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s0["activities"][1]["title"] = "Vocabulary Introduction: Session 1"
    s0["activities"][1]["description"] = "Learn 6 words: average, dream, practice, probably, protect, spend"
    s0["activities"][1]["data"]["text"] = (
        "Let's dive into the first 6 vocabulary words from the basketball court scene "
        "in 'The Pursuit of Happyness.' Each word comes straight from Chris Gardner's dialogue, "
        "and understanding how he uses them will change the way you hear everyday English.\n\n"

        "The first word is 'average.' It's an adjective meaning 'typical, ordinary, not outstanding.' "
        "Chris uses this word when talking about what most people settle for — an average life, "
        "an average job, average expectations. But the whole point of the film is that Chris refuses "
        "to be average. He's a man who sleeps in a subway bathroom and still shows up in a suit "
        "the next morning. 'Average' can also be a noun (the mathematical mean) or a verb "
        "('She averages eight hours of sleep'). Common phrases: 'above average,' 'below average,' "
        "'on average.' Example: The average person checks their phone over 90 times a day, "
        "but she decided to break that habit.\n\n"

        "The second word is 'dream.' It's both a noun and a verb — and it's the beating heart "
        "of this entire film. As a noun: 'a dream' is something you hope for, aspire to, "
        "or see while sleeping. As a verb: 'to dream' means to have ambitions or to experience "
        "images during sleep. Chris tells his son: 'You got a dream, you gotta protect it.' "
        "In that sentence, 'dream' isn't about sleeping — it's about the future you believe in "
        "even when no one else does. Common collocations: 'dream big,' 'dream come true,' "
        "'follow your dream,' 'pipe dream' (an unrealistic hope). "
        "Example: She had a dream of opening her own bakery, and ten years later she did it.\n\n"

        "The third word is 'practice.' It can be a noun or a verb. As a verb, it means "
        "'to perform an activity repeatedly to improve.' As a noun, it means 'the act of practicing' "
        "or 'a professional business' (a medical practice, a law practice). On the basketball court, "
        "Chris's son practices his shots — and Chris uses that moment to teach a life lesson. "
        "Practice is what separates dreamers from achievers. 'Practice makes perfect' is the classic "
        "saying, though many teachers now prefer 'practice makes progress.' "
        "Example: He practiced his presentation twelve times before stepping on stage.\n\n"

        "The fourth word is 'probably.' It's an adverb meaning 'almost certainly, very likely.' "
        "Chris uses it in a pivotal moment — he almost tells his son that he'll 'probably' "
        "never be a professional basketball player. It's the word of lowered expectations, "
        "the word that kills dreams before they start. But Chris catches himself and takes it back. "
        "'Probably' sits between 'possibly' (less certain) and 'definitely' (fully certain). "
        "It's one of the most common adverbs in spoken English. "
        "Example: She'll probably arrive around seven, but don't hold me to that.\n\n"

        "The fifth word is 'protect.' It's a verb meaning 'to keep safe from harm or danger.' "
        "This is the word that defines Chris Gardner as a father. 'You got a dream, you gotta "
        "protect it.' He's not talking about physical protection — he's talking about shielding "
        "your ambitions from people who tell you they're impossible. 'Protect' takes a direct object: "
        "'protect your family,' 'protect the environment.' The noun form is 'protection.' "
        "Example: A good mentor protects your confidence while pushing you to grow.\n\n"

        "The sixth word is 'spend.' It's a verb meaning 'to use money to pay for something' "
        "or 'to pass time in a particular way.' Chris spends every waking hour trying to build "
        "a better life — spending time studying for his broker's exam, spending his last dollars "
        "on bus fare, spending nights in shelters. 'Spend' is irregular: spend, spent, spent. "
        "Common patterns: 'spend money on,' 'spend time doing,' 'spend the night.' "
        "Example: They spent the entire weekend painting the apartment and eating takeout.\n\n"

        "So there you have it — your first 6 words: average, dream, practice, probably, protect, "
        "and spend. Each one is a thread in the story of a father who refused to give up. "
        "Let's practice them now!"
    )

    # Activities 2-6: flashcards/vocab — update titles and descriptions
    s0["activities"][2]["title"] = "Flashcards: Dreams and the Basketball Court"
    s0["activities"][2]["description"] = "Learn 6 words: average, dream, practice, probably, protect, spend"

    s0["activities"][3]["title"] = "Flashcards: Speak Session 1 Vocabulary"
    s0["activities"][3]["description"] = "Practice saying 6 words: average, dream, practice, probably, protect, spend"

    s0["activities"][4]["title"] = "Flashcards: Recognize Session 1 Vocabulary"
    s0["activities"][4]["description"] = "Recognize 6 words: average, dream, practice, probably, protect, spend"

    s0["activities"][5]["title"] = "Flashcards: Recall Session 1 Vocabulary"
    s0["activities"][5]["description"] = "Recall 6 words: average, dream, practice, probably, protect, spend"

    s0["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 1"
    s0["activities"][6]["description"] = "Master 6 words: average, dream, practice, probably, protect, spend"

    # Activity 7: introAudio — grammar/usage
    s0["activities"][7]["title"] = "Grammar and Usage: Session 1"
    s0["activities"][7]["description"] = "How to use Session 1 vocabulary naturally in sentences"
    s0["activities"][7]["data"]["text"] = (
        "Great work! You've met your first 6 words. Now let's look at how they work "
        "in real English sentences, using Chris Gardner's dialogue as our guide.\n\n"
        "'Average' functions as an adjective ('an average day'), a noun ('the national average'), "
        "and a verb ('She averages 10,000 steps a day'). As an adjective, it often carries "
        "a slightly negative connotation — calling someone 'average' implies they're unremarkable. "
        "Chris Gardner's entire story is a rebellion against being average.\n\n"
        "'Dream' pairs with many verbs: 'have a dream,' 'chase a dream,' 'achieve a dream,' "
        "'give up on a dream.' As a verb, it takes 'of' or 'about': 'I dream of traveling the world,' "
        "'She dreamed about her childhood.' 'Dreamy' (adjective) means vague or romantically attractive. "
        "'A dream' can also modify nouns: 'a dream job,' 'a dream house,' 'a dream team.'\n\n"
        "'Practice' in American English is both the noun and verb spelling. In British English, "
        "the noun is 'practise' and the verb is 'practice.' Common structures: 'practice doing something' "
        "(not 'practice to do'). 'In practice' means 'in reality': 'In theory it's simple; "
        "in practice it's much harder.'\n\n"
        "'Probably' is one of the most frequently used adverbs in English. It usually comes "
        "before the main verb: 'She will probably come,' 'He's probably right.' "
        "In casual speech, it's often shortened to 'prolly.' The adjective form is 'probable,' "
        "and the noun is 'probability.'\n\n"
        "'Protect' takes a direct object: 'protect your dream,' 'protect the children.' "
        "'Protect from' and 'protect against' are both correct: 'Sunscreen protects against UV rays.' "
        "Related words: 'protection' (noun), 'protective' (adjective), 'protector' (noun).\n\n"
        "'Spend' is irregular: spend, spent, spent. It collocates with both money and time: "
        "'spend money on books,' 'spend time with family.' 'Spending' as a noun refers to expenditure: "
        "'government spending,' 'consumer spending.' Never say 'spend time to do' — "
        "it's 'spend time doing': 'I spent an hour reading.'"
    )

    # Activity 8: reading — keep text as-is (already English), update title/description
    s0["activities"][8]["title"] = "Read: The Pursuit of Happyness Excerpt (Part 1)"
    s0["activities"][8]["description"] = "Read the basketball court dialogue from The Pursuit of Happyness"

    # Activity 9: speakReading
    s0["activities"][9]["title"] = "Speak: Practice the Dialogue (Part 1)"
    s0["activities"][9]["description"] = "Practice speaking the basketball court dialogue aloud"

    # Activity 10: readAlong
    s0["activities"][10]["title"] = "Listen: The Pursuit of Happyness Excerpt (Part 1)"
    s0["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s0["activities"][11]["title"] = "Write: Dreams and Determination"
    s0["activities"][11]["description"] = "Write sentences using Session 1 vocabulary"
    ws_items_0 = s0["activities"][11]["data"]["items"]
    ws_items_0[0]["prompt"] = (
        "Use the word 'average' to write about refusing to settle for the ordinary — "
        "just as Chris Gardner refuses to accept an average life for himself and his son. "
        "Example: She was tired of average results, so she started waking up at five "
        "and putting in the extra hours no one else was willing to."
    )
    ws_items_0[1]["prompt"] = (
        "Use the word 'dream' to write about an ambition or aspiration — "
        "like Chris telling his son to never let anyone take his dream away. "
        "Example: His dream of becoming a pilot started the day his grandfather "
        "took him to an airshow when he was seven years old."
    )
    ws_items_0[2]["prompt"] = (
        "Use the word 'practice' to write about repetition and improvement — "
        "the way Chris's son practices basketball on the court while his father watches. "
        "Example: She practiced the piano piece so many times that her fingers "
        "knew the notes before her mind did."
    )
    ws_items_0[3]["prompt"] = (
        "Use the word 'probably' to express likelihood or uncertainty — "
        "remembering how Chris almost used it to crush his son's dream before catching himself. "
        "Example: You'll probably never regret being kind to someone, "
        "even if they don't return the favor."
    )
    ws_items_0[4]["prompt"] = (
        "Use the word 'protect' to write about safeguarding something precious — "
        "like Chris's famous line: 'You got a dream, you gotta protect it.' "
        "Example: A true friend protects your reputation even when you're not in the room."
    )
    ws_items_0[5]["prompt"] = (
        "Use the word 'spend' to write about how you use time or money — "
        "the way Chris spends every waking hour fighting for a better future. "
        "Example: He spent three years building the business from nothing, "
        "and now it supports his entire family."
    )

    # ── Session 1: Group 2 — broker, chance, internship, opportunity, possibly, struggle ──
    s1 = content["learningSessions"][1]
    s1["title"] = "Session 2: The Struggle and the Chance"

    # Activity 0: introAudio — session intro
    s1["activities"][0]["title"] = "Introduction to Session 2"
    s1["activities"][0]["description"] = "Recap Session 1 and introduce the theme of struggle and opportunity"
    s1["activities"][0]["data"]["text"] = (
        "Welcome back to Session 2! In our first session, you learned 6 words from the "
        "basketball court scene: average, dream, practice, probably, protect, and spend. "
        "You discovered how Chris Gardner uses the simplest language to deliver the most powerful "
        "lesson a father can give — that your dream belongs to you, and no one has the right "
        "to tell you it's impossible.\n\n"
        "Now we're going deeper into Chris's story. This part of the film follows him into "
        "the world of finance — a world he has no business entering. He has no college degree, "
        "no connections, no money. What he has is a Rubik's Cube, a relentless work ethic, "
        "and the ability to solve problems faster than anyone in the room. He talks his way "
        "into an unpaid internship at Dean Witter Reynolds, a prestigious brokerage firm, "
        "competing against twenty other candidates — all of whom have advantages he doesn't.\n\n"
        "Today you'll learn 6 new words: broker, chance, internship, opportunity, possibly, "
        "and struggle. These words carry the weight of Chris's fight to survive — and by the end "
        "of this session, you'll hear them echoing through every scene in the film."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s1["activities"][1]["title"] = "Vocabulary Introduction: Session 2"
    s1["activities"][1]["description"] = "Learn 6 words: broker, chance, internship, opportunity, possibly, struggle"
    s1["activities"][1]["data"]["text"] = (
        "Let's learn 6 new vocabulary words from the next part of Chris Gardner's story — "
        "the scenes where he fights his way into the world of Wall Street.\n\n"

        "The first word is 'broker.' It's a noun meaning 'a person who buys and sells goods "
        "or assets for others.' In the film, Chris Gardner's entire goal is to become a stockbroker — "
        "someone who trades stocks and securities on behalf of clients. The word comes from "
        "the Old French 'broceur,' meaning 'small trader.' Today, 'broker' appears in many contexts: "
        "a real estate broker, an insurance broker, a power broker (someone who influences decisions "
        "behind the scenes). As a verb, 'to broker' means to arrange or negotiate: "
        "'She brokered a deal between the two companies.' "
        "Example: After six months of grueling training, he finally earned his license as a stockbroker.\n\n"

        "The second word is 'chance.' It's a noun meaning 'a possibility of something happening' "
        "or 'an opportunity.' Chris Gardner takes a chance on himself — he bets everything on "
        "the slim possibility that he can outperform twenty other internship candidates. "
        "'Chance' can mean probability ('There's a good chance of rain'), opportunity "
        "('Give me a chance to explain'), or luck ('It happened by chance'). "
        "Common phrases: 'take a chance,' 'by any chance,' 'fat chance' (very unlikely), "
        "'stand a chance' (have a possibility of success). "
        "Example: She took a chance on a startup nobody believed in, and it changed her life.\n\n"

        "The third word is 'internship.' It's a noun meaning 'a period of work experience "
        "offered by an organization, often unpaid, to gain practical skills.' Chris's internship "
        "at Dean Witter is the central plot device of the film — it's unpaid, brutally competitive, "
        "and only one of twenty interns will be offered a full-time position. The word combines "
        "'intern' (a trainee) with the suffix '-ship' (a state or condition). "
        "'Do an internship,' 'apply for an internship,' 'summer internship.' "
        "Example: Her internship at the hospital convinced her that medicine was her calling.\n\n"

        "The fourth word is 'opportunity.' It's a noun meaning 'a set of circumstances that makes "
        "something possible.' This is the word that drives Chris Gardner forward. Every setback "
        "is just a door that hasn't opened yet. Every rejection is one step closer to the one 'yes' "
        "that matters. 'Opportunity' is often paired with verbs of action: 'seize an opportunity,' "
        "'create an opportunity,' 'miss an opportunity.' The adjective form is 'opportune' "
        "(well-timed). 'Equal opportunity' means fair access for everyone. "
        "Example: The conference turned out to be an unexpected opportunity to meet her future business partner.\n\n"

        "The fifth word is 'possibly.' It's an adverb meaning 'perhaps, maybe.' "
        "It expresses a lower degree of certainty than 'probably.' Chris uses it when weighing "
        "his options — could he possibly make it as a broker with no degree and no money? "
        "The answer, against all odds, is yes. 'Possibly' often appears in polite requests: "
        "'Could you possibly help me?' It can also express disbelief: 'How could you possibly "
        "think that was a good idea?' The adjective form is 'possible,' the noun is 'possibility.' "
        "Example: Could you possibly send me the report by Friday? I'd really appreciate it.\n\n"

        "The sixth word is 'struggle.' It's both a noun and a verb meaning 'to fight hard "
        "to achieve something despite difficulty.' If there's one word that defines Chris Gardner's "
        "life, it's 'struggle.' He struggles to pay rent, struggles to feed his son, struggles "
        "to keep his dignity in a world that keeps trying to strip it away. As a verb: "
        "'She struggled with the math problem for an hour.' As a noun: 'The struggle for equality.' "
        "Common phrases: 'struggle to survive,' 'daily struggle,' 'power struggle.' "
        "Example: The first year of running a business is always a struggle, but the second year "
        "is where you find out if you're built for it.\n\n"

        "Your 6 new words: broker, chance, internship, opportunity, possibly, struggle. "
        "Combined with Session 1, you now have 12 words from Chris Gardner's world. "
        "Let's put them to work!"
    )

    # Activities 2-6: flashcards/vocab
    s1["activities"][2]["title"] = "Flashcards: The Struggle and the Chance"
    s1["activities"][2]["description"] = "Learn 6 words: broker, chance, internship, opportunity, possibly, struggle"

    s1["activities"][3]["title"] = "Flashcards: Speak Session 2 Vocabulary"
    s1["activities"][3]["description"] = "Practice saying 6 words: broker, chance, internship, opportunity, possibly, struggle"

    s1["activities"][4]["title"] = "Flashcards: Recognize Session 2 Vocabulary"
    s1["activities"][4]["description"] = "Recognize 6 words: broker, chance, internship, opportunity, possibly, struggle"

    s1["activities"][5]["title"] = "Flashcards: Recall Session 2 Vocabulary"
    s1["activities"][5]["description"] = "Recall 6 words: broker, chance, internship, opportunity, possibly, struggle"

    s1["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 2"
    s1["activities"][6]["description"] = "Master 6 words: broker, chance, internship, opportunity, possibly, struggle"

    # Activity 7: introAudio — grammar/usage
    s1["activities"][7]["title"] = "Grammar and Usage: Session 2"
    s1["activities"][7]["description"] = "How to use Session 2 vocabulary naturally in sentences"
    s1["activities"][7]["data"]["text"] = (
        "Excellent! Let's explore how these 6 words behave in real English.\n\n"
        "'Broker' as a noun takes articles: 'a broker,' 'the broker.' As a verb, it's transitive: "
        "'broker a deal,' 'broker a peace agreement.' The compound 'stockbroker' is one word. "
        "'Brokerage' is the noun for the business or the fee: 'a brokerage firm,' 'brokerage fees.' "
        "In the film, Chris doesn't just want to be any broker — he wants to be the best.\n\n"
        "'Chance' has subtle differences depending on the article. 'A chance' means an opportunity: "
        "'Give me a chance.' 'The chance' refers to a specific opportunity: 'This is the chance "
        "I've been waiting for.' 'By chance' means accidentally: 'We met by chance at the airport.' "
        "'Chances are' means 'it's likely': 'Chances are she already knows.'\n\n"
        "'Internship' is countable: 'an internship,' 'two internships.' It collocates with "
        "'unpaid,' 'paid,' 'summer,' 'competitive.' The person doing it is an 'intern.' "
        "'To intern' is also a verb: 'She interned at a law firm last summer.' "
        "In Chris's case, the internship is unpaid — which makes his situation even more desperate.\n\n"
        "'Opportunity' is formal and positive. 'Chance' is its casual synonym. "
        "'Opportunity knocks' is a common saying. 'Window of opportunity' means a limited time "
        "to act. 'Equal opportunity employer' is a legal/HR term. The plural 'opportunities' "
        "is very common: 'career opportunities,' 'growth opportunities.'\n\n"
        "'Possibly' is weaker than 'probably' but stronger than 'unlikely.' "
        "Scale of certainty: definitely > probably > possibly > unlikely > impossible. "
        "In polite requests, 'possibly' softens the ask: 'Could you possibly help me move?' "
        "'Not possibly' expresses impossibility: 'I can't possibly finish by tomorrow.'\n\n"
        "'Struggle' as a verb takes 'to' + infinitive: 'struggle to understand,' "
        "'struggle to survive.' As a noun, it takes 'for' or 'against': "
        "'the struggle for justice,' 'the struggle against poverty.' "
        "'Struggling' as an adjective means having difficulty: 'a struggling artist,' "
        "'a struggling business.' Chris Gardner is the ultimate struggling hero."
    )

    # Activity 8-10: reading/speak/listen — keep text, update titles
    s1["activities"][8]["title"] = "Read: The Pursuit of Happyness Excerpt (Part 2)"
    s1["activities"][8]["description"] = "Read the dialogue about Chris's internship and struggle"

    s1["activities"][9]["title"] = "Speak: Practice the Dialogue (Part 2)"
    s1["activities"][9]["description"] = "Practice speaking the internship dialogue aloud"

    s1["activities"][10]["title"] = "Listen: The Pursuit of Happyness Excerpt (Part 2)"
    s1["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s1["activities"][11]["title"] = "Write: Struggle and Opportunity"
    s1["activities"][11]["description"] = "Write sentences using Session 2 vocabulary"
    ws_items_1 = s1["activities"][11]["data"]["items"]
    ws_items_1[0]["prompt"] = (
        "Use the word 'broker' to write about someone who facilitates deals or trades — "
        "like Chris Gardner's dream of becoming a stockbroker against all odds. "
        "Example: The real estate broker found them a house they never thought they could afford."
    )
    ws_items_1[1]["prompt"] = (
        "Use the word 'chance' to write about taking a risk or seizing a possibility — "
        "the way Chris takes a chance on an unpaid internship with everything on the line. "
        "Example: He took a chance on a job interview in a city where he knew no one, "
        "and it turned out to be the best decision of his life."
    )
    ws_items_1[2]["prompt"] = (
        "Use the word 'internship' to write about gaining experience through work — "
        "like Chris competing against twenty candidates for a single position. "
        "Example: The internship didn't pay a cent, but the skills she gained "
        "were worth more than any salary."
    )
    ws_items_1[3]["prompt"] = (
        "Use the word 'opportunity' to write about a favorable circumstance — "
        "the way Chris sees every closed door as a chance to find an open window. "
        "Example: The layoff felt like a disaster at first, but it turned into "
        "the opportunity she needed to start her own company."
    )
    ws_items_1[4]["prompt"] = (
        "Use the word 'possibly' to express uncertainty or make a polite request — "
        "like Chris weighing whether he could possibly survive an unpaid internship while homeless. "
        "Example: Could you possibly lend me your notes from yesterday's lecture? "
        "I missed the class due to a family emergency."
    )
    ws_items_1[5]["prompt"] = (
        "Use the word 'struggle' to describe fighting through difficulty — "
        "the way Chris struggles every single day to keep his son safe and his dream alive. "
        "Example: The struggle to learn a new language is real, but every small victory "
        "makes the next one a little easier."
    )

    # ── Session 2: Group 3 — appreciate, happier, lucky, period, shirt, welcome ──
    s2 = content["learningSessions"][2]
    s2["title"] = "Session 3: The Moment Everything Changes"

    # Activity 0: introAudio — session intro
    s2["activities"][0]["title"] = "Introduction to Session 3"
    s2["activities"][0]["description"] = "Recap Sessions 1-2 and introduce the themes of gratitude and triumph"
    s2["activities"][0]["data"]["text"] = (
        "Welcome to Session 3 — the final learning session before your review! "
        "So far you've learned 12 words from Chris Gardner's world. In Session 1, you met "
        "average, dream, practice, probably, protect, and spend — the words of the basketball court, "
        "where a father kneels down and tells his son to never let anyone steal his dream. "
        "In Session 2, you learned broker, chance, internship, opportunity, possibly, and struggle — "
        "the words of Wall Street, where a homeless man in a borrowed suit outworks everyone "
        "in the room.\n\n"
        "Now we reach the climax of the film. Chris has survived six months of unpaid work, "
        "sleeping in shelters, running across the city to pick up his son from daycare before "
        "it closes. He's sold every bone-density scanner. He's studied every night. And now "
        "the partners at Dean Witter call him into a room to tell him whether he got the job.\n\n"
        "Your final 6 words: appreciate, happier, lucky, period, shirt, and welcome. "
        "By the end of this session, you'll have all 18 vocabulary words — and you'll understand "
        "why Chris Gardner walks out of that office building, tears streaming down his face, "
        "and starts clapping in the middle of a crowded street."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s2["activities"][1]["title"] = "Vocabulary Introduction: Session 3"
    s2["activities"][1]["description"] = "Learn 6 words: appreciate, happier, lucky, period, shirt, welcome"
    s2["activities"][1]["data"]["text"] = (
        "Here are your final 6 vocabulary words, drawn from the most triumphant scenes "
        "in The Pursuit of Happyness.\n\n"

        "The first word is 'appreciate.' It's a verb with two main meanings: "
        "'to recognize the value of something' and 'to be grateful for something.' "
        "When Chris finally gets the job, the depth of his appreciation is beyond words — "
        "he's not just grateful for a paycheck, he's grateful for the proof that his struggle "
        "meant something. 'Appreciate' is followed by a noun or gerund: 'I appreciate your help,' "
        "'I appreciate you coming.' Never say 'I appreciate you to come.' "
        "The noun form is 'appreciation.' "
        "Example: You don't truly appreciate what you have until you've experienced losing everything.\n\n"

        "The second word is 'happier.' It's the comparative form of 'happy' — meaning 'more happy.' "
        "The film's title itself is a clue: 'The Pursuit of Happyness' (deliberately misspelled "
        "from a mural Chris sees outside his son's daycare). Chris isn't chasing happiness — "
        "he's chasing something happier than what he has now. One-syllable adjectives add '-er': "
        "'tall → taller.' Two-syllable adjectives ending in 'y' change to '-ier': 'happy → happier,' "
        "'easy → easier.' Longer adjectives use 'more': 'more beautiful,' not 'beautifuler.' "
        "Example: She realized she was happier with less — fewer possessions, fewer obligations, "
        "and more time for the people she loved.\n\n"

        "The third word is 'lucky.' It's an adjective meaning 'having good fortune.' "
        "Chris Gardner doesn't believe in luck — he believes in preparation meeting opportunity. "
        "But when the partners offer him the job, even he has to admit that some part of it "
        "feels like luck. 'Lucky' collocates with many nouns: 'lucky break,' 'lucky charm,' "
        "'lucky guess,' 'lucky number.' 'Get lucky' means to have unexpected good fortune. "
        "'Luckily' is the adverb form. "
        "Example: She felt lucky to have a mentor who believed in her before she believed in herself.\n\n"

        "The fourth word is 'period.' It's a noun with several meanings: 'a length of time' "
        "('a period of growth'), 'a punctuation mark' (the dot at the end of a sentence), "
        "or 'a class session in school' ('first period'). In the film, Chris refers to a period "
        "of his life — the darkest chapter, the one where everything fell apart before it came "
        "together. In American English, 'period' at the end of a statement means 'and that's final': "
        "'I'm not going. Period.' "
        "Example: That six-month period was the hardest of his life, but it shaped everything that came after.\n\n"

        "The fifth word is 'shirt.' It's a noun — a garment for the upper body. "
        "In the film, Chris's shirt matters more than you'd think. He shows up to his internship "
        "interview covered in paint because he spent the night in jail after unpaid parking tickets. "
        "He's wearing the wrong shirt for a Wall Street interview — and he still gets the job "
        "because his mind is sharper than his clothes. 'Shirt' appears in many idioms: "
        "'keep your shirt on' (stay calm), 'lose your shirt' (lose all your money), "
        "'the shirt off your back' (extreme generosity). "
        "Example: He ironed his only good shirt the night before the interview, "
        "knowing first impressions could make or break his chance.\n\n"

        "The sixth and final word is 'welcome.' It can be an adjective, verb, noun, or interjection. "
        "As an adjective: 'You're welcome here.' As a verb: 'We welcome new members.' "
        "As an interjection: 'Welcome!' When Chris is finally welcomed into the firm as a full "
        "employee — not an intern, not a candidate, but a broker — it's the culmination of "
        "everything he's fought for. 'You're welcome' is the standard response to 'thank you.' "
        "'Welcome to' introduces someone to a new place or situation: 'Welcome to the team.' "
        "Example: The warm welcome she received on her first day made all the anxiety disappear.\n\n"

        "And there you have it — all 18 words: average, dream, practice, probably, protect, spend, "
        "broker, chance, internship, opportunity, possibly, struggle, appreciate, happier, lucky, "
        "period, shirt, and welcome. You now have the complete vocabulary of Chris Gardner's story. "
        "Let's practice these final 6!"
    )

    # Activities 2-6: flashcards/vocab
    s2["activities"][2]["title"] = "Flashcards: The Moment Everything Changes"
    s2["activities"][2]["description"] = "Learn 6 words: appreciate, happier, lucky, period, shirt, welcome"

    s2["activities"][3]["title"] = "Flashcards: Speak Session 3 Vocabulary"
    s2["activities"][3]["description"] = "Practice saying 6 words: appreciate, happier, lucky, period, shirt, welcome"

    s2["activities"][4]["title"] = "Flashcards: Recognize Session 3 Vocabulary"
    s2["activities"][4]["description"] = "Recognize 6 words: appreciate, happier, lucky, period, shirt, welcome"

    s2["activities"][5]["title"] = "Flashcards: Recall Session 3 Vocabulary"
    s2["activities"][5]["description"] = "Recall 6 words: appreciate, happier, lucky, period, shirt, welcome"

    s2["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 3"
    s2["activities"][6]["description"] = "Master 6 words: appreciate, happier, lucky, period, shirt, welcome"

    # Activity 7: introAudio — grammar/usage
    s2["activities"][7]["title"] = "Grammar and Usage: Session 3"
    s2["activities"][7]["description"] = "How to use Session 3 vocabulary naturally in sentences"
    s2["activities"][7]["data"]["text"] = (
        "Let's look at how these final 6 words work in English grammar.\n\n"
        "'Appreciate' is transitive — it always takes an object: 'I appreciate your patience,' "
        "'We appreciate the effort.' In formal contexts: 'I would appreciate it if you could send me "
        "the report.' Never say 'I appreciate for your help' — drop the 'for.' "
        "The adjective 'appreciative' means 'feeling or showing gratitude': "
        "'an appreciative audience.'\n\n"
        "'Happier' follows the standard comparative pattern for two-syllable adjectives ending in 'y': "
        "drop the 'y,' add '-ier.' Happy → happier. Easy → easier. Busy → busier. "
        "The superlative is 'happiest.' 'Happily' is the adverb: 'They lived happily ever after.' "
        "'Happiness' is the noun — and it's the word in the film's title, deliberately misspelled "
        "as 'Happyness' to reflect a mural Chris sees every day.\n\n"
        "'Lucky' takes 'to' + infinitive: 'I'm lucky to have you.' It also takes 'that': "
        "'We're lucky that the weather held.' 'Lucky' vs. 'fortunate': 'lucky' is casual, "
        "'fortunate' is formal. 'Luck' (noun) is uncountable: 'good luck,' 'bad luck,' "
        "'a stroke of luck.' 'Luck out' (phrasal verb) means to be unexpectedly fortunate.\n\n"
        "'Period' in American English is the punctuation mark (.) — British English calls it "
        "a 'full stop.' As a time word: 'a period of time,' 'the colonial period,' "
        "'a grace period.' In school: 'first period,' 'lunch period.' "
        "As an emphatic closer: 'I said no. Period.' — meaning the discussion is over.\n\n"
        "'Shirt' is countable: 'a shirt,' 'three shirts.' Types: 'dress shirt,' 't-shirt,' "
        "'polo shirt,' 'button-down shirt.' 'Shirt' appears in idioms: "
        "'stuffed shirt' (a pompous person), 'keep your shirt on' (be patient). "
        "In the film, Chris's paint-stained shirt becomes a symbol of his refusal to let "
        "appearances define his worth.\n\n"
        "'Welcome' as an adjective follows 'be': 'You're welcome,' 'Changes are welcome.' "
        "As a verb: 'We welcome feedback,' 'She welcomed the guests.' "
        "'Welcome' + 'to' introduces: 'Welcome to New York,' 'Welcome to the team.' "
        "'Welcoming' (adjective) means warm and friendly: 'a welcoming atmosphere.'"
    )

    # Activity 8-10: reading/speak/listen
    s2["activities"][8]["title"] = "Read: The Pursuit of Happyness Excerpt (Part 3)"
    s2["activities"][8]["description"] = "Read the dialogue about gratitude and triumph"

    s2["activities"][9]["title"] = "Speak: Practice the Dialogue (Part 3)"
    s2["activities"][9]["description"] = "Practice speaking the final dialogue excerpt aloud"

    s2["activities"][10]["title"] = "Listen: The Pursuit of Happyness Excerpt (Part 3)"
    s2["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s2["activities"][11]["title"] = "Write: Gratitude and Triumph"
    s2["activities"][11]["description"] = "Write sentences using Session 3 vocabulary"
    ws_items_2 = s2["activities"][11]["data"]["items"]
    ws_items_2[0]["prompt"] = (
        "Use the word 'appreciate' to express gratitude or recognition of value — "
        "the way Chris appreciates every small victory after months of sleeping in shelters. "
        "Example: I didn't appreciate how much my parents sacrificed until I became a parent myself."
    )
    ws_items_2[1]["prompt"] = (
        "Use the word 'happier' to compare levels of happiness — "
        "like Chris pursuing a life that's happier than the one he was given. "
        "Example: She discovered she was happier teaching children than working in corporate finance."
    )
    ws_items_2[2]["prompt"] = (
        "Use the word 'lucky' to write about good fortune or gratitude — "
        "the way Chris feels when the partners finally offer him the job. "
        "Example: I consider myself lucky to have grown up in a home filled with books and conversation."
    )
    ws_items_2[3]["prompt"] = (
        "Use the word 'period' to refer to a stretch of time or to end a statement emphatically — "
        "like Chris looking back on the darkest period of his life. "
        "Example: That two-year period of living abroad changed the way I see the world. Period."
    )
    ws_items_2[4]["prompt"] = (
        "Use the word 'shirt' in a sentence about appearance, preparation, or an idiom — "
        "like Chris showing up to his interview in a paint-stained shirt and still getting the job. "
        "Example: He would give you the shirt off his back if he thought you needed it more than he did."
    )
    ws_items_2[5]["prompt"] = (
        "Use the word 'welcome' as a greeting, an adjective, or a verb — "
        "like the moment Chris is finally welcomed into the firm as a full broker. "
        "Example: After months of feeling like an outsider, the team's warm welcome "
        "made her realize she finally belonged."
    )

    # ── Session 3: Review (4 activities) ──
    s3 = content["learningSessions"][3]
    s3["title"] = "Review"

    s3["activities"][0]["title"] = "Congratulations and Review"
    s3["activities"][0]["description"] = "Celebrate your progress and prepare for the full review"
    s3["activities"][0]["data"]["text"] = (
        "Congratulations! You've learned all 18 vocabulary words from The Pursuit of Happyness. "
        "Let's take a moment to look back at what you've accomplished.\n\n"
        "In Session 1, you learned average, dream, practice, probably, protect, and spend — "
        "the words of the basketball court scene, where Chris Gardner kneels beside his son "
        "and delivers the line that defines the entire film: 'You got a dream, you gotta protect it.'\n\n"
        "In Session 2, you learned broker, chance, internship, opportunity, possibly, and struggle — "
        "the words of Chris's impossible fight to break into Wall Street with no degree, no money, "
        "and no safety net — just a Rubik's Cube and an unbreakable will.\n\n"
        "In Session 3, you learned appreciate, happier, lucky, period, shirt, and welcome — "
        "the words of the film's climax, where a man who slept in subway bathrooms walks out "
        "of a boardroom as a stockbroker, tears streaming down his face, clapping alone "
        "in a crowded street because no one else knows what he's been through.\n\n"
        "Now it's time to review all 18 words together. This review session will test your "
        "recognition and recall across all three groups. After this, you'll be ready to read "
        "the complete dialogue in the final session. Let's go!"
    )

    s3["activities"][1]["title"] = "Flashcards: Review All 18 Words"
    s3["activities"][1]["description"] = "Review all 18 vocabulary words from The Pursuit of Happyness"

    s3["activities"][2]["title"] = "Flashcards: Recognize All Vocabulary"
    s3["activities"][2]["description"] = "Test your recognition of all 18 words"

    s3["activities"][3]["title"] = "Flashcards: Recall All Vocabulary"
    s3["activities"][3]["description"] = "Test your recall of all 18 words"

    # ── Session 4: Full reading + farewell (5 activities) ──
    s4 = content["learningSessions"][4]
    s4["title"] = "Full Dialogue Reading"

    s4["activities"][0]["title"] = "Introduction to the Complete Reading"
    s4["activities"][0]["description"] = "Prepare for reading the full Pursuit of Happyness dialogue"
    s4["activities"][0]["data"]["text"] = (
        "Welcome to the final session! This is the moment everything comes together. "
        "Over the past three sessions, you've built a vocabulary of 18 words drawn directly "
        "from The Pursuit of Happyness. You've learned their meanings, practiced their pronunciation, "
        "explored their grammar, and used them in your own writing.\n\n"
        "Now you're going to read the complete dialogue — all three excerpts combined into one "
        "continuous passage. As you read, you'll encounter every single one of your 18 words "
        "in context. This time, they won't be new — they'll be familiar friends.\n\n"
        "Here are all 18 words you'll see: average, dream, practice, probably, protect, spend, "
        "broker, chance, internship, opportunity, possibly, struggle, appreciate, happier, lucky, "
        "period, shirt, and welcome.\n\n"
        "Take your time with the reading. Let Chris Gardner's voice come through. "
        "And remember — you got a dream, you gotta protect it."
    )

    s4["activities"][1]["title"] = "Read: Complete Pursuit of Happyness Dialogue"
    s4["activities"][1]["description"] = "Read the full dialogue from beginning to end"

    s4["activities"][2]["title"] = "Speak: Practice the Complete Dialogue"
    s4["activities"][2]["description"] = "Practice speaking the entire dialogue aloud"

    s4["activities"][3]["title"] = "Listen: Complete Pursuit of Happyness Dialogue"
    s4["activities"][3]["description"] = "Listen to the complete dialogue and follow along"

    s4["activities"][4]["title"] = "Farewell and Vocabulary Review"
    s4["activities"][4]["description"] = "Final review of all 18 words and farewell"
    s4["activities"][4]["data"]["text"] = (
        "You've done it — you've completed the entire Pursuit of Happyness vocabulary course! "
        "Let's do one final review of all 18 words before we say goodbye.\n\n"

        "'Average' — typical, ordinary, not outstanding. "
        "Example: An average day for Chris Gardner was anything but ordinary.\n\n"
        "'Dream' — an ambition, a hope for the future. "
        "Example: She held onto her dream even when everyone around her said it was impossible.\n\n"
        "'Practice' — to perform repeatedly to improve; the act of practicing. "
        "Example: Years of practice turned a nervous beginner into a confident speaker.\n\n"
        "'Probably' — almost certainly, very likely. "
        "Example: He'll probably look back on this year as the turning point of his life.\n\n"
        "'Protect' — to keep safe from harm. "
        "Example: The best thing you can do for your dream is protect it from people who don't understand it.\n\n"
        "'Spend' — to use money or time. "
        "Example: She spent every evening studying, knowing the sacrifice would pay off.\n\n"

        "'Broker' — a person who buys and sells for others. "
        "Example: He went from sleeping in shelters to working as one of the top brokers in the city.\n\n"
        "'Chance' — a possibility or opportunity. "
        "Example: All he needed was one chance to prove what he could do.\n\n"
        "'Internship' — a period of work experience, often unpaid. "
        "Example: The internship was brutal, but it opened every door that followed.\n\n"
        "'Opportunity' — a favorable set of circumstances. "
        "Example: She created her own opportunity when none was offered to her.\n\n"
        "'Possibly' — perhaps, maybe. "
        "Example: Could this possibly be the break he'd been waiting for?\n\n"
        "'Struggle' — to fight hard despite difficulty. "
        "Example: Every struggle he endured made the victory sweeter.\n\n"

        "'Appreciate' — to recognize value or feel grateful. "
        "Example: He learned to appreciate the small things — a warm bed, a full meal, his son's laughter.\n\n"
        "'Happier' — more happy, the comparative form. "
        "Example: They were happier in their tiny apartment than they'd ever been in the big house.\n\n"
        "'Lucky' — having good fortune. "
        "Example: He didn't feel lucky — he felt like he'd earned every single thing he had.\n\n"
        "'Period' — a length of time; an emphatic ending. "
        "Example: That period of his life was over. He was never going back. Period.\n\n"
        "'Shirt' — a garment for the upper body. "
        "Example: He showed up in a paint-stained shirt and still got the job — "
        "because talent doesn't care what you're wearing.\n\n"
        "'Welcome' — a greeting; to receive warmly. "
        "Example: 'Welcome to Dean Witter' — four words that changed his life forever.\n\n"

        "Thank you for learning with Chris Gardner. You came for 18 vocabulary words, "
        "but I hope you're leaving with something more — a reminder that the distance between "
        "where you are and where you want to be is bridged by showing up, every single day, "
        "even when the world tells you to quit. "
        "Keep reading, keep speaking, keep writing. And remember — "
        "you got a dream, you gotta protect it. Goodbye, and good luck!"
    )

    return content


def create():
    token = get_firebase_id_token(UID)
    content = build_content()
    validate(content)
    print("Uploading curriculum...")
    resp = requests.post(f"{API_BASE}/curriculum/create", json={
        "firebaseIdToken": token,
        "language": "en",
        "userLanguage": "en",
        "content": json.dumps(content),
    })
    resp.raise_for_status()
    result = resp.json()
    cid = result.get("id") or result.get("curriculumId")
    print(f"Created en-en Pursuit of Happyness curriculum: {cid}")
    return cid


if __name__ == "__main__":
    create()
