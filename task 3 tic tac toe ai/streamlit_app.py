import streamlit as st
import time
from game_logic import TicTacToe
from ai_player import SmartAIPlayer

# Page configuration
st.set_page_config(
    page_title="🎮 Tic Tac Toe with AI",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .game-board {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 10px;
        max-width: 400px;
        margin: 0 auto;
    }
    .cell {
        aspect-ratio: 1;
        border: 2px solid #1f77b4;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        font-weight: bold;
        cursor: pointer;
        background-color: #f0f2f6;
        transition: all 0.3s ease;
    }
    .cell:hover {
        background-color: #e0e0e0;
        transform: scale(1.05);
    }
    .cell.x {
        color: #ff6b6b;
    }
    .cell.o {
        color: #4ecdc4;
    }
    .game-info {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
    .stats-card {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def initialize_game():
    """Initialize a new game"""
    return TicTacToe()

@st.cache_resource
def initialize_ai(difficulty):
    """Initialize AI player"""
    ai = SmartAIPlayer(difficulty)
    return ai

def display_board(game):
    """Display the game board with interactive buttons"""
    st.markdown('<h3 style="text-align: center;">🎯 Game Board</h3>', unsafe_allow_html=True)
    
    # Create a 3x3 grid of buttons
    cols = st.columns(3)
    
    for i in range(3):
        for j in range(3):
            with cols[j]:
                cell_value = game.board[i][j]
                if cell_value == ' ':
                    cell_value = str(i * 3 + j + 1)
                
                # Determine button color and style
                if game.board[i][j] == 'X':
                    button_style = "background-color: #ff6b6b; color: white;"
                elif game.board[i][j] == 'O':
                    button_style = "background-color: #4ecdc4; color: white;"
                else:
                    button_style = "background-color: #f0f2f6; color: #333;"
                
                # Create button
                if st.button(
                    cell_value,
                    key=f"cell_{i}_{j}",
                    use_container_width=True,
                    help=f"Position {i * 3 + j + 1}"
                ):
                    if game.is_valid_move(i, j):
                        st.session_state.last_move = (i, j)
                        st.rerun()

def display_game_info(game, ai_difficulty=None):
    """Display game information"""
    st.markdown('<div class="game-info">', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Current Player", game.current_player)
    
    with col2:
        if game.game_over:
            if game.winner == 'Draw':
                st.metric("Result", "🤝 Draw")
            else:
                st.metric("Result", f"🎉 {game.winner} wins!")
        else:
            st.metric("Status", "Playing")
    
    with col3:
        if ai_difficulty:
            st.metric("AI Difficulty", ai_difficulty.title())
        else:
            st.metric("Moves Made", len(game.moves_history))
    
    st.markdown('</div>', unsafe_allow_html=True)

def display_stats(stats):
    """Display game statistics"""
    st.markdown('<h3>📊 Game Statistics</h3>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f'''
        <div class="stats-card">
            <h4>🏆 Wins</h4>
            <h2>{stats['wins']}</h2>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        st.markdown(f'''
        <div class="stats-card">
            <h4>😔 Losses</h4>
            <h2>{stats['losses']}</h2>
        </div>
        ''', unsafe_allow_html=True)
    
    with col3:
        st.markdown(f'''
        <div class="stats-card">
            <h4>🤝 Draws</h4>
            <h2>{stats['draws']}</h2>
        </div>
        ''', unsafe_allow_html=True)
    
    with col4:
        total = sum(stats.values())
        if total > 0:
            win_rate = (stats['wins'] / total) * 100
            st.markdown(f'''
            <div class="stats-card">
                <h4>📈 Win Rate</h4>
                <h2>{win_rate:.1f}%</h2>
            </div>
            ''', unsafe_allow_html=True)
        else:
            st.markdown(f'''
            <div class="stats-card">
                <h4>📈 Win Rate</h4>
                <h2>0%</h2>
            </div>
            ''', unsafe_allow_html=True)

def main():
    # Initialize session state
    if 'game' not in st.session_state:
        st.session_state.game = initialize_game()
    if 'stats' not in st.session_state:
        st.session_state.stats = {'wins': 0, 'losses': 0, 'draws': 0}
    if 'game_mode' not in st.session_state:
        st.session_state.game_mode = None
    if 'ai_difficulty' not in st.session_state:
        st.session_state.ai_difficulty = None
    if 'player_symbol' not in st.session_state:
        st.session_state.player_symbol = 'X'
    if 'ai_symbol' not in st.session_state:
        st.session_state.ai_symbol = 'O'
    if 'ai_player' not in st.session_state:
        st.session_state.ai_player = None
    if 'last_move' not in st.session_state:
        st.session_state.last_move = None

    # Header
    st.markdown('<h1 class="main-header">🎮 Tic Tac Toe with AI</h1>', unsafe_allow_html=True)
    
    # Sidebar for game controls
    with st.sidebar:
        st.title("🎮 Game Controls")
        
        # Game mode selection
        st.subheader("Game Mode")
        game_mode = st.selectbox(
            "Choose game mode:",
            ["Player vs Player", "Player vs AI", "AI vs AI"]
        )
        
        if game_mode != st.session_state.game_mode:
            st.session_state.game_mode = game_mode
            st.session_state.game.reset_game()
            st.session_state.last_move = None
        
        # AI difficulty selection
        if "AI" in game_mode:
            st.subheader("AI Settings")
            ai_difficulty = st.selectbox(
                "AI Difficulty:",
                ["Easy", "Medium", "Hard", "Unbeatable"]
            )
            
            if ai_difficulty != st.session_state.ai_difficulty:
                st.session_state.ai_difficulty = ai_difficulty.lower()
                st.session_state.ai_player = initialize_ai(st.session_state.ai_difficulty)
        
        # Player symbol selection (for PvE)
        if game_mode == "Player vs AI":
            st.subheader("Player Settings")
            player_symbol = st.selectbox(
                "Your symbol:",
                ["X (First)", "O (Second)"]
            )
            
            if player_symbol == "X (First)":
                st.session_state.player_symbol = 'X'
                st.session_state.ai_symbol = 'O'
            else:
                st.session_state.player_symbol = 'O'
                st.session_state.ai_symbol = 'X'
            
            if st.session_state.ai_player:
                st.session_state.ai_player.set_player_symbol(st.session_state.ai_symbol)
        
        # Game controls
        st.subheader("Game Controls")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🔄 New Game"):
                st.session_state.game.reset_game()
                st.session_state.last_move = None
                st.rerun()
        
        with col2:
            if st.button("📊 Reset Stats"):
                st.session_state.stats = {'wins': 0, 'losses': 0, 'draws': 0}
                st.rerun()
        
        # Display current game info
        st.subheader("Current Game")
        st.write(f"Mode: {game_mode}")
        if "AI" in game_mode:
            st.write(f"AI Difficulty: {st.session_state.ai_difficulty.title()}")
        if game_mode == "Player vs AI":
            st.write(f"Your Symbol: {st.session_state.player_symbol}")
    
    # Main game area
    game = st.session_state.game
    
    # Handle last move
    if st.session_state.last_move:
        row, col = st.session_state.last_move
        if game.make_move(row, col):
            st.session_state.last_move = None
            
            # Update stats if game is over
            if game.game_over and game_mode == "Player vs AI":
                if game.winner == st.session_state.player_symbol:
                    st.session_state.stats['wins'] += 1
                elif game.winner == st.session_state.ai_symbol:
                    st.session_state.stats['losses'] += 1
                elif game.winner == 'Draw':
                    st.session_state.stats['draws'] += 1
    
    # AI move for PvE
    if (game_mode == "Player vs AI" and 
        not game.game_over and 
        game.current_player == st.session_state.ai_symbol and
        st.session_state.ai_player):
        
        with st.spinner(f"🤖 AI ({st.session_state.ai_difficulty.title()}) is thinking..."):
            time.sleep(1)  # Add delay for better UX
            row, col = st.session_state.ai_player.get_move(game)
            game.make_move(row, col)
            
            # Update stats if game is over
            if game.game_over:
                if game.winner == st.session_state.player_symbol:
                    st.session_state.stats['wins'] += 1
                elif game.winner == st.session_state.ai_symbol:
                    st.session_state.stats['losses'] += 1
                elif game.winner == 'Draw':
                    st.session_state.stats['draws'] += 1
    
    # AI vs AI mode
    if game_mode == "AI vs AI" and not game.game_over:
        if 'ai1' not in st.session_state:
            st.session_state.ai1 = SmartAIPlayer(st.session_state.ai_difficulty)
            st.session_state.ai1.set_player_symbol('X')
            st.session_state.ai2 = SmartAIPlayer(st.session_state.ai_difficulty)
            st.session_state.ai2.set_player_symbol('O')
        
        current_ai = st.session_state.ai1 if game.current_player == 'X' else st.session_state.ai2
        
        with st.spinner(f"🤖 {game.current_player} ({st.session_state.ai_difficulty.title()}) thinking..."):
            time.sleep(1.5)
            row, col = current_ai.get_move(game)
            game.make_move(row, col)
    
    # Display game board
    display_board(game)
    
    # Display game information
    display_game_info(game, st.session_state.ai_difficulty)
    
    # Display statistics
    if game_mode == "Player vs AI":
        display_stats(st.session_state.stats)
    
    # Game over message
    if game.game_over:
        st.markdown("---")
        if game.winner == 'Draw':
            st.success("🤝 It's a Draw!")
        else:
            st.success(f"🎉 {game.winner} wins!")
        
        if st.button("🔄 Play Again"):
            st.session_state.game.reset_game()
            st.session_state.last_move = None
            st.rerun()

if __name__ == "__main__":
    main() 