import sounddevice as sd
from kokoro_onnx import Kokoro

VOICE = "am_echo"
SPEED = 1.0

kokoro = Kokoro("kokoro-v1.0.onnx", "voices-v1.0.bin")

def speak(text):
    samples, sample_rate = kokoro.create(text, voice=VOICE, speed=SPEED, lang="en-us")
    sd.play(samples, sample_rate)
    sd.wait()

if __name__ == "__main__":
    speak("Yo Triston, it's Travis. New voice, who dis?")