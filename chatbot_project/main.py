#!/usr/bin/env python3
"""
Rule-Based Chatbot Application
A simple chatbot that responds based on predefined rules and patterns.
"""

import os
import sys
from chatbot import RuleBasedChatbot

def clear_screen():
    """Clear the console screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print the application banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                    RULE-BASED CHATBOT                       ║
    ║                                                              ║
    ║  Welcome! I'm your friendly chatbot assistant.              ║
    ║  Type 'help' to see what I can do, or 'quit' to exit.       ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def print_help():
    """Print help information"""
    help_text = """
    🤖 CHATBOT COMMANDS & FEATURES:
    
    💬 CONVERSATION:
    - Say hello, hi, hey
    - Ask "how are you?"
    - Tell me your name: "My name is [name]"
    - Ask for jokes: "Tell me a joke"
    
    ⏰ TIME & DATE:
    - "What time is it?"
    - "What's the date today?"
    - "Current time"
    
    🧮 MATH CALCULATIONS:
    - "What is 5 + 3?"
    - "Calculate 10 * 2"
    - "15 - 7"
    - "20 / 4"
    
    🌤️ WEATHER:
    - "How's the weather?"
    - "Weather forecast"
    
    📋 OTHER COMMANDS:
    - "help" - Show this help message
    - "history" - Show conversation history
    - "clear" - Clear conversation history
    - "save" - Save conversation to file
    - "quit" or "exit" - Exit the chatbot
    
    💡 TIP: I understand natural language, so feel free to chat naturally!
    """
    print(help_text)

def print_history(chatbot):
    """Print conversation history"""
    history = chatbot.get_conversation_history()
    if not history:
        print("No conversation history yet.")
        return
    
    print("\n📜 CONVERSATION HISTORY:")
    print("=" * 50)
    
    for i, entry in enumerate(history, 1):
        if "user" in entry:
            print(f"{i}. You: {entry['user']}")
        elif "bot" in entry:
            print(f"   Bot: {entry['bot']}")
        print()

def main():
    """Main application function"""
    clear_screen()
    print_banner()
    
    # Initialize chatbot
    chatbot = RuleBasedChatbot("Assistant")
    
    print("Bot: Hello! I'm your rule-based chatbot. How can I help you today?")
    print("     (Type 'help' for commands, 'quit' to exit)\n")
    
    while True:
        try:
            # Get user input
            user_input = input("You: ").strip()
            
            # Handle special commands
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print(f"\nBot: Goodbye! Thanks for chatting with me!")
                break
            
            elif user_input.lower() == 'help':
                print_help()
                continue
            
            elif user_input.lower() == 'history':
                print_history(chatbot)
                continue
            
            elif user_input.lower() == 'clear':
                chatbot.clear_history()
                print("Bot: Conversation history cleared!")
                continue
            
            elif user_input.lower() == 'save':
                filename = input("Enter filename to save (default: conversation.json): ").strip()
                if not filename:
                    filename = "conversation.json"
                chatbot.save_conversation(filename)
                print(f"Bot: Conversation saved to {filename}!")
                continue
            
            elif not user_input:
                print("Bot: Please say something!")
                continue
            
            # Get bot response
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}\n")
            
        except KeyboardInterrupt:
            print(f"\n\nBot: Goodbye! Thanks for chatting with me!")
            break
        except Exception as e:
            print(f"Bot: Sorry, something went wrong: {e}")
            continue

if __name__ == "__main__":
    main() 