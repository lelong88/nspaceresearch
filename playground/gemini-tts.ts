// Gemini 2.5 Pro TTS - text-to-speech with bilingual support
import { execSync } from "child_process";
import { writeFileSync } from "fs";

const GEMINI_API_KEY = process.env.GEMINI_API_KEY;
const text = `Read this text naturally, speaking Vietnamese and Chinese words in their original languages:
Chào bạn! Chào mừng đến với bài học 'Câu chuyện về lòng tử tế'. Trong buổi đầu tiên này, chúng ta sẽ bắt đầu với tình huống khẩn cấp khi nhân vật chính nhận tin con bị bệnh nặng (严重). Anh ấy phải vay tiền và vội vã đi trong đêm. Hãy cùng học những từ vựng đầu tiên để hiểu rõ hoàn cảnh này nhé! Bắt đầu thôi (开始)!`;

async function main() {
  const res = await fetch(
    `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro-preview-tts:generateContent?key=${GEMINI_API_KEY}`,
    {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        contents: [{ parts: [{ text }] }],
        generationConfig: {
          responseModalities: ["AUDIO"],
          speechConfig: { voiceConfig: { prebuiltVoiceConfig: { voiceName: "Kore" } } },
        },
      }),
    }
  );

  const json = await res.json();
  if (json.error) return console.error("Error:", json.error.message);

  const audioData = json.candidates?.[0]?.content?.parts?.[0]?.inlineData?.data;
  if (!audioData) return console.log("No audio data received");

  writeFileSync("gemini-output.pcm", Buffer.from(audioData, "base64"));
  execSync("ffmpeg -y -f s16le -ar 24000 -ac 1 -i gemini-output.pcm gemini-output.mp3 2>/dev/null");
  console.log("Audio saved to gemini-output.mp3");
}

main();
