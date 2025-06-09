import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyaudio

# Set GROQ_API_KEY environment variable for future use
os.environ['GROQ_API_KEY'] = "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"
api_key = os.getenv('GROQ_API_KEY')

if not api_key:
    raise ValueError("API key is missing. Set the GROQ_API_KEY environment variable.")

try:
    from groq import Groq
except ImportError:
    raise ImportError("The 'groq' library is not installed. Please install it using 'pip install groq'.")

# Initialize recognizer and text-to-speech engine
listener = sr.Recognizer()
machine = pyttsx3.init()
client = Groq(api_key=api_key)

def talk(text):
    """Convert text to speech."""
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    """Listen for voice input and return the recognized instruction."""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            speech = listener.listen(source)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            print(instruction)
            return instruction
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        print("Could not request results; check your network connection.")
        return ""

def greet_and_chat():
    """Greets the user, takes voice input, and provides chatbot responses until 'bye' is entered."""
    print("Hi! Welcome to our ChatBot")
    talk("Hi! Welcome to our ChatBot. How can I assist you today?")

    while True:
        instruction = input_instruction()

        # Check for exit keyword
        if 'bye' in instruction:
            print("Thanks for chatting! See you next time.")
            talk("Thanks for chatting! See you next time.")
            break

        # Use Groq API for chat completion
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": instruction,
                    }
                ],
                model="llama3-8b-8192",
            )
            response = chat_completion.choices[0].message.content
            print(response)
            talk(response)    #this is used to read out the response
        except Exception as e:
            print(f"An error occurred: {e}")
            talk("Sorry, I encountered an error. Please try again.")

if __name__ == "__main__":
    greet_and_chat()
