import re
import random
import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple

class RuleBasedChatbot:
    def __init__(self, name: str = "ChatBot"):
        self.name = name
        self.user_name = "User"
        self.conversation_history = []
        self.rules = self._load_rules()
        self.context = {}
        
    def _load_rules(self) -> Dict:
        """Load predefined rules for responses"""
        return {
            "greetings": {
                "patterns": [
                    r"\b(hi|hello|hey|good morning|good afternoon|good evening)\b",
                    r"\b(how are you|how's it going|what's up)\b"
                ],
                "responses": [
                    "Hello! How can I help you today?",
                    f"Hi there! I'm {self.name}. Nice to meet you!",
                    "Hello! I'm here to assist you.",
                    "Hey! How can I be of service?"
                ]
            },
            "farewell": {
                "patterns": [
                    r"\b(bye|goodbye|see you|take care|exit|quit)\b",
                    r"\b(thank you|thanks)\b"
                ],
                "responses": [
                    "Goodbye! Have a great day!",
                    "See you later! Feel free to come back anytime.",
                    "Take care! It was nice chatting with you.",
                    "You're welcome! Come back soon!"
                ]
            },
            "weather": {
                "patterns": [
                    r"\b(weather|temperature|forecast|rain|sunny)\b",
                    r"\b(how's the weather|what's the weather like)\b"
                ],
                "responses": [
                    "I can't check the weather in real-time, but I hope it's nice where you are!",
                    "I don't have access to weather data, but I'd recommend checking a weather app.",
                    "The weather is always good for a chat! 😊"
                ]
            },
            "time": {
                "patterns": [
                    r"\b(time|what time|current time|clock)\b",
                    r"\b(date|what date|today)\b"
                ],
                "responses": [
                    f"The current time is {datetime.now().strftime('%H:%M:%S')}.",
                    f"Today is {datetime.now().strftime('%A, %B %d, %Y')}.",
                    f"It's {datetime.now().strftime('%I:%M %p')} right now."
                ]
            },
            "help": {
                "patterns": [
                    r"\b(help|what can you do|capabilities|features)\b",
                    r"\b(commands|options|menu)\b"
                ],
                "responses": [
                    "I can help you with:\n- Greetings and casual conversation\n- Time and date information\n- Basic calculations\n- Simple questions\n- Weather (general info)\nJust ask me anything!",
                    "I'm a rule-based chatbot! I can chat, tell time, do math, and more. What would you like to know?"
                ]
            },
            "math": {
                "patterns": [
                    r"\b(calculate|compute|math|add|subtract|multiply|divide)\b",
                    r"\b(\d+\s*[\+\-\*\/]\s*\d+)",
                    r"\b(what is|what's)\s+\d+\s*[\+\-\*\/]\s*\d+"
                ],
                "responses": [
                    "I can help with basic math! Try asking something like 'what is 5 + 3' or 'calculate 10 * 2'",
                    "I'm ready to do some calculations! Just give me a math problem."
                ]
            },
            "jokes": {
                "patterns": [
                    r"\b(joke|funny|humor|laugh)\b",
                    r"\b(tell me a joke|make me laugh)\b"
                ],
                "responses": [
                    "Why don't scientists trust atoms? Because they make up everything! 😄",
                    "What do you call a fake noodle? An impasta! 🍝",
                    "Why did the scarecrow win an award? He was outstanding in his field! 🌾",
                    "I told my wife she was drawing her eyebrows too high. She looked surprised! 😲"
                ]
            },
            "name": {
                "patterns": [
                    r"\b(what's your name|who are you|your name)\b",
                    r"\b(call you|your name is)\b"
                ],
                "responses": [
                    f"My name is {self.name}! Nice to meet you!",
                    f"I'm {self.name}, your friendly chatbot assistant.",
                    f"You can call me {self.name}!"
                ]
            },
            "user_name": {
                "patterns": [
                    r"\b(my name is|i'm|i am)\s+(\w+)",
                    r"\b(call me|i'm called)\s+(\w+)"
                ],
                "responses": [
                    "Nice to meet you, {user_name}!",
                    "Hello {user_name}! How are you today?",
                    "Great to know you, {user_name}!"
                ]
            },
            "default": {
                "patterns": [],
                "responses": [
                    "I'm not sure I understand. Could you rephrase that?",
                    "That's interesting! Tell me more about it.",
                    "I'm still learning. Could you ask me something else?",
                    "I don't have a specific response for that, but I'm here to chat!"
                ]
            }
        }
    
    def _extract_user_name(self, message: str) -> Optional[str]:
        """Extract user name from message"""
        for pattern in self.rules["user_name"]["patterns"]:
            match = re.search(pattern, message, re.IGNORECASE)
            if match:
                return match.group(2)
        return None
    
    def _calculate_math(self, message: str) -> Optional[str]:
        """Perform basic mathematical calculations"""
        # Find mathematical expressions
        math_pattern = r'(\d+)\s*([\+\-\*\/])\s*(\d+)'
        match = re.search(math_pattern, message)
        
        if match:
            num1 = int(match.group(1))
            operator = match.group(2)
            num2 = int(match.group(3))
            
            try:
                if operator == '+':
                    result = num1 + num2
                elif operator == '-':
                    result = num1 - num2
                elif operator == '*':
                    result = num1 * num2
                elif operator == '/':
                    if num2 == 0:
                        return "Sorry, I can't divide by zero!"
                    result = num1 / num2
                else:
                    return None
                
                return f"The result of {num1} {operator} {num2} is {result}"
            except:
                return "Sorry, I couldn't calculate that."
        
        return None
    
    def _find_matching_rule(self, message: str) -> Tuple[str, List[str]]:
        """Find the best matching rule for the given message"""
        message_lower = message.lower()
        
        # Check for math calculations first
        math_result = self._calculate_math(message)
        if math_result:
            return "math", [math_result]
        
        # Check for user name
        user_name = self._extract_user_name(message)
        if user_name:
            self.user_name = user_name
            responses = [resp.format(user_name=user_name) for resp in self.rules["user_name"]["responses"]]
            return "user_name", responses
        
        # Check other rules
        for rule_name, rule_data in self.rules.items():
            if rule_name in ["default", "user_name"]:
                continue
                
            for pattern in rule_data["patterns"]:
                if re.search(pattern, message_lower):
                    return rule_name, rule_data["responses"]
        
        # Return default response
        return "default", self.rules["default"]["responses"]
    
    def get_response(self, message: str) -> str:
        """Generate a response based on the input message"""
        # Add to conversation history
        self.conversation_history.append({"user": message, "timestamp": datetime.now()})
        
        # Find matching rule and get response
        rule_name, responses = self._find_matching_rule(message)
        
        # Select a random response from the matching rule
        response = random.choice(responses)
        
        # Add response to conversation history
        self.conversation_history.append({"bot": response, "timestamp": datetime.now()})
        
        return response
    
    def get_conversation_history(self) -> List[Dict]:
        """Get the conversation history"""
        return self.conversation_history
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
    
    def save_conversation(self, filename: str = "conversation.json"):
        """Save conversation history to a JSON file"""
        with open(filename, 'w') as f:
            json.dump(self.conversation_history, f, indent=2, default=str)
    
    def load_conversation(self, filename: str = "conversation.json"):
        """Load conversation history from a JSON file"""
        try:
            with open(filename, 'r') as f:
                self.conversation_history = json.load(f)
        except FileNotFoundError:
            print(f"File {filename} not found.")
        except json.JSONDecodeError:
            print(f"Error reading {filename}.") 