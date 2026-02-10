import speech_recognition as sr
import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()

# ===============================
# STEP 1: Speech to Text
# ===============================
r = sr.Recognizer()

try:
    with sr.AudioFile("audio.wav") as source:
        audio = r.record(source)

    text = r.recognize_google(audio)
    print("🎤 Recognized Text:", text)

except Exception as e:
    print("❌ Speech recognition failed:", e)
    sys.exit()

prompt = text
print("📝 Final Prompt for Image:", prompt)

# ===============================
# STEP 2: Image Generation (HF)
# ===============================
HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"

headers = {
    "Authorization": f"Bearer {HF_TOKEN}"
}

print("🖼️ Sending prompt to image model...")

response = requests.post(
    API_URL,
    headers=headers,
    json={"inputs": prompt},
    timeout=120
)

# ===============================
# STEP 3: Save Image
# ===============================
if response.status_code == 200:
    with open("generated_image.png", "wb") as f:
        f.write(response.content)

    print("✅ Image generated successfully!")
    print("📁 Saved as: generated_image.png")

else:
    print("❌ Image API Error")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
