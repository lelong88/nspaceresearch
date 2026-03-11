#!/usr/bin/env python3
"""Chapter 13: The Standoff — bilingual Vietnamese-English curriculum."""

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
    "The trucks stopped at the gate. Frank got out first, followed by six men Maya didn't recognize. They were big, "
    "serious-looking men in work clothes, carrying tools. The concrete truck idled behind them, its engine rumbling.\n\n"
    "Frank walked to the gate and looked at Maya. His face was set, determined.\n\n"
    '"Step aside," he said. "We\'re coming in."\n\n"No," Maya said. "You\'re not."\n\n'
    '"This isn\'t your decision. A man disappeared because of that light. The town has a right to protect itself."\n\n'
    '"Ben is back," Maya said. "He\'s safe. He\'s at home with his sister right now."\n\n'
    'Frank blinked. For a moment, surprise broke through his hard expression. "Back? How?"\n\n'
    '"I found him. At Cape Sorrow, sixty miles south. The light moved him there — it didn\'t hurt him. He\'s fine."\n\n'
    '"Moved him?" Frank shook his head. "You\'re talking nonsense. The light is dangerous. It took a man from his boat in '
    "the middle of the night. I don't care if he's back — it shouldn't have happened.\"\n\n"
    '"I agree. And I\'m working on making sure it doesn\'t happen again. But sealing the hole is not the answer."\n\n'
    '"It\'s the only answer."'
)

SECTION_2 = (
    '"No, it isn\'t." Maya stepped forward. "Frank, listen to me. The light under this house is connected to six other '
    "lights along the coast. They form a network — a system that keeps the earth stable. If you destroy one, the others "
    'will react. The consequences could be catastrophic."\n\n'
    '"Says who? Your dead grandmother?"\n\n'
    '"Says Catherine Voss, who built this house. Says the research she did for thirty years. Says the light itself."\n\n'
    "Frank laughed. \"The light told you. Right. And I suppose it also told you that you're the only one who can save us "
    'all."\n\n'
    "Maya didn't answer. Because that was, in fact, exactly what the light had told her.\n\n"
    'Frank turned to his men. "Let\'s go. Open the gate."\n\n'
    "One of the men stepped forward and reached for the gate latch. Sam moved to block him.\n\n"
    '"Don\'t," Sam said quietly.\n\n'
    "The man looked at Sam, then at Frank. Frank nodded. The man pushed Sam aside — not roughly, but firmly — and opened "
    "the gate.\n\n"
    '"Frank, stop," Maya said. "Please. Give me one month. Twenty-six days. If I can\'t fix this by then, I\'ll let you '
    "seal it. I'll help you seal it. But give me a chance.\"\n\n"
    "Frank paused. His men waited behind him, uncertain.\n\n"
    '"Twenty-six days," he repeated.\n\n"That\'s all I\'m asking."'
)

SECTION_3 = (
    '"And what happens in twenty-six days if you fail?"\n\n'
    '"Then you were right, and I was wrong. And we do it your way."\n\n'
    "Frank studied her face. Maya held his gaze, trying to project a confidence she didn't entirely feel.\n\n"
    '"Two weeks," Frank said. "Not twenty-six days. Fourteen. If things aren\'t better in two weeks — if the dreams don\'t '
    "stop, if the tides don't go back to normal, if anyone else disappears — we seal it. No more discussion.\"\n\n"
    "Maya's heart sank. Two weeks. That was barely enough time to reach the remaining four lights, let alone figure out "
    "how to stabilize the network permanently.\n\n"
    "But it was better than nothing.\n\n"
    '"Deal," she said.\n\n'
    "Frank held out his hand. Maya shook it. His grip was hard and rough.\n\n"
    '"Fourteen days," he said. "Starting now."\n\n'
    "He turned and walked back to his truck. His men followed, looking relieved. The trucks backed down Cliff Road and "
    "disappeared into the trees.\n\n"
    'Sam let out a long breath. "That was intense."\n\n'
    '"That was just the beginning," Maya said. She sat down on the porch steps. Her legs were shaking — from exhaustion, '
    "from adrenaline, from fear. \"Two weeks, Sam. I have two weeks to visit four more lights spread across hundreds of "
    'miles of coastline."'
)

SECTION_4 = (
    '"Then we\'d better start planning." Sam sat down next to her. "Where are the other four?"\n\n'
    "Maya pulled out Catherine's map and spread it between them.\n\n"
    '"Point Silence, Mist Harbor, Shell Beach, and The Deep Place. They\'re all in California, spread along the coast from '
    'the Oregon border to somewhere south of San Francisco."\n\n'
    'Sam studied the map. "That\'s a lot of driving. But it\'s doable. If we plan the route right, we could hit two in a '
    'day."\n\n"We?"\n\n'
    '"I told you — you\'re not doing this alone." He pulled out his phone. "Let me call Ben. And Lily. We need a team."\n\n'
    "Within an hour, they were all sitting around the kitchen table at Alder House — Maya, Sam, Ben, and Lily. Ben looked "
    "tired but determined. Lily looked scared but angry — angry at the light for taking her brother, angry at Frank for "
    "threatening the house, angry at the situation in general.\n\n"
    '"So we\'re going on a road trip," Lily said. "To touch magical lights in caves along the coast. To save the earth."\n\n'
    '"When you say it like that, it sounds crazy," Ben said.\n\n'
    '"It is crazy," Lily said. "But I saw your face when you came home this morning. You saw something real. I believe you."\n\n'
    "Maya spread the map on the table. \"Here's what I'm thinking. We split into two teams. Sam and I will drive south and "
    "hit the four remaining lights. Ben and Lily will stay here and watch the house. Keep Frank away. Keep the town "
    'calm."\n\n'
    '"How do we keep the town calm?" Lily asked.\n\n'
    '"Tell them the truth — or as much of it as they can handle. Tell them Ben is back and safe. Tell them I\'m working on '
    'a solution. Buy us time."\n\n'
    'Ben nodded. "I can do that. People will listen to me — I\'m the guy who got kidnapped by a magic light and lived to '
    'tell about it."\n\n'
    '"That\'s one way to put it," Sam said.'
)

SECTION_5 = (
    "They spent the next hour planning the route. Point Silence was about a hundred and fifty miles south, near the "
    "Oregon-California border. Mist Harbor was another hundred miles beyond that. Shell Beach was further south still. And "
    "The Deep Place — the last point on the map — was somewhere near Big Sur, almost five hundred miles from Alder Bay.\n\n"
    '"We can do it in three days if we push it," Sam said. "Leave tomorrow morning, drive south, hit the lights, drive '
    'back."\n\n'
    '"Three days out of fourteen," Maya said. "That leaves eleven days to figure out the rest."\n\n'
    '"The rest being...?"\n\n'
    '"How to stabilize the network permanently. How to make sure the light stays contained without a Voss sitting on top '
    "of it twenty-four hours a day. How to find the nexus.\"\n\n"
    '"The nexus?" Lily asked.\n\n'
    "Maya pointed to the center of Catherine's map, where the lines connecting the seven points converged. \"The central "
    "point of the network. Catherine believed that if she could reach the nexus, she could understand the whole system. "
    'Maybe even control it."\n\n'
    '"Where is it?" Sam asked.\n\n'
    "Maya looked at the map. The lines converged at a point in the ocean, about fifty miles off the coast of northern "
    "California.\n\n"
    '"It\'s underwater," she said. "In the middle of the Pacific."\n\n'
    "The table went quiet.\n\n"
    '"Well," Ben said finally. "That\'s a problem."\n\n'
    '"One thing at a time," Maya said. "First, we strengthen the connections. Then we figure out the nexus."\n\n'
    "They agreed on the plan. Sam would close the café for a few days — his mother could handle it. Ben and Lily would "
    "take shifts at Alder House, making sure no one came up the road. Maya and Sam would leave at dawn.\n\n"
    "As the others left, Sam lingered at the door.\n\n"
    '"Maya," he said. "What if it\'s not enough? What if we touch all seven lights and the network still isn\'t stable?"\n\n'
    "Maya thought about the vision she'd had in the basement — herself, older, standing with light pouring from her hands. "
    "Smiling.\n\n"
    '"Then we\'ll figure something else out," she said. "We have to."\n\n'
    "Sam nodded and left. Maya locked the door and went to the library. She had one more night with Eleanor's journals, "
    "and she intended to use it.\n\n"
    "She picked up the journal covering 1995 to 2000 and opened it. A photograph fell out — old, faded, showing two women "
    "standing in front of Alder House. One was Eleanor, gray-haired and stern. The other was younger, with dark hair and a "
    "familiar face.\n\n"
    "Maya's mother.\n\n"
    "On the back of the photograph, in Eleanor's handwriting:\n\n"
    '"Margaret and me. The last time she visited. She said she would never come back. She said she would never let Maya '
    "near this place. I pray she is wrong. The light needs Maya. I have seen it.\"\n\n"
    "Maya held the photograph for a long time, looking at her mother's face. Young, beautiful, angry.\n\n"
    "What had her mother known? What had she been running from?\n\n"
    "And what had Eleanor seen in the light that made her so certain Maya would come?\n\n"
    "The answers were in the journals. Maya turned the page and kept reading, racing against the dawn."
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["rumbling", "determined", "nonsense", "idled"]
S2_VOCAB = ["catastrophic", "uncertain", "latch", "roughly"]
S3_VOCAB = ["adrenaline", "stabilize", "permanently", "intense"]
S4_VOCAB = ["threatening", "remaining", "doable", "converged"]
S5_VOCAB = ["lingered", "intended", "stern", "photograph"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB


def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 13: Đối Đầu (The Standoff)",
        "preview": {
            "text": (
                "Frank đến với xe tải bê tông và sáu người. Maya đàm phán được 14 ngày — nếu "
                "không giải quyết được thì Frank sẽ bịt lỗ. Cả nhóm lên kế hoạch road trip đến "
                "bốn ánh sáng còn lại. Maya tìm thấy ảnh mẹ mình cùng Eleanor và lời tiên tri "
                "rằng ánh sáng cần cô. Học 20 từ vựng tiếng Anh trung cấp qua chương này."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 13. Maya đối đầu Frank, thương lượng "
            "14 ngày, lập kế hoạch chuyến đi, và phát hiện bí mật về mẹ mình."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Frank đến với đội quân",
                "activities": [
                    {"title": "Flashcards: Frank đến",
                     "description": "Học 4 từ: rumbling, determined, nonsense, idled",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Frank đến",
                     "description": "Xe tải dừng trước cổng. Frank và sáu người đàn ông bước xuống. Maya chặn lại — Ben đã về an toàn, nhưng Frank không quan tâm.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Frank đến",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Đàm phán tại cổng",
                "activities": [
                    {"title": "Flashcards: Đàm phán tại cổng",
                     "description": "Học 4 từ: catastrophic, uncertain, latch, roughly",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Đàm phán tại cổng",
                     "description": "Maya giải thích về mạng lưới bảy ánh sáng. Frank cười nhạo. Người của Frank mở cổng, đẩy Sam sang bên. Maya xin 26 ngày.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Đàm phán tại cổng",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Thỏa thuận 14 ngày",
                "activities": [
                    {"title": "Flashcards: Thỏa thuận 14 ngày",
                     "description": "Học 4 từ: adrenaline, stabilize, permanently, intense",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Thỏa thuận 14 ngày",
                     "description": "Frank chỉ cho 14 ngày thay vì 26. Maya chấp nhận — bắt tay. Xe tải rút đi. Hai tuần để đến bốn ánh sáng còn lại.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Thỏa thuận 14 ngày",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Lập kế hoạch road trip",
                "activities": [
                    {"title": "Flashcards: Lập kế hoạch",
                     "description": "Học 4 từ: threatening, remaining, doable, converged",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Lập kế hoạch",
                     "description": "Bốn người ngồi quanh bàn bếp. Maya và Sam sẽ lái xe về nam. Ben và Lily canh nhà. Lily tin — vì cô thấy mặt Ben khi anh về.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Lập kế hoạch",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Nexus và ảnh của mẹ",
                "activities": [
                    {"title": "Flashcards: Nexus và ảnh của mẹ",
                     "description": "Học 4 từ: lingered, intended, stern, photograph",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Nexus và ảnh của mẹ",
                     "description": "Nexus nằm giữa Thái Bình Dương. Sam hỏi — nếu không đủ thì sao? Maya tìm thấy ảnh mẹ cùng Eleanor và lời tiên tri về mình.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Nexus và ảnh của mẹ",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 13",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 13 từ cuộc đối đầu với Frank đến khi Maya tìm thấy ảnh mẹ.",
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
    print(f"Chapter 13 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
