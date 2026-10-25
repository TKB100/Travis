import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

SAMPLE_RATE = 16000
SECONDS = 3
NUM_SAMPLES = SAMPLE_RATE * SECONDS
model = WhisperModel("small.en", device="cpu", compute_type="int8")


def listening():
    print("Recording now.....")
    recording = sd.rec(NUM_SAMPLES, samplerate=SAMPLE_RATE, channels=1)
    sd.wait()
    print("Recording is done.")

    loudness = np.abs(recording).max()
    if loudness < 0.02:
        print("No audio came through")
        return ""

    audio = recording.flatten()
    segments, info = model.transcribe(audio)

    text = ""
    for segment in segments:
        text += segment.text

    return text.strip()

if __name__ == "__main__":
    result = listening()
    print("You said:", result)


