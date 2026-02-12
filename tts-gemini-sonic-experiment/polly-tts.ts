// Amazon Polly TTS - for text-to-speech without audio input
// Nova Sonic requires speech input (it's speech-to-speech, not text-to-speech)

import { PollyClient, SynthesizeSpeechCommand } from "@aws-sdk/client-polly";
import { writeFileSync } from "fs";
import { Readable } from "stream";

const client = new PollyClient({ region: "us-east-1" });

async function main() {
  const command = new SynthesizeSpeechCommand({
    Text: "Hello! This is Amazon Polly generating speech from text.",
    OutputFormat: "mp3",
    VoiceId: "Matthew",
    Engine: "neural",
  });

  const response = await client.send(command);
  const chunks: Buffer[] = [];
  
  for await (const chunk of response.AudioStream as Readable) {
    chunks.push(chunk);
  }

  writeFileSync("output.mp3", Buffer.concat(chunks));
  console.log("Audio saved to output.mp3");
}

main().catch(console.error);
