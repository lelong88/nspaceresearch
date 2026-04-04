"""
Create en-en song curriculum #3: What a Wonderful World
Mirror of vi-en source 5WdGkIlyRDO4dzsL — all Vietnamese UI text rewritten in English.

Source song: What a Wonderful World by Louis Armstrong (1967)
YouTube: https://www.youtube.com/watch?v=A3yCcXgbKrE

18 vocabulary words in 3 groups of 6 (same as vi-en source):
  Group 1: blessed, bloom, bright, sacred, skies, wonderful
  Group 2: faces, pretty, rainbow, really, saying, shaking
  Group 3: babies, colors, friends, grow, learn, world

All user-facing text in English. Reading passages stay as-is (already English).
Vocabulary words stay as-is (already English).

Requirements: 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 9.1, 9.2, 9.3, 9.4, 9.5
"""

import sys, json, requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"
SOURCE_ID = "5WdGkIlyRDO4dzsL"

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
    content["title"] = "'What a Wonderful World' — Louis Armstrong"

    content["description"] = (
        "WHAT IF THE SECRET TO HAPPINESS WAS SIMPLY PAYING ATTENTION?\n\n"
        "In 1967, the world was on fire — Vietnam, civil rights marches, cities burning. "
        "And in the middle of all that chaos, Louis Armstrong walked into a recording studio "
        "and sang about green trees, red roses, blue skies, and babies crying. Not because he "
        "was naive. Because he was wise. He'd seen more hardship in his life than most people "
        "could imagine — growing up in poverty in New Orleans, facing racism at every turn, "
        "burying friends and watching the country tear itself apart. And still, he chose to see "
        "the beauty. That's not ignorance. That's courage.\n\n"
        "The song flopped in America when it was first released. It took years — and a movie "
        "called 'Good Morning, Vietnam' — for the world to catch up to what Louis already knew: "
        "that wonder isn't something you find. It's something you practice. Every line of this song "
        "is an act of deliberate attention — noticing the colors of the rainbow, the faces of "
        "friends, the sound of babies learning to grow.\n\n"
        "Now imagine understanding every word Louis sings — from 'bloom' when he watches roses "
        "open in the sun, to 'sacred' when he describes the quiet holiness of an ordinary day, "
        "to 'wonderful' when he names the feeling that rises in your chest when you stop rushing "
        "and actually look at the world around you.\n\n"
        "18 vocabulary words drawn directly from the lyrics, combined with "
        "a multi-sensory learning method — listening, reading, speaking, writing — "
        "so you sharpen your English while carrying Louis Armstrong's reminder that "
        "beauty is everywhere, if you just slow down enough to see it."
    )

    content["preview"] = {
        "text": (
            "Have you ever stopped in the middle of a busy day and suddenly noticed "
            "how beautiful the sky looked? That pause — that moment of unexpected wonder — "
            "is exactly what Louis Armstrong captured in this song. And now you'll learn "
            "English through the very words he chose.\n\n"
            "18 English vocabulary words you'll learn: blessed, bloom, bright, sacred, skies, "
            "wonderful, faces, pretty, rainbow, really, saying, shaking, babies, colors, "
            "friends, grow, learn, world.\n\n"
            "Across 5 sessions you'll read the actual lyrics, discover how Louis uses "
            "the simplest words to celebrate the beauty hiding in plain sight — from the "
            "bright blessed day to the sacred dark night, from the colors of the rainbow "
            "to the faces of friends saying 'I love you.'\n\n"
            "Tap the link below to watch Louis Armstrong perform — after this course, "
            "you'll hear him sing and understand every single word naturally."
        )
    }

    content["contentTypeTags"] = ["music"]
    content["is_public"] = False

    # ── Session 0: Group 1 — blessed, bloom, bright, sacred, skies, wonderful ──
    s0 = content["learningSessions"][0]
    s0["title"] = "Session 1: The Beauty of Nature — What a Wonderful World"

    # Activity 0: introAudio — song intro
    s0["activities"][0]["title"] = "Introduction to the Song"
    s0["activities"][0]["description"] = "Setting the stage for Louis Armstrong's celebration of beauty"
    s0["activities"][0]["data"]["text"] = (
        "Welcome to the vocabulary-through-music course! Today we begin with one of "
        "the most beloved songs ever recorded — 'What a Wonderful World' by Louis Armstrong. "
        "Released in 1967, this song was written by Bob Thiele and George David Weiss specifically "
        "for Louis, whose gravelly, warm voice could make even the simplest words feel like a prayer. "
        "The song was a commercial failure in the United States when it first came out — it sold "
        "fewer than a thousand copies. But in the United Kingdom, it went straight to number one. "
        "It took two decades and a Robin Williams movie for America to finally hear what the rest "
        "of the world already knew: this song is a masterpiece of gratitude.\n\n"
        "Louis Armstrong was born in 1901 in one of the poorest neighborhoods in New Orleans. "
        "He grew up without a father, spent time in a juvenile detention home, and faced brutal "
        "racism throughout his career. And yet, when he sang 'What a Wonderful World,' there was "
        "no irony in his voice — only sincerity. He genuinely believed that the world was full "
        "of beauty, not because he hadn't seen its ugliness, but because he chose to look past it.\n\n"
        "In this first session, you'll learn 6 vocabulary words that appear in the opening verses "
        "of the song: blessed, bloom, bright, sacred, skies, and wonderful. Each word captures "
        "a different facet of the natural beauty Louis celebrates — and by the end of this session "
        "you'll hear them not as simple adjectives, but as acts of deliberate wonder."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s0["activities"][1]["title"] = "Vocabulary Introduction: Session 1"
    s0["activities"][1]["description"] = "Learn 6 words: blessed, bloom, bright, sacred, skies, wonderful"
    s0["activities"][1]["data"]["text"] = (
        "Let's dive into the first 6 vocabulary words from 'What a Wonderful World.' "
        "Each word comes straight from Louis Armstrong's lyrics, and understanding how he uses them "
        "will change the way you hear this song — and English — forever.\n\n"

        "The first word is 'blessed.' It's an adjective meaning 'made holy by religious rite' "
        "or, more commonly, 'fortunate and happy.' Louis sings about 'the bright blessed day' — "
        "a day that feels touched by something sacred, something larger than ordinary life. "
        "In everyday English, 'blessed' has two pronunciations: one syllable ('blest') in casual speech, "
        "and two syllables ('bless-ed') in formal or poetic contexts. The song uses the two-syllable "
        "version for its musical rhythm. 'Bless' is the verb; 'blessing' is the noun. "
        "Common phrases: 'blessed with' (fortunate to have), 'count your blessings' (appreciate what you have). "
        "Example: She felt blessed to have grown up near the ocean, where every morning began with the sound of waves.\n\n"

        "The second word is 'bloom.' It's a verb meaning 'to produce flowers' or 'to flourish.' "
        "Louis watches roses bloom — a simple image of nature doing what it does best, "
        "unfolding beauty without effort or fanfare. 'Bloom' can also be a noun: 'a rose in full bloom,' "
        "'the bloom of youth.' The word carries a sense of natural timing — things bloom when they're ready, "
        "not when you force them. 'Blooming' as an adjective means 'flourishing': 'a blooming garden.' "
        "In British slang, 'blooming' is a mild intensifier: 'blooming marvelous.' "
        "Example: The cherry trees bloom for only two weeks each spring, and the whole city stops to watch.\n\n"

        "The third word is 'bright.' It's an adjective meaning 'giving out or reflecting a lot of light' "
        "or 'intelligent and quick-witted.' Louis pairs it with 'blessed' to describe the day — "
        "a day that's not just sunny but radiant, glowing with something more than light. "
        "'Bright' has both physical and figurative meanings: a bright room (well-lit), a bright student "
        "(intelligent), a bright future (promising), bright colors (vivid). The comparative is 'brighter,' "
        "the superlative 'brightest.' 'Brighten' is the verb: 'Her smile brightened the room.' "
        "Example: The bright morning sun poured through the window and made everything in the kitchen glow gold.\n\n"

        "The fourth word is 'sacred.' It's an adjective meaning 'connected with God or a god; "
        "regarded with great respect and reverence.' Louis sings about 'the dark sacred night' — "
        "turning darkness into something holy, something worthy of awe rather than fear. "
        "This is one of the song's most beautiful moves: night isn't scary, it's sacred. "
        "'Sacred' can also mean 'too important to be changed or interfered with': "
        "'sacred traditions,' 'nothing is sacred' (everything can be questioned). "
        "Example: The old library felt like a sacred space — hushed, warm, and full of stories waiting to be found.\n\n"

        "The fifth word is 'skies.' It's the plural of 'sky' — the region of the atmosphere "
        "seen from the earth. Louis sings about 'skies of blue' — a simple, painterly image "
        "that places you outdoors, looking up. In English, 'sky' is often pluralized in poetic "
        "or literary contexts: 'under foreign skies,' 'clear skies ahead,' 'the skies opened up' "
        "(it started raining heavily). 'Skyline' is the outline of buildings against the sky. "
        "'Sky-high' means extremely high. "
        "Example: After weeks of rain, the skies finally cleared and the whole neighborhood came outside to celebrate.\n\n"

        "The sixth word is 'wonderful.' It's an adjective meaning 'inspiring delight, pleasure, "
        "or admiration; extremely good.' This is the word that carries the entire song — "
        "'What a wonderful world.' Louis doesn't say 'beautiful' or 'amazing' or 'incredible.' "
        "He says 'wonderful' — full of wonder. The word literally means 'full of things that cause wonder.' "
        "'Wonder' is the noun and verb: 'I wonder why,' 'a sense of wonder.' "
        "'Wonderfully' is the adverb. 'Wondrous' is a more literary synonym. "
        "Example: The most wonderful thing about traveling isn't the places — it's the way it changes how you see home.\n\n"

        "Your first 6 words: blessed, bloom, bright, sacred, skies, and wonderful. "
        "Each one is woven into the fabric of Louis Armstrong's hymn to the beauty of ordinary life. "
        "Let's practice them now!"
    )

    # Activities 2-6: flashcards/vocab — update titles and descriptions
    s0["activities"][2]["title"] = "Flashcards: The Beauty of Nature"
    s0["activities"][2]["description"] = "Learn 6 words: blessed, bloom, bright, sacred, skies, wonderful"

    s0["activities"][3]["title"] = "Flashcards: Speak Session 1 Vocabulary"
    s0["activities"][3]["description"] = "Practice saying 6 words: blessed, bloom, bright, sacred, skies, wonderful"

    s0["activities"][4]["title"] = "Flashcards: Recognize Session 1 Vocabulary"
    s0["activities"][4]["description"] = "Recognize 6 words: blessed, bloom, bright, sacred, skies, wonderful"

    s0["activities"][5]["title"] = "Flashcards: Recall Session 1 Vocabulary"
    s0["activities"][5]["description"] = "Recall 6 words: blessed, bloom, bright, sacred, skies, wonderful"

    s0["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 1"
    s0["activities"][6]["description"] = "Master 6 words: blessed, bloom, bright, sacred, skies, wonderful"

    # Activity 7: introAudio — grammar/usage
    s0["activities"][7]["title"] = "Grammar and Usage: Session 1"
    s0["activities"][7]["description"] = "How to use Session 1 vocabulary naturally in sentences"
    s0["activities"][7]["data"]["text"] = (
        "Great work! You've met your first 6 words. Now let's look at how they work "
        "in real English sentences, using the lyrics of 'What a Wonderful World' as our guide.\n\n"
        "'Blessed' has two pronunciations that signal different meanings. As a one-syllable adjective "
        "('blest'), it's informal: 'I'm blessed to have you.' As a two-syllable adjective ('bless-ed'), "
        "it's formal or poetic: 'the blessed day.' The verb 'bless' is regular: bless, blessed, blessed. "
        "'Bless you' is said after a sneeze. 'Blessing in disguise' means something that seems bad "
        "but turns out good. 'Count your blessings' means appreciate what you have.\n\n"
        "'Bloom' is a regular verb: bloom, bloomed, bloomed. It's intransitive — flowers bloom, "
        "they don't bloom something. 'In bloom' means currently flowering: 'The garden is in bloom.' "
        "'Full bloom' means at the peak of flowering or development: 'a career in full bloom.' "
        "'Late bloomer' describes someone who develops or succeeds later than expected. "
        "'Blooming' as a present participle: 'The blooming roses filled the air with fragrance.'\n\n"
        "'Bright' is a one-syllable adjective with regular comparison: bright, brighter, brightest. "
        "It collocates widely: 'bright light,' 'bright idea,' 'bright future,' 'bright colors,' "
        "'bright side' (the positive aspect). 'Brighten' is the verb: 'The news brightened her day.' "
        "'Brightly' is the adverb: 'The stars shone brightly.' 'Brightness' is the noun.\n\n"
        "'Sacred' is always an adjective — there's no verb form. It modifies nouns: "
        "'sacred ground,' 'sacred music,' 'sacred duty,' 'sacred cow' (something that cannot be criticized). "
        "The opposite is 'profane' or 'secular.' 'Sacredness' is the noun form, though it's rarely used. "
        "'Sacrifice' is related etymologically — giving something up for something sacred.\n\n"
        "'Skies' — the plural of 'sky' is used more often than you might expect. "
        "Singular: 'The sky is blue.' Plural: 'Under clear skies,' 'The skies darkened.' "
        "The plural often appears in weather contexts and poetic language. "
        "'Skyward' means 'toward the sky.' 'Skyscraper' is a very tall building. "
        "'The sky's the limit' means there are no restrictions.\n\n"
        "'Wonderful' is a two-syllable adjective. It doesn't follow the '-er/-est' pattern — "
        "use 'more wonderful' and 'most wonderful.' 'Wonderfully' is the adverb: "
        "'wonderfully kind,' 'wonderfully strange.' 'Wonder' as a verb takes a clause: "
        "'I wonder if she's coming.' As a noun: 'a sense of wonder,' 'the seven wonders of the world.'"
    )

    # Activity 8: reading — keep text as-is (already English), update title/description
    s0["activities"][8]["title"] = "Read: What a Wonderful World Lyrics (Part 1)"
    s0["activities"][8]["description"] = "Read the opening verses about trees, roses, and skies"

    # Activity 9: speakReading
    s0["activities"][9]["title"] = "Speak: Practice the Lyrics (Part 1)"
    s0["activities"][9]["description"] = "Practice speaking the opening verses aloud"

    # Activity 10: readAlong
    s0["activities"][10]["title"] = "Listen: What a Wonderful World (Part 1)"
    s0["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s0["activities"][11]["title"] = "Write: Nature and Wonder"
    s0["activities"][11]["description"] = "Write sentences using Session 1 vocabulary"
    ws_items_0 = s0["activities"][11]["data"]["items"]
    ws_items_0[0]["prompt"] = (
        "Use the word 'blessed' to write about feeling fortunate or touched by something special — "
        "just as Louis Armstrong sings about the bright blessed day. "
        "Example: She felt blessed to have grown up near the ocean, where every morning began with the sound of waves."
    )
    ws_items_0[1]["prompt"] = (
        "Use the word 'bloom' to write about something flowering or flourishing — "
        "like the roses Louis watches bloom in the song. "
        "Example: The cherry trees bloom for only two weeks each spring, and the whole city stops to watch."
    )
    ws_items_0[2]["prompt"] = (
        "Use the word 'bright' to describe something luminous, vivid, or promising — "
        "like the bright blessed day that opens the song. "
        "Example: The bright morning sun poured through the window and made everything in the kitchen glow gold."
    )
    ws_items_0[3]["prompt"] = (
        "Use the word 'sacred' to write about something holy, revered, or deeply important — "
        "as Louis transforms the dark night into something sacred and beautiful. "
        "Example: The old library felt like a sacred space — hushed, warm, and full of stories waiting to be found."
    )
    ws_items_0[4]["prompt"] = (
        "Use the word 'skies' to write about the sky or atmosphere — "
        "like the skies of blue that Louis celebrates in the opening verse. "
        "Example: After weeks of rain, the skies finally cleared and the whole neighborhood came outside to celebrate."
    )
    ws_items_0[5]["prompt"] = (
        "Use the word 'wonderful' to describe something that inspires delight or admiration — "
        "the very word Louis chose to capture his feeling about the world. "
        "Example: The most wonderful thing about traveling isn't the places — it's the way it changes how you see home."
    )

    # ── Session 1: Group 2 — faces, pretty, rainbow, really, saying, shaking ──
    s1 = content["learningSessions"][1]
    s1["title"] = "Session 2: People and Connection"

    # Activity 0: introAudio — session intro
    s1["activities"][0]["title"] = "Introduction to Session 2"
    s1["activities"][0]["description"] = "Recap Session 1 and introduce the theme of human connection"
    s1["activities"][0]["data"]["text"] = (
        "Welcome back to Session 2! In our first session, you learned 6 words from the opening "
        "of 'What a Wonderful World': blessed, bloom, bright, sacred, skies, and wonderful. "
        "You discovered how Louis Armstrong uses the simplest vocabulary to paint a picture "
        "of natural beauty — where every day is blessed, every night is sacred, and roses bloom "
        "under skies so blue they make you forget whatever was weighing on your mind.\n\n"
        "Now Louis turns his gaze from nature to people. In these verses, he watches friends "
        "greeting each other, shaking hands, and saying 'I love you.' He notices the colors "
        "of the rainbow reflected in the faces of people passing by. This is where the song "
        "shifts from landscape painting to portrait — from the beauty of the world to the beauty "
        "of the people in it.\n\n"
        "Today you'll learn 6 new words: faces, pretty, rainbow, really, saying, and shaking. "
        "These words carry the warmth of human connection — the small, everyday gestures "
        "that Louis Armstrong found just as wonderful as any sunset."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s1["activities"][1]["title"] = "Vocabulary Introduction: Session 2"
    s1["activities"][1]["description"] = "Learn 6 words: faces, pretty, rainbow, really, saying, shaking"
    s1["activities"][1]["data"]["text"] = (
        "Let's learn 6 new vocabulary words from the heart of 'What a Wonderful World' — "
        "the verses where Louis Armstrong turns his attention to people.\n\n"

        "The first word is 'faces.' It's the plural of 'face' — the front part of the head, "
        "from the forehead to the chin. Louis watches the faces of people he passes on the street "
        "and sees beauty in every one. 'Face' is one of the most versatile words in English: "
        "as a noun, it means the physical face ('a kind face'), a surface ('the face of a clock'), "
        "or reputation ('save face,' 'lose face'). As a verb, it means 'to confront': "
        "'face the truth,' 'face your fears.' 'Face-to-face' means in person. "
        "'Facial' is the adjective form. "
        "Example: The faces in the old photograph told a story that words never could.\n\n"

        "The second word is 'pretty.' It's an adjective meaning 'attractive in a delicate way' "
        "or an adverb meaning 'to a fairly high degree.' Louis uses it as an adverb — "
        "things are 'pretty' wonderful, meaning quite wonderful, remarkably wonderful. "
        "As an adjective: 'a pretty garden,' 'a pretty dress.' As an adverb: 'pretty good,' "
        "'pretty much,' 'pretty sure.' The adverb use is informal but extremely common in spoken English. "
        "'Prettily' is the formal adverb for the adjective meaning. "
        "Example: The village was pretty in a way that postcards could never capture — you had to stand there and breathe it in.\n\n"

        "The third word is 'rainbow.' It's a noun meaning 'an arch of colors visible in the sky, "
        "caused by the refraction of sunlight through rain.' Louis sings about the colors of the rainbow "
        "being 'so pretty in the sky' — a moment of pure visual wonder. 'Rainbow' is also used "
        "figuratively to mean 'a wide range or variety': 'a rainbow of flavors,' 'rainbow coalition.' "
        "The phrase 'chasing rainbows' means pursuing unrealistic goals. "
        "'At the end of the rainbow' refers to an imaginary place of treasure (from the pot-of-gold legend). "
        "Example: After the storm, a perfect rainbow stretched across the valley, and for a moment nobody said a word.\n\n"

        "The fourth word is 'really.' It's an adverb meaning 'in actual fact' or 'very, thoroughly.' "
        "Louis sings 'And I think to myself, what a wonderful world' — and the 'really' in the song "
        "emphasizes that he genuinely, truly means it. 'Really' is one of the most common words "
        "in spoken English. It can express emphasis ('I really love this'), surprise ('Really?'), "
        "or sincerity ('I really mean it'). 'Real' is the adjective; 'reality' is the noun. "
        "Example: She didn't really understand the painting until she stood in front of it and let it wash over her.\n\n"

        "The fifth word is 'saying.' It's the present participle of 'say,' used here as a verb form. "
        "Louis watches friends saying 'How do you do?' and 'I love you' — the everyday phrases "
        "that hold relationships together. 'Say' is irregular: say, said, said. "
        "'Saying' can also be a noun meaning 'a well-known phrase or proverb': "
        "'as the saying goes,' 'an old saying.' 'Say' vs. 'tell': 'say' focuses on the words spoken, "
        "'tell' focuses on the person being addressed. "
        "Example: Sometimes the most powerful thing you can do is keep saying 'I'm here' until someone believes you.\n\n"

        "The sixth word is 'shaking.' It's the present participle of 'shake,' meaning 'to tremble "
        "or vibrate' or 'to grasp someone's hand and move it up and down as a greeting.' "
        "Louis watches friends shaking hands — a universal gesture of warmth and respect. "
        "'Shake' is irregular: shake, shook, shaken. 'Shake hands' is the standard phrase "
        "(no article needed). 'Shake' has many figurative uses: 'shake off a cold,' "
        "'shake up the industry,' 'shaken but not stirred,' 'shake with fear.' "
        "A 'handshake' is the noun form of the greeting. "
        "Example: They met as strangers, shaking hands politely, and left as friends who would remember that day forever.\n\n"

        "Your 6 new words: faces, pretty, rainbow, really, saying, shaking. "
        "Combined with Session 1, you now have 12 words from 'What a Wonderful World.' "
        "Let's put them to work!"
    )

    # Activities 2-6: flashcards/vocab
    s1["activities"][2]["title"] = "Flashcards: People and Connection"
    s1["activities"][2]["description"] = "Learn 6 words: faces, pretty, rainbow, really, saying, shaking"

    s1["activities"][3]["title"] = "Flashcards: Speak Session 2 Vocabulary"
    s1["activities"][3]["description"] = "Practice saying 6 words: faces, pretty, rainbow, really, saying, shaking"

    s1["activities"][4]["title"] = "Flashcards: Recognize Session 2 Vocabulary"
    s1["activities"][4]["description"] = "Recognize 6 words: faces, pretty, rainbow, really, saying, shaking"

    s1["activities"][5]["title"] = "Flashcards: Recall Session 2 Vocabulary"
    s1["activities"][5]["description"] = "Recall 6 words: faces, pretty, rainbow, really, saying, shaking"

    s1["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 2"
    s1["activities"][6]["description"] = "Master 6 words: faces, pretty, rainbow, really, saying, shaking"

    # Activity 7: introAudio — grammar/usage
    s1["activities"][7]["title"] = "Grammar and Usage: Session 2"
    s1["activities"][7]["description"] = "How to use Session 2 vocabulary naturally in sentences"
    s1["activities"][7]["data"]["text"] = (
        "Excellent! Let's explore how these 6 words behave in real English.\n\n"
        "'Faces' — 'face' as a noun is countable: 'a face,' 'two faces,' 'many faces.' "
        "As a verb, 'face' is regular: face, faced, faced. 'Face up to' means 'to accept and deal with': "
        "'Face up to your responsibilities.' 'Face-to-face' is an adjective/adverb: "
        "'a face-to-face meeting.' 'Faceless' means anonymous or impersonal. "
        "'About-face' means a complete reversal of direction or opinion.\n\n"
        "'Pretty' as an adverb is informal but ubiquitous in spoken English. "
        "'Pretty good,' 'pretty much,' 'pretty sure,' 'pretty well' — these are everyday phrases. "
        "As an adjective, 'pretty' is milder than 'beautiful': 'a pretty flower' vs. 'a beautiful sunset.' "
        "The comparative is 'prettier,' the superlative 'prettiest.' "
        "'Prettify' means to make something look more attractive (often superficially).\n\n"
        "'Rainbow' is a compound noun (rain + bow). It's countable: 'a rainbow,' 'two rainbows.' "
        "The traditional colors are red, orange, yellow, green, blue, indigo, violet — "
        "remembered by the mnemonic 'Roy G. Biv.' 'Rainbow' as an adjective means 'multicolored': "
        "'rainbow sprinkles,' 'a rainbow flag.' 'Double rainbow' is when two arcs appear simultaneously.\n\n"
        "'Really' sits in different positions for different effects. Before an adjective: "
        "'really beautiful' (emphasis). Before a verb: 'I really think so' (sincerity). "
        "As a standalone response: 'Really?' (surprise or disbelief). "
        "'Really and truly' is an emphatic phrase meaning 'genuinely.' "
        "In formal writing, 'truly,' 'genuinely,' or 'indeed' are preferred over 'really.'\n\n"
        "'Saying' — the verb 'say' is irregular: say, said, said. Pronunciation note: "
        "'said' rhymes with 'bed,' not 'paid.' 'Say' takes direct speech ('She said, \"Hello\"') "
        "or reported speech ('She said that she was tired'). 'That is to say' means 'in other words.' "
        "'Needless to say' means 'obviously.' As a noun, 'a saying' is a proverb or maxim.\n\n"
        "'Shaking' — 'shake' is irregular: shake, shook, shaken. "
        "'Shake hands with' is the full phrase: 'I shook hands with the ambassador.' "
        "'Shake' can mean tremble ('shaking with cold'), mix ('shake the bottle'), "
        "or disturb ('the news shook her'). 'Shaky' is the adjective: 'a shaky start,' "
        "'shaky evidence.' 'Shake-up' is a noun meaning a major reorganization."
    )

    # Activity 8-10: reading/speak/listen — keep text, update titles
    s1["activities"][8]["title"] = "Read: What a Wonderful World Lyrics (Part 2)"
    s1["activities"][8]["description"] = "Read the middle verses about people, rainbows, and greetings"

    s1["activities"][9]["title"] = "Speak: Practice the Lyrics (Part 2)"
    s1["activities"][9]["description"] = "Practice speaking the middle verses aloud"

    s1["activities"][10]["title"] = "Listen: What a Wonderful World (Part 2)"
    s1["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s1["activities"][11]["title"] = "Write: Connection and Warmth"
    s1["activities"][11]["description"] = "Write sentences using Session 2 vocabulary"
    ws_items_1 = s1["activities"][11]["data"]["items"]
    ws_items_1[0]["prompt"] = (
        "Use the word 'faces' to write about the people around you — "
        "like Louis Armstrong noticing the beauty in the faces of strangers passing by. "
        "Example: The faces in the old photograph told a story that words never could."
    )
    ws_items_1[1]["prompt"] = (
        "Use the word 'pretty' as an adjective or adverb — "
        "as Louis uses it to describe how the rainbow's colors look in the sky. "
        "Example: The village was pretty in a way that postcards could never capture — you had to stand there and breathe it in."
    )
    ws_items_1[2]["prompt"] = (
        "Use the word 'rainbow' to write about color, variety, or a moment of natural beauty — "
        "like the rainbow Louis celebrates as one of the world's wonders. "
        "Example: After the storm, a perfect rainbow stretched across the valley, and for a moment nobody said a word."
    )
    ws_items_1[3]["prompt"] = (
        "Use the word 'really' to emphasize something genuine or true — "
        "as Louis really, truly means it when he says the world is wonderful. "
        "Example: She didn't really understand the painting until she stood in front of it and let it wash over her."
    )
    ws_items_1[4]["prompt"] = (
        "Use the word 'saying' to write about words spoken between people — "
        "like the friends Louis watches saying 'How do you do?' and 'I love you.' "
        "Example: Sometimes the most powerful thing you can do is keep saying 'I'm here' until someone believes you."
    )
    ws_items_1[5]["prompt"] = (
        "Use the word 'shaking' to write about a greeting, a tremor, or a physical gesture — "
        "like the friends Louis watches shaking hands on the street. "
        "Example: They met as strangers, shaking hands politely, and left as friends who would remember that day forever."
    )

    # ── Session 2: Group 3 — babies, colors, friends, grow, learn, world ──
    s2 = content["learningSessions"][2]
    s2["title"] = "Session 3: Growth and Hope"

    # Activity 0: introAudio — session intro
    s2["activities"][0]["title"] = "Introduction to Session 3"
    s2["activities"][0]["description"] = "Recap Sessions 1-2 and introduce the themes of growth and the future"
    s2["activities"][0]["data"]["text"] = (
        "Welcome to Session 3 — the final learning session before your review! "
        "So far you've learned 12 words from 'What a Wonderful World.' In Session 1, you met "
        "blessed, bloom, bright, sacred, skies, and wonderful — the words of the song's opening, "
        "where Louis Armstrong paints the natural world in strokes of light and color, "
        "turning an ordinary day into something blessed and a dark night into something sacred. "
        "In Session 2, you learned faces, pretty, rainbow, really, saying, and shaking — "
        "the words of the song's middle section, where Louis shifts from nature to people "
        "and finds the same beauty in a handshake as in a sunset.\n\n"
        "Now we reach the song's most hopeful moment. Louis watches babies being born, "
        "watches them grow, and imagines all the things they'll learn — things he'll never "
        "live to see. This is where the song becomes something more than a celebration of "
        "the present. It becomes a love letter to the future. Louis is saying: the world "
        "is wonderful now, and it will be wonderful after I'm gone, because new people "
        "will keep discovering its beauty.\n\n"
        "Your final 6 words: babies, colors, friends, grow, learn, and world. "
        "By the end of this session, you'll have all 18 vocabulary words — and you'll hear "
        "'What a Wonderful World' the way Louis Armstrong intended it to be heard."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s2["activities"][1]["title"] = "Vocabulary Introduction: Session 3"
    s2["activities"][1]["description"] = "Learn 6 words: babies, colors, friends, grow, learn, world"
    s2["activities"][1]["data"]["text"] = (
        "Here are your final 6 vocabulary words, drawn from the most hopeful verses "
        "of 'What a Wonderful World.'\n\n"

        "The first word is 'babies.' It's the plural of 'baby' — a very young child. "
        "Louis watches babies cry and then watches them grow, and in that simple observation "
        "he captures the entire arc of human life. 'Baby' is one of the most emotionally loaded "
        "words in English — it can mean an infant ('a newborn baby'), a term of endearment "
        "('Hey, baby'), or something new and precious ('This project is my baby'). "
        "The adjective form is 'baby' itself: 'baby steps' (small, cautious steps), "
        "'baby blue' (a pale shade of blue). 'Babyish' means immature. "
        "Example: The sound of babies laughing is one of those things that makes even the most cynical person smile.\n\n"

        "The second word is 'colors.' It's the plural of 'color' — the property of objects "
        "that produces different sensations on the eye as a result of the way they reflect light. "
        "Louis sings about the colors of the rainbow and the colors in the faces of people — "
        "using 'colors' as a bridge between nature and humanity. 'Color' is both a noun and a verb: "
        "'What color is it?' (noun), 'Color the picture' (verb). 'Colorful' means vivid or lively: "
        "'a colorful personality.' 'Off-color' means slightly unwell or inappropriate. "
        "Note: British English spells it 'colour.' "
        "Example: The market was an explosion of colors — spices in orange and red, fabrics in blue and gold.\n\n"

        "The third word is 'friends.' It's the plural of 'friend' — a person you know well "
        "and regard with affection and trust. Louis watches friends greeting each other, "
        "and in that simple image he finds one of the world's greatest wonders. "
        "'Friend' is one of the oldest words in English, going back to Old English 'freond.' "
        "'Friendly' is the adjective; 'friendship' is the noun; 'befriend' is the verb "
        "(to become friends with). Common phrases: 'a friend in need is a friend indeed,' "
        "'make friends,' 'just friends,' 'best friend.' "
        "Example: The best friends are the ones who make you feel like no time has passed, even after years apart.\n\n"

        "The fourth word is 'grow.' It's a verb meaning 'to increase in size, number, or degree' "
        "or 'to develop and mature.' Louis watches babies grow — a process that contains "
        "all the wonder and possibility of being alive. 'Grow' is irregular: grow, grew, grown. "
        "It can be intransitive ('The tree grew tall') or transitive ('She grows vegetables'). "
        "'Grow up' means to mature: 'When I grow up, I want to be a pilot.' "
        "'Growth' is the noun; 'growing' as an adjective means 'increasing': 'a growing concern.' "
        "Example: Watching her children grow was like watching a time-lapse of everything she hoped for them.\n\n"

        "The fifth word is 'learn.' It's a verb meaning 'to gain knowledge or skill through study, "
        "experience, or being taught.' Louis imagines all the things the babies will learn — "
        "and in that imagination, he sees the future of the wonderful world. "
        "'Learn' can be regular (learned) or irregular (learnt, mainly British). "
        "It takes various patterns: 'learn something' ('learn English'), 'learn to do something' "
        "('learn to swim'), 'learn from' ('learn from mistakes'). 'Learner' is the noun; "
        "'learning' is both a noun and an adjective: 'a learning experience,' 'lifelong learning.' "
        "Example: The most important thing she learned in college wasn't in any textbook — it was how to ask the right questions.\n\n"

        "The sixth and final word is 'world.' It's a noun meaning 'the earth, together with all "
        "of its countries, peoples, and natural features.' This is the word that gives the song "
        "its title and its meaning. Louis doesn't say 'what a wonderful country' or 'what a wonderful city' — "
        "he says 'world,' encompassing everything and everyone. 'World' has rich figurative uses: "
        "'the world of music,' 'a world of difference,' 'out of this world' (extraordinary), "
        "'the whole world' (everyone). 'Worldly' means experienced and sophisticated. "
        "Example: She traveled the world looking for beauty and found it had been in her backyard all along.\n\n"

        "And there you have it — all 18 words: blessed, bloom, bright, sacred, skies, wonderful, "
        "faces, pretty, rainbow, really, saying, shaking, babies, colors, friends, grow, learn, "
        "and world. You now have the complete vocabulary of 'What a Wonderful World.' "
        "Let's practice these final 6!"
    )

    # Activities 2-6: flashcards/vocab
    s2["activities"][2]["title"] = "Flashcards: Growth and Hope"
    s2["activities"][2]["description"] = "Learn 6 words: babies, colors, friends, grow, learn, world"

    s2["activities"][3]["title"] = "Flashcards: Speak Session 3 Vocabulary"
    s2["activities"][3]["description"] = "Practice saying 6 words: babies, colors, friends, grow, learn, world"

    s2["activities"][4]["title"] = "Flashcards: Recognize Session 3 Vocabulary"
    s2["activities"][4]["description"] = "Recognize 6 words: babies, colors, friends, grow, learn, world"

    s2["activities"][5]["title"] = "Flashcards: Recall Session 3 Vocabulary"
    s2["activities"][5]["description"] = "Recall 6 words: babies, colors, friends, grow, learn, world"

    s2["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 3"
    s2["activities"][6]["description"] = "Master 6 words: babies, colors, friends, grow, learn, world"

    # Activity 7: introAudio — grammar/usage
    s2["activities"][7]["title"] = "Grammar and Usage: Session 3"
    s2["activities"][7]["description"] = "How to use Session 3 vocabulary naturally in sentences"
    s2["activities"][7]["data"]["text"] = (
        "Let's look at how these final 6 words work in English grammar.\n\n"
        "'Babies' — 'baby' follows the standard rule for nouns ending in consonant + y: "
        "change 'y' to 'ies.' Baby → babies. As a verb, 'baby' means 'to treat with excessive care': "
        "'Don't baby me.' 'Baby' as an adjective: 'baby teeth,' 'baby shower,' 'baby boom' "
        "(a period of high birth rates). 'Babysit' means to care for children temporarily. "
        "'Babe' is an informal synonym, also used as a term of endearment.\n\n"
        "'Colors' — 'color' as a verb means 'to fill with color' or 'to influence': "
        "'Don't let bias color your judgment.' 'Colorful' means vivid or interesting: "
        "'a colorful character.' 'Colorless' means dull or lacking interest. "
        "'Color-blind' means unable to distinguish certain colors, or figuratively, "
        "not influenced by race. 'True colors' means someone's real character: "
        "'She showed her true colors under pressure.'\n\n"
        "'Friends' — 'friend' as a verb is used in social media: 'She friended me on Facebook.' "
        "'Unfriend' means to remove someone. 'Friendly' can be an adjective ('a friendly smile') "
        "or a noun in gaming ('friendly fire' — accidentally attacking your own side). "
        "'Befriend' means to become friends with someone. 'Friendless' means having no friends. "
        "'Friendship' is the noun: 'a lifelong friendship.'\n\n"
        "'Grow' is irregular: grow, grew, grown. Phrasal verbs: 'grow up' (mature), "
        "'grow into' (become suited to), 'grow out of' (become too big or mature for), "
        "'grow on' (become gradually more liked): 'The song grew on me.' "
        "'Grown-up' is a noun/adjective meaning adult. 'Outgrow' means to grow too large for "
        "or to leave behind: 'She outgrew her childhood fears.'\n\n"
        "'Learn' — 'learn' can take a direct object ('learn a language'), an infinitive "
        "('learn to cook'), or a clause ('I learned that patience matters'). "
        "'Learn by heart' means to memorize. 'Learn the hard way' means to learn through "
        "painful experience. 'Learned' (two syllables, 'learn-ed') as an adjective means "
        "'scholarly': 'a learned professor.' 'Learning curve' describes the rate of progress.\n\n"
        "'World' — 'world' is usually singular: 'the world,' 'a world of difference.' "
        "Plural 'worlds' appears in: 'worlds apart' (very different), 'the best of both worlds,' "
        "'other worlds' (planets or dimensions). 'Worldwide' means 'across the entire world.' "
        "'Worldly' means experienced or materialistic. 'World-class' means among the best. "
        "'World-weary' means tired of life's difficulties."
    )

    # Activity 8-10: reading/speak/listen
    s2["activities"][8]["title"] = "Read: What a Wonderful World Lyrics (Part 3)"
    s2["activities"][8]["description"] = "Read the final verses about babies, growth, and the future"

    s2["activities"][9]["title"] = "Speak: Practice the Lyrics (Part 3)"
    s2["activities"][9]["description"] = "Practice speaking the final verses aloud"

    s2["activities"][10]["title"] = "Listen: What a Wonderful World (Part 3)"
    s2["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s2["activities"][11]["title"] = "Write: Growth and the Future"
    s2["activities"][11]["description"] = "Write sentences using Session 3 vocabulary"
    ws_items_2 = s2["activities"][11]["data"]["items"]
    ws_items_2[0]["prompt"] = (
        "Use the word 'babies' to write about new life, beginnings, or innocence — "
        "like Louis Armstrong watching babies cry and imagining all they'll become. "
        "Example: The sound of babies laughing is one of those things that makes even the most cynical person smile."
    )
    ws_items_2[1]["prompt"] = (
        "Use the word 'colors' to write about variety, vividness, or visual beauty — "
        "like the colors of the rainbow that Louis sees in the sky and in people's faces. "
        "Example: The market was an explosion of colors — spices in orange and red, fabrics in blue and gold."
    )
    ws_items_2[2]["prompt"] = (
        "Use the word 'friends' to write about the people who matter most — "
        "like the friends Louis watches greeting each other with warmth and love. "
        "Example: The best friends are the ones who make you feel like no time has passed, even after years apart."
    )
    ws_items_2[3]["prompt"] = (
        "Use the word 'grow' to write about development, change, or maturation — "
        "like Louis watching babies grow and seeing the future unfold. "
        "Example: Watching her children grow was like watching a time-lapse of everything she hoped for them."
    )
    ws_items_2[4]["prompt"] = (
        "Use the word 'learn' to write about gaining knowledge or understanding — "
        "like Louis imagining all the things the next generation will learn. "
        "Example: The most important thing she learned in college wasn't in any textbook — it was how to ask the right questions."
    )
    ws_items_2[5]["prompt"] = (
        "Use the word 'world' to write about the earth, humanity, or the totality of experience — "
        "the very word Louis chose to name everything he finds wonderful. "
        "Example: She traveled the world looking for beauty and found it had been in her backyard all along."
    )

    # ── Session 3: Review (4 activities) ──
    s3 = content["learningSessions"][3]
    s3["title"] = "Review"

    s3["activities"][0]["title"] = "Congratulations and Review"
    s3["activities"][0]["description"] = "Celebrate your progress and prepare for the full review"
    s3["activities"][0]["data"]["text"] = (
        "Congratulations! You've learned all 18 vocabulary words from 'What a Wonderful World.' "
        "Let's take a moment to look back at what you've accomplished.\n\n"
        "In Session 1, you learned blessed, bloom, bright, sacred, skies, and wonderful — "
        "the words of the song's opening, where Louis Armstrong turns an ordinary day into "
        "a canvas of light and color, finding holiness in both the bright day and the dark night.\n\n"
        "In Session 2, you learned faces, pretty, rainbow, really, saying, and shaking — "
        "the words of the song's middle section, where Louis shifts from nature to people "
        "and discovers that a handshake between friends is just as wonderful as a rainbow.\n\n"
        "In Session 3, you learned babies, colors, friends, grow, learn, and world — "
        "the words of the song's most hopeful moment, where Louis watches new life enter "
        "the world and imagines all the beauty still to come.\n\n"
        "Now it's time to review all 18 words together. This review session will test your "
        "recognition and recall across all three groups. After this, you'll be ready to read "
        "the complete lyrics in the final session. Let's go!"
    )

    s3["activities"][1]["title"] = "Flashcards: Review All 18 Words"
    s3["activities"][1]["description"] = "Review all 18 vocabulary words from What a Wonderful World"

    s3["activities"][2]["title"] = "Flashcards: Recognize All Vocabulary"
    s3["activities"][2]["description"] = "Test your recognition of all 18 words"

    s3["activities"][3]["title"] = "Flashcards: Recall All Vocabulary"
    s3["activities"][3]["description"] = "Test your recall of all 18 words"

    # ── Session 4: Full reading + farewell (5 activities) ──
    s4 = content["learningSessions"][4]
    s4["title"] = "Full Lyrics Reading"

    s4["activities"][0]["title"] = "Introduction to the Complete Reading"
    s4["activities"][0]["description"] = "Prepare for reading the full What a Wonderful World lyrics"
    s4["activities"][0]["data"]["text"] = (
        "Welcome to the final session! This is the moment everything comes together. "
        "Over the past three sessions, you've built a vocabulary of 18 words drawn directly "
        "from the lyrics of 'What a Wonderful World.' You've learned their meanings, practiced their "
        "pronunciation, explored their grammar, and used them in your own writing.\n\n"
        "Now you're going to read the complete lyrics — all three sections combined into one "
        "continuous passage. As you read, you'll encounter every single one of your 18 words "
        "in context. This time, they won't be new — they'll be familiar friends.\n\n"
        "Here are all 18 words you'll see: blessed, bloom, bright, sacred, skies, wonderful, "
        "faces, pretty, rainbow, really, saying, shaking, babies, colors, friends, grow, learn, "
        "and world.\n\n"
        "Take your time with the reading. Let Louis's voice come through the words. "
        "And remember — the world is wonderful, if you just slow down enough to notice."
    )

    s4["activities"][1]["title"] = "Read: Complete What a Wonderful World Lyrics"
    s4["activities"][1]["description"] = "Read the full lyrics from beginning to end"

    s4["activities"][2]["title"] = "Speak: Practice the Complete Lyrics"
    s4["activities"][2]["description"] = "Practice speaking the entire lyrics aloud"

    s4["activities"][3]["title"] = "Listen: Complete What a Wonderful World"
    s4["activities"][3]["description"] = "Listen to the complete lyrics and follow along"

    s4["activities"][4]["title"] = "Farewell and Vocabulary Review"
    s4["activities"][4]["description"] = "Final review of all 18 words and farewell"
    s4["activities"][4]["data"]["text"] = (
        "You've done it — you've completed the entire 'What a Wonderful World' vocabulary course! "
        "Let's do one final review of all 18 words before we say goodbye.\n\n"

        "'Blessed' — fortunate, happy, or made holy. "
        "Example: On quiet mornings like this, she felt blessed just to be alive and watching the light change.\n\n"
        "'Bloom' — to produce flowers; to flourish and develop. "
        "Example: The old rose bush bloomed every May without fail, as if keeping a promise to the garden.\n\n"
        "'Bright' — giving out light; intelligent; promising. "
        "Example: His bright eyes told you everything — he was curious about the world and couldn't hide it.\n\n"
        "'Sacred' — connected with the divine; too important to be interfered with. "
        "Example: Sunday mornings were sacred in their family — no phones, no plans, just pancakes and conversation.\n\n"
        "'Skies' — the region of the atmosphere; the heavens above. "
        "Example: Under the wide open skies of Montana, every problem she had seemed to shrink to nothing.\n\n"
        "'Wonderful' — inspiring delight and admiration; full of wonder. "
        "Example: The wonderful thing about old friendships is that you can pick up exactly where you left off.\n\n"

        "'Faces' — the front parts of heads; surfaces; aspects. "
        "Example: She remembered the faces of her students long after she forgot their names.\n\n"
        "'Pretty' — attractive in a delicate way; fairly or quite (as adverb). "
        "Example: The solution was pretty simple once they stopped overthinking it.\n\n"
        "'Rainbow' — an arch of colors in the sky; a wide variety. "
        "Example: The children drew rainbows on the sidewalk with chalk, turning the whole street into a gallery.\n\n"
        "'Really' — in actual fact; very; truly. "
        "Example: He didn't really know what he wanted until he lost it.\n\n"
        "'Saying' — speaking words; a well-known phrase or proverb. "
        "Example: There's an old saying that the best time to plant a tree was twenty years ago.\n\n"
        "'Shaking' — trembling; grasping and moving someone's hand as a greeting. "
        "Example: His voice was shaking, but he stood up and spoke anyway — and that made all the difference.\n\n"

        "'Babies' — very young children; new beginnings. "
        "Example: The hospital was full of new babies that morning, and every single one of them was a miracle.\n\n"
        "'Colors' — the properties of light that create visual sensations; varieties. "
        "Example: Autumn paints the mountains in colors so vivid they look like they belong in a dream.\n\n"
        "'Friends' — people you know well and regard with affection. "
        "Example: The friends who stayed through the hard years were the ones she treasured most.\n\n"
        "'Grow' — to increase in size; to develop and mature. "
        "Example: Gardens grow best when you give them sunlight, water, and the patience to wait.\n\n"
        "'Learn' — to gain knowledge or skill through experience. "
        "Example: Every mistake she made taught her something, and eventually she learned to be grateful for all of them.\n\n"
        "'World' — the earth and everything in it; the totality of human experience. "
        "Example: He saw the world not as it was, but as it could be — and that vision changed everyone around him.\n\n"

        "Thank you for learning with Louis Armstrong's 'What a Wonderful World.' "
        "You came for 18 vocabulary words, but I hope you're leaving with something more — "
        "a pair of eyes that sees a little differently. Louis Armstrong didn't have an easy life. "
        "He had every reason to be bitter, every reason to look at the world and see only "
        "what was broken. Instead, he chose to see green trees, red roses, blue skies, "
        "and the faces of friends. That choice — to notice beauty when it would be easier "
        "to notice pain — is the real lesson of this song. "
        "Keep reading, keep speaking, keep writing — and every now and then, "
        "stop what you're doing, look around, and think to yourself: what a wonderful world."
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
    print(f"Created en-en What a Wonderful World curriculum: {cid}")
    return cid


if __name__ == "__main__":
    create()
