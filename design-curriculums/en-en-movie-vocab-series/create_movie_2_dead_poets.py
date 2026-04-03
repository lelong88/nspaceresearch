"""
Create en-en movie curriculum #2: Dead Poets Society
Mirror of vi-en source LLy5qjuLk0VZ7SIi — all Vietnamese UI text rewritten in English.

Source movie: Dead Poets Society (1989)
YouTube: https://www.youtube.com/watch?v=vi0Lbjs5ECI

18 vocabulary words in 3 groups of 6 (same as vi-en source):
  Group 1: gather, poet, rosebuds, seize, sentiment, stanza
  Group 2: breathing, limited, peruse, springs, timid, worms
  Group 3: almighty, capable, destined, extraordinary, squander, whisper

All user-facing text in English. Reading passages stay as-is (already English).
Vocabulary words stay as-is (already English).

Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 9.1, 9.2, 9.3, 9.4, 9.5
"""

import sys, json, requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"
SOURCE_ID = "LLy5qjuLk0VZ7SIi"

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
    content["title"] = "'Dead Poets Society' — Carpe Diem, Seize the Day"

    content["description"] = (
        "WHEN WAS THE LAST TIME YOU DID SOMETHING BECAUSE YOU TRULY "
        "WANTED TO — NOT BECAUSE SOMEONE EXPECTED YOU TO?\n\n"
        "Every day you follow a script someone else wrote — the career your parents chose, "
        "the opinions you're afraid to voice, the poem you never dared to read aloud. "
        "John Keating walks into a classroom of obedient boys at Welton Academy, "
        "tears a page out of a textbook, and says two words that change everything: "
        "'Carpe diem.' Seize the day.\n\n"
        "This is a film about the war between conformity and self-expression — "
        "between the safe path and the one that makes your heart pound. "
        "Keating doesn't teach poetry the way it's supposed to be taught. "
        "He stands on desks. He makes his students rip out pages. "
        "He whispers 'Carpe diem' like it's a secret that could save their lives — "
        "because for some of them, it does.\n\n"
        "When you understand that 'rosebuds' in 'Gather ye rosebuds while ye may' "
        "isn't about flowers but about the fleeting nature of youth itself — "
        "you'll start hearing English with completely new ears. "
        "That's the moment cinema becomes your greatest teacher.\n\n"
        "18 vocabulary words drawn directly from the film's dialogue, combined with "
        "a multi-sensory learning method — listening, reading, speaking, writing — "
        "so you sharpen your English while carrying Keating's revolutionary message: "
        "make your lives extraordinary."
    )

    content["preview"] = {
        "text": (
            "Remember the scene where Mr. Keating whispers 'Carpe diem' to a room full "
            "of wide-eyed boys, their faces reflected in a glass case of old photographs — "
            "young men who once had the same dreams and are now 'fertilizing daffodils'?\n\n"
            "18 English vocabulary words you'll learn: gather, poet, rosebuds, seize, "
            "sentiment, stanza, breathing, limited, peruse, springs, timid, worms, "
            "almighty, capable, destined, extraordinary, squander, whisper.\n\n"
            "Across 5 sessions you'll read Keating's actual dialogue, discover how a teacher "
            "uses poetry to crack open the minds of boys trapped by tradition — from the "
            "rosebuds of Robert Herrick to the barbaric yawp of Walt Whitman.\n\n"
            "Tap the link below to watch the original scene — after this course, "
            "you'll hear Keating's voice and understand every word as if he were "
            "speaking directly to you."
        )
    }

    content["contentTypeTags"] = ["movie"]
    content["is_public"] = False

    # ── Session 0: Group 1 — gather, poet, rosebuds, seize, sentiment, stanza ──
    s0 = content["learningSessions"][0]
    s0["title"] = "Session 1: Gather Ye Rosebuds While Ye May"

    # Activity 0: introAudio — scene intro
    s0["activities"][0]["title"] = "Introduction to the Film Scene"
    s0["activities"][0]["description"] = "Setting the stage for the Carpe Diem scene from Dead Poets Society"
    s0["activities"][0]["data"]["text"] = (
        "Welcome to the vocabulary-through-cinema course! Today we begin with one of "
        "the most inspiring classroom scenes ever filmed — the 'Carpe Diem' scene from "
        "'Dead Poets Society.' The 1989 film starring Robin Williams tells the story of "
        "John Keating, an English teacher at the elite Welton Academy, who uses poetry "
        "to awaken his students' passion for life, beauty, and independent thought.\n\n"
        "In this scene, Keating leads his students to a glass trophy case filled with "
        "photographs of former Welton boys — young men who once had the same fire in their eyes, "
        "the same ambitions, the same belief that they were invincible. 'They're not that different "
        "from you, are they?' Keating asks. Then he leans in close and whispers: 'Carpe diem. "
        "Seize the day, boys. Make your lives extraordinary.' It's a moment that has inspired "
        "millions of viewers to question whether they're truly living or merely existing.\n\n"
        "In this first session, you'll learn 6 vocabulary words that appear in Keating's "
        "dialogue: gather, poet, rosebuds, seize, sentiment, and stanza. Each word is "
        "woven into the fabric of the scene, and by the end of this session you'll hear "
        "them the way Keating means them — not as textbook definitions, but as calls to action."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s0["activities"][1]["title"] = "Vocabulary Introduction: Session 1"
    s0["activities"][1]["description"] = "Learn 6 words: gather, poet, rosebuds, seize, sentiment, stanza"
    s0["activities"][1]["data"]["text"] = (
        "Let's dive into the first 6 vocabulary words from the Carpe Diem scene in "
        "'Dead Poets Society.' Each word comes straight from Keating's lesson, and understanding "
        "how he uses them will change the way you hear everyday English.\n\n"

        "The first word is 'gather.' It's a verb meaning 'to come together' or 'to collect.' "
        "Keating quotes the 17th-century poet Robert Herrick: 'Gather ye rosebuds while ye may.' "
        "In this poem, 'gather' means to seize opportunities before they vanish — to pick the flowers "
        "of life while they're still blooming. 'Gather' is wonderfully versatile: 'gather information,' "
        "'gather courage,' 'gather around the fire,' 'a gathering of friends.' The word carries "
        "a sense of bringing things together with purpose. "
        "Example: She gathered her thoughts before stepping up to the microphone.\n\n"

        "The second word is 'poet.' It's a noun — a person who writes poems. Keating is obsessed "
        "with poets. He believes poetry isn't a dusty academic subject but a living, breathing force "
        "that can change how you see the world. The Dead Poets Society itself is a secret club "
        "where students read poetry aloud in a cave by candlelight. 'Poet' comes from the Greek "
        "'poietes,' meaning 'maker.' Related words: 'poetry' (the art form), 'poetic' (adjective), "
        "'poetics' (the study of poetry). 'Poetic justice' means a fitting, ironic outcome. "
        "Example: She didn't call herself a poet, but every email she wrote read like a love letter.\n\n"

        "The third word is 'rosebuds.' It's a plural noun — the buds of roses before they bloom. "
        "In Herrick's poem, rosebuds symbolize youth, beauty, and fleeting opportunity. "
        "'Gather ye rosebuds while ye may' means: enjoy your youth while you have it, because "
        "time is passing and the flowers will wilt. Keating uses this poem to teach his students "
        "that life is short and every moment matters. A 'rosebud' can also refer to something "
        "in its early, promising stage — 'Rosebud' is famously the last word spoken in 'Citizen Kane.' "
        "Example: The garden was full of rosebuds in early June, each one a promise of color to come.\n\n"

        "The fourth word is 'seize.' It's a verb meaning 'to grab suddenly and forcefully' or "
        "'to take hold of an opportunity.' 'Carpe diem' translates literally as 'seize the day' — "
        "and Keating delivers it like a battle cry. 'Seize' implies urgency and decisiveness: "
        "you don't gently take the day — you grab it with both hands. 'Seize an opportunity,' "
        "'seize control,' 'seize the moment.' The noun form is 'seizure' (a sudden attack or "
        "the act of taking possession). "
        "Example: When the chance to study abroad appeared, she seized it without hesitation.\n\n"

        "The fifth word is 'sentiment.' It's a noun meaning 'a feeling or opinion, especially "
        "one based on emotion rather than reason.' Keating asks his students to consider the "
        "sentiment behind the poetry — not just the words on the page, but the feeling that drove "
        "the poet to write them. 'Sentiment' can be positive ('public sentiment was in her favor') "
        "or negative ('sentimental' sometimes implies excessive emotion). 'Sentimental value' "
        "means something is valued for emotional reasons, not monetary ones. "
        "Example: The old watch had no market value, but its sentimental value was immeasurable.\n\n"

        "The sixth word is 'stanza.' It's a noun — a group of lines in a poem, separated from "
        "other groups by a space. Think of a stanza as a paragraph in poetry. Keating has his "
        "students analyze stanzas to find the heartbeat of a poem — the rhythm, the imagery, "
        "the emotion packed into a few carefully chosen lines. 'Stanza' comes from Italian, "
        "meaning 'stopping place' or 'room.' A poem might have four stanzas of four lines each, "
        "or any other combination. "
        "Example: The final stanza of the poem hit her so hard she had to read it three times.\n\n"

        "So there you have it — your first 6 words: gather, poet, rosebuds, seize, sentiment, "
        "and stanza. Each one is woven into Keating's lesson about living fully. "
        "Let's practice them now!"
    )

    # Activities 2-6: flashcards/vocab
    s0["activities"][2]["title"] = "Flashcards: Gather Ye Rosebuds"
    s0["activities"][2]["description"] = "Learn 6 words: gather, poet, rosebuds, seize, sentiment, stanza"

    s0["activities"][3]["title"] = "Flashcards: Speak Session 1 Vocabulary"
    s0["activities"][3]["description"] = "Practice saying 6 words: gather, poet, rosebuds, seize, sentiment, stanza"

    s0["activities"][4]["title"] = "Flashcards: Recognize Session 1 Vocabulary"
    s0["activities"][4]["description"] = "Recognize 6 words: gather, poet, rosebuds, seize, sentiment, stanza"

    s0["activities"][5]["title"] = "Flashcards: Recall Session 1 Vocabulary"
    s0["activities"][5]["description"] = "Recall 6 words: gather, poet, rosebuds, seize, sentiment, stanza"

    s0["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 1"
    s0["activities"][6]["description"] = "Master 6 words: gather, poet, rosebuds, seize, sentiment, stanza"

    # Activity 7: introAudio — grammar/usage
    s0["activities"][7]["title"] = "Grammar and Usage: Session 1"
    s0["activities"][7]["description"] = "How to use Session 1 vocabulary naturally in sentences"
    s0["activities"][7]["data"]["text"] = (
        "Great work! You've met your first 6 words. Now let's look at how they work "
        "in real English sentences, using Dead Poets Society's dialogue as our guide.\n\n"
        "'Gather' is a regular verb: gather, gathered, gathered. It pairs naturally with many "
        "nouns: 'gather information,' 'gather speed,' 'gather dust' (to be neglected), "
        "'gather momentum.' 'A gathering' is a noun meaning a meeting or assembly. "
        "Herrick's 'Gather ye rosebuds' uses the archaic 'ye' (you), giving it a timeless quality.\n\n"
        "'Poet' is a countable noun: 'a poet,' 'poets.' 'Poetess' (female poet) is considered "
        "outdated — use 'poet' for everyone. 'Poetic' as an adjective: 'poetic language,' "
        "'poetic license' (creative freedom to bend the rules). 'Poetically' is the adverb. "
        "Keating treats poets as prophets — people who see truths others miss.\n\n"
        "'Rosebuds' — the singular 'rosebud' is a compound noun: rose + bud. A 'bud' is any "
        "flower before it opens. 'Nip it in the bud' means to stop something early before it grows. "
        "In Herrick's poem, rosebuds are a metaphor for youth — beautiful but temporary.\n\n"
        "'Seize' is a regular verb: seize, seized, seized. 'Seize upon' means to eagerly take "
        "advantage of: 'She seized upon the idea.' 'Seize up' means to stop working suddenly: "
        "'The engine seized up.' The legal term 'seizure of assets' means confiscation. "
        "'Carpe diem' has entered English directly from Latin thanks to this film.\n\n"
        "'Sentiment' is a countable noun: 'a sentiment,' 'sentiments.' 'I share your sentiments' "
        "means 'I agree with your feelings.' 'Sentimental' (adjective) can be positive or negative — "
        "'a sentimental gift' vs. 'overly sentimental.' 'Sentimentality' is the noun form.\n\n"
        "'Stanza' is a countable noun: 'a stanza,' 'stanzas.' Common stanza types: 'couplet' "
        "(2 lines), 'tercet' (3 lines), 'quatrain' (4 lines). 'Verse' is sometimes used "
        "interchangeably with 'stanza,' though technically 'verse' can mean a single line."
    )

    # Activity 8: reading
    s0["activities"][8]["title"] = "Read: Dead Poets Society Excerpt (Part 1)"
    s0["activities"][8]["description"] = "Read the Carpe Diem classroom dialogue from Dead Poets Society"

    # Activity 9: speakReading
    s0["activities"][9]["title"] = "Speak: Practice the Dialogue (Part 1)"
    s0["activities"][9]["description"] = "Practice speaking the Carpe Diem dialogue aloud"

    # Activity 10: readAlong
    s0["activities"][10]["title"] = "Listen: Dead Poets Society Excerpt (Part 1)"
    s0["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s0["activities"][11]["title"] = "Write: Poetry and Seizing the Day"
    s0["activities"][11]["description"] = "Write sentences using Session 1 vocabulary"
    ws_items_0 = s0["activities"][11]["data"]["items"]
    ws_items_0[0]["prompt"] = (
        "Use the word 'gather' to write about collecting something meaningful — "
        "just as Herrick urges us to gather rosebuds before time runs out. "
        "Example: She gathered every letter he had ever written and read them "
        "by candlelight on the anniversary of his passing."
    )
    ws_items_0[1]["prompt"] = (
        "Use the word 'poet' to describe someone who sees the world differently — "
        "like Keating, who believes poets are the ones who truly understand life. "
        "Example: You don't need to publish a book to be a poet — "
        "anyone who finds beauty in ordinary moments deserves the title."
    )
    ws_items_0[2]["prompt"] = (
        "Use the word 'rosebuds' literally or as a metaphor for fleeting youth — "
        "the way Herrick's poem reminds us that beauty doesn't last forever. "
        "Example: Her grandmother always said that childhood years are rosebuds — "
        "you must enjoy them before they bloom and scatter in the wind."
    )
    ws_items_0[3]["prompt"] = (
        "Use the word 'seize' to describe grabbing an opportunity with urgency — "
        "like Keating's battle cry: 'Seize the day, boys.' "
        "Example: When the scholarship offer arrived, he seized it with both hands, "
        "knowing chances like that don't come twice."
    )
    ws_items_0[4]["prompt"] = (
        "Use the word 'sentiment' to express a feeling or opinion — "
        "like the emotion behind a poem that moves you to tears. "
        "Example: The sentiment behind her farewell speech was so genuine "
        "that even the toughest people in the room were wiping their eyes."
    )
    ws_items_0[5]["prompt"] = (
        "Use the word 'stanza' to talk about poetry or structured expression — "
        "like Keating teaching his students to find the heartbeat of a poem. "
        "Example: The third stanza of the poem changed everything — "
        "it was where the poet stopped describing the world and started questioning it."
    )


    # ── Session 1: Group 2 — breathing, limited, peruse, springs, timid, worms ──
    s1 = content["learningSessions"][1]
    s1["title"] = "Session 2: We Are Food for Worms"

    # Activity 0: introAudio — session intro
    s1["activities"][0]["title"] = "Introduction to Session 2"
    s1["activities"][0]["description"] = "Recap Session 1 and introduce the theme of mortality and courage"
    s1["activities"][0]["data"]["text"] = (
        "Welcome back to Session 2! In our first session, you learned 6 words from the "
        "Carpe Diem scene: gather, poet, rosebuds, seize, sentiment, and stanza. "
        "You discovered how Keating uses a 17th-century poem to wake his students up — "
        "to make them see that youth is a rosebud that won't stay in bloom forever, "
        "and that the only response to time's passing is to seize every moment.\n\n"
        "Now Keating goes further. He leads the boys to the trophy case and makes them "
        "stare at the faces of former students — young men who once walked these same halls, "
        "sat in these same chairs, had the same fire in their eyes. 'They're not that different "
        "from you, are they?' he says. 'Same haircuts. Full of hormones, just like you. "
        "Invincible, just like you feel.' Then the gut punch: 'They're fertilizing daffodils now.'\n\n"
        "Today you'll learn 6 new words: breathing, limited, peruse, springs, timid, and worms. "
        "These words carry the weight of mortality and the urgency it creates — and by the end "
        "of this session, you'll understand why Keating believes confronting death is the first "
        "step toward truly living."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s1["activities"][1]["title"] = "Vocabulary Introduction: Session 2"
    s1["activities"][1]["description"] = "Learn 6 words: breathing, limited, peruse, springs, timid, worms"
    s1["activities"][1]["data"]["text"] = (
        "Let's learn 6 new vocabulary words from the next part of Dead Poets Society — "
        "the scenes where Keating confronts his students with the reality of mortality.\n\n"

        "The first word is 'breathing.' It's the present participle of 'breathe,' used as "
        "a noun (gerund) or adjective. Keating tells his students that the boys in the old "
        "photographs were once 'breathing' — alive, full of potential, just like them. "
        "The word carries enormous weight in this context: breathing is the most basic sign "
        "of life, and Keating uses it to remind the boys that life is temporary. "
        "'Breathing room' means space to relax. 'Breathe in/out' describes the physical act. "
        "'Breathtaking' means astonishingly beautiful. 'Breath' (noun) vs. 'breathe' (verb) — "
        "a common spelling trap. "
        "Example: She stood at the summit, barely breathing, overwhelmed by the view stretching to the horizon.\n\n"

        "The second word is 'limited.' It's an adjective meaning 'restricted in size, amount, "
        "or extent.' Keating wants his students to understand that their time is limited — "
        "that the years of youth feel infinite but are actually heartbreakingly short. "
        "'Limited edition' means a small number produced. 'Limited liability' is a legal term. "
        "'Limit' as a verb: 'Limit your screen time.' 'Limitation' as a noun: 'know your limitations.' "
        "The opposite is 'unlimited.' "
        "Example: We have a limited window of opportunity — if we don't act now, it closes forever.\n\n"

        "The third word is 'peruse.' It's a verb that has an interesting double life. "
        "Traditionally, 'peruse' means 'to read carefully and thoroughly' — the opposite of skimming. "
        "But in modern casual usage, many people use it to mean 'to browse or skim.' "
        "Keating uses it in the traditional sense — he wants his students to peruse poetry deeply, "
        "not just glance at it. This word is more formal than 'read' and implies deliberate attention. "
        "'Perusal' is the noun form: 'for your perusal' (for you to examine). "
        "Example: She perused the contract line by line before signing, catching a clause that would have cost her thousands.\n\n"

        "The fourth word is 'springs.' It can be a noun (plural of 'spring') or a verb "
        "(third person singular of 'to spring'). As a noun, 'spring' has multiple meanings: "
        "the season between winter and summer, a coiled metal device, or a natural source of water. "
        "In the film, 'springs' connects to the idea of renewal and youth — spring is the season "
        "of new beginnings, and Keating's students are in the spring of their lives. "
        "As a verb: 'spring into action,' 'spring a surprise,' 'spring to mind.' "
        "Example: Hope springs eternal — even in the darkest winter, something inside us believes in spring.\n\n"

        "The fifth word is 'timid.' It's an adjective meaning 'showing a lack of courage or "
        "confidence; easily frightened.' Keating challenges his students not to be timid — "
        "not to let fear of judgment or failure stop them from expressing themselves. "
        "At Welton Academy, conformity is rewarded and individuality is punished, so being timid "
        "is the safe choice. Keating wants them to choose the dangerous one. "
        "'Timid' is softer than 'cowardly' — it implies shyness rather than moral failure. "
        "'Timidity' is the noun. 'Timidly' is the adverb. "
        "Example: The timid boy who never raised his hand in class turned out to be the one with the most brilliant ideas.\n\n"

        "The sixth word is 'worms.' It's the plural of 'worm' — a long, thin invertebrate "
        "that lives in soil. Keating tells his students: 'We are food for worms, lads.' "
        "It's a blunt, almost shocking reminder of mortality — that no matter how young, "
        "how talented, how invincible you feel, you will one day return to the earth. "
        "'Worm' can also be a verb: 'worm your way into' means to gradually gain access "
        "through persistence or manipulation. 'Can of worms' means a complicated situation "
        "that's best left alone. 'Bookworm' is someone who reads a lot. "
        "Example: The old saying is true — we are all food for worms, so we might as well live boldly while we can.\n\n"

        "Your 6 new words: breathing, limited, peruse, springs, timid, worms. "
        "Combined with Session 1, you now have 12 words from Dead Poets Society. "
        "Let's put them to work!"
    )

    # Activities 2-6: flashcards/vocab
    s1["activities"][2]["title"] = "Flashcards: Mortality and Courage"
    s1["activities"][2]["description"] = "Learn 6 words: breathing, limited, peruse, springs, timid, worms"

    s1["activities"][3]["title"] = "Flashcards: Speak Session 2 Vocabulary"
    s1["activities"][3]["description"] = "Practice saying 6 words: breathing, limited, peruse, springs, timid, worms"

    s1["activities"][4]["title"] = "Flashcards: Recognize Session 2 Vocabulary"
    s1["activities"][4]["description"] = "Recognize 6 words: breathing, limited, peruse, springs, timid, worms"

    s1["activities"][5]["title"] = "Flashcards: Recall Session 2 Vocabulary"
    s1["activities"][5]["description"] = "Recall 6 words: breathing, limited, peruse, springs, timid, worms"

    s1["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 2"
    s1["activities"][6]["description"] = "Master 6 words: breathing, limited, peruse, springs, timid, worms"

    # Activity 7: introAudio — grammar/usage
    s1["activities"][7]["title"] = "Grammar and Usage: Session 2"
    s1["activities"][7]["description"] = "How to use Session 2 vocabulary naturally in sentences"
    s1["activities"][7]["data"]["text"] = (
        "Excellent! Let's explore how these 6 words behave in real English.\n\n"
        "'Breathing' — 'breathe' is the verb (regular: breathe, breathed, breathed). "
        "'Breath' is the noun (rhymes with 'death'). 'Breathe' has a long 'ee' sound; "
        "'breath' has a short 'e.' This spelling/pronunciation difference trips up many learners. "
        "'Breathing space' means room to think. 'Heavy breathing' describes labored respiration. "
        "Keating's use of 'breathing' reduces life to its most elemental act.\n\n"
        "'Limited' — the verb 'limit' is regular: limit, limited, limited. "
        "'Limited to' means restricted to: 'Seating is limited to 50 people.' "
        "'Off-limits' means forbidden: 'The rooftop is off-limits.' "
        "'Sky's the limit' means there are no restrictions. The irony in the film is that "
        "Welton Academy limits everything — thought, expression, ambition — while Keating "
        "tries to show the boys that their potential is unlimited.\n\n"
        "'Peruse' — a formal verb. 'Peruse' + direct object: 'peruse a document,' "
        "'peruse the menu.' 'At your perusal' is a formal phrase meaning 'for you to examine.' "
        "Be aware that many native speakers use 'peruse' to mean 'browse casually,' "
        "which is technically the opposite of its original meaning. Context will tell you which.\n\n"
        "'Springs' — as a season, always lowercase unless starting a sentence: 'in spring,' "
        "'last spring.' As a water source: 'hot springs,' 'natural springs.' "
        "As a verb: 'spring, sprang, sprung.' 'Spring to life' means to suddenly become active. "
        "'Spring chicken' in 'no spring chicken' means someone is no longer young.\n\n"
        "'Timid' — synonyms include 'shy,' 'bashful,' 'reserved.' 'Timid' implies a deeper "
        "lack of confidence than 'shy.' 'Intimidate' (to make someone timid) shares the same "
        "Latin root: 'timidus.' Keating's mission is to de-intimidate his students.\n\n"
        "'Worms' — 'worm' as a verb: 'worm your way out of something' (escape through cunning). "
        "'Wormhole' in physics is a theoretical passage through spacetime. "
        "'Early bird catches the worm' means those who act first get the reward. "
        "Keating's 'food for worms' echoes Shakespeare's Hamlet: 'A man may fish with the worm "
        "that hath eat of a king.' Mortality is the great equalizer."
    )

    # Activity 8-10: reading/speak/listen
    s1["activities"][8]["title"] = "Read: Dead Poets Society Excerpt (Part 2)"
    s1["activities"][8]["description"] = "Read the dialogue about mortality and the urgency of living"

    s1["activities"][9]["title"] = "Speak: Practice the Dialogue (Part 2)"
    s1["activities"][9]["description"] = "Practice speaking the mortality dialogue aloud"

    s1["activities"][10]["title"] = "Listen: Dead Poets Society Excerpt (Part 2)"
    s1["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s1["activities"][11]["title"] = "Write: Mortality and Living Fully"
    s1["activities"][11]["description"] = "Write sentences using Session 2 vocabulary"
    ws_items_1 = s1["activities"][11]["data"]["items"]
    ws_items_1[0]["prompt"] = (
        "Use the word 'breathing' to describe the simple act of being alive — "
        "like Keating reminding his students that the boys in the photographs were once breathing. "
        "Example: As long as you are breathing, you have the power to change your story."
    )
    ws_items_1[1]["prompt"] = (
        "Use the word 'limited' to describe something restricted or finite — "
        "like Keating's warning that youth and time are limited resources. "
        "Example: Our time together is limited, so let's make every conversation count."
    )
    ws_items_1[2]["prompt"] = (
        "Use the word 'peruse' to describe reading or examining something carefully — "
        "like Keating wanting his students to truly engage with poetry, not just skim it. "
        "Example: He perused the old map for hours, tracing routes that explorers had followed centuries ago."
    )
    ws_items_1[3]["prompt"] = (
        "Use the word 'springs' as a noun or verb to evoke renewal or sudden action — "
        "like the spring of youth that Keating urges his students not to waste. "
        "Example: Inspiration springs from the strangest places — a conversation, a rainstorm, a line in a book."
    )
    ws_items_1[4]["prompt"] = (
        "Use the word 'timid' to describe hesitation or lack of confidence — "
        "like the students who are afraid to speak up in a world that punishes individuality. "
        "Example: She was timid at first, but once she started reading her poem aloud, her voice grew stronger with every line."
    )
    ws_items_1[5]["prompt"] = (
        "Use the word 'worms' literally or in the phrase 'food for worms' — "
        "like Keating's blunt reminder that mortality comes for everyone. "
        "Example: We are all food for worms in the end — the only question is what we do with the time before."
    )


    # ── Session 2: Group 3 — almighty, capable, destined, extraordinary, squander, whisper ──
    s2 = content["learningSessions"][2]
    s2["title"] = "Session 3: Make Your Lives Extraordinary"

    # Activity 0: introAudio — session intro
    s2["activities"][0]["title"] = "Introduction to Session 3"
    s2["activities"][0]["description"] = "Recap Sessions 1-2 and introduce the themes of destiny and self-expression"
    s2["activities"][0]["data"]["text"] = (
        "Welcome to Session 3 — the final learning session before your review! "
        "So far you've learned 12 words from Dead Poets Society. In Session 1, you met "
        "gather, poet, rosebuds, seize, sentiment, and stanza — the words of Keating's "
        "first lesson, where a 17th-century poem becomes a call to arms against wasted time. "
        "In Session 2, you learned breathing, limited, peruse, springs, timid, and worms — "
        "the words of mortality, where Keating forces his students to stare at the faces "
        "of dead men and ask themselves: 'What will your verse be?'\n\n"
        "Now we reach the climax of Keating's philosophy. He doesn't just want his students "
        "to acknowledge that life is short — he wants them to do something about it. "
        "'Make your lives extraordinary,' he says. Not ordinary. Not acceptable. Extraordinary. "
        "It's a word that means 'beyond the ordinary' — and Keating believes every single one "
        "of his students is capable of it.\n\n"
        "Your final 6 words: almighty, capable, destined, extraordinary, squander, and whisper. "
        "By the end of this session, you'll have all 18 vocabulary words — and you'll understand "
        "why this film has inspired generations to stand on their desks and see the world differently."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s2["activities"][1]["title"] = "Vocabulary Introduction: Session 3"
    s2["activities"][1]["description"] = "Learn 6 words: almighty, capable, destined, extraordinary, squander, whisper"
    s2["activities"][1]["data"]["text"] = (
        "Here are your final 6 vocabulary words, drawn from the most powerful moments "
        "in Dead Poets Society.\n\n"

        "The first word is 'almighty.' It's an adjective meaning 'having complete power; "
        "omnipotent' or, informally, 'very great or intense.' In the film, Keating quotes "
        "Walt Whitman: 'O me! O life! ... That the powerful play goes on, and you may contribute "
        "a verse.' The 'almighty' power of poetry, in Keating's view, is its ability to change "
        "how you see yourself and the world. 'The Almighty' (capitalized) refers to God. "
        "'Almighty' as an intensifier: 'an almighty crash,' 'an almighty mess.' "
        "The word carries a sense of overwhelming force. "
        "Example: The almighty roar of the waterfall drowned out every other sound in the valley.\n\n"

        "The second word is 'capable.' It's an adjective meaning 'having the ability or quality "
        "necessary to do something.' Keating sees capability in every student — even the ones "
        "who have been told their whole lives that they're not good enough. 'Capable of' is the "
        "standard preposition: 'She's capable of great things.' 'Capability' is the noun. "
        "'Incapable' is the opposite. 'Capable' implies not just ability but competence — "
        "a capable person doesn't just try, they succeed. "
        "Example: She proved she was capable of leading the team through the most difficult quarter in the company's history.\n\n"

        "The third word is 'destined.' It's an adjective meaning 'certain to meet a particular "
        "fate' or 'intended for a particular purpose.' The students at Welton are told they're "
        "destined for greatness — but it's a narrow, prescribed greatness: doctor, lawyer, banker. "
        "Keating wants them to discover what they're truly destined for, not what their fathers "
        "decided. 'Destined for' is the standard phrase: 'destined for success,' 'destined for "
        "each other.' 'Destiny' is the noun. 'Destination' is where you're going physically. "
        "Example: From the moment she picked up a violin at age four, everyone knew she was destined to perform on the world's greatest stages.\n\n"

        "The fourth word is 'extraordinary.' It's an adjective meaning 'very unusual or remarkable; "
        "beyond what is ordinary.' This is the word Keating builds his entire philosophy around: "
        "'Make your lives extraordinary.' The word breaks down as 'extra' (beyond) + 'ordinary' "
        "(normal). It's pronounced ex-TROR-din-ary (5 syllables, though many speakers compress it "
        "to 4). 'Extraordinarily' is the adverb. The opposite is simply 'ordinary.' "
        "Example: The most extraordinary people are often the ones who started with the least and refused to accept it.\n\n"

        "The fifth word is 'squander.' It's a verb meaning 'to waste something valuable, "
        "especially time, money, or an opportunity, in a reckless or foolish way.' "
        "Keating's entire message is: don't squander your youth. Don't let the years slip by "
        "while you're following someone else's plan. 'Squander' is stronger than 'waste' — "
        "it implies that what was lost was precious and the loss was avoidable. "
        "'Squander a fortune,' 'squander an opportunity,' 'squander your talent.' "
        "Example: He squandered his twenties chasing approval from people who never cared about him.\n\n"

        "The sixth and final word is 'whisper.' It can be a verb or a noun. As a verb, "
        "it means 'to speak very softly, using one's breath rather than one's voice.' "
        "Keating doesn't shout 'Carpe diem' — he whispers it. And that whisper is more powerful "
        "than any shout could be, because it feels like a secret, a gift, something meant just "
        "for you. 'Whisper' as a noun: 'She spoke in a whisper.' 'Whisper campaign' means "
        "spreading rumors quietly. 'It's whispered that...' means there are rumors. "
        "Example: He leaned in close and whispered the answer, as if sharing the most important secret in the world.\n\n"

        "And there you have it — all 18 words: gather, poet, rosebuds, seize, sentiment, stanza, "
        "breathing, limited, peruse, springs, timid, worms, almighty, capable, destined, "
        "extraordinary, squander, and whisper. You now have the complete vocabulary of "
        "Dead Poets Society. Let's practice these final 6!"
    )

    # Activities 2-6: flashcards/vocab
    s2["activities"][2]["title"] = "Flashcards: Destiny and Self-Expression"
    s2["activities"][2]["description"] = "Learn 6 words: almighty, capable, destined, extraordinary, squander, whisper"

    s2["activities"][3]["title"] = "Flashcards: Speak Session 3 Vocabulary"
    s2["activities"][3]["description"] = "Practice saying 6 words: almighty, capable, destined, extraordinary, squander, whisper"

    s2["activities"][4]["title"] = "Flashcards: Recognize Session 3 Vocabulary"
    s2["activities"][4]["description"] = "Recognize 6 words: almighty, capable, destined, extraordinary, squander, whisper"

    s2["activities"][5]["title"] = "Flashcards: Recall Session 3 Vocabulary"
    s2["activities"][5]["description"] = "Recall 6 words: almighty, capable, destined, extraordinary, squander, whisper"

    s2["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 3"
    s2["activities"][6]["description"] = "Master 6 words: almighty, capable, destined, extraordinary, squander, whisper"

    # Activity 7: introAudio — grammar/usage
    s2["activities"][7]["title"] = "Grammar and Usage: Session 3"
    s2["activities"][7]["description"] = "How to use Session 3 vocabulary naturally in sentences"
    s2["activities"][7]["data"]["text"] = (
        "Let's look at how these final 6 words work in English grammar.\n\n"
        "'Almighty' — as an adjective, it precedes the noun: 'almighty power,' 'an almighty storm.' "
        "As a noun (with 'the'): 'the Almighty' means God. The informal intensifier use is common "
        "in British English: 'an almighty row' (a huge argument). 'Almighty' combines 'all' + 'mighty' "
        "— literally 'all-powerful.'\n\n"
        "'Capable' — always followed by 'of' + gerund: 'capable of achieving,' 'capable of understanding.' "
        "Never 'capable to do.' 'Capability' (noun) can be plural: 'military capabilities,' "
        "'technological capabilities.' 'Incapable of' is the negative form. "
        "Keating sees capability where others see limitation.\n\n"
        "'Destined' — 'destined for' + noun: 'destined for greatness.' 'Destined to' + verb: "
        "'destined to fail.' 'Destiny' vs. 'fate': 'destiny' often implies a positive or grand "
        "outcome, while 'fate' can be neutral or negative. 'Predestined' means determined in advance.\n\n"
        "'Extraordinary' — note the pronunciation: the 'extra' prefix is compressed, so it sounds "
        "like 'ik-STROR-din-ary,' not 'EX-tra-OR-din-ary.' 'Extraordinary measures,' "
        "'extraordinary circumstances,' 'an extraordinary talent.' In legal language, "
        "'extraordinary session' means a special meeting outside the regular schedule.\n\n"
        "'Squander' — a transitive verb that always takes a direct object: 'squander money,' "
        "'squander time,' 'squander goodwill.' You can't just 'squander' — you must squander "
        "something. The word implies both waste and regret. 'Squandered' as an adjective: "
        "'a squandered opportunity.' There's no common noun form.\n\n"
        "'Whisper' — regular verb: whisper, whispered, whispered. 'Whisper to someone,' "
        "'whisper in someone's ear,' 'whisper sweet nothings' (romantic murmuring). "
        "'A stage whisper' is a loud whisper intended to be heard by the audience. "
        "Keating's whisper of 'Carpe diem' is a stage whisper in the best sense — "
        "quiet enough to feel intimate, loud enough to change lives."
    )

    # Activity 8-10: reading/speak/listen
    s2["activities"][8]["title"] = "Read: Dead Poets Society Excerpt (Part 3)"
    s2["activities"][8]["description"] = "Read the dialogue about destiny, self-expression, and making life extraordinary"

    s2["activities"][9]["title"] = "Speak: Practice the Dialogue (Part 3)"
    s2["activities"][9]["description"] = "Practice speaking the final dialogue excerpt aloud"

    s2["activities"][10]["title"] = "Listen: Dead Poets Society Excerpt (Part 3)"
    s2["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s2["activities"][11]["title"] = "Write: Destiny and Extraordinary Lives"
    s2["activities"][11]["description"] = "Write sentences using Session 3 vocabulary"
    ws_items_2 = s2["activities"][11]["data"]["items"]
    ws_items_2[0]["prompt"] = (
        "Use the word 'almighty' to describe overwhelming power or intensity — "
        "like the almighty force of poetry that Keating believes can change lives. "
        "Example: The almighty silence that followed her confession was louder than any words could have been."
    )
    ws_items_2[1]["prompt"] = (
        "Use the word 'capable' to describe someone's ability or potential — "
        "like Keating seeing greatness in students the world has written off. "
        "Example: Every child is capable of brilliance — the tragedy is how many are never given the chance to show it."
    )
    ws_items_2[2]["prompt"] = (
        "Use the word 'destined' to write about fate or purpose — "
        "like the tension between what the students are told they're destined for "
        "and what they truly want to become. "
        "Example: She always felt destined for something bigger than the small town she grew up in."
    )
    ws_items_2[3]["prompt"] = (
        "Use the word 'extraordinary' to describe something beyond the ordinary — "
        "like Keating's command: 'Make your lives extraordinary.' "
        "Example: The most extraordinary thing about her was not her talent but her refusal to give up."
    )
    ws_items_2[4]["prompt"] = (
        "Use the word 'squander' to describe wasting something precious — "
        "like Keating's warning not to squander the gift of youth and time. "
        "Example: He squandered years of his life trying to be someone he was never meant to be."
    )
    ws_items_2[5]["prompt"] = (
        "Use the word 'whisper' to describe speaking softly or sharing a secret — "
        "like Keating whispering 'Carpe diem' as if it were the most important secret in the world. "
        "Example: The wind whispered through the trees, carrying the scent of rain and the promise of change."
    )


    # ── Session 3: Review (4 activities) ──
    s3 = content["learningSessions"][3]
    s3["title"] = "Review"

    s3["activities"][0]["title"] = "Congratulations and Review"
    s3["activities"][0]["description"] = "Celebrate your progress and prepare for the full review"
    s3["activities"][0]["data"]["text"] = (
        "Congratulations! You've learned all 18 vocabulary words from Dead Poets Society. "
        "Let's take a moment to look back at what you've accomplished.\n\n"
        "In Session 1, you learned gather, poet, rosebuds, seize, sentiment, and stanza — "
        "the words of Keating's first lesson, where a 17th-century poem about gathering rosebuds "
        "becomes a battle cry to seize the day and find the sentiment hidden in every stanza.\n\n"
        "In Session 2, you learned breathing, limited, peruse, springs, timid, and worms — "
        "the words of mortality, where Keating forces his students to confront the fact that "
        "their time is limited, that they are food for worms, and that being timid is a luxury "
        "they cannot afford.\n\n"
        "In Session 3, you learned almighty, capable, destined, extraordinary, squander, "
        "and whisper — the words of transformation, where Keating whispers 'Carpe diem' "
        "and challenges every student to believe they are capable of something extraordinary "
        "and destined for more than a life of quiet conformity.\n\n"
        "Now it's time to review all 18 words together. This review session will test your "
        "recognition and recall across all three groups. After this, you'll be ready to read "
        "the complete dialogue in the final session. Let's go!"
    )

    s3["activities"][1]["title"] = "Flashcards: Review All 18 Words"
    s3["activities"][1]["description"] = "Review all 18 vocabulary words from Dead Poets Society"

    s3["activities"][2]["title"] = "Flashcards: Recognize All Vocabulary"
    s3["activities"][2]["description"] = "Test your recognition of all 18 words"

    s3["activities"][3]["title"] = "Flashcards: Recall All Vocabulary"
    s3["activities"][3]["description"] = "Test your recall of all 18 words"

    # ── Session 4: Full reading + farewell (5 activities) ──
    s4 = content["learningSessions"][4]
    s4["title"] = "Full Dialogue Reading"

    s4["activities"][0]["title"] = "Introduction to the Complete Reading"
    s4["activities"][0]["description"] = "Prepare for reading the full Dead Poets Society dialogue"
    s4["activities"][0]["data"]["text"] = (
        "Welcome to the final session! This is the moment everything comes together. "
        "Over the past three sessions, you've built a vocabulary of 18 words drawn directly "
        "from Dead Poets Society's dialogue. You've learned their meanings, practiced "
        "their pronunciation, explored their grammar, and used them in your own writing.\n\n"
        "Now you're going to read the complete dialogue — all three excerpts combined into one "
        "continuous passage. As you read, you'll encounter every single one of your 18 words "
        "in context. This time, they won't be new — they'll be familiar friends.\n\n"
        "Here are all 18 words you'll see: gather, poet, rosebuds, seize, sentiment, stanza, "
        "breathing, limited, peruse, springs, timid, worms, almighty, capable, destined, "
        "extraordinary, squander, and whisper.\n\n"
        "Take your time with the reading. Let Keating's voice come through. "
        "And remember — carpe diem. Seize the day."
    )

    s4["activities"][1]["title"] = "Read: Complete Dead Poets Society Dialogue"
    s4["activities"][1]["description"] = "Read the full classroom dialogue from beginning to end"

    s4["activities"][2]["title"] = "Speak: Practice the Complete Dialogue"
    s4["activities"][2]["description"] = "Practice speaking the entire dialogue aloud"

    s4["activities"][3]["title"] = "Listen: Complete Dead Poets Society Dialogue"
    s4["activities"][3]["description"] = "Listen to the complete dialogue and follow along"

    s4["activities"][4]["title"] = "Farewell and Vocabulary Review"
    s4["activities"][4]["description"] = "Final review of all 18 words and farewell"
    s4["activities"][4]["data"]["text"] = (
        "You've done it — you've completed the entire Dead Poets Society vocabulary course! "
        "Let's do one final review of all 18 words before we say goodbye.\n\n"

        "'Gather' — to collect or come together, as in Herrick's call to gather rosebuds. "
        "Example: They gathered around the campfire and shared stories until the stars came out.\n\n"
        "'Poet' — a person who writes poems, and in Keating's world, a person who truly sees. "
        "Example: Every great poet started as someone who simply refused to stop noticing things.\n\n"
        "'Rosebuds' — the buds of roses, and a metaphor for the fleeting beauty of youth. "
        "Example: The rosebuds in the garden reminded her that nothing beautiful lasts forever.\n\n"
        "'Seize' — to grab forcefully, to take hold of an opportunity with urgency. "
        "Example: She seized the microphone and delivered the speech that changed everything.\n\n"
        "'Sentiment' — a feeling or opinion, especially one rooted in emotion. "
        "Example: The sentiment behind his words mattered more than the words themselves.\n\n"
        "'Stanza' — a group of lines in a poem, like a paragraph in prose. "
        "Example: The final stanza brought the entire poem together in a way nobody expected.\n\n"

        "'Breathing' — the act of drawing air into and expelling it from the lungs; being alive. "
        "Example: She paused, barely breathing, as the last note of the symphony faded into silence.\n\n"
        "'Limited' — restricted in size, amount, or extent; finite. "
        "Example: Time is the most limited resource we have — spend it on what matters.\n\n"
        "'Peruse' — to read or examine carefully and thoroughly. "
        "Example: He perused the ancient manuscript, searching for the passage that had eluded scholars for centuries.\n\n"
        "'Springs' — the season of renewal, or sources of water, or the act of leaping forward. "
        "Example: Creativity springs from the courage to be wrong.\n\n"
        "'Timid' — lacking courage or confidence; easily frightened. "
        "Example: The timid voice that began the poem grew into a roar by the final line.\n\n"
        "'Worms' — invertebrates in soil, and Keating's blunt reminder of mortality. "
        "Example: We are food for worms — so why waste a single day being someone you're not?\n\n"

        "'Almighty' — having complete power; overwhelmingly great. "
        "Example: The almighty crash of thunder shook the windows and silenced the room.\n\n"
        "'Capable' — having the ability to do something; competent. "
        "Example: You are capable of far more than you've been led to believe.\n\n"
        "'Destined' — certain to meet a particular fate; meant for something. "
        "Example: Some people are destined to lead — they just need someone to tell them so.\n\n"
        "'Extraordinary' — beyond what is ordinary; remarkable. "
        "Example: An extraordinary life isn't built on talent alone — it's built on the refusal to settle.\n\n"
        "'Squander' — to waste something valuable in a reckless way. "
        "Example: Don't squander the years you have — they pass faster than you think.\n\n"
        "'Whisper' — to speak very softly; a quiet, intimate sound. "
        "Example: He whispered 'thank you' so quietly she almost didn't hear it — but she felt it.\n\n"

        "Thank you for learning with Dead Poets Society. You came for 18 vocabulary words, "
        "but I hope you're leaving with something more — a reminder that conformity is the enemy "
        "of greatness, that poetry is not a luxury but a necessity, and that the most powerful "
        "words are sometimes the ones spoken in a whisper.\n\n"
        "Carpe diem. Seize the day. Make your lives extraordinary. "
        "Keep reading, keep speaking, keep writing. Goodbye, and good luck!"
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
    print(f"Created en-en Dead Poets Society curriculum: {cid}")
    return cid


if __name__ == "__main__":
    create()
