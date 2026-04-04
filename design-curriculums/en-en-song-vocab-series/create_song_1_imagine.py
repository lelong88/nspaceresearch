"""
Create en-en song curriculum #1: Imagine
Mirror of vi-en source jHM7Pekp6LtLjqok — all Vietnamese UI text rewritten in English.

Source song: Imagine by John Lennon (1971)
YouTube: https://www.youtube.com/watch?v=YkgkThdzX-8

18 vocabulary words in 3 groups of 6 (same as vi-en source):
  Group 1: imagine, heaven, dreamer, hope, above, below
  Group 2: peace, religion, countries, living, join, someday
  Group 3: possessions, greed, hunger, brotherhood, sharing, wonder

All user-facing text in English. Reading passages stay as-is (already English).
Vocabulary words stay as-is (already English).

Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 9.1, 9.2, 9.3, 9.4, 9.5
"""

import sys, json, requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"
SOURCE_ID = "jHM7Pekp6LtLjqok"

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
    content["title"] = "'Imagine' — John Lennon"

    content["description"] = (
        "CLOSE YOUR EYES AND PICTURE A WORLD WITH NO BORDERS, NO HUNGER, NO GREED — JUST PEOPLE LIVING AS ONE.\n\n"
        "That's exactly what John Lennon asked the world to do in 1971 when he sat at a white "
        "grand piano and sang three minutes that would outlive him by decades. 'Imagine' isn't "
        "just a song — it's a thought experiment wrapped in a melody so gentle it disarms you "
        "before you realize how radical the lyrics actually are. No heaven, no countries, no "
        "possessions — Lennon strips away every structure humans cling to and asks: what's left? "
        "The answer, he suggests, is peace.\n\n"
        "Now imagine not just humming along, but UNDERSTANDING every word Lennon chose — "
        "from 'dreamer' when he admits the world might call him naive, "
        "to 'brotherhood' when he paints his vision of humanity united, "
        "to 'greed' when he names the force that keeps us apart. "
        "Each vocabulary word is a brushstroke in Lennon's portrait of a better world.\n\n"
        "When you hear 'imagine all the people living life in peace' and you truly grasp "
        "that 'living' here means not just surviving but thriving with purpose — "
        "that's the moment English stops being a subject and becomes a lens. "
        "Music doesn't just teach you words; it teaches you how words feel.\n\n"
        "18 vocabulary words drawn directly from the lyrics, combined with "
        "a multi-sensory learning method — listening, reading, speaking, writing — "
        "so you sharpen your English while carrying John Lennon's dream of "
        "peace, unity, and a world without walls in your heart."
    )

    content["preview"] = {
        "text": (
            "Have you ever listened to 'Imagine' and felt the walls between people dissolve — "
            "just for a moment? John Lennon wrote this song as a blueprint for a world that "
            "doesn't exist yet — and now you'll learn English through the very words he chose.\n\n"
            "18 English vocabulary words you'll learn: imagine, heaven, dreamer, hope, above, "
            "below, peace, religion, countries, living, join, someday, possessions, greed, "
            "hunger, brotherhood, sharing, wonder.\n\n"
            "Across 5 sessions you'll read the actual lyrics, discover how Lennon uses "
            "the simplest words to challenge the deepest assumptions — from the heaven "
            "he asks you to erase to the brotherhood he asks you to build.\n\n"
            "Tap the link below to watch the original music video — after this course, "
            "you'll hear Lennon sing and understand every single word naturally."
        )
    }

    content["contentTypeTags"] = ["music"]
    content["is_public"] = False

    # ── Session 0: Group 1 — imagine, heaven, dreamer, hope, above, below ──
    s0 = content["learningSessions"][0]
    s0["title"] = "Session 1: Imagine — Dreams and Vision"

    # Activity 0: introAudio — song intro
    s0["activities"][0]["title"] = "Introduction to the Song"
    s0["activities"][0]["description"] = "Setting the stage for John Lennon's anthem of peace and possibility"
    s0["activities"][0]["data"]["text"] = (
        "Welcome to the vocabulary-through-music course! Today we begin with one of "
        "the most iconic songs in the history of popular music — 'Imagine' by John Lennon. "
        "Released in 1971, just one year after the Beatles broke up, this song became "
        "Lennon's defining solo statement — a gentle, piano-driven meditation on what the "
        "world could look like if we stripped away the things that divide us.\n\n"
        "The genius of 'Imagine' lies in its simplicity. Lennon doesn't shout or preach. "
        "He sits at a piano and asks you to picture something — no heaven above, no hell below, "
        "no countries, no religion, no possessions. One by one, he removes the structures "
        "that humans have built and fought over for centuries, and what remains is startlingly "
        "beautiful: just people, sharing the world, living in peace. The melody is so soft "
        "that the radical nature of the words almost slips past you unnoticed.\n\n"
        "In this first session, you'll learn 6 vocabulary words from the opening verse "
        "of the song: imagine, heaven, dreamer, hope, above, and below. These are the words "
        "Lennon uses to set up his thought experiment — and by the end of this session, "
        "you'll hear them not as simple dictionary entries, but as invitations to see "
        "the world through entirely different eyes."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s0["activities"][1]["title"] = "Vocabulary Introduction: Session 1"
    s0["activities"][1]["description"] = "Learn 6 words: imagine, heaven, dreamer, hope, above, below"
    s0["activities"][1]["data"]["text"] = (
        "Let's dive into the first 6 vocabulary words from 'Imagine.' "
        "Each word comes straight from John Lennon's lyrics, and understanding how he uses them "
        "will change the way you hear this song — and English — forever.\n\n"

        "The first word is 'imagine.' It's a verb meaning 'to form a mental image of something "
        "not present or not yet real.' This is the most important word in the entire song — it's "
        "the title, the first word of the first line, and the engine that drives every verse. "
        "Lennon doesn't say 'there is no heaven' — he says 'imagine there's no heaven.' "
        "That single word transforms a statement into an invitation. You can imagine a future, "
        "imagine a conversation, imagine yourself in someone else's shoes. 'Imagination' is the "
        "noun; 'imaginary' means not real; 'imaginative' means creative. "
        "Example: She closed her eyes and tried to imagine what the city looked like a hundred years ago.\n\n"

        "The second word is 'heaven.' It's a noun meaning 'the abode of God and the angels, "
        "or a place of supreme happiness.' In the song, Lennon asks us to imagine there's no "
        "heaven — not to attack belief, but to ask what would happen if people stopped dividing "
        "themselves over where they think they're going after death. 'Heaven' is also used "
        "casually: 'This beach is heaven,' 'Good heavens!' (surprise), 'heaven-sent' (perfectly "
        "timed), 'move heaven and earth' (do everything possible). The adjective is 'heavenly.' "
        "Example: After a week of camping in the rain, a hot shower felt like absolute heaven.\n\n"

        "The third word is 'dreamer.' It's a noun meaning 'a person who dreams, or who has "
        "impractical ideas and plans.' Lennon famously sings 'You may say I'm a dreamer, but "
        "I'm not the only one.' He owns the label — yes, his vision is idealistic, but he's "
        "not alone in wanting it. A 'dreamer' can be positive (visionary, creative) or negative "
        "(unrealistic, head in the clouds). The verb is 'dream'; 'dreamy' means vague or "
        "attractive; 'daydreamer' is someone who fantasizes during waking hours. "
        "Example: People called him a dreamer, but his ideas eventually changed the entire industry.\n\n"

        "The fourth word is 'hope.' It can be a noun or a verb. As a noun, it means 'a feeling "
        "of expectation and desire for something to happen.' As a verb: 'I hope you're well.' "
        "In the song, Lennon hopes that someday the world will join together as one. 'Hope' is "
        "lighter than 'wish' — it implies possibility, not just desire. 'Hopeful' means optimistic; "
        "'hopeless' means without hope or very bad at something; 'hopefully' is an adverb that "
        "also functions as a sentence modifier: 'Hopefully, it won't rain.' "
        "Example: Even in the darkest moments, she never lost hope that things would get better.\n\n"

        "The fifth word is 'above.' It's a preposition or adverb meaning 'at a higher level or "
        "position.' Lennon sings 'Imagine there's no heaven... above us only sky' — replacing "
        "the idea of a divine realm with the simple, beautiful reality of open sky. 'Above' "
        "has both literal and figurative uses: 'the apartment above,' 'above average,' "
        "'above suspicion,' 'above all' (most importantly). It's the opposite of 'below.' "
        "Example: The stars above seemed close enough to touch on that clear mountain night.\n\n"

        "The sixth word is 'below.' It's a preposition or adverb meaning 'at a lower level or "
        "position.' In the song, Lennon pairs it with 'above': no heaven above, no hell below — "
        "just the earth and the people on it. 'Below' has literal uses ('the valley below,' "
        "'below the surface') and figurative ones ('below average,' 'below expectations,' "
        "'below the belt' meaning unfair). 'Below zero' means colder than the freezing point. "
        "Example: From the cliff's edge, the river below looked like a thin silver ribbon.\n\n"

        "Your first 6 words: imagine, heaven, dreamer, hope, above, and below. "
        "Each one is part of John Lennon's invitation to see the world differently. "
        "Let's practice them now!"
    )

    # Activities 2-6: flashcards/vocab — update titles and descriptions
    s0["activities"][2]["title"] = "Flashcards: Dreams and Vision"
    s0["activities"][2]["description"] = "Learn 6 words: imagine, heaven, dreamer, hope, above, below"

    s0["activities"][3]["title"] = "Flashcards: Speak Session 1 Vocabulary"
    s0["activities"][3]["description"] = "Practice saying 6 words: imagine, heaven, dreamer, hope, above, below"

    s0["activities"][4]["title"] = "Flashcards: Recognize Session 1 Vocabulary"
    s0["activities"][4]["description"] = "Recognize 6 words: imagine, heaven, dreamer, hope, above, below"

    s0["activities"][5]["title"] = "Flashcards: Recall Session 1 Vocabulary"
    s0["activities"][5]["description"] = "Recall 6 words: imagine, heaven, dreamer, hope, above, below"

    s0["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 1"
    s0["activities"][6]["description"] = "Master 6 words: imagine, heaven, dreamer, hope, above, below"

    # Activity 7: introAudio — grammar/usage
    s0["activities"][7]["title"] = "Grammar and Usage: Session 1"
    s0["activities"][7]["description"] = "How to use Session 1 vocabulary naturally in sentences"
    s0["activities"][7]["data"]["text"] = (
        "Great work! You've met your first 6 words. Now let's look at how they work "
        "in real English sentences, using the lyrics of 'Imagine' as our guide.\n\n"
        "'Imagine' is a regular verb: imagine, imagined, imagined. It can take a direct object "
        "('imagine a world'), a clause ('imagine that there's no heaven'), or a gerund "
        "('imagine living without fear'). In the song, Lennon uses 'imagine' with a clause: "
        "'Imagine there's no heaven.' The noun 'imagination' is uncountable when it means "
        "'the faculty of imagining' but countable in phrases like 'a vivid imagination.' "
        "'Imaginary' means not real; 'imaginative' means creative.\n\n"
        "'Heaven' is usually uncountable when referring to the spiritual place ('go to heaven,' "
        "not 'go to a heaven'). But 'the heavens' (plural) means 'the sky': 'The heavens opened' "
        "(it started raining heavily). 'Heavenly' is the adjective. 'For heaven's sake!' is an "
        "exclamation of frustration. 'Heaven knows' means 'nobody knows.'\n\n"
        "'Dreamer' is a countable noun formed by adding '-er' to 'dream.' This is a productive "
        "English pattern: teach → teacher, sing → singer, dream → dreamer. 'Dream' itself can "
        "be a noun or verb. Past tense: 'dreamed' or 'dreamt' (both correct). "
        "'Dream up' means to invent: 'She dreamed up a brilliant plan.'\n\n"
        "'Hope' as a verb takes a clause ('I hope you're happy') or an infinitive ('I hope to see "
        "you soon'). Never 'I hope you to come' — that's a common error. As a noun: 'a ray of hope,' "
        "'in the hope of,' 'beyond hope.' 'Hopeful' and 'hopeless' are opposites. "
        "'Hopefully' as a sentence adverb ('Hopefully, it'll work') is widely accepted despite "
        "some traditionalists objecting.\n\n"
        "'Above' and 'below' are spatial opposites. Both can be prepositions ('above the clouds,' "
        "'below the surface') or adverbs ('the sky above,' 'the valley below'). "
        "'Above' in figurative use: 'above average,' 'above the law,' 'above all.' "
        "'Below' in figurative use: 'below par,' 'below the belt,' 'below freezing.' "
        "In the song, Lennon uses both as adverbs: 'above us only sky' — no preposition needed "
        "because the meaning is clear from context."
    )

    # Activity 8: reading — keep text as-is (already English), update title/description
    s0["activities"][8]["title"] = "Read: Imagine Lyrics (Part 1)"
    s0["activities"][8]["description"] = "Read the opening verse of Imagine"

    # Activity 9: speakReading
    s0["activities"][9]["title"] = "Speak: Practice the Lyrics (Part 1)"
    s0["activities"][9]["description"] = "Practice speaking the opening verse aloud"

    # Activity 10: readAlong
    s0["activities"][10]["title"] = "Listen: Imagine (Part 1)"
    s0["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s0["activities"][11]["title"] = "Write: Dreams and Possibility"
    s0["activities"][11]["description"] = "Write sentences using Session 1 vocabulary"
    ws_items_0 = s0["activities"][11]["data"]["items"]
    ws_items_0[0]["prompt"] = (
        "Use the word 'imagine' to write about picturing something that doesn't exist yet — "
        "just as John Lennon invites the listener to imagine a world without barriers. "
        "Example: She closed her eyes and tried to imagine what the city looked like a hundred years ago."
    )
    ws_items_0[1]["prompt"] = (
        "Use the word 'heaven' to write about a place of supreme happiness or the spiritual realm — "
        "as Lennon asks us to imagine a world without it, leaving only the sky above. "
        "Example: After a week of camping in the rain, a hot shower felt like absolute heaven."
    )
    ws_items_0[2]["prompt"] = (
        "Use the word 'dreamer' to describe someone with bold, idealistic visions — "
        "like Lennon calling himself a dreamer while insisting he's not the only one. "
        "Example: People called him a dreamer, but his ideas eventually changed the entire industry."
    )
    ws_items_0[3]["prompt"] = (
        "Use the word 'hope' to write about expectation and desire for something good — "
        "as the song hopes that someday the world will live as one. "
        "Example: Even in the darkest moments, she never lost hope that things would get better."
    )
    ws_items_0[4]["prompt"] = (
        "Use the word 'above' to describe something at a higher position — literally or figuratively — "
        "like the song's image of 'above us only sky.' "
        "Example: The stars above seemed close enough to touch on that clear mountain night."
    )
    ws_items_0[5]["prompt"] = (
        "Use the word 'below' to describe something at a lower position — literally or figuratively — "
        "as Lennon pairs it with 'above' to erase the idea of heaven and hell. "
        "Example: From the cliff's edge, the river below looked like a thin silver ribbon."
    )

    # ── Session 1: Group 2 — peace, religion, countries, living, join, someday ──
    s1 = content["learningSessions"][1]
    s1["title"] = "Session 2: Peace and Unity"

    # Activity 0: introAudio — session intro
    s1["activities"][0]["title"] = "Introduction to Session 2"
    s1["activities"][0]["description"] = "Recap Session 1 and introduce the theme of peace and unity"
    s1["activities"][0]["data"]["text"] = (
        "Welcome back to Session 2! In our first session, you learned 6 words from the opening "
        "of 'Imagine': imagine, heaven, dreamer, hope, above, and below. You discovered "
        "how John Lennon uses the gentlest vocabulary to launch the most radical thought experiment "
        "in pop music — asking you to erase heaven and hell from the picture and see what remains: "
        "just sky, just earth, just us.\n\n"
        "Now we're moving into the second verse, where Lennon turns his gaze from the spiritual "
        "to the political. He asks you to imagine no countries — no borders, no flags, no armies. "
        "No religion, either — not as an attack on faith, but as a question: what if the things "
        "we organize ourselves around are the very things keeping us apart? The answer he offers "
        "is disarmingly simple: people living life in peace.\n\n"
        "Today you'll learn 6 new words: peace, religion, countries, living, join, and someday. "
        "These words carry the political heart of the song — the moment where Lennon's dream "
        "expands from the personal to the global."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s1["activities"][1]["title"] = "Vocabulary Introduction: Session 2"
    s1["activities"][1]["description"] = "Learn 6 words: peace, religion, countries, living, join, someday"
    s1["activities"][1]["data"]["text"] = (
        "Let's learn 6 new vocabulary words from the second verse of 'Imagine' — "
        "the verse where John Lennon reimagines the political world.\n\n"

        "The first word is 'peace.' It's a noun meaning 'freedom from disturbance, or a state "
        "in which there is no war or fighting.' Lennon sings 'imagine all the people living life "
        "in peace' — the simplest possible vision of what the world could be. 'Peace' is one of "
        "the most loaded words in English. It can mean the absence of war ('world peace'), "
        "inner calm ('peace of mind'), or quiet ('peace and quiet'). 'Peaceful' is the adjective; "
        "'peacefully' the adverb. 'Peacekeeper,' 'peacemaker,' 'peace treaty' — the word builds "
        "compounds easily. The phrase 'rest in peace' is used for the deceased. "
        "Example: After years of conflict, the two neighbors finally found a way to live in peace.\n\n"

        "The second word is 'religion.' It's a noun meaning 'a system of faith and worship, "
        "or a pursuit or interest followed with great devotion.' Lennon asks us to imagine "
        "no religion — not to condemn belief, but to wonder whether organized systems of faith "
        "sometimes create more division than unity. 'Religion' is countable when referring to "
        "specific faiths ('the world's major religions') and uncountable as a concept ('religion "
        "and politics'). 'Religious' is the adjective; 'religiously' can mean 'devoutly' or "
        "'very regularly': 'She exercises religiously.' "
        "Example: The course explored how religion has shaped art, architecture, and music across centuries.\n\n"

        "The third word is 'countries.' It's the plural of 'country' — a nation with its own "
        "government, occupying a particular territory. Lennon asks us to imagine no countries — "
        "no borders, nothing to kill or die for. 'Country' has two main meanings: a nation "
        "('a developing country') and rural land ('the country' vs. 'the city'). "
        "'Countryside' means rural areas. 'Countryman' means a fellow citizen or a rural person. "
        "'Country music' is a genre. 'Cross-country' means across the land. "
        "Example: She had visited over thirty countries by the time she turned twenty-five.\n\n"

        "The fourth word is 'living.' It can be a noun, adjective, or present participle of 'live.' "
        "As a noun: 'make a living' (earn money), 'the living' (people who are alive). "
        "As an adjective: 'a living legend,' 'living proof.' In the song, 'living life in peace' "
        "uses 'living' as a present participle — an ongoing, continuous action. Lennon's point "
        "is that peace isn't a destination; it's a way of being. 'Living room,' 'living wage,' "
        "'living conditions' — the word appears everywhere in English. "
        "Example: She believed that living with purpose was more important than living with comfort.\n\n"

        "The fifth word is 'join.' It's a verb meaning 'to come together, to connect, or to become "
        "a member of.' Lennon hopes that someday the world will join together — that people will "
        "choose connection over separation. 'Join' is versatile: 'join a club,' 'join hands,' "
        "'join the conversation,' 'join forces.' 'Join in' means to participate: 'Everyone joined "
        "in the singing.' 'Joint' as an adjective means shared: 'a joint effort,' 'a joint account.' "
        "Example: When the entire audience joined in singing the chorus, the concert became something magical.\n\n"

        "The sixth word is 'someday.' It's an adverb meaning 'at some unspecified time in the future.' "
        "Lennon sings 'I hope someday you'll join us' — placing his dream firmly in the future, "
        "acknowledging it hasn't happened yet but refusing to give up on it. 'Someday' is always "
        "about the future and always indefinite — you don't know when. Compare with 'one day,' "
        "which can refer to past or future. 'Some day' (two words) is sometimes used interchangeably, "
        "but 'someday' (one word) is standard as an adverb. "
        "Example: Someday, she told herself, she would stand on that stage and tell her story.\n\n"

        "Your 6 new words: peace, religion, countries, living, join, someday. "
        "Combined with Session 1, you now have 12 words from 'Imagine.' "
        "Let's put them to work!"
    )

    # Activities 2-6: flashcards/vocab
    s1["activities"][2]["title"] = "Flashcards: Peace and Unity"
    s1["activities"][2]["description"] = "Learn 6 words: peace, religion, countries, living, join, someday"

    s1["activities"][3]["title"] = "Flashcards: Speak Session 2 Vocabulary"
    s1["activities"][3]["description"] = "Practice saying 6 words: peace, religion, countries, living, join, someday"

    s1["activities"][4]["title"] = "Flashcards: Recognize Session 2 Vocabulary"
    s1["activities"][4]["description"] = "Recognize 6 words: peace, religion, countries, living, join, someday"

    s1["activities"][5]["title"] = "Flashcards: Recall Session 2 Vocabulary"
    s1["activities"][5]["description"] = "Recall 6 words: peace, religion, countries, living, join, someday"

    s1["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 2"
    s1["activities"][6]["description"] = "Master 6 words: peace, religion, countries, living, join, someday"

    # Activity 7: introAudio — grammar/usage
    s1["activities"][7]["title"] = "Grammar and Usage: Session 2"
    s1["activities"][7]["description"] = "How to use Session 2 vocabulary naturally in sentences"
    s1["activities"][7]["data"]["text"] = (
        "Excellent! Let's explore how these 6 words behave in real English.\n\n"
        "'Peace' is usually uncountable — you say 'peace,' not 'a peace,' except in diplomatic "
        "contexts: 'a lasting peace,' 'a fragile peace.' Common collocations: 'at peace' (calm "
        "or dead), 'keep the peace' (maintain order), 'peace of mind' (freedom from worry), "
        "'peace offering' (a gift to end a dispute). 'Peaceful' describes a state; 'peaceable' "
        "describes a person's character.\n\n"
        "'Religion' as a countable noun: 'Christianity is a religion.' As uncountable: "
        "'the role of religion in society.' 'Religious' can mean 'relating to religion' "
        "('religious education') or 'very thorough' ('with religious attention to detail'). "
        "The phrase 'freedom of religion' is a fundamental right in many constitutions.\n\n"
        "'Countries' — 'country' is always countable. Note the plural spelling: country → countries "
        "(y → ies after a consonant). 'Country' as an adjective means rural: 'country roads,' "
        "'country life.' Don't confuse 'country' (nation) with 'county' (administrative division). "
        "'Countrywide' means across the entire nation.\n\n"
        "'Living' has rich grammar. As a gerund/present participle: 'Living alone taught her "
        "independence.' As an adjective: 'the living room,' 'a living organism.' As a noun: "
        "'earn a living,' 'the cost of living.' 'Living' vs. 'alive': 'a living creature' "
        "(adjective before noun) vs. 'the creature is alive' (adjective after verb). "
        "You can't say 'an alive creature.'\n\n"
        "'Join' is transitive: 'join the team,' 'join us.' 'Join in' is intransitive: "
        "'Everyone joined in.' 'Join up' means to enlist in the military. 'Joint' as a noun "
        "means a connection point ('a joint in the pipe') or an informal word for a place "
        "('a pizza joint'). 'Jointly' means together: 'They jointly own the property.'\n\n"
        "'Someday' vs. 'some day': 'someday' (one word) is an adverb meaning 'at an unspecified "
        "future time.' 'Some day' (two words) can mean 'a particular day': 'Pick some day next week.' "
        "In practice, they're often interchangeable. 'Someday' always looks forward — you can't "
        "say 'someday in the past.' Compare: 'one day' can be past or future."
    )

    # Activity 8-10: reading/speak/listen — keep text, update titles
    s1["activities"][8]["title"] = "Read: Imagine Lyrics (Part 2)"
    s1["activities"][8]["description"] = "Read the second verse about peace, countries, and unity"

    s1["activities"][9]["title"] = "Speak: Practice the Lyrics (Part 2)"
    s1["activities"][9]["description"] = "Practice speaking the second verse aloud"

    s1["activities"][10]["title"] = "Listen: Imagine (Part 2)"
    s1["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s1["activities"][11]["title"] = "Write: Unity and Connection"
    s1["activities"][11]["description"] = "Write sentences using Session 2 vocabulary"
    ws_items_1 = s1["activities"][11]["data"]["items"]
    ws_items_1[0]["prompt"] = (
        "Use the word 'peace' to write about calm, harmony, or the absence of conflict — "
        "like Lennon's vision of all people living life in peace. "
        "Example: After years of conflict, the two neighbors finally found a way to live in peace."
    )
    ws_items_1[1]["prompt"] = (
        "Use the word 'religion' to write about faith, belief systems, or devotion — "
        "as the song asks what would happen if religion no longer divided people. "
        "Example: The course explored how religion has shaped art, architecture, and music across centuries."
    )
    ws_items_1[2]["prompt"] = (
        "Use the word 'countries' to write about nations, borders, or global diversity — "
        "as Lennon imagines a world with no countries and nothing to kill or die for. "
        "Example: She had visited over thirty countries by the time she turned twenty-five."
    )
    ws_items_1[3]["prompt"] = (
        "Use the word 'living' to write about the way someone exists or earns their livelihood — "
        "as the song envisions people truly living, not just surviving. "
        "Example: She believed that living with purpose was more important than living with comfort."
    )
    ws_items_1[4]["prompt"] = (
        "Use the word 'join' to write about coming together or connecting with others — "
        "like Lennon's hope that someday the world will join as one. "
        "Example: When the entire audience joined in singing the chorus, the concert became something magical."
    )
    ws_items_1[5]["prompt"] = (
        "Use the word 'someday' to write about a future possibility you believe in — "
        "as Lennon places his dream in the future without giving up on it. "
        "Example: Someday, she told herself, she would stand on that stage and tell her story."
    )

    # ── Session 2: Group 3 — possessions, greed, hunger, brotherhood, sharing, wonder ──
    s2 = content["learningSessions"][2]
    s2["title"] = "Session 3: Sharing and Brotherhood"

    # Activity 0: introAudio — session intro
    s2["activities"][0]["title"] = "Introduction to Session 3"
    s2["activities"][0]["description"] = "Recap Sessions 1-2 and introduce the themes of sharing and brotherhood"
    s2["activities"][0]["data"]["text"] = (
        "Welcome to Session 3 — the final learning session before your review! "
        "So far you've learned 12 words from 'Imagine.' In Session 1, you met "
        "imagine, heaven, dreamer, hope, above, and below — the words of the song's opening, "
        "where John Lennon asks you to erase heaven and hell and see what's left: just sky, "
        "just earth, just the present moment. "
        "In Session 2, you learned peace, religion, countries, living, join, and someday — "
        "the words of the song's political verse, where Lennon strips away borders and belief "
        "systems and finds that what remains is people living life in peace.\n\n"
        "Now we reach the song's final verse — and its most personal challenge. Lennon turns "
        "from the spiritual and the political to the economic. He asks you to imagine no "
        "possessions — no greed, no hunger, just a brotherhood of man sharing all the world. "
        "This is where the song stops being a gentle daydream and becomes a direct confrontation "
        "with how we organize our lives.\n\n"
        "Your final 6 words: possessions, greed, hunger, brotherhood, sharing, and wonder. "
        "By the end of this session, you'll have all 18 vocabulary words — and you'll hear "
        "'Imagine' the way John Lennon intended it to be heard."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s2["activities"][1]["title"] = "Vocabulary Introduction: Session 3"
    s2["activities"][1]["description"] = "Learn 6 words: possessions, greed, hunger, brotherhood, sharing, wonder"
    s2["activities"][1]["data"]["text"] = (
        "Here are your final 6 vocabulary words, drawn from the most challenging verse "
        "of 'Imagine.'\n\n"

        "The first word is 'possessions.' It's the plural of 'possession' — a noun meaning "
        "'something that belongs to you, something you own.' Lennon asks us to imagine no "
        "possessions — a world where ownership doesn't define identity or create inequality. "
        "This is perhaps the most radical line in the song. 'Possession' can also mean 'the state "
        "of having or owning something': 'in possession of a weapon,' 'take possession of a house.' "
        "In a supernatural context, 'possession' means being controlled by a spirit. "
        "'Possessive' as an adjective means unwilling to share, or in grammar, showing ownership "
        "('John's' is a possessive form). "
        "Example: After the fire, she realized that her most valuable possessions were the memories, not the things.\n\n"

        "The second word is 'greed.' It's a noun meaning 'an intense and selfish desire for "
        "something, especially wealth, power, or food.' Lennon names greed as one of the forces "
        "that would vanish in his imagined world — the engine of inequality. 'Greed' is always "
        "negative. 'Greedy' is the adjective: 'a greedy landlord,' 'greedy for power.' "
        "'Greedily' is the adverb. The phrase 'greed is good' became famous from the movie "
        "'Wall Street' — used ironically to critique capitalism. "
        "Example: The company's downfall wasn't caused by bad luck — it was caused by unchecked greed at the top.\n\n"

        "The third word is 'hunger.' It's a noun meaning 'a feeling of discomfort caused by lack "
        "of food, or a strong desire for something.' Lennon pairs 'no need for greed or hunger' — "
        "in his imagined world, nobody goes without. 'Hunger' has both literal and figurative uses: "
        "'world hunger' (famine), 'a hunger for knowledge' (strong desire). 'Hungry' is the "
        "adjective; 'hungrily' the adverb. 'Hunger strike' is a protest by refusing to eat. "
        "'Hunger pangs' are the physical sensations of being very hungry. "
        "Example: Her hunger for learning drove her to read three books a week, even during the busiest months.\n\n"

        "The fourth word is 'brotherhood.' It's a noun meaning 'the relationship between brothers, "
        "or a feeling of kinship and solidarity among all people.' Lennon sings about 'a brotherhood "
        "of man' — humanity united as one family. 'Brotherhood' is one of those words that carries "
        "enormous emotional weight. It implies equality, mutual support, and shared identity. "
        "'Brother' is the root; 'brotherly' is the adjective: 'brotherly love.' "
        "The word is traditionally gendered, and modern usage sometimes prefers 'solidarity' or "
        "'community,' but 'brotherhood' retains its poetic power. "
        "Example: The soldiers spoke of a brotherhood forged not by blood but by shared hardship.\n\n"

        "The fifth word is 'sharing.' It's the present participle of 'share,' used as a noun "
        "or adjective meaning 'giving a portion of something to others.' Lennon's vision is "
        "a world where people share everything — 'sharing all the world.' 'Share' as a verb: "
        "'share a meal,' 'share an idea,' 'share a room.' As a noun: 'your fair share,' "
        "'market share.' 'Sharing' as a gerund: 'Sharing is caring' (a common saying). "
        "'Shareholder' is someone who owns stock in a company. "
        "Example: The best conversations happen when both people are willing to do the sharing, not just the talking.\n\n"

        "The sixth and final word is 'wonder.' It can be a noun or a verb. As a noun, it means "
        "'a feeling of amazement and admiration' or 'something remarkable': 'the seven wonders "
        "of the world.' As a verb, it means 'to feel curious' or 'to think about something': "
        "'I wonder what he meant.' Lennon asks 'I wonder if you can' — gently challenging the "
        "listener to try imagining his vision. 'Wonderful' means extremely good; 'wonderfully' "
        "is the adverb. 'No wonder' means 'it's not surprising': 'No wonder she's tired.' "
        "Example: She stood at the edge of the canyon, filled with a sense of wonder at the sheer scale of it.\n\n"

        "And there you have it — all 18 words: imagine, heaven, dreamer, hope, above, below, "
        "peace, religion, countries, living, join, someday, possessions, greed, hunger, "
        "brotherhood, sharing, and wonder. You now have the complete vocabulary of 'Imagine.' "
        "Let's practice these final 6!"
    )

    # Activities 2-6: flashcards/vocab
    s2["activities"][2]["title"] = "Flashcards: Sharing and Brotherhood"
    s2["activities"][2]["description"] = "Learn 6 words: possessions, greed, hunger, brotherhood, sharing, wonder"

    s2["activities"][3]["title"] = "Flashcards: Speak Session 3 Vocabulary"
    s2["activities"][3]["description"] = "Practice saying 6 words: possessions, greed, hunger, brotherhood, sharing, wonder"

    s2["activities"][4]["title"] = "Flashcards: Recognize Session 3 Vocabulary"
    s2["activities"][4]["description"] = "Recognize 6 words: possessions, greed, hunger, brotherhood, sharing, wonder"

    s2["activities"][5]["title"] = "Flashcards: Recall Session 3 Vocabulary"
    s2["activities"][5]["description"] = "Recall 6 words: possessions, greed, hunger, brotherhood, sharing, wonder"

    s2["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 3"
    s2["activities"][6]["description"] = "Master 6 words: possessions, greed, hunger, brotherhood, sharing, wonder"

    # Activity 7: introAudio — grammar/usage
    s2["activities"][7]["title"] = "Grammar and Usage: Session 3"
    s2["activities"][7]["description"] = "How to use Session 3 vocabulary naturally in sentences"
    s2["activities"][7]["data"]["text"] = (
        "Let's look at how these final 6 words work in English grammar.\n\n"
        "'Possessions' — 'possession' is countable when it means 'a thing you own': "
        "'personal possessions,' 'worldly possessions.' It's uncountable when it means "
        "'the state of owning': 'in possession of,' 'take possession.' "
        "The verb 'possess' is formal: 'She possesses great talent.' "
        "'Possessive' in grammar refers to forms showing ownership: 'my,' 'your,' 'John's.' "
        "In relationships, 'possessive' means jealously controlling.\n\n"
        "'Greed' is an uncountable noun — you can't say 'a greed' or 'greeds.' "
        "It's always 'greed,' 'pure greed,' 'corporate greed.' "
        "'Greedy' is the adjective: 'greedy for power,' 'a greedy child.' "
        "The phrase 'greed knows no bounds' means greed has no limits. "
        "'Greediness' is a less common noun form.\n\n"
        "'Hunger' is usually uncountable: 'hunger is a global problem,' 'die of hunger.' "
        "But it can be countable in figurative use: 'a hunger for success.' "
        "The verb 'hunger' is literary: 'She hungered for freedom.' "
        "More commonly, 'hungry' is used: 'I'm hungry,' 'hungry for change.' "
        "'Hunger' vs. 'famine': hunger is the feeling or condition; famine is a widespread "
        "shortage of food.\n\n"
        "'Brotherhood' is usually uncountable when it means 'the bond between people': "
        "'a sense of brotherhood.' It's countable when it means 'an organization': "
        "'a brotherhood of firefighters.' The adjective 'brotherly' modifies nouns: "
        "'brotherly love,' 'brotherly advice.' 'Sisterhood' is the female equivalent. "
        "'Sibling' is the gender-neutral term for brother or sister.\n\n"
        "'Sharing' as a gerund can be the subject of a sentence: 'Sharing is caring.' "
        "As a present participle: 'They were sharing a pizza.' 'Share' takes a direct object "
        "and often 'with': 'Share this with your friends.' 'Share in' means to participate: "
        "'Share in the profits.' 'Shared' as an adjective: 'a shared experience,' "
        "'shared responsibility.'\n\n"
        "'Wonder' as a verb takes a clause: 'I wonder if she's coming,' 'I wonder why he left.' "
        "Never 'I wonder that' — use 'if' or a question word. As a noun: 'a sense of wonder,' "
        "'the wonders of nature,' 'it's a wonder he survived.' 'Wonderful' is one of the most "
        "common positive adjectives in English. 'Wonderland' means an imaginary beautiful place. "
        "'Wondrous' is a literary synonym for 'wonderful.'"
    )

    # Activity 8-10: reading/speak/listen
    s2["activities"][8]["title"] = "Read: Imagine Lyrics (Part 3)"
    s2["activities"][8]["description"] = "Read the final verse about possessions, brotherhood, and sharing"

    s2["activities"][9]["title"] = "Speak: Practice the Lyrics (Part 3)"
    s2["activities"][9]["description"] = "Practice speaking the final verse aloud"

    s2["activities"][10]["title"] = "Listen: Imagine (Part 3)"
    s2["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s2["activities"][11]["title"] = "Write: Brotherhood and Sharing"
    s2["activities"][11]["description"] = "Write sentences using Session 3 vocabulary"
    ws_items_2 = s2["activities"][11]["data"]["items"]
    ws_items_2[0]["prompt"] = (
        "Use the word 'possessions' to write about things people own — or the idea of letting go of them — "
        "like Lennon's challenge to imagine a world with no possessions at all. "
        "Example: After the fire, she realized that her most valuable possessions were the memories, not the things."
    )
    ws_items_2[1]["prompt"] = (
        "Use the word 'greed' to write about selfish desire for more than one needs — "
        "as the song names greed as a force that would vanish in a world of true sharing. "
        "Example: The company's downfall wasn't caused by bad luck — it was caused by unchecked greed at the top."
    )
    ws_items_2[2]["prompt"] = (
        "Use the word 'hunger' to write about physical need or a deep desire for something — "
        "as Lennon dreams of a world where no one goes hungry. "
        "Example: Her hunger for learning drove her to read three books a week, even during the busiest months."
    )
    ws_items_2[3]["prompt"] = (
        "Use the word 'brotherhood' to write about solidarity, kinship, or shared humanity — "
        "like Lennon's vision of a brotherhood of man sharing all the world. "
        "Example: The soldiers spoke of a brotherhood forged not by blood but by shared hardship."
    )
    ws_items_2[4]["prompt"] = (
        "Use the word 'sharing' to write about giving a portion of something to others — "
        "as the song envisions people sharing all the world instead of hoarding it. "
        "Example: The best conversations happen when both people are willing to do the sharing, not just the talking."
    )
    ws_items_2[5]["prompt"] = (
        "Use the word 'wonder' to write about curiosity, amazement, or something remarkable — "
        "like Lennon's gentle challenge: 'I wonder if you can.' "
        "Example: She stood at the edge of the canyon, filled with a sense of wonder at the sheer scale of it."
    )

    # ── Session 3: Review (4 activities) ──
    s3 = content["learningSessions"][3]
    s3["title"] = "Review"

    s3["activities"][0]["title"] = "Congratulations and Review"
    s3["activities"][0]["description"] = "Celebrate your progress and prepare for the full review"
    s3["activities"][0]["data"]["text"] = (
        "Congratulations! You've learned all 18 vocabulary words from 'Imagine.' "
        "Let's take a moment to look back at what you've accomplished.\n\n"
        "In Session 1, you learned imagine, heaven, dreamer, hope, above, and below — "
        "the words of the song's opening verse, where John Lennon asks you to erase the "
        "boundaries between heaven and earth and see the world as it simply is.\n\n"
        "In Session 2, you learned peace, religion, countries, living, join, and someday — "
        "the words of the song's political verse, where Lennon strips away borders and belief "
        "systems and finds that what remains is people living life in peace.\n\n"
        "In Session 3, you learned possessions, greed, hunger, brotherhood, sharing, and wonder — "
        "the words of the song's most radical verse, where Lennon challenges us to imagine "
        "a world without ownership, where humanity shares everything as one family.\n\n"
        "Now it's time to review all 18 words together. This review session will test your "
        "recognition and recall across all three groups. After this, you'll be ready to read "
        "the complete lyrics in the final session. Let's go!"
    )

    s3["activities"][1]["title"] = "Flashcards: Review All 18 Words"
    s3["activities"][1]["description"] = "Review all 18 vocabulary words from Imagine"

    s3["activities"][2]["title"] = "Flashcards: Recognize All Vocabulary"
    s3["activities"][2]["description"] = "Test your recognition of all 18 words"

    s3["activities"][3]["title"] = "Flashcards: Recall All Vocabulary"
    s3["activities"][3]["description"] = "Test your recall of all 18 words"

    # ── Session 4: Full reading + farewell (5 activities) ──
    s4 = content["learningSessions"][4]
    s4["title"] = "Full Lyrics Reading"

    s4["activities"][0]["title"] = "Introduction to the Complete Reading"
    s4["activities"][0]["description"] = "Prepare for reading the full Imagine lyrics"
    s4["activities"][0]["data"]["text"] = (
        "Welcome to the final session! This is the moment everything comes together. "
        "Over the past three sessions, you've built a vocabulary of 18 words drawn directly "
        "from the lyrics of 'Imagine.' You've learned their meanings, practiced their "
        "pronunciation, explored their grammar, and used them in your own writing.\n\n"
        "Now you're going to read the complete lyrics — all three verses combined into one "
        "continuous passage. As you read, you'll encounter every single one of your 18 words "
        "in context. This time, they won't be new — they'll be familiar friends.\n\n"
        "Here are all 18 words you'll see: imagine, heaven, dreamer, hope, above, below, "
        "peace, religion, countries, living, join, someday, possessions, greed, hunger, "
        "brotherhood, sharing, and wonder.\n\n"
        "Take your time with the reading. Let Lennon's voice come through the words. "
        "And remember — you may say he's a dreamer, but he's not the only one."
    )

    s4["activities"][1]["title"] = "Read: Complete Imagine Lyrics"
    s4["activities"][1]["description"] = "Read the full lyrics from beginning to end"

    s4["activities"][2]["title"] = "Speak: Practice the Complete Lyrics"
    s4["activities"][2]["description"] = "Practice speaking the entire lyrics aloud"

    s4["activities"][3]["title"] = "Listen: Complete Imagine"
    s4["activities"][3]["description"] = "Listen to the complete lyrics and follow along"

    s4["activities"][4]["title"] = "Farewell and Vocabulary Review"
    s4["activities"][4]["description"] = "Final review of all 18 words and farewell"
    s4["activities"][4]["data"]["text"] = (
        "You've done it — you've completed the entire 'Imagine' vocabulary course! "
        "Let's do one final review of all 18 words before we say goodbye.\n\n"

        "'Imagine' — to form a mental image of something not present or not yet real. "
        "Example: Close your eyes and imagine a world where every child has enough to eat.\n\n"
        "'Heaven' — the abode of God and the angels, or a place of supreme happiness. "
        "Example: The smell of fresh bread baking on a Sunday morning — that's my idea of heaven.\n\n"
        "'Dreamer' — a person who dreams, or who has bold, idealistic visions. "
        "Example: Every great invention started in the mind of a dreamer who refused to accept 'impossible.'\n\n"
        "'Hope' — a feeling of expectation and desire for something good to happen. "
        "Example: He planted a tree in the backyard — a small act of hope for a future he might never see.\n\n"
        "'Above' — at a higher level or position, literally or figuratively. "
        "Example: Above the noise of the city, she could hear a single bird singing.\n\n"
        "'Below' — at a lower level or position, literally or figuratively. "
        "Example: The temperature dropped below freezing, and the puddles turned to glass overnight.\n\n"

        "'Peace' — freedom from disturbance, or a state without war or fighting. "
        "Example: The old man sat by the lake in perfect peace, watching the water catch the last light.\n\n"
        "'Religion' — a system of faith and worship, or a pursuit followed with great devotion. "
        "Example: For her, gardening was almost a religion — she tended her plants with sacred attention.\n\n"
        "'Countries' — nations with their own governments, occupying particular territories. "
        "Example: The festival brought together musicians from twelve different countries, all playing on the same stage.\n\n"
        "'Living' — the way someone exists; being alive; earning a livelihood. "
        "Example: He made a modest living as a carpenter, but his real wealth was in the friendships he built.\n\n"
        "'Join' — to come together, to connect, or to become a member of something. "
        "Example: One by one, the neighbors joined the effort to rebuild the playground after the storm.\n\n"
        "'Someday' — at some unspecified time in the future. "
        "Example: Someday this will all make sense — but right now, just keep going.\n\n"

        "'Possessions' — things that belong to you; things you own. "
        "Example: He packed his few possessions into a single suitcase and started a new life across the ocean.\n\n"
        "'Greed' — an intense and selfish desire for more than one needs. "
        "Example: It wasn't ambition that destroyed him — it was greed disguised as ambition.\n\n"
        "'Hunger' — a feeling caused by lack of food, or a strong desire for something. "
        "Example: The hunger in her eyes wasn't for food — it was for a chance to prove herself.\n\n"
        "'Brotherhood' — the relationship between brothers, or solidarity among all people. "
        "Example: In that moment of crisis, strangers became family — a brotherhood born of shared survival.\n\n"
        "'Sharing' — giving a portion of something to others. "
        "Example: The secret to a good friendship isn't perfection — it's the willingness to keep sharing the truth.\n\n"
        "'Wonder' — a feeling of amazement, or to feel curious about something. "
        "Example: Children never lose their sense of wonder — they just need adults who don't crush it.\n\n"

        "Thank you for learning with John Lennon's 'Imagine.' "
        "You came for 18 vocabulary words, but I hope you're leaving with something more — "
        "a reminder that the simplest words, arranged with care, can hold an entire philosophy. "
        "Lennon didn't need complex language to challenge the world. He needed 'imagine,' "
        "'peace,' 'sharing,' and 'wonder' — and he trusted that the listener would do the rest. "
        "Keep reading, keep speaking, keep writing — and keep imagining. "
        "The dreamers are never really alone. Goodbye, and carry the music with you!"
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
    print(f"Created en-en Imagine curriculum: {cid}")
    return cid


if __name__ == "__main__":
    create()
