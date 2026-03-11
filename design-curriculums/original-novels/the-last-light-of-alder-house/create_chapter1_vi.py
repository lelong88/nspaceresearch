#!/usr/bin/env python3
"""
Create a bilingual Vietnamese-English curriculum for Chapter 1 of
"The Last Light of Alder House" and upload via curriculum/create API.

Follows the exact structure of curriculum_966407991a60:
  - viewFlashcards + reading + readAlong per session
  - Final session: full vocab flashcards + full chapter readAlong
"""

import json
import sys
import requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

API_URL = "https://helloapi.step.is/curriculum/create"
UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
LANGUAGE = "en"
USER_LANGUAGE = "vi"

KEYS_TO_STRIP = {
    "mp3Url", "illustrationSet", "chapterBookmarks", "segments",
    "whiteboardItems", "userReadingId", "lessonUniqueId",
    "curriculumTags", "taskId", "imageId",
}


def strip_keys(obj, keys_to_remove):
    if isinstance(obj, dict):
        return {k: strip_keys(v, keys_to_remove)
                for k, v in obj.items() if k not in keys_to_remove}
    if isinstance(obj, list):
        return [strip_keys(i, keys_to_remove) for i in obj]
    return obj


# --- Reading texts (English story, unchanged) ---

SECTION_1 = (
    'Maya Chen had not thought about Alder Bay in years. The small town on the Oregon coast was just a faded memory — the smell of salt air, the sound of waves, and the face of a grandmother she barely knew.\n\n'
    'So when the letter arrived on a Tuesday morning in March, Maya almost threw it away. It looked official, with a law firm\'s name printed in dark blue across the envelope: Whitfield & Associates, Alder Bay, Oregon.\n\n'
    'She opened it standing at her kitchen counter in Portland, still holding her coffee.\n\n'
    'Dear Ms. Chen,\n\n'
    'We regret to inform you of the passing of your grandmother, Eleanor Voss, on February 28th. As her sole living heir, you have inherited her property at 14 Cliff Road, Alder Bay, known locally as "Alder House."\n\n'
    'We kindly request your presence in Alder Bay at your earliest convenience to discuss the terms of the estate and sign the necessary documents.\n\n'
    'Sincerely,\nThomas Whitfield, Attorney at Law'
)

SECTION_2 = (
    'Maya read the letter twice. She put down her coffee. Her hands were shaking, but she was not sure why.\n\n'
    'She had met Eleanor Voss only once, when she was seven years old. Her mother had driven them to Alder Bay for a weekend visit. Maya remembered a tall woman with silver hair and sharp blue eyes. She remembered a large, dark house on a cliff above the ocean. She remembered her mother arguing with Eleanor in the kitchen, their voices low and angry.\n\n'
    'They had left the next morning, and her mother never spoke of Eleanor again.\n\n'
    'Now her mother was gone too — cancer, three years ago — and Maya was alone. She was twenty-eight, working as a graphic designer for a small company in Portland. She had a cat named Oliver, a one-bedroom apartment, and not much else.\n\n'
    'She looked at the letter again. Sole living heir.\n\n'
    'A house. On the coast. It was probably falling apart. It was probably worth nothing. But something pulled at her — a feeling she could not name. Curiosity, maybe. Or something deeper.\n\n'
    'She called the law firm that afternoon.\n\n'
    '"Ms. Chen. Thank you for calling. I\'m sorry for your loss."\n\n'
    '"Thank you," Maya said. "I didn\'t really know her, to be honest."\n\n'
    'There was a pause. "I see. Well, Eleanor was... a remarkable woman. She lived in Alder House for over fifty years. She was very specific in her will. Everything goes to you — the house, the land, and the contents inside."\n\n'
    '"I can come Friday," she said.\n\n'
    'After she hung up, Maya sat on her couch and stared at the wall. Oliver jumped into her lap and purred.\n\n'
    '"What do you think, Oliver?" she said. "Should we go see what Grandma left us?"\n\n'
    'Oliver blinked slowly, which Maya took as a yes.'
)

SECTION_3 = (
    'The drive from Portland to Alder Bay took about three hours. Maya left early Friday morning, before the sun was fully up. The highway followed the Columbia River west, then turned south along the coast. The ocean appeared and disappeared between the trees, gray and restless under a cloudy sky.\n\n'
    'Alder Bay was not on most maps. It was too small — just a few hundred people living in a town that time seemed to have forgotten. Maya almost missed the turn. A small wooden sign, half-hidden by bushes, read: ALDER BAY — POP. 342.\n\n'
    'The road wound down through thick forest and then opened up to reveal the town. It sat in a natural bay, protected from the worst of the ocean storms by two rocky headlands. There was a main street with a grocery store, a post office, a café, and a few other shops. Fishing boats rocked gently in a small harbor. Everything looked old but clean, like a photograph from another time.'
)

SECTION_4 = (
    'Maya parked in front of the law office, a small white building with a wooden sign. She checked her reflection in the rearview mirror, took a breath, and went inside.\n\n'
    'Thomas Whitfield was a man in his sixties with kind eyes and a gray beard. His office smelled like old books and coffee. He shook Maya\'s hand and offered her a seat.\n\n'
    '"Thank you for coming," he said. "I know it\'s a long drive."\n\n'
    '"It\'s fine. I wanted to see the place."\n\n'
    'He nodded and opened a folder on his desk. "The paperwork is straightforward. Eleanor owned the house and two acres of land outright. No debts, no liens. It\'s all yours, free and clear."\n\n'
    '"What\'s the house like?" Maya asked.\n\n'
    'Whitfield leaned back in his chair. "It\'s old. Built in 1892. Eleanor maintained it well, but it needs work. It\'s a beautiful property, though. Right on the cliff, overlooking the ocean. There\'s nothing else like it in town."\n\n'
    'He paused, then reached into his desk drawer and pulled out a sealed envelope. It was cream-colored, with Maya\'s name written on the front in elegant handwriting.\n\n'
    '"This is the letter she left for you," he said. "She gave it to me two years ago, with very specific instructions. I was to give it to you only in person, only after her death."\n\n'
    'Maya took the envelope. It felt heavy in her hands.\n\n'
    'He gave her a set of keys — three old brass keys on a simple ring — and directions to Cliff Road.'
)

SECTION_5 = (
    '"One more thing," Whitfield said as Maya stood to leave. "Eleanor was a private person. She didn\'t have many friends in town. But the people here respected her. Some of them were... afraid of her, I think."\n\n'
    '"Afraid? Why?"\n\n'
    'Whitfield smiled, but it didn\'t quite reach his eyes. "Alder House has a reputation. Old houses always do, especially in small towns. Don\'t let the stories bother you."\n\n'
    '"What stories?"\n\n'
    'But Whitfield just shook her hand and opened the door for her. "Welcome to Alder Bay, Ms. Chen. If you need anything, don\'t hesitate to call."\n\n'
    'Maya walked back to her car with the keys in one hand and the envelope in the other. The sky had grown darker, and a cold wind was blowing in from the sea.\n\n'
    'She looked up at the cliff north of town. She could see it there — a large, dark shape against the gray sky. Alder House.\n\n'
    'It was waiting for her.\n\n'
    'And somewhere deep inside, in a place she didn\'t fully understand, Maya felt that she had been waiting for it too.'
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

# --- Vocabulary ---
S1_VOCAB = ["faded", "heir", "estate", "envelope"]
S2_VOCAB = ["curiosity", "remarkable", "specific", "hesitate"]
S3_VOCAB = ["restless", "harbor", "headland", "reveal"]
S4_VOCAB = ["straightforward", "property", "maintain", "elegant"]
S5_VOCAB = ["reputation", "cliff", "brass", "private"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB


# --- Build curriculum (mirrors curriculum_966407991a60 structure exactly) ---

def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 1: Bức Thư (The Letter)",
        "preview": {
            "text": (
                "Maya Chen nhận được một bức thư thông báo bà ngoại đã qua đời và để lại "
                "cho cô một ngôi nhà bí ẩn trên bờ biển Oregon. Cô lái xe đến thị trấn nhỏ "
                "Alder Bay để ký giấy tờ — và phát hiện ngôi nhà có một danh tiếng đáng sợ. "
                "Chương trình này dạy 20 từ vựng tiếng Anh trung cấp thông qua câu chuyện "
                "bí ẩn hấp dẫn, giúp bạn vừa đọc truyện vừa mở rộng vốn từ tự nhiên."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 1 của tiểu thuyết bí ẩn. "
            "Qua 6 buổi học, bạn sẽ học flashcards và đọc từng phần câu chuyện, thẩm thấu "
            "từ vựng mới trong ngữ cảnh khi Maya thừa kế Alder House và đến thị trấn ven biển Alder Bay."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Bức thư đến",
                "activities": [
                    {
                        "title": "Flashcards: Bức thư đến",
                        "description": "Học 4 từ: faded, heir, estate, envelope",
                        "activityType": "viewFlashcards",
                        "practiceMinutes": 2,
                        "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2},
                    },
                    {
                        "title": "Đọc: Bức thư đến",
                        "description": "Đọc phần mở đầu — Maya nhận được bức thư bất ngờ từ công ty luật ở thị trấn cô hầu như không nhớ.",
                        "activityType": "reading",
                        "practiceMinutes": 5,
                        "data": {"text": SECTION_1, "audioSpeed": -0.2},
                    },
                    {
                        "title": "Nghe: Bức thư đến",
                        "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                        "activityType": "readAlong",
                        "practiceMinutes": 2,
                        "data": {"text": SECTION_1, "audioSpeed": -0.2},
                    },
                ],
            },
            {
                "title": "Buổi 2: Quyết định của Maya",
                "activities": [
                    {
                        "title": "Flashcards: Quyết định của Maya",
                        "description": "Học 4 từ: curiosity, remarkable, specific, hesitate",
                        "activityType": "viewFlashcards",
                        "practiceMinutes": 2,
                        "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2},
                    },
                    {
                        "title": "Đọc: Quyết định của Maya",
                        "description": "Đọc về ký ức của Maya, cuộc gọi với luật sư, và quyết định đến Alder Bay.",
                        "activityType": "reading",
                        "practiceMinutes": 5,
                        "data": {"text": SECTION_2, "audioSpeed": -0.2},
                    },
                    {
                        "title": "Nghe: Quyết định của Maya",
                        "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                        "activityType": "readAlong",
                        "practiceMinutes": 3,
                        "data": {"text": SECTION_2, "audioSpeed": -0.2},
                    },
                ],
            },
            {
                "title": "Buổi 3: Hành trình đến Alder Bay",
                "activities": [
                    {
                        "title": "Flashcards: Hành trình đến Alder Bay",
                        "description": "Học 4 từ: restless, harbor, headland, reveal",
                        "activityType": "viewFlashcards",
                        "practiceMinutes": 2,
                        "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2},
                    },
                    {
                        "title": "Đọc: Hành trình đến Alder Bay",
                        "description": "Đọc về chuyến lái xe của Maya dọc bờ biển và cái nhìn đầu tiên về thị trấn nhỏ bị lãng quên.",
                        "activityType": "reading",
                        "practiceMinutes": 2,
                        "data": {"text": SECTION_3, "audioSpeed": -0.2},
                    },
                    {
                        "title": "Nghe: Hành trình đến Alder Bay",
                        "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                        "activityType": "readAlong",
                        "practiceMinutes": 2,
                        "data": {"text": SECTION_3, "audioSpeed": -0.2},
                    },
                ],
            },
            {
                "title": "Buổi 4: Gặp luật sư",
                "activities": [
                    {
                        "title": "Flashcards: Gặp luật sư",
                        "description": "Học 4 từ: straightforward, property, maintain, elegant",
                        "activityType": "viewFlashcards",
                        "practiceMinutes": 2,
                        "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2},
                    },
                    {
                        "title": "Đọc: Gặp luật sư",
                        "description": "Đọc về cuộc gặp của Maya với Thomas Whitfield — giấy tờ, chìa khóa, và bức thư cá nhân từ Eleanor.",
                        "activityType": "reading",
                        "practiceMinutes": 5,
                        "data": {"text": SECTION_4, "audioSpeed": -0.2},
                    },
                    {
                        "title": "Nghe: Gặp luật sư",
                        "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                        "activityType": "readAlong",
                        "practiceMinutes": 3,
                        "data": {"text": SECTION_4, "audioSpeed": -0.2},
                    },
                ],
            },
            {
                "title": "Buổi 5: Ngôi nhà trên vách đá",
                "activities": [
                    {
                        "title": "Flashcards: Ngôi nhà trên vách đá",
                        "description": "Học 4 từ: reputation, cliff, brass, private",
                        "activityType": "viewFlashcards",
                        "practiceMinutes": 2,
                        "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2},
                    },
                    {
                        "title": "Đọc: Ngôi nhà trên vách đá",
                        "description": "Đọc cảnh cuối — lời cảnh báo của luật sư, cái nhìn đầu tiên của Maya về Alder House, và cảm giác ngôi nhà đang chờ đợi cô.",
                        "activityType": "reading",
                        "practiceMinutes": 5,
                        "data": {"text": SECTION_5, "audioSpeed": -0.2},
                    },
                    {
                        "title": "Nghe: Ngôi nhà trên vách đá",
                        "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                        "activityType": "readAlong",
                        "practiceMinutes": 2,
                        "data": {"text": SECTION_5, "audioSpeed": -0.2},
                    },
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {
                        "title": "Flashcards: Ôn tập Chương 1",
                        "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                        "activityType": "viewFlashcards",
                        "practiceMinutes": 5,
                        "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2},
                    },
                    {
                        "title": "Nghe: Toàn bộ câu chuyện",
                        "description": "Nghe toàn bộ Chương 1 từ bức thư đến ngôi nhà trên vách đá.",
                        "activityType": "readAlong",
                        "practiceMinutes": 10,
                        "data": {"text": FULL_CHAPTER, "audioSpeed": -0.2},
                    },
                ],
            },
        ],
    }


# --- Upload ---

def main():
    print("Generating firebase token...")
    token = get_firebase_id_token(UID)

    print("Building curriculum...")
    content = build_curriculum()
    content = strip_keys(content, KEYS_TO_STRIP)

    print("Uploading...")
    payload = {
        "uid": UID,
        "language": LANGUAGE,
        "userLanguage": USER_LANGUAGE,
        "content": json.dumps(content, ensure_ascii=False),
        "firebaseIdToken": token,
    }
    resp = requests.post(API_URL, json=payload)
    resp.raise_for_status()
    result = resp.json()
    cid = result.get("id", "unknown")
    print(f"SUCCESS — curriculum id: {cid}")
    return cid


if __name__ == "__main__":
    main()
