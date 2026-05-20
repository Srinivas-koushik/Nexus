"""
Configuration module for Nexus Chatbot
Handles environment variables and API key management
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Configuration
GROQ_API_KEY = os.getenv('GROQ_API_KEY')
MODEL_NAME = os.getenv('MODEL_NAME', 'llama3-8b-8192')

# Application Configuration
APP_TITLE = os.getenv('APP_TITLE', 'Voice-Enabled Chatbot')

# Validation
if not GROQ_API_KEY:
    raise ValueError(
        "API key is missing. Please set the GROQ_API_KEY environment variable in .env file. "
        "Copy .env.example to .env and add your API key."
    )

# Application UI Configuration
CHAT_AREA_CONFIG = {
    'wrap': 'word',
    'width': 50,
    'height': 20,
    'font': ('Arial', 12)
}

INPUT_BOX_CONFIG = {
    'height': 3,
    'font': ('Arial', 12)
}

BUTTON_CONFIG = {
    'font': ('Arial', 12),
    'padx': 10,
    'pady': (0, 10)
}

MIC_BUTTON_CONFIG = {
    'text': '🎤',
    'font': ('Arial', 20)
}

SEND_BUTTON_CONFIG = {
    'text': 'Send',
    'font': ('Arial', 12)
}

# Message Configuration
GREETING_MESSAGE = "Hi! Welcome to our ChatBot. How can I assist you today?"
EXIT_MESSAGE = "Thanks for chatting! See you next time."
ERROR_MESSAGE = "Sorry, I encountered an error. Please try again."
LISTEN_MESSAGE = "Listening..."
UNKNOWN_MESSAGE = "Sorry, I did not understand that."
NETWORK_ERROR_MESSAGE = "Could not request results; check your network connection."
