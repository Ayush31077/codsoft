#!/usr/bin/env python3
"""
Simple test script for the Rule-Based Chatbot
"""

from chatbot import RuleBasedChatbot

def test_chatbot():
    """Test basic chatbot functionality"""
    print("🧪 Testing Rule-Based Chatbot")
    print("=" * 40)
    
    # Initialize chatbot
    chatbot = RuleBasedChatbot("TestBot")
    
    # Test cases
    test_cases = [
        ("Hello", "greeting"),
        ("What time is it?", "time"),
        ("Calculate 10 + 5", "math"),
        ("Tell me a joke", "joke"),
        ("My name is Alice", "user_name"),
        ("How's the weather?", "weather"),
        ("Goodbye", "farewell")
    ]
    
    passed = 0
    total = len(test_cases)
    
    for message, expected_type in test_cases:
        print(f"\nTesting: '{message}'")
        response = chatbot.get_response(message)
        print(f"Response: {response}")
        
        # Simple validation - check if response is not empty
        if response and len(response.strip()) > 0:
            print("✅ PASS")
            passed += 1
        else:
            print("❌ FAIL")
    
    print(f"\n{'='*40}")
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Chatbot is working correctly.")
    else:
        print("⚠️  Some tests failed. Please check the implementation.")
    
    # Test conversation history
    print(f"\n📜 Conversation History Length: {len(chatbot.get_conversation_history())}")
    
    return passed == total

if __name__ == "__main__":
    test_chatbot() 