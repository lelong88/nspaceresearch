#!/usr/bin/env python3
"""Chapter 3: The Town — bilingual Vietnamese-English curriculum."""

import json, sys, requests
sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

API_URL = "https://helloapi.step.is/curriculum/create"
UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
KEYS_TO_STRIP = {"mp3Url","illustrationSet","chapterBookmarks","segments",
    "whiteboardItems","userReadingId","lessonUniqueId","curriculumTags","taskId","imageId"}

def strip_keys(obj, keys):
    if isinstance(obj, dict):
        return {k: strip_keys(v, keys) for k, v in obj.items() if k not in keys}
    if isinstance(obj, list):
        return [strip_keys(i, keys) for i in obj]
    return obj

SECTION_1 = (
    "Maya did not sleep at Alder House that night. She drove back to town as the sun was setting and checked into the only "
    "place that rented rooms — a small bed and breakfast called The Harbor Inn, run by a woman named Ruth.\n\n"
    "Ruth was in her fifties, with short gray hair and a face that looked like it smiled often. She gave Maya a room on the "
    "second floor with a view of the harbor.\n\n"
    '"You\'re Eleanor\'s granddaughter," Ruth said. It was not a question.\n\n'
    '"Word travels fast," Maya said.\n\n'
    'Ruth laughed. "Honey, this is Alder Bay. Word doesn\'t travel — it\'s already there before you arrive. Everyone knows '
    'you\'re here."'
)

SECTION_2 = (
    'Maya set her bag down on the bed. "Did you know my grandmother?"\n\n'
    '"Everyone knew Eleanor. Not many people knew her well." Ruth leaned against the doorframe. "She kept to herself mostly. '
    "Came into town for groceries, went to the post office, had coffee at the café sometimes. But she was always... apart. "
    'Like she was carrying something heavy that nobody else could see."\n\n'
    '"What do people say about the house?" Maya asked.\n\n'
    "Ruth's smile faded slightly. \"Oh, you know how small towns are. Old house on a cliff, woman living alone for decades — "
    "people talk. Some say the house is haunted. Some say Eleanor was a witch.\" She laughed, but it sounded forced. "
    '"Nonsense, of course."\n\n'
    '"Of course," Maya said.\n\n'
    "After Ruth left, Maya sat on the bed and opened Eleanor's journal. She had brought it with her — she was not ready to "
    "leave it in the house.\n\n"
    "She turned to the entry after the gap.\n\n"
    "September 17, 1971\n\n"
    "I have not been able to write until now. What I saw in the basement — I am still trying to understand it.\n\n"
    "The stairs go down about twenty feet. The basement is large, carved out of the rock of the cliff itself. It is one big "
    "room with stone walls and a stone floor. In the center of the room, there is a hole.\n\n"
    "Not a well. Not a crack. A perfect circle, about three feet across, cut into the stone floor. And from this hole comes "
    "the light.\n\n"
    "It is the most beautiful thing I have ever seen. Blue-white, like moonlight on water, but alive. It pulses. It moves. "
    "And when I stood near it, I felt something I cannot describe. A warmth. A presence. As if the light knew I was there.\n\n"
    "I reached my hand toward it. And the light reached back."
)

SECTION_3 = (
    "Maya stopped reading. She looked out the window at the dark harbor. The fishing boats were still, their lights reflecting "
    "on the black water.\n\n"
    "She wanted to keep reading, but she was exhausted. She closed the journal, turned off the lamp, and lay in the dark, "
    "listening to the distant sound of the ocean.\n\n"
    "---\n\n"
    "The next morning, Maya walked to the café on Main Street. It was called The Wheelhouse, and it was warm and bright "
    "inside, with wooden tables and the smell of fresh coffee and bacon.\n\n"
    "A young man stood behind the counter. He was tall, with dark curly hair and brown skin. He smiled when Maya walked in.\n\n"
    '"You must be Maya," he said. "I\'m Sam. Welcome to Alder Bay."\n\n'
    '"Thanks," Maya said, sitting at the counter. "How does everyone already know my name?"\n\n'
    '"Ruth told Mrs. Patterson, Mrs. Patterson told my mom, my mom told me. That\'s how it works here." He poured her a '
    'coffee without asking. "What can I get you?"\n\n'
    '"Just coffee is fine. And maybe some answers."'
)

SECTION_4 = (
    'Sam raised an eyebrow. "Answers about what?"\n\n'
    '"About my grandmother. About the house."\n\n'
    "Sam's smile became careful. He glanced around the café. There were only two other customers — an old man reading a "
    "newspaper and a woman with a baby.\n\n"
    '"Eleanor was a good person," Sam said quietly. "She helped people. When my mom was sick a few years ago, Eleanor brought '
    'medicine — some kind of herbal thing she made. It worked better than anything the doctor gave her."\n\n'
    '"But?" Maya said, because she could hear the "but" in his voice.\n\n'
    '"But people were still nervous around her. She knew things she shouldn\'t have known. She\'d tell someone to be careful '
    "on the road, and the next day there'd be an accident in that exact spot. She'd ask about someone's health before they "
    'even knew they were sick."\n\n'
    '"That\'s... unusual," Maya said.\n\n'
    '"That\'s one word for it." Sam wiped the counter. "Look, I liked Eleanor. She was kind to me. But there were things about '
    'her that didn\'t make sense. And that house..." He shook his head. "I went up there once, when I was a kid. On a dare. '
    "I didn't even get to the front door. Something about the place just felt wrong. Like it was watching me.\""
)

SECTION_5 = (
    "The bell above the door rang, and a man walked in. He was about sixty, with a weathered face and cold gray eyes. He "
    "wore a heavy coat and work boots. He looked at Maya, and his expression hardened.\n\n"
    '"Morning, Frank," Sam said, his voice suddenly neutral.\n\n'
    "Frank nodded at Sam but kept his eyes on Maya. \"You're the Voss girl,\" he said.\n\n"
    '"I\'m Maya Chen. Eleanor was my grandmother."\n\n'
    '"I know who you are." Frank sat down two seats away from her. "You planning to stay?"\n\n'
    '"I haven\'t decided yet."\n\n'
    '"You should sell the house and go back to Portland. Nothing good comes from that place."\n\n'
    "The café went quiet. Even the old man with the newspaper looked up.\n\n"
    '"Frank—" Sam started.\n\n'
    '"I\'m just being honest," Frank said. "That house has been trouble for this town for a hundred years. Eleanor knew it. '
    'That\'s why she stayed up there alone. She was keeping something contained."\n\n'
    '"Contained?" Maya said. "What do you mean?"\n\n'
    "Frank looked at her for a long moment. Then he shook his head and turned to Sam. \"Coffee. Black.\"\n\n"
    "Maya waited, but Frank said nothing more. He stared straight ahead, his jaw tight.\n\n"
    "Sam gave Maya an apologetic look and mouthed the word \"sorry.\"\n\n"
    "Maya finished her coffee and left money on the counter. As she walked to the door, she stopped and turned back.\n\n"
    '"Frank," she said. "What\'s in the basement?"\n\n'
    "The old man's hand froze around his coffee cup. For just a second, Maya saw something in his eyes. Not anger.\n\n"
    "Fear.\n\n"
    '"Stay out of the basement," he said. "If you know what\'s good for you."\n\n'
    "Maya pushed open the door and stepped into the cold morning air. The sky was gray again, and the wind carried the smell "
    "of the sea.\n\n"
    "Two people had now told her to stay away from the basement. Her grandmother in a letter. And a stranger in a café.\n\n"
    "Which meant that whatever was down there was real. And it was important enough to frighten people.\n\n"
    "Maya looked up at the cliff. She could see Alder House from here, dark against the sky.\n\n"
    "She was going back. And this time, she was going to stay."
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["harbor", "inn", "granddaughter", "rented"]
S2_VOCAB = ["haunted", "carved", "presence", "pulse"]
S3_VOCAB = ["exhausted", "counter", "curly", "bacon"]
S4_VOCAB = ["nervous", "herbal", "unusual", "dare"]
S5_VOCAB = ["weathered", "contained", "apologetic", "frightened"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB

def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 3: Thị Trấn (The Town)",
        "preview": {
            "text": (
                "Maya ở lại thị trấn qua đêm và bắt đầu tìm hiểu về bà Eleanor qua những "
                "người dân Alder Bay. Cô đọc thêm nhật ký, gặp Sam ở quán cà phê, và đối "
                "mặt với Frank Burke — người đàn ông cảnh báo cô tránh xa tầng hầm. Học 20 "
                "từ vựng tiếng Anh qua những cuộc trò chuyện đầy bí ẩn trong thị trấn nhỏ."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 3. Maya khám phá thị trấn, "
            "gặp Sam và Frank, đọc nhật ký Eleanor về ánh sáng trong tầng hầm, và quyết "
            "định quay lại Alder House."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Nhà trọ Harbor Inn",
                "activities": [
                    {"title": "Flashcards: Nhà trọ Harbor Inn",
                     "description": "Học 4 từ: harbor, inn, granddaughter, rented",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Nhà trọ Harbor Inn",
                     "description": "Maya đến nhà trọ và gặp Ruth — người phụ nữ vui vẻ biết hết mọi chuyện trong thị trấn.",
                     "activityType": "reading", "practiceMinutes": 3,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Nhà trọ Harbor Inn",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Nhật ký — ánh sáng trong tầng hầm",
                "activities": [
                    {"title": "Flashcards: Ánh sáng trong tầng hầm",
                     "description": "Học 4 từ: haunted, carved, presence, pulse",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Ánh sáng trong tầng hầm",
                     "description": "Maya đọc nhật ký Eleanor — mô tả tầng hầm đá, cái lỗ tròn hoàn hảo, và ánh sáng xanh trắng sống động.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Ánh sáng trong tầng hầm",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Gặp Sam ở The Wheelhouse",
                "activities": [
                    {"title": "Flashcards: Gặp Sam",
                     "description": "Học 4 từ: exhausted, counter, curly, bacon",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Gặp Sam",
                     "description": "Sáng hôm sau Maya đến quán cà phê The Wheelhouse và gặp Sam — chàng trai thân thiện đầu tiên trong thị trấn.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Gặp Sam",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Câu chuyện về Eleanor",
                "activities": [
                    {"title": "Flashcards: Câu chuyện về Eleanor",
                     "description": "Học 4 từ: nervous, herbal, unusual, dare",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Câu chuyện về Eleanor",
                     "description": "Sam kể về Eleanor — bà giúp đỡ mọi người nhưng cũng biết những điều không ai giải thích được.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Câu chuyện về Eleanor",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Frank Burke và lời cảnh báo",
                "activities": [
                    {"title": "Flashcards: Frank Burke",
                     "description": "Học 4 từ: weathered, contained, apologetic, frightened",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Frank Burke",
                     "description": "Frank Burke bước vào quán — người đàn ông lạnh lùng nói Maya nên bán nhà và rời đi, rồi cảnh báo cô tránh xa tầng hầm.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Frank Burke",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 3",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 3 từ nhà trọ đến quyết định quay lại Alder House.",
                     "activityType": "readAlong", "practiceMinutes": 10,
                     "data": {"text": FULL_CHAPTER, "audioSpeed": -0.2}},
                ],
            },
        ],
    }

def main():
    token = get_firebase_id_token(UID)
    content = strip_keys(build_curriculum(), KEYS_TO_STRIP)
    payload = {"uid": UID, "language": "en", "userLanguage": "vi",
               "content": json.dumps(content, ensure_ascii=False), "firebaseIdToken": token}
    resp = requests.post(API_URL, json=payload)
    resp.raise_for_status()
    cid = resp.json().get("id", "unknown")
    print(f"Chapter 3 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
