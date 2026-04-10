"""
Create curriculum: Family Dinners (Bữa Cơm Gia Đình — Sợi Dây Kết Nối)
Level: beginner | Skill focus: balanced_skills | Content type: []
Topic: Relationships (family dinners) | 12 words (2 groups of 6) | 4 sessions | Bilingual (vi/en)
Tone: metaphor_led | Farewell tone: warm_accountability
"""

import sys
import json
import requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/vi-en-curriculum-expansion")
from validate_curriculum import validate_balanced_skills_beginner, validate_content_type_tags, validate_bilingual_prompts

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

# ── Vocabulary ──
# Group 1 (Session 1): family, dinner, gather, celebrate, grateful, relative
# Group 2 (Session 2): generation, tradition, prepare, delicious, toast, memory

W1 = ["family", "dinner", "gather", "celebrate", "grateful", "relative"]
W2 = ["generation", "tradition", "prepare", "delicious", "toast", "memory"]
ALL_WORDS = W1 + W2

content = {
    "title": "Bữa Cơm Gia Đình — Sợi Dây Kết Nối",
    "contentTypeTags": [],
    "description": (
        "BỮA CƠM GIA ĐÌNH LÀ CHIẾC CẦU NỐI GIỮA CÁC THẾ HỆ — VÀ BẠN ĐANG THIẾU NGÔN NGỮ ĐỂ BƯỚC LÊN CHIẾC CẦU ĐÓ.\n\n"
        "Bạn ngồi cạnh ông bà, cô chú, anh chị em. Mọi người cười nói, kể chuyện ngày xưa, "
        "nâng ly chúc mừng. Bạn muốn kể lại khoảnh khắc đó cho bạn bè nước ngoài — "
        "nhưng không biết nói 'sum họp' hay 'biết ơn' bằng tiếng Anh.\n\n"
        "Bữa cơm gia đình giống như một cuốn sách — mỗi món ăn là một trang, mỗi câu chuyện là một chương. "
        "Nhưng nếu bạn không có từ vựng, cuốn sách đó mãi đóng kín với thế giới bên ngoài. "
        "12 từ vựng trong bài học này sẽ mở cuốn sách đó ra.\n\n"
        "Sau bài học, bạn sẽ tự tin kể về bữa cơm gia đình, giới thiệu người thân, "
        "và chia sẻ truyền thống gia đình bằng tiếng Anh.\n\n"
        "Vừa học từ vựng ấm áp, vừa giữ gìn ký ức gia đình — "
        "mỗi từ là một sợi dây kết nối bạn với người thân và với thế giới."
    ),
    "preview": {
        "text": (
            "Picture a warm evening. Your whole family sits around a big table. "
            "Grandma tells a story. Dad raises his glass. Everyone laughs. "
            "You want to describe this moment in English, but the words escape you. "
            "This curriculum gives you 12 essential family dinner words — "
            "family, dinner, gather, celebrate, grateful, relative, generation, tradition, prepare, delicious, toast, and memory. "
            "Across four sessions, you will learn each word through flashcards, reading passages about real family meals "
            "in Vietnam, and guided writing exercises. By the end, you will confidently talk about family gatherings, "
            "describe traditions, and share warm memories in English — "
            "whether with foreign friends or in an English class."
        )
    },
    "learningSessions": [
        # ════════════════════════════════════════════
        # SESSION 1 — Phần 1 (Words: family, dinner, gather, celebrate, grateful, relative)
        # ════════════════════════════════════════════
        {
            "title": "Phần 1",
            "activities": [
                # ── introAudio: Welcome + Vocab Teaching ──
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài học",
                    "description": "Chào mừng bạn đến với bài học về bữa cơm gia đình bằng tiếng Anh.",
                    "data": {
                        "text": (
                            "Xin chào và chào mừng bạn đến với bài học 'Bữa Cơm Gia Đình — Sợi Dây Kết Nối'! "
                            "Hôm nay chúng ta sẽ học 6 từ vựng tiếng Anh rất quan trọng khi bạn nói về gia đình và bữa cơm chung. "
                            "Những từ này sẽ giúp bạn tự tin hơn khi kể về gia đình, mô tả bữa tiệc, và bày tỏ lòng biết ơn. "
                            "Sáu từ hôm nay là: family, dinner, gather, celebrate, grateful, và relative.\n\n"

                            "Từ đầu tiên là 'family'. Family là danh từ, nghĩa là 'gia đình'. "
                            "Ví dụ: 'My family eats together every evening.' — Gia đình tôi ăn cùng nhau mỗi tối. "
                            "Trong bài đọc, bạn sẽ thấy từ 'family' khi nhân vật nói về gia đình mình.\n\n"

                            "Từ thứ hai là 'dinner'. Dinner là danh từ, nghĩa là 'bữa tối' hoặc 'bữa cơm'. "
                            "Ví dụ: 'We have dinner at seven o'clock.' — Chúng tôi ăn tối lúc bảy giờ. "
                            "Trong bài đọc, từ 'dinner' xuất hiện khi nhân vật mô tả bữa cơm gia đình.\n\n"

                            "Từ thứ ba là 'gather'. Gather là động từ, nghĩa là 'tụ họp' hoặc 'sum họp'. "
                            "Ví dụ: 'We gather at grandma's house every Sunday.' — Chúng tôi tụ họp ở nhà bà mỗi Chủ nhật. "
                            "Trong bài đọc, bạn sẽ thấy từ 'gather' khi cả gia đình đến nhà bà ngoại.\n\n"

                            "Từ thứ tư là 'celebrate'. Celebrate là động từ, nghĩa là 'ăn mừng' hoặc 'kỷ niệm'. "
                            "Ví dụ: 'We celebrate my grandmother's birthday today.' — Hôm nay chúng tôi ăn mừng sinh nhật bà. "
                            "Trong bài đọc, 'celebrate' là hành động chính của bữa tiệc gia đình.\n\n"

                            "Từ thứ năm là 'grateful'. Grateful là tính từ, nghĩa là 'biết ơn'. "
                            "Ví dụ: 'I am grateful for my family.' — Tôi biết ơn gia đình mình. "
                            "Trong bài đọc, bạn sẽ thấy từ 'grateful' khi nhân vật bày tỏ lòng biết ơn.\n\n"

                            "Từ cuối cùng là 'relative'. Relative là danh từ, nghĩa là 'người thân' hoặc 'họ hàng'. "
                            "Ví dụ: 'Many relatives come to our house for Tết.' — Nhiều người thân đến nhà chúng tôi dịp Tết. "
                            "Trong bài đọc, từ 'relative' xuất hiện khi nhân vật kể về những người thân đến dự tiệc.\n\n"

                            "Bây giờ, hãy bắt đầu học từ vựng qua flashcards nhé!"
                        )
                    }
                },
                # ── viewFlashcards ──
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Bữa cơm gia đình (Phần 1)",
                    "description": "Học 6 từ: family, dinner, gather, celebrate, grateful, relative",
                    "data": {"vocabList": ["family", "dinner", "gather", "celebrate", "grateful", "relative"]}
                },
                # ── speakFlashcards ──
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Bữa cơm gia đình (Phần 1)",
                    "description": "Học 6 từ: family, dinner, gather, celebrate, grateful, relative",
                    "data": {"vocabList": ["family", "dinner", "gather", "celebrate", "grateful", "relative"]}
                },
                # ── vocabLevel1 ──
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Bữa cơm gia đình (Phần 1)",
                    "description": "Học 6 từ: family, dinner, gather, celebrate, grateful, relative",
                    "data": {"vocabList": ["family", "dinner", "gather", "celebrate", "grateful", "relative"]}
                },
                # ── vocabLevel2 ──
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Bữa cơm gia đình (Phần 1)",
                    "description": "Học 6 từ: family, dinner, gather, celebrate, grateful, relative",
                    "data": {"vocabList": ["family", "dinner", "gather", "celebrate", "grateful", "relative"]}
                },
                # ── reading ──
                {
                    "activityType": "reading",
                    "title": "Đọc: Sinh nhật bà ngoại",
                    "description": "Hà's family gathers for grandmother's birthday dinner.",
                    "data": {
                        "text": (
                            "Today is a special day. It is grandmother's birthday. "
                            "Hà's family gathers at her house.\n\n"
                            "Many relatives come. Uncle Hùng comes from Đà Nẵng. "
                            "Aunt Lan brings her children. The house is full of people.\n\n"
                            "They have a big dinner together. "
                            "There is rice, fish, soup, and fruit. "
                            "Everyone sits around the table.\n\n"
                            "Hà's father says, 'Let us celebrate grandmother's birthday!' "
                            "Everyone claps and smiles. "
                            "Hà feels grateful for her family. "
                            "She loves these dinner nights."
                        ),
                        "vocabList": ["family", "dinner", "gather", "celebrate", "grateful", "relative"]
                    }
                },
