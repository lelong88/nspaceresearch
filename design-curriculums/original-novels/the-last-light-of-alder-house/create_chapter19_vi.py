#!/usr/bin/env python3
"""Chapter 19: After the Light — bilingual Vietnamese-English curriculum."""

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
    'Maya slept for two days.\n\n'
    'Sam carried her from the boat to his truck, and Lily drove them up to Alder House. They put her in Eleanor\'s bed '
    'on the third floor — the room with the desk and the bookshelf and the window overlooking the ocean. Maya was '
    'unconscious before her head touched the pillow.\n\n'
    'She slept through the rest of that day, through the night, through the next day, and into the following morning. '
    'Sam, Ben, and Lily took turns sitting with her, checking her breathing, making sure she was okay.\n\n'
    'When she finally woke up, the first thing she noticed was the silence.\n\n'
    'Not the heavy, listening silence of before. A different kind — light, clean, peaceful. The silence of a house that '
    'was just a house. Old wood, old stone, old memories. But nothing more.\n\n'
    'The light was gone.\n\n'
    'Not gone from the earth — Maya could still feel it, faintly, like a distant heartbeat. The network was there, deep '
    'underground, pulsing steadily. But it was no longer pressing against the basement door. It was no longer trying to '
    'escape. It was balanced, stable, content.\n\n'
    'And Maya was no longer glowing. She checked her hands — normal. No blue-white shimmer beneath the skin. She took a '
    'deep breath — normal. Air, not water. She was herself again. Just Maya.'
)

SECTION_2 = (
    'She got out of bed slowly. Her body ached everywhere, and she was incredibly hungry. She found clean clothes in her '
    'suitcase and made her way downstairs.\n\n'
    'Sam was in the kitchen, making breakfast. The smell of eggs and toast filled the house.\n\n'
    '"Morning," he said, smiling. "Or afternoon, technically. It\'s one o\'clock."\n\n'
    '"I slept for two days?"\n\n'
    '"You earned it." He set a plate in front of her. "Eat. You need it."\n\n'
    'Maya ate three eggs, four pieces of toast, and drank two cups of coffee. It was the best meal of her life.\n\n'
    '"What happened while I was asleep?" she asked.\n\n'
    '"A lot, actually." Sam sat across from her. "The morning after your dive, something happened in town. People woke '
    'up feeling... different. Better. Lighter. Mrs. Patterson said it was like a weight had been lifted off the whole '
    'town. The fishermen said the bay was full of fish — more than they\'d seen in years. And the weather cleared up. '
    'First sunny day in weeks."\n\n'
    '"And Frank?"\n\n'
    '"Frank came up here yesterday. He stood at the gate for about ten minutes, just looking at the house. Then he left. '
    'He didn\'t try to come in. He didn\'t bring concrete." Sam paused. "I think he felt it too. Whatever you did down '
    'there — the whole town felt it."\n\n'
    'Maya looked out the kitchen window. The sky was blue — actually blue, not the usual gray. Sunlight streamed through '
    'the glass, making patterns on the old wooden floor.\n\n'
    '"The light doesn\'t need a guardian anymore," she said. "The network is self-sustaining now. It\'ll maintain itself."\n\n'
    '"So you\'re free?"\n\n'
    '"I\'m free." The word felt strange in her mouth. Free. After everything she\'d learned about her family, about the '
    'duty that had consumed four generations of Voss women — she was free.\n\n'
    'But freedom, she was discovering, came with its own questions.'
)

SECTION_3 = (
    'Over the next few days, Maya settled into a new routine. She cleaned the rest of the house — the bedrooms, the '
    'bathrooms, the attic. She fixed a broken window on the second floor and repaired a section of the porch railing. '
    'She planted flowers in the garden, pulling out the worst of the weeds and giving the old rose bushes room to '
    'breathe.\n\n'
    'She went into town every day. She had coffee at The Wheelhouse, bought groceries from Lily at the store, walked '
    'along the harbor. People smiled at her now. They said hello. They asked how she was doing.\n\n'
    'They didn\'t know exactly what had happened — Maya hadn\'t told anyone the full story, and she didn\'t plan to. But '
    'they knew something had changed. The town felt different. Healthier. Happier.\n\n'
    'Even Frank Burke was different. Maya saw him at the café one morning, sitting at the counter, drinking coffee. He '
    'nodded at her when she came in. Not friendly, exactly, but not hostile either. An acknowledgment. A truce.\n\n'
    '"Ms. Chen," he said.\n\n'
    '"Mr. Burke."\n\n'
    '"The house looks good. You\'ve been working on it."\n\n'
    '"It needed some attention."\n\n'
    'Frank was quiet for a moment. Then he said, "My father spent his whole life afraid of that house. Afraid of what '
    'was underneath it. He passed that fear on to me." He looked down at his coffee. "I\'m tired of being afraid."\n\n'
    '"Me too," Maya said.\n\n'
    'They didn\'t say anything else. But something had shifted between them — a wall coming down, slowly, brick by brick.'
)

SECTION_4 = (
    'A week after the dive, Maya went down to the basement for the last time.\n\n'
    'She unlocked the door and walked down the stone steps. The basement was dark — no glow, no pulse, no warmth. Just '
    'a stone room with a hole in the floor.\n\n'
    'She knelt beside the hole and looked down. It was dark. Empty. The light had retreated deep into the earth, back '
    'to the network, back to the nexus. It was still there — she could feel it if she concentrated — but it was far '
    'away. Sleeping, maybe. Or just resting, after millions of years of effort.\n\n'
    '"Thank you," Maya said into the darkness. "For choosing my family. For trusting us. For trusting me."\n\n'
    'She thought she felt something — the faintest pulse of warmth, like a hand squeezing hers. But it might have been '
    'her imagination.\n\n'
    'She stood up, climbed the stairs, and closed the basement door. She didn\'t lock it. There was nothing to lock away '
    'anymore.\n\n'
    'She went to the library and sat in Eleanor\'s chair. The journals were still on the shelf — twelve volumes, '
    'fifty-six years of one woman\'s life. Maya would keep them. They were part of her family\'s history, and she wanted '
    'to remember.\n\n'
    'She picked up the last journal — the one that ended in 2024, the year before Eleanor died. She turned to the final '
    'entry.'
)

SECTION_5 = (
    'December 31, 2024\n\n'
    'Another year ends. I am eighty-one, and I am tired.\n\n'
    'The light is restless tonight. It knows I am fading. It is worried — I can feel its worry like a cold wind through '
    'the house.\n\n'
    'But I am not worried. I have done my part. I have kept the balance for fifty-six years. And I know — I have always '
    'known — that Maya will come.\n\n'
    'She is strong. Stronger than me, stronger than Margaret, stronger than Catherine. She will not just maintain the '
    'balance. She will transform it. She will do what none of us could do.\n\n'
    'She will set the light free.\n\n'
    'And in doing so, she will set us all free.\n\n'
    'I am ready to go now. The house will wait for her. The light will wait for her.\n\n'
    'Goodbye, old friend. Take care of my granddaughter.\n\n'
    'With love,\nEleanor\n\n'
    'Maya closed the journal. Tears were falling on the pages, but she didn\'t wipe them away.\n\n'
    '"I did it, Eleanor," she whispered. "I set it free. Just like you said."\n\n'
    'The house was quiet around her. Peaceful. Just an old house on a cliff, full of books and memories and the faint '
    'smell of the sea.\n\n'
    'Maya sat in the chair for a long time, holding the journal, looking out the window at the ocean. The sun was '
    'setting, painting the sky in shades of gold and rose. The water sparkled. The cliffs glowed.\n\n'
    'It was beautiful. It had always been beautiful. She just hadn\'t been able to see it before.\n\n'
    'She put the journal back on the shelf, stood up, and went to the kitchen to make dinner. Sam was coming over later, '
    'and Ben and Lily too. They were going to eat together, like friends do. Like family.\n\n'
    'Maya smiled as she opened the refrigerator. For the first time in a very long time, she knew exactly where she '
    'belonged.'
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["unconscious", "shimmer", "beneath", "content"]
S2_VOCAB = ["guardian", "consumed", "streamed", "routine"]
S3_VOCAB = ["hostile", "acknowledgment", "truce", "settled"]
S4_VOCAB = ["retreated", "concentrated", "volumes", "imagination"]
S5_VOCAB = ["transform", "restless", "belonged", "whispered"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB


def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 19: Sau Ánh Sáng (After the Light)",
        "preview": {
            "text": (
                "Maya ngủ hai ngày liền sau cú lặn. Khi tỉnh dậy, ngôi nhà im lặng — nhưng là "
                "sự im lặng nhẹ nhàng, thanh bình, không còn nặng nề như trước. Ánh sáng đã rút "
                "sâu vào lòng đất, mạng lưới tự vận hành. Maya dọn dẹp nhà, sửa cửa sổ, trồng "
                "hoa, và bắt đầu hòa nhập với thị trấn. Frank Burke gặp cô ở quán cà phê và nói "
                "'I'm tired of being afraid.' Trong tầng hầm lần cuối, Maya cảm ơn ánh sáng. Và "
                "trong nhật ký cuối cùng của Eleanor, bà đã biết trước tất cả. Học 20 từ vựng "
                "tiếng Anh qua chương đầy cảm xúc này."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 19. Maya tỉnh dậy trong một thế giới "
            "đã thay đổi — ngôi nhà chỉ là ngôi nhà, thị trấn hồi sinh, và nhật ký Eleanor tiết "
            "lộ bà luôn biết Maya sẽ đến."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Tỉnh dậy",
                "activities": [
                    {"title": "Flashcards: Tỉnh dậy",
                     "description": "Học 4 từ: unconscious, shimmer, beneath, content",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Tỉnh dậy",
                     "description": "Maya ngủ hai ngày. Khi tỉnh, ngôi nhà im lặng thanh bình — ánh sáng đã rút đi, không còn phát sáng dưới da. Cô lại là chính mình.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Tỉnh dậy",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Thị trấn thay đổi",
                "activities": [
                    {"title": "Flashcards: Thị trấn thay đổi",
                     "description": "Học 4 từ: guardian, consumed, streamed, routine",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Thị trấn thay đổi",
                     "description": "Sam kể mọi thứ đã khác — cá đầy vịnh, trời nắng lần đầu sau nhiều tuần, Frank đứng nhìn ngôi nhà rồi bỏ đi. Maya tự do rồi, nhưng tự do đi kèm câu hỏi mới.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Thị trấn thay đổi",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Hòa giải với Frank",
                "activities": [
                    {"title": "Flashcards: Hòa giải với Frank",
                     "description": "Học 4 từ: hostile, acknowledgment, truce, settled",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Hòa giải với Frank",
                     "description": "Maya dọn nhà, trồng hoa, đi phố mỗi ngày. Frank gặp cô ở quán cà phê — không thù địch, chỉ gật đầu. 'I'm tired of being afraid,' ông nói. Bức tường giữa họ đang sụp dần.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Hòa giải với Frank",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Lần cuối xuống tầng hầm",
                "activities": [
                    {"title": "Flashcards: Lần cuối xuống tầng hầm",
                     "description": "Học 4 từ: retreated, concentrated, volumes, imagination",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Lần cuối xuống tầng hầm",
                     "description": "Maya xuống tầng hầm lần cuối — tối, trống, không còn ánh sáng. Cô cảm ơn ánh sáng đã chọn gia đình mình. Rồi đóng cửa, không khóa — không còn gì cần giấu.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Lần cuối xuống tầng hầm",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Nhật ký cuối cùng của Eleanor",
                "activities": [
                    {"title": "Flashcards: Nhật ký cuối cùng",
                     "description": "Học 4 từ: transform, restless, belonged, whispered",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Nhật ký cuối cùng",
                     "description": "Eleanor viết: 'Maya will come. She will set the light free.' Maya khóc, thì thầm 'I did it, Eleanor.' Rồi đứng dậy nấu cơm — Sam, Ben, Lily sẽ đến. Lần đầu tiên, cô biết mình thuộc về đâu.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Nhật ký cuối cùng",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 19",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 19 từ lúc Maya tỉnh dậy đến nhật ký cuối cùng của Eleanor.",
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
    print(f"Chapter 19 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
