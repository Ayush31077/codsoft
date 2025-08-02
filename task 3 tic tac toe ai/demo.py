#!/usr/bin/env python3
"""
Demo script for Tic Tac Toe with AI
This script demonstrates the AI capabilities and different game modes
"""

import time
from game_logic import TicTacToe
from ai_player import SmartAIPlayer

def run_demo():
    """Run a comprehensive demo of the Tic Tac Toe AI system"""
    print("🎮 TIC TAC TOE WITH AI - DEMO")
    print("=" * 50)
    
    # Demo 1: Easy AI vs Easy AI
    print("\n1️⃣ Demo 1: Easy AI vs Easy AI")
    print("-" * 30)
    demo_ai_vs_ai("easy", "easy")
    
    # Demo 2: Medium AI vs Medium AI
    print("\n2️⃣ Demo 2: Medium AI vs Medium AI")
    print("-" * 30)
    demo_ai_vs_ai("medium", "medium")
    
    # Demo 3: Unbeatable AI vs Unbeatable AI
    print("\n3️⃣ Demo 3: Unbeatable AI vs Unbeatable AI")
    print("-" * 30)
    demo_ai_vs_ai("unbeatable", "unbeatable")
    
    # Demo 4: Different difficulty levels
    print("\n4️⃣ Demo 4: Easy vs Unbeatable AI")
    print("-" * 30)
    demo_ai_vs_ai("easy", "unbeatable")
    
    # Demo 5: AI move analysis
    print("\n5️⃣ Demo 5: AI Move Analysis")
    print("-" * 30)
    demo_ai_analysis()
    
    print("\n🎉 Demo completed successfully!")
    print("\nNext steps:")
    print("   • Run 'python main.py' for interactive command-line interface")
    print("   • Run 'streamlit run streamlit_app.py' for web interface")
    print("   • Try different difficulty levels and game modes")

def demo_ai_vs_ai(difficulty1, difficulty2):
    """Demo AI vs AI game"""
    game = TicTacToe()
    ai1 = SmartAIPlayer(difficulty1)
    ai1.set_player_symbol('X')
    ai2 = SmartAIPlayer(difficulty2)
    ai2.set_player_symbol('O')
    
    print(f"🤖 AI 1 (X): {difficulty1.title()}")
    print(f"🤖 AI 2 (O): {difficulty2.title()}")
    print(f"🎯 Starting game...")
    
    move_count = 0
    while not game.game_over and move_count < 9:
        current_ai = ai1 if game.current_player == 'X' else ai2
        current_symbol = game.current_player
        
        print(f"\nMove {move_count + 1}: {current_symbol} ({current_ai.difficulty.title()})")
        
        # Get AI move
        row, col = current_ai.get_move(game)
        position = row * 3 + col + 1
        print(f"   AI chose position: {position}")
        
        # Make move
        game.make_move(row, col)
        move_count += 1
        
        # Display board
        display_board_compact(game)
        
        time.sleep(0.5)  # Small delay for readability
    
    # Game result
    print(f"\n🏁 Game Over!")
    if game.winner == 'Draw':
        print("🤝 Result: Draw")
    else:
        print(f"🎉 Winner: {game.winner}")
    
    print(f"📊 Total moves: {move_count}")

def demo_ai_analysis():
    """Demo AI move analysis"""
    print("🔍 Analyzing AI decision making...")
    
    # Create a specific board position
    game = TicTacToe()
    
    # Set up a specific scenario
    game.board = [
        ['X', 'O', 'X'],
        ['O', 'X', ' '],
        [' ', ' ', 'O']
    ]
    game.current_player = 'X'
    
    print("📋 Board position:")
    display_board_compact(game)
    print(f"🎯 Current player: {game.current_player}")
    
    # Test different AI difficulties
    difficulties = ["easy", "medium", "hard", "unbeatable"]
    
    for difficulty in difficulties:
        ai = SmartAIPlayer(difficulty)
        ai.set_player_symbol('X')
        
        print(f"\n🤖 {difficulty.title()} AI analysis:")
        
        # Get AI move
        start_time = time.time()
        row, col = ai.get_move(game)
        end_time = time.time()
        
        position = row * 3 + col + 1
        print(f"   Recommended move: Position {position}")
        print(f"   Decision time: {(end_time - start_time)*1000:.2f} ms")
        
        # Analyze why this move was chosen
        analyze_move(game, row, col, difficulty)

def analyze_move(game, row, col, difficulty):
    """Analyze why the AI chose a specific move"""
    print(f"   📊 Move analysis:")
    
    # Check if it's a winning move
    game.board[row][col] = 'X'
    if game.check_win(row, col):
        print(f"     ✅ Winning move!")
        game.board[row][col] = ' '
        return
    
    # Check if it blocks opponent's win
    game.board[row][col] = 'O'
    if game.check_win(row, col):
        print(f"     🛡️ Blocking opponent's win")
        game.board[row][col] = ' '
        return
    
    game.board[row][col] = ' '
    
    # Check strategic positions
    strategic_positions = [(0, 0), (0, 2), (2, 0), (2, 2), (1, 1)]
    if (row, col) in strategic_positions:
        if (row, col) == (1, 1):
            print(f"     🎯 Center position (most strategic)")
        else:
            print(f"     🎯 Corner position (strategic)")
    else:
        print(f"     📍 Edge position")

def display_board_compact(game):
    """Display board in compact format"""
    board = game.get_board_for_display()
    for i in range(3):
        row_str = " | ".join(board[i])
        print(f" {row_str} ")
        if i < 2:
            print("-----------")

def test_ai_performance():
    """Test AI performance across different scenarios"""
    print("\n🧪 AI Performance Test")
    print("-" * 30)
    
    scenarios = [
        # Scenario 1: Near win for X
        {
            'board': [['X', 'X', ' '], ['O', 'O', ' '], [' ', ' ', ' ']],
            'player': 'X',
            'description': 'X can win in 1 move'
        },
        # Scenario 2: Near win for O (block needed)
        {
            'board': [['X', 'X', ' '], ['O', 'O', ' '], [' ', ' ', ' ']],
            'player': 'O',
            'description': 'O must block X from winning'
        },
        # Scenario 3: Opening move
        {
            'board': [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']],
            'player': 'X',
            'description': 'Opening move'
        }
    ]
    
    difficulties = ["easy", "medium", "hard", "unbeatable"]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n📋 Scenario {i}: {scenario['description']}")
        
        for difficulty in difficulties:
            game = TicTacToe()
            game.board = [row[:] for row in scenario['board']]
            game.current_player = scenario['player']
            
            ai = SmartAIPlayer(difficulty)
            ai.set_player_symbol(scenario['player'])
            
            start_time = time.time()
            row, col = ai.get_move(game)
            end_time = time.time()
            
            position = row * 3 + col + 1
            print(f"   {difficulty.title()}: Position {position} ({(end_time - start_time)*1000:.2f} ms)")

if __name__ == "__main__":
    try:
        run_demo()
        
        # Optional: Run performance test
        print("\n" + "=" * 50)
        test_ai_performance()
        
    except Exception as e:
        print(f"❌ Error during demo: {e}")
        print("Please make sure all dependencies are installed.") 