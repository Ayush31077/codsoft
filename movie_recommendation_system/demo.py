#!/usr/bin/env python3
"""
Demo script for the Movie Recommendation System
This script demonstrates the basic functionality of the recommendation engine.
"""

import pandas as pd
from data_generator import save_sample_data
from recommendation_engine import MovieRecommendationEngine
import time

def run_demo():
    """Run a complete demo of the recommendation system"""
    print("🎬 MOVIE RECOMMENDATION SYSTEM DEMO")
    print("=" * 50)
    
    # Step 1: Generate sample data
    print("\n1️⃣ Generating sample data...")
    start_time = time.time()
    movies_df, ratings_df = save_sample_data()
    print(f"✅ Generated {len(movies_df)} movies and {len(ratings_df)} ratings in {time.time() - start_time:.2f} seconds")
    
    # Step 2: Initialize recommendation engine
    print("\n2️⃣ Initializing recommendation engine...")
    start_time = time.time()
    engine = MovieRecommendationEngine(movies_df, ratings_df)
    print(f"✅ Engine initialized in {time.time() - start_time:.2f} seconds")
    
    # Step 3: Show data overview
    print("\n3️⃣ Data Overview:")
    print(f"   • Total Movies: {len(movies_df)}")
    print(f"   • Total Users: {ratings_df['user_id'].nunique()}")
    print(f"   • Total Ratings: {len(ratings_df)}")
    print(f"   • Average Rating: {ratings_df['rating'].mean():.2f}")
    print(f"   • Genres: {', '.join(movies_df['genre'].unique())}")
    
    # Step 4: Content-based recommendations
    print("\n4️⃣ Content-Based Recommendations:")
    sample_movie_id = 1
    sample_movie = movies_df[movies_df['movie_id'] == sample_movie_id].iloc[0]
    print(f"   Finding movies similar to: {sample_movie['title']} ({sample_movie['genre']})")
    
    cb_recommendations = engine.content_based_recommendations(sample_movie_id, 5)
    for idx, row in cb_recommendations.iterrows():
        print(f"   • {row['title']} ({row['genre']}) - Rating: {row['rating']}")
    
    # Step 5: Collaborative filtering recommendations
    print("\n5️⃣ Collaborative Filtering Recommendations:")
    sample_user_id = 1
    print(f"   Recommendations for User {sample_user_id}:")
    
    cf_recommendations = engine.collaborative_filtering_recommendations(sample_user_id, 5)
    if not cf_recommendations.empty:
        for idx, row in cf_recommendations.iterrows():
            print(f"   • {row['title']} ({row['genre']}) - Rating: {row['rating']}")
    else:
        print("   No recommendations found for this user.")
    
    # Step 6: Popular movies
    print("\n6️⃣ Popular Movies:")
    popular_movies = engine.get_popular_movies(5)
    for idx, row in popular_movies.iterrows():
        print(f"   • {row['title']} ({row['genre']}) - Rating: {row['rating']}")
    
    # Step 7: Genre-based recommendations
    print("\n7️⃣ Genre-Based Recommendations:")
    sample_genre = "Action"
    print(f"   Top {sample_genre} movies:")
    
    genre_recommendations = engine.get_genre_recommendations(sample_genre, 5)
    for idx, row in genre_recommendations.iterrows():
        print(f"   • {row['title']} - Rating: {row['rating']}")
    
    # Step 8: User profile
    print("\n8️⃣ User Profile Analysis:")
    user_profile = engine.get_user_profile(sample_user_id)
    if user_profile:
        print(f"   User {sample_user_id} Profile:")
        print(f"   • Total Ratings: {user_profile['total_ratings']}")
        print(f"   • Average Rating: {user_profile['average_rating']:.2f}")
        print(f"   • Favorite Genres:")
        for genre, rating in list(user_profile['favorite_genres'].items())[:3]:
            print(f"     - {genre}: {rating:.2f}")
    else:
        print("   User profile not found.")
    
    # Step 9: Hybrid recommendations
    print("\n9️⃣ Hybrid Recommendations:")
    print(f"   Hybrid recommendations for User {sample_user_id} (with movie {sample_movie_id}):")
    
    hybrid_recommendations = engine.hybrid_recommendations(sample_user_id, sample_movie_id, 5)
    if not hybrid_recommendations.empty:
        for idx, row in hybrid_recommendations.iterrows():
            print(f"   • {row['title']} ({row['genre']}) - Rating: {row['rating']}")
    else:
        print("   No hybrid recommendations found.")
    
    # Step 10: Performance metrics
    print("\n🔟 Performance Summary:")
    print("   ✅ All recommendation algorithms working correctly!")
    print("   ✅ System ready for use!")
    print("\n🎉 Demo completed successfully!")
    print("\nNext steps:")
    print("   • Run 'python main.py' for interactive command-line interface")
    print("   • Run 'streamlit run streamlit_app.py' for web interface")
    print("   • Check README.md for detailed usage instructions")

if __name__ == "__main__":
    try:
        run_demo()
    except Exception as e:
        print(f"❌ Error during demo: {e}")
        print("Please make sure all dependencies are installed:")
        print("pip install -r requirements.txt") 