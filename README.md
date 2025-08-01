# 🤖 Rule-Based Chatbot

A simple yet powerful rule-based chatbot built in Python that responds to user input based on predefined patterns and rules.

## ✨ Features

- **Natural Language Processing**: Understands various ways to express the same intent
- **Mathematical Calculations**: Performs basic arithmetic operations
- **Time and Date**: Provides current time and date information
- **Conversation History**: Tracks and displays conversation history
- **User Name Recognition**: Remembers and uses the user's name
- **Jokes and Humor**: Tells random jokes to lighten the mood
- **Weather Queries**: Responds to weather-related questions
- **Extensible Rules**: Easy to add new rules and responses
- **JSON Export**: Save conversations to JSON files

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- No external dependencies required (uses only Python standard library)

### Installation

1. Clone or download this project
2. Navigate to the project directory:
   ```bash
   cd chatbot_project
   ```

### Running the Chatbot

#### Interactive Mode
```bash
python main.py
```

#### Demo Mode
```bash
python demo.py
```

## 📖 Usage

### Basic Commands

| Command | Description |
|---------|-------------|
| `help` | Show available commands and features |
| `history` | Display conversation history |
| `clear` | Clear conversation history |
| `save` | Save conversation to JSON file |
| `quit` / `exit` | Exit the chatbot |

### Example Conversations

```
You: Hello!
Bot: Hi there! I'm Assistant. Nice to meet you!

You: My name is John
Bot: Nice to meet you, John!

You: What time is it?
Bot: The current time is 14:30:25.

You: Calculate 15 + 27
Bot: The result of 15 + 27 is 42

You: Tell me a joke
Bot: Why don't scientists trust atoms? Because they make up everything! 😄

You: How's the weather?
Bot: I can't check the weather in real-time, but I hope it's nice where you are!

You: Goodbye
Bot: Goodbye! Have a great day!
```

## 🏗️ Project Structure

```
chatbot_project/
├── chatbot.py          # Main chatbot class and logic
├── main.py             # Interactive application
├── demo.py             # Demonstration script
├── requirements.txt    # Dependencies (none required)
├── README.md          # This file
└── conversation.json   # Generated conversation file (after saving)
```

## 🔧 Customization

### Adding New Rules

You can easily extend the chatbot by adding new rules in the `_load_rules()` method:

```python
"new_feature": {
    "patterns": [
        r"\b(your pattern here)\b",
        r"\b(another pattern)\b"
    ],
    "responses": [
        "Response 1",
        "Response 2",
        "Response 3"
    ]
}
```

### Modifying Responses

Edit the responses in the `_load_rules()` method to customize the chatbot's personality and responses.

## 🧪 Testing

Run the demo to see the chatbot in action:

```bash
python demo.py
```

This will showcase:
- Basic conversation flow
- Mathematical calculations
- Time and date responses
- Joke telling
- Conversation history

## 📝 Conversation History

The chatbot automatically tracks all conversations. You can:
- View history with the `history` command
- Clear history with the `clear` command
- Save history to a JSON file with the `save` command

## 🔍 How It Works

1. **Pattern Matching**: Uses regular expressions to match user input against predefined patterns
2. **Rule Selection**: Selects the most appropriate rule based on the input
3. **Response Generation**: Randomly selects a response from the matching rule
4. **Context Management**: Maintains conversation history and user context
5. **Special Processing**: Handles math calculations and user name extraction separately

## 🎯 Supported Features

### Conversation
- Greetings (hi, hello, hey, etc.)
- Farewells (bye, goodbye, etc.)
- How are you questions
- Name recognition and storage

### Information
- Current time and date
- Weather-related queries (general responses)
- Bot capabilities and help

### Calculations
- Basic arithmetic (+, -, *, /)
- Natural language math queries
- Error handling for division by zero

### Entertainment
- Random jokes
- Humorous responses
- Friendly conversation

## 🤝 Contributing

Feel free to enhance this chatbot by:
- Adding new rules and patterns
- Improving response quality
- Adding new features
- Optimizing performance

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Troubleshooting

### Common Issues

1. **Import Error**: Make sure you're in the correct directory
2. **Python Version**: Ensure you're using Python 3.6+
3. **File Permissions**: Check write permissions for saving conversations

### Getting Help

If you encounter any issues:
1. Check that all files are in the same directory
2. Verify Python version: `python --version`
3. Try running the demo first: `python demo.py`

---

**Enjoy chatting with your new rule-based chatbot! 🤖✨** 
