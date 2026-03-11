#!/usr/bin/env python3
"""Chapter 20: Home — bilingual Vietnamese-English curriculum."""

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
    'Three months later, Maya stood on the porch of Alder House and watched the sunset.\n\n'
    'The house looked different now. She had painted the exterior — a warm gray that matched the cliffs — and replaced '
    'the broken shutters. The garden was alive with color: roses, lavender, wildflowers, and herbs that Eleanor had '
    'planted years ago and that were now thriving under Maya\'s care. The iron gate had been oiled and repainted, and a '
    'new mailbox stood at the end of the gravel path, with "CHEN" painted on the side in neat letters.\n\n'
    'It was still Alder House. It would always be Alder House. But it was also Maya\'s house now, and it felt like it.\n\n'
    'She had made her decision a month after the dive. She called her boss in Portland and resigned. She arranged to '
    'have her apartment packed up and her things shipped to Alder Bay. Oliver the cat arrived in a carrier, looking '
    'annoyed, and spent three days hiding under the bed before deciding that the house was acceptable.'
)

SECTION_2 = (
    'Maya had started a small graphic design business, working remotely from the library. She had clients in Portland, '
    'Seattle, and San Francisco. The internet in Alder Bay was surprisingly good — someone had installed fiber optic '
    'cable a few years ago, and it reached all the way up Cliff Road.\n\n'
    'She had also started something else. In Catherine\'s cave on the cliff face, she had set up a small workspace — a '
    'desk, a lamp, a shelf of books. She was writing. Not journals, like Eleanor. A book. The story of Alder House, the '
    'light, and the Voss family. She didn\'t know if anyone would believe it, but she wanted it written down. For the '
    'future. For whoever came after her.\n\n'
    'Because even though the light no longer needed a guardian, Maya had decided to stay. Not out of duty. Not out of '
    'obligation. But because this was her home. This cliff, this house, this town — they were part of her now, as much '
    'as the light had ever been.'
)

SECTION_3 = (
    'Sam closed The Wheelhouse early on Fridays now. He would drive up Cliff Road with takeout containers and a bottle '
    'of wine, and they would eat dinner on the porch, watching the sun go down. Sometimes Ben and Lily came too. '
    'Sometimes it was just the two of them.\n\n'
    'Tonight it was just the two of them.\n\n'
    '"I got a letter today," Maya said, pouring wine into two glasses. "From a woman in California. She lives near '
    'Shell Beach. She said she found a cave on the beach with strange symbols on the walls, and she wanted to know if I '
    'knew anything about it."\n\n'
    'Sam raised an eyebrow. "What did you tell her?"\n\n'
    '"I told her the truth. That the symbols are very old, and that the cave is a special place, and that she should '
    'treat it with respect."\n\n'
    '"Did you tell her about the light?"\n\n'
    '"No. She\'ll figure that out on her own, if she\'s meant to." Maya sipped her wine. "The lights are quiet now. '
    'Stable. But they\'re still there. And I think... I think they\'ll reach out to people, over time. People who can '
    'feel them. People who are ready."\n\n'
    '"Like you were ready?"\n\n'
    '"I wasn\'t ready. I was terrified. But I showed up anyway." She smiled. "That\'s all you can do, really. Show up."'
)

SECTION_4 = (
    'Sam reached across the table and took her hand. It had become a habit — this easy, natural closeness between them. '
    'Not rushed, not dramatic. Just two people who had been through something extraordinary together and had come out '
    'the other side holding on to each other.\n\n'
    '"I\'m glad you showed up," he said.\n\n'
    '"Me too."\n\n'
    'They sat in comfortable silence, watching the last light fade from the sky. The stars appeared one by one, bright '
    'and clear. The ocean murmured below the cliff, steady and eternal.\n\n'
    'Maya thought about Eleanor. About Catherine and Margaret. About all the Voss women who had lived in this house, '
    'carrying the weight of the light on their shoulders. They had given their lives to maintain the balance. They had '
    'sacrificed everything — love, freedom, connection — to keep the world safe.\n\n'
    'Maya had ended that cycle. The light was free, and so was she. But she carried their memory with her, like a candle '
    'in the dark. She would not forget them. She would not let the world forget them.'
)

SECTION_5 = (
    'Later that night, after Sam had gone home, Maya walked through the house one last time before bed. She checked the '
    'locks, turned off the lights, and gave Oliver a scratch behind the ears.\n\n'
    'She paused at the basement door. She hadn\'t opened it in weeks. There was no need. But tonight, she felt a gentle '
    'tug — not the desperate pull of before, but something softer. An invitation.\n\n'
    'She opened the door and walked down the stairs.\n\n'
    'The basement was dark and quiet. The hole in the floor was just a hole — dark stone, cool air rising from below. '
    'No glow. No pulse.\n\n'
    'But as Maya stood there, in the silence and the dark, she felt something. A warmth, rising from deep below. Faint, '
    'gentle, barely there. Like a whisper. Like a memory.\n\n'
    'Like a heartbeat.\n\n'
    'The light was still there. Deep in the earth, far from the surface, doing its ancient work. Keeping the balance. '
    'Keeping the world turning. And it remembered her. It would always remember her.\n\n'
    'Maya placed her hand flat on the stone floor, next to the hole. The stone was warm.\n\n'
    '"Goodnight," she whispered.\n\n'
    'The warmth pulsed once beneath her hand. Soft. Grateful. Loving.\n\n'
    'Maya smiled. She stood up, climbed the stairs, and closed the door gently behind her.\n\n'
    'She went upstairs to her bedroom — Eleanor\'s old room on the third floor, with the desk and the bookshelf and the '
    'window overlooking the ocean. She got into bed and pulled the quilt up to her chin. Oliver jumped up and curled '
    'against her feet, purring.\n\n'
    'Through the window, she could see the stars. Thousands of them, scattered across the dark sky like points of light. '
    'Like a network. Like a constellation of small, bright, connected things.\n\n'
    'Maya closed her eyes.\n\n'
    'She was home.\n\n\n'
    'THE END'
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["exterior", "shutters", "thriving", "resigned"]
S2_VOCAB = ["remotely", "obligation", "guardian", "workspace"]
S3_VOCAB = ["symbols", "terrified", "respect", "stable"]
S4_VOCAB = ["extraordinary", "sacrificed", "murmured", "comfortable"]
S5_VOCAB = ["invitation", "constellation", "ancient", "gentle"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB


def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 20: Nhà (Home)",
        "preview": {
            "text": (
                "Ba tháng sau, Alder House đã thay đổi — sơn mới, vườn đầy hoa, hộp thư ghi "
                "tên 'CHEN.' Maya nghỉ việc ở Portland, mở công ty thiết kế từ xa, và bắt đầu "
                "viết sách về câu chuyện gia đình Voss. Mỗi tối thứ Sáu, Sam mang đồ ăn lên "
                "hiên nhà, họ ngồi ngắm hoàng hôn. Một phụ nữ ở California viết thư hỏi về hang "
                "động có ký hiệu lạ — ánh sáng đang tìm đến người mới. Đêm khuya, Maya xuống "
                "tầng hầm lần cuối, đặt tay lên sàn đá ấm và thì thầm 'Goodnight.' Chương cuối "
                "cùng — học 20 từ vựng tiếng Anh qua kết thúc đẹp của câu chuyện."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 20 — chương cuối. Maya đã tìm thấy "
            "nhà, tình yêu, và mục đích. Ánh sáng vẫn ở đó, sâu trong lòng đất, nhớ cô mãi mãi."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Ngôi nhà mới",
                "activities": [
                    {"title": "Flashcards: Ngôi nhà mới",
                     "description": "Học 4 từ: exterior, shutters, thriving, resigned",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Ngôi nhà mới",
                     "description": "Ba tháng sau, Alder House đã khác — sơn mới, vườn đầy hoa, hộp thư ghi 'CHEN.' Maya nghỉ việc Portland, chuyển hẳn về đây cùng Oliver.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Ngôi nhà mới",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Cuộc sống mới",
                "activities": [
                    {"title": "Flashcards: Cuộc sống mới",
                     "description": "Học 4 từ: remotely, obligation, guardian, workspace",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Cuộc sống mới",
                     "description": "Maya làm thiết kế từ xa, viết sách trong hang động Catherine. Cô ở lại không vì nghĩa vụ — mà vì đây là nhà.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Cuộc sống mới",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Tối thứ Sáu trên hiên nhà",
                "activities": [
                    {"title": "Flashcards: Tối thứ Sáu",
                     "description": "Học 4 từ: symbols, terrified, respect, stable",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Tối thứ Sáu",
                     "description": "Sam mang đồ ăn lên, họ uống rượu trên hiên. Maya kể về bức thư từ California — một phụ nữ tìm thấy hang động có ký hiệu. Ánh sáng đang tìm đến người mới.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Tối thứ Sáu",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Nhớ về những người đi trước",
                "activities": [
                    {"title": "Flashcards: Nhớ về những người đi trước",
                     "description": "Học 4 từ: extraordinary, sacrificed, murmured, comfortable",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Nhớ về những người đi trước",
                     "description": "Sam nắm tay Maya. Họ ngồi im ngắm sao. Maya nghĩ về Eleanor, Catherine, Margaret — những phụ nữ đã hy sinh cả đời. Cô mang ký ức họ như ngọn nến trong bóng tối.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Nhớ về những người đi trước",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Goodnight",
                "activities": [
                    {"title": "Flashcards: Goodnight",
                     "description": "Học 4 từ: invitation, constellation, ancient, gentle",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Goodnight",
                     "description": "Đêm khuya, Maya xuống tầng hầm. Đặt tay lên sàn đá ấm, thì thầm 'Goodnight.' Ánh sáng đập nhẹ một nhịp — biết ơn, yêu thương. Cô lên giường, nhìn sao qua cửa sổ. She was home.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Goodnight",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 20",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 20 — chương cuối cùng. Từ ngôi nhà mới đến lời chào buổi tối với ánh sáng. THE END.",
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
    print(f"Chapter 20 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
