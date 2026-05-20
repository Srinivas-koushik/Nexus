"""
Nexus Chatbot - Command Line Interface Version
Voice-enabled chatbot with Groq API integration (CLI mode)
Alternative to GUI version for terminal-based interaction
"""
from utils import audio_engine, chatbot_client
from config import GREETING_MESSAGE, EXIT_MESSAGE, ERROR_MESSAGE


def main():
    """Main CLI application entry point"""
    print("=" * 50)
    print(GREETING_MESSAGE)
    print("=" * 50)
    audio_engine.speak(GREETING_MESSAGE)
    
    while True:
        # Get user input
        instruction = audio_engine.listen()
        
        # Check for exit keyword
        if not instruction or 'bye' in instruction.lower():
            print(EXIT_MESSAGE)
            audio_engine.speak(EXIT_MESSAGE)
            break
        
        # Get and display chatbot response
        response = chatbot_client.get_response(instruction)
        print(f"ChatBot: {response}")
        audio_engine.speak(response)
        print("-" * 50)


if __name__ == "__main__":
    main()
