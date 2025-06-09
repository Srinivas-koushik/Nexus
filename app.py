import os
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext

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
            # print("Hi! Welcome to our ChatBot")
            # talk("Hi! Welcome to our ChatBot. How can I assist you today?")
            print("Listening...")
            speech = listener.listen(source)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            print(instruction)
            return instruction
    except sr.UnknownValueError:
        return "Sorry, I did not understand that."
    except sr.RequestError:
        return "Could not request results; check your network connection."
    except Exception as e:
        return f"An error occurred: {e}"

def send_message():
    user_input = input_box.get("1.0", tk.END).strip()
    if user_input:
        chat_area.insert(tk.END, "You: " + user_input + "\n")
        input_box.delete("1.0", tk.END)

        # Check for exit keyword
        if 'bye' in user_input:
            chat_area.insert(tk.END, "ChatBot: Thanks for chatting! See you next time.\n")
            talk("Thanks for chatting! See you next time.")
            return

        # Use Groq API for chat completion
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {"role": "user", "content": user_input}
                ],
                model="llama3-8b-8192",
            )
            response = chat_completion.choices[0].message.content
            chat_area.insert(tk.END, "ChatBot: " + response + "\n")
            talk(response)
        except Exception as e:
            error_message = f"An error occurred: {e}"
            chat_area.insert(tk.END, "ChatBot: " + error_message + "\n")
            talk("Sorry, I encountered an error. Please try again.")
    else:
        messagebox.showwarning("Input Error", "Please enter a message before sending.")

def listen_and_display():
    instruction = input_instruction()
    input_box.insert(tk.END, instruction)

# Create the main application window
root = tk.Tk()
root.title("Voice-Enabled Chatbot")

# Create a text area for displaying the chat
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20, font=("Arial", 12))
chat_area.pack(padx=10, pady=10)

# Create a text box for user input
input_box = tk.Text(root, height=3, font=("Arial", 12))
input_box.pack(padx=10, pady=(0, 10))

# Create a button to listen for voice input
mic_button = tk.Button(root, text="🎤", font=("Arial", 20), command=listen_and_display)
mic_button.pack(padx=10, pady=(0, 10))

# Create a button to send the message
send_button = tk.Button(root, text="Send", font=("Arial", 12), command=send_message)
send_button.pack(padx=10, pady=(0, 10))

# Run the application
root.mainloop()
