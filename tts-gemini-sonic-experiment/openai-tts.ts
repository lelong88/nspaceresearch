// OpenAI gpt-4o-mini-tts - text-to-speech with bilingual support
import { writeFileSync } from "fs";
import { config } from "dotenv";
config();

const OPENAI_API_KEY = process.env.OPENAI_API_KEY;
const text = `Read this text naturally, speaking Vietnamese and Chinese words in their original languages:
Chào bạn! Chào mừng đến với bài học 'Câu chuyện về lòng tử tế'. Trong buổi đầu tiên này, chúng ta sẽ bắt đầu với tình huống khẩn cấp khi nhân vật chính nhận tin con bị bệnh nặng (严重). Anh ấy phải vay tiền và vội vã đi trong đêm. Hãy cùng học những từ vựng đầu tiên để hiểu rõ hoàn cảnh này nhé! Bắt đầu thôi (开始)!`;

async function main() {
  const res = await fetch("https://api.openai.com/v1/audio/speech", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${OPENAI_API_KEY}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: "gpt-4o-mini-tts",
      input: text,
      voice: "alloy",
      response_format: "mp3",
    }),
  });

  if (!res.ok) {
    const err = await res.json();
    return console.error("Error:", err.error?.message || res.statusText);
  }

  const buffer = Buffer.from(await res.arrayBuffer());
  writeFileSync("openai-output.mp3", buffer);
  console.log("Audio saved to openai-output.mp3");
}

main();
