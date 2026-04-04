"""
Create en-en song curriculum #0: Heal the World
Mirror of vi-en source qVv18hr5L4sTQs6i — all Vietnamese UI text rewritten in English.

Source song: Heal the World by Michael Jackson (1991)
YouTube: https://www.youtube.com/watch?v=nhcG9wqn0gU

18 vocabulary words in 3 groups of 6 (same as vi-en source):
  Group 1: heal, brighter, sorrow, entire, care, space
  Group 2: bliss, dread, joyful, grace, reveal, existing
  Group 3: spirits, fear, create, nations, plain, heavenly

All user-facing text in English. Reading passages stay as-is (already English).
Vocabulary words stay as-is (already English).

Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 9.1, 9.2, 9.3, 9.4, 9.5
"""

import sys, json, requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"
SOURCE_ID = "qVv18hr5L4sTQs6i"

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
    content["title"] = "'Heal the World' — Michael Jackson"

    content["description"] = (
        "WHAT IF ONE SONG COULD ACTUALLY CHANGE THE WAY YOU SEE THE WORLD?\n\n"
        "There are melodies that bypass your brain and go straight to your chest — "
        "songs that make you feel something before you even understand the words. "
        "'Heal the World' is one of those songs. Michael Jackson wrote it in 1991 "
        "as a plea to humanity: stop the suffering, hold each other closer, and "
        "remember that every single person has the power to make things better. "
        "From a child in a war zone to a grandmother humming in her kitchen, "
        "the message lands the same way — because compassion doesn't need a translator.\n\n"
        "Now imagine not just feeling the song, but UNDERSTANDING every word Michael sings — "
        "from 'sorrow' when he names the pain the world carries, "
        "to 'grace' when he describes the beauty that emerges when people choose kindness, "
        "to 'heal' when he asks you to do the one thing that matters most. "
        "Each vocabulary word is a window into the emotional architecture of the lyrics.\n\n"
        "When you realize that 'plain' in 'it's plain to see' doesn't mean 'boring' "
        "but 'obvious and clear' — you start hearing English the way songwriters intend it. "
        "That's the moment music becomes your most powerful language teacher.\n\n"
        "18 vocabulary words drawn directly from the lyrics, combined with "
        "a multi-sensory learning method — listening, reading, speaking, writing — "
        "so you sharpen your English while carrying Michael Jackson's message of "
        "compassion, healing, and hope in your heart."
    )

    content["preview"] = {
        "text": (
            "Have you ever listened to 'Heal the World' and felt like the entire planet "
            "was wrapping its arms around you? Michael Jackson wrote this song as a love letter "
            "to humanity — and now you'll learn English through the very words he chose.\n\n"
            "18 English vocabulary words you'll learn: heal, brighter, sorrow, entire, care, "
            "space, bliss, dread, joyful, grace, reveal, existing, spirits, fear, create, "
            "nations, plain, heavenly.\n\n"
            "Across 5 sessions you'll read the actual lyrics, discover how Michael uses "
            "the simplest words to express the deepest truths — from the sorrow that weighs "
            "on the world to the heavenly vision of what it could become.\n\n"
            "Tap the link below to watch the original music video — after this course, "
            "you'll hear Michael sing and understand every single word naturally."
        )
    }

    content["contentTypeTags"] = ["music"]
    content["is_public"] = False

    # ── Session 0: Group 1 — heal, brighter, sorrow, entire, care, space ──
    s0 = content["learningSessions"][0]
    s0["title"] = "Session 1: Healing and Love — Heal the World"

    # Activity 0: introAudio — song intro
    s0["activities"][0]["title"] = "Introduction to the Song"
    s0["activities"][0]["description"] = "Setting the stage for Michael Jackson's anthem of compassion"
    s0["activities"][0]["data"]["text"] = (
        "Welcome to the vocabulary-through-music course! Today we begin with one of "
        "the most emotionally powerful songs ever recorded — 'Heal the World' by Michael Jackson. "
        "Released in 1991 as part of the 'Dangerous' album, this song became an anthem for "
        "humanitarian causes around the globe. Michael Jackson didn't just sing it — he founded "
        "the Heal the World Foundation, dedicated to improving the lives of children everywhere.\n\n"
        "The song opens with a children's choir and builds into a sweeping orchestral arrangement "
        "that feels like a prayer set to music. The lyrics are deceptively simple — words like "
        "'heal,' 'care,' and 'brighter' — but strung together they create something that moves "
        "millions of people to tears. The message is universal: the world is broken, but love "
        "can fix it, and the fixing starts with you.\n\n"
        "In this first session, you'll learn 6 vocabulary words that appear in the opening verses "
        "of the song: heal, brighter, sorrow, entire, care, and space. Each word carries the "
        "emotional weight of Michael's plea — and by the end of this session you'll hear them "
        "not as isolated dictionary entries, but as pieces of a vision for a kinder, gentler world."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s0["activities"][1]["title"] = "Vocabulary Introduction: Session 1"
    s0["activities"][1]["description"] = "Learn 6 words: heal, brighter, sorrow, entire, care, space"
    s0["activities"][1]["data"]["text"] = (
        "Let's dive into the first 6 vocabulary words from 'Heal the World.' "
        "Each word comes straight from Michael Jackson's lyrics, and understanding how he uses them "
        "will change the way you hear this song — and English — forever.\n\n"

        "The first word is 'heal.' It's a verb meaning 'to make whole or sound again, to restore "
        "to health.' In the song's title and chorus, Michael sings 'Heal the world, make it a better "
        "place' — using 'heal' not for a physical wound but for the brokenness of humanity itself. "
        "This metaphorical use is powerful: you can heal a relationship, heal a community, heal "
        "a divided nation. The word can also be intransitive: 'The wound healed slowly.' "
        "Related forms: 'healing' (noun/adjective), 'healer' (noun). "
        "Example: Music has the power to heal wounds that medicine cannot reach.\n\n"

        "The second word is 'brighter.' It's the comparative form of 'bright,' meaning 'more "
        "luminous, more vivid, or more hopeful.' Michael sings about making the world a brighter "
        "place — not literally adding more light, but filling it with more hope and joy. "
        "'Bright' has both physical and figurative meanings: a bright room (well-lit), a bright "
        "student (intelligent), a bright future (promising). The comparative 'brighter' implies "
        "improvement — things are getting better. 'Brighten' is the verb form: 'Her smile "
        "brightened the room.' "
        "Example: Every small act of kindness makes someone's day a little brighter.\n\n"

        "The third word is 'sorrow.' It's a noun meaning 'deep distress, sadness, or grief.' "
        "Michael acknowledges that the world is full of sorrow — pain, loss, injustice — "
        "but he doesn't stop there. He uses sorrow as the starting point for healing. "
        "The word carries more weight than 'sadness' — it implies a deeper, more lasting pain. "
        "'Sorrow' is often literary or poetic: 'a life marked by sorrow,' 'to drown one's sorrows.' "
        "The adjective form is 'sorrowful.' "
        "Example: Behind her smile, there was a sorrow that only those closest to her could see.\n\n"

        "The fourth word is 'entire.' It's an adjective meaning 'whole, complete, with nothing "
        "missing.' Michael sings about the entire human race — every person on the planet, "
        "no exceptions. 'Entire' is stronger than 'whole' in many contexts because it emphasizes "
        "completeness: 'the entire population,' 'the entire album,' 'the entire afternoon.' "
        "The adverb form is 'entirely': 'That's entirely up to you.' "
        "Example: She read the entire book in one sitting, unable to put it down.\n\n"

        "The fifth word is 'care.' It can be a verb or a noun. As a verb, it means 'to feel "
        "concern or interest' — 'I care about you.' As a noun, it means 'the provision of what "
        "is needed for well-being' — 'medical care,' 'take care.' In the song, caring is the "
        "antidote to the world's pain. Michael's message is simple: if enough people care, "
        "the world heals. Common phrases: 'take care of,' 'care for,' 'couldn't care less,' "
        "'handle with care.' "
        "Example: The difference between a good teacher and a great one is how much they genuinely care.\n\n"

        "The sixth word is 'space.' It's a noun with multiple meanings: 'an area or expanse,' "
        "'outer space,' or 'room to exist and breathe.' In the lyrics, Michael asks us to make "
        "a little space — to create room in our hearts and in the world for love and understanding. "
        "This figurative use is common: 'Give me some space,' 'a safe space,' 'personal space.' "
        "The word can also be a verb: 'Space the chairs evenly.' "
        "Example: Sometimes the kindest thing you can do for someone is give them the space to figure things out.\n\n"

        "Your first 6 words: heal, brighter, sorrow, entire, care, and space. "
        "Each one is woven into the fabric of Michael Jackson's plea for a better world. "
        "Let's practice them now!"
    )

    # Activities 2-6: flashcards/vocab — update titles and descriptions
    s0["activities"][2]["title"] = "Flashcards: Healing and Love"
    s0["activities"][2]["description"] = "Learn 6 words: heal, brighter, sorrow, entire, care, space"

    s0["activities"][3]["title"] = "Flashcards: Speak Session 1 Vocabulary"
    s0["activities"][3]["description"] = "Practice saying 6 words: heal, brighter, sorrow, entire, care, space"

    s0["activities"][4]["title"] = "Flashcards: Recognize Session 1 Vocabulary"
    s0["activities"][4]["description"] = "Recognize 6 words: heal, brighter, sorrow, entire, care, space"

    s0["activities"][5]["title"] = "Flashcards: Recall Session 1 Vocabulary"
    s0["activities"][5]["description"] = "Recall 6 words: heal, brighter, sorrow, entire, care, space"

    s0["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 1"
    s0["activities"][6]["description"] = "Master 6 words: heal, brighter, sorrow, entire, care, space"

    # Activity 7: introAudio — grammar/usage
    s0["activities"][7]["title"] = "Grammar and Usage: Session 1"
    s0["activities"][7]["description"] = "How to use Session 1 vocabulary naturally in sentences"
    s0["activities"][7]["data"]["text"] = (
        "Great work! You've met your first 6 words. Now let's look at how they work "
        "in real English sentences, using the lyrics of 'Heal the World' as our guide.\n\n"
        "'Heal' is a regular verb: heal, healed, healed. It can be transitive ('heal the world,' "
        "'heal a wound') or intransitive ('the cut healed quickly'). The noun 'healing' is often "
        "used as an adjective: 'a healing process,' 'healing music.' 'Healer' refers to a person "
        "who heals. In the song, 'heal' is used as a transitive verb with 'the world' as its object — "
        "a bold, metaphorical command.\n\n"
        "'Brighter' is the comparative of 'bright.' Comparatives follow the pattern: "
        "one-syllable adjectives add '-er' (bright → brighter), while longer adjectives use 'more' "
        "(beautiful → more beautiful). 'Bright' is versatile: 'bright light,' 'bright idea,' "
        "'bright future.' The superlative is 'brightest.' 'Brighten up' is a phrasal verb meaning "
        "'to become or make more cheerful.'\n\n"
        "'Sorrow' is primarily a noun, but it can also be a literary verb: 'She sorrowed for her lost child.' "
        "Common collocations: 'deep sorrow,' 'express sorrow,' 'drown one's sorrows' (drink to forget). "
        "The adjective 'sorrowful' and adverb 'sorrowfully' are more formal. "
        "In everyday speech, 'sadness' or 'grief' are more common, but 'sorrow' carries a poetic weight "
        "that makes it perfect for song lyrics.\n\n"
        "'Entire' always comes before the noun it modifies: 'the entire world,' never 'the world entire' "
        "(except in poetry). It's synonymous with 'whole' but slightly more emphatic. "
        "'Entirely' as an adverb: 'I entirely agree,' 'That's entirely different.' "
        "Don't confuse 'entire' with 'total' — 'entire' emphasizes completeness, "
        "'total' emphasizes sum or amount.\n\n"
        "'Care' has rich grammar. As a verb: 'I care about you' (concern), 'I don't care' (indifference). "
        "'Care for' has two meanings: 'to look after' ('She cares for her elderly mother') and "
        "'to like' ('I don't care for spicy food'). As a noun: 'take care,' 'health care,' "
        "'with care.' 'Careful' (adjective), 'carefully' (adverb), 'careless' (adjective).\n\n"
        "'Space' is both countable and uncountable. Uncountable: 'There isn't enough space' (room). "
        "Countable: 'a parking space,' 'blank spaces.' 'Outer space' is always uncountable. "
        "As a verb: 'Space the plants two feet apart.' 'Spacious' means 'having a lot of space.' "
        "In the song, 'space' is used figuratively — emotional room for love to grow."
    )

    # Activity 8: reading — keep text as-is (already English), update title/description
    s0["activities"][8]["title"] = "Read: Heal the World Lyrics (Part 1)"
    s0["activities"][8]["description"] = "Read the opening verses of Heal the World"

    # Activity 9: speakReading
    s0["activities"][9]["title"] = "Speak: Practice the Lyrics (Part 1)"
    s0["activities"][9]["description"] = "Practice speaking the opening verses aloud"

    # Activity 10: readAlong
    s0["activities"][10]["title"] = "Listen: Heal the World (Part 1)"
    s0["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s0["activities"][11]["title"] = "Write: Love and Compassion"
    s0["activities"][11]["description"] = "Write sentences using Session 1 vocabulary"
    ws_items_0 = s0["activities"][11]["data"]["items"]
    ws_items_0[0]["prompt"] = (
        "Use the word 'heal' to write about restoring something broken — "
        "just as Michael Jackson calls on the world to heal itself through love. "
        "Example: Music has the power to heal wounds that medicine cannot reach."
    )
    ws_items_0[1]["prompt"] = (
        "Use the word 'brighter' to describe something becoming more hopeful or luminous — "
        "like the song's vision of a world made brighter by compassion. "
        "Example: Every small act of kindness makes someone's day a little brighter."
    )
    ws_items_0[2]["prompt"] = (
        "Use the word 'sorrow' to write about deep sadness or grief — "
        "as Michael acknowledges the sorrow in the world before offering hope. "
        "Example: Behind her smile, there was a sorrow that only those closest to her could see."
    )
    ws_items_0[3]["prompt"] = (
        "Use the word 'entire' to emphasize completeness or wholeness — "
        "the way the song speaks to the entire human race without exception. "
        "Example: She read the entire book in one sitting, unable to put it down."
    )
    ws_items_0[4]["prompt"] = (
        "Use the word 'care' to write about concern, compassion, or looking after someone — "
        "as the song's core message is that caring is the first step toward healing. "
        "Example: The difference between a good teacher and a great one is how much they genuinely care."
    )
    ws_items_0[5]["prompt"] = (
        "Use the word 'space' to write about room — physical or emotional — "
        "like the song's call to make a little space in your heart for love. "
        "Example: Sometimes the kindest thing you can do for someone is give them the space to figure things out."
    )

    # ── Session 1: Group 2 — bliss, dread, joyful, grace, reveal, existing ──
    s1 = content["learningSessions"][1]
    s1["title"] = "Session 2: Bliss and Grace"

    # Activity 0: introAudio — session intro
    s1["activities"][0]["title"] = "Introduction to Session 2"
    s1["activities"][0]["description"] = "Recap Session 1 and introduce the theme of joy and revelation"
    s1["activities"][0]["data"]["text"] = (
        "Welcome back to Session 2! In our first session, you learned 6 words from the opening "
        "of 'Heal the World': heal, brighter, sorrow, entire, care, and space. You discovered "
        "how Michael Jackson uses the simplest vocabulary to build a vision of a world transformed "
        "by compassion — where healing begins with caring, and even the deepest sorrow can give way "
        "to something brighter.\n\n"
        "Now we're moving into the heart of the song. In these verses, Michael shifts from naming "
        "the world's pain to imagining its cure. He sings about bliss — pure, uncomplicated happiness. "
        "He sings about grace — the effortless beauty that appears when people choose love over fear. "
        "And he asks a question that echoes through the entire song: are we truly living, or merely "
        "existing?\n\n"
        "Today you'll learn 6 new words: bliss, dread, joyful, grace, reveal, and existing. "
        "These words carry the emotional arc of the song's middle section — the moment where "
        "sorrow begins to transform into hope."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s1["activities"][1]["title"] = "Vocabulary Introduction: Session 2"
    s1["activities"][1]["description"] = "Learn 6 words: bliss, dread, joyful, grace, reveal, existing"
    s1["activities"][1]["data"]["text"] = (
        "Let's learn 6 new vocabulary words from the heart of 'Heal the World' — "
        "the verses where Michael Jackson imagines what the world could become.\n\n"

        "The first word is 'bliss.' It's a noun meaning 'supreme happiness, utter joy.' "
        "Michael sings about a world where bliss replaces suffering — a state of happiness "
        "so complete that nothing is missing. 'Bliss' is stronger than 'happiness' — it implies "
        "a transcendent, almost spiritual joy. The phrase 'ignorance is bliss' means that not "
        "knowing about problems can make you happier. 'Blissful' is the adjective form: "
        "'a blissful afternoon,' 'blissfully unaware.' "
        "Example: Watching the sunset from the mountaintop, she felt a moment of pure bliss.\n\n"

        "The second word is 'dread.' It can be a noun or a verb. As a noun, it means 'great fear "
        "or apprehension' — a heavy, anticipatory fear of something terrible. As a verb: "
        "'I dread Monday mornings.' In the song, Michael contrasts bliss with dread — "
        "in a world of true happiness, there would be no dread. The adjective 'dreadful' means "
        "'extremely bad or serious': 'dreadful weather,' 'a dreadful mistake.' "
        "'Dreaded' means 'feared': 'the dreaded exam.' "
        "Example: He felt a growing sense of dread as the storm clouds gathered on the horizon.\n\n"

        "The third word is 'joyful.' It's an adjective meaning 'feeling, expressing, or causing "
        "great pleasure and happiness.' Michael describes a joyful world — one where giving "
        "brings more happiness than taking. 'Joyful' is warmer and more expressive than 'happy.' "
        "It suggests an outward, radiant kind of happiness. Related words: 'joy' (noun), "
        "'joyfully' (adverb), 'joyous' (adjective, slightly more formal). "
        "'A joyful noise,' 'joyful tears,' 'a joyful reunion.' "
        "Example: The children's joyful laughter echoed through the empty hallways of the old school.\n\n"

        "The fourth word is 'grace.' It's a noun with several meanings: 'elegance of movement,' "
        "'courteous goodwill,' or 'divine favor.' In the song, Michael uses 'grace' in its most "
        "spiritual sense — the unearned beauty and kindness that flows when people open their hearts. "
        "'Grace' can also be a verb: 'She graced us with her presence.' "
        "Common phrases: 'saving grace' (a redeeming quality), 'grace period' (extra time allowed), "
        "'with grace' (elegantly), 'say grace' (pray before a meal). "
        "Example: She handled the criticism with such grace that even her harshest critics were impressed.\n\n"

        "The fifth word is 'reveal.' It's a verb meaning 'to make known something previously hidden.' "
        "In the lyrics, Michael sings about dreams being revealed — the idea that when we heal "
        "the world, hidden possibilities come to light. 'Reveal' implies something was concealed "
        "and is now being shown: 'reveal a secret,' 'reveal the truth,' 'the curtain reveals the stage.' "
        "The noun form is 'revelation': 'a shocking revelation.' "
        "Example: The morning fog lifted slowly, revealing a valley of wildflowers stretching to the horizon.\n\n"

        "The sixth word is 'existing.' It's the present participle of 'exist,' used as an adjective "
        "meaning 'currently present or in effect.' But in the song, Michael draws a profound "
        "distinction between living and merely existing — between a life filled with purpose and love, "
        "and one that's just going through the motions. 'Exist' means 'to be present, to have being.' "
        "'Existence' is the noun form. 'Existing conditions,' 'existing customers' — these are "
        "neutral uses. But 'merely existing' carries a note of sadness. "
        "Example: There's a difference between existing and truly living — and the gap is filled by passion.\n\n"

        "Your 6 new words: bliss, dread, joyful, grace, reveal, existing. "
        "Combined with Session 1, you now have 12 words from 'Heal the World.' "
        "Let's put them to work!"
    )

    # Activities 2-6: flashcards/vocab
    s1["activities"][2]["title"] = "Flashcards: Bliss and Grace"
    s1["activities"][2]["description"] = "Learn 6 words: bliss, dread, joyful, grace, reveal, existing"

    s1["activities"][3]["title"] = "Flashcards: Speak Session 2 Vocabulary"
    s1["activities"][3]["description"] = "Practice saying 6 words: bliss, dread, joyful, grace, reveal, existing"

    s1["activities"][4]["title"] = "Flashcards: Recognize Session 2 Vocabulary"
    s1["activities"][4]["description"] = "Recognize 6 words: bliss, dread, joyful, grace, reveal, existing"

    s1["activities"][5]["title"] = "Flashcards: Recall Session 2 Vocabulary"
    s1["activities"][5]["description"] = "Recall 6 words: bliss, dread, joyful, grace, reveal, existing"

    s1["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 2"
    s1["activities"][6]["description"] = "Master 6 words: bliss, dread, joyful, grace, reveal, existing"

    # Activity 7: introAudio — grammar/usage
    s1["activities"][7]["title"] = "Grammar and Usage: Session 2"
    s1["activities"][7]["description"] = "How to use Session 2 vocabulary naturally in sentences"
    s1["activities"][7]["data"]["text"] = (
        "Excellent! Let's explore how these 6 words behave in real English.\n\n"
        "'Bliss' is an uncountable noun — you can't say 'a bliss' or 'two blisses.' "
        "It's always 'pure bliss,' 'sheer bliss,' 'domestic bliss.' "
        "The adjective 'blissful' is common: 'a blissful silence,' 'blissfully ignorant.' "
        "The phrase 'wedded bliss' is often used humorously about married life.\n\n"
        "'Dread' as a verb takes a direct object or a gerund: 'I dread the exam,' "
        "'I dread going to the dentist.' Never 'I dread to go' in modern English (though "
        "it appears in older literature). As a noun: 'a sense of dread,' 'filled with dread.' "
        "'Dreadful' is the adjective; 'dreadfully' the adverb: 'dreadfully sorry.'\n\n"
        "'Joyful' vs. 'joyous': both mean 'full of joy,' but 'joyful' is more common in everyday "
        "speech while 'joyous' is slightly more formal or literary. 'A joyful occasion,' "
        "'joyful news.' The noun 'joy' stands alone: 'tears of joy,' 'a joy to watch.'\n\n"
        "'Grace' has fascinating grammar. As a noun: 'with grace,' 'by the grace of God,' "
        "'a grace note' (music term). As a verb: 'She graced the cover of the magazine.' "
        "'Graceful' means elegant; 'gracious' means kind and courteous. "
        "'Gracefully' and 'graciously' are the adverb forms.\n\n"
        "'Reveal' is a transitive verb — it always needs an object: 'reveal the answer,' "
        "'reveal yourself.' The passive is common: 'The winner was revealed.' "
        "'Revealing' as an adjective means 'making something known' or 'showing more of the body "
        "than usual': 'a revealing interview,' 'a revealing dress.'\n\n"
        "'Existing' as an adjective means 'currently in place': 'existing laws,' 'existing members.' "
        "The verb 'exist' is intransitive — it never takes an object: 'The problem exists,' "
        "not 'The problem exists something.' 'Existence' is the noun: 'the existence of life on Mars.' "
        "'Existent' is a rarer adjective form: 'non-existent' is more commonly used than 'existent.'"
    )

    # Activity 8-10: reading/speak/listen — keep text, update titles
    s1["activities"][8]["title"] = "Read: Heal the World Lyrics (Part 2)"
    s1["activities"][8]["description"] = "Read the middle verses about bliss, grace, and revelation"

    s1["activities"][9]["title"] = "Speak: Practice the Lyrics (Part 2)"
    s1["activities"][9]["description"] = "Practice speaking the middle verses aloud"

    s1["activities"][10]["title"] = "Listen: Heal the World (Part 2)"
    s1["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s1["activities"][11]["title"] = "Write: Grace and Hope"
    s1["activities"][11]["description"] = "Write sentences using Session 2 vocabulary"
    ws_items_1 = s1["activities"][11]["data"]["items"]
    ws_items_1[0]["prompt"] = (
        "Use the word 'bliss' to describe a moment of supreme happiness — "
        "like Michael Jackson's vision of a world where suffering gives way to pure joy. "
        "Example: Watching the sunset from the mountaintop, she felt a moment of pure bliss."
    )
    ws_items_1[1]["prompt"] = (
        "Use the word 'dread' to write about a deep, anticipatory fear — "
        "the kind of fear the song says would vanish in a world filled with love. "
        "Example: He felt a growing sense of dread as the storm clouds gathered on the horizon."
    )
    ws_items_1[2]["prompt"] = (
        "Use the word 'joyful' to describe something that radiates happiness — "
        "like the song's vision of a world where giving brings more joy than taking. "
        "Example: The children's joyful laughter echoed through the empty hallways of the old school."
    )
    ws_items_1[3]["prompt"] = (
        "Use the word 'grace' to write about elegance, kindness, or divine favor — "
        "as the song describes a world touched by grace when people choose love. "
        "Example: She handled the criticism with such grace that even her harshest critics were impressed."
    )
    ws_items_1[4]["prompt"] = (
        "Use the word 'reveal' to write about something hidden coming to light — "
        "like the song's promise that healing the world reveals dreams we never knew we had. "
        "Example: The morning fog lifted slowly, revealing a valley of wildflowers stretching to the horizon."
    )
    ws_items_1[5]["prompt"] = (
        "Use the word 'existing' to write about the difference between merely being alive "
        "and truly living — as Michael Jackson challenges us to do more than just exist. "
        "Example: There's a difference between existing and truly living — and the gap is filled by passion."
    )

    # ── Session 2: Group 3 — spirits, fear, create, nations, plain, heavenly ──
    s2 = content["learningSessions"][2]
    s2["title"] = "Session 3: Spirits and Peace"

    # Activity 0: introAudio — session intro
    s2["activities"][0]["title"] = "Introduction to Session 3"
    s2["activities"][0]["description"] = "Recap Sessions 1-2 and introduce the themes of courage and vision"
    s2["activities"][0]["data"]["text"] = (
        "Welcome to Session 3 — the final learning session before your review! "
        "So far you've learned 12 words from 'Heal the World.' In Session 1, you met "
        "heal, brighter, sorrow, entire, care, and space — the words of the song's opening plea, "
        "where Michael Jackson names the world's pain and asks us to make room for love. "
        "In Session 2, you learned bliss, dread, joyful, grace, reveal, and existing — "
        "the words of the song's emotional core, where sorrow begins to transform into hope "
        "and the difference between living and merely existing becomes clear.\n\n"
        "Now we reach the song's climax. Michael lifts his voice and calls on the spirits "
        "of every nation to rise above fear and create something new. This is where the song "
        "stops being a gentle ballad and becomes a rallying cry — a demand that we stop accepting "
        "the world as it is and start building the world as it should be.\n\n"
        "Your final 6 words: spirits, fear, create, nations, plain, and heavenly. "
        "By the end of this session, you'll have all 18 vocabulary words — and you'll hear "
        "'Heal the World' the way Michael Jackson intended it to be heard."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s2["activities"][1]["title"] = "Vocabulary Introduction: Session 3"
    s2["activities"][1]["description"] = "Learn 6 words: spirits, fear, create, nations, plain, heavenly"
    s2["activities"][1]["data"]["text"] = (
        "Here are your final 6 vocabulary words, drawn from the most powerful verses "
        "of 'Heal the World.'\n\n"

        "The first word is 'spirits.' It's the plural of 'spirit' — a word with many layers. "
        "It can mean 'the non-physical part of a person' (soul), 'a supernatural being' (ghost), "
        "or 'a prevailing mood or attitude' (team spirit). In the song, Michael sings about "
        "keeping our spirits high — maintaining courage, hope, and emotional strength even when "
        "the world feels heavy. 'In good spirits' means cheerful. 'The spirit of the law' means "
        "the intention behind a rule, not just its literal words. 'Spirited' means lively and brave. "
        "Example: Despite the setbacks, the team's spirits remained high throughout the entire project.\n\n"

        "The second word is 'fear.' It can be a noun or a verb. As a noun, it means 'an unpleasant "
        "emotion caused by the threat of danger, pain, or harm.' As a verb: 'I fear the worst.' "
        "Michael's song dreams of a world without fear — where people act from love instead of "
        "self-protection. 'Fear' is one of the most fundamental human emotions, and English has "
        "dozens of expressions built around it: 'fear of the unknown,' 'for fear of,' 'fearless,' "
        "'fearful,' 'fear factor.' The phrase 'no fear' is slang for 'don't worry.' "
        "Example: The only thing standing between you and your dream is the fear of taking the first step.\n\n"

        "The third word is 'create.' It's a verb meaning 'to bring something into existence.' "
        "Michael calls on us to create a better world — not to wait for it, but to build it "
        "with our own hands and hearts. 'Create' implies intentionality and imagination. "
        "You create art, create opportunities, create change. 'Creation' is the noun; "
        "'creative' is the adjective; 'creator' is the person who creates; 'creativity' is the ability. "
        "Example: She didn't wait for the perfect moment — she decided to create it.\n\n"

        "The fourth word is 'nations.' It's the plural of 'nation' — a large body of people "
        "united by common descent, history, culture, or language, inhabiting a particular territory. "
        "Michael sings about nations turning their swords into plowshares — an ancient image of "
        "choosing peace over war. 'Nation' is more formal than 'country' and carries a sense of "
        "identity and purpose. 'National' (adjective), 'nationality' (noun), 'nationwide' (adjective/adverb). "
        "'The United Nations' is the international organization. "
        "Example: The agreement brought together nations that had been rivals for centuries.\n\n"

        "The fifth word is 'plain.' It's an adjective with several meanings: 'clear and obvious' "
        "('it's plain to see'), 'simple and unadorned' ('plain clothes'), or 'not attractive' "
        "(somewhat blunt). In the song, Michael uses 'plain' in the sense of 'obvious' — "
        "'it's plain to see' that the world needs healing. This is one of those English words "
        "where context determines everything. 'Plain' can also be a noun meaning 'a large flat area "
        "of land': 'the Great Plains.' 'Plainly' is the adverb: 'She spoke plainly.' "
        "Example: The answer was plain to see, but nobody wanted to be the first to say it out loud.\n\n"

        "The sixth and final word is 'heavenly.' It's an adjective meaning 'of or relating to heaven' "
        "or, more commonly, 'extremely pleasant or beautiful.' Michael describes a heavenly place — "
        "a world so transformed by love that it feels like paradise. In everyday English, 'heavenly' "
        "is often used as an intensifier for something wonderful: 'This cake is heavenly,' "
        "'a heavenly aroma,' 'heavenly music.' 'Heaven' is the noun; 'heavenward' means 'toward heaven.' "
        "Example: The garden in spring was heavenly — roses in every color, birdsong from every branch.\n\n"

        "And there you have it — all 18 words: heal, brighter, sorrow, entire, care, space, "
        "bliss, dread, joyful, grace, reveal, existing, spirits, fear, create, nations, plain, "
        "and heavenly. You now have the complete vocabulary of 'Heal the World.' "
        "Let's practice these final 6!"
    )

    # Activities 2-6: flashcards/vocab
    s2["activities"][2]["title"] = "Flashcards: Spirits and Peace"
    s2["activities"][2]["description"] = "Learn 6 words: spirits, fear, create, nations, plain, heavenly"

    s2["activities"][3]["title"] = "Flashcards: Speak Session 3 Vocabulary"
    s2["activities"][3]["description"] = "Practice saying 6 words: spirits, fear, create, nations, plain, heavenly"

    s2["activities"][4]["title"] = "Flashcards: Recognize Session 3 Vocabulary"
    s2["activities"][4]["description"] = "Recognize 6 words: spirits, fear, create, nations, plain, heavenly"

    s2["activities"][5]["title"] = "Flashcards: Recall Session 3 Vocabulary"
    s2["activities"][5]["description"] = "Recall 6 words: spirits, fear, create, nations, plain, heavenly"

    s2["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 3"
    s2["activities"][6]["description"] = "Master 6 words: spirits, fear, create, nations, plain, heavenly"

    # Activity 7: introAudio — grammar/usage
    s2["activities"][7]["title"] = "Grammar and Usage: Session 3"
    s2["activities"][7]["description"] = "How to use Session 3 vocabulary naturally in sentences"
    s2["activities"][7]["data"]["text"] = (
        "Let's look at how these final 6 words work in English grammar.\n\n"
        "'Spirits' as a plural noun has three main uses: (1) supernatural beings — 'evil spirits,' "
        "'the spirits of the dead'; (2) mood or morale — 'in high spirits,' 'lift someone's spirits'; "
        "(3) alcoholic drinks — 'wine and spirits.' The singular 'spirit' can also mean 'the essential "
        "nature of something': 'the spirit of the law,' 'the spirit of adventure.' "
        "'Spiritual' is the adjective; 'spiritually' the adverb.\n\n"
        "'Fear' as a verb can take a direct object ('I fear failure') or a clause ('I fear that "
        "we're too late'). 'Fear for' means 'to be worried about': 'I fear for her safety.' "
        "'Fearful' means 'full of fear' or 'causing fear.' 'Fearless' means 'without fear.' "
        "'Fearsome' means 'frightening.' The phrase 'God-fearing' means devoutly religious.\n\n"
        "'Create' is a regular verb: create, created, created. It's transitive — it always needs "
        "an object: 'create a painting,' 'create problems,' 'create an account.' "
        "'Creative' (adjective), 'creation' (noun), 'creator' (noun), 'creativity' (noun). "
        "'Re-create' means to create again; 'recreate' (no hyphen) means to enjoy leisure.\n\n"
        "'Nations' — 'nation' is more formal than 'country.' 'A nation of immigrants,' "
        "'nation-building,' 'nationwide.' 'National' is the adjective: 'national anthem,' "
        "'national park.' 'Nationality' refers to citizenship. 'Nationalize' means to bring "
        "under government control.\n\n"
        "'Plain' has multiple parts of speech. Adjective: 'plain language,' 'plain truth,' "
        "'plain yogurt' (unflavored). Noun: 'the plains of Africa.' Adverb (informal): "
        "'That's just plain wrong.' 'Plainly' is the standard adverb: 'She spoke plainly.' "
        "'Plain-spoken' means direct and honest.\n\n"
        "'Heavenly' is always an adjective. It modifies nouns: 'heavenly bodies' (stars and planets), "
        "'heavenly music,' 'a heavenly dessert.' The noun 'heaven' can be singular or plural: "
        "'heaven' (the place) vs. 'the heavens' (the sky). 'Heavenward' means 'toward heaven.' "
        "'Good heavens!' is an exclamation of surprise."
    )

    # Activity 8-10: reading/speak/listen
    s2["activities"][8]["title"] = "Read: Heal the World Lyrics (Part 3)"
    s2["activities"][8]["description"] = "Read the final verses about spirits, nations, and peace"

    s2["activities"][9]["title"] = "Speak: Practice the Lyrics (Part 3)"
    s2["activities"][9]["description"] = "Practice speaking the final verses aloud"

    s2["activities"][10]["title"] = "Listen: Heal the World (Part 3)"
    s2["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s2["activities"][11]["title"] = "Write: Peace and Vision"
    s2["activities"][11]["description"] = "Write sentences using Session 3 vocabulary"
    ws_items_2 = s2["activities"][11]["data"]["items"]
    ws_items_2[0]["prompt"] = (
        "Use the word 'spirits' to write about mood, courage, or the non-physical essence of something — "
        "like Michael Jackson's call to keep our spirits high in the face of adversity. "
        "Example: Despite the setbacks, the team's spirits remained high throughout the entire project."
    )
    ws_items_2[1]["prompt"] = (
        "Use the word 'fear' to write about what holds people back — "
        "as the song dreams of a world where fear no longer controls our choices. "
        "Example: The only thing standing between you and your dream is the fear of taking the first step."
    )
    ws_items_2[2]["prompt"] = (
        "Use the word 'create' to write about bringing something new into existence — "
        "like Michael Jackson's call to create a better world through love and action. "
        "Example: She didn't wait for the perfect moment — she decided to create it."
    )
    ws_items_2[3]["prompt"] = (
        "Use the word 'nations' to write about countries, peoples, or global unity — "
        "as the song envisions nations choosing peace over conflict. "
        "Example: The agreement brought together nations that had been rivals for centuries."
    )
    ws_items_2[4]["prompt"] = (
        "Use the word 'plain' to write about something obvious or simple — "
        "like the song's declaration that 'it's plain to see' the world needs healing. "
        "Example: The answer was plain to see, but nobody wanted to be the first to say it out loud."
    )
    ws_items_2[5]["prompt"] = (
        "Use the word 'heavenly' to describe something extraordinarily beautiful or pleasant — "
        "like Michael Jackson's vision of a world so transformed by love it feels like paradise. "
        "Example: The garden in spring was heavenly — roses in every color, birdsong from every branch."
    )

    # ── Session 3: Review (4 activities) ──
    s3 = content["learningSessions"][3]
    s3["title"] = "Review"

    s3["activities"][0]["title"] = "Congratulations and Review"
    s3["activities"][0]["description"] = "Celebrate your progress and prepare for the full review"
    s3["activities"][0]["data"]["text"] = (
        "Congratulations! You've learned all 18 vocabulary words from 'Heal the World.' "
        "Let's take a moment to look back at what you've accomplished.\n\n"
        "In Session 1, you learned heal, brighter, sorrow, entire, care, and space — "
        "the words of the song's opening plea, where Michael Jackson names the world's pain "
        "and asks us to make room in our hearts for love and compassion.\n\n"
        "In Session 2, you learned bliss, dread, joyful, grace, reveal, and existing — "
        "the words of the song's emotional core, where sorrow transforms into hope "
        "and Michael challenges us to truly live, not merely exist.\n\n"
        "In Session 3, you learned spirits, fear, create, nations, plain, and heavenly — "
        "the words of the song's climax, where Michael calls on every nation to rise above fear "
        "and create a world so beautiful it feels like heaven on earth.\n\n"
        "Now it's time to review all 18 words together. This review session will test your "
        "recognition and recall across all three groups. After this, you'll be ready to read "
        "the complete lyrics in the final session. Let's go!"
    )

    s3["activities"][1]["title"] = "Flashcards: Review All 18 Words"
    s3["activities"][1]["description"] = "Review all 18 vocabulary words from Heal the World"

    s3["activities"][2]["title"] = "Flashcards: Recognize All Vocabulary"
    s3["activities"][2]["description"] = "Test your recognition of all 18 words"

    s3["activities"][3]["title"] = "Flashcards: Recall All Vocabulary"
    s3["activities"][3]["description"] = "Test your recall of all 18 words"

    # ── Session 4: Full reading + farewell (5 activities) ──
    s4 = content["learningSessions"][4]
    s4["title"] = "Full Lyrics Reading"

    s4["activities"][0]["title"] = "Introduction to the Complete Reading"
    s4["activities"][0]["description"] = "Prepare for reading the full Heal the World lyrics"
    s4["activities"][0]["data"]["text"] = (
        "Welcome to the final session! This is the moment everything comes together. "
        "Over the past three sessions, you've built a vocabulary of 18 words drawn directly "
        "from the lyrics of 'Heal the World.' You've learned their meanings, practiced their "
        "pronunciation, explored their grammar, and used them in your own writing.\n\n"
        "Now you're going to read the complete lyrics — all three sections combined into one "
        "continuous passage. As you read, you'll encounter every single one of your 18 words "
        "in context. This time, they won't be new — they'll be familiar friends.\n\n"
        "Here are all 18 words you'll see: heal, brighter, sorrow, entire, care, space, "
        "bliss, dread, joyful, grace, reveal, existing, spirits, fear, create, nations, "
        "plain, and heavenly.\n\n"
        "Take your time with the reading. Let Michael's voice come through the words. "
        "And remember — if enough people care, the world really can heal."
    )

    s4["activities"][1]["title"] = "Read: Complete Heal the World Lyrics"
    s4["activities"][1]["description"] = "Read the full lyrics from beginning to end"

    s4["activities"][2]["title"] = "Speak: Practice the Complete Lyrics"
    s4["activities"][2]["description"] = "Practice speaking the entire lyrics aloud"

    s4["activities"][3]["title"] = "Listen: Complete Heal the World"
    s4["activities"][3]["description"] = "Listen to the complete lyrics and follow along"

    s4["activities"][4]["title"] = "Farewell and Vocabulary Review"
    s4["activities"][4]["description"] = "Final review of all 18 words and farewell"
    s4["activities"][4]["data"]["text"] = (
        "You've done it — you've completed the entire 'Heal the World' vocabulary course! "
        "Let's do one final review of all 18 words before we say goodbye.\n\n"

        "'Heal' — to make whole or sound again, to restore to health. "
        "Example: Time doesn't heal all wounds, but it teaches you how to carry them.\n\n"
        "'Brighter' — more luminous, more hopeful, more promising. "
        "Example: After the rain, the colors of the garden looked even brighter than before.\n\n"
        "'Sorrow' — deep distress, sadness, or grief. "
        "Example: There is a kind of sorrow that only comes from loving something deeply.\n\n"
        "'Entire' — whole, complete, with nothing missing. "
        "Example: He spent the entire weekend building a treehouse for his daughter.\n\n"
        "'Care' — to feel concern; the provision of what is needed for well-being. "
        "Example: She cared for the stray cat until it was strong enough to find a home.\n\n"
        "'Space' — an area or expanse; room to exist and breathe. "
        "Example: The library was her favorite space — quiet, warm, and full of possibility.\n\n"

        "'Bliss' — supreme happiness, utter joy. "
        "Example: The first sip of coffee on a cold morning is a small moment of bliss.\n\n"
        "'Dread' — great fear or apprehension about something to come. "
        "Example: She felt a quiet dread every Sunday evening, knowing Monday was around the corner.\n\n"
        "'Joyful' — feeling, expressing, or causing great happiness. "
        "Example: The reunion was a joyful occasion — hugs, tears, and stories that lasted until midnight.\n\n"
        "'Grace' — elegance, courteous goodwill, or divine favor. "
        "Example: He accepted the award with grace, thanking everyone who had helped along the way.\n\n"
        "'Reveal' — to make known something previously hidden. "
        "Example: The final chapter revealed a twist that nobody saw coming.\n\n"
        "'Existing' — currently present; or merely surviving without truly living. "
        "Example: She realized she had been existing on autopilot and decided it was time to start living.\n\n"

        "'Spirits' — mood, courage, or the non-physical essence of a person. "
        "Example: A handwritten letter from an old friend lifted her spirits on the hardest day of the year.\n\n"
        "'Fear' — an unpleasant emotion caused by the threat of danger or harm. "
        "Example: Courage isn't the absence of fear — it's acting in spite of it.\n\n"
        "'Create' — to bring something into existence through imagination and effort. "
        "Example: The best teachers don't just deliver lessons — they create experiences.\n\n"
        "'Nations' — large bodies of people united by common identity, inhabiting a territory. "
        "Example: When nations cooperate instead of compete, extraordinary things become possible.\n\n"
        "'Plain' — clear and obvious; simple and unadorned. "
        "Example: He was a plain-spoken man who said exactly what he meant, no more, no less.\n\n"
        "'Heavenly' — of or relating to heaven; extremely pleasant or beautiful. "
        "Example: The aroma of fresh bread from the bakery next door was absolutely heavenly.\n\n"

        "Thank you for learning with Michael Jackson's 'Heal the World.' "
        "You came for 18 vocabulary words, but I hope you're leaving with something more — "
        "a reminder that the simplest words, sung with conviction, can carry the weight of "
        "an entire movement. Michael believed that one person could make a difference, "
        "and that belief lives in every word of this song. "
        "Keep reading, keep speaking, keep writing — and keep healing the world, "
        "one small act of kindness at a time. Goodbye, and carry the music with you!"
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
    print(f"Created en-en Heal the World curriculum: {cid}")
    return cid


if __name__ == "__main__":
    create()
