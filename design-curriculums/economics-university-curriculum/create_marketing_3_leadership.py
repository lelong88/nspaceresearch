"""
Create curriculum: Leadership – Lãnh Đạo & Hành Vi Tổ Chức
Series E — Marketing & Quản Trị (Marketing & Management), curriculum #3, displayOrder 2
18 words | 5 sessions | metaphor_led tone | introspective guide farewell
"""

import sys
import json
import requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums/economics-university-curriculum")
from validate_curriculum import validate_all

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
API_BASE = "https://helloapi.step.is"

# ── Word groups ──────────────────────────────────────────────
W1 = ["leadership", "delegation", "motivation", "empowerment", "accountability", "vision"]
W2 = ["organizational", "culture", "hierarchy", "collaboration", "conflict", "negotiation"]
W3 = ["transformational", "situational", "mentorship", "succession", "resilience", "agility"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Leadership – Lãnh Đạo & Hành Vi Tổ Chức",
    "contentTypeTags": [],
    "description": (
        "MỘT TỔ CHỨC GIỐNG NHƯ MỘT DÀN NHẠC — NHẠC CỤ CÓ THỂ HOÀN HẢO, NHƯNG KHÔNG CÓ NHẠC TRƯỞNG THÌ CHỈ CÓ TIẾNG ỒN.\n\n"
        "Bạn ngồi trong lớp quản trị, giảng viên đặt câu hỏi: 'Vì sao cùng một đội ngũ, "
        "dưới tay người quản lý này thì làm việc xuất sắc, nhưng đổi sang người khác thì rời rạc?' "
        "Bạn hiểu câu trả lời bằng tiếng Việt — nhưng khi đề thi yêu cầu phân tích "
        "leadership styles, delegation strategies, và organizational culture bằng tiếng Anh, "
        "bạn bắt đầu loay hoay. Những khái niệm này không trừu tượng, "
        "nhưng chúng là ngôn ngữ chung của mọi tổ chức trên thế giới.\n\n"
        "Hãy nghĩ về 18 từ vựng này như bộ la bàn của người dẫn đường — "
        "một khi bạn đọc được la bàn, bạn sẽ thấy rõ cách các nhà lãnh đạo "
        "truyền cảm hứng, phân quyền, xây dựng văn hóa, và dẫn dắt tổ chức qua biến động. "
        "Từ transformational leadership đến organizational agility, từ conflict resolution đến succession planning — "
        "bạn sẽ nắm được 'ngôn ngữ' mà mọi nhà quản trị trên thế giới dùng để lãnh đạo.\n\n"
        "Sau khóa học, bạn sẽ tự tin phân tích phong cách lãnh đạo bằng tiếng Anh, "
        "thuyết trình về hành vi tổ chức trong bài tập nhóm, "
        "và viết báo cáo đánh giá văn hóa doanh nghiệp bằng thuật ngữ chuyên ngành quốc tế.\n\n"
        "18 từ vựng — từ leadership đến agility — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy lãnh đạo và quản trị, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về lãnh đạo và hành vi tổ chức — "
            "ngôn ngữ chung của mọi nhà quản trị trên thế giới. "
            "Bạn sẽ học leadership, delegation, motivation, empowerment, accountability, vision trong phần đầu tiên, "
            "nơi bài đọc giải thích cách nhà lãnh đạo truyền cảm hứng và phân quyền hiệu quả. "
            "Tiếp theo là organizational, culture, hierarchy, collaboration, conflict, negotiation — "
            "những từ giúp bạn hiểu cách tổ chức vận hành, xung đột phát sinh và được giải quyết. "
            "Cuối cùng, transformational, situational, mentorship, succession, resilience, agility "
            "đưa bạn vào thế giới phong cách lãnh đạo hiện đại và khả năng thích ứng của tổ chức. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin phân tích lãnh đạo và hành vi tổ chức bằng tiếng Anh — "
            "không cần dừng lại tra từ điển mỗi dòng."
        )
    },
    "learningSessions": [
        # ── SESSION 1: Words 1-6 ─────────────────────────────
        {
            "title": "Phần 1",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 1",
                    "description": "Chào mừng bạn đến với bài học về lãnh đạo và hành vi tổ chức.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học thứ ba trong chuỗi từ vựng Marketing và Quản trị — "
                            "chủ đề hôm nay là Lãnh đạo và Hành vi tổ chức, hay trong tiếng Anh là Leadership and Organizational Behavior. "
                            "Mỗi tổ chức, dù là startup năm người hay tập đoàn mười nghìn nhân viên, "
                            "đều cần một người biết cách dẫn dắt — không chỉ ra lệnh, mà truyền cảm hứng. "
                            "Từ Viettel đến Google, từ quán cà phê nhỏ đến ngân hàng lớn — "
                            "tất cả đều vận hành dựa trên cùng một bộ nguyên tắc lãnh đạo.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: leadership, delegation, motivation, empowerment, accountability, và vision. "
                            "Đây là những từ nền tảng nhất — bạn sẽ gặp chúng trong mọi bài giảng về quản trị.\n\n"
                            "Từ đầu tiên là leadership — danh từ — nghĩa là lãnh đạo, "
                            "khả năng dẫn dắt, truyền cảm hứng và định hướng cho người khác để đạt được mục tiêu chung. "
                            "Ví dụ: 'Effective leadership requires more than authority — it demands the ability to listen, adapt, and inspire people to give their best even during difficult times.' "
                            "Trong bài đọc, leadership là chủ đề trung tâm — "
                            "mọi khía cạnh của hành vi tổ chức đều xoay quanh cách người lãnh đạo hành động.\n\n"
                            "Từ thứ hai là delegation — danh từ — nghĩa là ủy quyền, "
                            "việc giao nhiệm vụ và trách nhiệm cho người khác thay vì tự mình làm tất cả. "
                            "Ví dụ: 'The manager's delegation of the market analysis project to her junior team members allowed her to focus on strategic planning while giving them valuable experience.' "
                            "Trong bài đọc, delegation là kỹ năng quan trọng nhất mà nhà lãnh đạo cần học — "
                            "không ai có thể làm mọi thứ một mình.\n\n"
                            "Từ thứ ba là motivation — danh từ — nghĩa là động lực, "
                            "lý do bên trong hoặc bên ngoài thúc đẩy con người hành động và nỗ lực. "
                            "Ví dụ: 'The company discovered that employee motivation increased significantly when managers recognized individual contributions publicly rather than only rewarding team results.' "
                            "Trong bài đọc, motivation giải thích vì sao cùng một công việc, "
                            "có người làm hết mình còn có người chỉ làm cho xong.\n\n"
                            "Từ thứ tư là empowerment — danh từ — nghĩa là trao quyền, "
                            "việc trao cho nhân viên quyền tự quyết định và chịu trách nhiệm trong phạm vi công việc. "
                            "Ví dụ: 'Employee empowerment at the Vietnamese tech startup meant that any engineer could propose and lead a new project without waiting for approval from senior management.' "
                            "Trong bài đọc, empowerment là bước tiến xa hơn delegation — "
                            "không chỉ giao việc, mà còn giao quyền quyết định.\n\n"
                            "Từ thứ năm là accountability — danh từ — nghĩa là trách nhiệm giải trình, "
                            "nghĩa vụ chịu trách nhiệm về kết quả công việc và giải thích hành động của mình. "
                            "Ví dụ: 'The new CEO established a culture of accountability where every department head had to present monthly results and explain any deviation from the targets.' "
                            "Trong bài đọc, accountability là mặt kia của empowerment — "
                            "khi được trao quyền, bạn cũng phải chịu trách nhiệm về kết quả.\n\n"
                            "Từ cuối cùng là vision — danh từ — nghĩa là tầm nhìn, "
                            "bức tranh rõ ràng và đầy cảm hứng về tương lai mà nhà lãnh đạo muốn tổ chức hướng tới. "
                            "Ví dụ: 'The founder's vision of making quality education accessible to every child in rural Vietnam motivated the entire team to work through countless challenges without losing hope.' "
                            "Trong bài đọc, vision là điểm khởi đầu của mọi hành trình lãnh đạo — "
                            "không có tầm nhìn, tổ chức chỉ đi mà không biết đi đâu.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về cách nhà lãnh đạo truyền cảm hứng và phân quyền nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Lãnh đạo, ủy quyền và tầm nhìn",
                    "description": "Học 6 từ: leadership, delegation, motivation, empowerment, accountability, vision",
                    "data": {"vocabList": ["leadership", "delegation", "motivation", "empowerment", "accountability", "vision"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Lãnh đạo, ủy quyền và tầm nhìn",
                    "description": "Học 6 từ: leadership, delegation, motivation, empowerment, accountability, vision",
                    "data": {"vocabList": ["leadership", "delegation", "motivation", "empowerment", "accountability", "vision"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Lãnh đạo, ủy quyền và tầm nhìn",
                    "description": "Học 6 từ: leadership, delegation, motivation, empowerment, accountability, vision",
                    "data": {"vocabList": ["leadership", "delegation", "motivation", "empowerment", "accountability", "vision"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Lãnh đạo, ủy quyền và tầm nhìn",
                    "description": "Học 6 từ: leadership, delegation, motivation, empowerment, accountability, vision",
                    "data": {"vocabList": ["leadership", "delegation", "motivation", "empowerment", "accountability", "vision"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Lãnh đạo, ủy quyền và tầm nhìn",
                    "description": "Học 6 từ: leadership, delegation, motivation, empowerment, accountability, vision",
                    "data": {"vocabList": ["leadership", "delegation", "motivation", "empowerment", "accountability", "vision"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Nghệ thuật lãnh đạo và truyền cảm hứng",
                    "description": "What separates a manager from a leader is not a title on a business card — it is the ability to move people.",
                    "data": {
                        "text": (
                            "What separates a manager from a leader is not a title on a business card — "
                            "it is the ability to move people. "
                            "A manager tells employees what to do. "
                            "A leader inspires them to want to do it. "
                            "This distinction lies at the heart of leadership.\n\n"
                            "Leadership is the capacity to guide a group of people toward a shared goal. "
                            "It is not about having the loudest voice in the room "
                            "or making every decision alone. "
                            "The best leaders understand that their role is to create conditions "
                            "where others can do their best work. "
                            "In Vietnamese companies, this shift from command-and-control "
                            "to collaborative leadership is happening rapidly, "
                            "especially in the technology and startup sectors.\n\n"
                            "One of the most important skills a leader must develop is delegation. "
                            "Delegation means assigning tasks and responsibilities to others. "
                            "Many new managers struggle with delegation because they believe "
                            "they can do the work faster or better themselves. "
                            "But a leader who refuses to delegate becomes a bottleneck. "
                            "The team waits for one person to review, approve, and decide everything. "
                            "Effective delegation frees the leader to focus on strategy "
                            "while developing the skills and confidence of team members.\n\n"
                            "Delegation alone is not enough — people also need motivation. "
                            "Motivation is the internal or external force that drives people to act. "
                            "Some employees are motivated by financial rewards — bonuses, raises, promotions. "
                            "Others are motivated by recognition, meaningful work, or the chance to learn new skills. "
                            "A skilled leader learns what motivates each individual on the team "
                            "and creates an environment where those motivations are fulfilled. "
                            "Research shows that intrinsic motivation — the desire to do something "
                            "because it is personally rewarding — produces more sustained effort "
                            "than extrinsic motivation like money alone.\n\n"
                            "Beyond motivation, modern leadership emphasizes empowerment. "
                            "Empowerment goes further than delegation. "
                            "When a leader delegates, they assign a task. "
                            "When a leader empowers, they give people the authority to make decisions "
                            "within their area of responsibility. "
                            "An empowered employee does not need to ask permission for every small choice. "
                            "They have the trust and the tools to act independently. "
                            "In a Vietnamese manufacturing company, empowerment might mean "
                            "allowing floor supervisors to stop the production line "
                            "when they spot a quality problem, without waiting for a manager's approval.\n\n"
                            "With empowerment comes accountability. "
                            "Accountability means being responsible for the outcomes of your decisions "
                            "and being willing to explain them. "
                            "A culture of accountability does not mean punishing mistakes. "
                            "It means creating an environment where people own their results — "
                            "both successes and failures — and learn from them. "
                            "When accountability is absent, blame-shifting becomes the norm, "
                            "and the organization loses the ability to improve.\n\n"
                            "Finally, every great leader needs a clear vision. "
                            "Vision is a compelling picture of the future that the leader wants to create. "
                            "It answers the question: where are we going, and why does it matter? "
                            "A strong vision gives the team direction and purpose. "
                            "Without vision, daily tasks feel disconnected and meaningless. "
                            "With vision, even routine work becomes part of something larger. "
                            "The most effective leaders communicate their vision constantly — "
                            "not just in speeches, but in every decision they make and every priority they set."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Nghệ thuật lãnh đạo và truyền cảm hứng",
                    "description": "What separates a manager from a leader is not a title on a business card — it is the ability to move people.",
                    "data": {
                        "text": (
                            "What separates a manager from a leader is not a title on a business card — "
                            "it is the ability to move people. "
                            "A manager tells employees what to do. "
                            "A leader inspires them to want to do it. "
                            "This distinction lies at the heart of leadership.\n\n"
                            "Leadership is the capacity to guide a group of people toward a shared goal. "
                            "It is not about having the loudest voice in the room "
                            "or making every decision alone. "
                            "The best leaders understand that their role is to create conditions "
                            "where others can do their best work. "
                            "In Vietnamese companies, this shift from command-and-control "
                            "to collaborative leadership is happening rapidly, "
                            "especially in the technology and startup sectors.\n\n"
                            "One of the most important skills a leader must develop is delegation. "
                            "Delegation means assigning tasks and responsibilities to others. "
                            "Many new managers struggle with delegation because they believe "
                            "they can do the work faster or better themselves. "
                            "But a leader who refuses to delegate becomes a bottleneck. "
                            "The team waits for one person to review, approve, and decide everything. "
                            "Effective delegation frees the leader to focus on strategy "
                            "while developing the skills and confidence of team members.\n\n"
                            "Delegation alone is not enough — people also need motivation. "
                            "Motivation is the internal or external force that drives people to act. "
                            "Some employees are motivated by financial rewards — bonuses, raises, promotions. "
                            "Others are motivated by recognition, meaningful work, or the chance to learn new skills. "
                            "A skilled leader learns what motivates each individual on the team "
                            "and creates an environment where those motivations are fulfilled. "
                            "Research shows that intrinsic motivation — the desire to do something "
                            "because it is personally rewarding — produces more sustained effort "
                            "than extrinsic motivation like money alone.\n\n"
                            "Beyond motivation, modern leadership emphasizes empowerment. "
                            "Empowerment goes further than delegation. "
                            "When a leader delegates, they assign a task. "
                            "When a leader empowers, they give people the authority to make decisions "
                            "within their area of responsibility. "
                            "An empowered employee does not need to ask permission for every small choice. "
                            "They have the trust and the tools to act independently. "
                            "In a Vietnamese manufacturing company, empowerment might mean "
                            "allowing floor supervisors to stop the production line "
                            "when they spot a quality problem, without waiting for a manager's approval.\n\n"
                            "With empowerment comes accountability. "
                            "Accountability means being responsible for the outcomes of your decisions "
                            "and being willing to explain them. "
                            "A culture of accountability does not mean punishing mistakes. "
                            "It means creating an environment where people own their results — "
                            "both successes and failures — and learn from them. "
                            "When accountability is absent, blame-shifting becomes the norm, "
                            "and the organization loses the ability to improve.\n\n"
                            "Finally, every great leader needs a clear vision. "
                            "Vision is a compelling picture of the future that the leader wants to create. "
                            "It answers the question: where are we going, and why does it matter? "
                            "A strong vision gives the team direction and purpose. "
                            "Without vision, daily tasks feel disconnected and meaningless. "
                            "With vision, even routine work becomes part of something larger. "
                            "The most effective leaders communicate their vision constantly — "
                            "not just in speeches, but in every decision they make and every priority they set."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Nghệ thuật lãnh đạo và truyền cảm hứng",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "What separates a manager from a leader is not a title on a business card — "
                            "it is the ability to move people. "
                            "A manager tells employees what to do. "
                            "A leader inspires them to want to do it. "
                            "This distinction lies at the heart of leadership.\n\n"
                            "Leadership is the capacity to guide a group of people toward a shared goal. "
                            "It is not about having the loudest voice in the room "
                            "or making every decision alone. "
                            "The best leaders understand that their role is to create conditions "
                            "where others can do their best work. "
                            "In Vietnamese companies, this shift from command-and-control "
                            "to collaborative leadership is happening rapidly, "
                            "especially in the technology and startup sectors.\n\n"
                            "One of the most important skills a leader must develop is delegation. "
                            "Delegation means assigning tasks and responsibilities to others. "
                            "Many new managers struggle with delegation because they believe "
                            "they can do the work faster or better themselves. "
                            "But a leader who refuses to delegate becomes a bottleneck. "
                            "The team waits for one person to review, approve, and decide everything. "
                            "Effective delegation frees the leader to focus on strategy "
                            "while developing the skills and confidence of team members.\n\n"
                            "Delegation alone is not enough — people also need motivation. "
                            "Motivation is the internal or external force that drives people to act. "
                            "Some employees are motivated by financial rewards — bonuses, raises, promotions. "
                            "Others are motivated by recognition, meaningful work, or the chance to learn new skills. "
                            "A skilled leader learns what motivates each individual on the team "
                            "and creates an environment where those motivations are fulfilled. "
                            "Research shows that intrinsic motivation — the desire to do something "
                            "because it is personally rewarding — produces more sustained effort "
                            "than extrinsic motivation like money alone.\n\n"
                            "Beyond motivation, modern leadership emphasizes empowerment. "
                            "Empowerment goes further than delegation. "
                            "When a leader delegates, they assign a task. "
                            "When a leader empowers, they give people the authority to make decisions "
                            "within their area of responsibility. "
                            "An empowered employee does not need to ask permission for every small choice. "
                            "They have the trust and the tools to act independently. "
                            "In a Vietnamese manufacturing company, empowerment might mean "
                            "allowing floor supervisors to stop the production line "
                            "when they spot a quality problem, without waiting for a manager's approval.\n\n"
                            "With empowerment comes accountability. "
                            "Accountability means being responsible for the outcomes of your decisions "
                            "and being willing to explain them. "
                            "A culture of accountability does not mean punishing mistakes. "
                            "It means creating an environment where people own their results — "
                            "both successes and failures — and learn from them. "
                            "When accountability is absent, blame-shifting becomes the norm, "
                            "and the organization loses the ability to improve.\n\n"
                            "Finally, every great leader needs a clear vision. "
                            "Vision is a compelling picture of the future that the leader wants to create. "
                            "It answers the question: where are we going, and why does it matter? "
                            "A strong vision gives the team direction and purpose. "
                            "Without vision, daily tasks feel disconnected and meaningless. "
                            "With vision, even routine work becomes part of something larger. "
                            "The most effective leaders communicate their vision constantly — "
                            "not just in speeches, but in every decision they make and every priority they set."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Lãnh đạo, ủy quyền và tầm nhìn",
                    "description": "Viết câu sử dụng 6 từ vựng về lãnh đạo và truyền cảm hứng.",
                    "data": {
                        "vocabList": ["leadership", "delegation", "motivation", "empowerment", "accountability", "vision"],
                        "items": [
                            {
                                "targetVocab": "leadership",
                                "prompt": "Dùng từ 'leadership' để viết một câu về cách phong cách lãnh đạo ảnh hưởng đến hiệu suất đội nhóm. Ví dụ: The company's leadership style shifted from top-down command to collaborative decision-making, resulting in a thirty percent increase in employee satisfaction scores."
                            },
                            {
                                "targetVocab": "delegation",
                                "prompt": "Dùng từ 'delegation' để viết một câu về cách một nhà quản lý giao việc hiệu quả cho đội ngũ. Ví dụ: Through careful delegation of the product launch tasks, the director ensured that each team member worked on assignments matching their strengths while she focused on client relationships."
                            },
                            {
                                "targetVocab": "motivation",
                                "prompt": "Dùng từ 'motivation' để viết một câu về yếu tố thúc đẩy nhân viên làm việc hiệu quả hơn. Ví dụ: The survey revealed that employee motivation was driven more by opportunities for professional growth and meaningful projects than by salary increases alone."
                            },
                            {
                                "targetVocab": "empowerment",
                                "prompt": "Dùng từ 'empowerment' để viết một câu về cách trao quyền cho nhân viên cải thiện hiệu suất tổ chức. Ví dụ: The bank's empowerment policy allowed branch managers to approve loans up to five hundred million dong without consulting headquarters, cutting the approval time from two weeks to two days."
                            },
                            {
                                "targetVocab": "accountability",
                                "prompt": "Dùng từ 'accountability' để viết một câu về văn hóa trách nhiệm giải trình trong doanh nghiệp. Ví dụ: The new performance review system strengthened accountability by requiring every project leader to present measurable outcomes and explain any gaps between targets and actual results."
                            },
                            {
                                "targetVocab": "vision",
                                "prompt": "Dùng từ 'vision' để viết một câu về cách tầm nhìn của nhà lãnh đạo định hướng chiến lược tổ chức. Ví dụ: The founder's vision of building Vietnam's first globally recognized software company inspired engineers to stay with the firm despite receiving higher salary offers from foreign competitors."
                            }
                        ]
                    }
                }
            ]
        },
