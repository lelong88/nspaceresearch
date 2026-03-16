"""Final rewrite — vi-en curriculums that still use compressed style."""

import sys
import json
import requests

sys.path.insert(0, "/home/ubuntu/nspaceresearch/design-curriculums")
from firebase_token import get_firebase_id_token

UID = "zs5AMpVfqkcfDf8CJ9qrXdH58d73"
BASE_URL = "https://helloapi.step.is/curriculum"

rewrites = {
    "5OJgQ49zI8skRPfX": {
        "title": "Decide Your Destiny",
        "new": (
            "TẠI SAO BẠN NỖ LỰC NHƯNG VẪN THẤY MÔNG LUNG?\n\n"
            "Mọi quyết định bạn đưa ra — từ việc chọn việc làm đến người bạn yêu "
            "— đều bị chi phối bởi ba \"nút điều khiển\" ngầm: bạn tập trung vào đâu, "
            "bạn gán ý nghĩa gì cho nó, và bạn hành động ra sao.\n\n"
            "Hầu hết mọi người vận hành ba nút này một cách vô thức — rồi thắc mắc "
            "tại sao cuộc đời cứ trôi theo hoàn cảnh thay vì theo ý mình.\n\n"
            "Khám phá cách làm chủ ba quyết định định hình số phận, và xây dựng "
            "hệ thống giá trị cá nhân như la bàn dẫn đường cho mọi lựa chọn.\n\n"
            "Học 18 từ vựng đắt giá giúp bạn vừa nâng cấp tư duy về quyết định, "
            "vừa nâng trình tiếng Anh một cách vượt bậc."
        )
    },
    "eI92kJ5GYlDjRzhM": {
        "title": "Disagree and Commit",
        "new": (
            "BẠN CÓ DÁM NÓI THẲNG VỚI SẾP RẰNG SẾP SAI KHÔNG?\n\n"
            "Trong những đội nhóm xuất sắc nhất thế giới, bất đồng ý kiến không phải "
            "là vấn đề — nó là nhiên liệu. Vấn đề thực sự là khi mọi người gật đầu "
            "cho qua rồi âm thầm phá hoại.\n\n"
            "Nguyên tắc \"Disagree and Commit\" dạy bạn cách tranh luận thẳng thắn, "
            "ra quyết định dứt khoát, rồi cam kết hành động 100% — dù bạn không hoàn "
            "toàn đồng ý. Đó là nghệ thuật biến bất đồng thành sức mạnh.\n\n"
            "Học 18 từ vựng tiếng Anh đắt giá giúp bạn vừa nâng cấp kỹ năng làm việc "
            "nhóm, vừa tự tin tranh luận bằng tiếng Anh trong môi trường quốc tế."
        )
    },
}
