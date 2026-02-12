// Nova 2 Sonic TTS via crossmodal text input
// NOTE: Bilingual (Mandarin-English) quality is poor - model struggles with code-switching
// Consider Gemini 2.5 Pro TTS for better multilingual results

import { BedrockRuntimeClient, InvokeModelWithBidirectionalStreamCommand } from "@aws-sdk/client-bedrock-runtime";
import { writeFileSync } from "fs";
import { execSync } from "child_process";

const client = new BedrockRuntimeClient({ region: "us-east-1" });
const promptName = crypto.randomUUID();
const systemContentName = crypto.randomUUID();
const audioContentName = crypto.randomUUID();
const textContentName = crypto.randomUUID();
const encoder = new TextEncoder();
const decoder = new TextDecoder();

const userText = "Read this mixed language text naturally: Hello, hôm nay trời đẹp quá! I'm learning tiếng Việt, it's very thú vị. Let's go eat phở tonight!";
const silentChunk = Buffer.alloc(2048).toString("base64");

async function main() {
  const audioChunks: Buffer[] = [];
  let gotResponse = false;
  let silentCount = 0;

  async function* generateChunks(): AsyncGenerator<{ chunk: { bytes: Uint8Array } }> {
    const send = (e: object) => ({ chunk: { bytes: encoder.encode(JSON.stringify(e)) } });
    const delay = (ms: number) => new Promise(r => setTimeout(r, ms));

    // Session and prompt start
    yield send({ event: { sessionStart: { inferenceConfiguration: { maxTokens: 1024, topP: 0.9, temperature: 0.7 } } } });
    yield send({ event: { promptStart: { promptName, textOutputConfiguration: { mediaType: "text/plain" }, audioOutputConfiguration: { mediaType: "audio/lpcm", sampleRateHertz: 24000, sampleSizeBits: 16, channelCount: 1, voiceId: "tiffany", encoding: "base64", audioType: "SPEECH" } } } });

    // System prompt
    yield send({ event: { contentStart: { promptName, contentName: systemContentName, type: "TEXT", interactive: false, role: "SYSTEM", textInputConfiguration: { mediaType: "text/plain" } } } });
    yield send({ event: { textInput: { promptName, contentName: systemContentName, content: "You are a bilingual assistant. When reading mixed language text, speak each language in its original form - speak Chinese words in Chinese and English words in English. Do not translate. Preserve the code-switching exactly as written." } } });
    yield send({ event: { contentEnd: { promptName, contentName: systemContentName } } });

    // Audio stream start
    yield send({ event: { contentStart: { promptName, contentName: audioContentName, type: "AUDIO", interactive: true, role: "USER", audioInputConfiguration: { mediaType: "audio/lpcm", sampleRateHertz: 16000, sampleSizeBits: 16, channelCount: 1, audioType: "SPEECH", encoding: "base64" } } } });

    // Initial silent audio
    for (let i = 0; i < 3; i++) {
      yield send({ event: { audioInput: { promptName, contentName: audioContentName, content: silentChunk } } });
      await delay(20);
    }

    // Crossmodal text input
    yield send({ event: { contentStart: { promptName, contentName: textContentName, role: "USER", type: "TEXT", interactive: true, textInputConfiguration: { mediaType: "text/plain" } } } });
    yield send({ event: { textInput: { promptName, contentName: textContentName, content: userText } } });
    yield send({ event: { contentEnd: { promptName, contentName: textContentName } } });

    // Keep sending silent audio until response received
    while (!gotResponse && silentCount < 200) {
      yield send({ event: { audioInput: { promptName, contentName: audioContentName, content: silentChunk } } });
      silentCount++;
      await delay(50);
    }

    // End session
    yield send({ event: { contentEnd: { promptName, contentName: audioContentName } } });
    yield send({ event: { promptEnd: { promptName } } });
    yield send({ event: { sessionEnd: {} } });
  }

  const command = new InvokeModelWithBidirectionalStreamCommand({
    modelId: "amazon.nova-2-sonic-v1:0",
    body: generateChunks(),
  });

  console.log("Sending request to Nova 2 Sonic...");
  const response = await client.send(command);

  for await (const event of response.body!) {
    if (event.chunk?.bytes) {
      const json = JSON.parse(decoder.decode(event.chunk.bytes));
      if (json.event?.textOutput) console.log("Text:", json.event.textOutput.content);
      if (json.event?.audioOutput?.content) audioChunks.push(Buffer.from(json.event.audioOutput.content, "base64"));
      if (json.event?.completionEnd) gotResponse = true;
    }
  }

  if (audioChunks.length === 0) return console.log("No audio received");

  writeFileSync("output.pcm", Buffer.concat(audioChunks));
  execSync("ffmpeg -y -f s16le -ar 24000 -ac 1 -i output.pcm output.mp3 2>/dev/null");
  console.log(`Audio saved to output.mp3 (${audioChunks.length} chunks)`);
}

main().catch(console.error);
