#!/usr/bin/env python3
"""Chapter 9: The Cliff Path — bilingual Vietnamese-English curriculum."""

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
    "Maya spent the next two days deep in Eleanor's journals, searching for answers. She found them — slowly, piece by "
    "piece, like assembling a puzzle in the dark.\n\n"
    "Eleanor had spent decades studying the light. She had tried everything — scientific instruments, meditation, even "
    "prayer. Most of it didn't work. But some things did.\n\n"
    "She discovered that the light responded to emotion. When Eleanor was calm and focused, the light was calm. When she "
    "was afraid or angry, the light became agitated. It mirrored her feelings, amplified them, and sent them back.\n\n"
    "She also discovered that the light had a cycle. It grew stronger and weaker over time, following a pattern that Eleanor "
    "eventually connected to the moon. During the new moon, when the sky was darkest, the light was at its strongest. During "
    "the full moon, it was at its weakest."
)

SECTION_2 = (
    "And she discovered something else — something that changed everything.\n\nThe light was not alone.\n\n"
    "In a journal entry from 1988, Eleanor wrote:\n\nMarch 22, 1988\n\n"
    "I have made a discovery that frightens me more than anything else in fifty years.\n\n"
    "The light in the basement is not the only one. There are others.\n\n"
    "I found the first clue in Catherine's old papers — a map she drew in 1910, showing the coastline from here to "
    "California. She marked seven points along the coast with small circles. Alder Bay was one of them.\n\n"
    "I thought they were just landmarks. But last week, during the new moon, I went down to the basement and asked the "
    "light to show me. I put my hands in the glow and concentrated.\n\n"
    "It showed me. Seven lights, spread along the Pacific coast, each one buried deep in the earth. Each one pulsing with "
    "the same rhythm. Connected, like stars in a constellation. Like organs in a body.\n\n"
    "Alder Bay's light is not unique. It is part of something larger. Something that stretches for hundreds of miles beneath "
    "the ground.\n\n"
    "And if one light is disturbed — if one is sealed or destroyed — the others will react. The balance will break. And I "
    "cannot imagine what would happen then."
)

SECTION_3 = (
    "Maya put down the journal. Seven lights. Connected. Part of a system.\n\n"
    "If Frank sealed the hole in Alder Bay, it wouldn't just affect this town. It could affect the entire coast.\n\n"
    "She needed more information. She needed to find Catherine's map.\n\n"
    "Maya searched the library for hours. She went through every drawer, every shelf, every box of papers. She found old "
    "letters, receipts, photographs, and scientific notes — but no map.\n\n"
    "She was about to give up when she remembered the cliff path she had seen from the lighthouse. The stairs cut into the "
    "face of the cliff below the house. Maybe Catherine had used that path. Maybe there was something down there.\n\n"
    "The next morning, Maya put on her warmest clothes and hiking boots and went outside. She walked around the house to "
    "the back, where the garden ended at a low stone wall. Beyond the wall, the cliff dropped straight down to the ocean, "
    "a hundred feet below.\n\n"
    "She found the path at the north end of the wall. It was narrow — barely two feet wide — cut into the rock face and "
    "descending in a series of steep switchbacks. There was no railing, no rope, nothing to hold onto except the rock itself.\n\n"
    "Maya looked down. The waves crashed against the base of the cliff, sending white spray into the air. One wrong step "
    "and she would fall.\n\nShe took a breath and started down."
)

SECTION_4 = (
    "The path was old but solid. The steps were worn smooth by decades of use. Maya kept one hand on the cliff wall and "
    "moved slowly, testing each step before putting her full weight on it.\n\n"
    "Halfway down, the path turned and widened into a small ledge — a natural platform in the rock, about ten feet across. "
    "Maya stopped here to rest and look around.\n\n"
    "The view was stunning. The ocean stretched to the horizon, gray-green and endless. To the south, she could see the "
    "town and the harbor. To the north, the coastline curved away into mist.\n\n"
    "And on the ledge, she found something unexpected.\n\nA door.\n\n"
    "It was set into the cliff face — a wooden door, old and weathered, with iron hinges and a simple latch. It was almost "
    "invisible against the rock, hidden by shadows and moss.\n\n"
    "Maya tried the latch. It was stiff but not locked. The door swung inward with a groan, revealing a tunnel carved into "
    "the cliff.\n\n"
    "Maya turned on her flashlight and stepped inside.\n\n"
    "The tunnel was narrow and low, with rough stone walls. It went straight into the cliff for about thirty feet, then "
    "opened into a small cave. The cave was dry and surprisingly warm. And it was not empty.\n\n"
    "There was a wooden table against one wall, with a chair and an oil lamp. There were shelves carved into the rock, "
    "holding glass jars, dried plants, and small stone objects. And on the table, held flat by a smooth rock, was a large "
    "piece of paper.\n\nCatherine's map."
)

SECTION_5 = (
    "Maya picked it up carefully. It was hand-drawn on thick paper, yellowed with age but still clear. It showed the "
    "Pacific coastline from southern Oregon to northern California. Seven points were marked with small circles, each one "
    "labeled with a name:\n\n"
    "1. Alder Bay (Oregon)\n2. Cape Sorrow (Oregon)\n3. Redwood Cove (California)\n4. Point Silence (California)\n"
    "5. Mist Harbor (California)\n6. Shell Beach (California)\n7. The Deep Place (California)\n\n"
    "Lines connected the seven points, forming a pattern that looked like a constellation — or a web. And in the center of "
    "the web, Catherine had written a single word:\n\nNEXUS\n\n"
    "Maya stared at the map. Seven lights. Seven places. All connected. And somewhere in the middle of them all, a nexus — "
    "a central point where the connections met.\n\n"
    "She looked at the other objects in the cave. The glass jars contained dried herbs and minerals. The stone objects were "
    "carved with the same symbols she had seen in the basement. And on the shelf, behind the jars, she found a small "
    "leather notebook.\n\n"
    "She opened it. Catherine's handwriting — older, more formal than Eleanor's.\n\n"
    "June 8, 1910\n\n"
    "I have found the cave. It was here all along, hidden in the cliff face. I believe the native people used it as a "
    "place of ceremony, connected to the light above.\n\n"
    "I have begun my research here, away from the house. The light's influence is weaker in the cave — I can think more "
    "clearly. I have mapped the other sites along the coast. I believe there are seven in total, each one a point where "
    "the light breaks through from below.\n\n"
    "The lights are connected. They form a network — a living system beneath the earth. Disturbing one will affect the "
    "others. This is why the balance must be maintained. Not just here, but everywhere.\n\n"
    "I must find the nexus. The central point. If I can understand the nexus, I can understand the whole system. And "
    "perhaps I can find a way to stabilize it permanently.\n\n"
    "But I am running out of time. The light grows stronger every year. And I am growing old.\n\n"
    "Maya put the notebook in her pocket and rolled up the map carefully. She looked around the cave one more time, then "
    "headed back through the tunnel and out onto the ledge.\n\n"
    "The wind hit her face, cold and sharp. The ocean roared below.\n\n"
    "She had found what she was looking for — and more. The light wasn't just a local mystery. It was part of something "
    "enormous, something that stretched along the entire coast.\n\n"
    "And somewhere out there was the nexus. The key to understanding everything.\n\n"
    "Maya climbed back up the cliff path, the map tucked inside her jacket. Her mind was racing with questions and "
    "possibilities.\n\n"
    "She was so focused on her thoughts that she almost didn't notice the figure standing at the top of the path, waiting "
    "for her.\n\n"
    "It was Lily — the woman from the grocery store. And she was crying.\n\n"
    '"Maya," Lily said, her voice breaking. "Something\'s happened. You need to come to town. Now."'
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["assembling", "meditation", "agitated", "amplified"]
S2_VOCAB = ["constellation", "disturbed", "rhythm", "unique"]
S3_VOCAB = ["switchbacks", "receipts", "descending", "spray"]
S4_VOCAB = ["ledge", "stunning", "hinges", "latch"]
S5_VOCAB = ["nexus", "network", "stabilize", "ceremony"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB

def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 9: Con Đường Vách Đá (The Cliff Path)",
        "preview": {
            "text": (
                "Maya phát hiện ánh sáng phản ứng theo cảm xúc và theo chu kỳ trăng. Quan "
                "trọng hơn — có BẢY ánh sáng dọc bờ biển, kết nối thành mạng lưới. Cô leo "
                "xuống vách đá, tìm thấy hang động bí mật của Catherine với tấm bản đồ đánh "
                "dấu bảy điểm và từ NEXUS. Rồi Lily chạy đến khóc — có chuyện xảy ra."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 9. Maya khám phá mạng lưới bảy "
            "ánh sáng, tìm hang động và bản đồ của Catherine, rồi nhận tin khẩn từ Lily."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Ánh sáng phản ứng theo cảm xúc",
                "activities": [
                    {"title": "Flashcards: Ánh sáng và cảm xúc",
                     "description": "Học 4 từ: assembling, meditation, agitated, amplified",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Ánh sáng và cảm xúc",
                     "description": "Eleanor phát hiện ánh sáng phản chiếu cảm xúc và theo chu kỳ trăng — mạnh nhất khi trăng non.",
                     "activityType": "reading", "practiceMinutes": 3,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Ánh sáng và cảm xúc",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Bảy ánh sáng",
                "activities": [
                    {"title": "Flashcards: Bảy ánh sáng",
                     "description": "Học 4 từ: constellation, disturbed, rhythm, unique",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Bảy ánh sáng",
                     "description": "Eleanor phát hiện năm 1988 — có bảy ánh sáng dọc bờ biển, kết nối như chòm sao. Phá một cái sẽ ảnh hưởng tất cả.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Bảy ánh sáng",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Leo xuống vách đá",
                "activities": [
                    {"title": "Flashcards: Leo xuống vách đá",
                     "description": "Học 4 từ: switchbacks, receipts, descending, spray",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Leo xuống vách đá",
                     "description": "Maya tìm bản đồ Catherine — leo xuống con đường hẹp trên vách đá, sóng đập bên dưới, một bước sai là rơi.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Leo xuống vách đá",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Hang động bí mật",
                "activities": [
                    {"title": "Flashcards: Hang động bí mật",
                     "description": "Học 4 từ: ledge, stunning, hinges, latch",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Hang động bí mật",
                     "description": "Giữa vách đá có cánh cửa gỗ ẩn — bên trong là phòng nghiên cứu của Catherine với bàn, đèn dầu, và tấm bản đồ.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Hang động bí mật",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Bản đồ và NEXUS",
                "activities": [
                    {"title": "Flashcards: Bản đồ và NEXUS",
                     "description": "Học 4 từ: nexus, network, stabilize, ceremony",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Bản đồ và NEXUS",
                     "description": "Bản đồ đánh dấu bảy điểm từ Oregon đến California với từ NEXUS ở giữa. Rồi Lily xuất hiện — đang khóc.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Bản đồ và NEXUS",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 9",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 9 từ nhật ký Eleanor đến khi Lily chạy đến khóc.",
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
    print(f"Chapter 9 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
