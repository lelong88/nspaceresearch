"""
Chapter 7: Cơn Bão (The Storm)
A storm damages the garden and Linh faces a setback, but the community rallies.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 7."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["forecast", "thunder", "shelter"]
    vocab_2 = ["damage", "branch", "flood"]
    vocab_3 = ["despair", "ruin", "hopeless"]
    vocab_4 = ["repair", "teamwork", "effort"]
    vocab_5 = ["strength", "overcome", "determination"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "The weather forecast on Tuesday said a big storm was coming. Linh had never "
        "experienced an English storm before. In Melbourne, storms were hot and fast. "
        "Here, the sky turned dark grey and the wind began to blow from the north.\n\n"
        "By afternoon, the rain was heavy. Linh could hear thunder in the distance, "
        "getting closer. She closed all the windows and brought the garden tools inside. "
        "Mrs. Patterson called to check on her.\n\n"
        "\"Stay inside, dear. These autumn storms can be strong. The cottage is solid — "
        "it has survived worse than this.\"\n\n"
        "Linh made tea and sat by the window. She watched the trees bend in the wind. "
        "The rain hit the glass like small stones. She thought about the garden and "
        "hoped the plants would be safe.\n\n"
        "At eight o'clock, the power went out. Linh found candles in the kitchen drawer "
        "and lit them. She sat in the shelter of the old cottage, listening to the storm "
        "rage outside."
    )

    passage_2 = (
        "The storm lasted all night. Linh slept badly, waking up every time the wind "
        "shook the windows. At six in the morning, the rain finally stopped. She put "
        "on her boots and went outside.\n\n"
        "The damage was terrible. A large branch from the old oak tree had fallen across "
        "the garden path. The fence on the east side was broken. Water covered the lower "
        "part of the garden like a small flood.\n\n"
        "The greenhouse was the worst. Two glass panels had broken. Rain had come inside "
        "and soaked everything. The wooden workbench was wet. The bags of soil had burst "
        "open.\n\n"
        "Linh walked through the garden slowly. The rose bushes were bent and damaged. "
        "The herb garden was under water. Three weeks of work — clearing, planting, "
        "restoring — had been undone in one night.\n\n"
        "She stood in the middle of the garden and looked at the mess around her. She "
        "did not know where to start."
    )

    passage_3 = (
        "Linh sat on the wet garden bench and felt despair wash over her. Everything "
        "she had worked on was in ruin. The paths they had cleared were covered in mud "
        "and leaves. The new seedlings she had planted were gone.\n\n"
        "She thought about going home. Back to Melbourne, back to her normal life. "
        "What was she doing here, alone in a foreign country, trying to fix a garden "
        "that nature kept destroying?\n\n"
        "For a moment, everything felt hopeless. She looked at the broken greenhouse "
        "and the fallen tree branch and wanted to cry.\n\n"
        "Then she remembered something from the notebook. Minh Tran had written: "
        "\"A garden is not a thing you build once. It is a thing you build again and "
        "again. Every storm, every winter, every drought — the garden falls. And every "
        "spring, you plant again.\"\n\n"
        "Linh wiped her eyes. Her great-great-grandfather had survived a war. He had "
        "built a life in a country that was not his own. A storm was nothing compared "
        "to that."
    )

    passage_4 = (
        "By nine o'clock, Tom arrived with his truck. He had a chainsaw and rope to "
        "move the fallen branch. Sarah came with hot coffee and sandwiches. The two "
        "teenagers showed up with brooms and buckets.\n\n"
        "\"We heard about the damage,\" Tom said. \"Let us help.\"\n\n"
        "They worked all day. Tom cut the branch into pieces and moved them. Sarah and "
        "Linh pumped water out of the greenhouse. The teenagers swept mud from the "
        "paths. It was hard work, but the repair went faster than Linh expected.\n\n"
        "The teamwork was amazing. Everyone knew what to do. Tom fixed the broken fence "
        "with new wood. Sarah replanted the herbs that had survived. By the end of the "
        "day, the garden looked different — not perfect, but alive again.\n\n"
        "\"This is what villages do,\" Mrs. Patterson said, watching from her garden "
        "chair. \"We help each other. That is how we survive.\"\n\n"
        "Linh looked at her team and felt a wave of effort and love that she had never "
        "experienced before."
    )

    passage_5 = (
        "That evening, Linh sat alone in the kitchen. She was tired but she felt "
        "something new — a quiet strength inside her. The storm had tested her, and "
        "she had not given up.\n\n"
        "She opened the notebook and read Minh's words again: \"A garden is not a "
        "thing you build once.\" She understood now. The garden was like life. Things "
        "break. Things fall. But you can always start again.\n\n"
        "She thought about her mother in Melbourne. Their relationship was like the "
        "garden — damaged by time and silence. But maybe it could be repaired too. "
        "Maybe she could overcome the distance between them.\n\n"
        "Linh picked up her phone and typed a message to her mother: \"Mum, I found "
        "something amazing in the garden. I want to tell you about it. Can we talk "
        "tomorrow?\"\n\n"
        "She pressed send. It was a small step, but it took determination. She put "
        "the phone down and looked out at the garden in the moonlight. The storm was "
        "over. Tomorrow, she would keep digging."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Một cơn bão lớn tàn phá khu vườn — cây đổ, nhà kính vỡ, ba tuần công sức "
        "bị cuốn trôi trong một đêm. Linh gần như tuyệt vọng và muốn bỏ về Melbourne. "
        "Nhưng lời của cụ Minh trong cuốn sổ nhắc cô: 'Khu vườn không phải thứ bạn "
        "xây một lần.' Dân làng đến giúp sửa chữa, và Linh tìm thấy sức mạnh mới. "
        "Cô nhắn tin cho mẹ lần đầu tiên. Bạn sẽ ôn lại 15 từ vựng: forecast, thunder, "
        "shelter, damage, branch, flood, despair, ruin, hopeless, repair, teamwork, "
        "effort, strength, overcome, determination. Mỗi buổi học gồm thẻ từ vựng nhanh, "
        "đọc một đoạn truyện hấp dẫn và luyện nghe theo. Buổi 6 tổng ôn toàn bộ từ "
        "vựng và nghe lại cả chương."
    )

    description = (
        "Chương 7: Cơn bão tàn phá khu vườn, Linh gần tuyệt vọng nhưng dân làng đến "
        "giúp sửa chữa. Cô tìm thấy sức mạnh nội tâm và nhắn tin cho mẹ lần đầu. "
        "Luyện đọc 5 đoạn văn với 15 từ vựng sơ trung cấp."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Khu Vườn Những Lá Thư Bị Lãng Quên (The Garden of Forgotten Letters) — Chương 7: Cơn Bão (The Storm)",
        "language": "en",
        "userLanguage": "vi",
        "level": "preintermediate",
        "audioSpeed": -0.2,
        "preview": {
            "text": preview_text
        },
        "description": description,
        "learningSessions": []
    }

    # --- Helper to build sessions 1-5 ---
    passages = [passage_1, passage_2, passage_3, passage_4, passage_5]
    vocab_groups = [vocab_1, vocab_2, vocab_3, vocab_4, vocab_5]

    for i in range(5):
        session_num = i + 1
        vocab = vocab_groups[i]
        passage = passages[i]
        desc_preview = passage[:80].rstrip() + "..."

        session = {
            "title": f"Phần {session_num}",
            "activities": [
                {
                    "activityType": "viewFlashcards",
                    "title": f"Flashcards: Phần {session_num}",
                    "description": f"Học 3 từ: {', '.join(vocab)}",
                    "data": {
                        "vocabList": vocab,
                        "audioSpeed": -0.2
                    }
                },
                {
                    "activityType": "reading",
                    "title": f"Đọc: Phần {session_num}",
                    "description": desc_preview,
                    "data": {
                        "text": passage,
                        "audioSpeed": -0.2
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": f"Nghe: Phần {session_num}",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": passage
                    }
                }
            ]
        }
        curriculum["learningSessions"].append(session)

    # --- Session 6: Review ---
    review_session = {
        "title": "Ôn tập",
        "activities": [
            {
                "activityType": "viewFlashcards",
                "title": "Flashcards: Ôn tập Cơn Bão",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Cơn Bão.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
