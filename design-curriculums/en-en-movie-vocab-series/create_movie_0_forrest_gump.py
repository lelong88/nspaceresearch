"""
Create en-en movie curriculum #0: Forrest Gump
Mirror of vi-en source 5MsWSZwcWGYpfnrO — all Vietnamese UI text rewritten in English.

Source movie: Forrest Gump (1994)
YouTube: https://www.youtube.com/watch?v=vdtqSaJO-iM

18 vocabulary words in 3 groups of 6 (same as vi-en source):
  Group 1: chocolate, comfortable, million, bet, wish, shoes
  Group 2: awful, worn, remember, smart, explain, understand
  Group 3: vacation, dying, meals, combs, strangers, love

All user-facing text in English. Reading passages stay as-is (already English).
Vocabulary words stay as-is (already English).

Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 9.1, 9.2, 9.3, 9.4, 9.5
"""

import sys, json, requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"
SOURCE_ID = "5MsWSZwcWGYpfnrO"

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

    # Every activity has title, description, practiceMinutes
    for i, session in enumerate(content["learningSessions"]):
        if "title" not in session:
            errors.append(f"Session {i} missing title")
        for j, act in enumerate(session["activities"]):
            for field in ("title", "description", "practiceMinutes"):
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
    content["title"] = "'Forrest Gump' — Life Is Like a Box of Chocolates"

    content["description"] = (
        "HAVE YOU EVER FELT LIKE LIFE KEEPS HANDING YOU SURPRISES "
        "YOU NEVER SAW COMING?\n\n"
        "Every morning you wake up facing choices no one can predict — "
        "the job you take, the stranger you sit next to on a bench, "
        "the offhand remark that rewrites your entire story. "
        "Forrest Gump sits at a bus stop with a box of chocolates on his lap "
        "and tells his life story to anyone who'll listen — and every single line "
        "carries a lesson that millions of people still carry with them thirty years later.\n\n"
        "Imagine not just watching the film, but UNDERSTANDING every word Forrest says — "
        "from 'comfortable' when he compliments a stranger's shoes, "
        "to 'remember' when he recalls his very first pair, "
        "to 'love' when he delivers the most famous line in the movie: "
        "'I'm not a smart man, but I know what love is.' "
        "Each vocabulary word is a doorway into the emotional world of the film.\n\n"
        "When you realize that 'awful' in 'an awful lot' doesn't mean 'terrible' "
        "but 'a huge amount' — you'll start hearing English with completely new ears. "
        "That's the moment cinema becomes your greatest teacher.\n\n"
        "18 vocabulary words drawn directly from the film's dialogue, combined with "
        "a multi-sensory learning method — listening, reading, speaking, writing — "
        "so you sharpen your English while carrying Forrest Gump's beautifully simple "
        "philosophy of life in your heart."
    )

    content["preview"] = {
        "text": (
            "Remember the scene where Forrest Gump sits on a bus-stop bench, "
            "a box of chocolates on his lap, telling his life story to anyone who sits down?\n\n"
            "18 English vocabulary words you'll learn: chocolate, comfortable, million, bet, wish, "
            "shoes, awful, worn, remember, smart, explain, understand, vacation, dying, meals, "
            "combs, strangers, love.\n\n"
            "Across 5 sessions you'll read Forrest's actual dialogue, discover how he uses "
            "the simplest words to say the most profound things — from his very first pair of shoes "
            "to the truest love he's ever known.\n\n"
            "Tap the link below to watch the original scene — after this course, "
            "you'll hear Forrest tell his story and understand every single word naturally."
        )
    }

    content["contentTypeTags"] = ["movie"]
    content["is_public"] = False

    # ── Session 0: Group 1 — chocolate, comfortable, million, bet, wish, shoes ──
    s0 = content["learningSessions"][0]
    s0["title"] = "Session 1: Life Is Like a Box of Chocolates"

    # Activity 0: introAudio — scene intro
    s0["activities"][0]["title"] = "Introduction to the Film Scene"
    s0["activities"][0]["description"] = "Setting the stage for the iconic bus-stop scene from Forrest Gump"
    s0["activities"][0]["data"]["text"] = (
        "Welcome to the vocabulary-through-cinema course! Today we begin with one of "
        "the most iconic scenes in Hollywood history — the bus-stop bench scene from "
        "'Forrest Gump.' The 1994 film starring Tom Hanks won six Academy Awards and "
        "gave the world a line that has become part of everyday English: 'Life is like "
        "a box of chocolates. You never know what you're gonna get.'\n\n"
        "In this scene, Forrest sits on a bench waiting for a bus, a box of chocolates "
        "balanced on his lap, and begins telling his life story to complete strangers. "
        "What makes the scene so powerful is the contrast between Forrest's simple way "
        "of speaking and the extraordinary depth of what he's actually saying. He talks "
        "about shoes, about his mama's wisdom, about luck and destiny — all in words "
        "a child could understand, yet every sentence carries a weight that stays with you.\n\n"
        "In this first session, you'll learn 6 vocabulary words that appear in Forrest's "
        "dialogue: chocolate, comfortable, million, bet, wish, and shoes. Each word is "
        "woven into the fabric of the scene, and by the end of this session you'll hear "
        "them the way Forrest means them — not just as dictionary entries, but as pieces "
        "of a philosophy about life, kindness, and the surprises that shape who we become."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s0["activities"][1]["title"] = "Vocabulary Introduction: Session 1"
    s0["activities"][1]["description"] = "Learn 6 words: chocolate, comfortable, million, bet, wish, shoes"
    s0["activities"][1]["data"]["text"] = (
        "Let's dive into the first 6 vocabulary words from the bus-stop scene in 'Forrest Gump.' "
        "Each word comes straight from Forrest's dialogue, and understanding how he uses them "
        "will change the way you hear everyday English.\n\n"

        "The first word is 'chocolate.' It's a noun — a sweet food made from cacao beans. "
        "But in this film, chocolate is so much more than candy. Forrest opens the entire scene "
        "by offering a chocolate to the stranger sitting next to him: 'Do you want a chocolate? "
        "I could eat about a million and a half of these.' The box of chocolates on his lap "
        "becomes the film's central metaphor — life is unpredictable, just like reaching into "
        "a box without knowing which flavor you'll get. You can use 'chocolate' as a countable "
        "noun ('a chocolate,' 'two chocolates') when talking about individual pieces, or as an "
        "uncountable noun ('I love chocolate') when talking about the substance in general. "
        "Example: She bought a box of chocolates for her mother's birthday.\n\n"

        "The second word is 'comfortable.' It's an adjective meaning 'providing physical ease "
        "and relaxation.' Forrest notices a woman's shoes on the bench and says: 'Those must be "
        "comfortable shoes. I'll bet you could walk all day in shoes like that and not feel a thing.' "
        "It's a small, kind observation — the kind of thing most people wouldn't bother saying — "
        "but it tells you everything about Forrest's character. He notices people. He cares about "
        "their comfort. The word has three syllables: COM-for-ta-ble (though in casual speech, "
        "many native speakers say 'COMF-ter-ble,' dropping the middle vowel). "
        "Example: After a long flight, all I wanted was a comfortable chair and a cup of tea.\n\n"

        "The third word is 'million.' It's a noun and adjective meaning 'one thousand thousands — "
        "the number 1,000,000.' Forrest uses it with playful exaggeration: 'I could eat about "
        "a million and a half of these.' He doesn't literally mean 1.5 million chocolates — "
        "he's expressing how much he loves them. This kind of hyperbole is extremely common "
        "in spoken English. People say 'I've told you a million times' or 'There were a million "
        "people at the concert' without meaning the exact number. "
        "Example: The startup raised two million dollars in its first round of funding.\n\n"

        "The fourth word is 'bet.' It can be a verb or a noun. As a verb, it means 'to risk "
        "something on an uncertain outcome' or, more casually, 'to be fairly sure about something.' "
        "Forrest says: 'I'll bet you could walk all day in shoes like that.' He's not gambling — "
        "he's expressing confidence. This casual use of 'bet' is everywhere in English: "
        "'I bet it's going to rain,' 'I bet she already knows.' As a noun: 'That's a safe bet.' "
        "Example: I bet you didn't know that Forrest Gump was based on a novel.\n\n"

        "The fifth word is 'wish.' It's both a verb and a noun meaning 'to want something that "
        "is not easily attainable' or 'a desire or hope.' Forrest talks about wishing he had "
        "shoes as nice as the ones he sees. A wish carries a sense of longing — it's not just "
        "wanting something, it's wanting something you might not get. 'I wish I could fly.' "
        "'Make a wish before you blow out the candles.' The verb often appears in the subjunctive: "
        "'I wish I were taller' (not 'I wish I was,' though both are used in casual speech). "
        "Example: She closed her eyes and made a wish before tossing the coin into the fountain.\n\n"

        "The sixth and final word for this session is 'shoes.' It's a plural noun — coverings "
        "for the feet. In Forrest Gump, shoes are a recurring symbol. Mama puts leg braces on "
        "young Forrest's shoes. Jenny tells him to run. His shoes carry him across a football "
        "field, through Vietnam, and across the entire United States. When Forrest says 'Mama "
        "always said you can tell a lot about a person by their shoes — where they go, where "
        "they've been,' he's really talking about life journeys. "
        "Example: He laced up his running shoes and headed out into the morning fog.\n\n"

        "So there you have it — your first 6 words: chocolate, comfortable, million, bet, wish, "
        "and shoes. Each one is simple on the surface, but in Forrest's mouth they become "
        "something deeper. Let's practice them now!"
    )

    # Activities 2-6: flashcards/vocab — just update titles and descriptions
    s0["activities"][2]["title"] = "Flashcards: Life Is Like a Box of Chocolates"
    s0["activities"][2]["description"] = "Learn 6 words: chocolate, comfortable, million, bet, wish, shoes"

    s0["activities"][3]["title"] = "Flashcards: Speak Session 1 Vocabulary"
    s0["activities"][3]["description"] = "Practice saying 6 words: chocolate, comfortable, million, bet, wish, shoes"

    s0["activities"][4]["title"] = "Flashcards: Recognize Session 1 Vocabulary"
    s0["activities"][4]["description"] = "Recognize 6 words: chocolate, comfortable, million, bet, wish, shoes"

    s0["activities"][5]["title"] = "Flashcards: Recall Session 1 Vocabulary"
    s0["activities"][5]["description"] = "Recall 6 words: chocolate, comfortable, million, bet, wish, shoes"

    s0["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 1"
    s0["activities"][6]["description"] = "Master 6 words: chocolate, comfortable, million, bet, wish, shoes"

    # Activity 7: introAudio — grammar/usage
    s0["activities"][7]["title"] = "Grammar and Usage: Session 1"
    s0["activities"][7]["description"] = "How to use Session 1 vocabulary naturally in sentences"
    s0["activities"][7]["data"]["text"] = (
        "Great work! You've met your first 6 words. Now let's look at how they work "
        "in real English sentences, using Forrest Gump's dialogue as our guide.\n\n"
        "'Chocolate' is a countable noun when referring to individual pieces — 'a chocolate,' "
        "'two chocolates' — and uncountable when referring to the substance: 'I love chocolate.' "
        "Forrest uses it both ways. The phrase 'a box of chocolates' is countable (individual pieces). "
        "Common collocations: chocolate cake, chocolate chip, hot chocolate, dark chocolate.\n\n"
        "'Comfortable' often follows linking verbs: 'These shoes are comfortable,' 'I feel comfortable.' "
        "It can also precede nouns: 'a comfortable chair,' 'a comfortable silence.' "
        "The opposite is 'uncomfortable.' In casual speech, it's often shortened to three syllables: "
        "'COMF-ter-ble.' Forrest's line — 'Those must be comfortable shoes' — uses 'must be' "
        "to express a confident guess, a very common English pattern.\n\n"
        "'Million' works as both a noun and an adjective. With a number: 'two million people' "
        "(no 's'). Without a number: 'millions of people' (with 's'). Forrest's 'a million and a half' "
        "is hyperbole — exaggeration for effect. This is one of the most natural things in spoken English.\n\n"
        "'Bet' in casual speech almost always means 'I'm fairly sure': 'I bet you're tired,' "
        "'I'll bet it rains tomorrow.' The formal meaning — wagering money — still exists but is "
        "less common in everyday conversation. 'You bet!' as a standalone phrase means 'Absolutely!'\n\n"
        "'Wish' takes the subjunctive in formal English: 'I wish I were there' (not 'was'). "
        "In everyday speech, both forms are accepted. 'Wish' + past tense talks about the present: "
        "'I wish I had more time.' 'Wish' + past perfect talks about the past: "
        "'I wish I had studied harder.' 'Wish' + 'would' expresses frustration: "
        "'I wish it would stop raining.'\n\n"
        "'Shoes' is almost always plural — you rarely talk about a single shoe unless one is lost. "
        "Common phrases: 'in someone's shoes' (empathy), 'fill someone's shoes' (replace someone), "
        "'if the shoe fits' (if the description applies to you). Forrest's mama uses shoes as a "
        "metaphor for life's journey — and that metaphor runs through the entire film."
    )

    # Activity 8: reading — keep text as-is (already English), update title/description
    s0["activities"][8]["title"] = "Read: Forrest Gump Excerpt (Part 1)"
    s0["activities"][8]["description"] = "Read the bus-stop bench dialogue from Forrest Gump"

    # Activity 9: speakReading
    s0["activities"][9]["title"] = "Speak: Practice the Dialogue (Part 1)"
    s0["activities"][9]["description"] = "Practice speaking the bus-stop bench dialogue aloud"

    # Activity 10: readAlong
    s0["activities"][10]["title"] = "Listen: Forrest Gump Excerpt (Part 1)"
    s0["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s0["activities"][11]["title"] = "Write: Life and Surprises"
    s0["activities"][11]["description"] = "Write sentences using Session 1 vocabulary"
    ws_items_0 = s0["activities"][11]["data"]["items"]
    ws_items_0[0]["prompt"] = (
        "Use the word 'chocolate' to write about something unexpectedly sweet in life — "
        "just as Forrest offers chocolates to strangers without expecting anything in return. "
        "Example: Life handed me a chocolate I never expected — a phone call from an old friend "
        "on the loneliest night of the year."
    )
    ws_items_0[1]["prompt"] = (
        "Use the word 'comfortable' to describe a feeling of ease or belonging — "
        "like Forrest noticing a stranger's shoes and imagining how good they must feel. "
        "Example: After years of moving from city to city, I finally found a place "
        "where I felt truly comfortable."
    )
    ws_items_0[2]["prompt"] = (
        "Use the word 'million' to express a large quantity or exaggeration — "
        "the way Forrest says he could eat 'a million and a half' chocolates. "
        "Example: I must have checked my phone a million times before the results came out."
    )
    ws_items_0[3]["prompt"] = (
        "Use the word 'bet' to express confidence about something — "
        "like Forrest saying 'I'll bet you could walk all day in shoes like that.' "
        "Example: I bet she practiced that speech a hundred times before stepping on stage."
    )
    ws_items_0[4]["prompt"] = (
        "Use the word 'wish' to talk about a longing or desire — "
        "the way Forrest wishes he had shoes as nice as the ones he sees. "
        "Example: Sometimes I wish I could go back to that summer and live it all over again."
    )
    ws_items_0[5]["prompt"] = (
        "Use the word 'shoes' to talk about journeys or empathy — "
        "as Mama tells Forrest you can tell a lot about a person by their shoes. "
        "Example: You never really understand someone until you've walked a mile in their shoes."
    )

    # ── Session 1: Group 2 — awful, worn, remember, smart, explain, understand ──
    s1 = content["learningSessions"][1]
    s1["title"] = "Session 2: Shoes and Mama's Wisdom"

    # Activity 0: introAudio — session intro
    s1["activities"][0]["title"] = "Introduction to Session 2"
    s1["activities"][0]["description"] = "Recap Session 1 and introduce the theme of memory and wisdom"
    s1["activities"][0]["data"]["text"] = (
        "Welcome back to Session 2! In our first session, you learned 6 words from the "
        "bus-stop bench scene: chocolate, comfortable, million, bet, wish, and shoes. "
        "You discovered how Forrest uses the simplest language to say the most profound things — "
        "offering chocolates to strangers, admiring someone's shoes, and quoting his mama's "
        "philosophy about life's unpredictability.\n\n"
        "Now we're going deeper into Forrest's story. In this part of the film, Forrest "
        "remembers his childhood — the leg braces, the first pair of shoes, and the moment "
        "his mama explained the world to him in words he could understand. Mama is the heart "
        "of the film. She's the one who teaches Forrest that being different isn't a weakness, "
        "that intelligence isn't the only kind of smart, and that life will always find a way "
        "to surprise you.\n\n"
        "Today you'll learn 6 new words: awful, worn, remember, smart, explain, and understand. "
        "These words carry the emotional weight of Forrest's childhood memories — and by the end "
        "of this session, you'll hear them echoing through every scene in the film."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s1["activities"][1]["title"] = "Vocabulary Introduction: Session 2"
    s1["activities"][1]["description"] = "Learn 6 words: awful, worn, remember, smart, explain, understand"
    s1["activities"][1]["data"]["text"] = (
        "Let's learn 6 new vocabulary words from the next part of Forrest Gump's story — "
        "the scenes where he remembers his childhood and his mama's wisdom.\n\n"

        "The first word is 'awful.' It's an adjective that means 'very bad or unpleasant.' "
        "But here's the twist — in Forrest Gump, the word appears in the phrase 'an awful lot,' "
        "which doesn't mean 'a terrible amount.' It means 'a very large amount.' Forrest says: "
        "'That's an awful lot of running.' This double meaning catches many learners off guard. "
        "'Awful' by itself is negative: 'The weather was awful.' But 'an awful lot of' is "
        "intensifying — it means 'a huge quantity of.' This is one of those English quirks "
        "that you just have to know. Other examples: 'She spends an awful lot of time reading.' "
        "'There were an awful lot of people at the park.' "
        "Example: He went through an awful lot of trouble to make her birthday special.\n\n"

        "The second word is 'worn.' It's the past participle of 'wear,' used as an adjective "
        "meaning 'damaged or shabby from use.' Forrest's first shoes are worn — they've been "
        "through miles of walking, running, and living. When something is 'worn,' it tells a story. "
        "A worn book has been read many times. A worn path has been walked by many feet. "
        "'Worn out' means exhausted: 'I'm completely worn out after that hike.' "
        "Example: The worn leather of his father's wallet still smelled faintly of cedar.\n\n"

        "The third word is 'remember.' It's a verb meaning 'to recall from memory.' "
        "Forrest is a storyteller — the entire film is built on his memories. 'I remember' "
        "is how he introduces each chapter of his life. The word carries warmth and nostalgia "
        "in this context. 'Remember' can take a gerund: 'I remember meeting her for the first time.' "
        "Or an infinitive (with a different meaning): 'Remember to lock the door' (don't forget). "
        "Example: I still remember the smell of my grandmother's kitchen on Sunday mornings.\n\n"

        "The fourth word is 'smart.' It's an adjective meaning 'intelligent' or 'clever.' "
        "One of the most heartbreaking and beautiful lines in the film is: 'I'm not a smart man, "
        "but I know what love is.' Forrest knows he isn't book-smart — his IQ is below average — "
        "but he has a kind of emotional intelligence that the 'smart' people around him lack. "
        "The word can also mean 'well-dressed' in British English, or 'sharp' as in 'a smart decision.' "
        "Example: She made the smart choice to save her money instead of spending it all at once.\n\n"

        "The fifth word is 'explain.' It's a verb meaning 'to make something clear or understandable.' "
        "Mama explains the world to Forrest in simple terms he can grasp. She doesn't use big words "
        "or complicated theories — she uses metaphors. 'Life is like a box of chocolates.' "
        "That's explaining at its finest. 'Explain' is followed by a noun or a clause: "
        "'Can you explain the rules?' 'She explained why she was late.' Never say 'explain me' — "
        "it's 'explain to me' or 'explain it.' "
        "Example: The teacher explained the concept so clearly that even the youngest students understood.\n\n"

        "The sixth word is 'understand.' It's a verb meaning 'to comprehend the meaning of something.' "
        "Forrest may not understand everything the world throws at him, but he understands "
        "the things that matter most — loyalty, love, and keeping your promises. "
        "'Understand' is irregular: understand, understood, understood. "
        "Common patterns: 'I understand what you mean,' 'Do you understand?' "
        "'It's understandable' (adjective form). "
        "Example: It took me years to understand what my father was really trying to teach me.\n\n"

        "Your 6 new words: awful, worn, remember, smart, explain, understand. "
        "Combined with Session 1, you now have 12 words from Forrest Gump's world. "
        "Let's put them to work!"
    )

    # Activities 2-6: flashcards/vocab
    s1["activities"][2]["title"] = "Flashcards: Shoes and Mama's Wisdom"
    s1["activities"][2]["description"] = "Learn 6 words: awful, worn, remember, smart, explain, understand"

    s1["activities"][3]["title"] = "Flashcards: Speak Session 2 Vocabulary"
    s1["activities"][3]["description"] = "Practice saying 6 words: awful, worn, remember, smart, explain, understand"

    s1["activities"][4]["title"] = "Flashcards: Recognize Session 2 Vocabulary"
    s1["activities"][4]["description"] = "Recognize 6 words: awful, worn, remember, smart, explain, understand"

    s1["activities"][5]["title"] = "Flashcards: Recall Session 2 Vocabulary"
    s1["activities"][5]["description"] = "Recall 6 words: awful, worn, remember, smart, explain, understand"

    s1["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 2"
    s1["activities"][6]["description"] = "Master 6 words: awful, worn, remember, smart, explain, understand"

    # Activity 7: introAudio — grammar/usage
    s1["activities"][7]["title"] = "Grammar and Usage: Session 2"
    s1["activities"][7]["description"] = "How to use Session 2 vocabulary naturally in sentences"
    s1["activities"][7]["data"]["text"] = (
        "Excellent! Let's explore how these 6 words behave in real English.\n\n"
        "'Awful' has two distinct uses. As a pure adjective: 'an awful day,' 'awful news.' "
        "As an intensifier in 'an awful lot of': 'an awful lot of money,' 'an awful lot of work.' "
        "Don't confuse them — context makes it clear. 'Awfully' as an adverb can also intensify: "
        "'awfully kind,' 'awfully sorry.'\n\n"
        "'Worn' functions as both past participle and adjective. Past participle: 'I've worn this "
        "jacket for ten years.' Adjective: 'a worn carpet,' 'worn-out shoes.' "
        "The phrasal verb 'wear out' means to exhaust or to use until damaged: "
        "'The children wore me out,' 'These tires are worn out.'\n\n"
        "'Remember' pairs with gerunds for past events: 'I remember seeing the ocean for the first time.' "
        "With infinitives, it means 'don't forget': 'Remember to call your mother.' "
        "This gerund/infinitive distinction changes the meaning entirely — a classic English trap.\n\n"
        "'Smart' collocates with many nouns: 'smart decision,' 'smart phone,' 'smart casual.' "
        "In American English it primarily means 'intelligent.' In British English it can also mean "
        "'well-dressed' or 'neat.' 'Street smart' vs. 'book smart' is a common distinction.\n\n"
        "'Explain' never takes a direct personal object without 'to': say 'explain it to me,' "
        "never 'explain me it.' Common structures: 'explain how/why/what,' "
        "'explain the difference between X and Y.'\n\n"
        "'Understand' is often confused with 'know.' 'Know' is about facts; 'understand' is about "
        "comprehension and empathy. Forrest knows facts — dates, names, places. But when he says "
        "'I know what love is,' he means he understands it deeply. That's the difference."
    )

    # Activity 8-10: reading/speak/listen — keep text, update titles
    s1["activities"][8]["title"] = "Read: Forrest Gump Excerpt (Part 2)"
    s1["activities"][8]["description"] = "Read the dialogue about Forrest's childhood and Mama's wisdom"

    s1["activities"][9]["title"] = "Speak: Practice the Dialogue (Part 2)"
    s1["activities"][9]["description"] = "Practice speaking the childhood memories dialogue aloud"

    s1["activities"][10]["title"] = "Listen: Forrest Gump Excerpt (Part 2)"
    s1["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s1["activities"][11]["title"] = "Write: Memory and Wisdom"
    s1["activities"][11]["description"] = "Write sentences using Session 2 vocabulary"
    ws_items_1 = s1["activities"][11]["data"]["items"]
    ws_items_1[0]["prompt"] = (
        "Use the word 'awful' to describe something very bad, or use 'an awful lot of' "
        "to express a large quantity — like Forrest saying 'That's an awful lot of running.' "
        "Example: Moving to a new country involved an awful lot of paperwork and patience."
    )
    ws_items_1[1]["prompt"] = (
        "Use the word 'worn' to describe something that shows signs of heavy use — "
        "like Forrest's childhood shoes that carried him through leg braces and beyond. "
        "Example: The worn pages of the cookbook told the story of a thousand family dinners."
    )
    ws_items_1[2]["prompt"] = (
        "Use the word 'remember' to recall a meaningful moment from your past — "
        "the way Forrest remembers every detail of his childhood with vivid clarity. "
        "Example: I remember the exact moment I realized I wanted to become a teacher."
    )
    ws_items_1[3]["prompt"] = (
        "Use the word 'smart' to talk about intelligence or a clever decision — "
        "keeping in mind Forrest's line: 'I'm not a smart man, but I know what love is.' "
        "Example: The smartest thing I ever did was listen to advice I didn't want to hear."
    )
    ws_items_1[4]["prompt"] = (
        "Use the word 'explain' to describe making something clear to someone — "
        "like Mama explaining the world to Forrest through simple, powerful metaphors. "
        "Example: She explained the math problem using a story about sharing pizza slices."
    )
    ws_items_1[5]["prompt"] = (
        "Use the word 'understand' to talk about deep comprehension or empathy — "
        "the way Forrest understands love even when the world says he shouldn't. "
        "Example: It takes real effort to understand someone whose life experience is completely different from yours."
    )

    # ── Session 2: Group 3 — vacation, dying, meals, combs, strangers, love ──
    s2 = content["learningSessions"][2]
    s2["title"] = "Session 3: Life, Death, and Love"

    # Activity 0: introAudio — session intro
    s2["activities"][0]["title"] = "Introduction to Session 3"
    s2["activities"][0]["description"] = "Recap Sessions 1-2 and introduce the themes of family and love"
    s2["activities"][0]["data"]["text"] = (
        "Welcome to Session 3 — the final learning session before your review! "
        "So far you've learned 12 words from Forrest Gump's world. In Session 1, you met "
        "chocolate, comfortable, million, bet, wish, and shoes — the words of the bus-stop bench, "
        "where Forrest offers kindness to strangers and quotes his mama's chocolate-box philosophy. "
        "In Session 2, you learned awful, worn, remember, smart, explain, and understand — "
        "the words of childhood, memory, and Mama's gift for making the complicated feel simple.\n\n"
        "Now we reach the emotional heart of the film. Forrest talks about the people he loved "
        "and lost — about vacations he never took, about watching someone die, about the small "
        "rituals that hold a life together. This is where the film stops being funny and starts "
        "being devastating. And the words Forrest uses are, as always, heartbreakingly simple.\n\n"
        "Your final 6 words: vacation, dying, meals, combs, strangers, and love. "
        "By the end of this session, you'll have all 18 vocabulary words — and you'll hear "
        "Forrest's story the way it was meant to be heard."
    )

    # Activity 1: introAudio — vocabulary teaching (500-800 words)
    s2["activities"][1]["title"] = "Vocabulary Introduction: Session 3"
    s2["activities"][1]["description"] = "Learn 6 words: vacation, dying, meals, combs, strangers, love"
    s2["activities"][1]["data"]["text"] = (
        "Here are your final 6 vocabulary words, drawn from the most emotional scenes "
        "in Forrest Gump.\n\n"

        "The first word is 'vacation.' It's a noun meaning 'a period of time spent away from "
        "work or school, usually for rest or travel.' In the film, Forrest talks about taking "
        "a vacation — but for him, a vacation isn't a luxury resort or a beach holiday. "
        "It's simply time away from the routine of life, time to breathe and reflect. "
        "American English uses 'vacation' where British English uses 'holiday.' "
        "'On vacation' means currently away: 'She's on vacation this week.' "
        "'Take a vacation' means to go on one: 'You need to take a vacation.' "
        "Example: They saved for two years to take a family vacation to the Grand Canyon.\n\n"

        "The second word is 'dying.' It's the present participle of 'die,' used as an adjective "
        "or part of a continuous tense. In the film, Forrest faces the death of people he loves — "
        "and the word 'dying' carries an unbearable weight in his simple narration. "
        "'Dying' can be literal: 'The flowers are dying.' Or figurative: 'I'm dying to know what happened' "
        "(extremely eager), 'I'm dying of thirst' (very thirsty). The figurative uses are very common "
        "in casual English. 'A dying art' means something that's disappearing. "
        "Example: She sat by the window of the hospital room, watching the dying light of the afternoon.\n\n"

        "The third word is 'meals.' It's the plural of 'meal' — an occasion when food is eaten, "
        "or the food itself. Forrest mentions meals in the context of daily life — the simple act "
        "of sitting down to eat with someone you love. Meals are rituals. They mark the rhythm "
        "of a day. 'Three meals a day,' 'a home-cooked meal,' 'skip a meal.' "
        "In English, the main meals are breakfast, lunch, and dinner (or supper). "
        "Example: Some of my happiest memories are of family meals around a crowded kitchen table.\n\n"

        "The fourth word is 'combs.' It can be a noun (plural of 'comb' — a tool for arranging hair) "
        "or a verb (third person singular of 'to comb' — to arrange hair with a comb). "
        "In the film, this small domestic detail — combing hair — represents care, tenderness, "
        "and the quiet intimacy of everyday love. 'She combs her daughter's hair every morning.' "
        "'A fine-toothed comb' is also used figuratively: 'go through something with a fine-toothed comb' "
        "means to examine very carefully. "
        "Example: Every evening, she combs her hair slowly while listening to the radio.\n\n"

        "The fifth word is 'strangers.' It's the plural of 'stranger' — a person you don't know. "
        "The entire bus-stop scene is built on Forrest talking to strangers. He doesn't see them "
        "as strangers — he sees them as people worth talking to. That's his superpower. "
        "'Stranger' can also mean 'someone unfamiliar with something': 'He's no stranger to hard work.' "
        "'Don't talk to strangers' is the classic parental warning. "
        "Example: The kindness of strangers restored her faith in humanity after a terrible week.\n\n"

        "The sixth and final word — the word the entire film builds toward — is 'love.' "
        "It's both a noun and a verb, and it might be the most powerful word in the English language. "
        "Forrest says: 'I'm not a smart man, but I know what love is.' That single line contains "
        "the entire thesis of the film — that love doesn't require intelligence, wealth, or status. "
        "It just requires showing up. 'Love' as a noun: 'a mother's love,' 'love at first sight.' "
        "As a verb: 'I love you,' 'She loves reading.' 'Fall in love,' 'make love,' 'love letter' — "
        "the collocations are endless because love touches everything. "
        "Example: He didn't have the words to explain it, but he knew what love felt like.\n\n"

        "And there you have it — all 18 words: chocolate, comfortable, million, bet, wish, shoes, "
        "awful, worn, remember, smart, explain, understand, vacation, dying, meals, combs, strangers, "
        "and love. You now have the complete vocabulary of Forrest Gump's bus-stop story. "
        "Let's practice these final 6!"
    )

    # Activities 2-6: flashcards/vocab
    s2["activities"][2]["title"] = "Flashcards: Life, Death, and Love"
    s2["activities"][2]["description"] = "Learn 6 words: vacation, dying, meals, combs, strangers, love"

    s2["activities"][3]["title"] = "Flashcards: Speak Session 3 Vocabulary"
    s2["activities"][3]["description"] = "Practice saying 6 words: vacation, dying, meals, combs, strangers, love"

    s2["activities"][4]["title"] = "Flashcards: Recognize Session 3 Vocabulary"
    s2["activities"][4]["description"] = "Recognize 6 words: vacation, dying, meals, combs, strangers, love"

    s2["activities"][5]["title"] = "Flashcards: Recall Session 3 Vocabulary"
    s2["activities"][5]["description"] = "Recall 6 words: vacation, dying, meals, combs, strangers, love"

    s2["activities"][6]["title"] = "Flashcards: Deep Knowledge Session 3"
    s2["activities"][6]["description"] = "Master 6 words: vacation, dying, meals, combs, strangers, love"

    # Activity 7: introAudio — grammar/usage
    s2["activities"][7]["title"] = "Grammar and Usage: Session 3"
    s2["activities"][7]["description"] = "How to use Session 3 vocabulary naturally in sentences"
    s2["activities"][7]["data"]["text"] = (
        "Let's look at how these final 6 words work in English grammar.\n\n"
        "'Vacation' in American English is equivalent to 'holiday' in British English. "
        "'Go on vacation,' 'take a vacation,' 'vacation days,' 'summer vacation.' "
        "As a verb (informal American): 'We vacationed in Maine last summer.' "
        "The adjective form is 'vacationing': 'vacationing tourists.'\n\n"
        "'Dying' as a present participle: 'He is dying' (continuous tense). "
        "As an adjective: 'a dying wish,' 'a dying breed,' 'the dying embers.' "
        "Figurative uses are extremely common: 'I'm dying to see that movie,' "
        "'I'm dying of boredom.' These are informal and should be used in casual contexts.\n\n"
        "'Meals' — the three standard meals are breakfast, lunch, and dinner. "
        "'Meal prep' is preparing food in advance. 'A square meal' means a substantial, "
        "satisfying meal. 'Meal' vs. 'dish': a meal is the entire eating occasion; "
        "a dish is one item of food served as part of a meal.\n\n"
        "'Combs' as a verb takes a direct object: 'She combs her hair.' "
        "'Comb through' means to search carefully: 'Police combed through the evidence.' "
        "A 'honeycomb' is the wax structure bees build. The 'b' in 'comb' is silent — "
        "it's pronounced /koʊm/.\n\n"
        "'Strangers' — 'a complete stranger,' 'a total stranger' (emphasis on not knowing them). "
        "'No stranger to' means experienced with: 'She's no stranger to controversy.' "
        "'Strange' (adjective) and 'stranger' (noun) share a root but have different nuances.\n\n"
        "'Love' is one of the most versatile words in English. As a noun: 'first love,' "
        "'love story,' 'love of my life.' As a verb: 'I love cooking,' 'I'd love to come.' "
        "'Lovely' (adjective) means beautiful or delightful. 'Lovable' means easy to love. "
        "In British English, 'love' is also a casual term of address: 'Thanks, love.'"
    )

    # Activity 8-10: reading/speak/listen
    s2["activities"][8]["title"] = "Read: Forrest Gump Excerpt (Part 3)"
    s2["activities"][8]["description"] = "Read the dialogue about life, death, and love"

    s2["activities"][9]["title"] = "Speak: Practice the Dialogue (Part 3)"
    s2["activities"][9]["description"] = "Practice speaking the final dialogue excerpt aloud"

    s2["activities"][10]["title"] = "Listen: Forrest Gump Excerpt (Part 3)"
    s2["activities"][10]["description"] = "Listen to the passage you just read and follow along."

    # Activity 11: writingSentence
    s2["activities"][11]["title"] = "Write: Family and Love"
    s2["activities"][11]["description"] = "Write sentences using Session 3 vocabulary"
    ws_items_2 = s2["activities"][11]["data"]["items"]
    ws_items_2[0]["prompt"] = (
        "Use the word 'vacation' to write about rest, escape, or time away — "
        "the way Forrest talks about stepping away from the routine of life. "
        "Example: The best vacation I ever took was a week in a cabin with no phone signal."
    )
    ws_items_2[1]["prompt"] = (
        "Use the word 'dying' literally or figuratively — "
        "like the film's unflinching look at loss, or the casual 'I'm dying to know.' "
        "Example: The dying sunlight painted the clouds in shades of gold and crimson."
    )
    ws_items_2[2]["prompt"] = (
        "Use the word 'meals' to write about food, routine, or togetherness — "
        "the way shared meals in the film represent the quiet rhythm of love. "
        "Example: The simplest meals — bread, cheese, and conversation — are often the most memorable."
    )
    ws_items_2[3]["prompt"] = (
        "Use the word 'combs' (verb or noun) to describe a small act of care — "
        "the way the film uses everyday gestures to show tenderness. "
        "Example: She combs through old photographs every December, remembering faces she hasn't seen in years."
    )
    ws_items_2[4]["prompt"] = (
        "Use the word 'strangers' to write about connection or distance between people — "
        "like Forrest, who tells his deepest stories to people he's never met. "
        "Example: We started the train ride as strangers and ended it as friends."
    )
    ws_items_2[5]["prompt"] = (
        "Use the word 'love' to express deep affection, passion, or devotion — "
        "remembering Forrest's line: 'I'm not a smart man, but I know what love is.' "
        "Example: Love isn't about grand gestures — it's about showing up, day after day, even when it's hard."
    )

    # ── Session 3: Review (4 activities) ──
    s3 = content["learningSessions"][3]
    s3["title"] = "Review"

    s3["activities"][0]["title"] = "Congratulations and Review"
    s3["activities"][0]["description"] = "Celebrate your progress and prepare for the full review"
    s3["activities"][0]["data"]["text"] = (
        "Congratulations! You've learned all 18 vocabulary words from Forrest Gump's bus-stop "
        "story. Let's take a moment to look back at what you've accomplished.\n\n"
        "In Session 1, you learned chocolate, comfortable, million, bet, wish, and shoes — "
        "the words of Forrest's opening scene, where a box of chocolates becomes a metaphor "
        "for life's unpredictability and a pair of shoes becomes a symbol for life's journey.\n\n"
        "In Session 2, you learned awful, worn, remember, smart, explain, and understand — "
        "the words of childhood and Mama's wisdom, where Forrest discovers that being different "
        "isn't a weakness and that the simplest explanations are often the truest.\n\n"
        "In Session 3, you learned vacation, dying, meals, combs, strangers, and love — "
        "the words of the film's emotional core, where everyday rituals become acts of devotion "
        "and a man who isn't 'smart' turns out to understand the most important thing of all.\n\n"
        "Now it's time to review all 18 words together. This review session will test your "
        "recognition and recall across all three groups. After this, you'll be ready to read "
        "the complete dialogue in the final session. Let's go!"
    )

    s3["activities"][1]["title"] = "Flashcards: Review All 18 Words"
    s3["activities"][1]["description"] = "Review all 18 vocabulary words from Forrest Gump"

    s3["activities"][2]["title"] = "Flashcards: Recognize All Vocabulary"
    s3["activities"][2]["description"] = "Test your recognition of all 18 words"

    s3["activities"][3]["title"] = "Flashcards: Recall All Vocabulary"
    s3["activities"][3]["description"] = "Test your recall of all 18 words"

    # ── Session 4: Full reading + farewell (5 activities) ──
    s4 = content["learningSessions"][4]
    s4["title"] = "Full Dialogue Reading"

    s4["activities"][0]["title"] = "Introduction to the Complete Reading"
    s4["activities"][0]["description"] = "Prepare for reading the full Forrest Gump dialogue"
    s4["activities"][0]["data"]["text"] = (
        "Welcome to the final session! This is the moment everything comes together. "
        "Over the past three sessions, you've built a vocabulary of 18 words drawn directly "
        "from Forrest Gump's dialogue. You've learned their meanings, practiced their pronunciation, "
        "explored their grammar, and used them in your own writing.\n\n"
        "Now you're going to read the complete dialogue — all three excerpts combined into one "
        "continuous passage. As you read, you'll encounter every single one of your 18 words "
        "in context. This time, they won't be new — they'll be familiar friends.\n\n"
        "Here are all 18 words you'll see: chocolate, comfortable, million, bet, wish, shoes, "
        "awful, worn, remember, smart, explain, understand, vacation, dying, meals, combs, "
        "strangers, and love.\n\n"
        "Take your time with the reading. Let Forrest's voice come through. "
        "And remember — life is like a box of chocolates."
    )

    s4["activities"][1]["title"] = "Read: Complete Forrest Gump Dialogue"
    s4["activities"][1]["description"] = "Read the full bus-stop bench dialogue from beginning to end"

    s4["activities"][2]["title"] = "Speak: Practice the Complete Dialogue"
    s4["activities"][2]["description"] = "Practice speaking the entire dialogue aloud"

    s4["activities"][3]["title"] = "Listen: Complete Forrest Gump Dialogue"
    s4["activities"][3]["description"] = "Listen to the complete dialogue and follow along"

    s4["activities"][4]["title"] = "Farewell and Vocabulary Review"
    s4["activities"][4]["description"] = "Final review of all 18 words and farewell"
    s4["activities"][4]["data"]["text"] = (
        "You've done it — you've completed the entire Forrest Gump vocabulary course! "
        "Let's do one final review of all 18 words before we say goodbye.\n\n"

        "'Chocolate' — a sweet food, and in this film, a metaphor for life's surprises. "
        "Example: He always kept a bar of chocolate in his desk drawer for bad days.\n\n"
        "'Comfortable' — providing ease and relaxation. "
        "Example: The old armchair was the most comfortable seat in the house.\n\n"
        "'Million' — the number 1,000,000, often used for exaggeration. "
        "Example: A million thoughts raced through her mind as she opened the letter.\n\n"
        "'Bet' — to wager, or to express confidence. "
        "Example: I bet you can't eat just one of these cookies.\n\n"
        "'Wish' — a desire for something unlikely or impossible. "
        "Example: He made a wish on the first star he saw that evening.\n\n"
        "'Shoes' — footwear, and in this film, a symbol for life's journey. "
        "Example: She packed three pairs of shoes for a trip that was supposed to last two days.\n\n"

        "'Awful' — very bad, or (in 'an awful lot') very much. "
        "Example: There's an awful lot of talent in this room tonight.\n\n"
        "'Worn' — showing damage from use; past participle of 'wear.' "
        "Example: The worn steps of the old library told of generations of readers.\n\n"
        "'Remember' — to recall from memory. "
        "Example: Do you remember the first song you ever learned by heart?\n\n"
        "'Smart' — intelligent, clever. "
        "Example: It was a smart move to start saving money early.\n\n"
        "'Explain' — to make clear or understandable. "
        "Example: Can you explain why the sky turns red at sunset?\n\n"
        "'Understand' — to comprehend deeply. "
        "Example: I finally understand why she made the choice she did.\n\n"

        "'Vacation' — time away from work or routine. "
        "Example: A good vacation doesn't have to be expensive — just different.\n\n"
        "'Dying' — in the process of death; or extremely eager. "
        "Example: I'm dying to hear how the story ends.\n\n"
        "'Meals' — occasions for eating food. "
        "Example: They shared three meals a day and never ran out of things to talk about.\n\n"
        "'Combs' — tools for hair, or the act of arranging hair. "
        "Example: She combs her daughter's hair every morning before school.\n\n"
        "'Strangers' — people you don't know. "
        "Example: Sometimes the best advice comes from complete strangers.\n\n"
        "'Love' — deep affection, the most powerful force in Forrest's world. "
        "Example: 'I'm not a smart man, but I know what love is.'\n\n"

        "Thank you for learning with Forrest Gump. You came for 18 vocabulary words, "
        "but I hope you're leaving with something more — a reminder that the simplest words, "
        "spoken with sincerity, can carry the deepest meaning. "
        "Keep reading, keep speaking, keep writing. And remember — "
        "you never know what you're gonna get. Goodbye, and good luck!"
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
    print(f"Created en-en Forrest Gump curriculum: {cid}")
    return cid


if __name__ == "__main__":
    create()
