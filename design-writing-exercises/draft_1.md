# Draft 1 – Bài tập viết: Buổi 1 – Healthspan vs. Lifespan

## Mục tiêu
Học viên sử dụng 6 từ vựng buổi 1 (**lifespan, healthspan, longevity, chronic disease, vitality, mortality**) trong các bài viết ngắn, từ mức câu đơn đến đoạn văn ngắn.

---

## Bài tập 1A – Viết câu với từ vựng mục tiêu

Viết câu tiếng Anh sử dụng từ vựng mục tiêu buổi 1. Mỗi từ có câu ví dụ tiếng Việt để gợi ý.

1. 🎯 **lifespan**
   > Tuổi thọ trung bình của con người đã tăng từ 40 lên 75 tuổi trong thế kỷ qua.
   → _______________________________________________

2. 🎯 **healthspan**
   > Bà tôi sống đến 92 tuổi, nhưng tuổi thọ khỏe mạnh của bà kết thúc vào khoảng 70 tuổi khi bà không còn tự đi lại được.
   → _______________________________________________

3. 🎯 **longevity**
   > Trường thọ không chỉ là đếm số năm sống — mà là cách bạn sống những năm đó.
   → _______________________________________________

4. 🎯 **chronic disease**
   > Bệnh tim và tiểu đường là những ví dụ về bệnh mãn tính phát triển chậm qua hàng thập kỷ.
   → _______________________________________________

5. 🎯 **vitality**
   > Dù đã 80 tuổi, bà ấy vẫn tràn đầy sức sống — bà làm vườn, nấu ăn, và đi bộ mỗi sáng.
   → _______________________________________________

6. 🎯 **mortality**
   > Vắc-xin đã giảm đáng kể tỷ lệ tử vong ở trẻ sơ sinh trên toàn thế giới.
   → _______________________________________________

---

## Bài tập 1B – Viết đoạn văn ngắn

Viết đoạn văn 4-6 câu sử dụng ít nhất 4 trong 6 từ vựng buổi 1

### Đề 1:
> Describe someone you know (or have heard of) who lived a long life. Did they have a long lifespan, a long healthspan, or both? What was the difference?

### Đề 2:
> Do you think people today focus more on lifespan or healthspan? Why?

---

## Tiêu chí tự đánh giá

| Tiêu chí | ✅ Đạt | ⬜ Cần cải thiện |
|---|---|---|
| Sử dụng đúng ít nhất 4/6 từ vựng | | |
| Từ vựng được dùng đúng ngữ cảnh | | |
| Câu có cấu trúc ngữ pháp rõ ràng | | |
| Đoạn văn có ý chính và logic mạch lạc | | |

---

## Ví dụ JSON – Tích hợp vào curriculum

Dưới đây là ví dụ cách các bài tập viết trên có thể được biểu diễn dưới dạng activity JSON, tương thích với cấu trúc `learningSessions[].activities[]` trong curriculum hiện tại. Đặt các activity này vào cuối mảng `activities` của Buổi 1.

```json
[
    {
        "activityType": "writingSentence",
        "title": "Viết câu với từ vựng mục tiêu",
        "description": "Viết câu tiếng Anh sử dụng từ vựng mục tiêu buổi 1: lifespan, healthspan, longevity, chronic disease, vitality.",
        "practiceMinutes": 8,
        "data": {
            "vocabList": ["lifespan", "healthspan", "longevity", "chronic disease", "vitality", "mortality"],
            "items": [
                {
                    "targetVocab": "lifespan",
                    "prompt": "Sử dụng từ 'lifespan' để nói về tuổi thọ con người. Ví dụ: Tuổi thọ trung bình của con người đã tăng từ 40 lên 75 tuổi trong thế kỷ qua."
                },
                {
                    "targetVocab": "healthspan",
                    "prompt": "Sử dụng từ 'healthspan' để nói về việc bảo vệ tuổi thọ khỏe mạnh. Ví dụ: Bà tôi sống đến 92 tuổi, nhưng tuổi thọ khỏe mạnh của bà kết thúc vào khoảng 70 tuổi khi bà không còn tự đi lại được."
                },
                {
                    "targetVocab": "longevity",
                    "prompt": "Sử dụng từ 'longevity' để nói về sự trường thọ và chất lượng cuộc sống. Ví dụ: Trường thọ không chỉ là đếm số năm sống — mà là cách bạn sống những năm đó."
                },
                {
                    "targetVocab": "chronic disease",
                    "prompt": "Sử dụng từ 'chronic disease' để nói về các bệnh mãn tính phổ biến. Ví dụ: Bệnh tim và tiểu đường là những ví dụ về bệnh mãn tính phát triển chậm qua hàng thập kỷ."
                },
                {
                    "targetVocab": "vitality",
                    "prompt": "Sử dụng từ 'vitality' để nói về sức sống và năng lượng. Ví dụ: Dù đã 80 tuổi, bà ấy vẫn tràn đầy sức sống — bà làm vườn, nấu ăn, và đi bộ mỗi sáng."
                },
                {
                    "targetVocab": "mortality",
                    "prompt": "Sử dụng từ 'mortality' để nói về tỷ lệ tử vong. Ví dụ: Vắc-xin đã giảm đáng kể tỷ lệ tử vong ở trẻ sơ sinh trên toàn thế giới."
                }
            ]
        }
    },
    {
        "activityType": "writingParagraph",
        "title": "Viết đoạn văn ngắn",
        "description": "Viết đoạn văn 4-6 câu sử dụng ít nhất 4 trong 6 từ vựng buổi 1",
        "practiceMinutes": 10,
        "data": {
            "prompt": "Chọn một trong các đề bài sau. Viết 4-6 câu bằng tiếng Anh. Sử dụng ít nhất 4 trong 6 từ vựng đã học.",
            "vocabList": ["lifespan", "healthspan", "longevity", "chronic disease", "vitality", "mortality"],
            "prompts": [
                "Describe someone you know (or have heard of) who lived a long life. Did they have a long lifespan, a long healthspan, or both? What was the difference?",
                "Do you think people today focus more on lifespan or healthspan? Why?"
            ],
            "rubric": [
                "Correctly uses at least 4 out of 6 vocabulary words",
                "Vocabulary is used in appropriate context",
                "Sentences have clear grammatical structure",
                "Paragraph has a clear main idea and logical coherence"
            ]
        }
    }
]
```
