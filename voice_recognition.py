import requests
import sounddevice as sd
import scipy.io.wavfile as wav
import numpy as np
import os
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

# Your Groq Whisper API key
GROQ_API_KEY = 
GROQ_TRANSCRIBE_URL = 
GROQ_CHAT_URL =

def record_and_transcribe():
    record_audio()  # Record user's voice
    return transcribe_audio()  # Convert speech to text


# Function to record audio
def record_audio(filename="input.wav", duration=4, samplerate=44100):
    print("Recording... Speak now!")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype=np.int16)
    sd.wait()
    wav.write(filename, samplerate, recording)
    print("Recording saved.")

# Function to transcribe speech to text using Groq Whisper API
def transcribe_audio(filename="input.wav"):
    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    files = {"file": open(filename, "rb")}
    data = {"model": "distil-whisper-large-v3-en"}

    response = requests.post(GROQ_TRANSCRIBE_URL, headers=headers, files=files, data=data)
    
    if response.status_code == 200:
        return response.json().get("text", "").strip()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return ""

# Function to get AI-generated response using `llama-3-70b-versatile`
def get_ai_response(user_input):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }
    
    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": user_input}],
        "temperature": 0.7,
        "max_tokens": 300,
    }

    response = requests.post(GROQ_CHAT_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return "Sorry, I couldn't process that."

# Function to convert text to speech and play it
def speak_text(text):
    tts = gTTS(text=text, lang="en")
    tts.save("response.mp3")
    audio = AudioSegment.from_file("response.mp3", format="mp3")
    play(audio)

# Main function to handle the conversation
def voice_chat():
    record_audio()  # Record user's voice
    user_input = transcribe_audio()  # Convert speech to text

    if user_input:
        print(f"You: {user_input}")
        ai_response = get_ai_response(user_input)  # Get AI response
        print(f"AI: {ai_response}")
        speak_text(ai_response)  # Speak the AI response

if __name__ == "__main__":
    while True:
        print("\nSay something (or type 'exit' to quit)...")
        voice_chat()
