import random
from typing import List, Tuple, Optional

class TicTacToe:
    def __init__(self):
        """Initialize a new Tic Tac Toe game"""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        self.moves_history = []
    
    def reset_game(self):
        """Reset the game to initial state"""
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
        self.moves_history = []
    
    def get_board(self) -> List[List[str]]:
        """Get current board state"""
        return [row[:] for row in self.board]
    
    def get_available_moves(self) -> List[Tuple[int, int]]:
        """Get list of available moves (empty positions)"""
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    moves.append((i, j))
        return moves
    
    def is_valid_move(self, row: int, col: int) -> bool:
        """Check if a move is valid"""
        return (0 <= row < 3 and 0 <= col < 3 and 
                self.board[row][col] == ' ' and 
                not self.game_over)
    
    def make_move(self, row: int, col: int) -> bool:
        """Make a move and return True if successful"""
        if not self.is_valid_move(row, col):
            return False
        
        self.board[row][col] = self.current_player
        self.moves_history.append((row, col, self.current_player))
        
        # Check for win
        if self.check_win(row, col):
            self.game_over = True
            self.winner = self.current_player
        # Check for draw
        elif len(self.get_available_moves()) == 0:
            self.game_over = True
            self.winner = 'Draw'
        else:
            # Switch players
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        
        return True
    
    def check_win(self, row: int, col: int) -> bool:
        """Check if the last move resulted in a win"""
        player = self.board[row][col]
        
        # Check row
        if all(self.board[row][i] == player for i in range(3)):
            return True
        
        # Check column
        if all(self.board[i][col] == player for i in range(3)):
            return True
        
        # Check diagonals
        if row == col and all(self.board[i][i] == player for i in range(3)):
            return True
        
        if row + col == 2 and all(self.board[i][2-i] == player for i in range(3)):
            return True
        
        return False
    
    def get_game_state(self) -> str:
        """Get current game state"""
        if self.game_over:
            if self.winner == 'Draw':
                return "Draw"
            else:
                return f"{self.winner} wins!"
        else:
            return f"{self.current_player}'s turn"
    
    def display_board(self) -> str:
        """Return a string representation of the board"""
        board_str = ""
        for i in range(3):
            board_str += " " + " | ".join(self.board[i]) + " \n"
            if i < 2:
                board_str += "-----------\n"
        return board_str
    
    def get_board_for_display(self) -> List[List[str]]:
        """Get board with numbered positions for display"""
        display_board = []
        for i in range(3):
            row = []
            for j in range(3):
                if self.board[i][j] == ' ':
                    row.append(str(i * 3 + j + 1))
                else:
                    row.append(self.board[i][j])
            display_board.append(row)
        return display_board
    
    def undo_last_move(self) -> bool:
        """Undo the last move"""
        if not self.moves_history:
            return False
        
        row, col, player = self.moves_history.pop()
        self.board[row][col] = ' '
        self.current_player = player
        self.game_over = False
        self.winner = None
        
        return True
    
    def get_score(self, player: str) -> int:
        """Get score for a player (1 for win, -1 for loss, 0 for draw)"""
        if not self.game_over:
            return 0
        
        if self.winner == player:
            return 1
        elif self.winner == 'Draw':
            return 0
        else:
            return -1 