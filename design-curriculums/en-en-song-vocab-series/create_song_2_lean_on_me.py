"""
Create en-en song curriculum #2: Lean on Me
Mirror of vi-en source 4Ho0bZURRPz2TiJA — all Vietnamese UI text rewritten in English.

Source song: Lean on Me by Bill Withers (1972)
YouTube: https://www.youtube.com/watch?v=fOZ-MySzAQo

18 vocabulary words in 3 groups of 6 (same as vi-en source):
  Group 1: lean, somebody, sorrow, strong, wise, carry
  Group 2: faith, pride, swallow, borrow, load, needs
  Group 3: bear, pain, problem, road, share, understand

All user-facing text in English. Reading passages stay as-is (already English).
Vocabulary words stay as-is (already English).

Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 9.1, 9.2, 9.3, 9.4, 9.5
"""

import sys, json, requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"
SOURCE_ID = "4Ho0bZURRPz2TiJA"

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
    if "music" not in content.get("contentTypeTags", []):
        errors.append("Missing 'music' in contentTypeTags")

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
    content["title"] = "'Lean on Me' — Bill Withers"

    content["description"] = (
        "SOMETIMES THE STRONGEST THING YOU CAN DO IS ASK FOR HELP.\n\n"
        "Bill Withers recorded 'Lean on Me' in 1972 with nothing but a piano, "
        "a bass line, and a voice that sounds like it's speaking directly to you. "
        "No orchestra, no production tricks — just a man telling you the simplest truth "
        "in the world: nobody makes it alone. The song became an instant anthem because "
        "it says out loud what most people are too proud to admit — that we all need "
        "somebody to lean on, and there's no shame in that.\n\n"
        "What makes this song extraordinary isn't complexity — it's honesty. "
        "Bill Withers grew up in a coal-mining town in West Virginia, the youngest of six children. "
        "He didn't start recording music until he was 31. When he wrote 'Lean on Me,' "
        "he was drawing on a lifetime of watching neighbors help neighbors, "
        "of communities that survived because people carried each other's burdens "
        "without being asked.\n\n"
        "Now imagine understanding every word Bill sings — from 'sorrow' when he names "
        "the weight people carry alone, to 'swallow' when he talks about pride getting "
        "in the way of asking for help, to 'lean' when he offers the simplest, most powerful "
        "gesture of friendship there is. Each vocabulary word is a lesson in what it means "
        "to be human.\n\n"
        "18 vocabulary words drawn directly from the lyrics, combined with "
        "a multi-sensory learning method — listening, reading, speaking, writing — "
        "so you build your English while absorbing Bill Withers' timeless message "
        "about friendship, support, and the courage it takes to let someone in."
    )

    content["preview"] = {
        "text": (
            "Have you ever had a friend who showed up exactly when you needed them most — "
            "not with advice, not with solutions, just with their presence? That's what "
            "'Lean on Me' sounds like. Bill Withers wrote this song as a promise between friends, "
            "and now you'll learn English through the very words he chose.\n\n"
            "18 English vocabulary words you'll learn: lean, somebody, sorrow, strong, wise, "
            "carry, faith, pride, swallow, borrow, load, needs, bear, pain, problem, road, "
            "share, understand.\n\n"
            "Across 5 sessions you'll read the actual lyrics, discover how Bill uses "
            "everyday words to express the deepest truths about friendship — from the sorrow "
            "we carry alone to the strength we find when we finally lean on each other.\n\n"
            "Tap the link below to watch the original performance — after this course, "
            "you'll hear Bill sing and understand every single word naturally."
        )
    }

    content["contentTypeTags"] = ["music"]
    content["is_public"] = False

    # ── Session 0: Group 1 — lean, somebody, sorrow, strong, wise, carry ──
    s0 = content["learningSessions"][0]
    s0["title"] = "Session 1: Leaning on Each Other — Lean on Me"

    # Activity 0: introAudio — song intro
    s0["activities"][0]["title"] = "Introduction to the Song"
    s0["activities"][0]["description"] = "Setting the stage for Bill Withers' anthem of friendship"
    s0["activities"][0]["data"]["text"] = (
        "Welcome to the vocabulary-through-music course! Today we begin with one of "
        "the most beloved songs in American music history — 'Lean on Me' by Bill Withers. "
        "Released in 1972 on the album 'Still Bill,' this song reached number one on the "
        "Billboard Hot 100 and has been covered, sampled, and sung at gatherings around the "
        "world for over fifty years. It was played at Barack Obama's inauguration. It was sung "
        "by communities after natural disasters. It's the song people reach for when words fail "
        "and all that's left is the need to hold each other up.\n\n"
        "Bill Withers wrote it after moving to Los Angeles from a small town in West Virginia. "
        "He missed the sense of community he'd grown up with — neighbors who looked out for "
        "each other without being asked. The song is his way of recreating that feeling in music: "
        "a simple promise that says, 'I'm here. You don't have to do this alone.'\n\n"
        "In this first session, you'll learn 6 vocabulary words from the opening verses: "
        "lean, somebody, sorrow, strong, wise, and carry. These are the words Bill uses to "
        "paint a picture of friendship at its most essential — no conditions, no judgment, "
        "just one person offering to carry another's weight."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s0["activities"][1]["title"] = "Vocabulary Introduction: Session 1"
    s0["activities"][1]["description"] = "Learn 6 words: lean, somebody, sorrow, strong, wise, carry"
    s0["activities"][1]["data"]["text"] = (
        "Let's dive into the first 6 vocabulary words from 'Lean on Me.' "
        "Each word comes straight from Bill Withers' lyrics, and understanding how he uses them "
        "will change the way you hear this song — and English — forever.\n\n"

        "The first word is 'lean.' It's a verb meaning 'to incline the body against something "
        "for support.' In the song's title and chorus, Bill sings 'Lean on me, when you're not "
        "strong' — using 'lean' as a metaphor for emotional dependence. When you lean on someone, "
        "you trust them to hold you up. The word can also mean 'thin' as an adjective ('lean meat') "
        "or 'to tilt' ('the tower leans to the left'). But in this song, it's purely about "
        "support and trust. Related phrases: 'lean into' (embrace difficulty), 'lean on' (depend on). "
        "Example: When everything fell apart, she leaned on her closest friends to get through it.\n\n"

        "The second word is 'somebody.' It's a pronoun meaning 'some person, someone.' "
        "Bill sings 'We all need somebody to lean on' — and the beauty of 'somebody' here is "
        "its universality. He doesn't say 'a therapist' or 'a parent' — just 'somebody.' "
        "Anyone. The word implies that the specific identity doesn't matter; what matters is "
        "that the person exists. 'Somebody' can also mean 'a person of importance': "
        "'She wants to be somebody.' The negative form is 'nobody.' "
        "Example: Everybody needs somebody who believes in them, even when they don't believe in themselves.\n\n"

        "The third word is 'sorrow.' It's a noun meaning 'deep distress, sadness, or grief.' "
        "Bill acknowledges that sorrow is part of life — 'We all have sorrow' — but he doesn't "
        "let it be the end of the story. Sorrow is the starting point for connection. "
        "The word carries more weight than 'sadness' — it implies a deeper, more lasting pain. "
        "'Sorrow' is often literary or poetic: 'a life marked by sorrow,' 'to drown one's sorrows.' "
        "The adjective form is 'sorrowful.' "
        "Example: There was a quiet sorrow in his eyes that he never talked about but everyone could see.\n\n"

        "The fourth word is 'strong.' It's an adjective meaning 'having great physical power' "
        "or 'able to withstand force or pressure.' But in the song, Bill uses it emotionally: "
        "'when you're not strong' — meaning when you feel unable to cope, when life has worn you down. "
        "This emotional use of 'strong' is extremely common in English: 'Stay strong,' "
        "'She's a strong person,' 'strong enough to ask for help.' The comparative is 'stronger,' "
        "the superlative 'strongest.' 'Strength' is the noun; 'strengthen' is the verb. "
        "Example: Being strong doesn't mean hiding your pain — it means knowing when to let others help.\n\n"

        "The fifth word is 'wise.' It's an adjective meaning 'having or showing experience, "
        "knowledge, and good judgment.' Bill sings about being wise enough to know when you need help. "
        "In English, 'wise' is deeper than 'smart' or 'intelligent' — it implies life experience "
        "and emotional maturity. A wise person doesn't just know facts; they understand people. "
        "'Wisdom' is the noun; 'wisely' is the adverb. Common phrases: 'wise beyond their years,' "
        "'a wise decision,' 'word to the wise.' "
        "Example: The wisest people she knew were the ones who admitted how much they still had to learn.\n\n"

        "The sixth word is 'carry.' It's a verb meaning 'to support and move something from one "
        "place to another.' In the song, Bill offers to carry someone's burden — their emotional "
        "weight, their problems, their pain. This figurative use is powerful: 'carry a burden,' "
        "'carry the weight of the world,' 'carry someone through a hard time.' "
        "The word can also mean 'to have on your person' ('carry a wallet') or 'to transmit' "
        "('carry a disease'). 'Carrier' is the noun form. "
        "Example: She carried the weight of her family's expectations without ever complaining.\n\n"

        "Your first 6 words: lean, somebody, sorrow, strong, wise, and carry. "
        "Each one is woven into the fabric of Bill Withers' promise of friendship. "
        "Let's practice them now!"
    )

    # Activities 2-6: flashcards/vocab — update titles and descriptions
    s0["activities"][2]["title"] = "Flashcards: Leaning on Each Other"
    s0["activities"][2]["description"] = "Learn 6 words: lean, somebody, sorrow, strong, wise, carry"

    s0["activities"][3]["title"] = "Flashcards: Speak Session 1 Vocabulary"
    s0["activities"][3]["description"] = "Practice saying 6 words: lean, somebody, sorrow, strong, wise, carry"

    s0["activities"][4]["title"] = "Flashcards: Recognize Session 1 Vocabulary"
    s0["activities"][4]["description"] = "Recognize 6 words: lean, somebody, sorrow, strong, wise, carry"

    s0["activities"][5]["title"] = "Flashcards: Recall Session 1 Vocabulary"
    s0["activities"][5]["description"] = "Recall 6 words: lean, somebody, sorrow, strong, wise, carry"

    s0["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 1"
    s0["activities"][6]["description"] = "Master 6 words: lean, somebody, sorrow, strong, wise, carry"

    # Activity 7: introAudio — grammar/usage
    s0["activities"][7]["title"] = "Grammar and Usage: Session 1"
    s0["activities"][7]["description"] = "How to use Session 1 vocabulary naturally in sentences"
    s0["activities"][7]["data"]["text"] = (
        "Great work! You've met your first 6 words. Now let's look at how they work "
        "in real English sentences, using the lyrics of 'Lean on Me' as our guide.\n\n"
        "'Lean' is a regular verb: lean, leaned, leaned (British English also uses 'leant'). "
        "It's often followed by a preposition: 'lean on' (depend on), 'lean against' (rest against), "
        "'lean forward,' 'lean back.' As an adjective, 'lean' means thin or efficient: "
        "'lean meat,' 'a lean organization.' The phrasal verb 'lean into' has become popular "
        "in business English, meaning to embrace a challenge rather than avoid it.\n\n"
        "'Somebody' and 'someone' are interchangeable in most contexts. 'Somebody' is slightly "
        "more informal. Both take singular verbs: 'Somebody is at the door,' not 'Somebody are.' "
        "In questions and negatives, 'anybody/anyone' is preferred: 'Is anybody there?' "
        "'Nobody/no one' is the negative: 'Nobody came.' 'Somebody else' means 'a different person.'\n\n"
        "'Sorrow' is primarily a noun, but it can also be a literary verb: 'She sorrowed for her lost child.' "
        "Common collocations: 'deep sorrow,' 'express sorrow,' 'drown one's sorrows' (drink to forget). "
        "The adjective 'sorrowful' and adverb 'sorrowfully' are more formal. "
        "In everyday speech, 'sadness' or 'grief' are more common, but 'sorrow' carries a poetic weight "
        "that makes it perfect for song lyrics.\n\n"
        "'Strong' is a one-syllable adjective with irregular comparison: strong, stronger, strongest. "
        "It collocates widely: 'strong coffee' (concentrated), 'strong wind' (powerful), "
        "'strong opinion' (firm), 'strong relationship' (solid). The noun 'strength' drops the 'o': "
        "strong → strength. 'Strengthen' is the verb: 'Exercise strengthens your muscles.' "
        "'Strongly' is the adverb: 'I strongly disagree.'\n\n"
        "'Wise' follows regular comparison: wise, wiser, wisest. 'Wisdom' is the noun — "
        "note the spelling change. 'Wisely' is the adverb: 'She invested wisely.' "
        "The suffix '-wise' can be added to nouns to mean 'in terms of': 'money-wise,' "
        "'time-wise.' 'Wise up' is a phrasal verb meaning 'to become aware': 'It's time to wise up.'\n\n"
        "'Carry' is a regular verb: carry, carried, carried. It takes a direct object: "
        "'carry a bag,' 'carry a tune,' 'carry a conversation.' Phrasal verbs: "
        "'carry on' (continue), 'carry out' (execute), 'carry over' (transfer). "
        "'Carry' can also mean 'to win' in some contexts: 'She carried the election.'"
    )

    # Activity 8: reading — keep text as-is (already English), update title/description
    s0["activities"][8]["title"] = "Read: Lean on Me Lyrics (Part 1)"
    s0["activities"][8]["description"] = "Read the opening verses of Lean on Me"

    # Activity 9: speakReading
    s0["activities"][9]["title"] = "Speak: Practice the Lyrics (Part 1)"
    s0["activities"][9]["description"] = "Practice speaking the opening verses aloud"

    # Activity 10: readAlong
    s0["activities"][10]["title"] = "Listen: Lean on Me (Part 1)"
    s0["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s0["activities"][11]["title"] = "Write: Friendship and Support"
    s0["activities"][11]["description"] = "Write sentences using Session 1 vocabulary"
    ws_items_0 = s0["activities"][11]["data"]["items"]
    ws_items_0[0]["prompt"] = (
        "Use the word 'lean' to write about depending on someone for support — "
        "just as Bill Withers invites a friend to lean on him when times are hard. "
        "Example: When everything fell apart, she leaned on her closest friends to get through it."
    )
    ws_items_0[1]["prompt"] = (
        "Use the word 'somebody' to write about the importance of having someone in your life — "
        "as the song reminds us that we all need somebody to lean on. "
        "Example: Everybody needs somebody who believes in them, even when they don't believe in themselves."
    )
    ws_items_0[2]["prompt"] = (
        "Use the word 'sorrow' to write about deep sadness or grief — "
        "as Bill acknowledges that sorrow is a universal part of the human experience. "
        "Example: There was a quiet sorrow in his eyes that he never talked about but everyone could see."
    )
    ws_items_0[3]["prompt"] = (
        "Use the word 'strong' to write about strength — physical or emotional — "
        "as the song speaks to those moments when you're not feeling strong enough. "
        "Example: Being strong doesn't mean hiding your pain — it means knowing when to let others help."
    )
    ws_items_0[4]["prompt"] = (
        "Use the word 'wise' to write about wisdom, experience, or good judgment — "
        "as the song suggests that true wisdom includes knowing when to ask for help. "
        "Example: The wisest people she knew were the ones who admitted how much they still had to learn."
    )
    ws_items_0[5]["prompt"] = (
        "Use the word 'carry' to write about bearing a burden for someone else — "
        "like Bill Withers' offer to carry a friend's weight when they can't do it alone. "
        "Example: She carried the weight of her family's expectations without ever complaining."
    )

    # ── Session 1: Group 2 — faith, pride, swallow, borrow, load, needs ──
    s1 = content["learningSessions"][1]
    s1["title"] = "Session 2: Faith and Pride"

    # Activity 0: introAudio — session intro
    s1["activities"][0]["title"] = "Introduction to Session 2"
    s1["activities"][0]["description"] = "Recap Session 1 and introduce the theme of faith and humility"
    s1["activities"][0]["data"]["text"] = (
        "Welcome back to Session 2! In our first session, you learned 6 words from the opening "
        "of 'Lean on Me': lean, somebody, sorrow, strong, wise, and carry. You discovered "
        "how Bill Withers uses the simplest vocabulary to build a portrait of friendship — "
        "where leaning on somebody isn't weakness but wisdom, and carrying another person's "
        "sorrow is the strongest thing you can do.\n\n"
        "Now we're moving into the heart of the song. In these verses, Bill gets more specific "
        "about what stops people from asking for help. He sings about pride — the stubborn voice "
        "that says 'I can handle this alone.' He sings about faith — the quiet trust that someone "
        "will be there when you call. And he uses one of the most vivid images in the song: "
        "swallowing your pride, as if pride were something physical stuck in your throat.\n\n"
        "Today you'll learn 6 new words: faith, pride, swallow, borrow, load, and needs. "
        "These words carry the emotional tension of the song — the push and pull between "
        "wanting to be independent and knowing you can't do everything alone."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s1["activities"][1]["title"] = "Vocabulary Introduction: Session 2"
    s1["activities"][1]["description"] = "Learn 6 words: faith, pride, swallow, borrow, load, needs"
    s1["activities"][1]["data"]["text"] = (
        "Let's learn 6 new vocabulary words from the heart of 'Lean on Me' — "
        "the verses where Bill Withers talks about what keeps people from reaching out.\n\n"

        "The first word is 'faith.' It's a noun meaning 'complete trust or confidence in someone "
        "or something.' Bill doesn't use 'faith' in a religious sense here — he uses it to describe "
        "the trust between friends. Having faith in someone means believing they'll come through "
        "for you. 'Faith' can also mean 'a system of religious belief': 'the Christian faith.' "
        "Common phrases: 'keep the faith' (stay hopeful), 'in good faith' (with honest intentions), "
        "'a leap of faith' (trusting without proof). 'Faithful' is the adjective; 'faithfully' the adverb. "
        "Example: She never lost faith in her brother, even when everyone else had given up on him.\n\n"

        "The second word is 'pride.' It's a noun meaning 'a feeling of deep pleasure or satisfaction "
        "from one's own achievements' or 'an excessively high opinion of oneself.' In the song, "
        "pride is the obstacle — the thing that stops you from asking for help. Bill says you need "
        "to swallow your pride, meaning set aside your ego. But pride isn't always negative: "
        "'She takes pride in her work' is positive. 'Pride and joy' means something you're very proud of. "
        "'Proud' is the adjective; 'proudly' the adverb. "
        "Example: His pride wouldn't let him admit he was struggling, even to his closest friends.\n\n"

        "The third word is 'swallow.' It's a verb meaning 'to cause food or drink to pass from "
        "the mouth to the stomach.' But in the song, Bill uses it figuratively: 'swallow your pride' — "
        "meaning to suppress your ego, to push down the part of you that resists asking for help. "
        "This figurative use is common: 'swallow your anger,' 'hard to swallow' (difficult to accept), "
        "'swallow a lie' (believe something false). 'Swallow' can also be a noun — it's a type of bird. "
        "Example: It took everything he had to swallow his pride and apologize, but it saved the friendship.\n\n"

        "The fourth word is 'borrow.' It's a verb meaning 'to take and use something belonging to "
        "someone else with the intention of returning it.' In the song, Bill offers his strength "
        "to borrow — you can take it, use it, and give it back when you're on your feet again. "
        "This is a beautiful metaphor: strength as something lendable. 'Borrow' is the opposite "
        "of 'lend': 'I borrow from you; you lend to me.' Common phrases: 'borrow time' (delay the inevitable), "
        "'borrowed ideas.' The noun 'borrower' refers to the person who borrows. "
        "Example: You can borrow my courage today — I'll need yours tomorrow.\n\n"

        "The fifth word is 'load.' It's a noun meaning 'a heavy or bulky thing being carried' "
        "or 'a weight or source of pressure.' Bill sings about helping someone carry their load — "
        "their problems, their emotional weight. 'Load' is both literal ('a truckload of bricks') "
        "and figurative ('a heavy load on her shoulders'). As a verb, 'load' means 'to put cargo on': "
        "'load the truck,' 'load a program.' Common phrases: 'a load off my mind' (relief), "
        "'loads of' (informal for 'lots of'). "
        "Example: After talking to her friend, she felt like a huge load had been lifted off her shoulders.\n\n"

        "The sixth word is 'needs.' It can be a noun (plural of 'need') or a verb (third person singular). "
        "As a noun, 'needs' refers to things that are necessary: 'basic needs,' 'emotional needs,' "
        "'the needs of the community.' In the song, Bill recognizes that everyone has needs — "
        "no one is completely self-sufficient. As a verb: 'She needs help.' "
        "The phrase 'needs must' is an old expression meaning 'it's necessary.' "
        "'Needy' means 'requiring a lot of attention or support.' "
        "Example: A good friend pays attention to your needs even when you don't say them out loud.\n\n"

        "Your 6 new words: faith, pride, swallow, borrow, load, needs. "
        "Combined with Session 1, you now have 12 words from 'Lean on Me.' "
        "Let's put them to work!"
    )

    # Activities 2-6: flashcards/vocab
    s1["activities"][2]["title"] = "Flashcards: Faith and Pride"
    s1["activities"][2]["description"] = "Learn 6 words: faith, pride, swallow, borrow, load, needs"

    s1["activities"][3]["title"] = "Flashcards: Speak Session 2 Vocabulary"
    s1["activities"][3]["description"] = "Practice saying 6 words: faith, pride, swallow, borrow, load, needs"

    s1["activities"][4]["title"] = "Flashcards: Recognize Session 2 Vocabulary"
    s1["activities"][4]["description"] = "Recognize 6 words: faith, pride, swallow, borrow, load, needs"

    s1["activities"][5]["title"] = "Flashcards: Recall Session 2 Vocabulary"
    s1["activities"][5]["description"] = "Recall 6 words: faith, pride, swallow, borrow, load, needs"

    s1["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 2"
    s1["activities"][6]["description"] = "Master 6 words: faith, pride, swallow, borrow, load, needs"

    # Activity 7: introAudio — grammar/usage
    s1["activities"][7]["title"] = "Grammar and Usage: Session 2"
    s1["activities"][7]["description"] = "How to use Session 2 vocabulary naturally in sentences"
    s1["activities"][7]["data"]["text"] = (
        "Excellent! Let's explore how these 6 words behave in real English.\n\n"
        "'Faith' is an uncountable noun when it means 'trust': 'I have faith in you,' "
        "not 'I have a faith in you.' But it's countable when it means 'a religion': "
        "'people of different faiths.' 'Faithful' means loyal: 'a faithful friend,' "
        "'a faithful dog.' 'Faithless' means disloyal or without belief. "
        "'In good faith' is a legal and everyday phrase meaning 'with honest intentions.'\n\n"
        "'Pride' is usually uncountable: 'She felt pride,' not 'She felt a pride.' "
        "But 'a pride of lions' is a collective noun for a group of lions. "
        "'Proud' is the adjective: 'I'm proud of you.' 'Pride oneself on' means "
        "'to be especially proud of': 'She prides herself on her punctuality.' "
        "'Swallow your pride' and 'take pride in' are the two most common idioms.\n\n"
        "'Swallow' is a regular verb: swallow, swallowed, swallowed. "
        "Literally: 'Chew your food before you swallow.' Figuratively: 'swallow your pride,' "
        "'swallow your words' (take back what you said), 'a bitter pill to swallow' "
        "(something unpleasant you must accept). The noun 'swallow' can mean the act of swallowing "
        "or a small migratory bird.\n\n"
        "'Borrow' is a regular verb: borrow, borrowed, borrowed. "
        "It's often confused with 'lend': 'Can I borrow your pen?' (I take it) vs. "
        "'Can you lend me your pen?' (you give it). Never say 'Can you borrow me your pen?' — "
        "that's a common error. 'Borrowing' can also be abstract: 'borrowed time,' "
        "'borrowed ideas,' 'a borrowed phrase.'\n\n"
        "'Load' as a noun: 'a heavy load,' 'a load of laundry,' 'loads of fun.' "
        "As a verb: 'load the dishwasher,' 'load a webpage.' 'Loaded' as an adjective "
        "means 'carrying a load,' 'wealthy' (slang), or 'biased': 'a loaded question.' "
        "'Overload' means too much: 'information overload,' 'overloaded with work.'\n\n"
        "'Needs' — the verb 'need' can be a regular verb ('She needs help') or a modal verb "
        "('Need I say more?'). The modal use is formal and mostly British. "
        "As a noun, 'needs' is always plural when referring to requirements: "
        "'basic needs,' 'special needs,' 'the needs of the many.' "
        "'Needless' means unnecessary: 'needless to say' (it goes without saying)."
    )

    # Activity 8-10: reading/speak/listen — keep text, update titles
    s1["activities"][8]["title"] = "Read: Lean on Me Lyrics (Part 2)"
    s1["activities"][8]["description"] = "Read the middle verses about faith, pride, and asking for help"

    s1["activities"][9]["title"] = "Speak: Practice the Lyrics (Part 2)"
    s1["activities"][9]["description"] = "Practice speaking the middle verses aloud"

    s1["activities"][10]["title"] = "Listen: Lean on Me (Part 2)"
    s1["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s1["activities"][11]["title"] = "Write: Faith and Sharing"
    s1["activities"][11]["description"] = "Write sentences using Session 2 vocabulary"
    ws_items_1 = s1["activities"][11]["data"]["items"]
    ws_items_1[0]["prompt"] = (
        "Use the word 'faith' to write about trust or confidence in someone — "
        "like the quiet faith between friends that Bill Withers sings about. "
        "Example: She never lost faith in her brother, even when everyone else had given up on him."
    )
    ws_items_1[1]["prompt"] = (
        "Use the word 'pride' to write about self-respect or ego — "
        "as the song warns that too much pride can keep you from accepting help. "
        "Example: His pride wouldn't let him admit he was struggling, even to his closest friends."
    )
    ws_items_1[2]["prompt"] = (
        "Use the word 'swallow' to write about suppressing an emotion or accepting something difficult — "
        "like the song's call to swallow your pride and reach out. "
        "Example: It took everything he had to swallow his pride and apologize, but it saved the friendship."
    )
    ws_items_1[3]["prompt"] = (
        "Use the word 'borrow' to write about taking something temporarily — "
        "as Bill offers his strength for a friend to borrow until they're back on their feet. "
        "Example: You can borrow my courage today — I'll need yours tomorrow."
    )
    ws_items_1[4]["prompt"] = (
        "Use the word 'load' to write about a burden or weight someone carries — "
        "like the emotional load the song promises to help lighten. "
        "Example: After talking to her friend, she felt like a huge load had been lifted off her shoulders."
    )
    ws_items_1[5]["prompt"] = (
        "Use the word 'needs' to write about what people require — "
        "as the song recognizes that everyone has needs they can't meet alone. "
        "Example: A good friend pays attention to your needs even when you don't say them out loud."
    )

    # ── Session 2: Group 3 — bear, pain, problem, road, share, understand ──
    s2 = content["learningSessions"][2]
    s2["title"] = "Session 3: Bearing and Sharing"

    # Activity 0: introAudio — session intro
    s2["activities"][0]["title"] = "Introduction to Session 3"
    s2["activities"][0]["description"] = "Recap Sessions 1-2 and introduce the themes of endurance and empathy"
    s2["activities"][0]["data"]["text"] = (
        "Welcome to Session 3 — the final learning session before your review! "
        "So far you've learned 12 words from 'Lean on Me.' In Session 1, you met "
        "lean, somebody, sorrow, strong, wise, and carry — the words of the song's opening promise, "
        "where Bill Withers tells a friend that leaning on someone isn't weakness but wisdom, "
        "and that carrying another's sorrow is what strong people do. "
        "In Session 2, you learned faith, pride, swallow, borrow, load, and needs — "
        "the words of the song's emotional core, where Bill names the thing that stops most people "
        "from asking for help: pride.\n\n"
        "Now we reach the song's final message. Bill shifts from offering help to describing "
        "what true friendship looks like in practice. He sings about bearing pain together, "
        "about sharing the road, about the deep understanding that comes from walking alongside "
        "someone through their hardest days. This is where the song stops being advice "
        "and becomes a lived experience.\n\n"
        "Your final 6 words: bear, pain, problem, road, share, and understand. "
        "By the end of this session, you'll have all 18 vocabulary words — and you'll hear "
        "'Lean on Me' the way Bill Withers intended it to be heard."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s2["activities"][1]["title"] = "Vocabulary Introduction: Session 3"
    s2["activities"][1]["description"] = "Learn 6 words: bear, pain, problem, road, share, understand"
    s2["activities"][1]["data"]["text"] = (
        "Here are your final 6 vocabulary words, drawn from the most powerful verses "
        "of 'Lean on Me.'\n\n"

        "The first word is 'bear.' It's a verb meaning 'to carry, support, or endure.' "
        "In the song, Bill sings about bearing someone's pain — taking on their suffering "
        "as if it were your own. 'Bear' is one of the richest verbs in English: "
        "'bear a burden' (carry it), 'bear fruit' (produce results), 'bear in mind' (remember), "
        "'bear witness' (testify), 'can't bear it' (can't tolerate it). The past tense is 'bore,' "
        "the past participle 'borne.' Of course, 'bear' is also a noun — the large furry animal. "
        "Context always makes the meaning clear. "
        "Example: She bore the responsibility of caring for her siblings with quiet determination.\n\n"

        "The second word is 'pain.' It's a noun meaning 'physical suffering or discomfort' "
        "or 'mental suffering or distress.' Bill uses it in the emotional sense — the pain "
        "that comes from loss, loneliness, or feeling overwhelmed. 'Pain' is both countable "
        "and uncountable: 'I'm in pain' (uncountable), 'growing pains' (countable). "
        "'Painful' is the adjective; 'painfully' the adverb; 'painkiller' is medicine that reduces pain. "
        "The phrase 'no pain, no gain' means effort is required for progress. "
        "Example: The pain of losing someone you love never fully goes away — you just learn to carry it differently.\n\n"

        "The third word is 'problem.' It's a noun meaning 'a matter or situation regarded as "
        "unwelcome or harmful and needing to be dealt with.' Bill sings about helping with "
        "someone's problems — the practical difficulties of life. 'Problem' is one of the most "
        "common nouns in English: 'solve a problem,' 'no problem' (you're welcome), "
        "'problem-solving,' 'the root of the problem.' 'Problematic' is the adjective. "
        "In informal speech, 'no problem' has largely replaced 'you're welcome.' "
        "Example: The biggest problem wasn't the situation itself — it was facing it alone.\n\n"

        "The fourth word is 'road.' It's a noun meaning 'a wide way leading from one place "
        "to another.' But in the song, Bill uses 'road' as a metaphor for life's journey — "
        "the path you walk, with all its twists and difficulties. This metaphorical use is "
        "deeply embedded in English: 'the road ahead,' 'a long road to recovery,' "
        "'the road less traveled,' 'down the road' (in the future), 'on the road' (traveling). "
        "'Roadblock' means an obstacle; 'roadmap' means a plan. "
        "Example: The road to forgiveness is long, but every step forward makes the next one easier.\n\n"

        "The fifth word is 'share.' It's a verb meaning 'to give a portion of something to others' "
        "or 'to have something in common.' Bill sings about sharing burdens — dividing the weight "
        "so no one person has to carry it all. 'Share' is fundamental to human connection: "
        "'share a meal,' 'share your feelings,' 'share a room,' 'share responsibility.' "
        "As a noun, 'share' means 'a portion': 'your fair share,' 'market share,' "
        "'shares' (stocks in a company). "
        "Example: The moment she shared what she was going through, the weight on her shoulders halved.\n\n"

        "The sixth and final word is 'understand.' It's a verb meaning 'to perceive the intended "
        "meaning of words or a speaker' or 'to be sympathetically aware of someone's feelings.' "
        "In the song, understanding is the deepest form of friendship — not just hearing someone's "
        "words but truly grasping what they're going through. The past tense is 'understood.' "
        "'Understanding' can be a noun ('a deep understanding'), an adjective ('an understanding friend'), "
        "or a gerund. 'Misunderstand' is the opposite. "
        "Example: You don't have to fix my problems — just understanding that they exist is enough.\n\n"

        "And there you have it — all 18 words: lean, somebody, sorrow, strong, wise, carry, "
        "faith, pride, swallow, borrow, load, needs, bear, pain, problem, road, share, "
        "and understand. You now have the complete vocabulary of 'Lean on Me.' "
        "Let's practice these final 6!"
    )

    # Activities 2-6: flashcards/vocab
    s2["activities"][2]["title"] = "Flashcards: Bearing and Sharing"
    s2["activities"][2]["description"] = "Learn 6 words: bear, pain, problem, road, share, understand"

    s2["activities"][3]["title"] = "Flashcards: Speak Session 3 Vocabulary"
    s2["activities"][3]["description"] = "Practice saying 6 words: bear, pain, problem, road, share, understand"

    s2["activities"][4]["title"] = "Flashcards: Recognize Session 3 Vocabulary"
    s2["activities"][4]["description"] = "Recognize 6 words: bear, pain, problem, road, share, understand"

    s2["activities"][5]["title"] = "Flashcards: Recall Session 3 Vocabulary"
    s2["activities"][5]["description"] = "Recall 6 words: bear, pain, problem, road, share, understand"

    s2["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 3"
    s2["activities"][6]["description"] = "Master 6 words: bear, pain, problem, road, share, understand"

    # Activity 7: introAudio — grammar/usage
    s2["activities"][7]["title"] = "Grammar and Usage: Session 3"
    s2["activities"][7]["description"] = "How to use Session 3 vocabulary naturally in sentences"
    s2["activities"][7]["data"]["text"] = (
        "Let's look at how these final 6 words work in English grammar.\n\n"
        "'Bear' as a verb is irregular: bear, bore, borne (or born for 'give birth'). "
        "It's transitive: 'bear a burden,' 'bear the cost,' 'bear responsibility.' "
        "'I can't bear it' means 'I can't tolerate it.' 'Bear with me' means 'be patient with me.' "
        "'Bear in mind' means 'remember.' 'Bearable' means 'tolerable'; 'unbearable' means "
        "'too painful or difficult to endure.' Don't confuse the verb 'bear' with the noun 'bear' "
        "(the animal) — they're spelled the same but unrelated.\n\n"
        "'Pain' as a noun is both countable and uncountable. Uncountable: 'She's in pain,' "
        "'pain relief.' Countable: 'aches and pains,' 'growing pains,' 'a pain in the neck' "
        "(an annoying person or thing). 'Painful' is the adjective: 'a painful memory,' "
        "'painfully honest.' 'Painless' means without pain: 'a painless procedure.' "
        "The verb 'pain' is formal: 'It pains me to say this.'\n\n"
        "'Problem' is a countable noun: 'a problem,' 'two problems,' 'many problems.' "
        "It collocates with verbs: 'solve a problem,' 'face a problem,' 'cause a problem,' "
        "'address a problem.' 'Problematic' is the adjective: 'a problematic situation.' "
        "'Problem-solving' is a compound noun/adjective. In informal English, 'no problem' "
        "is used as 'you're welcome' or 'it's fine.'\n\n"
        "'Road' is a countable noun: 'a road,' 'two roads,' 'the main road.' "
        "Metaphorical uses are everywhere: 'the road to success,' 'a bumpy road,' "
        "'at a crossroads' (facing a decision), 'the road ahead,' 'hit the road' (leave). "
        "'Road' vs. 'street': roads connect places; streets are in towns with buildings on both sides. "
        "'Roadside' means 'at the edge of a road.'\n\n"
        "'Share' is a regular verb: share, shared, shared. It takes a direct object and often "
        "'with': 'share something with someone.' 'Share' can also be intransitive: "
        "'Children need to learn to share.' As a noun: 'your share of the profits,' "
        "'market share,' 'shares' (stocks). 'Shareholder' is a person who owns shares.\n\n"
        "'Understand' is irregular: understand, understood, understood. "
        "It can take a direct object ('I understand the problem'), a clause ('I understand that "
        "you're upset'), or stand alone ('I understand'). 'Understanding' as a noun means "
        "'comprehension' or 'an informal agreement': 'We have an understanding.' "
        "'Misunderstand' is the opposite: 'Don't misunderstand me.' "
        "'Understandable' means 'reasonable': 'Your frustration is understandable.'"
    )

    # Activity 8-10: reading/speak/listen
    s2["activities"][8]["title"] = "Read: Lean on Me Lyrics (Part 3)"
    s2["activities"][8]["description"] = "Read the final verses about bearing pain and sharing the road"

    s2["activities"][9]["title"] = "Speak: Practice the Lyrics (Part 3)"
    s2["activities"][9]["description"] = "Practice speaking the final verses aloud"

    s2["activities"][10]["title"] = "Listen: Lean on Me (Part 3)"
    s2["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s2["activities"][11]["title"] = "Write: Empathy and Understanding"
    s2["activities"][11]["description"] = "Write sentences using Session 3 vocabulary"
    ws_items_2 = s2["activities"][11]["data"]["items"]
    ws_items_2[0]["prompt"] = (
        "Use the word 'bear' to write about enduring or carrying something difficult — "
        "like Bill Withers' promise to help bear a friend's pain. "
        "Example: She bore the responsibility of caring for her siblings with quiet determination."
    )
    ws_items_2[1]["prompt"] = (
        "Use the word 'pain' to write about suffering — physical or emotional — "
        "as the song acknowledges that pain is part of life but doesn't have to be faced alone. "
        "Example: The pain of losing someone you love never fully goes away — you just learn to carry it differently."
    )
    ws_items_2[2]["prompt"] = (
        "Use the word 'problem' to write about a difficulty or challenge — "
        "as the song offers to help with whatever problems a friend is facing. "
        "Example: The biggest problem wasn't the situation itself — it was facing it alone."
    )
    ws_items_2[3]["prompt"] = (
        "Use the word 'road' to write about a journey or path through life — "
        "like the song's image of walking the road together instead of alone. "
        "Example: The road to forgiveness is long, but every step forward makes the next one easier."
    )
    ws_items_2[4]["prompt"] = (
        "Use the word 'share' to write about giving part of something to others — "
        "as the song's deepest message is that sharing burdens makes them lighter. "
        "Example: The moment she shared what she was going through, the weight on her shoulders halved."
    )
    ws_items_2[5]["prompt"] = (
        "Use the word 'understand' to write about truly grasping someone's experience — "
        "as the song shows that understanding is the deepest form of friendship. "
        "Example: You don't have to fix my problems — just understanding that they exist is enough."
    )

    # ── Session 3: Review (4 activities) ──
    s3 = content["learningSessions"][3]
    s3["title"] = "Review"

    s3["activities"][0]["title"] = "Congratulations and Review"
    s3["activities"][0]["description"] = "Celebrate your progress and prepare for the full review"
    s3["activities"][0]["data"]["text"] = (
        "Congratulations! You've learned all 18 vocabulary words from 'Lean on Me.' "
        "Let's take a moment to look back at what you've accomplished.\n\n"
        "In Session 1, you learned lean, somebody, sorrow, strong, wise, and carry — "
        "the words of the song's opening promise, where Bill Withers paints a picture of "
        "friendship at its most essential: one person offering to carry another's weight "
        "without conditions or judgment.\n\n"
        "In Session 2, you learned faith, pride, swallow, borrow, load, and needs — "
        "the words of the song's emotional core, where Bill names the biggest obstacle "
        "to asking for help — pride — and offers his strength as something you can borrow "
        "until you find your own again.\n\n"
        "In Session 3, you learned bear, pain, problem, road, share, and understand — "
        "the words of the song's deepest message, where friendship becomes action: "
        "bearing pain together, sharing the road, and understanding each other "
        "not through words but through presence.\n\n"
        "Now it's time to review all 18 words together. This review session will test your "
        "recognition and recall across all three groups. After this, you'll be ready to read "
        "the complete lyrics in the final session. Let's go!"
    )

    s3["activities"][1]["title"] = "Flashcards: Review All 18 Words"
    s3["activities"][1]["description"] = "Review all 18 vocabulary words from Lean on Me"

    s3["activities"][2]["title"] = "Flashcards: Recognize All Vocabulary"
    s3["activities"][2]["description"] = "Test your recognition of all 18 words"

    s3["activities"][3]["title"] = "Flashcards: Recall All Vocabulary"
    s3["activities"][3]["description"] = "Test your recall of all 18 words"

    # ── Session 4: Full reading + farewell (5 activities) ──
    s4 = content["learningSessions"][4]
    s4["title"] = "Full Lyrics Reading"

    s4["activities"][0]["title"] = "Introduction to the Complete Reading"
    s4["activities"][0]["description"] = "Prepare for reading the full Lean on Me lyrics"
    s4["activities"][0]["data"]["text"] = (
        "Welcome to the final session! This is the moment everything comes together. "
        "Over the past three sessions, you've built a vocabulary of 18 words drawn directly "
        "from the lyrics of 'Lean on Me.' You've learned their meanings, practiced their "
        "pronunciation, explored their grammar, and used them in your own writing.\n\n"
        "Now you're going to read the complete lyrics — all three sections combined into one "
        "continuous passage. As you read, you'll encounter every single one of your 18 words "
        "in context. This time, they won't be new — they'll be familiar friends.\n\n"
        "Here are all 18 words you'll see: lean, somebody, sorrow, strong, wise, carry, "
        "faith, pride, swallow, borrow, load, needs, bear, pain, problem, road, share, "
        "and understand.\n\n"
        "Take your time with the reading. Let Bill's voice come through the words. "
        "And remember — we all need somebody to lean on."
    )

    s4["activities"][1]["title"] = "Read: Complete Lean on Me Lyrics"
    s4["activities"][1]["description"] = "Read the full lyrics from beginning to end"

    s4["activities"][2]["title"] = "Speak: Practice the Complete Lyrics"
    s4["activities"][2]["description"] = "Practice speaking the entire lyrics aloud"

    s4["activities"][3]["title"] = "Listen: Complete Lean on Me"
    s4["activities"][3]["description"] = "Listen to the complete lyrics and follow along"

    s4["activities"][4]["title"] = "Farewell and Vocabulary Review"
    s4["activities"][4]["description"] = "Final review of all 18 words and farewell"
    s4["activities"][4]["data"]["text"] = (
        "You've done it — you've completed the entire 'Lean on Me' vocabulary course! "
        "Let's do one final review of all 18 words before we say goodbye.\n\n"

        "'Lean' — to incline the body against something for support; to depend on someone. "
        "Example: After the diagnosis, he finally learned to lean on the people who loved him.\n\n"
        "'Somebody' — some person; anyone. "
        "Example: All it takes is somebody who listens without trying to fix everything.\n\n"
        "'Sorrow' — deep distress, sadness, or grief. "
        "Example: The sorrow of saying goodbye was softened by the promise of meeting again.\n\n"
        "'Strong' — having great power or ability to withstand; emotionally resilient. "
        "Example: She was strong not because nothing hurt her, but because she kept going when it did.\n\n"
        "'Wise' — having experience, knowledge, and good judgment. "
        "Example: A wise friend once told her that asking for help is a sign of strength, not weakness.\n\n"
        "'Carry' — to support and move; to bear a burden for someone. "
        "Example: They carried each other through the hardest year of their lives without keeping score.\n\n"

        "'Faith' — complete trust or confidence in someone. "
        "Example: He kept faith in the friendship even when months passed without a phone call.\n\n"
        "'Pride' — a feeling of satisfaction; an excessively high opinion of oneself. "
        "Example: It was pride that kept him silent, and humility that finally made him speak.\n\n"
        "'Swallow' — to cause to pass from mouth to stomach; to suppress an emotion. "
        "Example: She swallowed her frustration and chose to listen instead of argue.\n\n"
        "'Borrow' — to take something with the intention of returning it. "
        "Example: On the days when her own hope ran out, she borrowed her mother's.\n\n"
        "'Load' — a heavy thing being carried; a weight or source of pressure. "
        "Example: Sharing the load didn't make the problem disappear, but it made it bearable.\n\n"
        "'Needs' — things that are necessary; requirements for well-being. "
        "Example: The best relationships are the ones where both people's needs matter equally.\n\n"

        "'Bear' — to carry, support, or endure something difficult. "
        "Example: He bore the loss quietly, but his friends could see it in his eyes.\n\n"
        "'Pain' — physical or emotional suffering. "
        "Example: Sometimes the deepest pain comes not from what happened, but from facing it alone.\n\n"
        "'Problem' — a matter needing to be dealt with; a difficulty. "
        "Example: The problem looked impossible until they decided to tackle it together.\n\n"
        "'Road' — a way leading from one place to another; a journey through life. "
        "Example: The road was long and uncertain, but walking it with a friend made all the difference.\n\n"
        "'Share' — to give a portion to others; to have something in common. "
        "Example: They shared everything — meals, secrets, silences, and the occasional terrible joke.\n\n"
        "'Understand' — to perceive meaning; to be sympathetically aware of someone's feelings. "
        "Example: She didn't need him to have the answers — she just needed him to understand.\n\n"

        "Thank you for learning with Bill Withers' 'Lean on Me.' "
        "You came for 18 vocabulary words, but I hope you're leaving with something more — "
        "a reminder that the simplest offer in the world is also the most powerful: "
        "'I'm here. Lean on me.' Bill Withers didn't need fancy words or complicated melodies. "
        "He just needed the truth — that nobody makes it alone, and there's no shame in "
        "reaching out. Keep reading, keep speaking, keep writing — and when someone you love "
        "is struggling, don't wait for them to ask. Just show up. That's what this song is about."
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
    print(f"Created en-en Lean on Me curriculum: {cid}")
    return cid


if __name__ == "__main__":
    create()
