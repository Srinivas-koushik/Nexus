"""
Utility module for Nexus Chatbot
Contains reusable functions for speech recognition, text-to-speech, and API interactions
"""
import speech_recognition as sr
import pyttsx3
from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME, LISTEN_MESSAGE, UNKNOWN_MESSAGE, NETWORK_ERROR_MESSAGE


class AudioEngine:
    """Handles speech recognition and text-to-speech operations"""
    
    def __init__(self):
        """Initialize audio recognizer and text-to-speech engine"""
        self.listener = sr.Recognizer()
        self.speaker = pyttsx3.init()
    
    def speak(self, text):
        """
        Convert text to speech.
        
        Args:
            text (str): Text to convert to speech
        """
        self.speaker.say(text)
        self.speaker.runAndWait()
    
    def listen(self):
        """
        Listen for voice input and return recognized text.
        
        Returns:
            str: Recognized instruction or error message
        """
        try:
            with sr.Microphone() as source:
                print(LISTEN_MESSAGE)
                speech = self.listener.listen(source)
                instruction = self.listener.recognize_google(speech)
                instruction = instruction.lower()
                print(instruction)
                return instruction
        except sr.UnknownValueError:
            return UNKNOWN_MESSAGE
        except sr.RequestError:
            return NETWORK_ERROR_MESSAGE
        except Exception as e:
            return f"An error occurred: {e}"


class ChatbotClient:
    """Handles Groq API interactions for chatbot responses"""
    
    def __init__(self, api_key=GROQ_API_KEY, model=MODEL_NAME):
        """
        Initialize Groq API client.
        
        Args:
            api_key (str): Groq API key
            model (str): Model name to use
        """
        self.client = Groq(api_key=api_key)
        self.model = model
    
    def get_response(self, user_message):
        """
        Get chatbot response using Groq API.
        
        Args:
            user_message (str): User's input message
            
        Returns:
            str: Chatbot's response or error message
        """
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {"role": "user", "content": user_message}
                ],
                model=self.model,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return f"An error occurred: {e}"


# Global instances
audio_engine = AudioEngine()
chatbot_client = ChatbotClient()
