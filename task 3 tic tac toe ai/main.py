#!/usr/bin/env python3
"""
Tic Tac Toe with AI - Main Game Interface
A comprehensive Tic Tac Toe game with multiple AI difficulty levels
"""

import os
import time
from game_logic import TicTacToe
from ai_player import AIPlayer, SmartAIPlayer

class TicTacToeGame:
    def __init__(self):
        self.game = TicTacToe()
        self.ai_player = None
        self.game_mode = None
        self.player_symbol = 'X'
        self.ai_symbol = 'O'
        self.stats = {'wins': 0, 'losses': 0, 'draws': 0}
    
    def clear_screen(self):
        """Clear the console screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_title(self):
        """Display the game title"""
        print("=" * 50)
        print("🎮 TIC TAC TOE WITH AI 🎮")
        print("=" * 50)
    
    def display_board(self):
        """Display the current game board"""
        print("\n" + "=" * 30)
        print("🎯 GAME BOARD")
        print("=" * 30)
        
        board = self.game.get_board_for_display()
        for i in range(3):
            print(f" {' | '.join(board[i])} ")
            if i < 2:
                print("-----------")
        
        print("\n" + "=" * 30)
        print(f"📊 Game State: {self.game.get_game_state()}")
        print("=" * 30)
    
    def display_stats(self):
        """Display game statistics"""
        print(f"\n📈 GAME STATISTICS:")
        print(f"   Wins: {self.stats['wins']}")
        print(f"   Losses: {self.stats['losses']}")
        print(f"   Draws: {self.stats['draws']}")
        total = sum(self.stats.values())
        if total > 0:
            win_rate = (self.stats['wins'] / total) * 100
            print(f"   Win Rate: {win_rate:.1f}%")
    
    def get_game_mode(self):
        """Get game mode from user"""
        print("\n🎮 SELECT GAME MODE:")
        print("1. Player vs Player")
        print("2. Player vs AI")
        print("3. AI vs AI")
        print("4. View Statistics")
        print("5. Exit")
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-5): "))
                if choice == 1:
                    return "pvp"
                elif choice == 2:
                    return "pve"
                elif choice == 3:
                    return "ai_vs_ai"
                elif choice == 4:
                    return "stats"
                elif choice == 5:
                    return "exit"
                else:
                    print("❌ Please enter a number between 1 and 5.")
            except ValueError:
                print("❌ Please enter a valid number.")
    
    def get_ai_difficulty(self):
        """Get AI difficulty from user"""
        print("\n🤖 SELECT AI DIFFICULTY:")
        print("1. Easy (Random moves)")
        print("2. Medium (70% smart, 30% random)")
        print("3. Hard (90% smart, 10% random)")
        print("4. Unbeatable (Perfect play)")
        
        while True:
            try:
                choice = int(input("\nEnter difficulty (1-4): "))
                difficulties = {1: "easy", 2: "medium", 3: "hard", 4: "unbeatable"}
                if choice in difficulties:
                    return difficulties[choice]
                else:
                    print("❌ Please enter a number between 1 and 4.")
            except ValueError:
                print("❌ Please enter a valid number.")
    
    def get_player_symbol(self):
        """Let player choose their symbol"""
        print("\n🎯 CHOOSE YOUR SYMBOL:")
        print("1. X (Goes first)")
        print("2. O (Goes second)")
        
        while True:
            try:
                choice = int(input("\nEnter your choice (1-2): "))
                if choice == 1:
                    return 'X', 'O'
                elif choice == 2:
                    return 'O', 'X'
                else:
                    print("❌ Please enter 1 or 2.")
            except ValueError:
                print("❌ Please enter a valid number.")
    
    def get_player_move(self):
        """Get move from human player"""
        print(f"\n🎯 Your turn ({self.player_symbol})!")
        print("Enter position (1-9):")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        
        while True:
            try:
                position = int(input("\nEnter position (1-9): "))
                if 1 <= position <= 9:
                    # Convert position to row, col
                    row = (position - 1) // 3
                    col = (position - 1) % 3
                    
                    if self.game.is_valid_move(row, col):
                        return row, col
                    else:
                        print("❌ That position is already taken!")
                else:
                    print("❌ Please enter a number between 1 and 9.")
            except ValueError:
                print("❌ Please enter a valid number.")
    
    def get_ai_move(self):
        """Get move from AI player"""
        print(f"\n🤖 AI thinking... ({self.ai_symbol})")
        time.sleep(1)  # Add some delay for better UX
        
        move = self.ai_player.get_move(self.game)
        print(f"AI chose position: {move[0] * 3 + move[1] + 1}")
        return move
    
    def play_pvp_game(self):
        """Play Player vs Player game"""
        print("\n🎮 PLAYER VS PLAYER MODE")
        print("=" * 30)
        
        while not self.game.game_over:
            self.clear_screen()
            self.display_title()
            self.display_board()
            
            current_symbol = self.game.current_player
            print(f"\n🎯 {current_symbol}'s turn!")
            
            row, col = self.get_player_move()
            self.game.make_move(row, col)
        
        self.clear_screen()
        self.display_title()
        self.display_board()
        self.display_game_result()
    
    def play_pve_game(self):
        """Play Player vs AI game"""
        print("\n🎮 PLAYER VS AI MODE")
        print("=" * 30)
        
        # Setup AI
        difficulty = self.get_ai_difficulty()
        self.ai_player = SmartAIPlayer(difficulty)
        self.ai_player.set_player_symbol(self.ai_symbol)
        
        # Let player choose symbol
        self.player_symbol, self.ai_symbol = self.get_player_symbol()
        self.ai_player.set_player_symbol(self.ai_symbol)
        
        print(f"\n🎯 You are: {self.player_symbol}")
        print(f"🤖 AI is: {self.ai_symbol} (Difficulty: {difficulty.title()})")
        
        while not self.game.game_over:
            self.clear_screen()
            self.display_title()
            self.display_board()
            
            if self.game.current_player == self.player_symbol:
                # Player's turn
                row, col = self.get_player_move()
                self.game.make_move(row, col)
            else:
                # AI's turn
                row, col = self.get_ai_move()
                self.game.make_move(row, col)
        
        self.clear_screen()
        self.display_title()
        self.display_board()
        self.update_stats()
        self.display_game_result()
    
    def play_ai_vs_ai_game(self):
        """Play AI vs AI game"""
        print("\n🎮 AI VS AI MODE")
        print("=" * 30)
        
        # Setup both AIs
        print("🤖 AI 1 (X):")
        ai1_difficulty = self.get_ai_difficulty()
        ai1 = SmartAIPlayer(ai1_difficulty)
        ai1.set_player_symbol('X')
        
        print("\n🤖 AI 2 (O):")
        ai2_difficulty = self.get_ai_difficulty()
        ai2 = SmartAIPlayer(ai2_difficulty)
        ai2.set_player_symbol('O')
        
        print(f"\n🤖 AI 1: {ai1_difficulty.title()} | AI 2: {ai2_difficulty.title()}")
        input("\nPress Enter to start the AI battle...")
        
        while not self.game.game_over:
            self.clear_screen()
            self.display_title()
            self.display_board()
            
            current_ai = ai1 if self.game.current_player == 'X' else ai2
            current_symbol = self.game.current_player
            
            print(f"\n🤖 {current_symbol} ({current_ai.difficulty.title()}) thinking...")
            time.sleep(1.5)
            
            row, col = current_ai.get_move(self.game)
            self.game.make_move(row, col)
        
        self.clear_screen()
        self.display_title()
        self.display_board()
        self.display_game_result()
    
    def update_stats(self):
        """Update game statistics"""
        if self.game.winner == self.player_symbol:
            self.stats['wins'] += 1
        elif self.game.winner == self.ai_symbol:
            self.stats['losses'] += 1
        elif self.game.winner == 'Draw':
            self.stats['draws'] += 1
    
    def display_game_result(self):
        """Display the final game result"""
        print("\n" + "=" * 40)
        print("🏁 GAME OVER!")
        print("=" * 40)
        
        if self.game.winner == 'Draw':
            print("🤝 It's a Draw!")
        else:
            print(f"🎉 {self.game.winner} wins!")
        
        if self.game_mode == "pve":
            self.display_stats()
        
        print("\n" + "=" * 40)
    
    def show_statistics(self):
        """Show game statistics"""
        self.clear_screen()
        self.display_title()
        self.display_stats()
        
        if sum(self.stats.values()) == 0:
            print("\n📊 No games played yet!")
        else:
            total = sum(self.stats.values())
            print(f"\n📊 Total Games: {total}")
        
        input("\nPress Enter to continue...")
    
    def reset_stats(self):
        """Reset game statistics"""
        self.stats = {'wins': 0, 'losses': 0, 'draws': 0}
        print("✅ Statistics reset!")
    
    def run(self):
        """Main game loop"""
        while True:
            self.clear_screen()
            self.display_title()
            
            # Reset game for new round
            self.game.reset_game()
            
            # Get game mode
            self.game_mode = self.get_game_mode()
            
            if self.game_mode == "exit":
                print("\n👋 Thanks for playing!")
                break
            elif self.game_mode == "stats":
                self.show_statistics()
                continue
            elif self.game_mode == "pvp":
                self.play_pvp_game()
            elif self.game_mode == "pve":
                self.play_pve_game()
            elif self.game_mode == "ai_vs_ai":
                self.play_ai_vs_ai_game()
            
            # Ask if player wants to play again
            if self.game_mode in ["pvp", "pve", "ai_vs_ai"]:
                print("\n🔄 Play again? (y/n): ", end="")
                play_again = input().lower().strip()
                if play_again not in ['y', 'yes']:
                    print("\n👋 Thanks for playing!")
                    break

def main():
    """Main function"""
    game = TicTacToeGame()
    try:
        game.run()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")

if __name__ == "__main__":
    main() 