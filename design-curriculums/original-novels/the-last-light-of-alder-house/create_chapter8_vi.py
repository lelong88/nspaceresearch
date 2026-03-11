#!/usr/bin/env python3
"""Chapter 8: The Warning — bilingual Vietnamese-English curriculum."""

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
    "Three days after her visit to the basement, Maya was in the library reading Eleanor's journals when she heard a car "
    "coming up Cliff Road.\n\n"
    "She went to the window. A black pickup truck was parked outside the gate. Frank Burke was standing beside it, looking "
    "up at the house.\n\n"
    "Maya's heart beat faster, but she kept her face calm. She walked to the front door and opened it.\n\n"
    '"Mr. Burke," she said.\n\n'
    "Frank didn't smile. He stood at the gate with his hands in his coat pockets, his gray eyes fixed on her.\n\n"
    '"I need to talk to you," he said.\n\n'
    '"Then come in."\n\n'
    '"I\'d rather not." He looked at the house as if it might bite him. "I\'ll say what I need to say from here."\n\n'
    "Maya walked down the porch steps and across the garden to the gate. Up close, Frank looked older than she had first "
    "thought. His face was deeply lined, and there were dark circles under his eyes.\n\n"
    '"You went into the basement," he said. It was not a question.\n\n'
    "Maya didn't ask how he knew. In Alder Bay, everyone seemed to know everything.\n\n"
    '"Yes," she said.\n\n'
    "Frank's jaw tightened. \"That was a mistake.\""
)

SECTION_2 = (
    '"Why?"\n\n'
    '"Because every time someone goes down there, the light gets stronger. It feeds on attention. On contact. Your grandmother '
    "understood that. She went down as little as possible — once a month, maybe less. And you've been here a week and you're "
    'already visiting it like it\'s a pet."\n\n'
    '"I went once," Maya said.\n\n'
    '"Once is enough. The light remembers. It\'s already changing — I can feel it. The whole town can feel it." He stepped '
    "closer to the gate. \"The dreams are getting worse. My wife hasn't slept in four nights. The fishermen are saying the "
    "water in the bay is warmer than it should be. And last night, three people saw a glow on the cliff. A blue glow.\"\n\n"
    "Maya said nothing. She remembered the light she had seen in the garden on her first night.\n\n"
    '"Your grandmother spent fifty years keeping that thing quiet," Frank said. "Fifty years of discipline and sacrifice. '
    'And you\'re going to undo all of it because you\'re curious."\n\n'
    '"I\'m not just curious," Maya said. "I\'m trying to understand."\n\n'
    '"Understanding is dangerous. Catherine Voss tried to understand it, and she nearly destroyed the town. Your grandmother '
    'tried to understand it, and it consumed her life. You think you\'re different?"\n\n'
    '"Maybe I am."\n\n'
    "Frank laughed — a short, bitter sound. \"That's what they all said.\" He reached into his coat and pulled out a folded "
    "piece of paper. He held it through the gate. \"Read this.\""
)

SECTION_3 = (
    "Maya took the paper and unfolded it. It was a photocopy of a newspaper article, old and faded. The headline read:\n\n"
    "MYSTERIOUS INCIDENT AT ALDER BAY — THREE FISHERMEN MISSING AFTER STRANGE LIGHTS SEEN ON COAST\n\n"
    "The article was dated October 15, 1952.\n\n"
    "Maya read quickly. Three fishermen had gone out at night and never returned. Their boat was found the next morning, "
    "empty and undamaged, floating in the bay. Several witnesses reported seeing unusual lights on the cliff near Alder "
    "House on the same night. The fishermen were never found.\n\n"
    '"1952," Maya said. "That was before Eleanor\'s time."\n\n'
    '"It was Margaret\'s time. Your great-grandmother. She lost control of the light for one night — just one night — and '
    "three men disappeared.\" Frank's voice was hard. \"Their families never got answers. Their children grew up without "
    'fathers. And Margaret went right back to living in that house, pretending nothing had happened."\n\n'
    "Maya stared at the article. Three men. Gone."
)

SECTION_4 = (
    '"I\'m not telling you this to be cruel," Frank said, and for the first time, his voice softened slightly. "I\'m telling '
    "you because you need to understand what you're dealing with. The light is not your friend. It's not a gift. It's a "
    'force of nature, and it doesn\'t care about you or me or anyone in this town."\n\n'
    '"Then what do you suggest?" Maya asked.\n\n'
    '"Seal it. Let me bring my people up here with concrete and steel. We\'ll fill the hole, close the basement, and end '
    'this. Forever."\n\n'
    '"And what happens to the light?"\n\n'
    '"It dies. Or it goes somewhere else. I don\'t care, as long as it\'s not here."\n\n'
    "Maya thought about Eleanor's journals. About Catherine's warnings. About the carved words on the basement wall: "
    "REMEMBER THE BALANCE.\n\n"
    '"What if sealing it makes things worse?" she said. "What if the light can\'t be destroyed — only moved? What if '
    'blocking it here just pushes it somewhere else, somewhere without anyone to contain it?"\n\n'
    "Frank's eyes narrowed. \"That's what Eleanor always said. And I never believed her.\"\n\n"
    '"Maybe you should have."\n\n'
    "They stared at each other across the gate. The wind blew between them, cold and sharp.\n\n"
    '"I\'m giving you a choice," Frank said. "Let us seal it, or deal with it yourself. But if something goes wrong — if '
    'people get hurt — that\'s on you."\n\n'
    "He turned and walked back to his truck. Maya watched him drive away, the black truck disappearing down the road between "
    "the trees."
)

SECTION_5 = (
    "She looked down at the newspaper article in her hand. Three fishermen. Missing. Never found.\n\n"
    "She folded the article and put it in her pocket. Then she went back inside and straight to the library. She needed to "
    "find Eleanor's journals from the 1950s — the ones that covered Margaret's time.\n\n"
    "She found the right journal and opened it to 1952.\n\n"
    "October 16, 1952 (Margaret's account, copied by Eleanor)\n\n"
    "Something terrible has happened. The light escaped last night. I don't know how — I was asleep, and when I woke, the "
    "whole house was glowing. I ran to the basement, but the door was already open. The light was everywhere — in the walls, "
    "in the air, pouring out of the windows like water.\n\n"
    "I managed to push it back. It took hours. But by then, the damage was done.\n\n"
    "Three men are missing from the bay. I know the light took them. I don't know where. I don't know if they're alive.\n\n"
    "God forgive me. I fell asleep. I fell asleep, and people are gone.\n\n"
    "Maya closed the journal. Her hands were cold.\n\n"
    "She understood Frank's anger now. She understood his fear. The light was beautiful, yes. It was peaceful, yes. But it "
    "was also powerful beyond anything she could imagine. And if she made a mistake — if she lost control, even for a moment "
    "— people could die.\n\n"
    "She sat in the library for a long time, thinking. The house was silent around her. The light in the basement pulsed "
    "steadily, unaware of her doubt.\n\n"
    "Or maybe it was very aware. Maybe it was waiting to see what she would decide.\n\n"
    "Maya picked up the journal again. There had to be more. There had to be something Eleanor had learned — some way to "
    "control the light safely, some way to maintain the balance without risking lives.\n\n"
    "She turned the page and kept reading.\n\n"
    "And deep below the house, the light pulsed a little brighter."
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["pickup", "lined", "tightened", "calm"]
S2_VOCAB = ["discipline", "sacrifice", "consumed", "curious"]
S3_VOCAB = ["photocopy", "headline", "witnesses", "undamaged"]
S4_VOCAB = ["concrete", "narrowed", "contain", "sharp"]
S5_VOCAB = ["escaped", "glowing", "damage", "doubt"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB

def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 8: Lời Cảnh Báo (The Warning)",
        "preview": {
            "text": (
                "Frank Burke đến Alder House với bài báo năm 1952 — ba ngư dân mất tích khi "
                "ánh sáng thoát ra. Ông đòi đổ bê tông lấp tầng hầm. Maya đọc nhật ký của "
                "Margaret và hiểu sức mạnh đáng sợ của ánh sáng. Cô phải tìm cách kiểm soát "
                "nó mà không gây nguy hiểm cho ai."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 8. Frank đối đầu Maya với bằng "
            "chứng về sự nguy hiểm của ánh sáng, và Maya phải đối mặt với trách nhiệm nặng nề."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Frank Burke đến",
                "activities": [
                    {"title": "Flashcards: Frank Burke đến",
                     "description": "Học 4 từ: pickup, lined, tightened, calm",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Frank Burke đến",
                     "description": "Frank đến Alder House nhưng không dám bước vào — ông biết Maya đã xuống tầng hầm.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Frank Burke đến",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Ánh sáng nhớ mọi thứ",
                "activities": [
                    {"title": "Flashcards: Ánh sáng nhớ mọi thứ",
                     "description": "Học 4 từ: discipline, sacrifice, consumed, curious",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Ánh sáng nhớ mọi thứ",
                     "description": "Frank nói ánh sáng mạnh lên mỗi khi có người xuống — Eleanor giữ kỷ luật 50 năm mà Maya phá vỡ trong một tuần.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Ánh sáng nhớ mọi thứ",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Bài báo năm 1952",
                "activities": [
                    {"title": "Flashcards: Bài báo năm 1952",
                     "description": "Học 4 từ: photocopy, headline, witnesses, undamaged",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Bài báo năm 1952",
                     "description": "Frank đưa bài báo cũ — ba ngư dân mất tích, thuyền tìm thấy trống rỗng, ánh sáng lạ trên vách đá.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Bài báo năm 1952",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Đổ bê tông hay tự giải quyết",
                "activities": [
                    {"title": "Flashcards: Đổ bê tông hay tự giải quyết",
                     "description": "Học 4 từ: concrete, narrowed, contain, sharp",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Đổ bê tông hay tự giải quyết",
                     "description": "Frank muốn lấp tầng hầm bằng bê tông. Maya lo nếu phá hủy ánh sáng ở đây, nó sẽ thoát ra nơi khác.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Đổ bê tông hay tự giải quyết",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Nhật ký của Margaret",
                "activities": [
                    {"title": "Flashcards: Nhật ký của Margaret",
                     "description": "Học 4 từ: escaped, glowing, damage, doubt",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Nhật ký của Margaret",
                     "description": "Maya đọc nhật ký Margaret — bà ngủ quên, ánh sáng thoát ra, ba người biến mất. Maya hiểu sức mạnh đáng sợ của nó.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Nhật ký của Margaret",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 8",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 8 từ lúc Frank đến đến khi Maya đọc nhật ký Margaret.",
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
    print(f"Chapter 8 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
