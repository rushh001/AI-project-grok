# AI Voice Assistant (Sara)

A voice-activated AI assistant for Windows that listens to spoken commands and executes them (opening apps, browsers, folders, and more). Unrecognized commands fall back to an AI-powered conversational mode powered by Groq's LLaMA and Whisper models.

---

## Features

- 🎙️ **Voice Recognition** – Records audio from your microphone and transcribes it using Groq's Whisper API (`distil-whisper-large-v3-en`).
- 🤖 **AI Conversation** – Unrecognized commands are handled by Groq's `llama-3.3-70b-versatile` model.
- 🗣️ **Text-to-Speech** – AI responses can be spoken aloud using Google Text-to-Speech (gTTS).
- 🖥️ **Application Launcher** – Open common Windows apps by voice:
  - Browsers: Brave, Chrome, Edge
  - Office apps: Notepad, Excel, Word
  - System tools: Terminal/CMD, File Explorer
  - Communication: WhatsApp, Gmail, Outlook
- 📁 **Folder Navigation** – Quickly open Downloads, Documents, Desktop, Pictures, Music, or Videos.
- 🔍 **Google Search** – Say *"search for <query>"* to open a Google search in your browser.
- 🌤️ **Weather & News** – Utility functions for fetching weather data (OpenWeather API) and top news headlines (NewsAPI).

---

## Prerequisites

- Python 3.8+
- Windows OS (application-launch commands use Windows-specific calls)
- A microphone connected to your system
- API keys for:
  - [Groq](https://console.groq.com/) (Whisper transcription + LLaMA chat)
  - [OpenWeatherMap](https://openweathermap.org/api) (weather feature)
  - [NewsAPI](https://newsapi.org/) (news feature)

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/rushh001/AI-project-grok.git
   cd AI-project-grok
   ```

2. **Install dependencies**

   ```bash
   pip install requests sounddevice scipy numpy gtts pydub
   ```

   > **Note:** `pydub` requires [FFmpeg](https://ffmpeg.org/download.html) to be installed and available on your system PATH for audio playback.

---

## Configuration

> ⚠️ **Never commit real API keys to source control.** Use environment variables or a `.env` file (e.g. with [`python-dotenv`](https://pypi.org/project/python-dotenv/)) and add `config.py` to `.gitignore`.

Open `config.py` and replace the placeholder values with your actual API keys:

```python
WEATHER_API_KEY = "your_openweather_api_key"
NEWS_API_KEY    = "your_newsapi_key"
GROQ_API_KEY    = "your_groq_api_key"
```

Open `voice_recognition.py` and set the Groq API endpoints:

```python
GROQ_API_KEY         = "your_groq_api_key"
GROQ_TRANSCRIBE_URL  = "https://api.groq.com/openai/v1/audio/transcriptions"
GROQ_CHAT_URL        = "https://api.groq.com/openai/v1/chat/completions"
```

If your Windows username is different from the default, update the user folder path in `command_handler.py`:

```python
USER_FOLDER = r"C:\Users\<your-username>"
```

---

## Usage

Run the assistant from the command line:

```bash
python main.py
```

The assistant will:
1. Print `Listening for voice commands...`
2. Record 4 seconds of audio from your microphone.
3. Transcribe the audio and print the recognized command.
4. Execute the matching command, or query the AI for an intelligent response.

### Example voice commands

| Say…                              | Action                                      |
|-----------------------------------|---------------------------------------------|
| `open brave`                      | Launches Brave browser                      |
| `open notepad`                    | Launches Notepad                            |
| `open downloads`                  | Opens the Downloads folder                  |
| `search for Python tutorials`     | Opens a Google search for Python tutorials  |
| `open gmail`                      | Opens Gmail in your default browser         |
| `What is the speed of light?`     | Asks the LLaMA AI and prints the answer     |

---

## Project Structure

```
AI-project-grok/
├── main.py              # Entry point – records voice and dispatches commands
├── voice_recognition.py # Audio recording, Whisper transcription, AI chat & TTS
├── command_handler.py   # Maps recognized commands to system actions
├── utils.py             # Weather and news API helper functions
└── config.py            # API key configuration (do not commit real keys)
```

---

## Technologies Used

| Library / Service | Purpose |
|---|---|
| [sounddevice](https://python-sounddevice.readthedocs.io/) | Microphone audio recording |
| [scipy](https://scipy.org/) | WAV file writing |
| [numpy](https://numpy.org/) | Audio data handling |
| [gTTS](https://gtts.readthedocs.io/) | Text-to-speech synthesis |
| [pydub](https://github.com/jiaaro/pydub) | Audio playback |
| [requests](https://docs.python-requests.org/) | HTTP API calls |
| [Groq Whisper API](https://console.groq.com/docs/speech-text) | Speech-to-text transcription |
| [Groq LLaMA API](https://console.groq.com/docs/openai) | AI conversation responses |
| [OpenWeatherMap API](https://openweathermap.org/api) | Weather data |
| [NewsAPI](https://newsapi.org/) | News headlines |

---

## License

This project is open source. Feel free to use, modify, and distribute it.
