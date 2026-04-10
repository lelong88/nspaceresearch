"""
Create curriculum: Corporate Governance – Quản Trị Doanh Nghiệp
Series D — Kế Toán & Tài Chính Doanh Nghiệp (Accounting & Corporate Finance), curriculum #5
18 words | 5 sessions | empathetic_observation tone | introspective guide farewell
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
W1 = ["governance", "board", "director", "fiduciary", "accountability", "transparency"]
W2 = ["stakeholder", "shareholder", "proxy", "charter", "bylaw", "oversight"]
W3 = ["whistleblower", "ethics", "conflict", "disclosure", "remuneration", "succession"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Corporate Governance – Quản Trị Doanh Nghiệp",
    "contentTypeTags": [],
    "description": (
        "BẠN ĐÃ BAO GIỜ TỰ HỎI VÌ SAO MỘT DOANH NGHIỆP LỚN CÓ THỂ SỤP ĐỔ CHỈ VÌ MỘT QUYẾT ĐỊNH SAI CỦA BAN LÃNH ĐẠO?\n\n"
        "Bạn đọc tin tức về những vụ bê bối doanh nghiệp — CEO bị sa thải vì xung đột lợi ích, "
        "hội đồng quản trị bị cổ đông kiện vì thiếu minh bạch, nhân viên tố giác gian lận nội bộ. "
        "Bạn hiểu câu chuyện bằng tiếng Việt, nhưng khi đọc bài nghiên cứu tiếng Anh về "
        "governance, fiduciary duty, hay whistleblower protection — bạn cảm thấy như đang đứng ngoài cuộc trò chuyện.\n\n"
        "Quản trị doanh nghiệp không phải là chuyện xa vời — nó là hệ thống 'phanh' và 'lái' "
        "giữ cho mọi tổ chức đi đúng hướng. Không có governance tốt, "
        "một công ty có lợi nhuận tỷ đô vẫn có thể lao xuống vực chỉ trong vài tháng. "
        "Hãy nghĩ về 18 từ vựng này như bản đồ hệ thống quyền lực bên trong doanh nghiệp — "
        "từ board và director đến stakeholder và shareholder, "
        "từ ethics và accountability đến whistleblower và succession.\n\n"
        "Sau khóa học, bạn sẽ tự tin đọc báo cáo quản trị doanh nghiệp bằng tiếng Anh, "
        "hiểu cách hội đồng quản trị vận hành, phân tích xung đột lợi ích trong case study, "
        "và viết nhận xét về cơ chế giám sát doanh nghiệp bằng ngôn ngữ chuyên ngành.\n\n"
        "18 từ vựng — từ governance đến succession — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy quản trị doanh nghiệp, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về quản trị doanh nghiệp — "
            "ngôn ngữ của quyền lực, trách nhiệm và minh bạch trong tổ chức. "
            "Bạn sẽ học governance, board, director, fiduciary, accountability, transparency trong phần đầu tiên, "
            "nơi bài đọc giải thích cách hội đồng quản trị vận hành và nghĩa vụ ủy thác của người lãnh đạo. "
            "Tiếp theo là stakeholder, shareholder, proxy, charter, bylaw, oversight — "
            "những từ giúp bạn hiểu cơ chế giám sát và quyền biểu quyết của cổ đông. "
            "Cuối cùng, whistleblower, ethics, conflict, disclosure, remuneration, succession "
            "đưa bạn vào thế giới đạo đức kinh doanh, tố giác gian lận và kế hoạch kế nhiệm. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin phân tích cơ chế quản trị doanh nghiệp bằng tiếng Anh — "
            "từ phòng họp hội đồng quản trị đến báo cáo thường niên."
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
                    "description": "Chào mừng bạn đến với bài học về quản trị doanh nghiệp.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học cuối cùng trong chuỗi từ vựng Kế toán và Tài chính doanh nghiệp — "
                            "chủ đề hôm nay là Quản trị doanh nghiệp, hay trong tiếng Anh là Corporate Governance. "
                            "Nếu kế toán là ngôn ngữ của tiền bạc, thì quản trị doanh nghiệp là ngôn ngữ của quyền lực và trách nhiệm. "
                            "Ai ra quyết định? Ai giám sát? Ai chịu trách nhiệm khi mọi thứ đi sai hướng? "
                            "Đây là những câu hỏi mà corporate governance trả lời.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: governance, board, director, fiduciary, accountability, và transparency. "
                            "Đây là bộ từ nền tảng về cấu trúc quyền lực trong doanh nghiệp.\n\n"
                            "Từ đầu tiên là governance — danh từ — nghĩa là quản trị, "
                            "hệ thống các quy tắc, thực tiễn và quy trình mà một tổ chức được điều hành và kiểm soát. "
                            "Ví dụ: 'Good corporate governance ensures that the company is managed in the best interests of all parties, not just the executives who run it day to day.' "
                            "Trong bài đọc, governance là khái niệm bao trùm — "
                            "nó bao gồm mọi cơ chế giúp doanh nghiệp hoạt động minh bạch và có trách nhiệm.\n\n"
                            "Từ thứ hai là board — danh từ — nghĩa là hội đồng, "
                            "thường dùng trong cụm board of directors — hội đồng quản trị, "
                            "nhóm người được bầu để giám sát và định hướng chiến lược cho doanh nghiệp. "
                            "Ví dụ: 'The board meets quarterly to review the company's financial performance, approve major investments, and evaluate the CEO's leadership.' "
                            "Trong bài đọc, board là cơ quan quyền lực cao nhất — "
                            "họ đại diện cho cổ đông và chịu trách nhiệm cuối cùng về mọi quyết định lớn.\n\n"
                            "Từ thứ ba là director — danh từ — nghĩa là thành viên hội đồng quản trị, "
                            "người được bầu hoặc bổ nhiệm vào hội đồng để giám sát hoạt động doanh nghiệp. "
                            "Ví dụ: 'The independent directors on the board have no financial ties to the company, which allows them to make objective decisions without personal bias.' "
                            "Trong bài đọc, director có hai loại: executive director — người vừa quản lý vừa ngồi trong hội đồng, "
                            "và independent director — người bên ngoài, đảm bảo tính khách quan.\n\n"
                            "Từ thứ tư là fiduciary — tính từ/danh từ — nghĩa là ủy thác, "
                            "nghĩa vụ pháp lý phải hành động vì lợi ích tốt nhất của người khác. "
                            "Ví dụ: 'Directors have a fiduciary duty to act in the best interests of shareholders, which means they cannot use company resources for personal gain.' "
                            "Trong bài đọc, fiduciary duty là nền tảng đạo đức của quản trị — "
                            "nó buộc người lãnh đạo phải đặt lợi ích của tổ chức lên trên lợi ích cá nhân.\n\n"
                            "Từ thứ năm là accountability — danh từ — nghĩa là trách nhiệm giải trình, "
                            "nghĩa vụ phải chịu trách nhiệm về hành động và quyết định của mình. "
                            "Ví dụ: 'The new governance framework increased accountability by requiring every executive to report their decisions and results to the board each quarter.' "
                            "Trong bài đọc, accountability là cơ chế đảm bảo rằng "
                            "không ai trong doanh nghiệp có thể hành động mà không phải giải trình.\n\n"
                            "Từ cuối cùng là transparency — danh từ — nghĩa là minh bạch, "
                            "việc công khai thông tin để các bên liên quan có thể đánh giá và giám sát. "
                            "Ví dụ: 'Transparency in financial reporting means that investors can see exactly how the company earns and spends its money, with no hidden transactions.' "
                            "Trong bài đọc, transparency là nguyên tắc sống còn — "
                            "thiếu minh bạch, niềm tin của nhà đầu tư và công chúng sẽ sụp đổ.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về cách hội đồng quản trị vận hành và nghĩa vụ ủy thác nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Quản trị, hội đồng và trách nhiệm",
                    "description": "Học 6 từ: governance, board, director, fiduciary, accountability, transparency",
                    "data": {"vocabList": ["governance", "board", "director", "fiduciary", "accountability", "transparency"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Quản trị, hội đồng và trách nhiệm",
                    "description": "Học 6 từ: governance, board, director, fiduciary, accountability, transparency",
                    "data": {"vocabList": ["governance", "board", "director", "fiduciary", "accountability", "transparency"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Quản trị, hội đồng và trách nhiệm",
                    "description": "Học 6 từ: governance, board, director, fiduciary, accountability, transparency",
                    "data": {"vocabList": ["governance", "board", "director", "fiduciary", "accountability", "transparency"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Quản trị, hội đồng và trách nhiệm",
                    "description": "Học 6 từ: governance, board, director, fiduciary, accountability, transparency",
                    "data": {"vocabList": ["governance", "board", "director", "fiduciary", "accountability", "transparency"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Quản trị, hội đồng và trách nhiệm",
                    "description": "Học 6 từ: governance, board, director, fiduciary, accountability, transparency",
                    "data": {"vocabList": ["governance", "board", "director", "fiduciary", "accountability", "transparency"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Hội đồng quản trị và nghĩa vụ ủy thác",
                    "description": "Every corporation, whether it is a small family business or a multinational giant, needs a system of rules and practices to guide how it is managed.",
                    "data": {
                        "text": (
                            "Every corporation, whether it is a small family business or a multinational giant, "
                            "needs a system of rules and practices to guide how it is managed. "
                            "This system is called corporate governance. "
                            "Governance determines who makes decisions, who monitors those decisions, "
                            "and how the interests of different groups are balanced.\n\n"
                            "At the center of corporate governance is the board of directors. "
                            "The board is a group of individuals elected by shareholders "
                            "to oversee the company's management and strategic direction. "
                            "In Vietnam, publicly listed companies are required by law "
                            "to have a board that meets regularly and reports to shareholders. "
                            "The board does not run the company day to day — "
                            "that is the job of the CEO and the management team. "
                            "Instead, the board sets the overall direction, approves major decisions, "
                            "and holds management accountable for results.\n\n"
                            "Each member of the board is called a director. "
                            "There are two main types of directors. "
                            "Executive directors are also part of the company's management — "
                            "for example, the CEO might sit on the board. "
                            "Independent directors, on the other hand, have no management role "
                            "and no financial relationship with the company beyond their board position. "
                            "Independent directors are considered essential for good governance "
                            "because they can challenge management decisions without personal bias.\n\n"
                            "Every director has a fiduciary duty to the company and its shareholders. "
                            "A fiduciary duty is a legal obligation to act in the best interests of others, "
                            "not in one's own interest. "
                            "This means a director cannot approve a deal that benefits a friend's company "
                            "at the expense of shareholders. "
                            "If a director violates this duty, shareholders can take legal action. "
                            "Fiduciary responsibility is the moral and legal backbone of corporate governance.\n\n"
                            "Accountability is another pillar of good governance. "
                            "Accountability means that every person in a position of power "
                            "must answer for their actions and decisions. "
                            "The CEO is accountable to the board. "
                            "The board is accountable to the shareholders. "
                            "When accountability breaks down — when leaders can act without consequences — "
                            "the risk of mismanagement and fraud increases dramatically.\n\n"
                            "Closely linked to accountability is transparency. "
                            "Transparency means making information available openly and honestly. "
                            "A transparent company publishes detailed financial reports, "
                            "discloses executive compensation, and explains its decision-making processes. "
                            "Without transparency, shareholders and the public cannot evaluate "
                            "whether the company is being managed well. "
                            "Together, accountability and transparency form the foundation "
                            "on which all other governance practices are built."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Hội đồng quản trị và nghĩa vụ ủy thác",
                    "description": "Every corporation, whether it is a small family business or a multinational giant, needs a system of rules and practices to guide how it is managed.",
                    "data": {
                        "text": (
                            "Every corporation, whether it is a small family business or a multinational giant, "
                            "needs a system of rules and practices to guide how it is managed. "
                            "This system is called corporate governance. "
                            "Governance determines who makes decisions, who monitors those decisions, "
                            "and how the interests of different groups are balanced.\n\n"
                            "At the center of corporate governance is the board of directors. "
                            "The board is a group of individuals elected by shareholders "
                            "to oversee the company's management and strategic direction. "
                            "In Vietnam, publicly listed companies are required by law "
                            "to have a board that meets regularly and reports to shareholders. "
                            "The board does not run the company day to day — "
                            "that is the job of the CEO and the management team. "
                            "Instead, the board sets the overall direction, approves major decisions, "
                            "and holds management accountable for results.\n\n"
                            "Each member of the board is called a director. "
                            "There are two main types of directors. "
                            "Executive directors are also part of the company's management — "
                            "for example, the CEO might sit on the board. "
                            "Independent directors, on the other hand, have no management role "
                            "and no financial relationship with the company beyond their board position. "
                            "Independent directors are considered essential for good governance "
                            "because they can challenge management decisions without personal bias.\n\n"
                            "Every director has a fiduciary duty to the company and its shareholders. "
                            "A fiduciary duty is a legal obligation to act in the best interests of others, "
                            "not in one's own interest. "
                            "This means a director cannot approve a deal that benefits a friend's company "
                            "at the expense of shareholders. "
                            "If a director violates this duty, shareholders can take legal action. "
                            "Fiduciary responsibility is the moral and legal backbone of corporate governance.\n\n"
                            "Accountability is another pillar of good governance. "
                            "Accountability means that every person in a position of power "
                            "must answer for their actions and decisions. "
                            "The CEO is accountable to the board. "
                            "The board is accountable to the shareholders. "
                            "When accountability breaks down — when leaders can act without consequences — "
                            "the risk of mismanagement and fraud increases dramatically.\n\n"
                            "Closely linked to accountability is transparency. "
                            "Transparency means making information available openly and honestly. "
                            "A transparent company publishes detailed financial reports, "
                            "discloses executive compensation, and explains its decision-making processes. "
                            "Without transparency, shareholders and the public cannot evaluate "
                            "whether the company is being managed well. "
                            "Together, accountability and transparency form the foundation "
                            "on which all other governance practices are built."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Hội đồng quản trị và nghĩa vụ ủy thác",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Every corporation, whether it is a small family business or a multinational giant, "
                            "needs a system of rules and practices to guide how it is managed. "
                            "This system is called corporate governance. "
                            "Governance determines who makes decisions, who monitors those decisions, "
                            "and how the interests of different groups are balanced.\n\n"
                            "At the center of corporate governance is the board of directors. "
                            "The board is a group of individuals elected by shareholders "
                            "to oversee the company's management and strategic direction. "
                            "In Vietnam, publicly listed companies are required by law "
                            "to have a board that meets regularly and reports to shareholders. "
                            "The board does not run the company day to day — "
                            "that is the job of the CEO and the management team. "
                            "Instead, the board sets the overall direction, approves major decisions, "
                            "and holds management accountable for results.\n\n"
                            "Each member of the board is called a director. "
                            "There are two main types of directors. "
                            "Executive directors are also part of the company's management — "
                            "for example, the CEO might sit on the board. "
                            "Independent directors, on the other hand, have no management role "
                            "and no financial relationship with the company beyond their board position. "
                            "Independent directors are considered essential for good governance "
                            "because they can challenge management decisions without personal bias.\n\n"
                            "Every director has a fiduciary duty to the company and its shareholders. "
                            "A fiduciary duty is a legal obligation to act in the best interests of others, "
                            "not in one's own interest. "
                            "This means a director cannot approve a deal that benefits a friend's company "
                            "at the expense of shareholders. "
                            "If a director violates this duty, shareholders can take legal action. "
                            "Fiduciary responsibility is the moral and legal backbone of corporate governance.\n\n"
                            "Accountability is another pillar of good governance. "
                            "Accountability means that every person in a position of power "
                            "must answer for their actions and decisions. "
                            "The CEO is accountable to the board. "
                            "The board is accountable to the shareholders. "
                            "When accountability breaks down — when leaders can act without consequences — "
                            "the risk of mismanagement and fraud increases dramatically.\n\n"
                            "Closely linked to accountability is transparency. "
                            "Transparency means making information available openly and honestly. "
                            "A transparent company publishes detailed financial reports, "
                            "discloses executive compensation, and explains its decision-making processes. "
                            "Without transparency, shareholders and the public cannot evaluate "
                            "whether the company is being managed well. "
                            "Together, accountability and transparency form the foundation "
                            "on which all other governance practices are built."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Quản trị, hội đồng và trách nhiệm",
                    "description": "Viết câu sử dụng 6 từ vựng về quản trị doanh nghiệp và hội đồng quản trị.",
                    "data": {
                        "vocabList": ["governance", "board", "director", "fiduciary", "accountability", "transparency"],
                        "items": [
                            {
                                "targetVocab": "governance",
                                "prompt": "Dùng từ 'governance' để viết một câu về hệ thống quản trị của một doanh nghiệp niêm yết và tầm quan trọng của nó. Ví dụ: The company reformed its corporate governance structure after investors complained that too much power was concentrated in the hands of the founding family."
                            },
                            {
                                "targetVocab": "board",
                                "prompt": "Dùng từ 'board' để viết một câu về vai trò của hội đồng quản trị trong việc giám sát doanh nghiệp. Ví dụ: The board voted unanimously to replace the CEO after an internal investigation revealed that he had approved several contracts without proper authorization."
                            },
                            {
                                "targetVocab": "director",
                                "prompt": "Dùng từ 'director' để viết một câu về vai trò của thành viên hội đồng quản trị độc lập. Ví dụ: The company appointed three independent directors to the board to ensure that management decisions were reviewed by people with no personal financial interest in the outcomes."
                            },
                            {
                                "targetVocab": "fiduciary",
                                "prompt": "Dùng từ 'fiduciary' để viết một câu về nghĩa vụ ủy thác của người lãnh đạo doanh nghiệp. Ví dụ: The court ruled that the former chairman had violated his fiduciary duty by approving a real estate deal that benefited his brother's company at the expense of shareholders."
                            },
                            {
                                "targetVocab": "accountability",
                                "prompt": "Dùng từ 'accountability' để viết một câu về cơ chế giải trình trong doanh nghiệp. Ví dụ: The new governance code strengthened accountability by requiring all senior executives to present their quarterly results directly to the board and answer questions from independent directors."
                            },
                            {
                                "targetVocab": "transparency",
                                "prompt": "Dùng từ 'transparency' để viết một câu về tầm quan trọng của minh bạch trong quản trị doanh nghiệp. Ví dụ: Investors praised the company for its transparency after it published a detailed report explaining every major decision made by the board during the previous fiscal year."
                            }
                        ]
                    }
                }
            ]
        },
        # ── SESSION 2: Words 7-12 ─────────────────────────────
        {
            "title": "Phần 2",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 2",
                    "description": "Ôn lại phần 1 và học 6 từ mới về cổ đông, giám sát và điều lệ doanh nghiệp.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "governance — quản trị, board — hội đồng, director — thành viên hội đồng quản trị, "
                            "fiduciary — ủy thác, accountability — trách nhiệm giải trình, và transparency — minh bạch. "
                            "Bạn đã hiểu cách hội đồng quản trị vận hành và nghĩa vụ pháp lý của người lãnh đạo. "
                            "Bây giờ, chúng ta sẽ đi vào một khía cạnh quan trọng khác: "
                            "quyền của cổ đông, cơ chế giám sát, và các văn bản pháp lý nội bộ.\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: stakeholder, shareholder, proxy, charter, bylaw, và oversight. "
                            "Đây là bộ từ vựng giúp bạn hiểu ai có quyền gì trong doanh nghiệp.\n\n"
                            "Từ đầu tiên là stakeholder — danh từ — nghĩa là bên liên quan, "
                            "bất kỳ cá nhân hoặc tổ chức nào bị ảnh hưởng bởi hoạt động của doanh nghiệp. "
                            "Ví dụ: 'The company's stakeholders include not only shareholders but also employees, customers, suppliers, local communities, and government regulators.' "
                            "Trong bài đọc, stakeholder là khái niệm rộng hơn shareholder — "
                            "nó bao gồm tất cả những ai có lợi ích gắn liền với doanh nghiệp.\n\n"
                            "Từ thứ hai là shareholder — danh từ — nghĩa là cổ đông, "
                            "người sở hữu cổ phần trong doanh nghiệp và có quyền biểu quyết. "
                            "Ví dụ: 'Shareholders have the right to vote on major decisions such as electing board members, approving mergers, and changing the company's charter.' "
                            "Trong bài đọc, shareholder là chủ sở hữu thực sự của doanh nghiệp — "
                            "hội đồng quản trị phải hành động vì lợi ích của họ.\n\n"
                            "Từ thứ ba là proxy — danh từ — nghĩa là ủy quyền, "
                            "quyền bỏ phiếu thay cho cổ đông khi họ không thể tham dự đại hội. "
                            "Ví dụ: 'Many small shareholders who cannot attend the annual meeting submit a proxy form authorizing another person to vote on their behalf.' "
                            "Trong bài đọc, proxy voting là cơ chế quan trọng — "
                            "nó cho phép cổ đông nhỏ lẻ vẫn có tiếng nói trong các quyết định lớn.\n\n"
                            "Từ thứ tư là charter — danh từ — nghĩa là điều lệ, "
                            "văn bản pháp lý thành lập doanh nghiệp, quy định mục đích và cấu trúc cơ bản. "
                            "Ví dụ: 'The company's charter specifies the maximum number of board members, the types of shares that can be issued, and the procedures for calling a special meeting.' "
                            "Trong bài đọc, charter là 'hiến pháp' của doanh nghiệp — "
                            "mọi quy tắc khác đều phải tuân theo nó.\n\n"
                            "Từ thứ năm là bylaw — danh từ — nghĩa là nội quy, "
                            "các quy tắc chi tiết hướng dẫn hoạt động hàng ngày của doanh nghiệp. "
                            "Ví dụ: 'The company's bylaws require that at least two-thirds of board members must be present for any vote to be valid.' "
                            "Trong bài đọc, bylaw bổ sung cho charter — "
                            "nếu charter là hiến pháp, thì bylaw là luật chi tiết.\n\n"
                            "Từ cuối cùng là oversight — danh từ — nghĩa là giám sát, "
                            "việc theo dõi và kiểm tra hoạt động của doanh nghiệp để đảm bảo tuân thủ. "
                            "Ví dụ: 'The audit committee provides independent oversight of the company's financial reporting to ensure that the numbers presented to investors are accurate and complete.' "
                            "Trong bài đọc, oversight là chức năng cốt lõi của hội đồng quản trị — "
                            "không có giám sát, quyền lực sẽ bị lạm dụng.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về quyền cổ đông và cơ chế giám sát doanh nghiệp nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Cổ đông, giám sát và điều lệ",
                    "description": "Học 6 từ: stakeholder, shareholder, proxy, charter, bylaw, oversight",
                    "data": {"vocabList": ["stakeholder", "shareholder", "proxy", "charter", "bylaw", "oversight"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Cổ đông, giám sát và điều lệ",
                    "description": "Học 6 từ: stakeholder, shareholder, proxy, charter, bylaw, oversight",
                    "data": {"vocabList": ["stakeholder", "shareholder", "proxy", "charter", "bylaw", "oversight"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Cổ đông, giám sát và điều lệ",
                    "description": "Học 6 từ: stakeholder, shareholder, proxy, charter, bylaw, oversight",
                    "data": {"vocabList": ["stakeholder", "shareholder", "proxy", "charter", "bylaw", "oversight"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Cổ đông, giám sát và điều lệ",
                    "description": "Học 6 từ: stakeholder, shareholder, proxy, charter, bylaw, oversight",
                    "data": {"vocabList": ["stakeholder", "shareholder", "proxy", "charter", "bylaw", "oversight"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Cổ đông, giám sát và điều lệ",
                    "description": "Học 6 từ: stakeholder, shareholder, proxy, charter, bylaw, oversight",
                    "data": {"vocabList": ["stakeholder", "shareholder", "proxy", "charter", "bylaw", "oversight"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Quyền cổ đông và cơ chế giám sát",
                    "description": "A corporation belongs to its shareholders — the people and institutions that own its shares.",
                    "data": {
                        "text": (
                            "A corporation belongs to its shareholders — "
                            "the people and institutions that own its shares. "
                            "But ownership and management are not the same thing. "
                            "Shareholders do not run the company day to day. "
                            "Instead, they elect a board of directors to manage on their behalf. "
                            "This separation of ownership and control creates a need "
                            "for rules, rights, and oversight mechanisms.\n\n"
                            "A shareholder's most important right is the right to vote. "
                            "At the annual general meeting, shareholders vote on critical matters: "
                            "electing directors, approving the annual financial statements, "
                            "and deciding on major transactions like mergers or acquisitions. "
                            "Each share typically carries one vote, "
                            "so shareholders with more shares have more influence.\n\n"
                            "But not every shareholder can attend the meeting in person. "
                            "A small investor in Ho Chi Minh City may own shares in a company "
                            "headquartered in Hanoi. This is where proxy voting becomes essential. "
                            "A proxy allows a shareholder to authorize someone else "
                            "to vote on their behalf. Before the meeting, "
                            "the company sends proxy materials explaining each issue to be voted on. "
                            "The shareholder then submits a proxy form indicating how they want to vote. "
                            "Proxy voting ensures that even absent shareholders "
                            "can participate in corporate decisions.\n\n"
                            "The rules that govern how a company operates are found in two key documents. "
                            "The first is the corporate charter. "
                            "The charter is the founding document that establishes the company as a legal entity. "
                            "It defines the company's purpose, the types of shares it can issue, "
                            "and the basic structure of its governance. "
                            "Changing the charter usually requires a vote by shareholders, "
                            "because it is the most fundamental document of the organization.\n\n"
                            "The second document is the set of bylaws. "
                            "Bylaws are more detailed than the charter "
                            "and cover the practical rules of daily governance. "
                            "They specify how often the board must meet, "
                            "how many directors are needed for a vote to be valid, "
                            "how new directors are nominated, and how conflicts of interest are handled. "
                            "While the charter sets the broad framework, "
                            "the bylaws fill in the operational details.\n\n"
                            "Beyond shareholders, a well-governed company also considers its stakeholders. "
                            "A stakeholder is anyone who is affected by the company's actions — "
                            "employees, customers, suppliers, local communities, and regulators. "
                            "Modern governance theory argues that companies should balance "
                            "the interests of all stakeholders, not just shareholders. "
                            "A company that pollutes a river to cut costs may increase short-term profits "
                            "for shareholders, but it harms the community — a key stakeholder.\n\n"
                            "Oversight is the mechanism that holds everything together. "
                            "The board provides oversight of management. "
                            "Audit committees provide oversight of financial reporting. "
                            "Regulators provide oversight of the entire industry. "
                            "Without effective oversight, even the best charter and bylaws "
                            "are just words on paper. "
                            "Good governance requires not only good rules "
                            "but also people and institutions willing to enforce them."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Quyền cổ đông và cơ chế giám sát",
                    "description": "A corporation belongs to its shareholders — the people and institutions that own its shares.",
                    "data": {
                        "text": (
                            "A corporation belongs to its shareholders — "
                            "the people and institutions that own its shares. "
                            "But ownership and management are not the same thing. "
                            "Shareholders do not run the company day to day. "
                            "Instead, they elect a board of directors to manage on their behalf. "
                            "This separation of ownership and control creates a need "
                            "for rules, rights, and oversight mechanisms.\n\n"
                            "A shareholder's most important right is the right to vote. "
                            "At the annual general meeting, shareholders vote on critical matters: "
                            "electing directors, approving the annual financial statements, "
                            "and deciding on major transactions like mergers or acquisitions. "
                            "Each share typically carries one vote, "
                            "so shareholders with more shares have more influence.\n\n"
                            "But not every shareholder can attend the meeting in person. "
                            "A small investor in Ho Chi Minh City may own shares in a company "
                            "headquartered in Hanoi. This is where proxy voting becomes essential. "
                            "A proxy allows a shareholder to authorize someone else "
                            "to vote on their behalf. Before the meeting, "
                            "the company sends proxy materials explaining each issue to be voted on. "
                            "The shareholder then submits a proxy form indicating how they want to vote. "
                            "Proxy voting ensures that even absent shareholders "
                            "can participate in corporate decisions.\n\n"
                            "The rules that govern how a company operates are found in two key documents. "
                            "The first is the corporate charter. "
                            "The charter is the founding document that establishes the company as a legal entity. "
                            "It defines the company's purpose, the types of shares it can issue, "
                            "and the basic structure of its governance. "
                            "Changing the charter usually requires a vote by shareholders, "
                            "because it is the most fundamental document of the organization.\n\n"
                            "The second document is the set of bylaws. "
                            "Bylaws are more detailed than the charter "
                            "and cover the practical rules of daily governance. "
                            "They specify how often the board must meet, "
                            "how many directors are needed for a vote to be valid, "
                            "how new directors are nominated, and how conflicts of interest are handled. "
                            "While the charter sets the broad framework, "
                            "the bylaws fill in the operational details.\n\n"
                            "Beyond shareholders, a well-governed company also considers its stakeholders. "
                            "A stakeholder is anyone who is affected by the company's actions — "
                            "employees, customers, suppliers, local communities, and regulators. "
                            "Modern governance theory argues that companies should balance "
                            "the interests of all stakeholders, not just shareholders. "
                            "A company that pollutes a river to cut costs may increase short-term profits "
                            "for shareholders, but it harms the community — a key stakeholder.\n\n"
                            "Oversight is the mechanism that holds everything together. "
                            "The board provides oversight of management. "
                            "Audit committees provide oversight of financial reporting. "
                            "Regulators provide oversight of the entire industry. "
                            "Without effective oversight, even the best charter and bylaws "
                            "are just words on paper. "
                            "Good governance requires not only good rules "
                            "but also people and institutions willing to enforce them."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Quyền cổ đông và cơ chế giám sát",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "A corporation belongs to its shareholders — "
                            "the people and institutions that own its shares. "
                            "But ownership and management are not the same thing. "
                            "Shareholders do not run the company day to day. "
                            "Instead, they elect a board of directors to manage on their behalf. "
                            "This separation of ownership and control creates a need "
                            "for rules, rights, and oversight mechanisms.\n\n"
                            "A shareholder's most important right is the right to vote. "
                            "At the annual general meeting, shareholders vote on critical matters: "
                            "electing directors, approving the annual financial statements, "
                            "and deciding on major transactions like mergers or acquisitions. "
                            "Each share typically carries one vote, "
                            "so shareholders with more shares have more influence.\n\n"
                            "But not every shareholder can attend the meeting in person. "
                            "A small investor in Ho Chi Minh City may own shares in a company "
                            "headquartered in Hanoi. This is where proxy voting becomes essential. "
                            "A proxy allows a shareholder to authorize someone else "
                            "to vote on their behalf. Before the meeting, "
                            "the company sends proxy materials explaining each issue to be voted on. "
                            "The shareholder then submits a proxy form indicating how they want to vote. "
                            "Proxy voting ensures that even absent shareholders "
                            "can participate in corporate decisions.\n\n"
                            "The rules that govern how a company operates are found in two key documents. "
                            "The first is the corporate charter. "
                            "The charter is the founding document that establishes the company as a legal entity. "
                            "It defines the company's purpose, the types of shares it can issue, "
                            "and the basic structure of its governance. "
                            "Changing the charter usually requires a vote by shareholders, "
                            "because it is the most fundamental document of the organization.\n\n"
                            "The second document is the set of bylaws. "
                            "Bylaws are more detailed than the charter "
                            "and cover the practical rules of daily governance. "
                            "They specify how often the board must meet, "
                            "how many directors are needed for a vote to be valid, "
                            "how new directors are nominated, and how conflicts of interest are handled. "
                            "While the charter sets the broad framework, "
                            "the bylaws fill in the operational details.\n\n"
                            "Beyond shareholders, a well-governed company also considers its stakeholders. "
                            "A stakeholder is anyone who is affected by the company's actions — "
                            "employees, customers, suppliers, local communities, and regulators. "
                            "Modern governance theory argues that companies should balance "
                            "the interests of all stakeholders, not just shareholders. "
                            "A company that pollutes a river to cut costs may increase short-term profits "
                            "for shareholders, but it harms the community — a key stakeholder.\n\n"
                            "Oversight is the mechanism that holds everything together. "
                            "The board provides oversight of management. "
                            "Audit committees provide oversight of financial reporting. "
                            "Regulators provide oversight of the entire industry. "
                            "Without effective oversight, even the best charter and bylaws "
                            "are just words on paper. "
                            "Good governance requires not only good rules "
                            "but also people and institutions willing to enforce them."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Cổ đông, giám sát và điều lệ",
                    "description": "Viết câu sử dụng 6 từ vựng về quyền cổ đông và cơ chế giám sát.",
                    "data": {
                        "vocabList": ["stakeholder", "shareholder", "proxy", "charter", "bylaw", "oversight"],
                        "items": [
                            {
                                "targetVocab": "stakeholder",
                                "prompt": "Dùng từ 'stakeholder' để viết một câu về các bên liên quan của doanh nghiệp và lợi ích khác nhau của họ. Ví dụ: The company held a stakeholder meeting to hear concerns from employees, local residents, and environmental groups before approving the new factory construction plan."
                            },
                            {
                                "targetVocab": "shareholder",
                                "prompt": "Dùng từ 'shareholder' để viết một câu về quyền biểu quyết của cổ đông tại đại hội. Ví dụ: The largest shareholder, holding thirty percent of the company's shares, used her voting power to block the proposed merger with a foreign competitor."
                            },
                            {
                                "targetVocab": "proxy",
                                "prompt": "Dùng từ 'proxy' để viết một câu về cơ chế bỏ phiếu ủy quyền tại đại hội cổ đông. Ví dụ: Over sixty percent of votes at the annual meeting were cast by proxy because most individual shareholders lived too far away to attend in person."
                            },
                            {
                                "targetVocab": "charter",
                                "prompt": "Dùng từ 'charter' để viết một câu về điều lệ doanh nghiệp và vai trò pháp lý của nó. Ví dụ: The company's charter limits the board to nine members and requires that at least one-third of them must be independent directors with no ties to management."
                            },
                            {
                                "targetVocab": "bylaw",
                                "prompt": "Dùng từ 'bylaw' để viết một câu về nội quy doanh nghiệp và cách nó hướng dẫn hoạt động hàng ngày. Ví dụ: According to the company's bylaws, any director who misses three consecutive board meetings without a valid reason will automatically lose their seat."
                            },
                            {
                                "targetVocab": "oversight",
                                "prompt": "Dùng từ 'oversight' để viết một câu về vai trò giám sát của hội đồng quản trị hoặc cơ quan quản lý. Ví dụ: The government strengthened regulatory oversight of the banking sector after several small banks collapsed due to risky lending practices that went unchecked for years."
                            }
                        ]
                    }
                }
            ]
        },
        # ── SESSION 3: Words 13-18 ────────────────────────────
        {
            "title": "Phần 3",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu từ vựng phần 3",
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về đạo đức, tố giác và kế nhiệm.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: governance, board, director, fiduciary, accountability, transparency — "
                            "những khái niệm cốt lõi về cấu trúc quyền lực và trách nhiệm trong doanh nghiệp. "
                            "Trong phần 2, bạn đã học thêm stakeholder, shareholder, proxy, charter, bylaw, oversight — "
                            "bộ từ vựng về quyền cổ đông, văn bản pháp lý nội bộ và cơ chế giám sát.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào một khía cạnh rất nhạy cảm nhưng cực kỳ quan trọng: "
                            "đạo đức kinh doanh, tố giác gian lận, và kế hoạch kế nhiệm lãnh đạo. "
                            "Bạn sẽ học 6 từ mới: whistleblower, ethics, conflict, disclosure, remuneration, và succession.\n\n"
                            "Từ đầu tiên là whistleblower — danh từ — nghĩa là người tố giác, "
                            "nhân viên hoặc cá nhân bên trong tổ chức báo cáo hành vi sai trái hoặc gian lận. "
                            "Ví dụ: 'The whistleblower reported that senior managers had been falsifying sales figures for over two years, leading to a full investigation by the securities regulator.' "
                            "Trong bài đọc, whistleblower là người dũng cảm — "
                            "họ chấp nhận rủi ro cá nhân để bảo vệ lợi ích chung.\n\n"
                            "Từ thứ hai là ethics — danh từ — nghĩa là đạo đức, "
                            "hệ thống nguyên tắc đạo đức hướng dẫn hành vi trong kinh doanh. "
                            "Ví dụ: 'The company's code of ethics prohibits employees from accepting gifts worth more than five hundred thousand dong from any supplier or business partner.' "
                            "Trong bài đọc, ethics là la bàn đạo đức — "
                            "nó giúp mọi người trong tổ chức phân biệt đúng sai khi đối mặt với tình huống khó.\n\n"
                            "Từ thứ ba là conflict — danh từ — nghĩa là xung đột, "
                            "thường dùng trong cụm conflict of interest — xung đột lợi ích, "
                            "tình huống khi lợi ích cá nhân mâu thuẫn với nghĩa vụ chuyên môn. "
                            "Ví dụ: 'The director declared a conflict of interest and excused herself from the vote because her husband's company was one of the bidders for the construction contract.' "
                            "Trong bài đọc, conflict of interest là một trong những rủi ro lớn nhất — "
                            "nếu không được phát hiện và xử lý, nó có thể phá hủy niềm tin của cổ đông.\n\n"
                            "Từ thứ tư là disclosure — danh từ — nghĩa là công bố thông tin, "
                            "nghĩa vụ phải tiết lộ thông tin quan trọng cho các bên liên quan. "
                            "Ví dụ: 'The governance code requires full disclosure of all related-party transactions so that shareholders can assess whether the deals were fair and in the company's best interest.' "
                            "Trong bài đọc, disclosure trong quản trị doanh nghiệp rộng hơn disclosure trong kế toán — "
                            "nó bao gồm cả thù lao lãnh đạo, xung đột lợi ích, và rủi ro tiềm ẩn.\n\n"
                            "Từ thứ năm là remuneration — danh từ — nghĩa là thù lao, "
                            "tổng thu nhập mà lãnh đạo doanh nghiệp nhận được, bao gồm lương, thưởng và cổ phiếu. "
                            "Ví dụ: 'The remuneration committee recommended a twenty percent increase in the CEO's bonus after the company exceeded its annual revenue target by a significant margin.' "
                            "Trong bài đọc, remuneration là chủ đề nhạy cảm — "
                            "cổ đông muốn biết lãnh đạo được trả bao nhiêu và liệu mức thù lao có xứng đáng.\n\n"
                            "Từ cuối cùng là succession — danh từ — nghĩa là kế nhiệm, "
                            "quá trình chuẩn bị và chuyển giao quyền lãnh đạo cho thế hệ tiếp theo. "
                            "Ví dụ: 'The board developed a detailed succession plan to ensure a smooth transition when the current CEO retires at the end of next year.' "
                            "Trong bài đọc, succession planning là dấu hiệu của quản trị tốt — "
                            "một doanh nghiệp không có kế hoạch kế nhiệm đang đặt tương lai vào tay may rủi.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về đạo đức kinh doanh và kế hoạch kế nhiệm nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Đạo đức, tố giác và kế nhiệm",
                    "description": "Học 6 từ: whistleblower, ethics, conflict, disclosure, remuneration, succession",
                    "data": {"vocabList": ["whistleblower", "ethics", "conflict", "disclosure", "remuneration", "succession"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Đạo đức, tố giác và kế nhiệm",
                    "description": "Học 6 từ: whistleblower, ethics, conflict, disclosure, remuneration, succession",
                    "data": {"vocabList": ["whistleblower", "ethics", "conflict", "disclosure", "remuneration", "succession"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Đạo đức, tố giác và kế nhiệm",
                    "description": "Học 6 từ: whistleblower, ethics, conflict, disclosure, remuneration, succession",
                    "data": {"vocabList": ["whistleblower", "ethics", "conflict", "disclosure", "remuneration", "succession"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Đạo đức, tố giác và kế nhiệm",
                    "description": "Học 6 từ: whistleblower, ethics, conflict, disclosure, remuneration, succession",
                    "data": {"vocabList": ["whistleblower", "ethics", "conflict", "disclosure", "remuneration", "succession"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Đạo đức, tố giác và kế nhiệm",
                    "description": "Học 6 từ: whistleblower, ethics, conflict, disclosure, remuneration, succession",
                    "data": {"vocabList": ["whistleblower", "ethics", "conflict", "disclosure", "remuneration", "succession"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Đạo đức kinh doanh, tố giác và kế nhiệm",
                    "description": "Corporate governance is not only about structures and rules — it is also about culture and values.",
                    "data": {
                        "text": (
                            "Corporate governance is not only about structures and rules — "
                            "it is also about culture and values. "
                            "A company can have a perfect charter, detailed bylaws, "
                            "and an impressive board of directors, "
                            "but if the people inside the organization do not act ethically, "
                            "the governance system will fail.\n\n"
                            "Ethics is the foundation of corporate culture. "
                            "Business ethics refers to the principles that guide "
                            "how people behave in a professional setting. "
                            "Most large companies have a written code of ethics "
                            "that sets clear expectations for employees at every level. "
                            "The code typically covers topics like honesty in financial reporting, "
                            "fair treatment of employees, responsible use of company resources, "
                            "and respect for the law. "
                            "A strong ethical culture does not eliminate wrongdoing entirely, "
                            "but it creates an environment where people are more likely "
                            "to do the right thing — and more likely to speak up when they see problems.\n\n"
                            "One of the most serious governance risks is a conflict of interest. "
                            "A conflict of interest occurs when a person in a position of power "
                            "has a personal interest that could influence their professional judgment. "
                            "For example, if a board member's family owns a company "
                            "that is bidding for a contract with the corporation, "
                            "that director has a conflict. "
                            "Good governance requires that conflicts be declared openly "
                            "and that the conflicted person step aside from the decision. "
                            "Failure to manage conflicts of interest can lead to unfair deals, "
                            "financial losses, and a collapse of trust.\n\n"
                            "Disclosure plays a critical role in managing these risks. "
                            "In the context of corporate governance, disclosure means "
                            "making important information available to shareholders and the public. "
                            "Companies must disclose executive compensation, related-party transactions, "
                            "potential conflicts of interest, and any material risks facing the business. "
                            "Without disclosure, shareholders cannot make informed decisions "
                            "about whether the company is being managed in their best interest.\n\n"
                            "When internal controls fail and wrongdoing occurs, "
                            "whistleblowers often become the last line of defense. "
                            "A whistleblower is someone inside the organization "
                            "who reports illegal or unethical behavior to authorities or the public. "
                            "Whistleblowing takes courage because the person often faces "
                            "retaliation from colleagues or superiors. "
                            "Many countries, including Vietnam, have laws that protect whistleblowers "
                            "from being fired or punished for reporting genuine concerns. "
                            "Companies with strong governance encourage whistleblowing "
                            "by creating anonymous reporting channels and promising protection.\n\n"
                            "Another important governance topic is executive remuneration. "
                            "Remuneration refers to the total compensation that senior leaders receive — "
                            "salary, bonuses, stock options, and other benefits. "
                            "A remuneration committee, usually made up of independent directors, "
                            "decides how much the CEO and other executives should be paid. "
                            "The goal is to set compensation that attracts talented leaders "
                            "while aligning their interests with those of shareholders. "
                            "If executives are paid too much regardless of performance, "
                            "shareholders lose trust in the governance system.\n\n"
                            "Finally, every well-governed company plans for succession. "
                            "Succession planning is the process of identifying and preparing "
                            "future leaders to take over key positions. "
                            "When a CEO retires, falls ill, or is removed, "
                            "the company needs a qualified replacement ready to step in. "
                            "Without a succession plan, a leadership vacuum can cause "
                            "confusion, falling stock prices, and loss of confidence among investors. "
                            "The best boards begin succession planning years in advance, "
                            "grooming internal candidates and maintaining a list of potential external hires."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Đạo đức kinh doanh, tố giác và kế nhiệm",
                    "description": "Corporate governance is not only about structures and rules — it is also about culture and values.",
                    "data": {
                        "text": (
                            "Corporate governance is not only about structures and rules — "
                            "it is also about culture and values. "
                            "A company can have a perfect charter, detailed bylaws, "
                            "and an impressive board of directors, "
                            "but if the people inside the organization do not act ethically, "
                            "the governance system will fail.\n\n"
                            "Ethics is the foundation of corporate culture. "
                            "Business ethics refers to the principles that guide "
                            "how people behave in a professional setting. "
                            "Most large companies have a written code of ethics "
                            "that sets clear expectations for employees at every level. "
                            "The code typically covers topics like honesty in financial reporting, "
                            "fair treatment of employees, responsible use of company resources, "
                            "and respect for the law. "
                            "A strong ethical culture does not eliminate wrongdoing entirely, "
                            "but it creates an environment where people are more likely "
                            "to do the right thing — and more likely to speak up when they see problems.\n\n"
                            "One of the most serious governance risks is a conflict of interest. "
                            "A conflict of interest occurs when a person in a position of power "
                            "has a personal interest that could influence their professional judgment. "
                            "For example, if a board member's family owns a company "
                            "that is bidding for a contract with the corporation, "
                            "that director has a conflict. "
                            "Good governance requires that conflicts be declared openly "
                            "and that the conflicted person step aside from the decision. "
                            "Failure to manage conflicts of interest can lead to unfair deals, "
                            "financial losses, and a collapse of trust.\n\n"
                            "Disclosure plays a critical role in managing these risks. "
                            "In the context of corporate governance, disclosure means "
                            "making important information available to shareholders and the public. "
                            "Companies must disclose executive compensation, related-party transactions, "
                            "potential conflicts of interest, and any material risks facing the business. "
                            "Without disclosure, shareholders cannot make informed decisions "
                            "about whether the company is being managed in their best interest.\n\n"
                            "When internal controls fail and wrongdoing occurs, "
                            "whistleblowers often become the last line of defense. "
                            "A whistleblower is someone inside the organization "
                            "who reports illegal or unethical behavior to authorities or the public. "
                            "Whistleblowing takes courage because the person often faces "
                            "retaliation from colleagues or superiors. "
                            "Many countries, including Vietnam, have laws that protect whistleblowers "
                            "from being fired or punished for reporting genuine concerns. "
                            "Companies with strong governance encourage whistleblowing "
                            "by creating anonymous reporting channels and promising protection.\n\n"
                            "Another important governance topic is executive remuneration. "
                            "Remuneration refers to the total compensation that senior leaders receive — "
                            "salary, bonuses, stock options, and other benefits. "
                            "A remuneration committee, usually made up of independent directors, "
                            "decides how much the CEO and other executives should be paid. "
                            "The goal is to set compensation that attracts talented leaders "
                            "while aligning their interests with those of shareholders. "
                            "If executives are paid too much regardless of performance, "
                            "shareholders lose trust in the governance system.\n\n"
                            "Finally, every well-governed company plans for succession. "
                            "Succession planning is the process of identifying and preparing "
                            "future leaders to take over key positions. "
                            "When a CEO retires, falls ill, or is removed, "
                            "the company needs a qualified replacement ready to step in. "
                            "Without a succession plan, a leadership vacuum can cause "
                            "confusion, falling stock prices, and loss of confidence among investors. "
                            "The best boards begin succession planning years in advance, "
                            "grooming internal candidates and maintaining a list of potential external hires."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Đạo đức kinh doanh, tố giác và kế nhiệm",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Corporate governance is not only about structures and rules — "
                            "it is also about culture and values. "
                            "A company can have a perfect charter, detailed bylaws, "
                            "and an impressive board of directors, "
                            "but if the people inside the organization do not act ethically, "
                            "the governance system will fail.\n\n"
                            "Ethics is the foundation of corporate culture. "
                            "Business ethics refers to the principles that guide "
                            "how people behave in a professional setting. "
                            "Most large companies have a written code of ethics "
                            "that sets clear expectations for employees at every level. "
                            "The code typically covers topics like honesty in financial reporting, "
                            "fair treatment of employees, responsible use of company resources, "
                            "and respect for the law. "
                            "A strong ethical culture does not eliminate wrongdoing entirely, "
                            "but it creates an environment where people are more likely "
                            "to do the right thing — and more likely to speak up when they see problems.\n\n"
                            "One of the most serious governance risks is a conflict of interest. "
                            "A conflict of interest occurs when a person in a position of power "
                            "has a personal interest that could influence their professional judgment. "
                            "For example, if a board member's family owns a company "
                            "that is bidding for a contract with the corporation, "
                            "that director has a conflict. "
                            "Good governance requires that conflicts be declared openly "
                            "and that the conflicted person step aside from the decision. "
                            "Failure to manage conflicts of interest can lead to unfair deals, "
                            "financial losses, and a collapse of trust.\n\n"
                            "Disclosure plays a critical role in managing these risks. "
                            "In the context of corporate governance, disclosure means "
                            "making important information available to shareholders and the public. "
                            "Companies must disclose executive compensation, related-party transactions, "
                            "potential conflicts of interest, and any material risks facing the business. "
                            "Without disclosure, shareholders cannot make informed decisions "
                            "about whether the company is being managed in their best interest.\n\n"
                            "When internal controls fail and wrongdoing occurs, "
                            "whistleblowers often become the last line of defense. "
                            "A whistleblower is someone inside the organization "
                            "who reports illegal or unethical behavior to authorities or the public. "
                            "Whistleblowing takes courage because the person often faces "
                            "retaliation from colleagues or superiors. "
                            "Many countries, including Vietnam, have laws that protect whistleblowers "
                            "from being fired or punished for reporting genuine concerns. "
                            "Companies with strong governance encourage whistleblowing "
                            "by creating anonymous reporting channels and promising protection.\n\n"
                            "Another important governance topic is executive remuneration. "
                            "Remuneration refers to the total compensation that senior leaders receive — "
                            "salary, bonuses, stock options, and other benefits. "
                            "A remuneration committee, usually made up of independent directors, "
                            "decides how much the CEO and other executives should be paid. "
                            "The goal is to set compensation that attracts talented leaders "
                            "while aligning their interests with those of shareholders. "
                            "If executives are paid too much regardless of performance, "
                            "shareholders lose trust in the governance system.\n\n"
                            "Finally, every well-governed company plans for succession. "
                            "Succession planning is the process of identifying and preparing "
                            "future leaders to take over key positions. "
                            "When a CEO retires, falls ill, or is removed, "
                            "the company needs a qualified replacement ready to step in. "
                            "Without a succession plan, a leadership vacuum can cause "
                            "confusion, falling stock prices, and loss of confidence among investors. "
                            "The best boards begin succession planning years in advance, "
                            "grooming internal candidates and maintaining a list of potential external hires."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Đạo đức, tố giác và kế nhiệm",
                    "description": "Viết câu sử dụng 6 từ vựng về đạo đức kinh doanh và kế hoạch kế nhiệm.",
                    "data": {
                        "vocabList": ["whistleblower", "ethics", "conflict", "disclosure", "remuneration", "succession"],
                        "items": [
                            {
                                "targetVocab": "whistleblower",
                                "prompt": "Dùng từ 'whistleblower' để viết một câu về vai trò của người tố giác trong việc phát hiện gian lận doanh nghiệp. Ví dụ: The whistleblower, a mid-level accountant, provided regulators with evidence that the company had been inflating its revenue figures by recording fake sales transactions."
                            },
                            {
                                "targetVocab": "ethics",
                                "prompt": "Dùng từ 'ethics' để viết một câu về bộ quy tắc đạo đức của doanh nghiệp và cách nó hướng dẫn hành vi nhân viên. Ví dụ: The company's code of ethics requires all employees to report any suspicious financial activity to the compliance department within twenty-four hours."
                            },
                            {
                                "targetVocab": "conflict",
                                "prompt": "Dùng từ 'conflict' để viết một câu về xung đột lợi ích trong hội đồng quản trị. Ví dụ: The board member disclosed a conflict of interest when the company considered purchasing office space from a real estate firm owned by his brother."
                            },
                            {
                                "targetVocab": "disclosure",
                                "prompt": "Dùng từ 'disclosure' để viết một câu về nghĩa vụ công bố thông tin quản trị doanh nghiệp. Ví dụ: The annual governance report included full disclosure of each director's other business interests, ensuring that shareholders could identify any potential conflicts."
                            },
                            {
                                "targetVocab": "remuneration",
                                "prompt": "Dùng từ 'remuneration' để viết một câu về thù lao lãnh đạo và cách nó được quyết định. Ví dụ: The remuneration committee tied the CEO's bonus to three specific performance metrics: revenue growth, customer satisfaction, and employee retention rate."
                            },
                            {
                                "targetVocab": "succession",
                                "prompt": "Dùng từ 'succession' để viết một câu về kế hoạch kế nhiệm lãnh đạo trong doanh nghiệp. Ví dụ: The board's succession plan identified the current chief operating officer as the top internal candidate to replace the CEO when she retires in two years."
                            }
                        ]
                    }
                }
            ]
        },
        # ── SESSION 4: Review (all 18 words) ─────────────────
        {
            "title": "Ôn tập",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu ôn tập",
                    "description": "Chúc mừng bạn đã học xong 18 từ vựng! Cùng ôn lại trước khi đọc bài tổng hợp.",
                    "data": {
                        "text": (
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Quản trị doanh nghiệp. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "governance — quản trị, board — hội đồng, director — thành viên hội đồng quản trị, "
                            "fiduciary — ủy thác, accountability — trách nhiệm giải trình, và transparency — minh bạch. "
                            "Đây là bộ từ vựng cốt lõi về cấu trúc quyền lực trong doanh nghiệp.\n\n"
                            "Trong phần 2, bạn đã đi sâu vào quyền cổ đông và cơ chế giám sát: "
                            "stakeholder — bên liên quan, shareholder — cổ đông, proxy — ủy quyền, "
                            "charter — điều lệ, bylaw — nội quy, và oversight — giám sát. "
                            "Những từ này giúp bạn hiểu ai có quyền gì và ai giám sát ai.\n\n"
                            "Trong phần 3, bạn đã khám phá: "
                            "whistleblower — người tố giác, ethics — đạo đức, conflict — xung đột, "
                            "disclosure — công bố thông tin, remuneration — thù lao, và succession — kế nhiệm. "
                            "Đây là những từ về đạo đức kinh doanh, minh bạch và tương lai lãnh đạo.\n\n"
                            "Bây giờ, phần ôn tập này sẽ giúp bạn củng cố toàn bộ 18 từ vựng. "
                            "Bạn sẽ xem lại flashcard, luyện phát âm, và viết câu với tất cả các từ. "
                            "Sau phần ôn tập, bạn sẽ sẵn sàng cho bài đọc tổng hợp — "
                            "một bài viết dài hơn sử dụng cả 18 từ trong một ngữ cảnh liền mạch. "
                            "Hãy bắt đầu nào!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: governance, board, director, fiduciary, accountability, transparency, stakeholder, shareholder, proxy, charter, bylaw, oversight, whistleblower, ethics, conflict, disclosure, remuneration, succession",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: governance, board, director, fiduciary, accountability, transparency, stakeholder, shareholder, proxy, charter, bylaw, oversight, whistleblower, ethics, conflict, disclosure, remuneration, succession",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: governance, board, director, fiduciary, accountability, transparency, stakeholder, shareholder, proxy, charter, bylaw, oversight, whistleblower, ethics, conflict, disclosure, remuneration, succession",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: governance, board, director, fiduciary, accountability, transparency, stakeholder, shareholder, proxy, charter, bylaw, oversight, whistleblower, ethics, conflict, disclosure, remuneration, succession",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: governance, board, director, fiduciary, accountability, transparency, stakeholder, shareholder, proxy, charter, bylaw, oversight, whistleblower, ethics, conflict, disclosure, remuneration, succession",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng quản trị doanh nghiệp",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "items": [
                            {
                                "targetVocab": "governance",
                                "prompt": "Dùng từ 'governance' để viết một câu về cách cải cách quản trị giúp doanh nghiệp phục hồi niềm tin sau bê bối. Ví dụ: After the accounting scandal, the company hired an international consulting firm to redesign its corporate governance framework from the ground up."
                            },
                            {
                                "targetVocab": "board",
                                "prompt": "Dùng từ 'board' để viết một câu về quyết định quan trọng của hội đồng quản trị ảnh hưởng đến chiến lược doanh nghiệp. Ví dụ: The board approved a five-year expansion plan that would double the company's manufacturing capacity in Southeast Asia."
                            },
                            {
                                "targetVocab": "director",
                                "prompt": "Dùng từ 'director' để viết một câu về trách nhiệm của thành viên hội đồng quản trị trong việc bảo vệ lợi ích cổ đông. Ví dụ: The lead independent director called an emergency meeting after discovering that the CEO had signed a major contract without board approval."
                            },
                            {
                                "targetVocab": "fiduciary",
                                "prompt": "Dùng từ 'fiduciary' để viết một câu về hậu quả khi vi phạm nghĩa vụ ủy thác. Ví dụ: The court ordered the former director to pay damages of ten billion dong for breaching his fiduciary duty by steering a lucrative contract to his own private company."
                            },
                            {
                                "targetVocab": "accountability",
                                "prompt": "Dùng từ 'accountability' để viết một câu về cơ chế giải trình giữa ban điều hành và hội đồng quản trị. Ví dụ: The new governance policy requires monthly accountability reports from every department head, which are then reviewed by the board's audit committee."
                            },
                            {
                                "targetVocab": "transparency",
                                "prompt": "Dùng từ 'transparency' để viết một câu về cách minh bạch giúp thu hút nhà đầu tư nước ngoài. Ví dụ: Foreign investors cited the company's exceptional transparency as the main reason they chose to invest, noting that its annual reports were among the most detailed in the industry."
                            },
                            {
                                "targetVocab": "stakeholder",
                                "prompt": "Dùng từ 'stakeholder' để viết một câu về cách doanh nghiệp cân bằng lợi ích của nhiều bên liên quan. Ví dụ: The CEO acknowledged that the factory closure would affect multiple stakeholders, including two thousand employees, dozens of local suppliers, and the surrounding community."
                            },
                            {
                                "targetVocab": "shareholder",
                                "prompt": "Dùng từ 'shareholder' để viết một câu về quyền của cổ đông trong việc thay đổi ban lãnh đạo. Ví dụ: A group of minority shareholders filed a petition demanding the removal of three board members who they believed had failed to protect the company from financial losses."
                            },
                            {
                                "targetVocab": "proxy",
                                "prompt": "Dùng từ 'proxy' để viết một câu về cuộc chiến ủy quyền giữa các nhóm cổ đông. Ví dụ: The activist investor launched a proxy fight, sending letters to all shareholders urging them to vote against the current board's reelection at the upcoming annual meeting."
                            },
                            {
                                "targetVocab": "charter",
                                "prompt": "Dùng từ 'charter' để viết một câu về việc sửa đổi điều lệ doanh nghiệp. Ví dụ: Shareholders voted to amend the company's charter to require that the positions of chairman and CEO be held by two different people, preventing excessive concentration of power."
                            },
                            {
                                "targetVocab": "bylaw",
                                "prompt": "Dùng từ 'bylaw' để viết một câu về nội quy doanh nghiệp liên quan đến quy trình bầu cử hội đồng quản trị. Ví dụ: The company updated its bylaws to allow shareholders to nominate director candidates directly, rather than relying solely on the nomination committee's recommendations."
                            },
                            {
                                "targetVocab": "oversight",
                                "prompt": "Dùng từ 'oversight' để viết một câu về hậu quả khi thiếu giám sát trong doanh nghiệp. Ví dụ: The lack of proper oversight allowed the finance department to manipulate quarterly earnings reports for three consecutive years before an external auditor finally discovered the irregularities."
                            },
                            {
                                "targetVocab": "whistleblower",
                                "prompt": "Dùng từ 'whistleblower' để viết một câu về cơ chế bảo vệ người tố giác trong doanh nghiệp. Ví dụ: The company established a confidential whistleblower hotline so that employees could report concerns about fraud or misconduct without fear of retaliation from their managers."
                            },
                            {
                                "targetVocab": "ethics",
                                "prompt": "Dùng từ 'ethics' để viết một câu về chương trình đào tạo đạo đức kinh doanh cho nhân viên. Ví dụ: All new employees must complete a mandatory ethics training program that covers topics such as bribery prevention, data privacy, and responsible use of company resources."
                            },
                            {
                                "targetVocab": "conflict",
                                "prompt": "Dùng từ 'conflict' để viết một câu về cách xử lý xung đột lợi ích trong quyết định kinh doanh. Ví dụ: The governance manual requires any director with a potential conflict of interest to declare it in writing and abstain from voting on the related matter."
                            },
                            {
                                "targetVocab": "disclosure",
                                "prompt": "Dùng từ 'disclosure' để viết một câu về yêu cầu công bố thông tin thù lao lãnh đạo. Ví dụ: The securities regulator now requires public companies to include detailed disclosure of all executive compensation packages in their annual governance reports."
                            },
                            {
                                "targetVocab": "remuneration",
                                "prompt": "Dùng từ 'remuneration' để viết một câu về mối liên hệ giữa thù lao lãnh đạo và hiệu quả kinh doanh. Ví dụ: The remuneration committee reduced the CEO's bonus by forty percent after the company missed its annual profit target for the second consecutive year."
                            },
                            {
                                "targetVocab": "succession",
                                "prompt": "Dùng từ 'succession' để viết một câu về tầm quan trọng của kế hoạch kế nhiệm đối với sự ổn định doanh nghiệp. Ví dụ: The sudden resignation of the CEO exposed the company's lack of a succession plan, causing the stock price to drop fifteen percent in a single trading session."
                            }
                        ]
                    }
                }
            ]
        },
        # ── SESSION 5: Full reading + farewell ────────────────
        {
            "title": "Đọc toàn bài",
            "activities": [
                {
                    "activityType": "introAudio",
                    "title": "Giới thiệu bài đọc tổng hợp",
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về quản trị doanh nghiệp.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về quản trị doanh nghiệp — từ cấu trúc hội đồng quản trị, "
                            "quyền cổ đông, đến đạo đức kinh doanh và kế hoạch kế nhiệm.\n\n"
                            "Bạn sẽ gặp lại governance, board, director, fiduciary, accountability, transparency "
                            "trong phần mở đầu về nền tảng của hệ thống quản trị. "
                            "Tiếp theo, stakeholder, shareholder, proxy, charter, bylaw, oversight "
                            "sẽ giúp bạn hiểu cơ chế quyền lực và giám sát. "
                            "Và cuối cùng, whistleblower, ethics, conflict, disclosure, remuneration, succession "
                            "sẽ đưa bạn vào thế giới đạo đức và tương lai lãnh đạo doanh nghiệp.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Quản trị doanh nghiệp — Bức tranh toàn cảnh",
                    "description": "Imagine you are a financial analyst preparing a governance assessment of a large Vietnamese corporation that recently applied to list its shares on an international stock exchange.",
                    "data": {
                        "text": (
                            "Imagine you are a financial analyst preparing a governance assessment "
                            "of a large Vietnamese corporation that recently applied to list its shares "
                            "on an international stock exchange. "
                            "International investors will not buy shares in a company "
                            "unless they are confident that its governance meets global standards. "
                            "Your job is to evaluate every aspect of how this company is governed.\n\n"
                            "You begin with the company's governance framework. "
                            "Governance is the system of rules, practices, and processes "
                            "by which a company is directed and controlled. "
                            "A strong governance framework protects investors, "
                            "ensures accountability, and builds long-term trust. "
                            "You review the company's charter — the founding document "
                            "that establishes its legal structure, defines the types of shares it can issue, "
                            "and sets the basic rules for how it operates. "
                            "The charter looks solid: it limits the board to eleven members "
                            "and requires that at least four must be independent.\n\n"
                            "Next, you examine the bylaws. "
                            "The bylaws provide the detailed operational rules — "
                            "how often the board must meet, how votes are conducted, "
                            "how new directors are nominated, and how conflicts of interest are managed. "
                            "You note that the bylaws require the board to meet at least six times per year "
                            "and that any director who misses more than two consecutive meetings "
                            "must explain the absence in writing.\n\n"
                            "You then look at the board of directors itself. "
                            "The board has eleven members: four executive directors "
                            "who also hold management positions, three independent directors "
                            "with no ties to the company, and four non-executive directors "
                            "who represent major shareholders. "
                            "Each director has a fiduciary duty to act in the best interests "
                            "of the company and its shareholders — not in their own personal interest. "
                            "You check whether any director has a known conflict of interest. "
                            "One director's spouse owns a logistics company "
                            "that provides services to the corporation. "
                            "The conflict has been properly disclosed, "
                            "and the director abstains from any vote related to logistics contracts.\n\n"
                            "Transparency is a key area of your assessment. "
                            "You review the company's annual report and find detailed disclosure "
                            "of executive remuneration, related-party transactions, "
                            "and the board's decision-making process. "
                            "The remuneration report shows that the CEO's total compensation "
                            "includes a base salary, a performance bonus tied to revenue growth, "
                            "and stock options that vest over three years. "
                            "The remuneration committee, made up entirely of independent directors, "
                            "approved the package after benchmarking it against similar companies in the region.\n\n"
                            "You also assess how the company treats its stakeholders. "
                            "A stakeholder is anyone affected by the company's operations — "
                            "not just shareholders, but also employees, customers, suppliers, "
                            "and the communities where the company operates. "
                            "The company publishes an annual sustainability report "
                            "that addresses environmental impact, labor practices, "
                            "and community investment. "
                            "This suggests that management takes a broad view of its responsibilities, "
                            "not just a narrow focus on shareholder returns.\n\n"
                            "Shareholder rights are another critical area. "
                            "You verify that shareholders can vote on all major decisions — "
                            "electing directors, approving mergers, and amending the charter. "
                            "The company also offers proxy voting, "
                            "allowing shareholders who cannot attend the annual meeting "
                            "to submit their votes in advance. "
                            "Last year, over forty percent of votes were cast by proxy, "
                            "indicating strong engagement from investors who are not physically present.\n\n"
                            "Oversight mechanisms are well established. "
                            "The board has three specialized committees: "
                            "an audit committee that oversees financial reporting, "
                            "a remuneration committee that sets executive pay, "
                            "and a nomination committee that identifies candidates for the board. "
                            "Each committee is chaired by an independent director, "
                            "providing a layer of oversight that separates decision-making from self-interest.\n\n"
                            "You check the company's ethics program. "
                            "The code of ethics covers bribery prevention, data privacy, "
                            "fair competition, and responsible sourcing. "
                            "All employees receive annual ethics training, "
                            "and the company has a confidential whistleblower hotline. "
                            "Last year, a whistleblower reported that a regional sales manager "
                            "had been accepting kickbacks from a supplier. "
                            "The company investigated, terminated the manager, "
                            "and reported the incident to regulators — "
                            "a sign that the whistleblower system actually works.\n\n"
                            "Finally, you review the company's succession plan. "
                            "Succession planning ensures that the company is prepared "
                            "for leadership transitions. "
                            "The board has identified two internal candidates "
                            "who could replace the current CEO if needed. "
                            "Both candidates have been given expanded responsibilities "
                            "to prepare them for the top role. "
                            "The existence of a clear succession plan reassures investors "
                            "that the company will not face a leadership crisis "
                            "if the CEO departs unexpectedly.\n\n"
                            "After completing your assessment, you conclude that the company's "
                            "governance meets international standards. "
                            "Its charter and bylaws are well drafted. "
                            "Its board includes a healthy mix of independent and executive directors. "
                            "Accountability and transparency are embedded in its reporting practices. "
                            "Stakeholder interests are considered alongside shareholder returns. "
                            "And its ethics program, whistleblower protections, "
                            "and succession planning demonstrate a commitment "
                            "to long-term responsible management. "
                            "This is what good corporate governance looks like — "
                            "not just rules on paper, but a living system "
                            "that earns the trust of everyone it touches."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Quản trị doanh nghiệp — Bức tranh toàn cảnh",
                    "description": "Imagine you are a financial analyst preparing a governance assessment of a large Vietnamese corporation that recently applied to list its shares on an international stock exchange.",
                    "data": {
                        "text": (
                            "Imagine you are a financial analyst preparing a governance assessment "
                            "of a large Vietnamese corporation that recently applied to list its shares "
                            "on an international stock exchange. "
                            "International investors will not buy shares in a company "
                            "unless they are confident that its governance meets global standards. "
                            "Your job is to evaluate every aspect of how this company is governed.\n\n"
                            "You begin with the company's governance framework. "
                            "Governance is the system of rules, practices, and processes "
                            "by which a company is directed and controlled. "
                            "A strong governance framework protects investors, "
                            "ensures accountability, and builds long-term trust. "
                            "You review the company's charter — the founding document "
                            "that establishes its legal structure, defines the types of shares it can issue, "
                            "and sets the basic rules for how it operates. "
                            "The charter looks solid: it limits the board to eleven members "
                            "and requires that at least four must be independent.\n\n"
                            "Next, you examine the bylaws. "
                            "The bylaws provide the detailed operational rules — "
                            "how often the board must meet, how votes are conducted, "
                            "how new directors are nominated, and how conflicts of interest are managed. "
                            "You note that the bylaws require the board to meet at least six times per year "
                            "and that any director who misses more than two consecutive meetings "
                            "must explain the absence in writing.\n\n"
                            "You then look at the board of directors itself. "
                            "The board has eleven members: four executive directors "
                            "who also hold management positions, three independent directors "
                            "with no ties to the company, and four non-executive directors "
                            "who represent major shareholders. "
                            "Each director has a fiduciary duty to act in the best interests "
                            "of the company and its shareholders — not in their own personal interest. "
                            "You check whether any director has a known conflict of interest. "
                            "One director's spouse owns a logistics company "
                            "that provides services to the corporation. "
                            "The conflict has been properly disclosed, "
                            "and the director abstains from any vote related to logistics contracts.\n\n"
                            "Transparency is a key area of your assessment. "
                            "You review the company's annual report and find detailed disclosure "
                            "of executive remuneration, related-party transactions, "
                            "and the board's decision-making process. "
                            "The remuneration report shows that the CEO's total compensation "
                            "includes a base salary, a performance bonus tied to revenue growth, "
                            "and stock options that vest over three years. "
                            "The remuneration committee, made up entirely of independent directors, "
                            "approved the package after benchmarking it against similar companies in the region.\n\n"
                            "You also assess how the company treats its stakeholders. "
                            "A stakeholder is anyone affected by the company's operations — "
                            "not just shareholders, but also employees, customers, suppliers, "
                            "and the communities where the company operates. "
                            "The company publishes an annual sustainability report "
                            "that addresses environmental impact, labor practices, "
                            "and community investment. "
                            "This suggests that management takes a broad view of its responsibilities, "
                            "not just a narrow focus on shareholder returns.\n\n"
                            "Shareholder rights are another critical area. "
                            "You verify that shareholders can vote on all major decisions — "
                            "electing directors, approving mergers, and amending the charter. "
                            "The company also offers proxy voting, "
                            "allowing shareholders who cannot attend the annual meeting "
                            "to submit their votes in advance. "
                            "Last year, over forty percent of votes were cast by proxy, "
                            "indicating strong engagement from investors who are not physically present.\n\n"
                            "Oversight mechanisms are well established. "
                            "The board has three specialized committees: "
                            "an audit committee that oversees financial reporting, "
                            "a remuneration committee that sets executive pay, "
                            "and a nomination committee that identifies candidates for the board. "
                            "Each committee is chaired by an independent director, "
                            "providing a layer of oversight that separates decision-making from self-interest.\n\n"
                            "You check the company's ethics program. "
                            "The code of ethics covers bribery prevention, data privacy, "
                            "fair competition, and responsible sourcing. "
                            "All employees receive annual ethics training, "
                            "and the company has a confidential whistleblower hotline. "
                            "Last year, a whistleblower reported that a regional sales manager "
                            "had been accepting kickbacks from a supplier. "
                            "The company investigated, terminated the manager, "
                            "and reported the incident to regulators — "
                            "a sign that the whistleblower system actually works.\n\n"
                            "Finally, you review the company's succession plan. "
                            "Succession planning ensures that the company is prepared "
                            "for leadership transitions. "
                            "The board has identified two internal candidates "
                            "who could replace the current CEO if needed. "
                            "Both candidates have been given expanded responsibilities "
                            "to prepare them for the top role. "
                            "The existence of a clear succession plan reassures investors "
                            "that the company will not face a leadership crisis "
                            "if the CEO departs unexpectedly.\n\n"
                            "After completing your assessment, you conclude that the company's "
                            "governance meets international standards. "
                            "Its charter and bylaws are well drafted. "
                            "Its board includes a healthy mix of independent and executive directors. "
                            "Accountability and transparency are embedded in its reporting practices. "
                            "Stakeholder interests are considered alongside shareholder returns. "
                            "And its ethics program, whistleblower protections, "
                            "and succession planning demonstrate a commitment "
                            "to long-term responsible management. "
                            "This is what good corporate governance looks like — "
                            "not just rules on paper, but a living system "
                            "that earns the trust of everyone it touches."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Quản trị doanh nghiệp — Bức tranh toàn cảnh",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Imagine you are a financial analyst preparing a governance assessment "
                            "of a large Vietnamese corporation that recently applied to list its shares "
                            "on an international stock exchange. "
                            "International investors will not buy shares in a company "
                            "unless they are confident that its governance meets global standards. "
                            "Your job is to evaluate every aspect of how this company is governed.\n\n"
                            "You begin with the company's governance framework. "
                            "Governance is the system of rules, practices, and processes "
                            "by which a company is directed and controlled. "
                            "A strong governance framework protects investors, "
                            "ensures accountability, and builds long-term trust. "
                            "You review the company's charter — the founding document "
                            "that establishes its legal structure, defines the types of shares it can issue, "
                            "and sets the basic rules for how it operates. "
                            "The charter looks solid: it limits the board to eleven members "
                            "and requires that at least four must be independent.\n\n"
                            "Next, you examine the bylaws. "
                            "The bylaws provide the detailed operational rules — "
                            "how often the board must meet, how votes are conducted, "
                            "how new directors are nominated, and how conflicts of interest are managed. "
                            "You note that the bylaws require the board to meet at least six times per year "
                            "and that any director who misses more than two consecutive meetings "
                            "must explain the absence in writing.\n\n"
                            "You then look at the board of directors itself. "
                            "The board has eleven members: four executive directors "
                            "who also hold management positions, three independent directors "
                            "with no ties to the company, and four non-executive directors "
                            "who represent major shareholders. "
                            "Each director has a fiduciary duty to act in the best interests "
                            "of the company and its shareholders — not in their own personal interest. "
                            "You check whether any director has a known conflict of interest. "
                            "One director's spouse owns a logistics company "
                            "that provides services to the corporation. "
                            "The conflict has been properly disclosed, "
                            "and the director abstains from any vote related to logistics contracts.\n\n"
                            "Transparency is a key area of your assessment. "
                            "You review the company's annual report and find detailed disclosure "
                            "of executive remuneration, related-party transactions, "
                            "and the board's decision-making process. "
                            "The remuneration report shows that the CEO's total compensation "
                            "includes a base salary, a performance bonus tied to revenue growth, "
                            "and stock options that vest over three years. "
                            "The remuneration committee, made up entirely of independent directors, "
                            "approved the package after benchmarking it against similar companies in the region.\n\n"
                            "You also assess how the company treats its stakeholders. "
                            "A stakeholder is anyone affected by the company's operations — "
                            "not just shareholders, but also employees, customers, suppliers, "
                            "and the communities where the company operates. "
                            "The company publishes an annual sustainability report "
                            "that addresses environmental impact, labor practices, "
                            "and community investment. "
                            "This suggests that management takes a broad view of its responsibilities, "
                            "not just a narrow focus on shareholder returns.\n\n"
                            "Shareholder rights are another critical area. "
                            "You verify that shareholders can vote on all major decisions — "
                            "electing directors, approving mergers, and amending the charter. "
                            "The company also offers proxy voting, "
                            "allowing shareholders who cannot attend the annual meeting "
                            "to submit their votes in advance. "
                            "Last year, over forty percent of votes were cast by proxy, "
                            "indicating strong engagement from investors who are not physically present.\n\n"
                            "Oversight mechanisms are well established. "
                            "The board has three specialized committees: "
                            "an audit committee that oversees financial reporting, "
                            "a remuneration committee that sets executive pay, "
                            "and a nomination committee that identifies candidates for the board. "
                            "Each committee is chaired by an independent director, "
                            "providing a layer of oversight that separates decision-making from self-interest.\n\n"
                            "You check the company's ethics program. "
                            "The code of ethics covers bribery prevention, data privacy, "
                            "fair competition, and responsible sourcing. "
                            "All employees receive annual ethics training, "
                            "and the company has a confidential whistleblower hotline. "
                            "Last year, a whistleblower reported that a regional sales manager "
                            "had been accepting kickbacks from a supplier. "
                            "The company investigated, terminated the manager, "
                            "and reported the incident to regulators — "
                            "a sign that the whistleblower system actually works.\n\n"
                            "Finally, you review the company's succession plan. "
                            "Succession planning ensures that the company is prepared "
                            "for leadership transitions. "
                            "The board has identified two internal candidates "
                            "who could replace the current CEO if needed. "
                            "Both candidates have been given expanded responsibilities "
                            "to prepare them for the top role. "
                            "The existence of a clear succession plan reassures investors "
                            "that the company will not face a leadership crisis "
                            "if the CEO departs unexpectedly.\n\n"
                            "After completing your assessment, you conclude that the company's "
                            "governance meets international standards. "
                            "Its charter and bylaws are well drafted. "
                            "Its board includes a healthy mix of independent and executive directors. "
                            "Accountability and transparency are embedded in its reporting practices. "
                            "Stakeholder interests are considered alongside shareholder returns. "
                            "And its ethics program, whistleblower protections, "
                            "and succession planning demonstrate a commitment "
                            "to long-term responsible management. "
                            "This is what good corporate governance looks like — "
                            "not just rules on paper, but a living system "
                            "that earns the trust of everyone it touches."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích quản trị doanh nghiệp",
                    "description": "Viết đoạn văn tiếng Anh phân tích quản trị doanh nghiệp sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một khía cạnh của quản trị doanh nghiệp. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy phân tích vai trò của hội đồng quản trị trong việc đảm bảo quản trị tốt. Giải thích cách board và director thực hiện fiduciary duty, tầm quan trọng của accountability và transparency, và cách oversight ngăn chặn lạm dụng quyền lực.",
                            "Hãy giải thích vì sao đạo đức kinh doanh và cơ chế tố giác quan trọng đối với quản trị doanh nghiệp. Phân tích vai trò của ethics và whistleblower trong việc phát hiện conflict of interest, tầm quan trọng của disclosure về remuneration, và cách succession planning đảm bảo sự ổn định lãnh đạo."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay với tinh thần chiêm nghiệm.",
                    "data": {
                        "text": (
                            "Bạn vừa hoàn thành bài học về Quản trị doanh nghiệp — "
                            "bài cuối cùng trong chuỗi Kế toán và Tài chính doanh nghiệp. "
                            "Hãy dừng lại một chút và tự hỏi: "
                            "điều gì thực sự giữ cho một tổ chức đi đúng hướng? "
                            "Không phải lợi nhuận. Không phải công nghệ. "
                            "Mà là cách con người đối xử với quyền lực và trách nhiệm.\n\n"
                            "Fiduciary — nghĩa vụ ủy thác. Đây là từ mà bạn nên ghi nhớ sâu nhất. "
                            "Fiduciary duty không chỉ là khái niệm pháp lý — "
                            "nó là lời hứa rằng người được giao quyền sẽ dùng quyền đó "
                            "vì lợi ích của người khác, không phải của chính mình. "
                            "Hãy nghĩ xem: trong cuộc sống, bạn cũng đang giữ fiduciary duty "
                            "với gia đình, với đồng nghiệp, với cộng đồng. "
                            "Ví dụ mới: The pension fund manager has a fiduciary duty "
                            "to invest the retirement savings of three million workers wisely, "
                            "because every decision she makes affects their future security.\n\n"
                            "Accountability — trách nhiệm giải trình. "
                            "Trong một thế giới mà quyền lực dễ bị lạm dụng, "
                            "accountability là sợi dây giữ mọi người trung thực. "
                            "Không ai nên có quyền mà không phải giải trình. "
                            "Ví dụ mới: The new regulation requires all state-owned enterprises "
                            "to publish quarterly accountability reports detailing how public funds "
                            "were spent and what results were achieved.\n\n"
                            "Whistleblower — người tố giác. "
                            "Đây có lẽ là từ mang nhiều cảm xúc nhất trong bài học hôm nay. "
                            "Whistleblower là người dám nói sự thật khi mọi người xung quanh im lặng. "
                            "Họ chấp nhận rủi ro cá nhân để bảo vệ lợi ích chung. "
                            "Hãy tự hỏi: nếu bạn phát hiện gian lận ở nơi làm việc, "
                            "bạn có đủ dũng cảm để lên tiếng không? "
                            "Ví dụ mới: The whistleblower who exposed the bank's fraudulent lending practices "
                            "was initially ostracized by colleagues but was later recognized "
                            "by the government for protecting thousands of depositors from financial harm.\n\n"
                            "Ethics — đạo đức. Đạo đức không phải là bộ quy tắc treo trên tường — "
                            "nó là la bàn bên trong mỗi người, hướng dẫn bạn khi không ai nhìn thấy. "
                            "Một doanh nghiệp có thể có hàng trăm trang nội quy, "
                            "nhưng nếu văn hóa đạo đức yếu, những trang giấy đó vô nghĩa. "
                            "Ví dụ mới: The company's strong ethics culture was tested "
                            "when a major client offered a bribe to speed up delivery — "
                            "the sales team refused unanimously, knowing that short-term gain "
                            "was not worth long-term reputational damage.\n\n"
                            "Succession — kế nhiệm. Mọi nhà lãnh đạo đều sẽ rời đi — "
                            "câu hỏi là liệu tổ chức có sẵn sàng cho ngày đó không. "
                            "Succession planning không chỉ là chọn người thay thế — "
                            "nó là cách một tổ chức nói rằng: 'Chúng tôi nghĩ về tương lai, "
                            "không chỉ về hôm nay.' "
                            "Ví dụ mới: The founder spent her final three years as CEO "
                            "mentoring two senior vice presidents as part of the succession plan, "
                            "ensuring that the company's values and vision would survive her departure.\n\n"
                            "Disclosure — công bố thông tin. Minh bạch không phải là điểm yếu — "
                            "nó là sức mạnh. Khi một doanh nghiệp dám công bố mọi thứ, "
                            "từ thù lao lãnh đạo đến xung đột lợi ích, "
                            "nó đang nói với thế giới: 'Chúng tôi không có gì phải giấu.' "
                            "Ví dụ mới: The company's voluntary disclosure of its carbon emissions "
                            "and supply chain labor practices earned it a top governance rating "
                            "from three international sustainability agencies.\n\n"
                            "Bạn biết không, quản trị doanh nghiệp không chỉ là chuyện của phòng họp — "
                            "nó là câu chuyện về cách con người tổ chức quyền lực, "
                            "cách chúng ta xây dựng niềm tin, và cách chúng ta bảo vệ lẫn nhau "
                            "khỏi sự lạm dụng. Mỗi từ vựng bạn học hôm nay — "
                            "từ governance đến succession — là một mảnh ghép "
                            "trong bức tranh lớn hơn về cách thế giới kinh doanh vận hành.\n\n"
                            "Hãy mang theo 18 từ vựng này không chỉ vào phòng thi, "
                            "mà vào cách bạn nhìn nhận mọi tổ chức xung quanh mình. "
                            "Lần tới khi bạn đọc tin về một vụ bê bối doanh nghiệp, "
                            "bạn sẽ hiểu không chỉ chuyện gì đã xảy ra, "
                            "mà còn vì sao nó xảy ra — và cơ chế nào đã thất bại. "
                            "Đó là sức mạnh thực sự của kiến thức.\n\n"
                            "Chúc bạn tiếp tục hành trình khám phá — "
                            "hẹn gặp lại ở những bài học tiếp theo."
                        )
                    }
                }
            ]
        }
    ]
}

# ── Validate before upload ───────────────────────────────────
print("Validating content...")
validate_all(content)
print("Validation passed!")

# ── Upload ───────────────────────────────────────────────────
token = get_firebase_id_token(UID)
res = requests.post(
    f"{API_BASE}/curriculum/create",
    json={
        "firebaseIdToken": token,
        "language": "en",
        "userLanguage": "vi",
        "content": json.dumps(content),
    },
)
res.raise_for_status()
curriculum_id = res.json()["id"]
print(f"Created curriculum: {curriculum_id}")
print(f"Title: {content['title']}")

# ── Duplicate check SQL ──────────────────────────────────────
print("\n-- Duplicate check SQL (run manually): --")
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Corporate Governance – Quản Trị Doanh Nghiệp' AND uid = '{UID}' ORDER BY created_at;")
