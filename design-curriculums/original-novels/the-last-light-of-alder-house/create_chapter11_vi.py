#!/usr/bin/env python3
"""Chapter 11: Cape Sorrow — bilingual Vietnamese-English curriculum."""

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
    "The drive south took two hours. The coast highway was narrow and winding, with the ocean on one side and dark forest "
    "on the other. Rain started falling as Maya passed through small towns she had never heard of — places with names like "
    "Driftwood, Seal Rock, and Whisper Creek.\n\n"
    "Cape Sorrow was not a town. It was barely a place at all. A small sign on the highway marked the turnoff — a dirt road "
    "that led through thick trees to a parking area overlooking the ocean. There was nothing else. No buildings, no people, "
    "no lights.\n\n"
    "Maya parked and got out. The rain had stopped, but the air was wet and cold. The sky was dark — it was a new moon "
    "tonight, she realized. The darkest night of the month. The night when the light was strongest.\n\n"
    "She stood at the edge of the cliff and looked down. Cape Sorrow was a rocky headland, jutting out into the ocean like "
    "a fist. The waves crashed against it with tremendous force, sending spray fifty feet into the air.\n\n"
    "And there, at the base of the cliff, she saw it.\n\n"
    "A glow. Faint but unmistakable. Blue-white, pulsing with the same rhythm as the light in Alder Bay.\n\n"
    "The second light."
)

SECTION_2 = (
    "Maya looked for a way down. The cliff here was steeper than at Alder House — almost vertical. But she found a narrow "
    "trail, half-hidden by bushes, that zigzagged down the rock face. It was dangerous, especially in the dark, but Maya "
    "didn't hesitate.\n\n"
    "She turned on her flashlight and started down.\n\n"
    "The trail was slippery with rain and loose rock. Twice, Maya's foot slipped, and she grabbed at roots and stones to "
    "keep from falling. The sound of the waves grew louder as she descended, until it was a constant roar that filled her "
    "ears.\n\n"
    "At the bottom, she found a narrow beach — more rocks than sand — at the base of the cliff. The waves washed over her "
    "boots, cold as ice. And ahead of her, in the cliff face, she saw an opening. A cave.\n\n"
    "The glow was coming from inside.\n\n"
    "Maya walked toward it. The cave entrance was low and wide, like a mouth. She ducked inside and found herself in a "
    "passage similar to the tunnel at Alder House — rough stone walls, low ceiling, the smell of salt and earth.\n\n"
    "The passage opened into a larger cave. And there, in the center of the cave floor, was another hole. Another circle "
    "of light.\n\n"
    "This light was different from the one at Alder House. It was the same color — blue-white — but it pulsed faster, more "
    "urgently. And it was brighter. Much brighter. The whole cave was lit up like daylight.\n\n"
    "And lying on the cave floor, next to the hole, was a young man.\n\nBen."
)

SECTION_3 = (
    "Maya ran to him and knelt down. He was alive — she could see his chest rising and falling. His eyes were closed, and "
    "his face was peaceful, as if he was having a pleasant dream. His clothes were dry, which made no sense — he should "
    "have been soaked from the ocean.\n\n"
    '"Ben," Maya said, shaking his shoulder. "Ben, wake up."\n\n'
    "He didn't respond. She shook harder.\n\n"
    '"Ben!"\n\n'
    "His eyes opened. They were blue — bright blue, brighter than normal. And for a moment, they didn't seem to see her. "
    "They seemed to see something else, something far away.\n\n"
    "Then he blinked, and his eyes returned to normal — brown, confused, scared.\n\n"
    '"Where am I?" he said. His voice was rough, like he hadn\'t used it in a long time.\n\n'
    '"You\'re in a cave. At Cape Sorrow. About sixty miles south of Alder Bay."\n\n'
    '"What?" Ben sat up, looking around wildly. "How did I get here? I was on my boat. I was fishing. And then the water '
    'started glowing, and..." He trailed off, his face pale. "Something pulled me in. Into the water. But I didn\'t drown. '
    "I could breathe. And I saw things — lights, under the water, moving like fish. And then I was here.\"\n\n"
    '"The light brought you here," Maya said. "I don\'t know why."\n\n'
    "Ben looked at the glowing hole in the floor. \"That's the same thing. The same light. It's in the water too?\"\n\n"
    "\"It's everywhere. Under the ground, under the ocean. It's a network.\" Maya helped him stand. \"Can you walk?\"\n\n"
    '"I think so." He was unsteady but upright. "My sister — Lily — she must be worried."\n\n'
    '"She is. Everyone is. We need to get you back."'
)

SECTION_4 = (
    "Maya led Ben toward the cave entrance. But as they reached the passage, something happened.\n\n"
    "The light behind them surged. It rose from the hole like a fountain, filling the cave with blinding brightness. Maya "
    "and Ben both turned, shielding their eyes.\n\n"
    "And in the light, Maya saw something.\n\n"
    "A figure. Standing in the glow, made of light itself. It was tall and thin, with no face, no features — just a shape, "
    "a silhouette of pure blue-white radiance.\n\n"
    "It raised one hand toward Maya.\n\n"
    "And she heard a voice. Not with her ears — with her mind. A voice that was not human, not animal, not anything she had "
    "ever heard before. It was like the sound of the ocean and the wind and the earth all speaking at once.\n\n"
    '"You came," the voice said. "We have been waiting."\n\n'
    "Maya stared at the figure. Her heart was pounding, but she was not afraid. The voice was gentle. Welcoming.\n\n"
    '"Who are you?" she asked.\n\n'
    '"We are the light. We are what was here before. We are what will be here after. We are the balance."\n\n'
    '"The balance," Maya repeated. "What does that mean?"\n\n'
    '"The earth is alive. It breathes. It dreams. We are its breath. We are its dreams. For thousands of years, we have '
    "lived beneath the surface, keeping the world in harmony. But the harmony is breaking.\"\n\n"
    '"Breaking how?"\n\n'
    '"The connections between us are weakening. The seven points are losing their strength. If they fail, the earth will '
    'lose its balance. The oceans will rise. The ground will shake. Everything on the surface will suffer."\n\n'
    'Maya felt cold. "What can I do?"'
)

SECTION_5 = (
    '"You are a bridge. Your family has always been a bridge between us and the surface world. You can strengthen the '
    "connections. You can restore the balance. But you must visit each of the seven points. You must touch each light. And "
    'you must do it before the next new moon."\n\n'
    '"That\'s only a month away," Maya said.\n\n'
    '"Yes. Time is short. The man who wants to seal us — he must be stopped. If he destroys even one point, the network '
    'will collapse."\n\n'
    "The figure began to fade. The light was sinking back into the hole.\n\n"
    '"Wait," Maya said. "Why did you take Ben? Why bring him here?"\n\n'
    '"To bring you here," the voice said. "We needed you to see. To understand. To begin."\n\n'
    "The light faded. The cave went dark except for Maya's flashlight. The figure was gone.\n\n"
    "Ben was staring at the place where the figure had stood. His mouth was open.\n\n"
    '"Did you see that?" he whispered.\n\n"Yes."\n\n"Did you hear it?"\n\n"Yes."\n\n'
    'They stood in silence for a moment. Then Ben said, "We should probably get out of this cave."\n\n'
    'Maya almost laughed. "Yeah. Probably."\n\n'
    "They climbed back up the cliff trail together. It was harder going up, especially for Ben, who was still weak. But "
    "they made it to the top, wet and exhausted, and collapsed next to Maya's car.\n\n"
    "Maya checked her phone. Three missed calls from Sam. Two from Lily. One from a number she didn't recognize.\n\n"
    "She called Sam first.\n\n"
    '"Maya! Where are you? Are you okay?"\n\n'
    '"I\'m fine. I found Ben. He\'s alive."\n\n'
    'She heard Sam exhale with relief. "Thank God. Where was he?"\n\n'
    '"Cape Sorrow. It\'s a long story. I\'ll explain when I get back." She paused. "How\'s the house?"\n\n'
    '"Quiet. No one\'s come up. But Maya — Frank is serious about tomorrow. He\'s got a truck full of concrete and six guys '
    'ready to go. He\'s planning to come at dawn."\n\n'
    "Maya looked at her watch. It was almost midnight. Dawn was in six hours.\n\n"
    '"I\'ll be back before then," she said. "Don\'t let anyone near the house."\n\n'
    "She hung up and turned to Ben. \"Can you drive?\"\n\n"
    '"I think so. Why?"\n\n'
    '"Because I need you to drive my car back to Alder Bay. I need to make a stop on the way."\n\n'
    '"A stop where?"\n\n'
    "Maya pulled out Catherine's map and pointed to the third circle on the coast.\n\n"
    '"Redwood Cove," she said. "I need to touch the light there too. I\'ve already done two — Alder Bay and Cape Sorrow. '
    'Five more to go."\n\n'
    'Ben stared at her. "You\'re serious."\n\n"Completely."\n\n'
    '"And you\'re going to do this tonight? In the dark? Alone?"\n\n'
    '"I don\'t have a choice. Frank is going to try to seal the light tomorrow. If I can strengthen even one more connection '
    'before then, it might help."\n\n'
    "Ben was quiet for a moment. Then he shook his head and smiled — a tired, disbelieving smile.\n\n"
    '"I\'m coming with you," he said.\n\n'
    '"Ben, you just woke up in a cave after being kidnapped by a supernatural light. You should go home."\n\n'
    '"My sister will kill me either way. Might as well do something useful first." He held out his hand. "Give me the map. '
    'I know the coast road. I can get us to Redwood Cove in an hour."\n\n'
    "Maya looked at him. Then she handed over the map.\n\n"
    '"Let\'s go," she said.'
)

FULL_CHAPTER = "\n\n".join([SECTION_1, SECTION_2, SECTION_3, SECTION_4, SECTION_5])

S1_VOCAB = ["winding", "headland", "tremendous", "unmistakable"]
S2_VOCAB = ["zigzagged", "urgently", "slippery", "silhouette"]
S3_VOCAB = ["unsteady", "trailed", "pleasant", "wildly"]
S4_VOCAB = ["radiance", "harmony", "weakening", "surged"]
S5_VOCAB = ["supernatural", "collapse", "exhausted", "disbelieving"]
ALL_VOCAB = S1_VOCAB + S2_VOCAB + S3_VOCAB + S4_VOCAB + S5_VOCAB


def build_curriculum():
    return {
        "title": "The Last Light of Alder House — Chương 11: Mũi Đất Buồn (Cape Sorrow)",
        "preview": {
            "text": (
                "Maya lái xe đến Cape Sorrow và tìm thấy Ben nằm bất tỉnh trong hang động bên "
                "ánh sáng thứ hai. Khi cả hai chuẩn bị rời đi, một hình bóng bằng ánh sáng "
                "xuất hiện — nói về sự cân bằng, bảy điểm sáng, và sứ mệnh của Maya. Ben tình "
                "nguyện đi cùng đến Redwood Cove. Học 20 từ vựng tiếng Anh trung cấp qua chương này."
            ),
        },
        "description": (
            "Học 20 từ vựng tiếng Anh trung cấp qua Chương 11. Maya tìm thấy Ben ở Cape Sorrow, "
            "gặp thực thể ánh sáng tiết lộ sứ mệnh, rồi cùng Ben lên đường đến ánh sáng thứ ba."
        ),
        "learningSessions": [
            {
                "title": "Buổi 1: Đến Cape Sorrow",
                "activities": [
                    {"title": "Flashcards: Đến Cape Sorrow",
                     "description": "Học 4 từ: winding, headland, tremendous, unmistakable",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S1_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Đến Cape Sorrow",
                     "description": "Maya lái hai tiếng về phía nam, đến mũi đất hoang vắng trong đêm trăng non — và thấy ánh sáng xanh trắng nhấp nháy dưới chân vách đá.",
                     "activityType": "reading", "practiceMinutes": 4,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                    {"title": "Nghe: Đến Cape Sorrow",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_1, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 2: Xuống hang động",
                "activities": [
                    {"title": "Flashcards: Xuống hang động",
                     "description": "Học 4 từ: zigzagged, urgently, slippery, silhouette",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S2_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Xuống hang động",
                     "description": "Maya leo xuống vách đá trơn trượt, vào hang và tìm thấy ánh sáng thứ hai — sáng hơn, nhịp nhanh hơn. Và Ben nằm đó.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                    {"title": "Nghe: Xuống hang động",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_2, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 3: Ben tỉnh dậy",
                "activities": [
                    {"title": "Flashcards: Ben tỉnh dậy",
                     "description": "Học 4 từ: unsteady, trailed, pleasant, wildly",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S3_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Ben tỉnh dậy",
                     "description": "Ben mở mắt — mắt xanh rực rồi trở lại bình thường. Anh kể bị kéo xuống nước nhưng không chết đuối, thấy ánh sáng bơi như cá.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                    {"title": "Nghe: Ben tỉnh dậy",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_3, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 4: Thực thể ánh sáng",
                "activities": [
                    {"title": "Flashcards: Thực thể ánh sáng",
                     "description": "Học 4 từ: radiance, harmony, weakening, surged",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S4_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Thực thể ánh sáng",
                     "description": "Ánh sáng phun lên như đài phun nước, một hình bóng xuất hiện. Nó nói về sự cân bằng của trái đất, bảy điểm sáng đang yếu đi, và Maya là cầu nối.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                    {"title": "Nghe: Thực thể ánh sáng",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 2,
                     "data": {"text": SECTION_4, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 5: Sứ mệnh và lên đường",
                "activities": [
                    {"title": "Flashcards: Sứ mệnh và lên đường",
                     "description": "Học 4 từ: supernatural, collapse, exhausted, disbelieving",
                     "activityType": "viewFlashcards", "practiceMinutes": 2,
                     "data": {"vocabList": S5_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Đọc: Sứ mệnh và lên đường",
                     "description": "Ánh sáng giao sứ mệnh — chạm bảy điểm trước trăng non. Ben quyết định đi cùng Maya đến Redwood Cove ngay trong đêm.",
                     "activityType": "reading", "practiceMinutes": 5,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                    {"title": "Nghe: Sứ mệnh và lên đường",
                     "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                     "activityType": "readAlong", "practiceMinutes": 3,
                     "data": {"text": SECTION_5, "audioSpeed": -0.2}},
                ],
            },
            {
                "title": "Buổi 6: Ôn tập toàn bộ chương",
                "activities": [
                    {"title": "Flashcards: Ôn tập Chương 11",
                     "description": "Ôn lại toàn bộ 20 từ vựng trong chương.",
                     "activityType": "viewFlashcards", "practiceMinutes": 5,
                     "data": {"vocabList": ALL_VOCAB, "audioSpeed": -0.2}},
                    {"title": "Nghe: Toàn bộ câu chuyện",
                     "description": "Nghe toàn bộ Chương 11 từ lúc Maya đến Cape Sorrow đến khi cùng Ben lên đường.",
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
    print(f"Chapter 11 vi-en curriculum id: {cid}")
    return cid

if __name__ == "__main__":
    main()
