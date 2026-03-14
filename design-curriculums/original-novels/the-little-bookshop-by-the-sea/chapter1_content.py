def get_content():
    # Session reading passages — plain text from novel Chapter 1 (bold markers stripped)
    s1_text = (
        "Emma sat at her kitchen table in London. It was a grey Tuesday morning. "
        "She was drinking tea and looking at her phone when the postman knocked.\n\n"
        "He gave her a large brown envelope. It looked official. Her name was typed "
        "on the front: Emma Clarke.\n\n"
        "She opened it carefully. Inside was a letter from a lawyer named Mr. Davies. "
        "The letter said that her grandmother, Margaret Clarke, had died two weeks ago. "
        "Emma read the words again slowly. She did not cry. She just sat very still.\n\n"
        "The letter asked her to come to Cornwall. There were papers to sign. At the "
        "bottom of the page, there was a line for her signature. She put the letter "
        "down and looked out the window. The sky was the same grey as before, but "
        "everything felt different now."
    )

    s2_text = (
        "The letter explained more. Emma's grandmother had left her something. She "
        "would inherit a small bookshop in a town called Saltwick. Emma had not been "
        "there since she was eight years old.\n\n"
        "The bookshop was the only property Gran owned. It was on the main street, "
        "near the sea. Mr. Davies wrote that the shop had been closed since Gran "
        "became ill.\n\n"
        "The funeral had already happened. Emma felt a sharp pain in her chest when "
        "she read that. Nobody had told her. She had not spoken to Gran in years. Her "
        "mother never talked about Cornwall or the family there. Now it was too late.\n\n"
        "Emma put the letter back in the envelope. She needed to go. She did not know "
        "what she would do with a bookshop, but she knew she had to see it."
    )

    s3_text = (
        "The next morning, Emma took a taxi to Paddington Station. She bought a "
        "ticket to Cornwall. The train would take five hours.\n\n"
        "The countryside outside London was flat and green. Emma watched it pass "
        "through the window. Fields, farms, small villages. Everything moved slowly "
        "here. It was so different from the city.\n\n"
        "She was the only passenger in her section of the train. It was quiet. She "
        "could hear the sound of the wheels on the track. She closed her eyes for a "
        "moment and tried to remember Gran's face.\n\n"
        "At the last stop, she stood on the platform with her bag. The air smelled "
        "like salt and grass. A small sign said \"Saltwick — 3 miles.\" There were no "
        "taxis. She would have to find another way."
    )

    s4_text = (
        "Emma pulled her luggage behind her. She had packed only one small suitcase. "
        "She did not plan to stay long — maybe three or four days. Just enough time "
        "to sign the papers and decide what to do with the shop.\n\n"
        "The journey from the station to the town was along a narrow road. She walked "
        "past hedges and stone walls. A few cars passed, but mostly it was just her "
        "and the birds.\n\n"
        "After forty minutes, she began to see houses. Then a church. Then a row of "
        "shops. She had started to arrive. The town was small and quiet. The buildings "
        "were old, painted white and blue. She could hear the sea somewhere close.\n\n"
        "Emma stopped walking. She looked around. She was here. She was really here."
    )

    s5_text = (
        "Standing in the middle of the main street, Emma felt a memory come back. "
        "She was eight years old, holding Gran's hand, walking to the bookshop. Gran "
        "was laughing. The sun was warm. That was the last summer she visited.\n\n"
        "Now she was a stranger here. Nobody knew her. The few people on the street "
        "looked at her with polite curiosity but did not stop. She was just a woman "
        "with a suitcase.\n\n"
        "She felt nervous. What would the bookshop look like? Would it be empty? "
        "Would it feel like Gran? She did not know what to expect.\n\n"
        "She took a deep breath and started walking again. The bookshop was somewhere "
        "on this street. She would find it. She had come this far. There was no reason "
        "to stop now."
    )

    return {
        "title": "Tiệm Sách Nhỏ Bên Biển (The Little Bookshop by the Sea) — Chương 1: Tin Buồn (The News)",
        "preview": {
            "text": (
                "Emma nhận được một lá thư bất ngờ từ luật sư — bà ngoại đã qua đời và để lại cho cô một tiệm sách nhỏ ở Cornwall. "
                "Trong chương mở đầu đầy cảm xúc này, bạn sẽ theo chân Emma từ căn bếp ở London đến một thị trấn ven biển xa lạ. "
                "Bạn sẽ ôn lại 15 từ vựng quen thuộc: envelope, lawyer, signature, inherit, property, funeral, countryside, passenger, "
                "platform, luggage, journey, arrive, memory, stranger và nervous. Mỗi buổi học gồm thẻ từ vựng nhanh, đọc một đoạn "
                "truyện hấp dẫn và luyện đọc theo. Qua 5 đoạn văn ngắn, bạn sẽ cảm nhận được nỗi buồn, sự bất ngờ và quyết tâm "
                "của Emma khi bắt đầu hành trình mới. Buổi 6 tổng ôn toàn bộ từ vựng và đọc lại cả chương — giúp bạn đọc trôi chảy "
                "và tự tin hơn với tiếng Anh."
            )
        },
        "description": (
            "Chương 1 kể về Emma nhận tin bà ngoại qua đời và thừa kế tiệm sách ở Cornwall. "
            "Bạn sẽ luyện đọc 5 đoạn văn với 15 từ vựng trình độ sơ trung cấp, rèn kỹ năng đọc hiểu qua ngữ cảnh tự nhiên."
        ),
        "learningSessions": [
            {
                "activities": [
                    {"activityType": "viewFlashcards", "data": {"vocabList": ["envelope", "lawyer", "signature"], "audioSpeed": -0.2}},
                    {"activityType": "reading", "data": {"text": s1_text, "audioSpeed": -0.2}},
                    {"activityType": "readAlong", "data": {"text": s1_text}},
                ]
            },
            {
                "activities": [
                    {"activityType": "viewFlashcards", "data": {"vocabList": ["inherit", "property", "funeral"], "audioSpeed": -0.2}},
                    {"activityType": "reading", "data": {"text": s2_text, "audioSpeed": -0.2}},
                    {"activityType": "readAlong", "data": {"text": s2_text}},
                ]
            },
            {
                "activities": [
                    {"activityType": "viewFlashcards", "data": {"vocabList": ["countryside", "passenger", "platform"], "audioSpeed": -0.2}},
                    {"activityType": "reading", "data": {"text": s3_text, "audioSpeed": -0.2}},
                    {"activityType": "readAlong", "data": {"text": s3_text}},
                ]
            },
            {
                "activities": [
                    {"activityType": "viewFlashcards", "data": {"vocabList": ["luggage", "journey", "arrive"], "audioSpeed": -0.2}},
                    {"activityType": "reading", "data": {"text": s4_text, "audioSpeed": -0.2}},
                    {"activityType": "readAlong", "data": {"text": s4_text}},
                ]
            },
            {
                "activities": [
                    {"activityType": "viewFlashcards", "data": {"vocabList": ["memory", "stranger", "nervous"], "audioSpeed": -0.2}},
                    {"activityType": "reading", "data": {"text": s5_text, "audioSpeed": -0.2}},
                    {"activityType": "readAlong", "data": {"text": s5_text}},
                ]
            },
            {
                "activities": [
                    {
                        "activityType": "viewFlashcards",
                        "data": {
                            "vocabList": [
                                "envelope", "lawyer", "signature",
                                "inherit", "property", "funeral",
                                "countryside", "passenger", "platform",
                                "luggage", "journey", "arrive",
                                "memory", "stranger", "nervous",
                            ],
                            "audioSpeed": -0.2,
                        },
                    },
                    {
                        "activityType": "readAlong",
                        "data": {
                            "text": "\n\n".join([s1_text, s2_text, s3_text, s4_text, s5_text]),
                        },
                    },
                ]
            },
        ],
    }
