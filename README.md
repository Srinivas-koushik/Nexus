## 🤖 Nexus Chatbot

A voice-enabled chatbot powered by the **Groq API** with both GUI and CLI interfaces. This chatbot supports speech recognition, text-to-speech, and intelligent responses using the Llama 3 model.

---

## 🌟 Features

- 🎤 **Voice Input**: Real-time speech recognition
- 🔊 **Voice Output**: Text-to-speech responses
- 🖥️ **GUI Interface**: User-friendly tkinter-based interface
- 💻 **CLI Mode**: Command-line interface alternative
- 🔐 **Secure API Key Management**: Environment variable-based configuration
- 🚀 **Fast Responses**: Powered by Groq's ultra-fast inference

---

## 📋 Prerequisites

- Python 3.8+
- Groq API Key (get one from [groq.com](https://groq.com))
- Microphone (for voice input)
- Speakers (for voice output)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Srinivas-koushik/Nexus.git
cd Nexus
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

Copy the example environment file and add your Groq API key:

```bash
cp .env.example .env
```

Edit `.env` and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

> ⚠️ **Security Note**: Never commit the `.env` file to version control. It's already in `.gitignore`.

---

## 🎯 Usage

### GUI Mode (Recommended)

```bash
python app.py
```

- Click **🎤** button to speak your question
- Type your message in the text box and click **Send**
- Say **"bye"** to exit

### CLI Mode

```bash
python cli_chatbot.py
```

- The chatbot will prompt you to speak
- Say your question clearly
- Receive both text and voice responses
- Say **"bye"** to exit

---

## 📁 Project Structure

```
Nexus/
├── app.py              # GUI application (refactored)
├── cli_chatbot.py      # CLI application
├── config.py           # Configuration management
├── utils.py            # Reusable utilities (AudioEngine, ChatbotClient)
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
├── .gitignore          # Git ignore rules (includes .env)
└── README.md           # This file
```

---

## 🔧 Configuration

All settings are managed in `config.py`:

```python
GROQ_API_KEY = os.getenv('GROQ_API_KEY')  # From .env file
MODEL_NAME = os.getenv('MODEL_NAME', 'llama3-8b-8192')
```

---

## 🔐 Security Best Practices

✅ **What's Been Done:**
- API keys moved from code to `.env` file
- Sensitive text files removed from tracking
- Centralized configuration management
- `.env` file added to `.gitignore`
- Removed duplicate API key definitions

✅ **Your Responsibilities:**
- Never share your `.env` file
- Never commit `.env` to git
- Regenerate API keys if accidentally exposed
- Keep dependencies updated

---

## 🐛 Troubleshooting

### "API key is missing" Error

```bash
# Ensure .env file exists and contains GROQ_API_KEY
cat .env
```

### Microphone Not Detected

```bash
# Install PyAudio dependencies
# On Ubuntu: sudo apt-get install portaudio19-dev
# On macOS: brew install portaudio
# Then: pip install --upgrade pyaudio
```

### Speech Recognition Fails

- Check your internet connection (Google Speech API requires it)
- Ensure your microphone is working: `python -m sounddevice`
- Speak clearly and close to your microphone

---

## 📚 Code Improvements Made

### Before (Issues):
- ❌ API keys hardcoded in 3 files
- ❌ 95% code duplication between `app.py` and `chatbot.py`
- ❌ API keys stored in plaintext in `groqapi.txt`
- ❌ No configuration management
- ❌ No separation of concerns

### After (Refactored):
- ✅ Centralized config management (`config.py`)
- ✅ Reusable components (`utils.py`)
- ✅ Single source of truth for configuration
- ✅ Secure API key handling via environment variables
- ✅ Clean, maintainable code structure
- ✅ Both GUI and CLI interfaces
- ✅ Proper error handling

---

## 🤝 Contributing

Feel free to submit issues and enhancement requests!

---

## 📄 License

This project is open source and available under the MIT License.

---

## 👤 Author

**G. Srinivas Koushik**
- LinkedIn: [linkedin.com/in/g-srinivas-koushik-69506a217](https://linkedin.com/in/g-srinivas-koushik-69506a217)

---

## 🙏 Acknowledgments

- [Groq](https://groq.com) - Ultra-fast LLM inference
- [SpeechRecognition](https://github.com/Uberi/speech_recognition) - Speech to text
- [pyttsx3](https://github.com/nateshmbhat/pyttsx3) - Text to speech
- [tkinter](https://docs.python.org/3/library/tkinter.html) - GUI framework
