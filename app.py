"""
Nexus Chatbot - GUI Application
Voice-enabled chatbot with Groq API integration
"""
import tkinter as tk
from tkinter import messagebox, scrolledtext
from utils import audio_engine, chatbot_client
from config import (
    APP_TITLE, GREETING_MESSAGE, EXIT_MESSAGE, ERROR_MESSAGE,
    CHAT_AREA_CONFIG, INPUT_BOX_CONFIG, BUTTON_CONFIG,
    MIC_BUTTON_CONFIG, SEND_BUTTON_CONFIG
)


class ChatbotGUI:
    """Main GUI application for the voice-enabled chatbot"""
    
    def __init__(self, root):
        """
        Initialize the GUI application.
        
        Args:
            root (tk.Tk): Root window
        """
        self.root = root
        self.root.title(APP_TITLE)
        self.setup_ui()
        self.show_greeting()
    
    def setup_ui(self):
        """Set up the user interface components"""
        # Create chat display area
        self.chat_area = scrolledtext.ScrolledText(
            self.root,
            **CHAT_AREA_CONFIG
        )
        self.chat_area.pack(padx=10, pady=10)
        
        # Create input text box
        self.input_box = tk.Text(
            self.root,
            **INPUT_BOX_CONFIG
        )
        self.input_box.pack(padx=10, pady=(0, 10))
        
        # Create microphone button
        self.mic_button = tk.Button(
            self.root,
            **MIC_BUTTON_CONFIG,
            command=self.listen_and_display
        )
        self.mic_button.pack(padx=10, pady=(0, 10))
        
        # Create send button
        self.send_button = tk.Button(
            self.root,
            **SEND_BUTTON_CONFIG,
            command=self.send_message
        )
        self.send_button.pack(padx=10, pady=(0, 10))
    
    def show_greeting(self):
        """Display greeting message on startup"""
        self.chat_area.insert(tk.END, f"ChatBot: {GREETING_MESSAGE}\n")
        audio_engine.speak(GREETING_MESSAGE)
    
    def send_message(self):
        """Handle sending user message and getting chatbot response"""
        user_input = self.input_box.get("1.0", tk.END).strip()
        
        if not user_input:
            messagebox.showwarning("Input Error", "Please enter a message before sending.")
            return
        
        # Display user message
        self.chat_area.insert(tk.END, f"You: {user_input}\n")
        self.input_box.delete("1.0", tk.END)
        
        # Check for exit keyword
        if 'bye' in user_input.lower():
            self.chat_area.insert(tk.END, f"ChatBot: {EXIT_MESSAGE}\n")
            audio_engine.speak(EXIT_MESSAGE)
            return
        
        # Get and display chatbot response
        response = chatbot_client.get_response(user_input)
        self.chat_area.insert(tk.END, f"ChatBot: {response}\n")
        audio_engine.speak(response)
    
    def listen_and_display(self):
        """Listen for voice input and display in input box"""
        instruction = audio_engine.listen()
        if instruction:
            self.input_box.insert(tk.END, instruction)


def main():
    """Main application entry point"""
    root = tk.Tk()
    app = ChatbotGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
