"""
Chapter 9: Đối Mặt (The Confrontation)
Climax continues — Mai, David, and Whitfield expose Graves at a town meeting. Graves is arrested.
"""


def get_curriculum():
    """Return the complete curriculum dict for Chapter 9."""

    # --- Vocabulary: 15 A2-B1 words, 3 per passage ---
    vocab_1 = ["plan", "announce", "gather"]
    vocab_2 = ["crowd", "hall", "speech"]
    vocab_3 = ["proof", "deny", "witness"]
    vocab_4 = ["admit", "developer", "betray"]
    vocab_5 = ["justice", "arrest", "applause"]

    all_vocab = vocab_1 + vocab_2 + vocab_3 + vocab_4 + vocab_5

    # --- Reading passages (~150-200 words each) ---

    passage_1 = (
        "Mai, David, and Mr. Whitfield sat together in the underground vault. The "
        "old clockmaker looked tired but his eyes were clear. They needed a plan.\n\n"
        "\"We have the deed, the tunnel map, and your story,\" Mai said. \"That is "
        "enough to stop Graves. But we need the whole town to hear the truth.\"\n\n"
        "David agreed. \"If we go to the police alone, Graves will find a way to "
        "talk his way out. He has friends on the council. We need to announce this "
        "publicly.\"\n\n"
        "Mai thought for a moment. \"I will write an article for the local newspaper. "
        "Tom at the pub knows everyone in town. He can help us gather people for a "
        "meeting at the town hall.\"\n\n"
        "Mr. Whitfield nodded slowly. \"I have been hiding for three months. I am "
        "tired of being afraid. It is time.\"\n\n"
        "They agreed to meet the next evening. Mai would write the article. David "
        "would talk to Tom. And Mr. Whitfield would prepare to face the town again "
        "after his long disappearance."
    )

    passage_2 = (
        "The next evening, Mai stood outside the town hall. She could not believe "
        "how many people had come. A large crowd filled the street. Tom had done "
        "his job well. He had told everyone at the pub, and the news had spread "
        "quickly through the small town.\n\n"
        "Inside the hall, rows of wooden chairs were full. People stood along the "
        "walls. Mai saw Mrs. Chen near the front, and Lily from the post office "
        "was sitting by the window. Even Mrs. Blackwood had come.\n\n"
        "Mai walked to the front of the room. Her hands were shaking, but she "
        "kept her voice steady. She had prepared a short speech.\n\n"
        "\"Thank you all for coming tonight,\" she began. \"I came to Eldermere "
        "as a journalist to write a travel article. But I found something much "
        "more important. I found the truth about your clocktower, about Mr. "
        "Whitfield, and about what has been happening in this town.\"\n\n"
        "The room was completely silent. Every person was watching her."
    )

    passage_3 = (
        "Mai held up the old deed from 1890. \"This document is proof that the "
        "clocktower and the land around it belong to the people of Eldermere. It "
        "was signed by the Hargrove family and given to the town over a hundred "
        "years ago.\"\n\n"
        "She then showed the tunnel map and explained what she and David had found "
        "underground. The people in the room listened carefully. Some looked shocked. "
        "Others looked angry.\n\n"
        "Mr. Graves was sitting in the back row. His face was red. He stood up "
        "suddenly. \"This is nonsense,\" he said loudly. \"You cannot deny that I "
        "have served this town for twenty years. These are lies from a stranger.\"\n\n"
        "Mai looked at him calmly. \"I have one more witness,\" she said. She "
        "turned to the side door and nodded.\n\n"
        "The door opened. Mr. Whitfield walked into the room. He was thin and "
        "pale, but he stood straight. The crowd gasped. People covered their "
        "mouths. Mrs. Blackwood started to cry. The man they thought was dead "
        "was standing right in front of them."
    )

    passage_4 = (
        "The room was in shock. Mr. Whitfield walked slowly to the front. People "
        "reached out to touch his arm as he passed. He turned to face the crowd.\n\n"
        "\"I am sorry I disappeared,\" he said quietly. \"Three months ago, Mr. "
        "Graves came to my workshop. He told me to give him the deed. When I "
        "refused, he said he would make sure I could never speak about it. I was "
        "afraid, so I hid in the tunnels under the tower.\"\n\n"
        "Everyone looked at Graves. His face had gone white. He tried to speak "
        "but no words came out. Finally, he sat down heavily in his chair.\n\n"
        "\"I admit it,\" Graves said in a low voice. \"I knew about the deed. The "
        "council had a deal with a developer from London. They wanted to buy the "
        "tower land and build new houses. It would bring money to the town. I "
        "thought it was the right thing to do.\"\n\n"
        "\"You did not betray just the tower,\" David said, standing up. \"You "
        "betrayed the whole town. You threatened an old man and made him hide "
        "underground for three months.\""
    )

    passage_5 = (
        "The room erupted in angry voices. People stood up from their chairs. "
        "Tom shouted from the back, \"You had no right!\" Others called for "
        "Graves to resign from the council.\n\n"
        "Then Mrs. Chen stood up. The room went quiet. She was a respected woman "
        "in Eldermere. \"We are all angry,\" she said. \"But we must do the right "
        "thing. We must call the police and let justice decide.\"\n\n"
        "Mai nodded. She had already called the police station before the meeting. "
        "Within twenty minutes, two officers arrived at the town hall. They spoke "
        "to Mr. Whitfield and looked at the documents. Then they walked to Mr. "
        "Graves.\n\n"
        "\"Mr. Graves, we need you to come with us for questioning,\" one officer "
        "said. They led him out of the hall. It was not a formal arrest yet, but "
        "everyone knew it was coming.\n\n"
        "As Graves left the building, the room broke into applause. People clapped "
        "for Mr. Whitfield. They clapped for Mai. The silent clocktower had found "
        "its voice again."
    )

    full_chapter_text = "\n\n".join([passage_1, passage_2, passage_3, passage_4, passage_5])

    # --- Vietnamese metadata ---

    preview_text = (
        "Mai, David và ông Whitfield lên kế hoạch phơi bày sự thật trước toàn thị "
        "trấn. Mai viết bài báo, Tom giúp loan tin, và một cuộc họp được tổ chức tại "
        "tòa thị chính. Trước đám đông, Mai trình bày bằng chứng — tờ chứng thư, bản "
        "đồ đường hầm và lời khai của ông Whitfield. Graves cố phủ nhận nhưng khi ông "
        "Whitfield bước vào, cả phòng lặng đi. Graves buộc phải thú nhận âm mưu bán "
        "đất tháp đồng hồ cho nhà phát triển. Bạn sẽ ôn lại 15 từ vựng quen thuộc: "
        "plan, announce, gather, crowd, hall, speech, proof, deny, witness, admit, "
        "developer, betray, justice, arrest, applause. Mỗi buổi học gồm thẻ từ vựng "
        "nhanh, đọc một đoạn truyện hấp dẫn và luyện nghe theo. Buổi 6 tổng ôn toàn "
        "bộ từ vựng và nghe lại cả chương — giúp bạn đọc trôi chảy và tự tin hơn với "
        "tiếng Anh."
    )

    description = (
        "Chương 9 là cao trào của câu chuyện khi Mai tổ chức cuộc họp thị trấn để "
        "phơi bày sự thật. Graves bị vạch trần trước mọi người và bị cảnh sát đưa "
        "đi thẩm vấn. Bạn sẽ luyện đọc 5 đoạn văn với 15 từ vựng trình độ sơ trung "
        "cấp, rèn kỹ năng đọc hiểu qua ngữ cảnh tự nhiên."
    )

    # --- Build curriculum dict ---

    curriculum = {
        "title": "Tháp Đồng Hồ Im Lặng (The Silent Clocktower) — Chương 9: Đối Mặt (The Confrontation)",
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
                "title": "Flashcards: Ôn tập Đối Mặt",
                "description": "Ôn lại toàn bộ 15 từ vựng trong chương.",
                "data": {
                    "vocabList": all_vocab,
                    "audioSpeed": -0.2
                }
            },
            {
                "activityType": "readAlong",
                "title": "Nghe: Toàn bộ câu chuyện",
                "description": "Nghe toàn bộ chương Đối Mặt.",
                "data": {
                    "text": full_chapter_text
                }
            }
        ]
    }
    curriculum["learningSessions"].append(review_session)

    return curriculum
