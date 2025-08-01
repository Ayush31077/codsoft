#!/usr/bin/env python3
"""
Demo script for the Rule-Based Chatbot
This script demonstrates various capabilities of the chatbot.
"""

from chatbot import RuleBasedChatbot
import time

def demo_conversation():
    """Demonstrate a sample conversation with the chatbot"""
    print("🤖 RULE-BASED CHATBOT DEMO")
    print("=" * 50)
    
    # Initialize chatbot
    chatbot = RuleBasedChatbot("DemoBot")
    
    # Sample conversation
    demo_messages = [
        "Hello!",
        "My name is Alice",
        "What time is it?",
        "Tell me a joke",
        "What is 15 + 27?",
        "How's the weather?",
        "What can you do?",
        "Thank you!",
        "Goodbye"
    ]
    
    print("Starting demo conversation...\n")
    
    for message in demo_messages:
        print(f"You: {message}")
        response = chatbot.get_response(message)
        print(f"Bot: {response}")
        print("-" * 30)
        time.sleep(1)  # Add a small delay for better readability
    
    print("\nDemo completed!")

def demo_features():
    """Demonstrate specific features"""
    print("\n🔧 FEATURE DEMONSTRATION")
    print("=" * 50)
    
    chatbot = RuleBasedChatbot("FeatureBot")
    
    # Test different types of inputs
    test_cases = [
        ("Greeting", "Hi there!"),
        ("Math", "Calculate 25 * 4"),
        ("Time", "What's the current time?"),
        ("Weather", "How's the weather today?"),
        ("Joke", "Tell me something funny"),
        ("Name", "What's your name?"),
        ("User name", "My name is Bob"),
        ("Unknown", "What is quantum physics?"),
    ]
    
    for category, message in test_cases:
        print(f"\n{category}:")
        print(f"You: {message}")
        response = chatbot.get_response(message)
        print(f"Bot: {response}")

def demo_conversation_history():
    """Demonstrate conversation history feature"""
    print("\n📜 CONVERSATION HISTORY DEMO")
    print("=" * 50)
    
    chatbot = RuleBasedChatbot("HistoryBot")
    
    # Have a short conversation
    messages = ["Hello", "How are you?", "What's 10 + 5?", "Thanks!"]
    
    for message in messages:
        chatbot.get_response(message)
    
    # Show history
    history = chatbot.get_conversation_history()
    print("Conversation History:")
    for i, entry in enumerate(history, 1):
        if "user" in entry:
            print(f"{i}. You: {entry['user']}")
        elif "bot" in entry:
            print(f"   Bot: {entry['bot']}")

def main():
    """Main demo function"""
    print("Welcome to the Rule-Based Chatbot Demo!")
    print("This demo will showcase various features of the chatbot.\n")
    
    # Run different demos
    demo_conversation()
    demo_features()
    demo_conversation_history()
    
    print("\n🎉 Demo completed! You can now run 'python main.py' to interact with the chatbot yourself.")

if __name__ == "__main__":
    main() 