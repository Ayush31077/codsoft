import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from recommendation_engine import MovieRecommendationEngine
from data_generator import save_sample_data
import time

# Page configuration
st.set_page_config(
    page_title="🎬 Movie Recommendation System",
    page_icon="🎬",
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
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .recommendation-card {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #e0e0e0;
        margin-bottom: 0.5rem;
    }
    .stButton > button {
        width: 100%;
        border-radius: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    """Load or generate movie data"""
    try:
        movies_df = pd.read_csv('movies.csv')
        ratings_df = pd.read_csv('ratings.csv')
        return movies_df, ratings_df
    except FileNotFoundError:
        with st.spinner("Generating sample data..."):
            movies_df, ratings_df = save_sample_data()
        return movies_df, ratings_df

@st.cache_resource
def initialize_engine(movies_df, ratings_df):
    """Initialize the recommendation engine"""
    with st.spinner("Initializing recommendation engine..."):
        engine = MovieRecommendationEngine(movies_df, ratings_df)
    return engine

def main():
    # Header
    st.markdown('<h1 class="main-header">🎬 Movie Recommendation System</h1>', unsafe_allow_html=True)
    
    # Load data
    movies_df, ratings_df = load_data()
    
    # Initialize engine
    engine = initialize_engine(movies_df, ratings_df)
    
    # Sidebar
    st.sidebar.title("🎯 Navigation")
    page = st.sidebar.selectbox(
        "Choose a page:",
        ["🏠 Dashboard", "🎬 Get Recommendations", "👤 User Profiles", "📊 Analytics", "🔍 Search Movies"]
    )
    
    if page == "🏠 Dashboard":
        show_dashboard(movies_df, ratings_df, engine)
    elif page == "🎬 Get Recommendations":
        show_recommendations(movies_df, engine)
    elif page == "👤 User Profiles":
        show_user_profiles(engine)
    elif page == "📊 Analytics":
        show_analytics(movies_df, ratings_df)
    elif page == "🔍 Search Movies":
        show_search(movies_df)

def show_dashboard(movies_df, ratings_df, engine):
    """Show the main dashboard"""
    st.header("📊 Dashboard Overview")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Movies", len(movies_df))
    
    with col2:
        st.metric("Total Users", ratings_df['user_id'].nunique())
    
    with col3:
        st.metric("Total Ratings", len(ratings_df))
    
    with col4:
        st.metric("Avg Rating", f"{ratings_df['rating'].mean():.2f}")
    
    # Quick recommendations
    st.subheader("🔥 Popular Movies")
    popular_movies = engine.get_popular_movies(5)
    
    for idx, row in popular_movies.iterrows():
        with st.container():
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**{row['title']}**")
            with col2:
                st.write(f"🎭 {row['genre']}")
            with col3:
                st.write(f"⭐ {row['rating']}")
    
    # Genre distribution
    st.subheader("🎭 Genre Distribution")
    genre_counts = movies_df['genre'].value_counts()
    fig = px.pie(values=genre_counts.values, names=genre_counts.index, title="Movies by Genre")
    st.plotly_chart(fig, use_container_width=True)

def show_recommendations(movies_df, engine):
    """Show recommendation options"""
    st.header("🎬 Get Movie Recommendations")
    
    # Recommendation type selection
    rec_type = st.selectbox(
        "Choose recommendation type:",
        ["Content-Based", "Collaborative Filtering", "Hybrid", "Genre-Based", "Popular Movies"]
    )
    
    if rec_type == "Content-Based":
        st.subheader("🎯 Content-Based Recommendations")
        st.write("Get recommendations based on movie similarity")
        
        # Movie selection
        selected_movie = st.selectbox(
            "Select a movie you like:",
            movies_df['title'].tolist()
        )
        
        if st.button("Get Recommendations"):
            movie_id = movies_df[movies_df['title'] == selected_movie]['movie_id'].iloc[0]
            recommendations = engine.content_based_recommendations(movie_id, 10)
            
            st.subheader(f"Movies similar to '{selected_movie}':")
            for idx, row in recommendations.iterrows():
                with st.container():
                    col1, col2, col3 = st.columns([3, 1, 1])
                    with col1:
                        st.write(f"**{row['title']}**")
                    with col2:
                        st.write(f"🎭 {row['genre']}")
                    with col3:
                        st.write(f"⭐ {row['rating']}")
    
    elif rec_type == "Collaborative Filtering":
        st.subheader("👥 Collaborative Filtering Recommendations")
        st.write("Get recommendations based on similar users")
        
        user_id = st.number_input("Enter User ID (1-500):", min_value=1, max_value=500, value=1)
        
        if st.button("Get Recommendations"):
            recommendations = engine.collaborative_filtering_recommendations(user_id, 10)
            
            if not recommendations.empty:
                st.subheader(f"Recommended movies for User {user_id}:")
                for idx, row in recommendations.iterrows():
                    with st.container():
                        col1, col2, col3 = st.columns([3, 1, 1])
                        with col1:
                            st.write(f"**{row['title']}**")
                        with col2:
                            st.write(f"🎭 {row['genre']}")
                        with col3:
                            st.write(f"⭐ {row['rating']}")
            else:
                st.warning("No recommendations found for this user.")
    
    elif rec_type == "Hybrid":
        st.subheader("🔄 Hybrid Recommendations")
        st.write("Combine content-based and collaborative filtering")
        
        col1, col2 = st.columns(2)
        with col1:
            user_id = st.number_input("User ID (1-500):", min_value=1, max_value=500, value=1)
        with col2:
            selected_movie = st.selectbox(
                "Select a movie you like (optional):",
                ["None"] + movies_df['title'].tolist()
            )
        
        if st.button("Get Hybrid Recommendations"):
            movie_id = None
            if selected_movie != "None":
                movie_id = movies_df[movies_df['title'] == selected_movie]['movie_id'].iloc[0]
            
            recommendations = engine.hybrid_recommendations(user_id, movie_id, 10)
            
            if not recommendations.empty:
                st.subheader(f"Hybrid recommendations for User {user_id}:")
                for idx, row in recommendations.iterrows():
                    with st.container():
                        col1, col2, col3 = st.columns([3, 1, 1])
                        with col1:
                            st.write(f"**{row['title']}**")
                        with col2:
                            st.write(f"🎭 {row['genre']}")
                        with col3:
                            st.write(f"⭐ {row['rating']}")
            else:
                st.warning("No recommendations found.")
    
    elif rec_type == "Genre-Based":
        st.subheader("🎭 Genre-Based Recommendations")
        st.write("Get top movies by genre")
        
        genre = st.selectbox("Select genre:", movies_df['genre'].unique())
        
        if st.button("Get Genre Recommendations"):
            recommendations = engine.get_genre_recommendations(genre, 10)
            
            st.subheader(f"Top {genre} Movies:")
            for idx, row in recommendations.iterrows():
                with st.container():
                    col1, col2, col3 = st.columns([3, 1, 1])
                    with col1:
                        st.write(f"**{row['title']}**")
                    with col2:
                        st.write(f"🎭 {row['genre']}")
                    with col3:
                        st.write(f"⭐ {row['rating']}")
    
    elif rec_type == "Popular Movies":
        st.subheader("🔥 Popular Movies")
        st.write("Most popular movies based on ratings")
        
        n_movies = st.slider("Number of movies:", 5, 20, 10)
        
        if st.button("Get Popular Movies"):
            recommendations = engine.get_popular_movies(n_movies)
            
            st.subheader("Most Popular Movies:")
            for idx, row in recommendations.iterrows():
                with st.container():
                    col1, col2, col3 = st.columns([3, 1, 1])
                    with col1:
                        st.write(f"**{row['title']}**")
                    with col2:
                        st.write(f"🎭 {row['genre']}")
                    with col3:
                        st.write(f"⭐ {row['rating']}")

def show_user_profiles(engine):
    """Show user profile analysis"""
    st.header("👤 User Profiles")
    
    user_id = st.number_input("Enter User ID (1-500):", min_value=1, max_value=500, value=1)
    
    if st.button("View Profile"):
        profile = engine.get_user_profile(user_id)
        
        if profile:
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📊 User Statistics")
                st.metric("Total Ratings", profile['total_ratings'])
                st.metric("Average Rating", f"{profile['average_rating']:.2f}")
            
            with col2:
                st.subheader("🎭 Favorite Genres")
                for genre, rating in profile['favorite_genres'].items():
                    st.write(f"**{genre}**: {rating:.2f}")
            
            st.subheader("📝 Recent Ratings")
            recent_ratings = profile['recent_ratings']
            for idx, row in recent_ratings.iterrows():
                with st.container():
                    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
                    with col1:
                        st.write(f"**{row['title']}**")
                    with col2:
                        st.write(f"🎭 {row['genre']}")
                    with col3:
                        st.write(f"⭐ {row['rating']}")
                    with col4:
                        st.write(f"📅 {row['timestamp'].split()[0]}")
        else:
            st.error("User not found!")

def show_analytics(movies_df, ratings_df):
    """Show data analytics and visualizations"""
    st.header("📊 Analytics")
    
    # Rating distribution
    st.subheader("⭐ Rating Distribution")
    rating_counts = ratings_df['rating'].value_counts().sort_index()
    fig = px.bar(x=rating_counts.index, y=rating_counts.values, 
                 title="Distribution of Ratings",
                 labels={'x': 'Rating', 'y': 'Count'})
    st.plotly_chart(fig, use_container_width=True)
    
    # Average rating by genre
    st.subheader("🎭 Average Rating by Genre")
    genre_ratings = ratings_df.merge(movies_df, on='movie_id').groupby('genre')['rating'].mean().sort_values(ascending=False)
    fig = px.bar(x=genre_ratings.index, y=genre_ratings.values,
                 title="Average Rating by Genre",
                 labels={'x': 'Genre', 'y': 'Average Rating'})
    fig.update_xaxes(tickangle=45)
    st.plotly_chart(fig, use_container_width=True)
    
    # Movies by year
    st.subheader("📅 Movies by Year")
    year_counts = movies_df['year'].value_counts().sort_index()
    fig = px.line(x=year_counts.index, y=year_counts.values,
                  title="Number of Movies by Year",
                  labels={'x': 'Year', 'y': 'Number of Movies'})
    st.plotly_chart(fig, use_container_width=True)

def show_search(movies_df):
    """Show movie search functionality"""
    st.header("🔍 Search Movies")
    
    # Search by title
    search_term = st.text_input("Search movies by title:")
    
    if search_term:
        filtered_movies = movies_df[movies_df['title'].str.contains(search_term, case=False)]
        
        if not filtered_movies.empty:
            st.subheader(f"Search results for '{search_term}':")
            for idx, row in filtered_movies.iterrows():
                with st.container():
                    col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
                    with col1:
                        st.write(f"**{row['title']}**")
                    with col2:
                        st.write(f"🎭 {row['genre']}")
                    with col3:
                        st.write(f"⭐ {row['rating']}")
                    with col4:
                        st.write(f"📅 {row['year']}")
        else:
            st.info("No movies found matching your search.")
    
    # Filter by genre
    st.subheader("Filter by Genre")
    selected_genre = st.selectbox("Select genre:", ["All"] + movies_df['genre'].unique().tolist())
    
    if selected_genre != "All":
        genre_movies = movies_df[movies_df['genre'] == selected_genre]
        st.subheader(f"Movies in {selected_genre} genre:")
        
        for idx, row in genre_movies.head(20).iterrows():
            with st.container():
                col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
                with col1:
                    st.write(f"**{row['title']}**")
                with col2:
                    st.write(f"🎭 {row['genre']}")
                with col3:
                    st.write(f"⭐ {row['rating']}")
                with col4:
                    st.write(f"📅 {row['year']}")

if __name__ == "__main__":
    main() 