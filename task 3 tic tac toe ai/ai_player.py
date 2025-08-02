import random
from typing import Tuple, Optional
from game_logic import TicTacToe

class AIPlayer:
    def __init__(self, difficulty: str = "medium"):
        """
        Initialize AI player with specified difficulty
        difficulty: "easy", "medium", "hard", "unbeatable"
        """
        self.difficulty = difficulty
        self.player_symbol = None
    
    def set_player_symbol(self, symbol: str):
        """Set the AI player's symbol (X or O)"""
        self.player_symbol = symbol
    
    def get_move(self, game: TicTacToe) -> Tuple[int, int]:
        """Get the best move based on difficulty level"""
        if self.difficulty == "easy":
            return self._random_move(game)
        elif self.difficulty == "medium":
            return self._medium_move(game)
        elif self.difficulty == "hard":
            return self._hard_move(game)
        elif self.difficulty == "unbeatable":
            return self._unbeatable_move(game)
        else:
            return self._random_move(game)
    
    def _random_move(self, game: TicTacToe) -> Tuple[int, int]:
        """Make a random move"""
        available_moves = game.get_available_moves()
        return random.choice(available_moves)
    
    def _medium_move(self, game: TicTacToe) -> Tuple[int, int]:
        """Medium difficulty: 70% smart moves, 30% random moves"""
        if random.random() < 0.7:
            return self._smart_move(game)
        else:
            return self._random_move(game)
    
    def _hard_move(self, game: TicTacToe) -> Tuple[int, int]:
        """Hard difficulty: 90% smart moves, 10% random moves"""
        if random.random() < 0.9:
            return self._smart_move(game)
        else:
            return self._random_move(game)
    
    def _unbeatable_move(self, game: TicTacToe) -> Tuple[int, int]:
        """Unbeatable: Always make the best move"""
        return self._smart_move(game)
    
    def _smart_move(self, game: TicTacToe) -> Tuple[int, int]:
        """Make a smart move using minimax algorithm"""
        best_score = float('-inf')
        best_move = None
        
        for move in game.get_available_moves():
            # Make the move
            row, col = move
            game.board[row][col] = self.player_symbol
            
            # Check if this move wins immediately
            if game.check_win(row, col):
                game.board[row][col] = ' '  # Undo move
                return move
            
            # Check if opponent can win next move (block them)
            opponent_symbol = 'O' if self.player_symbol == 'X' else 'X'
            game.board[row][col] = opponent_symbol
            if game.check_win(row, col):
                game.board[row][col] = ' '  # Undo move
                return move
            
            # Use minimax for deeper analysis
            game.board[row][col] = self.player_symbol
            score = self._minimax(game, 0, False, float('-inf'), float('inf'))
            game.board[row][col] = ' '  # Undo move
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move if best_move else game.get_available_moves()[0]
    
    def _minimax(self, game: TicTacToe, depth: int, is_maximizing: bool, 
                 alpha: float, beta: float) -> float:
        """Minimax algorithm with alpha-beta pruning"""
        # Terminal states
        if game.game_over:
            if game.winner == self.player_symbol:
                return 10 - depth
            elif game.winner == 'Draw':
                return 0
            else:
                return depth - 10
        
        if is_maximizing:
            max_eval = float('-inf')
            for move in game.get_available_moves():
                row, col = move
                game.board[row][col] = self.player_symbol
                eval_score = self._minimax(game, depth + 1, False, alpha, beta)
                game.board[row][col] = ' '  # Undo move
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            opponent_symbol = 'O' if self.player_symbol == 'X' else 'X'
            for move in game.get_available_moves():
                row, col = move
                game.board[row][col] = opponent_symbol
                eval_score = self._minimax(game, depth + 1, True, alpha, beta)
                game.board[row][col] = ' '  # Undo move
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval

class SmartAIPlayer(AIPlayer):
    """Enhanced AI player with additional strategies"""
    
    def __init__(self, difficulty: str = "unbeatable"):
        super().__init__(difficulty)
        self.opening_moves = [(0, 0), (0, 2), (2, 0), (2, 2), (1, 1)]
    
    def _smart_move(self, game: TicTacToe) -> Tuple[int, int]:
        """Enhanced smart move with opening strategy"""
        available_moves = game.get_available_moves()
        
        # If it's the first move, prefer corners and center
        if len(game.moves_history) == 0:
            corner_moves = [move for move in available_moves if move in self.opening_moves]
            if corner_moves:
                return random.choice(corner_moves)
        
        # Check for immediate win
        for move in available_moves:
            row, col = move
            game.board[row][col] = self.player_symbol
            if game.check_win(row, col):
                game.board[row][col] = ' '
                return move
            game.board[row][col] = ' '
        
        # Check for opponent's immediate win (block)
        opponent_symbol = 'O' if self.player_symbol == 'X' else 'X'
        for move in available_moves:
            row, col = move
            game.board[row][col] = opponent_symbol
            if game.check_win(row, col):
                game.board[row][col] = ' '
                return move
            game.board[row][col] = ' '
        
        # Use minimax for deeper analysis
        return super()._smart_move(game)
    
    def _minimax(self, game: TicTacToe, depth: int, is_maximizing: bool, 
                 alpha: float, beta: float) -> float:
        """Enhanced minimax with better evaluation"""
        # Terminal states
        if game.game_over:
            if game.winner == self.player_symbol:
                return 100 - depth  # Prefer faster wins
            elif game.winner == 'Draw':
                return 0
            else:
                return depth - 100  # Prefer slower losses
        
        # Early termination for efficiency
        if depth > 6:
            return self._evaluate_position(game)
        
        if is_maximizing:
            max_eval = float('-inf')
            for move in game.get_available_moves():
                row, col = move
                game.board[row][col] = self.player_symbol
                eval_score = self._minimax(game, depth + 1, False, alpha, beta)
                game.board[row][col] = ' '
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            opponent_symbol = 'O' if self.player_symbol == 'X' else 'X'
            for move in game.get_available_moves():
                row, col = move
                game.board[row][col] = opponent_symbol
                eval_score = self._minimax(game, depth + 1, True, alpha, beta)
                game.board[row][col] = ' '
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval
    
    def _evaluate_position(self, game: TicTacToe) -> float:
        """Evaluate board position for non-terminal states"""
        score = 0
        
        # Evaluate rows, columns, and diagonals
        lines = [
            # Rows
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            # Columns
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            # Diagonals
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]
        
        for line in lines:
            line_score = self._evaluate_line(game, line)
            score += line_score
        
        return score
    
    def _evaluate_line(self, game: TicTacToe, line: list) -> float:
        """Evaluate a single line (row, column, or diagonal)"""
        player_count = 0
        opponent_count = 0
        empty_count = 0
        opponent_symbol = 'O' if self.player_symbol == 'X' else 'X'
        
        for row, col in line:
            cell = game.board[row][col]
            if cell == self.player_symbol:
                player_count += 1
            elif cell == opponent_symbol:
                opponent_count += 1
            else:
                empty_count += 1
        
        # Scoring logic
        if player_count == 2 and empty_count == 1:
            return 10  # Two in a row with space
        elif opponent_count == 2 and empty_count == 1:
            return -10  # Opponent has two in a row
        elif player_count == 1 and empty_count == 2:
            return 1  # One with two spaces
        elif opponent_count == 1 and empty_count == 2:
            return -1  # Opponent has one with two spaces
        
        return 0 