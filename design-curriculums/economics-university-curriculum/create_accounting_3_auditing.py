"""
Create curriculum: Auditing – Kiểm Toán
Series D — Kế Toán & Tài Chính Doanh Nghiệp (Accounting & Corporate Finance), curriculum #3
18 words | 5 sessions | provocative_question tone | warm accountability farewell
displayOrder 2
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
W1 = ["audit", "compliance", "assurance", "material", "misstatement", "opinion"]
W2 = ["internal", "external", "sampling", "evidence", "procedure", "engagement"]
W3 = ["fraud", "detection", "disclosure", "independence", "objectivity", "skepticism"]
ALL_WORDS = W1 + W2 + W3

# ── Content ──────────────────────────────────────────────────
content = {
    "title": "Auditing – Kiểm Toán",
    "contentTypeTags": [],
    "description": (
        "BẠN CÓ BIẾT AI LÀ NGƯỜI CUỐI CÙNG ĐỨNG GIỮA MỘT BÁO CÁO TÀI CHÍNH VÀ SỰ THẬT KHÔNG?\n\n"
        "Mỗi năm, hàng nghìn doanh nghiệp Việt Nam phải mời kiểm toán viên độc lập đến xem xét sổ sách. "
        "Bạn đọc báo cáo tài chính và thấy dòng chữ 'unqualified opinion' — nhưng bạn có hiểu "
        "nó nghĩa là gì không? Bạn nghe giảng viên nói về 'material misstatement' — "
        "nhưng bạn có biết tại sao một sai sót nhỏ có thể khiến cả báo cáo bị bác bỏ?\n\n"
        "Kiểm toán không phải là đếm tiền — nó là nghệ thuật tìm ra sự thật "
        "trong một biển dữ liệu tài chính. Hãy nghĩ về kiểm toán viên như thám tử tài chính: "
        "họ thu thập evidence, đánh giá procedure, kiểm tra sampling, "
        "và cuối cùng đưa ra opinion — ý kiến chuyên môn có sức nặng pháp lý.\n\n"
        "Sau khóa học, bạn sẽ đọc được báo cáo kiểm toán tiếng Anh mà không cần tra từ điển, "
        "hiểu sự khác biệt giữa internal audit và external audit, "
        "và tự tin thảo luận về fraud detection, auditor independence "
        "trong bài tập nhóm hay phỏng vấn tuyển dụng tại Big Four.\n\n"
        "18 từ vựng — từ audit đến skepticism — được dạy qua bài đọc, flashcard, luyện nói và viết. "
        "Bạn vừa nâng cấp tư duy kiểm toán, vừa nâng trình tiếng Anh chuyên ngành một cách vượt bậc."
    ),
    "preview": {
        "text": (
            "Khám phá 18 từ vựng tiếng Anh cốt lõi về kiểm toán — "
            "ngôn ngữ mà mọi kiểm toán viên trên thế giới sử dụng hàng ngày. "
            "Bạn sẽ học audit, compliance, assurance, material, misstatement, opinion trong phần đầu tiên, "
            "nơi bài đọc giải thích kiểm toán viên làm gì và vì sao ý kiến kiểm toán quan trọng. "
            "Tiếp theo là internal, external, sampling, evidence, procedure, engagement — "
            "những từ giúp bạn hiểu quy trình kiểm toán từ lập kế hoạch đến thu thập bằng chứng. "
            "Cuối cùng, fraud, detection, disclosure, independence, objectivity, skepticism "
            "đưa bạn vào thế giới đạo đức nghề nghiệp và phát hiện gian lận tài chính. "
            "Qua 3 bài đọc tiếng Anh, 1 phần ôn tập toàn diện và 1 bài đọc tổng hợp, "
            "bạn sẽ tự tin đọc hiểu báo cáo kiểm toán bằng tiếng Anh — "
            "sẵn sàng cho kỳ thi, bài tập nhóm, hay buổi phỏng vấn tại công ty kiểm toán."
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
                    "description": "Chào mừng bạn đến với bài học về kiểm toán.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với bài học thứ ba trong chuỗi từ vựng Kế toán và Tài chính doanh nghiệp — "
                            "chủ đề hôm nay là Kiểm toán, hay trong tiếng Anh là Auditing. "
                            "Nếu báo cáo tài chính là câu chuyện mà doanh nghiệp kể về sức khỏe tài chính của mình, "
                            "thì kiểm toán là quá trình xác minh xem câu chuyện đó có đáng tin hay không. "
                            "Mỗi năm, các công ty niêm yết trên sàn chứng khoán Việt Nam đều phải thuê "
                            "kiểm toán viên độc lập để kiểm tra báo cáo tài chính — "
                            "và toàn bộ quy trình đó được thực hiện bằng thuật ngữ kiểm toán quốc tế.\n\n"
                            "Trong phần này, bạn sẽ học 6 từ vựng: audit, compliance, assurance, material, misstatement, và opinion. "
                            "Đây là những từ nền tảng nhất — bạn sẽ gặp chúng trên mọi báo cáo kiểm toán.\n\n"
                            "Từ đầu tiên là audit — danh từ/động từ — nghĩa là kiểm toán, "
                            "quá trình kiểm tra và đánh giá độc lập các báo cáo tài chính của một tổ chức. "
                            "Ví dụ: 'The annual audit of the company's financial records took three weeks "
                            "and involved a team of twelve accountants from one of the Big Four firms.' "
                            "Trong bài đọc, audit là hoạt động trung tâm — "
                            "mọi thứ khác trong bài học đều xoay quanh quá trình này.\n\n"
                            "Từ thứ hai là compliance — danh từ — nghĩa là tuân thủ, "
                            "việc đảm bảo rằng doanh nghiệp hoạt động đúng theo luật pháp và quy định. "
                            "Ví dụ: 'The compliance department reviewed all transactions to ensure "
                            "that the company followed both Vietnamese accounting standards and international regulations.' "
                            "Trong bài đọc, compliance là mục tiêu mà kiểm toán hướng tới — "
                            "kiểm toán viên kiểm tra xem doanh nghiệp có tuân thủ các chuẩn mực hay không.\n\n"
                            "Từ thứ ba là assurance — danh từ — nghĩa là đảm bảo, "
                            "mức độ tin cậy mà kiểm toán viên cung cấp cho người đọc báo cáo tài chính. "
                            "Ví dụ: 'An audit provides reasonable assurance that the financial statements "
                            "are free from material misstatement, but it does not guarantee absolute accuracy.' "
                            "Trong bài đọc, assurance là sản phẩm cuối cùng của kiểm toán — "
                            "không phải sự chắc chắn tuyệt đối, mà là sự đảm bảo hợp lý.\n\n"
                            "Từ thứ tư là material — tính từ — nghĩa là trọng yếu, "
                            "đủ lớn hoặc đủ quan trọng để ảnh hưởng đến quyết định của người đọc báo cáo. "
                            "Ví dụ: 'The auditor determined that the error of five billion dong was material "
                            "because it could change an investor's decision about whether to buy shares in the company.' "
                            "Trong bài đọc, material là ngưỡng quan trọng — "
                            "không phải mọi sai sót đều đáng lo, chỉ những sai sót trọng yếu mới cần báo cáo.\n\n"
                            "Từ thứ năm là misstatement — danh từ — nghĩa là sai sót trên báo cáo, "
                            "thông tin tài chính không chính xác hoặc bị bỏ sót trên báo cáo tài chính. "
                            "Ví dụ: 'The auditors discovered a misstatement in the revenue figures — "
                            "the company had recorded sales of goods that had not yet been delivered to customers.' "
                            "Trong bài đọc, misstatement là thứ mà kiểm toán viên tìm kiếm — "
                            "sai sót có thể do nhầm lẫn hoặc do cố ý gian lận.\n\n"
                            "Từ cuối cùng là opinion — danh từ — nghĩa là ý kiến kiểm toán, "
                            "kết luận chính thức của kiểm toán viên về độ tin cậy của báo cáo tài chính. "
                            "Ví dụ: 'After completing the audit, the firm issued an unqualified opinion, "
                            "meaning the financial statements presented a true and fair view of the company's position.' "
                            "Trong bài đọc, opinion là sản phẩm quan trọng nhất của kiểm toán — "
                            "nó quyết định liệu nhà đầu tư có thể tin vào báo cáo tài chính hay không.\n\n"
                            "Bây giờ bạn đã biết 6 từ vựng đầu tiên. Hãy bắt đầu với flashcard, "
                            "sau đó đọc bài viết về vai trò của kiểm toán và ý kiến kiểm toán nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Kiểm toán và ý kiến kiểm toán",
                    "description": "Học 6 từ: audit, compliance, assurance, material, misstatement, opinion",
                    "data": {"vocabList": ["audit", "compliance", "assurance", "material", "misstatement", "opinion"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Kiểm toán và ý kiến kiểm toán",
                    "description": "Học 6 từ: audit, compliance, assurance, material, misstatement, opinion",
                    "data": {"vocabList": ["audit", "compliance", "assurance", "material", "misstatement", "opinion"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Kiểm toán và ý kiến kiểm toán",
                    "description": "Học 6 từ: audit, compliance, assurance, material, misstatement, opinion",
                    "data": {"vocabList": ["audit", "compliance", "assurance", "material", "misstatement", "opinion"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Kiểm toán và ý kiến kiểm toán",
                    "description": "Học 6 từ: audit, compliance, assurance, material, misstatement, opinion",
                    "data": {"vocabList": ["audit", "compliance", "assurance", "material", "misstatement", "opinion"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Kiểm toán và ý kiến kiểm toán",
                    "description": "Học 6 từ: audit, compliance, assurance, material, misstatement, opinion",
                    "data": {"vocabList": ["audit", "compliance", "assurance", "material", "misstatement", "opinion"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Vai trò của kiểm toán và ý kiến kiểm toán",
                    "description": "When a company publishes its financial statements, how do investors know the numbers are trustworthy?",
                    "data": {
                        "text": (
                            "When a company publishes its financial statements, "
                            "how do investors know the numbers are trustworthy? "
                            "The answer is the audit — an independent examination "
                            "of a company's financial records by a qualified professional.\n\n"
                            "In Vietnam, all publicly listed companies must undergo "
                            "an annual audit conducted by a licensed auditing firm. "
                            "The purpose of the audit is not to find every single error "
                            "in the accounting records. Instead, it provides reasonable assurance "
                            "that the financial statements, taken as a whole, "
                            "are free from material misstatement. "
                            "Reasonable assurance means a high level of confidence, "
                            "but not absolute certainty. "
                            "Auditors cannot check every transaction — "
                            "they use professional judgment to focus on the areas "
                            "that matter most.\n\n"
                            "The concept of materiality is central to every audit. "
                            "A misstatement is considered material if it is large enough "
                            "or important enough to influence the decisions of someone "
                            "reading the financial statements. "
                            "For example, if a company accidentally records an expense "
                            "of fifty thousand dong in the wrong category, "
                            "that error is unlikely to be material — "
                            "it will not change an investor's decision. "
                            "But if the company fails to report a liability "
                            "of ten billion dong, that misstatement is clearly material "
                            "because it hides a significant financial obligation.\n\n"
                            "Compliance is another key focus of the audit. "
                            "Auditors check whether the company has followed "
                            "the applicable accounting standards and legal requirements. "
                            "In Vietnam, companies must comply with Vietnamese Accounting Standards "
                            "and, for some listed firms, International Financial Reporting Standards. "
                            "If the auditor finds that the company has not followed these rules, "
                            "the compliance failure must be reported.\n\n"
                            "At the end of the audit, the auditor issues an opinion — "
                            "a formal conclusion about the reliability of the financial statements. "
                            "The most common type is an unqualified opinion, "
                            "sometimes called a clean opinion. "
                            "This means the auditor believes the statements present "
                            "a true and fair view of the company's financial position. "
                            "A qualified opinion means the statements are mostly accurate "
                            "but contain one or more issues that the auditor wants to highlight. "
                            "An adverse opinion means the statements are materially misstated "
                            "and should not be relied upon. "
                            "A disclaimer of opinion means the auditor could not obtain "
                            "enough evidence to form any conclusion at all.\n\n"
                            "For investors, the auditor's opinion is one of the most important "
                            "pieces of information in an annual report. "
                            "A clean opinion provides assurance that the numbers can be trusted. "
                            "Any other type of opinion is a warning sign "
                            "that something may be wrong with the company's financial reporting."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Vai trò của kiểm toán và ý kiến kiểm toán",
                    "description": "When a company publishes its financial statements, how do investors know the numbers are trustworthy?",
                    "data": {
                        "text": (
                            "When a company publishes its financial statements, "
                            "how do investors know the numbers are trustworthy? "
                            "The answer is the audit — an independent examination "
                            "of a company's financial records by a qualified professional.\n\n"
                            "In Vietnam, all publicly listed companies must undergo "
                            "an annual audit conducted by a licensed auditing firm. "
                            "The purpose of the audit is not to find every single error "
                            "in the accounting records. Instead, it provides reasonable assurance "
                            "that the financial statements, taken as a whole, "
                            "are free from material misstatement. "
                            "Reasonable assurance means a high level of confidence, "
                            "but not absolute certainty. "
                            "Auditors cannot check every transaction — "
                            "they use professional judgment to focus on the areas "
                            "that matter most.\n\n"
                            "The concept of materiality is central to every audit. "
                            "A misstatement is considered material if it is large enough "
                            "or important enough to influence the decisions of someone "
                            "reading the financial statements. "
                            "For example, if a company accidentally records an expense "
                            "of fifty thousand dong in the wrong category, "
                            "that error is unlikely to be material — "
                            "it will not change an investor's decision. "
                            "But if the company fails to report a liability "
                            "of ten billion dong, that misstatement is clearly material "
                            "because it hides a significant financial obligation.\n\n"
                            "Compliance is another key focus of the audit. "
                            "Auditors check whether the company has followed "
                            "the applicable accounting standards and legal requirements. "
                            "In Vietnam, companies must comply with Vietnamese Accounting Standards "
                            "and, for some listed firms, International Financial Reporting Standards. "
                            "If the auditor finds that the company has not followed these rules, "
                            "the compliance failure must be reported.\n\n"
                            "At the end of the audit, the auditor issues an opinion — "
                            "a formal conclusion about the reliability of the financial statements. "
                            "The most common type is an unqualified opinion, "
                            "sometimes called a clean opinion. "
                            "This means the auditor believes the statements present "
                            "a true and fair view of the company's financial position. "
                            "A qualified opinion means the statements are mostly accurate "
                            "but contain one or more issues that the auditor wants to highlight. "
                            "An adverse opinion means the statements are materially misstated "
                            "and should not be relied upon. "
                            "A disclaimer of opinion means the auditor could not obtain "
                            "enough evidence to form any conclusion at all.\n\n"
                            "For investors, the auditor's opinion is one of the most important "
                            "pieces of information in an annual report. "
                            "A clean opinion provides assurance that the numbers can be trusted. "
                            "Any other type of opinion is a warning sign "
                            "that something may be wrong with the company's financial reporting."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Vai trò của kiểm toán và ý kiến kiểm toán",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "When a company publishes its financial statements, "
                            "how do investors know the numbers are trustworthy? "
                            "The answer is the audit — an independent examination "
                            "of a company's financial records by a qualified professional.\n\n"
                            "In Vietnam, all publicly listed companies must undergo "
                            "an annual audit conducted by a licensed auditing firm. "
                            "The purpose of the audit is not to find every single error "
                            "in the accounting records. Instead, it provides reasonable assurance "
                            "that the financial statements, taken as a whole, "
                            "are free from material misstatement. "
                            "Reasonable assurance means a high level of confidence, "
                            "but not absolute certainty. "
                            "Auditors cannot check every transaction — "
                            "they use professional judgment to focus on the areas "
                            "that matter most.\n\n"
                            "The concept of materiality is central to every audit. "
                            "A misstatement is considered material if it is large enough "
                            "or important enough to influence the decisions of someone "
                            "reading the financial statements. "
                            "For example, if a company accidentally records an expense "
                            "of fifty thousand dong in the wrong category, "
                            "that error is unlikely to be material — "
                            "it will not change an investor's decision. "
                            "But if the company fails to report a liability "
                            "of ten billion dong, that misstatement is clearly material "
                            "because it hides a significant financial obligation.\n\n"
                            "Compliance is another key focus of the audit. "
                            "Auditors check whether the company has followed "
                            "the applicable accounting standards and legal requirements. "
                            "In Vietnam, companies must comply with Vietnamese Accounting Standards "
                            "and, for some listed firms, International Financial Reporting Standards. "
                            "If the auditor finds that the company has not followed these rules, "
                            "the compliance failure must be reported.\n\n"
                            "At the end of the audit, the auditor issues an opinion — "
                            "a formal conclusion about the reliability of the financial statements. "
                            "The most common type is an unqualified opinion, "
                            "sometimes called a clean opinion. "
                            "This means the auditor believes the statements present "
                            "a true and fair view of the company's financial position. "
                            "A qualified opinion means the statements are mostly accurate "
                            "but contain one or more issues that the auditor wants to highlight. "
                            "An adverse opinion means the statements are materially misstated "
                            "and should not be relied upon. "
                            "A disclaimer of opinion means the auditor could not obtain "
                            "enough evidence to form any conclusion at all.\n\n"
                            "For investors, the auditor's opinion is one of the most important "
                            "pieces of information in an annual report. "
                            "A clean opinion provides assurance that the numbers can be trusted. "
                            "Any other type of opinion is a warning sign "
                            "that something may be wrong with the company's financial reporting."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Kiểm toán và ý kiến kiểm toán",
                    "description": "Viết câu sử dụng 6 từ vựng về kiểm toán và ý kiến kiểm toán.",
                    "data": {
                        "vocabList": ["audit", "compliance", "assurance", "material", "misstatement", "opinion"],
                        "items": [
                            {
                                "targetVocab": "audit",
                                "prompt": "Dùng từ 'audit' để viết một câu về quá trình kiểm toán báo cáo tài chính của một doanh nghiệp. Ví dụ: The annual audit revealed that the company's accounting department had been recording revenue from long-term contracts incorrectly for the past two years."
                            },
                            {
                                "targetVocab": "compliance",
                                "prompt": "Dùng từ 'compliance' để viết một câu về việc tuân thủ chuẩn mực kế toán. Ví dụ: The auditors found that the company was not in compliance with international accounting standards because it had failed to disclose several related-party transactions."
                            },
                            {
                                "targetVocab": "assurance",
                                "prompt": "Dùng từ 'assurance' để viết một câu về mức độ đảm bảo mà kiểm toán cung cấp. Ví dụ: The audit provided reasonable assurance to shareholders that the financial statements were reliable, but it could not guarantee that every minor error had been detected."
                            },
                            {
                                "targetVocab": "material",
                                "prompt": "Dùng từ 'material' để viết một câu về tính trọng yếu trong kiểm toán. Ví dụ: The auditor concluded that the unrecorded liability of eight billion dong was material because it would significantly change the company's reported financial position."
                            },
                            {
                                "targetVocab": "misstatement",
                                "prompt": "Dùng từ 'misstatement' để viết một câu về sai sót trên báo cáo tài chính. Ví dụ: The misstatement in the inventory records overstated the company's total assets by three billion dong, misleading investors about the true value of the business."
                            },
                            {
                                "targetVocab": "opinion",
                                "prompt": "Dùng từ 'opinion' để viết một câu về ý kiến kiểm toán và tác động của nó. Ví dụ: When the auditing firm issued a qualified opinion on the company's financial statements, the stock price dropped by fifteen percent within a single trading day."
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
                    "description": "Ôn lại phần 1 và học 6 từ mới về quy trình kiểm toán và thu thập bằng chứng.",
                    "data": {
                        "text": (
                            "Chào mừng bạn trở lại! Trong phần trước, bạn đã học 6 từ vựng nền tảng: "
                            "audit — kiểm toán, compliance — tuân thủ, assurance — đảm bảo, "
                            "material — trọng yếu, misstatement — sai sót, và opinion — ý kiến kiểm toán. "
                            "Bạn đã hiểu vai trò của kiểm toán và tại sao ý kiến kiểm toán "
                            "là thông tin quan trọng nhất trong báo cáo thường niên. "
                            "Bây giờ, chúng ta sẽ đi sâu vào quy trình kiểm toán — "
                            "kiểm toán viên thực sự làm gì từ ngày đầu tiên đến ngày cuối cùng.\n\n"
                            "Trong phần 2, bạn sẽ học 6 từ mới: internal, external, sampling, evidence, procedure, và engagement. "
                            "Đây là bộ từ vựng về cách kiểm toán được thực hiện trong thực tế.\n\n"
                            "Từ đầu tiên là internal — tính từ — nghĩa là nội bộ, "
                            "thuộc về bên trong tổ chức. Trong kiểm toán, internal audit "
                            "là hoạt động kiểm tra do chính nhân viên của doanh nghiệp thực hiện. "
                            "Ví dụ: 'The internal audit team discovered that several employees "
                            "had been approving their own expense claims without a second signature, "
                            "violating the company's internal control policies.' "
                            "Trong bài đọc, internal audit là tuyến phòng thủ đầu tiên — "
                            "doanh nghiệp tự kiểm tra mình trước khi kiểm toán viên bên ngoài đến.\n\n"
                            "Từ thứ hai là external — tính từ — nghĩa là bên ngoài, "
                            "thuộc về một tổ chức độc lập không liên quan đến doanh nghiệp. "
                            "Ví dụ: 'The external auditors from Deloitte spent four weeks "
                            "examining the company's financial records before issuing their opinion.' "
                            "Trong bài đọc, external audit là kiểm toán độc lập — "
                            "do công ty kiểm toán bên ngoài thực hiện để đảm bảo tính khách quan.\n\n"
                            "Từ thứ ba là sampling — danh từ — nghĩa là lấy mẫu, "
                            "kỹ thuật chọn một phần nhỏ giao dịch để kiểm tra thay vì kiểm tra toàn bộ. "
                            "Ví dụ: 'Because the company processed over one million transactions during the year, "
                            "the auditors used statistical sampling to select a representative group "
                            "of five hundred transactions for detailed testing.' "
                            "Trong bài đọc, sampling là công cụ thực tế — "
                            "kiểm toán viên không thể kiểm tra mọi giao dịch nên phải chọn mẫu thông minh.\n\n"
                            "Từ thứ tư là evidence — danh từ — nghĩa là bằng chứng, "
                            "thông tin mà kiểm toán viên thu thập để hỗ trợ kết luận của mình. "
                            "Ví dụ: 'The auditor gathered evidence by reviewing bank statements, "
                            "confirming balances with third parties, and physically counting inventory in the warehouse.' "
                            "Trong bài đọc, evidence là nền tảng của mọi kết luận kiểm toán — "
                            "không có bằng chứng, không có ý kiến.\n\n"
                            "Từ thứ năm là procedure — danh từ — nghĩa là thủ tục hoặc quy trình, "
                            "các bước cụ thể mà kiểm toán viên thực hiện để thu thập bằng chứng. "
                            "Ví dụ: 'The audit procedure for testing revenue included selecting a sample of sales invoices "
                            "and tracing each one back to the original customer order and shipping documents.' "
                            "Trong bài đọc, procedure là phương pháp làm việc — "
                            "mỗi loại tài khoản có thủ tục kiểm toán riêng.\n\n"
                            "Từ cuối cùng là engagement — danh từ — nghĩa là hợp đồng kiểm toán, "
                            "thỏa thuận chính thức giữa công ty kiểm toán và khách hàng. "
                            "Ví dụ: 'The engagement letter specified the scope of the audit, "
                            "the responsibilities of both parties, and the expected completion date.' "
                            "Trong bài đọc, engagement là điểm khởi đầu — "
                            "trước khi kiểm toán bắt đầu, hai bên phải thống nhất phạm vi và trách nhiệm.\n\n"
                            "Sáu từ mới đã sẵn sàng. Hãy bắt đầu với flashcard rồi đọc bài viết "
                            "về quy trình kiểm toán và cách thu thập bằng chứng nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Quy trình kiểm toán và bằng chứng",
                    "description": "Học 6 từ: internal, external, sampling, evidence, procedure, engagement",
                    "data": {"vocabList": ["internal", "external", "sampling", "evidence", "procedure", "engagement"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Quy trình kiểm toán và bằng chứng",
                    "description": "Học 6 từ: internal, external, sampling, evidence, procedure, engagement",
                    "data": {"vocabList": ["internal", "external", "sampling", "evidence", "procedure", "engagement"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Quy trình kiểm toán và bằng chứng",
                    "description": "Học 6 từ: internal, external, sampling, evidence, procedure, engagement",
                    "data": {"vocabList": ["internal", "external", "sampling", "evidence", "procedure", "engagement"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Quy trình kiểm toán và bằng chứng",
                    "description": "Học 6 từ: internal, external, sampling, evidence, procedure, engagement",
                    "data": {"vocabList": ["internal", "external", "sampling", "evidence", "procedure", "engagement"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Quy trình kiểm toán và bằng chứng",
                    "description": "Học 6 từ: internal, external, sampling, evidence, procedure, engagement",
                    "data": {"vocabList": ["internal", "external", "sampling", "evidence", "procedure", "engagement"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Quy trình kiểm toán và thu thập bằng chứng",
                    "description": "An audit does not happen overnight — it is a structured process that unfolds in several stages.",
                    "data": {
                        "text": (
                            "An audit does not happen overnight — "
                            "it is a structured process that unfolds in several stages, "
                            "each with its own set of procedures and objectives.\n\n"
                            "The process begins with the engagement. "
                            "Before any audit work starts, the auditing firm and the client company "
                            "sign an engagement letter. This document defines the scope of the audit, "
                            "the time frame, the fees, and the responsibilities of each party. "
                            "The engagement letter is important because it sets clear expectations. "
                            "Without it, disagreements about what the audit should cover "
                            "could arise later and delay the entire process.\n\n"
                            "There are two main types of audits: internal and external. "
                            "An internal audit is conducted by employees who work for the company itself. "
                            "The internal audit department reports to senior management or the board of directors. "
                            "Its job is to evaluate the company's internal controls, "
                            "identify risks, and recommend improvements. "
                            "For example, an internal auditor at a Vietnamese bank "
                            "might review the loan approval process to make sure "
                            "that no single employee can approve a large loan without oversight.\n\n"
                            "An external audit, by contrast, is performed by an independent firm "
                            "that has no financial ties to the company. "
                            "External auditors are hired to provide an objective assessment "
                            "of the financial statements. In Vietnam, the Big Four accounting firms — "
                            "Deloitte, PwC, EY, and KPMG — conduct external audits "
                            "for most of the largest listed companies. "
                            "The independence of external auditors is what gives their opinion credibility.\n\n"
                            "Once the engagement is established and the audit team understands the business, "
                            "the auditors begin gathering evidence. "
                            "Audit evidence is any information that supports or contradicts "
                            "the numbers in the financial statements. "
                            "Evidence can take many forms: bank confirmations, supplier invoices, "
                            "shipping records, physical counts of inventory, "
                            "and interviews with company employees.\n\n"
                            "To gather evidence efficiently, auditors use sampling. "
                            "A large company may process millions of transactions in a single year. "
                            "It would be impossible to check every one. "
                            "Instead, auditors select a representative sample of transactions "
                            "and test them in detail. If the sample is free from errors, "
                            "the auditor can reasonably conclude that the entire population "
                            "of transactions is likely accurate. "
                            "If the sample reveals problems, the auditor expands the testing.\n\n"
                            "Each type of account requires specific audit procedures. "
                            "For cash, the procedure might involve confirming the bank balance "
                            "directly with the bank. For inventory, the procedure might include "
                            "visiting the warehouse and physically counting the goods. "
                            "For revenue, the procedure might involve tracing sales invoices "
                            "back to customer orders and delivery records. "
                            "The choice of procedure depends on the nature of the account "
                            "and the level of risk the auditor has identified.\n\n"
                            "Throughout the process, the audit team documents everything. "
                            "Every piece of evidence collected, every procedure performed, "
                            "and every conclusion reached is recorded in the audit working papers. "
                            "These papers serve as proof that the audit was conducted properly "
                            "and that the auditor's opinion is supported by sufficient evidence."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Quy trình kiểm toán và thu thập bằng chứng",
                    "description": "An audit does not happen overnight — it is a structured process that unfolds in several stages.",
                    "data": {
                        "text": (
                            "An audit does not happen overnight — "
                            "it is a structured process that unfolds in several stages, "
                            "each with its own set of procedures and objectives.\n\n"
                            "The process begins with the engagement. "
                            "Before any audit work starts, the auditing firm and the client company "
                            "sign an engagement letter. This document defines the scope of the audit, "
                            "the time frame, the fees, and the responsibilities of each party. "
                            "The engagement letter is important because it sets clear expectations. "
                            "Without it, disagreements about what the audit should cover "
                            "could arise later and delay the entire process.\n\n"
                            "There are two main types of audits: internal and external. "
                            "An internal audit is conducted by employees who work for the company itself. "
                            "The internal audit department reports to senior management or the board of directors. "
                            "Its job is to evaluate the company's internal controls, "
                            "identify risks, and recommend improvements. "
                            "For example, an internal auditor at a Vietnamese bank "
                            "might review the loan approval process to make sure "
                            "that no single employee can approve a large loan without oversight.\n\n"
                            "An external audit, by contrast, is performed by an independent firm "
                            "that has no financial ties to the company. "
                            "External auditors are hired to provide an objective assessment "
                            "of the financial statements. In Vietnam, the Big Four accounting firms — "
                            "Deloitte, PwC, EY, and KPMG — conduct external audits "
                            "for most of the largest listed companies. "
                            "The independence of external auditors is what gives their opinion credibility.\n\n"
                            "Once the engagement is established and the audit team understands the business, "
                            "the auditors begin gathering evidence. "
                            "Audit evidence is any information that supports or contradicts "
                            "the numbers in the financial statements. "
                            "Evidence can take many forms: bank confirmations, supplier invoices, "
                            "shipping records, physical counts of inventory, "
                            "and interviews with company employees.\n\n"
                            "To gather evidence efficiently, auditors use sampling. "
                            "A large company may process millions of transactions in a single year. "
                            "It would be impossible to check every one. "
                            "Instead, auditors select a representative sample of transactions "
                            "and test them in detail. If the sample is free from errors, "
                            "the auditor can reasonably conclude that the entire population "
                            "of transactions is likely accurate. "
                            "If the sample reveals problems, the auditor expands the testing.\n\n"
                            "Each type of account requires specific audit procedures. "
                            "For cash, the procedure might involve confirming the bank balance "
                            "directly with the bank. For inventory, the procedure might include "
                            "visiting the warehouse and physically counting the goods. "
                            "For revenue, the procedure might involve tracing sales invoices "
                            "back to customer orders and delivery records. "
                            "The choice of procedure depends on the nature of the account "
                            "and the level of risk the auditor has identified.\n\n"
                            "Throughout the process, the audit team documents everything. "
                            "Every piece of evidence collected, every procedure performed, "
                            "and every conclusion reached is recorded in the audit working papers. "
                            "These papers serve as proof that the audit was conducted properly "
                            "and that the auditor's opinion is supported by sufficient evidence."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Quy trình kiểm toán và thu thập bằng chứng",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "An audit does not happen overnight — "
                            "it is a structured process that unfolds in several stages, "
                            "each with its own set of procedures and objectives.\n\n"
                            "The process begins with the engagement. "
                            "Before any audit work starts, the auditing firm and the client company "
                            "sign an engagement letter. This document defines the scope of the audit, "
                            "the time frame, the fees, and the responsibilities of each party. "
                            "The engagement letter is important because it sets clear expectations. "
                            "Without it, disagreements about what the audit should cover "
                            "could arise later and delay the entire process.\n\n"
                            "There are two main types of audits: internal and external. "
                            "An internal audit is conducted by employees who work for the company itself. "
                            "The internal audit department reports to senior management or the board of directors. "
                            "Its job is to evaluate the company's internal controls, "
                            "identify risks, and recommend improvements. "
                            "For example, an internal auditor at a Vietnamese bank "
                            "might review the loan approval process to make sure "
                            "that no single employee can approve a large loan without oversight.\n\n"
                            "An external audit, by contrast, is performed by an independent firm "
                            "that has no financial ties to the company. "
                            "External auditors are hired to provide an objective assessment "
                            "of the financial statements. In Vietnam, the Big Four accounting firms — "
                            "Deloitte, PwC, EY, and KPMG — conduct external audits "
                            "for most of the largest listed companies. "
                            "The independence of external auditors is what gives their opinion credibility.\n\n"
                            "Once the engagement is established and the audit team understands the business, "
                            "the auditors begin gathering evidence. "
                            "Audit evidence is any information that supports or contradicts "
                            "the numbers in the financial statements. "
                            "Evidence can take many forms: bank confirmations, supplier invoices, "
                            "shipping records, physical counts of inventory, "
                            "and interviews with company employees.\n\n"
                            "To gather evidence efficiently, auditors use sampling. "
                            "A large company may process millions of transactions in a single year. "
                            "It would be impossible to check every one. "
                            "Instead, auditors select a representative sample of transactions "
                            "and test them in detail. If the sample is free from errors, "
                            "the auditor can reasonably conclude that the entire population "
                            "of transactions is likely accurate. "
                            "If the sample reveals problems, the auditor expands the testing.\n\n"
                            "Each type of account requires specific audit procedures. "
                            "For cash, the procedure might involve confirming the bank balance "
                            "directly with the bank. For inventory, the procedure might include "
                            "visiting the warehouse and physically counting the goods. "
                            "For revenue, the procedure might involve tracing sales invoices "
                            "back to customer orders and delivery records. "
                            "The choice of procedure depends on the nature of the account "
                            "and the level of risk the auditor has identified.\n\n"
                            "Throughout the process, the audit team documents everything. "
                            "Every piece of evidence collected, every procedure performed, "
                            "and every conclusion reached is recorded in the audit working papers. "
                            "These papers serve as proof that the audit was conducted properly "
                            "and that the auditor's opinion is supported by sufficient evidence."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Quy trình kiểm toán và bằng chứng",
                    "description": "Viết câu sử dụng 6 từ vựng về quy trình kiểm toán.",
                    "data": {
                        "vocabList": ["internal", "external", "sampling", "evidence", "procedure", "engagement"],
                        "items": [
                            {
                                "targetVocab": "internal",
                                "prompt": "Dùng từ 'internal' để viết một câu về vai trò của kiểm toán nội bộ trong doanh nghiệp. Ví dụ: The internal audit team recommended that the company strengthen its approval process for purchases over one hundred million dong to prevent unauthorized spending."
                            },
                            {
                                "targetVocab": "external",
                                "prompt": "Dùng từ 'external' để viết một câu về kiểm toán độc lập bên ngoài. Ví dụ: The board of directors hired an external auditing firm to review the financial statements because investors demanded an independent assessment of the company's accounts."
                            },
                            {
                                "targetVocab": "sampling",
                                "prompt": "Dùng từ 'sampling' để viết một câu về kỹ thuật lấy mẫu trong kiểm toán. Ví dụ: The auditors used statistical sampling to select three hundred invoices from a total of fifty thousand, testing each one for accuracy and proper authorization."
                            },
                            {
                                "targetVocab": "evidence",
                                "prompt": "Dùng từ 'evidence' để viết một câu về bằng chứng kiểm toán và cách thu thập. Ví dụ: The strongest piece of audit evidence was a confirmation letter from the bank, which verified that the company's reported cash balance was accurate to the last dong."
                            },
                            {
                                "targetVocab": "procedure",
                                "prompt": "Dùng từ 'procedure' để viết một câu về thủ tục kiểm toán cụ thể. Ví dụ: The audit procedure for testing inventory required the team to visit three warehouses across Vietnam and physically count the goods on the shelves."
                            },
                            {
                                "targetVocab": "engagement",
                                "prompt": "Dùng từ 'engagement' để viết một câu về hợp đồng kiểm toán giữa công ty và kiểm toán viên. Ví dụ: The engagement letter clearly stated that the audit would cover only the current fiscal year and would not include a review of the company's tax filings."
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
                    "description": "Ôn lại phần 1-2 và học 6 từ mới về gian lận, phát hiện và đạo đức kiểm toán.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng của chuỗi từ vựng! "
                            "Hãy cùng ôn lại nhanh những gì bạn đã học. "
                            "Trong phần 1, bạn đã nắm được 6 từ nền tảng: audit, compliance, assurance, material, misstatement, opinion — "
                            "những khái niệm cốt lõi về vai trò và kết quả của kiểm toán. "
                            "Trong phần 2, bạn đã học thêm internal, external, sampling, evidence, procedure, engagement — "
                            "bộ từ vựng về quy trình kiểm toán và cách thu thập bằng chứng.\n\n"
                            "Bây giờ, trong phần 3, chúng ta sẽ bước vào một khía cạnh nghiêm trọng hơn: "
                            "gian lận tài chính, phát hiện sai phạm, và đạo đức nghề nghiệp kiểm toán. "
                            "Bạn sẽ học 6 từ mới: fraud, detection, disclosure, independence, objectivity, và skepticism.\n\n"
                            "Từ đầu tiên là fraud — danh từ — nghĩa là gian lận, "
                            "hành vi cố ý lừa dối để thu lợi bất chính hoặc che giấu sự thật tài chính. "
                            "Ví dụ: 'The investigation revealed that senior managers had committed fraud "
                            "by inflating revenue figures for three consecutive years to meet performance targets.' "
                            "Trong bài đọc, fraud là mối đe dọa lớn nhất đối với độ tin cậy "
                            "của báo cáo tài chính — và là lý do kiểm toán viên phải luôn cảnh giác.\n\n"
                            "Từ thứ hai là detection — danh từ — nghĩa là phát hiện, "
                            "quá trình tìm ra sai sót, gian lận, hoặc vi phạm trong hồ sơ tài chính. "
                            "Ví dụ: 'Early detection of the accounting irregularities saved the company "
                            "from a much larger scandal that could have destroyed investor confidence entirely.' "
                            "Trong bài đọc, detection là mục tiêu quan trọng — "
                            "phát hiện sớm giúp ngăn chặn thiệt hại trước khi nó lan rộng.\n\n"
                            "Từ thứ ba là disclosure — danh từ — nghĩa là công bố thông tin, "
                            "nghĩa vụ cung cấp thông tin đầy đủ và trung thực cho người đọc báo cáo. "
                            "Ví dụ: 'The company's failure to make proper disclosure about the CEO's conflict of interest "
                            "led to a formal investigation by the securities regulator.' "
                            "Trong bài đọc, disclosure là nguyên tắc minh bạch — "
                            "kiểm toán viên phải đảm bảo rằng mọi thông tin quan trọng đều được công bố.\n\n"
                            "Từ thứ tư là independence — danh từ — nghĩa là tính độc lập, "
                            "trạng thái không bị ảnh hưởng bởi lợi ích tài chính hay quan hệ cá nhân với khách hàng. "
                            "Ví dụ: 'The auditing firm resigned from the engagement because accepting a large consulting contract "
                            "from the same client would have compromised its independence.' "
                            "Trong bài đọc, independence là nền tảng đạo đức — "
                            "nếu kiểm toán viên không độc lập, ý kiến kiểm toán mất hết giá trị.\n\n"
                            "Từ thứ năm là objectivity — danh từ — nghĩa là tính khách quan, "
                            "khả năng đánh giá sự việc dựa trên bằng chứng mà không bị thiên kiến. "
                            "Ví dụ: 'The auditor maintained objectivity throughout the engagement "
                            "by refusing to accept gifts from the client and avoiding personal relationships "
                            "with the company's management team.' "
                            "Trong bài đọc, objectivity đi đôi với independence — "
                            "kiểm toán viên phải vừa độc lập về mặt tổ chức, vừa khách quan trong đánh giá.\n\n"
                            "Từ cuối cùng là skepticism — danh từ — nghĩa là thái độ hoài nghi nghề nghiệp, "
                            "tư duy luôn đặt câu hỏi và không chấp nhận bằng chứng một cách mù quáng. "
                            "Ví dụ: 'Professional skepticism requires auditors to question every explanation "
                            "provided by management, even when the answers seem perfectly reasonable.' "
                            "Trong bài đọc, skepticism là phẩm chất quan trọng nhất — "
                            "kiểm toán viên giỏi không bao giờ tin ngay lần đầu.\n\n"
                            "Tuyệt vời! Bạn đã có đủ 18 từ vựng. Hãy hoàn thành flashcard "
                            "và đọc bài viết cuối cùng về gian lận tài chính và đạo đức kiểm toán nhé!"
                        )
                    }
                },
                {
                    "activityType": "viewFlashcards",
                    "title": "Flashcards: Gian lận và đạo đức kiểm toán",
                    "description": "Học 6 từ: fraud, detection, disclosure, independence, objectivity, skepticism",
                    "data": {"vocabList": ["fraud", "detection", "disclosure", "independence", "objectivity", "skepticism"]}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Gian lận và đạo đức kiểm toán",
                    "description": "Học 6 từ: fraud, detection, disclosure, independence, objectivity, skepticism",
                    "data": {"vocabList": ["fraud", "detection", "disclosure", "independence", "objectivity", "skepticism"]}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Gian lận và đạo đức kiểm toán",
                    "description": "Học 6 từ: fraud, detection, disclosure, independence, objectivity, skepticism",
                    "data": {"vocabList": ["fraud", "detection", "disclosure", "independence", "objectivity", "skepticism"]}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Gian lận và đạo đức kiểm toán",
                    "description": "Học 6 từ: fraud, detection, disclosure, independence, objectivity, skepticism",
                    "data": {"vocabList": ["fraud", "detection", "disclosure", "independence", "objectivity", "skepticism"]}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Gian lận và đạo đức kiểm toán",
                    "description": "Học 6 từ: fraud, detection, disclosure, independence, objectivity, skepticism",
                    "data": {"vocabList": ["fraud", "detection", "disclosure", "independence", "objectivity", "skepticism"]}
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Gian lận tài chính và đạo đức kiểm toán",
                    "description": "Not every error in a financial statement is an innocent mistake — some are deliberate acts of deception.",
                    "data": {
                        "text": (
                            "Not every error in a financial statement is an innocent mistake — "
                            "some are deliberate acts of deception. "
                            "When someone intentionally manipulates financial records "
                            "to mislead investors, creditors, or regulators, "
                            "that act is called fraud.\n\n"
                            "Financial fraud can take many forms. "
                            "A company might overstate its revenue by recording sales "
                            "that never actually happened. "
                            "It might understate its expenses by hiding costs in other accounts. "
                            "It might inflate the value of its assets "
                            "or fail to report significant liabilities. "
                            "In Vietnam, several high-profile cases have shown "
                            "that fraud can occur even in large, well-known companies "
                            "that appear to have strong financial controls.\n\n"
                            "The detection of fraud is one of the most challenging aspects of auditing. "
                            "Unlike ordinary errors, fraud is designed to be hidden. "
                            "The people who commit fraud often go to great lengths "
                            "to make the numbers look normal. "
                            "They may create fake documents, forge signatures, "
                            "or pressure subordinates to record false transactions. "
                            "Detection requires auditors to look beyond the surface "
                            "and question whether the evidence they are seeing is genuine.\n\n"
                            "This is where disclosure becomes critical. "
                            "Companies are required to disclose all information "
                            "that could affect the decisions of investors and other stakeholders. "
                            "If a company hides a major lawsuit, a conflict of interest, "
                            "or a significant change in accounting policy, "
                            "that failure of disclosure can be just as damaging as fraud itself. "
                            "Auditors must verify that the company's disclosures are complete and accurate — "
                            "not just that the numbers add up.\n\n"
                            "To perform their work effectively, auditors must maintain independence. "
                            "Independence means that the auditor has no financial interest "
                            "in the company being audited and no personal relationship "
                            "with its management that could influence the audit's outcome. "
                            "If an auditing firm also provides consulting services to the same client, "
                            "there is a risk that the firm might soften its audit findings "
                            "to keep the consulting contract. "
                            "For this reason, regulations in many countries — including Vietnam — "
                            "limit the types of non-audit services that an auditing firm "
                            "can provide to its audit clients.\n\n"
                            "Closely related to independence is objectivity. "
                            "While independence is about the auditor's organizational position, "
                            "objectivity is about the auditor's mindset. "
                            "An objective auditor evaluates evidence based on facts, "
                            "not on personal feelings or pressure from the client. "
                            "Objectivity requires the auditor to consider all evidence fairly, "
                            "even when the findings are uncomfortable for the client.\n\n"
                            "The foundation of both independence and objectivity "
                            "is professional skepticism. "
                            "Skepticism means approaching every audit with a questioning mind. "
                            "It does not mean assuming that the client is dishonest. "
                            "It means recognizing that errors and fraud can occur "
                            "and that the auditor must remain alert to signs of both. "
                            "A skeptical auditor does not simply accept management's explanations — "
                            "they ask for supporting evidence, look for inconsistencies, "
                            "and consider whether the information makes sense "
                            "in the context of the business.\n\n"
                            "Together, independence, objectivity, and skepticism "
                            "form the ethical backbone of the auditing profession. "
                            "Without these qualities, an audit would be nothing more "
                            "than a rubber stamp on whatever the company wants to report."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Gian lận tài chính và đạo đức kiểm toán",
                    "description": "Not every error in a financial statement is an innocent mistake — some are deliberate acts of deception.",
                    "data": {
                        "text": (
                            "Not every error in a financial statement is an innocent mistake — "
                            "some are deliberate acts of deception. "
                            "When someone intentionally manipulates financial records "
                            "to mislead investors, creditors, or regulators, "
                            "that act is called fraud.\n\n"
                            "Financial fraud can take many forms. "
                            "A company might overstate its revenue by recording sales "
                            "that never actually happened. "
                            "It might understate its expenses by hiding costs in other accounts. "
                            "It might inflate the value of its assets "
                            "or fail to report significant liabilities. "
                            "In Vietnam, several high-profile cases have shown "
                            "that fraud can occur even in large, well-known companies "
                            "that appear to have strong financial controls.\n\n"
                            "The detection of fraud is one of the most challenging aspects of auditing. "
                            "Unlike ordinary errors, fraud is designed to be hidden. "
                            "The people who commit fraud often go to great lengths "
                            "to make the numbers look normal. "
                            "They may create fake documents, forge signatures, "
                            "or pressure subordinates to record false transactions. "
                            "Detection requires auditors to look beyond the surface "
                            "and question whether the evidence they are seeing is genuine.\n\n"
                            "This is where disclosure becomes critical. "
                            "Companies are required to disclose all information "
                            "that could affect the decisions of investors and other stakeholders. "
                            "If a company hides a major lawsuit, a conflict of interest, "
                            "or a significant change in accounting policy, "
                            "that failure of disclosure can be just as damaging as fraud itself. "
                            "Auditors must verify that the company's disclosures are complete and accurate — "
                            "not just that the numbers add up.\n\n"
                            "To perform their work effectively, auditors must maintain independence. "
                            "Independence means that the auditor has no financial interest "
                            "in the company being audited and no personal relationship "
                            "with its management that could influence the audit's outcome. "
                            "If an auditing firm also provides consulting services to the same client, "
                            "there is a risk that the firm might soften its audit findings "
                            "to keep the consulting contract. "
                            "For this reason, regulations in many countries — including Vietnam — "
                            "limit the types of non-audit services that an auditing firm "
                            "can provide to its audit clients.\n\n"
                            "Closely related to independence is objectivity. "
                            "While independence is about the auditor's organizational position, "
                            "objectivity is about the auditor's mindset. "
                            "An objective auditor evaluates evidence based on facts, "
                            "not on personal feelings or pressure from the client. "
                            "Objectivity requires the auditor to consider all evidence fairly, "
                            "even when the findings are uncomfortable for the client.\n\n"
                            "The foundation of both independence and objectivity "
                            "is professional skepticism. "
                            "Skepticism means approaching every audit with a questioning mind. "
                            "It does not mean assuming that the client is dishonest. "
                            "It means recognizing that errors and fraud can occur "
                            "and that the auditor must remain alert to signs of both. "
                            "A skeptical auditor does not simply accept management's explanations — "
                            "they ask for supporting evidence, look for inconsistencies, "
                            "and consider whether the information makes sense "
                            "in the context of the business.\n\n"
                            "Together, independence, objectivity, and skepticism "
                            "form the ethical backbone of the auditing profession. "
                            "Without these qualities, an audit would be nothing more "
                            "than a rubber stamp on whatever the company wants to report."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Gian lận tài chính và đạo đức kiểm toán",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Not every error in a financial statement is an innocent mistake — "
                            "some are deliberate acts of deception. "
                            "When someone intentionally manipulates financial records "
                            "to mislead investors, creditors, or regulators, "
                            "that act is called fraud.\n\n"
                            "Financial fraud can take many forms. "
                            "A company might overstate its revenue by recording sales "
                            "that never actually happened. "
                            "It might understate its expenses by hiding costs in other accounts. "
                            "It might inflate the value of its assets "
                            "or fail to report significant liabilities. "
                            "In Vietnam, several high-profile cases have shown "
                            "that fraud can occur even in large, well-known companies "
                            "that appear to have strong financial controls.\n\n"
                            "The detection of fraud is one of the most challenging aspects of auditing. "
                            "Unlike ordinary errors, fraud is designed to be hidden. "
                            "The people who commit fraud often go to great lengths "
                            "to make the numbers look normal. "
                            "They may create fake documents, forge signatures, "
                            "or pressure subordinates to record false transactions. "
                            "Detection requires auditors to look beyond the surface "
                            "and question whether the evidence they are seeing is genuine.\n\n"
                            "This is where disclosure becomes critical. "
                            "Companies are required to disclose all information "
                            "that could affect the decisions of investors and other stakeholders. "
                            "If a company hides a major lawsuit, a conflict of interest, "
                            "or a significant change in accounting policy, "
                            "that failure of disclosure can be just as damaging as fraud itself. "
                            "Auditors must verify that the company's disclosures are complete and accurate — "
                            "not just that the numbers add up.\n\n"
                            "To perform their work effectively, auditors must maintain independence. "
                            "Independence means that the auditor has no financial interest "
                            "in the company being audited and no personal relationship "
                            "with its management that could influence the audit's outcome. "
                            "If an auditing firm also provides consulting services to the same client, "
                            "there is a risk that the firm might soften its audit findings "
                            "to keep the consulting contract. "
                            "For this reason, regulations in many countries — including Vietnam — "
                            "limit the types of non-audit services that an auditing firm "
                            "can provide to its audit clients.\n\n"
                            "Closely related to independence is objectivity. "
                            "While independence is about the auditor's organizational position, "
                            "objectivity is about the auditor's mindset. "
                            "An objective auditor evaluates evidence based on facts, "
                            "not on personal feelings or pressure from the client. "
                            "Objectivity requires the auditor to consider all evidence fairly, "
                            "even when the findings are uncomfortable for the client.\n\n"
                            "The foundation of both independence and objectivity "
                            "is professional skepticism. "
                            "Skepticism means approaching every audit with a questioning mind. "
                            "It does not mean assuming that the client is dishonest. "
                            "It means recognizing that errors and fraud can occur "
                            "and that the auditor must remain alert to signs of both. "
                            "A skeptical auditor does not simply accept management's explanations — "
                            "they ask for supporting evidence, look for inconsistencies, "
                            "and consider whether the information makes sense "
                            "in the context of the business.\n\n"
                            "Together, independence, objectivity, and skepticism "
                            "form the ethical backbone of the auditing profession. "
                            "Without these qualities, an audit would be nothing more "
                            "than a rubber stamp on whatever the company wants to report."
                        )
                    }
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Gian lận và đạo đức kiểm toán",
                    "description": "Viết câu sử dụng 6 từ vựng về gian lận và đạo đức kiểm toán.",
                    "data": {
                        "vocabList": ["fraud", "detection", "disclosure", "independence", "objectivity", "skepticism"],
                        "items": [
                            {
                                "targetVocab": "fraud",
                                "prompt": "Dùng từ 'fraud' để viết một câu về gian lận tài chính và hậu quả của nó. Ví dụ: The fraud scheme involved creating fake invoices from non-existent suppliers, allowing the finance director to steal over twenty billion dong from the company over four years."
                            },
                            {
                                "targetVocab": "detection",
                                "prompt": "Dùng từ 'detection' để viết một câu về việc phát hiện sai phạm trong kiểm toán. Ví dụ: The detection of the revenue manipulation was delayed by two years because the perpetrators had created convincing supporting documents for every fraudulent transaction."
                            },
                            {
                                "targetVocab": "disclosure",
                                "prompt": "Dùng từ 'disclosure' để viết một câu về nghĩa vụ công bố thông tin tài chính. Ví dụ: The auditor required the company to add a disclosure note explaining that the CEO's brother owned the supplier that accounted for forty percent of all purchases."
                            },
                            {
                                "targetVocab": "independence",
                                "prompt": "Dùng từ 'independence' để viết một câu về tính độc lập của kiểm toán viên. Ví dụ: The regulator questioned the auditing firm's independence after discovering that one of its senior partners had accepted a luxury vacation paid for by the client company."
                            },
                            {
                                "targetVocab": "objectivity",
                                "prompt": "Dùng từ 'objectivity' để viết một câu về tính khách quan trong đánh giá kiểm toán. Ví dụ: The auditor's objectivity was tested when the client's CEO personally called to argue that the disputed transaction should not be reported as a material misstatement."
                            },
                            {
                                "targetVocab": "skepticism",
                                "prompt": "Dùng từ 'skepticism' để viết một câu về thái độ hoài nghi nghề nghiệp. Ví dụ: It was the junior auditor's professional skepticism that uncovered the fraud — she noticed that the dates on several supplier invoices fell on public holidays when no business would have been open."
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
                            "Chúc mừng bạn! Bạn đã hoàn thành cả 3 phần học từ vựng về Kiểm toán. "
                            "Hãy cùng nhìn lại hành trình của bạn.\n\n"
                            "Trong phần 1, bạn đã học những khái niệm nền tảng nhất: "
                            "audit — kiểm toán, compliance — tuân thủ, assurance — đảm bảo, "
                            "material — trọng yếu, misstatement — sai sót, và opinion — ý kiến kiểm toán. "
                            "Đây là bộ từ vựng cốt lõi về vai trò và kết quả của kiểm toán.\n\n"
                            "Trong phần 2, bạn đã đi sâu vào quy trình kiểm toán: "
                            "internal — nội bộ, external — bên ngoài, sampling — lấy mẫu, "
                            "evidence — bằng chứng, procedure — thủ tục, và engagement — hợp đồng kiểm toán. "
                            "Những từ này giúp bạn hiểu kiểm toán viên thực sự làm gì mỗi ngày.\n\n"
                            "Trong phần 3, bạn đã khám phá: "
                            "fraud — gian lận, detection — phát hiện, disclosure — công bố thông tin, "
                            "independence — tính độc lập, objectivity — tính khách quan, và skepticism — thái độ hoài nghi. "
                            "Đây là những từ về đạo đức nghề nghiệp và phát hiện gian lận tài chính.\n\n"
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
                    "description": "Học 18 từ: audit, compliance, assurance, material, misstatement, opinion, internal, external, sampling, evidence, procedure, engagement, fraud, detection, disclosure, independence, objectivity, skepticism",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "speakFlashcards",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: audit, compliance, assurance, material, misstatement, opinion, internal, external, sampling, evidence, procedure, engagement, fraud, detection, disclosure, independence, objectivity, skepticism",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel1",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: audit, compliance, assurance, material, misstatement, opinion, internal, external, sampling, evidence, procedure, engagement, fraud, detection, disclosure, independence, objectivity, skepticism",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel2",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: audit, compliance, assurance, material, misstatement, opinion, internal, external, sampling, evidence, procedure, engagement, fraud, detection, disclosure, independence, objectivity, skepticism",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "vocabLevel3",
                    "title": "Flashcards: Ôn tập toàn bộ từ vựng",
                    "description": "Học 18 từ: audit, compliance, assurance, material, misstatement, opinion, internal, external, sampling, evidence, procedure, engagement, fraud, detection, disclosure, independence, objectivity, skepticism",
                    "data": {"vocabList": ALL_WORDS}
                },
                {
                    "activityType": "writingSentence",
                    "title": "Viết: Ôn tập toàn bộ từ vựng kiểm toán",
                    "description": "Viết câu sử dụng tất cả 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "items": [
                            {
                                "targetVocab": "audit",
                                "prompt": "Dùng từ 'audit' để viết một câu về tác động của kiểm toán đối với niềm tin của nhà đầu tư. Ví dụ: The company's decision to switch to a more reputable auditing firm restored investor confidence after the previous audit had failed to detect significant accounting irregularities."
                            },
                            {
                                "targetVocab": "compliance",
                                "prompt": "Dùng từ 'compliance' để viết một câu về hậu quả khi doanh nghiệp không tuân thủ quy định. Ví dụ: The securities regulator fined the company five billion dong for non-compliance with financial reporting deadlines, damaging its reputation among institutional investors."
                            },
                            {
                                "targetVocab": "assurance",
                                "prompt": "Dùng từ 'assurance' để viết một câu về sự khác biệt giữa đảm bảo hợp lý và đảm bảo tuyệt đối. Ví dụ: The audit report clearly stated that it provided reasonable assurance, not absolute assurance, because no audit can guarantee that every single error has been found."
                            },
                            {
                                "targetVocab": "material",
                                "prompt": "Dùng từ 'material' để viết một câu về cách xác định tính trọng yếu trong kiểm toán. Ví dụ: The audit team set the materiality threshold at two percent of total revenue, meaning any misstatement above that level would be considered material and reported to the board."
                            },
                            {
                                "targetVocab": "misstatement",
                                "prompt": "Dùng từ 'misstatement' để viết một câu về phát hiện sai sót trong quá trình kiểm toán. Ví dụ: The auditors identified a misstatement of twelve billion dong in the company's accounts receivable because several customer invoices had been recorded twice in the system."
                            },
                            {
                                "targetVocab": "opinion",
                                "prompt": "Dùng từ 'opinion' để viết một câu về các loại ý kiến kiểm toán khác nhau. Ví dụ: The auditing firm issued an adverse opinion because the company had refused to correct a material misstatement that overstated its total assets by twenty percent."
                            },
                            {
                                "targetVocab": "internal",
                                "prompt": "Dùng từ 'internal' để viết một câu về cách kiểm toán nội bộ giúp cải thiện quy trình doanh nghiệp. Ví dụ: The internal audit report recommended that the company implement a dual-signature requirement for all payments exceeding five hundred million dong."
                            },
                            {
                                "targetVocab": "external",
                                "prompt": "Dùng từ 'external' để viết một câu về yêu cầu kiểm toán bên ngoài đối với công ty niêm yết. Ví dụ: Vietnamese law requires all publicly listed companies to undergo an external audit every year, with the results published in the annual report for shareholders to review."
                            },
                            {
                                "targetVocab": "sampling",
                                "prompt": "Dùng từ 'sampling' để viết một câu về phương pháp lấy mẫu và độ tin cậy. Ví dụ: The auditors increased their sampling size from two hundred to five hundred transactions after the initial sample revealed an unusually high error rate in the expense records."
                            },
                            {
                                "targetVocab": "evidence",
                                "prompt": "Dùng từ 'evidence' để viết một câu về chất lượng bằng chứng kiểm toán. Ví dụ: The auditor considered the bank confirmation letter to be the most reliable piece of evidence because it came directly from an independent third party rather than from the company itself."
                            },
                            {
                                "targetVocab": "procedure",
                                "prompt": "Dùng từ 'procedure' để viết một câu về thủ tục kiểm toán cho một loại tài khoản cụ thể. Ví dụ: The standard audit procedure for verifying fixed assets required the team to physically inspect the equipment at each factory and compare serial numbers with the accounting records."
                            },
                            {
                                "targetVocab": "engagement",
                                "prompt": "Dùng từ 'engagement' để viết một câu về phạm vi và điều khoản của hợp đồng kiểm toán. Ví dụ: The engagement partner decided to assign additional staff to the audit after learning that the client had recently acquired two new subsidiaries with complex accounting structures."
                            },
                            {
                                "targetVocab": "fraud",
                                "prompt": "Dùng từ 'fraud' để viết một câu về một vụ gian lận tài chính và cách nó bị phát hiện. Ví dụ: The fraud was finally exposed when a whistleblower provided the auditors with internal emails showing that the sales director had instructed staff to backdate customer contracts."
                            },
                            {
                                "targetVocab": "detection",
                                "prompt": "Dùng từ 'detection' để viết một câu về công cụ hoặc phương pháp phát hiện gian lận. Ví dụ: The company invested in data analytics software to improve the detection of unusual patterns in financial transactions, such as payments to suppliers that only existed on paper."
                            },
                            {
                                "targetVocab": "disclosure",
                                "prompt": "Dùng từ 'disclosure' để viết một câu về tầm quan trọng của công bố thông tin đối với thị trường. Ví dụ: The stock exchange suspended trading in the company's shares after it was discovered that the annual report lacked proper disclosure of a pending lawsuit worth fifty billion dong."
                            },
                            {
                                "targetVocab": "independence",
                                "prompt": "Dùng từ 'independence' để viết một câu về quy định bảo vệ tính độc lập kiểm toán. Ví dụ: To protect auditor independence, Vietnamese regulations require that the lead audit partner be rotated every five years so that no single individual develops too close a relationship with the client."
                            },
                            {
                                "targetVocab": "objectivity",
                                "prompt": "Dùng từ 'objectivity' để viết một câu về thách thức trong việc duy trì tính khách quan. Ví dụ: The auditor's objectivity was challenged when the client offered to hire her husband as a consultant, creating a potential conflict of interest that had to be reported to the firm's ethics committee."
                            },
                            {
                                "targetVocab": "skepticism",
                                "prompt": "Dùng từ 'skepticism' để viết một câu về vai trò của thái độ hoài nghi trong phát hiện sai phạm. Ví dụ: The senior auditor's healthy skepticism led her to request original bank statements rather than accepting the photocopies provided by the client, which turned out to have been altered."
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
                    "description": "Giới thiệu bài đọc dài sử dụng toàn bộ 18 từ vựng về kiểm toán.",
                    "data": {
                        "text": (
                            "Chào mừng bạn đến với phần cuối cùng — bài đọc tổng hợp! "
                            "Bạn đã học và ôn tập 18 từ vựng qua ba phần trước. "
                            "Bây giờ, tất cả 18 từ sẽ xuất hiện trong một bài viết duy nhất, "
                            "kể câu chuyện hoàn chỉnh về kiểm toán — từ vai trò của kiểm toán viên, "
                            "quy trình thu thập bằng chứng, đến phát hiện gian lận và đạo đức nghề nghiệp.\n\n"
                            "Bạn sẽ gặp lại audit, compliance, assurance, material, misstatement, opinion "
                            "trong phần mở đầu về nền tảng của hệ thống kiểm toán. "
                            "Tiếp theo, internal, external, sampling, evidence, procedure, engagement "
                            "sẽ giúp bạn hiểu cách kiểm toán viên làm việc trong thực tế. "
                            "Và cuối cùng, fraud, detection, disclosure, independence, objectivity, skepticism "
                            "sẽ đưa bạn vào thế giới đạo đức nghề nghiệp và phòng chống gian lận.\n\n"
                            "Hãy đọc chậm, chú ý cách mỗi từ được sử dụng trong ngữ cảnh, "
                            "và thử đoán nghĩa trước khi nhìn lại định nghĩa. "
                            "Sau bài đọc, bạn sẽ viết một đoạn văn ngắn bằng tiếng Anh "
                            "để tổng hợp những gì đã học. Bắt đầu thôi!"
                        )
                    }
                },
                {
                    "activityType": "reading",
                    "title": "Đọc: Kiểm toán — Người gác cổng của sự minh bạch tài chính",
                    "description": "Picture yourself as a newly hired auditor at one of the Big Four accounting firms in Ho Chi Minh City.",
                    "data": {
                        "text": (
                            "Picture yourself as a newly hired auditor "
                            "at one of the Big Four accounting firms in Ho Chi Minh City. "
                            "Your first major assignment is the annual audit "
                            "of a Vietnamese manufacturing company listed on the stock exchange. "
                            "The company produces electronic components and exports them "
                            "to customers across Southeast Asia. "
                            "Your job is to determine whether the company's financial statements "
                            "can be trusted.\n\n"
                            "The process begins with the engagement. "
                            "Your firm signs an engagement letter with the client "
                            "that defines the scope of the audit, the timeline, "
                            "and the responsibilities of both parties. "
                            "The letter makes clear that the audit will provide reasonable assurance — "
                            "not absolute certainty — that the financial statements "
                            "are free from material misstatement. "
                            "This distinction is important: an audit reduces risk "
                            "but cannot eliminate it entirely.\n\n"
                            "Before the external audit begins, "
                            "you review the work of the company's internal audit department. "
                            "The internal team has already conducted its own review "
                            "of the company's controls and processes throughout the year. "
                            "Their reports show that they tested the purchasing approval process, "
                            "the inventory management system, and the revenue recognition policies. "
                            "While internal auditors work for the company, "
                            "their findings give you a useful starting point. "
                            "However, as an external auditor, you must form your own independent conclusions.\n\n"
                            "Your team begins gathering evidence. "
                            "For the cash accounts, the procedure involves sending confirmation letters "
                            "directly to the company's banks to verify the reported balances. "
                            "For inventory, you visit the main warehouse outside Ho Chi Minh City "
                            "and physically count a sample of the goods on the shelves. "
                            "For revenue, you select a sample of sales transactions "
                            "using statistical sampling and trace each one "
                            "from the customer order to the shipping document to the invoice. "
                            "Every piece of evidence is documented in the working papers.\n\n"
                            "During the sampling of revenue transactions, "
                            "you notice something unusual. "
                            "Several large sales were recorded on the last two days of the fiscal year, "
                            "but the shipping documents show that the goods "
                            "were not actually delivered until the following month. "
                            "This is a potential misstatement — "
                            "the company may have recognized revenue too early "
                            "to make its annual results look better. "
                            "You apply professional skepticism and dig deeper. "
                            "You request additional evidence: emails between the sales team and customers, "
                            "warehouse dispatch logs, and delivery confirmations.\n\n"
                            "The additional evidence confirms your suspicion. "
                            "The company recorded approximately eight billion dong in revenue "
                            "before the goods were actually delivered. "
                            "You must now determine whether this misstatement is material. "
                            "Your team had set the materiality threshold at five billion dong — "
                            "two percent of total revenue. "
                            "Since the misstatement exceeds this threshold, "
                            "it is clearly material and must be addressed.\n\n"
                            "You present your findings to the company's management. "
                            "They argue that the goods were ready for shipment "
                            "and that the delay was caused by a logistics problem, not by intent. "
                            "Your objectivity requires you to consider their explanation fairly, "
                            "but your skepticism also requires you to evaluate "
                            "whether the pattern suggests something more deliberate. "
                            "You check whether similar timing issues occurred in previous years "
                            "and find that they did — always at year-end, always inflating revenue.\n\n"
                            "This pattern raises concerns about possible fraud. "
                            "If management intentionally timed the recording of sales "
                            "to inflate year-end results, that would cross the line "
                            "from an accounting error to deliberate deception. "
                            "The detection of this pattern was only possible "
                            "because your team applied rigorous procedures "
                            "and maintained professional skepticism throughout the process.\n\n"
                            "You also review the company's disclosure notes. "
                            "Proper disclosure requires the company to explain "
                            "its revenue recognition policy and any significant judgments "
                            "that affect the financial statements. "
                            "You find that the existing disclosure is vague — "
                            "it does not mention the year-end timing issue "
                            "or the fact that some revenue was recognized before delivery. "
                            "You recommend that the company add a more detailed disclosure "
                            "so that investors can understand the situation.\n\n"
                            "Throughout this process, your independence is essential. "
                            "You have no financial interest in the company, "
                            "no personal relationship with its executives, "
                            "and no incentive to overlook problems. "
                            "Your firm's reputation depends on issuing honest opinions, "
                            "even when the findings are uncomfortable for the client.\n\n"
                            "You check the company's compliance with Vietnamese Accounting Standards "
                            "and International Financial Reporting Standards. "
                            "The early revenue recognition violates the standard "
                            "that requires revenue to be recorded only when control of goods "
                            "transfers to the customer. "
                            "This compliance failure must be included in your report.\n\n"
                            "After weeks of work, your team reaches a conclusion. "
                            "If the company corrects the revenue misstatement "
                            "and improves its disclosure, you can issue an unqualified opinion — "
                            "a clean opinion that tells investors the statements are reliable. "
                            "If the company refuses to make corrections, "
                            "you will issue a qualified opinion or, in the worst case, "
                            "an adverse opinion that warns investors "
                            "the statements cannot be trusted.\n\n"
                            "This is the power of the audit. "
                            "It is not just a technical exercise — "
                            "it is the mechanism that holds companies accountable "
                            "and gives investors the assurance they need "
                            "to make informed decisions. "
                            "Every procedure you performed, every piece of evidence you gathered, "
                            "and every judgment you made was guided by the same principles: "
                            "independence, objectivity, and skepticism."
                        )
                    }
                },
                {
                    "activityType": "speakReading",
                    "title": "Đọc: Kiểm toán — Người gác cổng của sự minh bạch tài chính",
                    "description": "Picture yourself as a newly hired auditor at one of the Big Four accounting firms in Ho Chi Minh City.",
                    "data": {
                        "text": (
                            "Picture yourself as a newly hired auditor "
                            "at one of the Big Four accounting firms in Ho Chi Minh City. "
                            "Your first major assignment is the annual audit "
                            "of a Vietnamese manufacturing company listed on the stock exchange. "
                            "The company produces electronic components and exports them "
                            "to customers across Southeast Asia. "
                            "Your job is to determine whether the company's financial statements "
                            "can be trusted.\n\n"
                            "The process begins with the engagement. "
                            "Your firm signs an engagement letter with the client "
                            "that defines the scope of the audit, the timeline, "
                            "and the responsibilities of both parties. "
                            "The letter makes clear that the audit will provide reasonable assurance — "
                            "not absolute certainty — that the financial statements "
                            "are free from material misstatement. "
                            "This distinction is important: an audit reduces risk "
                            "but cannot eliminate it entirely.\n\n"
                            "Before the external audit begins, "
                            "you review the work of the company's internal audit department. "
                            "The internal team has already conducted its own review "
                            "of the company's controls and processes throughout the year. "
                            "Their reports show that they tested the purchasing approval process, "
                            "the inventory management system, and the revenue recognition policies. "
                            "While internal auditors work for the company, "
                            "their findings give you a useful starting point. "
                            "However, as an external auditor, you must form your own independent conclusions.\n\n"
                            "Your team begins gathering evidence. "
                            "For the cash accounts, the procedure involves sending confirmation letters "
                            "directly to the company's banks to verify the reported balances. "
                            "For inventory, you visit the main warehouse outside Ho Chi Minh City "
                            "and physically count a sample of the goods on the shelves. "
                            "For revenue, you select a sample of sales transactions "
                            "using statistical sampling and trace each one "
                            "from the customer order to the shipping document to the invoice. "
                            "Every piece of evidence is documented in the working papers.\n\n"
                            "During the sampling of revenue transactions, "
                            "you notice something unusual. "
                            "Several large sales were recorded on the last two days of the fiscal year, "
                            "but the shipping documents show that the goods "
                            "were not actually delivered until the following month. "
                            "This is a potential misstatement — "
                            "the company may have recognized revenue too early "
                            "to make its annual results look better. "
                            "You apply professional skepticism and dig deeper. "
                            "You request additional evidence: emails between the sales team and customers, "
                            "warehouse dispatch logs, and delivery confirmations.\n\n"
                            "The additional evidence confirms your suspicion. "
                            "The company recorded approximately eight billion dong in revenue "
                            "before the goods were actually delivered. "
                            "You must now determine whether this misstatement is material. "
                            "Your team had set the materiality threshold at five billion dong — "
                            "two percent of total revenue. "
                            "Since the misstatement exceeds this threshold, "
                            "it is clearly material and must be addressed.\n\n"
                            "You present your findings to the company's management. "
                            "They argue that the goods were ready for shipment "
                            "and that the delay was caused by a logistics problem, not by intent. "
                            "Your objectivity requires you to consider their explanation fairly, "
                            "but your skepticism also requires you to evaluate "
                            "whether the pattern suggests something more deliberate. "
                            "You check whether similar timing issues occurred in previous years "
                            "and find that they did — always at year-end, always inflating revenue.\n\n"
                            "This pattern raises concerns about possible fraud. "
                            "If management intentionally timed the recording of sales "
                            "to inflate year-end results, that would cross the line "
                            "from an accounting error to deliberate deception. "
                            "The detection of this pattern was only possible "
                            "because your team applied rigorous procedures "
                            "and maintained professional skepticism throughout the process.\n\n"
                            "You also review the company's disclosure notes. "
                            "Proper disclosure requires the company to explain "
                            "its revenue recognition policy and any significant judgments "
                            "that affect the financial statements. "
                            "You find that the existing disclosure is vague — "
                            "it does not mention the year-end timing issue "
                            "or the fact that some revenue was recognized before delivery. "
                            "You recommend that the company add a more detailed disclosure "
                            "so that investors can understand the situation.\n\n"
                            "Throughout this process, your independence is essential. "
                            "You have no financial interest in the company, "
                            "no personal relationship with its executives, "
                            "and no incentive to overlook problems. "
                            "Your firm's reputation depends on issuing honest opinions, "
                            "even when the findings are uncomfortable for the client.\n\n"
                            "You check the company's compliance with Vietnamese Accounting Standards "
                            "and International Financial Reporting Standards. "
                            "The early revenue recognition violates the standard "
                            "that requires revenue to be recorded only when control of goods "
                            "transfers to the customer. "
                            "This compliance failure must be included in your report.\n\n"
                            "After weeks of work, your team reaches a conclusion. "
                            "If the company corrects the revenue misstatement "
                            "and improves its disclosure, you can issue an unqualified opinion — "
                            "a clean opinion that tells investors the statements are reliable. "
                            "If the company refuses to make corrections, "
                            "you will issue a qualified opinion or, in the worst case, "
                            "an adverse opinion that warns investors "
                            "the statements cannot be trusted.\n\n"
                            "This is the power of the audit. "
                            "It is not just a technical exercise — "
                            "it is the mechanism that holds companies accountable "
                            "and gives investors the assurance they need "
                            "to make informed decisions. "
                            "Every procedure you performed, every piece of evidence you gathered, "
                            "and every judgment you made was guided by the same principles: "
                            "independence, objectivity, and skepticism."
                        )
                    }
                },
                {
                    "activityType": "readAlong",
                    "title": "Nghe: Kiểm toán — Người gác cổng của sự minh bạch tài chính",
                    "description": "Nghe đoạn văn vừa đọc và theo dõi.",
                    "data": {
                        "text": (
                            "Picture yourself as a newly hired auditor "
                            "at one of the Big Four accounting firms in Ho Chi Minh City. "
                            "Your first major assignment is the annual audit "
                            "of a Vietnamese manufacturing company listed on the stock exchange. "
                            "The company produces electronic components and exports them "
                            "to customers across Southeast Asia. "
                            "Your job is to determine whether the company's financial statements "
                            "can be trusted.\n\n"
                            "The process begins with the engagement. "
                            "Your firm signs an engagement letter with the client "
                            "that defines the scope of the audit, the timeline, "
                            "and the responsibilities of both parties. "
                            "The letter makes clear that the audit will provide reasonable assurance — "
                            "not absolute certainty — that the financial statements "
                            "are free from material misstatement. "
                            "This distinction is important: an audit reduces risk "
                            "but cannot eliminate it entirely.\n\n"
                            "Before the external audit begins, "
                            "you review the work of the company's internal audit department. "
                            "The internal team has already conducted its own review "
                            "of the company's controls and processes throughout the year. "
                            "Their reports show that they tested the purchasing approval process, "
                            "the inventory management system, and the revenue recognition policies. "
                            "While internal auditors work for the company, "
                            "their findings give you a useful starting point. "
                            "However, as an external auditor, you must form your own independent conclusions.\n\n"
                            "Your team begins gathering evidence. "
                            "For the cash accounts, the procedure involves sending confirmation letters "
                            "directly to the company's banks to verify the reported balances. "
                            "For inventory, you visit the main warehouse outside Ho Chi Minh City "
                            "and physically count a sample of the goods on the shelves. "
                            "For revenue, you select a sample of sales transactions "
                            "using statistical sampling and trace each one "
                            "from the customer order to the shipping document to the invoice. "
                            "Every piece of evidence is documented in the working papers.\n\n"
                            "During the sampling of revenue transactions, "
                            "you notice something unusual. "
                            "Several large sales were recorded on the last two days of the fiscal year, "
                            "but the shipping documents show that the goods "
                            "were not actually delivered until the following month. "
                            "This is a potential misstatement — "
                            "the company may have recognized revenue too early "
                            "to make its annual results look better. "
                            "You apply professional skepticism and dig deeper. "
                            "You request additional evidence: emails between the sales team and customers, "
                            "warehouse dispatch logs, and delivery confirmations.\n\n"
                            "The additional evidence confirms your suspicion. "
                            "The company recorded approximately eight billion dong in revenue "
                            "before the goods were actually delivered. "
                            "You must now determine whether this misstatement is material. "
                            "Your team had set the materiality threshold at five billion dong — "
                            "two percent of total revenue. "
                            "Since the misstatement exceeds this threshold, "
                            "it is clearly material and must be addressed.\n\n"
                            "You present your findings to the company's management. "
                            "They argue that the goods were ready for shipment "
                            "and that the delay was caused by a logistics problem, not by intent. "
                            "Your objectivity requires you to consider their explanation fairly, "
                            "but your skepticism also requires you to evaluate "
                            "whether the pattern suggests something more deliberate. "
                            "You check whether similar timing issues occurred in previous years "
                            "and find that they did — always at year-end, always inflating revenue.\n\n"
                            "This pattern raises concerns about possible fraud. "
                            "If management intentionally timed the recording of sales "
                            "to inflate year-end results, that would cross the line "
                            "from an accounting error to deliberate deception. "
                            "The detection of this pattern was only possible "
                            "because your team applied rigorous procedures "
                            "and maintained professional skepticism throughout the process.\n\n"
                            "You also review the company's disclosure notes. "
                            "Proper disclosure requires the company to explain "
                            "its revenue recognition policy and any significant judgments "
                            "that affect the financial statements. "
                            "You find that the existing disclosure is vague — "
                            "it does not mention the year-end timing issue "
                            "or the fact that some revenue was recognized before delivery. "
                            "You recommend that the company add a more detailed disclosure "
                            "so that investors can understand the situation.\n\n"
                            "Throughout this process, your independence is essential. "
                            "You have no financial interest in the company, "
                            "no personal relationship with its executives, "
                            "and no incentive to overlook problems. "
                            "Your firm's reputation depends on issuing honest opinions, "
                            "even when the findings are uncomfortable for the client.\n\n"
                            "You check the company's compliance with Vietnamese Accounting Standards "
                            "and International Financial Reporting Standards. "
                            "The early revenue recognition violates the standard "
                            "that requires revenue to be recorded only when control of goods "
                            "transfers to the customer. "
                            "This compliance failure must be included in your report.\n\n"
                            "After weeks of work, your team reaches a conclusion. "
                            "If the company corrects the revenue misstatement "
                            "and improves its disclosure, you can issue an unqualified opinion — "
                            "a clean opinion that tells investors the statements are reliable. "
                            "If the company refuses to make corrections, "
                            "you will issue a qualified opinion or, in the worst case, "
                            "an adverse opinion that warns investors "
                            "the statements cannot be trusted.\n\n"
                            "This is the power of the audit. "
                            "It is not just a technical exercise — "
                            "it is the mechanism that holds companies accountable "
                            "and gives investors the assurance they need "
                            "to make informed decisions. "
                            "Every procedure you performed, every piece of evidence you gathered, "
                            "and every judgment you made was guided by the same principles: "
                            "independence, objectivity, and skepticism."
                        )
                    }
                },
                {
                    "activityType": "writingParagraph",
                    "title": "Viết: Phân tích quy trình kiểm toán",
                    "description": "Viết đoạn văn tiếng Anh phân tích quy trình kiểm toán sử dụng 18 từ vựng đã học.",
                    "data": {
                        "vocabList": ALL_WORDS,
                        "instructions": "Viết một đoạn văn bằng tiếng Anh (khoảng 100-150 từ) phân tích một khía cạnh của kiểm toán. Sử dụng ít nhất 8 từ vựng từ danh sách. Bạn có thể chọn một trong hai đề bài dưới đây.",
                        "prompts": [
                            "Hãy mô tả quy trình kiểm toán từ đầu đến cuối cho một công ty niêm yết tại Việt Nam. Giải thích vai trò của engagement letter, sự khác biệt giữa internal và external audit, cách auditor thu thập evidence thông qua sampling và procedure, và tại sao assurance chỉ ở mức hợp lý chứ không tuyệt đối.",
                            "Hãy phân tích tầm quan trọng của đạo đức nghề nghiệp trong kiểm toán. Giải thích vì sao independence, objectivity và skepticism là nền tảng của nghề kiểm toán, cách chúng giúp phát hiện fraud và misstatement, và hậu quả khi kiểm toán viên thiếu những phẩm chất này đối với disclosure và compliance."
                        ]
                    }
                },
                {
                    "activityType": "introAudio",
                    "title": "Lời kết",
                    "description": "Ôn lại từ vựng quan trọng và lời chia tay với tinh thần trách nhiệm ấm áp.",
                    "data": {
                        "text": (
                            "Bạn vừa hoàn thành bài học về Kiểm toán. "
                            "Và bây giờ, mình muốn thách thức bạn một chút: "
                            "18 từ vựng này không chỉ để thi — chúng là công cụ thực sự "
                            "mà bạn sẽ dùng trong sự nghiệp. Hãy cùng ôn lại "
                            "và nghĩ xem bạn sẽ áp dụng chúng ở đâu.\n\n"
                            "Audit — kiểm toán. Đây là từ bạn sẽ nghe nhiều nhất "
                            "nếu bạn bước vào ngành kế toán hay tài chính. "
                            "Mỗi năm, hàng nghìn cuộc kiểm toán diễn ra tại Việt Nam, "
                            "và mỗi cuộc kiểm toán đều cần người hiểu ngôn ngữ này. "
                            "Ví dụ mới: The company voluntarily requested an early audit "
                            "of its quarterly results to reassure nervous investors "
                            "after a competitor was caught falsifying its financial reports.\n\n"
                            "Evidence — bằng chứng. Trong kiểm toán, không có gì được chấp nhận "
                            "nếu không có bằng chứng. Lời nói của ban giám đốc không đủ — "
                            "kiểm toán viên cần tài liệu, xác nhận từ bên thứ ba, "
                            "và kiểm tra thực tế. Bạn có thể áp dụng tư duy này "
                            "vào mọi lĩnh vực: luôn hỏi 'bằng chứng ở đâu?' "
                            "Ví dụ mới: The audit team spent two days at the port "
                            "collecting evidence that the exported goods matched "
                            "the quantities recorded in the company's shipping documents.\n\n"
                            "Skepticism — thái độ hoài nghi nghề nghiệp. "
                            "Đây có lẽ là phẩm chất quan trọng nhất mà bạn học hôm nay. "
                            "Skepticism không phải là nghi ngờ mọi thứ — "
                            "mà là không bao giờ chấp nhận câu trả lời mà không kiểm chứng. "
                            "Trong phòng vấn tại Big Four, nếu bạn nói được về professional skepticism "
                            "bằng tiếng Anh, bạn đã ghi điểm rồi. "
                            "Ví dụ mới: The auditor's skepticism was justified "
                            "when she discovered that the supplier invoices "
                            "had been printed on the same printer as the company's internal documents, "
                            "suggesting they were fabricated.\n\n"
                            "Independence — tính độc lập. Không có independence, "
                            "kiểm toán chỉ là hình thức. Khi bạn đọc báo cáo kiểm toán, "
                            "hãy luôn hỏi: kiểm toán viên này có thực sự độc lập không? "
                            "Ví dụ mới: The firm declined a lucrative consulting contract "
                            "with the client to preserve its independence "
                            "and avoid any appearance of conflict of interest "
                            "during the upcoming annual audit.\n\n"
                            "Fraud — gian lận. Từ này nghe nặng nề, "
                            "nhưng nó là thực tế mà mọi kiểm toán viên phải đối mặt. "
                            "Gian lận tài chính không chỉ xảy ra ở nước ngoài — "
                            "Việt Nam cũng có những vụ việc đình đám. "
                            "Hiểu fraud bằng tiếng Anh giúp bạn đọc được "
                            "các báo cáo điều tra quốc tế và case study trong sách giáo khoa. "
                            "Ví dụ mới: The fraud investigation revealed "
                            "that the former CFO had created a network of shell companies "
                            "to siphon funds from the parent company over a period of six years.\n\n"
                            "Disclosure — công bố thông tin. Minh bạch là nền tảng "
                            "của mọi thị trường tài chính lành mạnh. "
                            "Khi bạn đọc báo cáo thường niên, đừng chỉ nhìn con số — "
                            "hãy đọc cả phần disclosure notes, vì đó là nơi "
                            "những câu chuyện thật sự được kể. "
                            "Ví dụ mới: The improved disclosure in this year's annual report "
                            "included a detailed breakdown of related-party transactions "
                            "that had previously been hidden in a single line item.\n\n"
                            "Bạn biết không, kiểm toán không chỉ là nghề — "
                            "nó là trách nhiệm. Mỗi kiểm toán viên đứng giữa "
                            "doanh nghiệp và nhà đầu tư, giữa con số và sự thật. "
                            "Và bây giờ, bạn đã có ngôn ngữ để tham gia cuộc đối thoại đó.\n\n"
                            "Mình thách thức bạn: tuần này, hãy mở một báo cáo kiểm toán "
                            "bằng tiếng Anh — của bất kỳ công ty nào trên sàn chứng khoán — "
                            "và thử đọc phần auditor's opinion. "
                            "Bạn sẽ ngạc nhiên khi thấy mình hiểu được bao nhiêu. "
                            "Đó là bằng chứng tốt nhất rằng 18 từ vựng này đã thay đổi cách bạn đọc. "
                            "Chúc bạn tiếp tục hành trình — hẹn gặp lại ở bài học tiếp theo!"
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
print(f"SELECT id, title, created_at FROM curriculum WHERE title = 'Auditing – Kiểm Toán' AND uid = '{UID}' ORDER BY created_at;")
