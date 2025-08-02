# 🎮 Tic Tac Toe with AI

A comprehensive Tic Tac Toe game featuring multiple AI difficulty levels, built with Python. The game includes both command-line and web interfaces, with advanced AI algorithms including minimax with alpha-beta pruning.

## 🌟 Features

- **Multiple AI Difficulty Levels**:
  - Easy: Random moves
  - Medium: 70% smart moves, 30% random
  - Hard: 90% smart moves, 10% random
  - Unbeatable: Perfect play using minimax algorithm

- **Game Modes**:
  - Player vs Player
  - Player vs AI
  - AI vs AI (watch two AIs battle)

- **Advanced AI Algorithms**:
  - Minimax algorithm with alpha-beta pruning
  - Strategic opening moves
  - Position evaluation
  - Win/block detection

- **Interactive Interfaces**:
  - Command-line interface with full functionality
  - Beautiful Streamlit web application
  - Real-time game statistics

- **Game Features**:
  - Move validation and undo functionality
  - Game state tracking
  - Statistics and win rates
  - Multiple difficulty levels

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project files**

2. **Install dependencies** (if using Streamlit):
   ```bash
   pip install streamlit
   ```

### Running the Game

#### Option 1: Command Line Interface
```bash
python main.py
```

#### Option 2: Streamlit Web App
```bash
streamlit run streamlit_app.py
```

#### Option 3: Demo Mode
```bash
python demo.py
```

## 📁 Project Structure

```
tic_tac_toe_ai/
├── game_logic.py      # Core game logic and board management
├── ai_player.py       # AI algorithms and difficulty levels
├── main.py           # Command-line interface
├── streamlit_app.py  # Web application
├── demo.py           # Demo and testing script
└── README.md         # Project documentation
```

## 🎯 How It Works

### 1. Game Logic (`game_logic.py`)
- Board representation and state management
- Move validation and win detection
- Game state tracking and history

### 2. AI Algorithms (`ai_player.py`)
- **Minimax Algorithm**: Recursive search for optimal moves
- **Alpha-Beta Pruning**: Optimization to reduce search space
- **Strategic Evaluation**: Position-based scoring
- **Difficulty Levels**: Mix of smart and random moves

### 3. AI Difficulty Levels

#### Easy
- Makes completely random moves
- Good for beginners or testing

#### Medium
- 70% smart moves using minimax
- 30% random moves for unpredictability
- Balanced challenge level

#### Hard
- 90% smart moves using minimax
- 10% random moves
- Challenging for most players

#### Unbeatable
- Always makes the optimal move
- Uses full minimax search
- Impossible to beat (best result is a draw)

## 🎮 Usage Guide

### Command Line Interface

1. **Select Game Mode**:
   - Player vs Player
   - Player vs AI
   - AI vs AI
   - View Statistics

2. **Choose AI Difficulty** (for AI modes):
   - Easy, Medium, Hard, or Unbeatable

3. **Select Your Symbol** (for PvE):
   - X (goes first)
   - O (goes second)

4. **Play the Game**:
   - Enter positions 1-9 to make moves
   - Watch AI responses
   - View game statistics

### Streamlit Web App

The web app provides a modern, interactive interface:

- **Game Board**: Click on numbered positions to make moves
- **Sidebar Controls**: Select game mode, difficulty, and settings
- **Real-time Updates**: See game state and statistics instantly
- **AI vs AI Mode**: Watch two AIs play against each other

## 🤖 AI Algorithm Details

### Minimax Algorithm
The AI uses the minimax algorithm to find the best move:

```python
def minimax(game, depth, is_maximizing, alpha, beta):
    if game_over:
        return evaluate_position()
    
    if is_maximizing:
        max_eval = -infinity
        for each possible move:
            make_move()
            eval = minimax(game, depth+1, False, alpha, beta)
            undo_move()
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Alpha-beta pruning
        return max_eval
    else:
        # Similar logic for minimizing player
```

### Alpha-Beta Pruning
Optimization technique that reduces the number of nodes evaluated:

- **Alpha**: Best score for maximizing player
- **Beta**: Best score for minimizing player
- **Pruning**: Skip branches that won't affect the final decision

### Strategic Evaluation
The AI evaluates board positions based on:

- **Winning lines**: 3 in a row
- **Blocking moves**: Prevent opponent from winning
- **Strategic positions**: Corners and center
- **Position control**: Number of winning opportunities

## 📊 Performance

### AI Decision Times
- **Easy**: < 1ms (random moves)
- **Medium**: 1-10ms (partial minimax)
- **Hard**: 5-50ms (mostly minimax)
- **Unbeatable**: 10-200ms (full minimax)

### Game Complexity
- **Total possible games**: 255,168
- **Optimal game length**: 5-9 moves
- **Perfect play result**: Always draw or win

## 🎯 Game Strategies

### For Players vs AI

#### Against Easy AI
- Play aggressively
- Take center and corners
- Create multiple winning opportunities

#### Against Medium AI
- Play strategically
- Focus on blocking AI's winning moves
- Use tactical positioning

#### Against Hard AI
- Play defensively
- Aim for draws
- Avoid obvious mistakes

#### Against Unbeatable AI
- Best possible result is a draw
- Play perfectly to achieve draw
- Any mistake will result in loss

### Optimal Opening Moves
1. **Center (5)**: Most strategic position
2. **Corners (1, 3, 7, 9)**: Good for creating multiple winning lines
3. **Edges (2, 4, 6, 8)**: Least strategic

## 🛠️ Technical Details

### Dependencies
- **Python 3.8+**: Core language
- **Streamlit**: Web interface (optional)
- **No external ML libraries**: Pure algorithmic implementation

### Algorithms Used
- **Minimax**: Game tree search
- **Alpha-Beta Pruning**: Search optimization
- **Position Evaluation**: Board state scoring
- **Move Generation**: Available moves calculation

### Code Structure
- **Object-Oriented Design**: Clean separation of concerns
- **Modular Architecture**: Easy to extend and modify
- **Type Hints**: Better code documentation
- **Error Handling**: Robust game experience

## 🎉 Future Enhancements

- **Machine Learning**: Neural network-based AI
- **Advanced Algorithms**: Monte Carlo Tree Search
- **Multiplayer**: Online multiplayer support
- **Tournament Mode**: AI vs AI competitions
- **Custom Boards**: Larger grid sizes
- **Move History**: Detailed game analysis
- **AI Training**: Learn from player moves

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new AI algorithms
- Improving the user interface
- Adding new game modes
- Optimizing performance
- Adding unit tests
- Enhancing documentation

## 📝 License

This project is open source and available under the MIT License.

## 🆘 Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all files are in the same directory
2. **Streamlit Issues**: Install Streamlit with `pip install streamlit`
3. **Performance Issues**: AI decision times may vary based on system

### Getting Help

If you encounter any issues:
1. Check the error messages carefully
2. Ensure Python 3.8+ is installed
3. Verify all files are present
4. Check file permissions

## 🎮 Game Rules

### Standard Tic Tac Toe Rules
1. Players take turns placing X and O on a 3x3 grid
2. First player to get 3 in a row (horizontally, vertically, or diagonally) wins
3. If all positions are filled without a winner, the game is a draw
4. X always goes first

### Position Numbering
```
 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 
```

---

**Enjoy playing Tic Tac Toe with AI! 🎮✨** 