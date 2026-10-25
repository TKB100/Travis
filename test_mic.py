import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

SAMPLE_RATE = 16000
SECONDS = 3
NUM_SAMPLES = SAMPLE_RATE * SECONDS
model = WhisperModel("small.en", device="cpu", compute_type="int8")

print("Recording now.....")
recording = sd.rec(NUM_SAMPLES, samplerate=SAMPLE_RATE, channels=1)
sd.wait()
loudness = np.abs(recording).max()
print("Recording is done.")
audio = recording.flatten()
segments, info = model.transcribe(audio)
for segment in segments:
    print(segment.text)


