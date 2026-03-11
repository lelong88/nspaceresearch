#!/usr/bin/env python3
"""Chapter 5: The Journals — bilingual Vietnamese-English curriculum."""

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
    "Maya woke up on the couch with Eleanor's journal on her chest and pale morning light coming through the curtains. "
    "She had not meant to fall asleep downstairs, but exhaustion had won.\n\n"
    "She sat up and listened. The house was quiet. No strange sounds. No mysterious lights. Just the distant crash of waves "
    "and the cry of seagulls.\n\n"
    "She made coffee in Eleanor's old kitchen and sat down with the journals. She had decided to read them in order. If she "
    "was going to understand this house — and the light beneath it — she needed to start at the beginning.\n\n"
    "Over the next three days, Maya read. She read in the kitchen, in the library, on the porch when the weather allowed it. "
    "She read by lamplight at night and by gray daylight during the day. She barely left the house."
)

SECTION_2 = (
    "The journals told the story of Eleanor's life at Alder House, and slowly, the story of the light.\n\n"
    "Eleanor had come to Alder House in 1968, when she was twenty-five years old. Her mother, Margaret, had lived there "
    "before her, and Margaret's mother, Catherine, before that. Catherine was the one who had built the house in 1892 — or "
    "rather, she had hired men to build it over the place where the light already existed.\n\n"
    "The light had been there long before the house. Long before the town. According to Eleanor's research, the native "
    "people who had lived on this coast for thousands of years knew about it. They called it \"the heart of the earth\" and "
    "considered it sacred. They never built anything over it. They visited it with respect and left offerings.\n\n"
    "Catherine Voss was different. She was a scientist — unusual for a woman in the 1890s — and she believed the light could "
    "be studied and understood. She built Alder House directly over the opening in the cliff, with the basement surrounding "
    "the hole. She spent the rest of her life trying to understand what the light was.\n\n"
    "She never succeeded. But she learned some things.\n\n"
    "The light was not fire. It was not electricity. It was not any kind of energy that science could explain. It seemed to "
    "be alive — or at least aware. It responded to the presence of people, especially people from the Voss family. It showed "
    "them visions. It gave them knowledge. And sometimes, it gave them power.\n\n"
    "Catherine discovered that when she spent time near the light, she could sense things — the weather before it changed, "
    "illness in other people, danger before it arrived. The longer she stayed near the light, the stronger these abilities "
    "became."
)

SECTION_3 = (
    "But there was a cost.\n\n"
    "The light wanted something in return. It wanted to grow. It wanted to spread beyond the basement, beyond the house, "
    "beyond the cliff. And if it was allowed to do that — if the door was left open too long, or if someone invited the "
    "light out — the consequences could be terrible.\n\n"
    "Catherine's journal, which Eleanor had copied into her own, described an incident in 1905. Catherine had fallen asleep "
    "in the basement, near the light. When she woke up, the light had spread. It had moved up the stairs, through the "
    "basement door, and into the house. The walls were glowing. The furniture was floating. And outside, the ocean had "
    "pulled back from the shore, as if the water itself was afraid.\n\n"
    "Catherine managed to push the light back. She stood at the top of the basement stairs and — Maya could not understand "
    "exactly how — she used her own will to force the light back down into the hole. It took her three hours. When it was "
    "over, she collapsed and did not wake up for two days.\n\n"
    "After that, Catherine made the rules. The basement door stays locked. No one sleeps near the light. And someone from "
    "the family must always live in the house, because the light responds to the Voss bloodline. Without a Voss present, "
    "the light becomes restless. It pushes against its boundaries. It tries to escape."
)

SECTION_4 = (
    "Maya put down the journal and rubbed her eyes. She had been reading for hours, and her head was full of impossible "
    "things.\n\n"
    "A light that was alive. A family duty that stretched back over a hundred years. And she — Maya Chen, graphic designer "
    "from Portland — was apparently the last person in the world who could keep this light contained.\n\n"
    "She laughed. It sounded strange in the empty house.\n\n"
    '"This is crazy," she said out loud.\n\n'
    "But even as she said it, she knew it wasn't. She had seen the light in the garden. She had felt the warmth through the "
    "floor. And she had read Eleanor's words — careful, precise, written by a woman who was clearly intelligent and not "
    "prone to fantasy.\n\n"
    "Something was real about all of this. Something was true.\n\n"
    "Maya stood up and walked to the entrance hall. She stood in front of the basement door and put her hand flat against "
    "the wood.\n\n"
    "It was warm. Not hot — just warm, like skin. Like something alive was pressing against the other side.\n\n"
    "She pulled her hand away.\n\n"
    '"Not yet," she whispered. "I\'m not ready yet."\n\n'
    "She went back to the library and picked up the next journal."
)

SECTION_5 = (
    "By the end of the third day, Maya had read through 1985. Eleanor's story was becoming more complex. The light was not "
    "the only secret in Alder Bay.\n\n"
    "In 1979, Eleanor had discovered that she was not the only one who knew about the light. A group of people in town — "
    "five or six families who had lived in Alder Bay for generations — knew about it too. They called themselves the Keepers, "
    "and they believed it was their duty to make sure the light never escaped.\n\n"
    "But they disagreed with Eleanor about how to do that.\n\n"
    "Eleanor believed the light should be left alone — contained but respected. She thought it was something natural, "
    "something ancient, something that had a right to exist.\n\n"
    "The Keepers believed the light was dangerous and should be destroyed. They had been trying to find a way to seal the "
    "hole permanently for decades. And they did not trust the Voss family to keep the light contained forever.\n\n"
    "The leader of the Keepers, in Eleanor's time, was a man named Harold Burke.\n\n"
    "Maya stopped reading.\n\nBurke. Frank Burke — the man in the café who had told her to sell the house and leave.\n\n"
    "She turned the page quickly.\n\n"
    "November 3, 1979\n\n"
    "Harold came to the house today. He stood at the gate and shouted at me. He said I was putting the whole town in danger. "
    "He said the light was getting stronger and that I was too weak to control it.\n\n"
    "I told him to leave. He said he would be back.\n\n"
    "I am worried. Not about Harold — he is angry, but he is not violent. I am worried because he might be right. The light "
    "IS getting stronger. I can feel it every night, pushing against the floor, pressing against the door.\n\n"
    "And I am tired. So tired.\n\nSometimes I wonder what would happen if I just let it out.\n\n"
    "Maya closed the journal. Outside, the sun was setting. The sky over the ocean was orange and red, and the first stars "
    "were appearing.\n\n"
    "She thought about Frank Burke in the café. His cold eyes. His warning.\n\n"
    "Stay out of the basement. If you know what's good for you.\n\n"
    "Was he trying to protect her? Or was he trying to protect the town from her?\n\n"
    "Maya didn't know. But she was starting to understand that in Alder Bay, nothing was simple, and no one was telling her "
    "the whole truth.\n\n"
    "She needed to find out more about the Keepers. And she needed to find out what had happened between Eleanor and Harold "
    "Burke.\n\n"
    "But first, she needed to eat. And maybe sleep. She had barely done either in three days.\n\n"
    "She went to the kitchen and opened the refrigerator. As she reached for the eggs, she heard something.\n\n"
    "A knock. Three slow knocks, coming from below.\n\nFrom the basement.\n\n"
    "Maya froze. She stood perfectly still, holding her breath, listening.\n\n"
    "Three more knocks. Slow. Deliberate. Patient.\n\n"
    "Something was down there. And it knew she was here.\n\n"
    "And for the first time, Maya had the strange, impossible feeling that it was not trying to scare her.\n\n"
    "It was trying to say hello."
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["exhaustion", "mysterious", "lamplight", "porch"]
S2_VOCAB = ["sacred", "offerings", "presence", "abilities"]
S3_VOCAB = ["consequences", "collapsed", "boundaries", "restless"]
S4_VOCAB = ["precise", "prone", "fantasy", "contained"]
S5_VOCAB = ["permanently", "disagreed", "deliberate", "patient"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB

def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 5: Những Cuốn Nhật Ký (The Journals)",
        "preview": {
            "text": (
                "Maya dành ba ngày đọc nhật ký của Eleanor và khám phá lịch sử Alder House. "
                "Ánh sáng đã tồn tại từ hàng ngàn năm trước, gia đình Voss xây nhà để canh "
                "giữ nó. Maya biết về nhóm Keepers muốn phá hủy ánh sáng, và nghe tiếng gõ "
                "cửa bí ẩn từ tầng hầm. Học 20 từ vựng qua bí mật ngày càng sâu của ngôi nhà."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 5. Maya đọc nhật ký và khám phá "
            "lịch sử gia đình Voss, nhóm Keepers, và mối liên hệ giữa ánh sáng với dòng máu "
            "của cô."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Ba ngày đọc sách",
                "activities": [
                    {"title": "Flashcards: Ba ngày đọc sách",
                     "description": "Học 4 từ: exhaustion, mysterious, lamplight, porch",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Ba ngày đọc sách",
                     "description": "Maya quyết định đọc hết nhật ký theo thứ tự — ba ngày liền không rời nhà.",
                     "activityType": "reading", "practiceMinutes": 3,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Ba ngày đọc sách",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Lịch sử gia đình Voss",
                "activities": [
                    {"title": "Flashcards: Gia đình Voss",
                     "description": "Học 4 từ: sacred, offerings, presence, abilities",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Gia đình Voss",
                     "description": "Catherine Voss xây nhà năm 1892 trên nơi ánh sáng tồn tại — người bản địa gọi nó là trái tim của trái đất.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Gia đình Voss",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Cái giá phải trả",
                "activities": [
                    {"title": "Flashcards: Cái giá phải trả",
                     "description": "Học 4 từ: consequences, collapsed, boundaries, restless",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Cái giá phải trả",
                     "description": "Năm 1905 Catherine ngủ quên trong tầng hầm — ánh sáng tràn ra, đồ đạc bay lơ lửng, biển rút xa bờ.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Cái giá phải trả",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Maya đứng trước cánh cửa",
                "activities": [
                    {"title": "Flashcards: Trước cánh cửa",
                     "description": "Học 4 từ: precise, prone, fantasy, contained",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Trước cánh cửa",
                     "description": "Maya chạm tay vào cửa tầng hầm — gỗ ấm như da người. Cô chưa sẵn sàng nhưng biết mọi thứ là thật.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Trước cánh cửa",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Nhóm Keepers và tiếng gõ cửa",
                "activities": [
                    {"title": "Flashcards: Keepers và tiếng gõ cửa",
                     "description": "Học 4 từ: permanently, disagreed, deliberate, patient",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Keepers và tiếng gõ cửa",
                     "description": "Maya biết về nhóm Keepers do Harold Burke dẫn đầu — rồi nghe ba tiếng gõ chậm rãi từ tầng hầm.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Keepers và tiếng gõ cửa",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 5",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 5 từ lúc Maya đọc nhật ký đến tiếng gõ cửa từ tầng hầm.",
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
    print(f"Chapter 5 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
