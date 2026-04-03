"""
Create en-en movie curriculum #1: The Shawshank Redemption
Mirror of vi-en source yCj2EZKIPTkFNqtS — all Vietnamese UI text rewritten in English.

Source movie: The Shawshank Redemption (1994)
YouTube: https://www.youtube.com/watch?v=kotNxb2YApk

18 vocabulary words in 3 groups of 6 (same as vi-en source):
  Group 1: beard, marbles, pacific, memory, worthless, charter
  Group 2: institutional, underestimate, scare, begin, outside, ocean
  Group 3: mistakes, paid, pipe, choice, busy, dying

All user-facing text in English. Reading passages stay as-is (already English).
Vocabulary words stay as-is (already English).

Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 9.1, 9.2, 9.3, 9.4, 9.5
"""

import sys, json, requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"
SOURCE_ID = "yCj2EZKIPTkFNqtS"

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
    content["title"] = "'The Shawshank Redemption' — Get Busy Living or Get Busy Dying"

    content["description"] = (
        "WHAT IF THE WALLS YOU'VE BUILT TO PROTECT YOURSELF ARE THE VERY THINGS "
        "KEEPING YOU TRAPPED?\n\n"
        "Think about it — the routines you cling to, the comfort zones you refuse to leave, "
        "the voice in your head that says 'better safe than sorry.' Andy Dufresne spent "
        "nineteen years inside Shawshank Prison, and yet he was freer than most people "
        "who've never seen the inside of a cell. His best friend Red spent forty years "
        "behind bars and couldn't imagine life on the outside — because the walls had become "
        "his entire world.\n\n"
        "This is a film about hope — the dangerous, stubborn, irrational kind of hope "
        "that refuses to die even when everything around you says it should. Andy crawls "
        "through a river of filth and comes out clean on the other side. Red sits in a parole "
        "hearing and finally tells the truth. And somewhere on a beach in Zihuatanejo, "
        "two old friends meet again under an impossibly blue sky.\n\n"
        "When you understand that 'institutional' doesn't just mean 'related to an institution' "
        "but describes a man so broken by the system that freedom itself becomes terrifying — "
        "you'll start hearing English with completely new depth. That's the moment cinema "
        "becomes your greatest teacher.\n\n"
        "18 vocabulary words drawn directly from the film's dialogue, combined with "
        "a multi-sensory learning method — listening, reading, speaking, writing — "
        "so you sharpen your English while carrying the most powerful message in cinema: "
        "hope is a good thing, maybe the best of things, and no good thing ever dies."
    )

    content["preview"] = {
        "text": (
            "Remember the scene where Andy Dufresne stands in the rain after crawling "
            "through five hundred yards of sewage pipe — arms spread wide, face turned "
            "to the sky, finally free?\n\n"
            "18 English vocabulary words you'll learn: beard, marbles, pacific, memory, "
            "worthless, charter, institutional, underestimate, scare, begin, outside, ocean, "
            "mistakes, paid, pipe, choice, busy, dying.\n\n"
            "Across 5 sessions you'll read Andy and Red's actual dialogue, discover how "
            "two men use the simplest words to talk about the biggest ideas — hope, freedom, "
            "fear, and the courage to start over.\n\n"
            "Tap the link below to watch the original scene — after this course, "
            "you'll hear Red's voice and understand every word as if he were talking to you."
        )
    }

    content["contentTypeTags"] = ["movie"]
    content["is_public"] = False

    # ── Session 0: Group 1 — beard, marbles, pacific, memory, worthless, charter ──
    s0 = content["learningSessions"][0]
    s0["title"] = "Session 1: The Dream of Zihuatanejo"

    # Activity 0: introAudio — scene intro
    s0["activities"][0]["title"] = "Introduction to the Film Scene"
    s0["activities"][0]["description"] = "Setting the stage for Andy's dream of freedom in The Shawshank Redemption"
    s0["activities"][0]["data"]["text"] = (
        "Welcome to the vocabulary-through-cinema course! Today we begin with one of "
        "the most beloved films ever made — 'The Shawshank Redemption.' Released in 1994 "
        "and based on a Stephen King novella, this film tells the story of Andy Dufresne, "
        "a banker wrongly convicted of murder, and Red, a long-time inmate who becomes "
        "his closest friend. Despite its modest box-office debut, the film has become "
        "the highest-rated movie on IMDb — a testament to its enduring power.\n\n"
        "The scene we're exploring is one of the most emotionally charged in cinema. "
        "Andy sits with Red in the prison yard and describes his dream — a little hotel "
        "on a beach in Zihuatanejo, Mexico, where the Pacific Ocean is as blue as it is "
        "in his dreams. Red listens, skeptical, afraid to hope. Andy talks about growing "
        "a beard, fixing up an old boat, and living a life with no memory of prison walls. "
        "It's a conversation about two very different ways of surviving — one through hope, "
        "the other through acceptance.\n\n"
        "In this first session, you'll learn 6 vocabulary words that appear in this dialogue: "
        "beard, marbles, pacific, memory, worthless, and charter. Each word carries the weight "
        "of Andy's dream and Red's doubt — and by the end of this session, you'll hear them "
        "not as dictionary entries, but as pieces of a conversation about what it means to be free."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s0["activities"][1]["title"] = "Vocabulary Introduction: Session 1"
    s0["activities"][1]["description"] = "Learn 6 words: beard, marbles, pacific, memory, worthless, charter"
    s0["activities"][1]["data"]["text"] = (
        "Let's dive into the first 6 vocabulary words from the prison-yard scene in "
        "'The Shawshank Redemption.' Each word comes straight from Andy and Red's dialogue, "
        "and understanding how they use them will change the way you hear everyday English.\n\n"

        "The first word is 'beard.' It's a noun — hair that grows on a man's chin and cheeks. "
        "Andy tells Red about his dream of life after prison: he wants to grow a beard, "
        "live on a beach, and never look back. In the film, the beard isn't just facial hair — "
        "it's a symbol of transformation. Inside Shawshank, inmates are clean-shaven, controlled, "
        "uniform. A beard means freedom, individuality, a new identity. 'Beard' can also be used "
        "as a verb in informal English: 'to beard someone' means to confront them boldly, though "
        "this usage is rare. Common collocations: 'grow a beard,' 'trim a beard,' 'a full beard.' "
        "Example: After retiring, he grew a thick beard and barely recognized himself in the mirror.\n\n"

        "The second word is 'marbles.' It's a plural noun — small glass balls used in children's "
        "games. But in the film, Red uses the idiom 'lose your marbles,' which means to go crazy "
        "or lose your mind. When Andy talks about his dream of Zihuatanejo, Red thinks he's lost "
        "his marbles — that hope is a dangerous thing inside prison walls. This idiom is very common "
        "in casual English: 'Have you lost your marbles?' 'She's got all her marbles' (she's still "
        "sharp-minded). The origin likely comes from the idea that marbles represent your wits — "
        "lose them and you've lost your sanity. "
        "Example: My grandmother is ninety-two and still has all her marbles — sharp as a tack.\n\n"

        "The third word is 'pacific.' It's an adjective meaning 'peaceful, calm' — from the Latin "
        "'pacificus.' But in the film, it refers to the Pacific Ocean — the vast body of water "
        "that represents Andy's ultimate freedom. Zihuatanejo sits on the Pacific coast of Mexico, "
        "and for Andy, the Pacific is everything Shawshank is not: open, boundless, beautiful. "
        "The word 'pacific' (lowercase) means 'peaceful': 'a pacific temperament.' "
        "'Pacific' (capitalized) is the ocean. 'Pacify' is the verb form: 'to pacify a crowd.' "
        "Example: The pacific waters of the bay reflected the sunset like a sheet of molten gold.\n\n"

        "The fourth word is 'memory.' It's a noun meaning 'the faculty by which the mind stores "
        "and remembers information,' or 'a recollection of a past event.' Andy dreams of a place "
        "with 'no memory' — a place where the past doesn't follow you, where you can start fresh "
        "without the weight of what happened before. 'Memory' is both the ability to remember "
        "('She has an excellent memory') and a specific recollection ('a childhood memory'). "
        "Common phrases: 'in memory of' (as a tribute), 'from memory' (without notes), "
        "'memory lane' (nostalgic revisiting of the past). "
        "Example: The smell of fresh bread always brings back memories of my grandmother's kitchen.\n\n"

        "The fifth word is 'worthless.' It's an adjective meaning 'having no value or use.' "
        "In the film, Andy describes a rock hammer as 'worthless' — too small to be a weapon, "
        "too insignificant to attract attention. But that 'worthless' little tool becomes the "
        "instrument of his escape. The word carries dramatic irony: what seems worthless turns out "
        "to be priceless. 'Worthless' is the opposite of 'valuable.' Related words: 'worth' (noun/adjective), "
        "'worthy' (deserving), 'worthwhile' (worth the time and effort). "
        "Example: The painting looked worthless, but an art dealer recognized it as a lost masterpiece.\n\n"

        "The sixth word is 'charter.' It can be a noun or a verb. As a noun, it means 'a written "
        "grant of rights' or 'the hiring of a vehicle (especially a boat or plane) for private use.' "
        "Andy dreams of chartering a fishing boat in Zihuatanejo — taking tourists out on the Pacific "
        "for deep-sea fishing. 'Charter a boat,' 'charter a flight,' 'a charter school' (a school "
        "operating under a special charter). As a verb: 'We chartered a yacht for the weekend.' "
        "Example: They chartered a small plane to reach the remote island before sunset.\n\n"

        "So there you have it — your first 6 words: beard, marbles, pacific, memory, worthless, "
        "and charter. Each one is woven into Andy's dream of freedom. Let's practice them now!"
    )

    # Activities 2-6: flashcards/vocab — update titles and descriptions
    s0["activities"][2]["title"] = "Flashcards: The Dream of Zihuatanejo"
    s0["activities"][2]["description"] = "Learn 6 words: beard, marbles, pacific, memory, worthless, charter"

    s0["activities"][3]["title"] = "Flashcards: Speak Session 1 Vocabulary"
    s0["activities"][3]["description"] = "Practice saying 6 words: beard, marbles, pacific, memory, worthless, charter"

    s0["activities"][4]["title"] = "Flashcards: Recognize Session 1 Vocabulary"
    s0["activities"][4]["description"] = "Recognize 6 words: beard, marbles, pacific, memory, worthless, charter"

    s0["activities"][5]["title"] = "Flashcards: Recall Session 1 Vocabulary"
    s0["activities"][5]["description"] = "Recall 6 words: beard, marbles, pacific, memory, worthless, charter"

    s0["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 1"
    s0["activities"][6]["description"] = "Master 6 words: beard, marbles, pacific, memory, worthless, charter"

    # Activity 7: introAudio — grammar/usage
    s0["activities"][7]["title"] = "Grammar and Usage: Session 1"
    s0["activities"][7]["description"] = "How to use Session 1 vocabulary naturally in sentences"
    s0["activities"][7]["data"]["text"] = (
        "Great work! You've met your first 6 words. Now let's look at how they work "
        "in real English sentences, using The Shawshank Redemption's dialogue as our guide.\n\n"
        "'Beard' is a countable noun: 'a beard,' 'beards.' Common collocations: 'grow a beard,' "
        "'shave off a beard,' 'a bushy beard,' 'a neatly trimmed beard.' The adjective 'bearded' "
        "describes someone who has a beard: 'a bearded man.' In Andy's case, growing a beard "
        "symbolizes shedding his prison identity — it's the first thing he'll do as a free man.\n\n"
        "'Marbles' in the literal sense is always plural when referring to the game: 'play marbles.' "
        "A single marble is 'a marble.' The idiom 'lose your marbles' is informal and humorous — "
        "use it in casual conversation, not formal writing. 'Marble' (uncountable) also refers to "
        "the stone: 'a marble floor,' 'a marble statue.' Context makes the meaning clear.\n\n"
        "'Pacific' as a proper noun (the Pacific Ocean) is always capitalized. As an adjective "
        "meaning 'peaceful,' it's lowercase: 'a pacific resolution to the conflict.' "
        "The related noun is 'pacifism' (opposition to war) and 'pacifist' (a person who opposes war). "
        "Andy's use of 'Pacific' is both literal and symbolic — the ocean represents peace.\n\n"
        "'Memory' is countable when referring to specific recollections: 'happy memories,' "
        "'a vivid memory.' It's uncountable when referring to the faculty: 'She has a good memory.' "
        "'Memorize' is the verb: 'memorize a poem.' 'Memorial' is a noun: 'a war memorial.' "
        "Andy's dream of 'no memory' means a place where the past can't reach you.\n\n"
        "'Worthless' is an absolute adjective — something is either worthless or it isn't. "
        "You wouldn't normally say 'more worthless' (though people do informally). "
        "The irony in the film is deliberate: the 'worthless' rock hammer is the most valuable "
        "object in the entire story. 'Worth' + amount: 'worth ten dollars,' 'worth the effort.'\n\n"
        "'Charter' as a verb takes a direct object: 'charter a boat,' 'charter a bus.' "
        "As a noun, it can mean a document ('the UN Charter') or a hired vehicle ('a charter flight'). "
        "'Chartered' as an adjective: 'a chartered accountant' (British English for a certified professional). "
        "Andy's dream of chartering a boat is the most concrete detail of his freedom plan."
    )

    # Activity 8: reading — keep text as-is (already English), update title/description
    s0["activities"][8]["title"] = "Read: The Shawshank Redemption Excerpt (Part 1)"
    s0["activities"][8]["description"] = "Read the prison-yard dialogue about Andy's dream of Zihuatanejo"

    # Activity 9: speakReading
    s0["activities"][9]["title"] = "Speak: Practice the Dialogue (Part 1)"
    s0["activities"][9]["description"] = "Practice speaking the prison-yard dialogue aloud"

    # Activity 10: readAlong
    s0["activities"][10]["title"] = "Listen: The Shawshank Redemption Excerpt (Part 1)"
    s0["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s0["activities"][11]["title"] = "Write: Hope and Dreams"
    s0["activities"][11]["description"] = "Write sentences using Session 1 vocabulary"
    ws_items_0 = s0["activities"][11]["data"]["items"]
    ws_items_0[0]["prompt"] = (
        "Use the word 'beard' to write about transformation or a new beginning — "
        "just as Andy imagines growing a beard as the first act of his free life. "
        "Example: After leaving the corporate world, he grew a beard and moved to a cabin "
        "in the mountains where nobody knew his name."
    )
    ws_items_0[1]["prompt"] = (
        "Use the word 'marbles' literally or in the idiom 'lose your marbles' — "
        "like Red thinking Andy has gone crazy for daring to hope. "
        "Example: My coworkers thought I'd lost my marbles when I quit my stable job "
        "to open a bookshop in a tiny coastal town."
    )
    ws_items_0[2]["prompt"] = (
        "Use the word 'pacific' to describe something peaceful or to reference the ocean — "
        "the way Andy describes the Pacific as the embodiment of freedom. "
        "Example: The pacific blue of the ocean stretched endlessly before them, "
        "erasing every worry they had carried from the mainland."
    )
    ws_items_0[3]["prompt"] = (
        "Use the word 'memory' to write about the past or starting fresh — "
        "like Andy dreaming of a place with no memory of prison walls. "
        "Example: She moved to a city where she had no memory attached to any street corner, "
        "and for the first time in years, she felt light."
    )
    ws_items_0[4]["prompt"] = (
        "Use the word 'worthless' to describe something that appears valueless but isn't — "
        "like the rock hammer that everyone dismissed but Andy used to carve his freedom. "
        "Example: The old notebook looked worthless, but inside it held the only copy "
        "of a song that would change her life."
    )
    ws_items_0[5]["prompt"] = (
        "Use the word 'charter' to write about hiring a vehicle or embarking on an adventure — "
        "like Andy's dream of chartering a fishing boat on the Pacific coast. "
        "Example: They chartered a sailboat for the afternoon and spent hours drifting "
        "along the coastline, watching dolphins leap through the waves."
    )

    # ── Session 1: Group 2 — institutional, underestimate, scare, begin, outside, ocean ──
    s1 = content["learningSessions"][1]
    s1["title"] = "Session 2: Red's Fear — An Institutional Man"

    # Activity 0: introAudio — session intro
    s1["activities"][0]["title"] = "Introduction to Session 2"
    s1["activities"][0]["description"] = "Recap Session 1 and introduce the theme of fear and institutionalization"
    s1["activities"][0]["data"]["text"] = (
        "Welcome back to Session 2! In our first session, you learned 6 words from the "
        "prison-yard scene: beard, marbles, pacific, memory, worthless, and charter. "
        "You discovered how Andy uses these simple words to paint a vivid picture of freedom — "
        "a beard he'll grow, a boat he'll charter, an ocean that has no memory of his suffering.\n\n"
        "Now we shift perspective. This session belongs to Red — the narrator, the realist, "
        "the man who has spent forty years inside Shawshank and can't imagine life beyond its walls. "
        "Red is what the film calls an 'institutional man' — someone so shaped by the system "
        "that the system has become his identity. He's terrified of the outside world. "
        "He underestimates his own ability to survive beyond the prison gates. "
        "And when Andy talks about hope, Red pushes back — because hope, to Red, is the most "
        "dangerous thing of all.\n\n"
        "Today you'll learn 6 new words: institutional, underestimate, scare, begin, outside, "
        "and ocean. These words carry the weight of Red's fear — and by the end of this session, "
        "you'll understand why freedom can be more terrifying than captivity."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s1["activities"][1]["title"] = "Vocabulary Introduction: Session 2"
    s1["activities"][1]["description"] = "Learn 6 words: institutional, underestimate, scare, begin, outside, ocean"
    s1["activities"][1]["data"]["text"] = (
        "Let's learn 6 new vocabulary words from the next part of The Shawshank Redemption — "
        "the scenes where Red confronts his deepest fears about life beyond prison.\n\n"

        "The first word is 'institutional.' It's an adjective meaning 'relating to or typical of "
        "an institution,' but in this film it takes on a devastating meaning. Red says: 'I'm an "
        "institutional man now.' He means that prison has become his entire world — he can't function "
        "without its routines, its rules, its walls. 'Institutional' can describe buildings "
        "('institutional architecture' — bland, uniform), food ('institutional meals' — mass-produced), "
        "or people ('institutionalized' — dependent on the system). The verb is 'institutionalize': "
        "'He was institutionalized after years in the system.' "
        "Example: After twenty years in the military, he found civilian life disorienting — "
        "he had become an institutional man without realizing it.\n\n"

        "The second word is 'underestimate.' It's a verb meaning 'to estimate something as less "
        "than its actual value, size, or importance.' Throughout the film, everyone underestimates "
        "Andy — the warden, the guards, even Red. They see a quiet banker, not a man capable of "
        "tunneling through a concrete wall with a rock hammer over nineteen years. "
        "'Underestimate' is the opposite of 'overestimate.' 'Never underestimate' is a common "
        "warning phrase: 'Never underestimate the power of kindness.' The noun form is 'underestimation.' "
        "Example: She underestimated how long the project would take and ended up working through the weekend.\n\n"

        "The third word is 'scare.' It can be a verb ('to frighten') or a noun ('a sudden fright'). "
        "Red is scared — not of prison, but of freedom. The outside world scares him because "
        "he doesn't know how to live in it anymore. 'Scare' is less formal than 'frighten' and "
        "more common in everyday speech. 'Scared' (adjective): 'I'm scared of heights.' "
        "'Scary' (adjective): 'a scary movie.' 'Scare' (noun): 'You gave me a scare!' "
        "Example: The thought of starting over in a new country scared her more than she wanted to admit.\n\n"

        "The fourth word is 'begin.' It's a verb meaning 'to start.' Red says he wouldn't know "
        "where to begin if he were released — the world has changed so much that the very act "
        "of starting feels impossible. 'Begin' is slightly more formal than 'start' but they're "
        "largely interchangeable. Irregular forms: begin, began, begun. 'Begin with' introduces "
        "the first item: 'Let's begin with the basics.' 'To begin with' means 'firstly.' "
        "Example: She didn't know where to begin, so she just picked up a pen and started writing.\n\n"

        "The fifth word is 'outside.' It can be a noun, adjective, adverb, or preposition — "
        "one of the most versatile words in English. In the film, 'outside' means the world "
        "beyond prison walls — a world Red hasn't seen in forty years. 'The outside world,' "
        "'on the outside' (in freedom), 'outside of work' (apart from work). "
        "For Red, 'outside' isn't just a direction — it's an entirely foreign country. "
        "Example: He pressed his face against the window, watching the outside world go by "
        "like a movie he wasn't part of.\n\n"

        "The sixth word is 'ocean.' It's a noun — a vast body of salt water. In the film, "
        "the ocean represents everything prison is not: open, limitless, alive. Andy dreams "
        "of the Pacific Ocean the way a drowning man dreams of air. Red fears it — because "
        "the ocean is too big, too free, too much for a man who has lived in a cell for decades. "
        "'Ocean' collocations: 'ocean view,' 'ocean breeze,' 'an ocean of possibilities.' "
        "The phrase 'a drop in the ocean' means something insignificantly small. "
        "Example: Standing at the edge of the cliff, she looked out at the ocean and felt "
        "both terrified and completely alive.\n\n"

        "Your 6 new words: institutional, underestimate, scare, begin, outside, ocean. "
        "Combined with Session 1, you now have 12 words from The Shawshank Redemption. "
        "Let's put them to work!"
    )

    # Activities 2-6: flashcards/vocab
    s1["activities"][2]["title"] = "Flashcards: Fear and Doubt"
    s1["activities"][2]["description"] = "Learn 6 words: institutional, underestimate, scare, begin, outside, ocean"

    s1["activities"][3]["title"] = "Flashcards: Speak Session 2 Vocabulary"
    s1["activities"][3]["description"] = "Practice saying 6 words: institutional, underestimate, scare, begin, outside, ocean"

    s1["activities"][4]["title"] = "Flashcards: Recognize Session 2 Vocabulary"
    s1["activities"][4]["description"] = "Recognize 6 words: institutional, underestimate, scare, begin, outside, ocean"

    s1["activities"][5]["title"] = "Flashcards: Recall Session 2 Vocabulary"
    s1["activities"][5]["description"] = "Recall 6 words: institutional, underestimate, scare, begin, outside, ocean"

    s1["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 2"
    s1["activities"][6]["description"] = "Master 6 words: institutional, underestimate, scare, begin, outside, ocean"

    # Activity 7: introAudio — grammar/usage
    s1["activities"][7]["title"] = "Grammar and Usage: Session 2"
    s1["activities"][7]["description"] = "How to use Session 2 vocabulary naturally in sentences"
    s1["activities"][7]["data"]["text"] = (
        "Excellent! Let's explore how these 6 words behave in real English.\n\n"
        "'Institutional' is a long adjective (5 syllables: in-sti-TU-tion-al) derived from "
        "'institution.' The verb 'institutionalize' means to place someone in an institution "
        "or to make something an established practice. 'Institutionalized' as an adjective "
        "describes someone who has become dependent on institutional life — exactly what Red means. "
        "In business: 'institutional investors' (large organizations that invest money).\n\n"
        "'Underestimate' is a compound verb: 'under' + 'estimate.' The prefix 'under-' means "
        "'less than' or 'below.' Compare: 'undervalue,' 'underperform,' 'underrate.' "
        "The opposite is 'overestimate.' 'Don't underestimate' is a common warning that implies "
        "hidden strength or complexity: 'Don't underestimate the difficulty of learning a language.'\n\n"
        "'Scare' has several useful forms. 'Scared' (adjective — feeling fear): 'I'm scared.' "
        "'Scary' (adjective — causing fear): 'That was scary.' 'Scare' (noun): 'a health scare.' "
        "'Scarecrow' (a figure in a field to scare birds). 'Scare away/off' (phrasal verb): "
        "'The noise scared the birds away.' Red's fear isn't of danger — it's of the unknown.\n\n"
        "'Begin' is slightly more formal than 'start' and often used in written English. "
        "Irregular conjugation: begin, began, begun. 'Beginning' (noun): 'a new beginning.' "
        "'Beginner' (noun): 'a beginner's course.' The phrase 'to begin with' means 'firstly' "
        "or 'at the start': 'To begin with, I didn't like the idea.'\n\n"
        "'Outside' is remarkably flexible. Adverb: 'Let's go outside.' Preposition: 'outside the door.' "
        "Noun: 'the outside of the building.' Adjective: 'an outside chance' (a slim possibility). "
        "'Outside of' (preposition, informal): 'Outside of work, she paints.' "
        "For Red, 'the outside' is a proper noun — it's a place, a concept, a fear.\n\n"
        "'Ocean' is usually preceded by 'the': 'the Atlantic Ocean,' 'the ocean.' "
        "Without 'the,' it's used in compounds: 'ocean floor,' 'ocean current,' 'oceanfront.' "
        "'Oceanic' is the adjective form: 'oceanic climate.' The metaphorical use is powerful: "
        "'an ocean of grief,' 'oceans apart.' Andy's ocean is both literal and metaphorical — "
        "it's the Pacific, and it's freedom itself."
    )

    # Activity 8-10: reading/speak/listen — keep text, update titles
    s1["activities"][8]["title"] = "Read: The Shawshank Redemption Excerpt (Part 2)"
    s1["activities"][8]["description"] = "Read the dialogue about Red's fear of the outside world"

    s1["activities"][9]["title"] = "Speak: Practice the Dialogue (Part 2)"
    s1["activities"][9]["description"] = "Practice speaking Red's monologue about institutionalization aloud"

    s1["activities"][10]["title"] = "Listen: The Shawshank Redemption Excerpt (Part 2)"
    s1["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s1["activities"][11]["title"] = "Write: Fear and Change"
    s1["activities"][11]["description"] = "Write sentences using Session 2 vocabulary"
    ws_items_1 = s1["activities"][11]["data"]["items"]
    ws_items_1[0]["prompt"] = (
        "Use the word 'institutional' to describe dependence on a system or routine — "
        "like Red saying he's become an institutional man who can't function without prison. "
        "Example: After decades in the same company, he realized he had become institutional — "
        "unable to imagine a life without the morning commute and the corner office."
    )
    ws_items_1[1]["prompt"] = (
        "Use the word 'underestimate' to write about hidden potential or misjudgment — "
        "like everyone underestimating Andy's quiet determination. "
        "Example: Never underestimate a person who has nothing left to lose — "
        "they are capable of things that would astonish you."
    )
    ws_items_1[2]["prompt"] = (
        "Use the word 'scare' to describe fear of the unknown or change — "
        "like Red being scared of the world beyond prison walls. "
        "Example: The idea of moving to a country where she didn't speak the language "
        "scared her, but she bought the plane ticket anyway."
    )
    ws_items_1[3]["prompt"] = (
        "Use the word 'begin' to write about starting something new — "
        "like Red saying he wouldn't know where to begin in the outside world. "
        "Example: The hardest part of any journey is deciding to begin — "
        "once you take the first step, the path reveals itself."
    )
    ws_items_1[4]["prompt"] = (
        "Use the word 'outside' to describe the world beyond a comfort zone — "
        "like Red's terror of the outside world after forty years behind bars. "
        "Example: Everything she wanted was waiting outside the walls she had built "
        "around herself — she just had to find the courage to step through."
    )
    ws_items_1[5]["prompt"] = (
        "Use the word 'ocean' to write about vastness, freedom, or possibility — "
        "like the Pacific Ocean representing everything Andy dreams of. "
        "Example: Standing at the shore, she realized the ocean didn't care about her problems — "
        "and somehow, that was the most comforting thought in the world."
    )

    # ── Session 2: Group 3 — mistakes, paid, pipe, choice, busy, dying ──
    s2 = content["learningSessions"][2]
    s2["title"] = "Session 3: Get Busy Living or Get Busy Dying"

    # Activity 0: introAudio — session intro
    s2["activities"][0]["title"] = "Introduction to Session 3"
    s2["activities"][0]["description"] = "Recap Sessions 1-2 and introduce the themes of choice and redemption"
    s2["activities"][0]["data"]["text"] = (
        "Welcome to Session 3 — the final learning session before your review! "
        "So far you've learned 12 words from The Shawshank Redemption. In Session 1, you met "
        "beard, marbles, pacific, memory, worthless, and charter — the words of Andy's dream, "
        "where a quiet banker describes a life of freedom on a Mexican beach. "
        "In Session 2, you learned institutional, underestimate, scare, begin, outside, and ocean — "
        "the words of Red's fear, where a man who has spent forty years in prison admits "
        "he's terrified of the world beyond the walls.\n\n"
        "Now we reach the climax. Andy delivers the most famous line in the film: "
        "'Get busy living or get busy dying.' It's a line about choice — the ultimate choice. "
        "You can accept the life you've been given, or you can fight for the life you want. "
        "Andy has made his choice. Now it's Red's turn.\n\n"
        "Your final 6 words: mistakes, paid, pipe, choice, busy, and dying. "
        "By the end of this session, you'll have all 18 vocabulary words — and you'll understand "
        "why this film has moved millions of people to tears."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s2["activities"][1]["title"] = "Vocabulary Introduction: Session 3"
    s2["activities"][1]["description"] = "Learn 6 words: mistakes, paid, pipe, choice, busy, dying"
    s2["activities"][1]["data"]["text"] = (
        "Here are your final 6 vocabulary words, drawn from the most pivotal scenes "
        "in The Shawshank Redemption.\n\n"

        "The first word is 'mistakes.' It's the plural of 'mistake' — an error in action, "
        "judgment, or belief. Andy tells Red: 'I made mistakes.' It's one of the most honest "
        "moments in the film — a man who was wrongly convicted of murder admitting that he still "
        "made real mistakes in his life. He didn't kill his wife, but he drove her away. "
        "'Mistake' as a verb means 'to misidentify': 'I mistook him for his brother.' "
        "'By mistake' means accidentally: 'I took your coat by mistake.' "
        "'Make a mistake' is the standard collocation — never 'do a mistake.' "
        "Example: The biggest mistake I ever made was assuming I had unlimited time to fix things.\n\n"

        "The second word is 'paid.' It's the past tense and past participle of 'pay.' "
        "Andy says he has 'paid' for his mistakes — not with money, but with nineteen years "
        "of his life inside Shawshank. 'Pay' has many meanings beyond money: 'pay attention,' "
        "'pay a visit,' 'pay the price,' 'pay your dues.' 'Paid' is the only correct past form — "
        "'payed' is only used in nautical contexts (paying out rope). "
        "'Well-paid' means earning a good salary. 'Paid off' means something was worth the effort: "
        "'All that hard work finally paid off.' "
        "Example: She paid for her reckless decision with three years of rebuilding trust.\n\n"

        "The third word is 'pipe.' It's a noun — a tube for conveying water, gas, or other fluids. "
        "But in the film, 'pipe' appears in the compound 'pipe dream' — an unattainable or fanciful "
        "hope. Red calls Andy's plan a 'pipe dream,' meaning it's a fantasy that will never come true. "
        "The phrase comes from the hallucinations caused by smoking opium pipes in the 19th century. "
        "'Pipe' also refers to a smoking pipe, a musical pipe, or plumbing pipes. "
        "'Pipeline' means a channel for delivery: 'a pipeline of talent.' "
        "Example: Everyone said opening a restaurant was a pipe dream, but she proved them all wrong.\n\n"

        "The fourth word is 'choice.' It's a noun meaning 'an act of selecting between alternatives.' "
        "The entire film builds to a single choice: get busy living or get busy dying. "
        "Andy chooses to live — to crawl through a sewage pipe, to emerge into the rain, "
        "to drive to Mexico and never look back. 'Choice' collocations: 'make a choice,' "
        "'have no choice,' 'the right choice,' 'a tough choice,' 'by choice' (voluntarily). "
        "The adjective 'choice' means 'of very good quality': 'choice cuts of meat.' "
        "Example: Every morning you wake up with a choice — to let yesterday define you "
        "or to start writing a new story.\n\n"

        "The fifth word is 'busy.' It's an adjective meaning 'actively engaged in work or activity.' "
        "Andy's line — 'Get busy living or get busy dying' — uses 'busy' in its most active sense. "
        "'Get busy' means 'start working hard at something.' It's a call to action, not a description "
        "of a schedule. 'Busy' can describe people ('I'm busy'), places ('a busy street'), "
        "or patterns ('a busy design'). 'Busy yourself with' means to occupy yourself: "
        "'She busied herself with gardening.' "
        "Example: Instead of worrying about what might go wrong, she got busy making things go right.\n\n"

        "The sixth and final word is 'dying.' It's the present participle of 'die,' used as "
        "an adjective or part of a continuous tense. In Andy's famous line, 'dying' is the opposite "
        "of 'living' — it's not physical death, but the slow death of giving up, of accepting "
        "a life you didn't choose, of letting the walls close in. 'Dying' can be literal: "
        "'The plant is dying.' Or figurative: 'I'm dying to know,' 'a dying art,' 'dying wish.' "
        "The contrast between 'living' and 'dying' in Andy's line is the moral center of the film. "
        "Example: He realized he had been dying slowly for years — not from illness, "
        "but from the absence of anything worth living for.\n\n"

        "And there you have it — all 18 words: beard, marbles, pacific, memory, worthless, charter, "
        "institutional, underestimate, scare, begin, outside, ocean, mistakes, paid, pipe, choice, "
        "busy, and dying. You now have the complete vocabulary of The Shawshank Redemption. "
        "Let's practice these final 6!"
    )

    # Activities 2-6: flashcards/vocab
    s2["activities"][2]["title"] = "Flashcards: Determination and Choice"
    s2["activities"][2]["description"] = "Learn 6 words: mistakes, paid, pipe, choice, busy, dying"

    s2["activities"][3]["title"] = "Flashcards: Speak Session 3 Vocabulary"
    s2["activities"][3]["description"] = "Practice saying 6 words: mistakes, paid, pipe, choice, busy, dying"

    s2["activities"][4]["title"] = "Flashcards: Recognize Session 3 Vocabulary"
    s2["activities"][4]["description"] = "Recognize 6 words: mistakes, paid, pipe, choice, busy, dying"

    s2["activities"][5]["title"] = "Flashcards: Recall Session 3 Vocabulary"
    s2["activities"][5]["description"] = "Recall 6 words: mistakes, paid, pipe, choice, busy, dying"

    s2["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 3"
    s2["activities"][6]["description"] = "Master 6 words: mistakes, paid, pipe, choice, busy, dying"

    # Activity 7: introAudio — grammar/usage
    s2["activities"][7]["title"] = "Grammar and Usage: Session 3"
    s2["activities"][7]["description"] = "How to use Session 3 vocabulary naturally in sentences"
    s2["activities"][7]["data"]["text"] = (
        "Let's look at how these final 6 words work in English grammar.\n\n"
        "'Mistakes' — 'make a mistake' is the standard collocation. Never 'do a mistake.' "
        "'Mistake' as a verb: 'I mistook her for someone else.' 'Mistaken' (adjective): "
        "'You're mistaken' (you're wrong). 'Mistakenly' (adverb): 'I mistakenly deleted the file.' "
        "Andy's admission of mistakes is powerful because it separates guilt from innocence — "
        "he's innocent of murder but not innocent of being a bad husband.\n\n"
        "'Paid' — irregular past tense of 'pay.' Common phrases: 'paid in full,' 'paid leave,' "
        "'paid off' (was worth it), 'paid the price' (suffered consequences). "
        "'Underpaid' means not earning enough. 'Overpaid' means earning too much. "
        "Andy has 'paid' in the most literal sense — with years of his life.\n\n"
        "'Pipe' — as a physical object: 'water pipe,' 'smoking pipe,' 'pipe organ.' "
        "As part of 'pipe dream': an unrealistic fantasy. 'Pipeline' is used in business "
        "and technology: 'a sales pipeline,' 'a data pipeline.' "
        "The verb 'pipe down' means 'be quiet': 'Pipe down, everyone!'\n\n"
        "'Choice' — 'make a choice,' 'have a choice,' 'no choice,' 'the choice is yours.' "
        "'Choose' is the verb (choose, chose, chosen). 'Choosy' means picky. "
        "Andy's line frames life as a binary choice — there is no middle ground.\n\n"
        "'Busy' — 'busy with' (occupied by): 'I'm busy with work.' "
        "'Busy doing' (engaged in): 'She's busy cooking.' 'Get busy' (start working): "
        "'Let's get busy.' 'Busybody' (a nosy person). The comparative is 'busier,' "
        "superlative 'busiest.' Andy's use of 'busy' transforms it from mundane to existential.\n\n"
        "'Dying' — present participle of 'die' (die, died, died, dying). "
        "'Dying' as adjective: 'a dying wish,' 'a dying breed.' "
        "Figurative: 'dying to know,' 'dying of laughter,' 'dying of boredom.' "
        "In Andy's line, 'dying' means choosing to waste your life — "
        "the slow death of surrender."
    )

    # Activity 8-10: reading/speak/listen
    s2["activities"][8]["title"] = "Read: The Shawshank Redemption Excerpt (Part 3)"
    s2["activities"][8]["description"] = "Read the dialogue about choice, redemption, and getting busy living"

    s2["activities"][9]["title"] = "Speak: Practice the Dialogue (Part 3)"
    s2["activities"][9]["description"] = "Practice speaking the final dialogue excerpt aloud"

    s2["activities"][10]["title"] = "Listen: The Shawshank Redemption Excerpt (Part 3)"
    s2["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s2["activities"][11]["title"] = "Write: Determination and Living"
    s2["activities"][11]["description"] = "Write sentences using Session 3 vocabulary"
    ws_items_2 = s2["activities"][11]["data"]["items"]
    ws_items_2[0]["prompt"] = (
        "Use the word 'mistakes' to write about errors and the lessons they carry — "
        "like Andy admitting he made mistakes even though he was innocent of the crime. "
        "Example: The mistakes I made in my twenties taught me more than any degree ever could."
    )
    ws_items_2[1]["prompt"] = (
        "Use the word 'paid' to describe a price someone has paid — not necessarily in money — "
        "like Andy saying he has paid for his mistakes with nineteen years of his life. "
        "Example: She paid for her honesty with a lost friendship, but she never regretted telling the truth."
    )
    ws_items_2[2]["prompt"] = (
        "Use the word 'pipe' in the phrase 'pipe dream' to describe an ambitious goal "
        "that others dismiss — like Red calling Andy's escape plan a pipe dream. "
        "Example: They called her idea of building a school in the village a pipe dream, "
        "but three years later, the first students walked through its doors."
    )
    ws_items_2[3]["prompt"] = (
        "Use the word 'choice' to write about a defining decision — "
        "like Andy's ultimate choice to get busy living instead of getting busy dying. "
        "Example: The choice to forgive wasn't easy, but it was the only one that set her free."
    )
    ws_items_2[4]["prompt"] = (
        "Use the word 'busy' in the sense of actively engaged or purposeful — "
        "like Andy's call to action: 'Get busy living or get busy dying.' "
        "Example: Instead of mourning what she had lost, she got busy building something new."
    )
    ws_items_2[5]["prompt"] = (
        "Use the word 'dying' literally or figuratively — "
        "like the film's contrast between dying slowly in prison and choosing to truly live. "
        "Example: The dying embers of the campfire mirrored the fading light in the sky, "
        "and for a moment, everything was perfectly still."
    )

    # ── Session 3: Review (4 activities) ──
    s3 = content["learningSessions"][3]
    s3["title"] = "Review"

    s3["activities"][0]["title"] = "Congratulations and Review"
    s3["activities"][0]["description"] = "Celebrate your progress and prepare for the full review"
    s3["activities"][0]["data"]["text"] = (
        "Congratulations! You've learned all 18 vocabulary words from The Shawshank Redemption. "
        "Let's take a moment to look back at what you've accomplished.\n\n"
        "In Session 1, you learned beard, marbles, pacific, memory, worthless, and charter — "
        "the words of Andy's dream, where a man who has spent nineteen years in prison "
        "describes a life of freedom on the Pacific coast of Mexico — growing a beard, "
        "chartering a fishing boat, and living in a place with no memory of suffering.\n\n"
        "In Session 2, you learned institutional, underestimate, scare, begin, outside, and ocean — "
        "the words of Red's fear, where a man who has been institutionalized for forty years "
        "admits he's scared of the outside world and doesn't know where to begin.\n\n"
        "In Session 3, you learned mistakes, paid, pipe, choice, busy, and dying — "
        "the words of the film's climax, where Andy delivers the line that defines the entire story: "
        "'Get busy living or get busy dying.' A choice between surrender and freedom, "
        "between a pipe dream and a plan, between paying for your mistakes forever "
        "and choosing to start again.\n\n"
        "Now it's time to review all 18 words together. This review session will test your "
        "recognition and recall across all three groups. After this, you'll be ready to read "
        "the complete dialogue in the final session. Let's go!"
    )

    s3["activities"][1]["title"] = "Flashcards: Review All 18 Words"
    s3["activities"][1]["description"] = "Review all 18 vocabulary words from The Shawshank Redemption"

    s3["activities"][2]["title"] = "Flashcards: Recognize All Vocabulary"
    s3["activities"][2]["description"] = "Test your recognition of all 18 words"

    s3["activities"][3]["title"] = "Flashcards: Recall All Vocabulary"
    s3["activities"][3]["description"] = "Test your recall of all 18 words"

    # ── Session 4: Full reading + farewell (5 activities) ──
    s4 = content["learningSessions"][4]
    s4["title"] = "Full Dialogue Reading"

    s4["activities"][0]["title"] = "Introduction to the Complete Reading"
    s4["activities"][0]["description"] = "Prepare for reading the full Shawshank Redemption dialogue"
    s4["activities"][0]["data"]["text"] = (
        "Welcome to the final session! This is the moment everything comes together. "
        "Over the past three sessions, you've built a vocabulary of 18 words drawn directly "
        "from The Shawshank Redemption's dialogue. You've learned their meanings, practiced "
        "their pronunciation, explored their grammar, and used them in your own writing.\n\n"
        "Now you're going to read the complete dialogue — all three excerpts combined into one "
        "continuous passage. As you read, you'll encounter every single one of your 18 words "
        "in context. This time, they won't be new — they'll be familiar friends.\n\n"
        "Here are all 18 words you'll see: beard, marbles, pacific, memory, worthless, charter, "
        "institutional, underestimate, scare, begin, outside, ocean, mistakes, paid, pipe, "
        "choice, busy, and dying.\n\n"
        "Take your time with the reading. Let Andy and Red's voices come through. "
        "And remember — hope is a good thing, maybe the best of things, "
        "and no good thing ever dies."
    )

    s4["activities"][1]["title"] = "Read: Complete Shawshank Redemption Dialogue"
    s4["activities"][1]["description"] = "Read the full dialogue from beginning to end"

    s4["activities"][2]["title"] = "Speak: Practice the Complete Dialogue"
    s4["activities"][2]["description"] = "Practice speaking the entire dialogue aloud"

    s4["activities"][3]["title"] = "Listen: Complete Shawshank Redemption Dialogue"
    s4["activities"][3]["description"] = "Listen to the complete dialogue and follow along"

    s4["activities"][4]["title"] = "Farewell and Vocabulary Review"
    s4["activities"][4]["description"] = "Final review of all 18 words and farewell"
    s4["activities"][4]["data"]["text"] = (
        "You've done it — you've completed the entire Shawshank Redemption vocabulary course! "
        "Let's do one final review of all 18 words before we say goodbye.\n\n"

        "'Beard' — hair on a man's face, and in this film, a symbol of freedom and new identity. "
        "Example: He grew a beard during his sabbatical and decided to keep it as a reminder of who he became.\n\n"
        "'Marbles' — small glass balls, or in the idiom 'lose your marbles,' your sanity. "
        "Example: People said she'd lost her marbles for quitting law school, but she'd never been happier.\n\n"
        "'Pacific' — peaceful, or the vast ocean that represents Andy's dream of freedom. "
        "Example: The pacific surface of the lake at dawn made the whole world feel still.\n\n"
        "'Memory' — the ability to remember, or a specific recollection from the past. "
        "Example: The memory of that conversation stayed with him for the rest of his life.\n\n"
        "'Worthless' — having no value, though in this film, the 'worthless' tool was priceless. "
        "Example: What seemed like a worthless skill turned out to be the one thing that saved the project.\n\n"
        "'Charter' — to hire a vehicle for private use, or a founding document. "
        "Example: They chartered a boat and spent the day fishing off the coast.\n\n"

        "'Institutional' — shaped by or dependent on an institution's routines and rules. "
        "Example: The institutional grey of the hospital walls made everything feel colder.\n\n"
        "'Underestimate' — to judge something as less important or capable than it really is. "
        "Example: Never underestimate someone who has been told their whole life that they can't.\n\n"
        "'Scare' — to frighten, or a sudden feeling of fear. "
        "Example: The first day at a new school can scare even the bravest kid.\n\n"
        "'Begin' — to start, to take the first step. "
        "Example: She didn't know where to begin, so she began with the truth.\n\n"
        "'Outside' — beyond the walls, beyond the comfort zone, beyond the known. "
        "Example: The outside world looked different after two years of working from home.\n\n"
        "'Ocean' — a vast body of water, and a metaphor for limitless possibility. "
        "Example: The ocean doesn't ask permission to be powerful — and neither should you.\n\n"

        "'Mistakes' — errors in judgment or action, and the lessons they carry. "
        "Example: His biggest mistake was waiting too long to say what mattered.\n\n"
        "'Paid' — past tense of pay; to have given something in exchange. "
        "Example: She paid for her independence with years of hard work and sacrifice.\n\n"
        "'Pipe' — a tube, or in 'pipe dream,' an impossible fantasy. "
        "Example: What started as a pipe dream became a thriving business in five years.\n\n"
        "'Choice' — the act of selecting between alternatives. "
        "Example: The choice to leave was the hardest thing he ever did — and the best.\n\n"
        "'Busy' — actively engaged, purposefully occupied. "
        "Example: She got busy living the moment she stopped waiting for permission.\n\n"
        "'Dying' — in the process of death, or desperately eager. "
        "Example: The dying light of the sunset turned the ocean to gold.\n\n"

        "Thank you for learning with The Shawshank Redemption. You came for 18 vocabulary words, "
        "but I hope you're leaving with something more — a reminder that hope is not naive, "
        "that freedom is not given but taken, and that the simplest words can carry "
        "the weight of an entire life.\n\n"
        "Get busy living. Keep reading, keep speaking, keep writing. "
        "And remember — no good thing ever dies. Goodbye, and good luck!"
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
    print(f"Created en-en Shawshank Redemption curriculum: {cid}")
    return cid


if __name__ == "__main__":
    create()
