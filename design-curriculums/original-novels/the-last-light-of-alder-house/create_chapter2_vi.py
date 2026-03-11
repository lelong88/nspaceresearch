#!/usr/bin/env python3
"""Chapter 2: Alder House — bilingual Vietnamese-English curriculum."""

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
    "Cliff Road was narrow and steep. It climbed away from the town through a tunnel of old trees — alders, Maya guessed, "
    "their bare branches reaching across the road like fingers. The pavement was cracked and covered with wet leaves.\n\n"
    "The road ended at a rusted iron gate. Beyond it, a gravel path led through an overgrown garden to the house.\n\n"
    "Maya stopped the car and stared.\n\n"
    "Alder House was larger than she remembered. Three stories tall, built of dark wood and gray stone. It had a wide front "
    "porch, tall windows, and a roof with several chimneys. The paint was peeling, and some of the windows were dark, but the "
    "house still had a strange beauty. It looked like it belonged there, growing out of the cliff like the trees around it.\n\n"
    "Behind the house, there was nothing but sky and ocean.\n\n"
    "Maya got out of the car. The wind was stronger here, carrying the sound of waves crashing against the rocks far below. "
    "She could taste salt on her lips.\n\n"
    "She tried the gate. It was not locked — it swung open with a long, low creak. She walked up the gravel path, her shoes "
    "crunching with each step. The garden on both sides was wild. Rose bushes had grown into tangled walls. A stone fountain "
    "stood in the center, dry and covered with moss.\n\n"
    "She climbed the porch steps. The wood groaned under her feet but held firm. She found the right key on the third try "
    "and pushed open the front door."
)

SECTION_2 = (
    "The smell hit her first — old wood, dust, and something else. Something sweet, like dried flowers. The entrance hall "
    "was large and dim. A staircase rose up to the second floor, its wooden railing carved with leaves and vines. The walls "
    "were covered with dark wallpaper, and old paintings hung in heavy frames.\n\n"
    "Maya stepped inside and closed the door behind her. The sound of the wind disappeared, replaced by a deep, heavy silence.\n\n"
    '"Hello?" she said, feeling foolish. Her voice echoed off the walls.\n\n'
    "She walked through the ground floor slowly. There was a living room with a stone fireplace, a dining room with a long "
    "table, a kitchen with an old iron stove, and a small library with shelves that reached the ceiling. Every room was full "
    "of furniture, books, and objects — as if Eleanor had simply stepped out and never come back.\n\n"
    "In the kitchen, Maya found a cup and saucer on the counter, washed and placed upside down to dry. A calendar on the "
    "wall showed February. A pair of reading glasses sat on the kitchen table next to a closed book.\n\n"
    "It felt wrong to be here. Like she was trespassing in someone else's life."
)

SECTION_3 = (
    "She remembered the letter in her pocket. She pulled it out and sat down at the kitchen table, in what must have been "
    "Eleanor's chair.\n\n"
    "She opened the envelope carefully. Inside was a single sheet of paper, covered in the same elegant handwriting.\n\n"
    "My dear Maya,\n\n"
    "If you are reading this, then I am gone, and you have come to Alder House. I am glad. I have waited a long time for this.\n\n"
    "I know your mother kept you away from me. She had her reasons, and I do not blame her. She wanted to protect you. But "
    "some things cannot be avoided, only delayed.\n\n"
    "You are the last of our family, Maya. And Alder House needs someone from our family. It has always needed one of us.\n\n"
    "I cannot explain everything in a letter. The house will show you, in time. But I must warn you: do not trust everything "
    "you see. Do not trust everyone in this town. And whatever you do, do not go into the basement until you understand what "
    "is down there.\n\n"
    "There is a room on the third floor — the last door on the left. It was mine. Inside, you will find my journal. Read it. "
    "It will answer some of your questions, though I fear it will also give you new ones.\n\n"
    "I am sorry I could not tell you this in person. I am sorry for many things. But I believe you are strong enough for "
    "what comes next.\n\n"
    "With all my love,\nEleanor\n\n"
    "Maya read the letter three times. Her heart was beating fast. She looked around the kitchen as if seeing it for the "
    "first time.\n\nDo not go into the basement."
)

SECTION_4 = (
    "She stood up and walked back to the entrance hall. There, under the staircase, she saw a door she had not noticed "
    "before. It was smaller than the others, made of heavy dark wood, with an iron lock.\n\n"
    "The basement door.\n\n"
    "Maya stared at it for a long moment. Then she turned away and looked up the staircase.\n\n"
    "The third floor. The last door on the left. Eleanor's room.\n\n"
    "She put her hand on the railing and began to climb.\n\n"
    "The second floor had four bedrooms and a bathroom. The rooms were neat and quiet, with beds made and curtains drawn. "
    "Maya did not stop to look. She kept climbing.\n\n"
    "The staircase to the third floor was narrower and steeper. The wallpaper here was older, faded to a pale yellow. The "
    "floorboards creaked with every step.\n\n"
    "There were three doors on the third floor. Two on the right, one on the left. Maya walked to the last door on the left "
    "and tried the handle.\n\nIt was locked.\n\n"
    "She tried the second key on the ring. It fit. The lock turned with a solid click, and the door swung open."
)

SECTION_5 = (
    "Eleanor's room was different from the rest of the house. It was smaller, simpler. A single bed with a white quilt. "
    "A wooden desk by the window. A bookshelf filled with old books. And on the desk, exactly where Eleanor said it would "
    "be, was a leather journal.\n\n"
    "Maya picked it up. It was thick and heavy, its brown leather cover worn smooth by years of handling. She opened it to "
    "the first page.\n\n"
    "The handwriting was Eleanor's, but younger somehow — the letters sharper, more hurried.\n\n"
    "September 3, 1971\n\n"
    "I have decided to write everything down. If something happens to me, someone must know the truth about this house. "
    "About what lives beneath it. About the light.\n\n"
    "It started three nights ago. I was reading in the library when I heard it — a sound from below the floor. Not a knock. "
    "Not a voice. Something else. Something like breathing.\n\n"
    "I went to the basement door. And I saw it — light, coming through the cracks around the door frame. A pale, blue-white "
    "light, pulsing slowly, like a heartbeat.\n\n"
    "I should have walked away. But I didn't.\n\nI opened the door.\n\n"
    "Maya turned the page, but the next entry was dated two weeks later. Whatever had happened when Eleanor opened that door, "
    "she had not written about it right away.\n\n"
    "Maya closed the journal and held it against her chest. Through the window, she could see the ocean stretching to the "
    "horizon, dark and endless under the gray sky.\n\n"
    "She had so many questions. About Eleanor. About the house. About the light in the basement.\n\n"
    "And somewhere below her feet, behind that heavy wooden door, she thought she heard something.\n\n"
    "A sound like breathing."
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["rusted", "overgrown", "creak", "gravel"]
S2_VOCAB = ["dim", "trespassing", "fireplace", "saucer"]
S3_VOCAB = ["delayed", "warn", "elegant", "avoided"]
S4_VOCAB = ["railing", "staircase", "faded", "creaked"]
S5_VOCAB = ["leather", "pulsing", "beneath", "horizon"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB

def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 2: Ngôi Nhà Alder (Alder House)",
        "preview": {
            "text": (
                "Maya đến Alder House lần đầu tiên — ngôi nhà ba tầng cũ kỹ trên vách đá "
                "nhìn ra biển. Bên trong, cô tìm thấy bức thư bí ẩn của bà Eleanor và cuốn "
                "nhật ký tiết lộ về một thứ ánh sáng kỳ lạ trong tầng hầm. Học 20 từ vựng "
                "tiếng Anh trung cấp qua hành trình khám phá ngôi nhà đầy bí ẩn."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 2. Maya khám phá Alder House, "
            "đọc bức thư cảnh báo của Eleanor, và phát hiện cuốn nhật ký kể về ánh sáng "
            "bí ẩn dưới tầng hầm."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Đến Alder House",
                "activities": [
                    {"title": "Flashcards: Đến Alder House",
                     "description": "Học 4 từ: rusted, overgrown, creak, gravel",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Đến Alder House",
                     "description": "Maya lái xe lên vách đá — cổng sắt rỉ sét, khu vườn hoang dại, và cái nhìn đầu tiên về ngôi nhà ba tầng.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Đến Alder House",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Bên trong ngôi nhà",
                "activities": [
                    {"title": "Flashcards: Bên trong ngôi nhà",
                     "description": "Học 4 từ: dim, trespassing, fireplace, saucer",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Bên trong ngôi nhà",
                     "description": "Maya bước vào — phòng khách, thư viện, nhà bếp với đồ vật Eleanor để lại như thể bà vừa bước ra ngoài.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Bên trong ngôi nhà",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Bức thư của Eleanor",
                "activities": [
                    {"title": "Flashcards: Bức thư của Eleanor",
                     "description": "Học 4 từ: delayed, warn, elegant, avoided",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Bức thư của Eleanor",
                     "description": "Maya đọc bức thư bà để lại — lời cảnh báo về tầng hầm và lời nhắn tìm cuốn nhật ký trên tầng ba.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Bức thư của Eleanor",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Leo lên tầng ba",
                "activities": [
                    {"title": "Flashcards: Leo lên tầng ba",
                     "description": "Học 4 từ: railing, staircase, faded, creaked",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Leo lên tầng ba",
                     "description": "Maya leo cầu thang, qua cánh cửa tầng hầm, lên tầng ba tìm căn phòng cuối cùng bên trái.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Leo lên tầng ba",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Cuốn nhật ký",
                "activities": [
                    {"title": "Flashcards: Cuốn nhật ký",
                     "description": "Học 4 từ: leather, pulsing, beneath, horizon",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Cuốn nhật ký",
                     "description": "Maya tìm thấy cuốn nhật ký da và đọc trang đầu — Eleanor viết về ánh sáng xanh trắng phát ra từ tầng hầm.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Cuốn nhật ký",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 2",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 2 từ lúc Maya đến ngôi nhà đến khi tìm thấy cuốn nhật ký.",
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
    print(f"Chapter 2 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
