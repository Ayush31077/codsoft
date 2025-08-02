import pandas as pd
import numpy as np
from data_generator import save_sample_data
from recommendation_engine import MovieRecommendationEngine
import matplotlib.pyplot as plt
import seaborn as sns

def display_menu():
    """Display the main menu options"""
    print("\n" + "="*50)
    print("🎬 MOVIE RECOMMENDATION SYSTEM 🎬")
    print("="*50)
    print("1. Generate Sample Data")
    print("2. Load Data and Initialize Engine")
    print("3. Get Content-Based Recommendations")
    print("4. Get Collaborative Filtering Recommendations")
    print("5. Get Hybrid Recommendations")
    print("6. Get Popular Movies")
    print("7. Get Genre-Based Recommendations")
    print("8. View User Profile")
    print("9. Show Data Statistics")
    print("10. Exit")
    print("="*50)

def generate_data():
    """Generate sample movie data"""
    print("Generating sample data...")
    movies_df, ratings_df = save_sample_data()
    print("✅ Sample data generated successfully!")
    return movies_df, ratings_df

def load_data():
    """Load data from CSV files"""
    try:
        movies_df = pd.read_csv('movies.csv')
        ratings_df = pd.read_csv('ratings.csv')
        print("✅ Data loaded successfully!")
        return movies_df, ratings_df
    except FileNotFoundError:
        print("❌ Data files not found. Please generate sample data first.")
        return None, None

def show_data_statistics(movies_df, ratings_df):
    """Display data statistics and visualizations"""
    if movies_df is None or ratings_df is None:
        print("❌ No data available. Please load data first.")
        return
    
    print("\n📊 DATA STATISTICS")
    print("-" * 30)
    print(f"Total Movies: {len(movies_df)}")
    print(f"Total Users: {ratings_df['user_id'].nunique()}")
    print(f"Total Ratings: {len(ratings_df)}")
    print(f"Average Rating: {ratings_df['rating'].mean():.2f}")
    
    # Genre distribution
    print(f"\n🎭 Top 5 Genres:")
    genre_counts = movies_df['genre'].value_counts().head(5)
    for genre, count in genre_counts.items():
        print(f"  {genre}: {count} movies")
    
    # Rating distribution
    print(f"\n⭐ Rating Distribution:")
    rating_counts = ratings_df['rating'].value_counts().sort_index()
    for rating, count in rating_counts.items():
        print(f"  {rating} stars: {count} ratings")
    
    # Create visualizations
    try:
        plt.figure(figsize=(15, 5))
        
        # Genre distribution plot
        plt.subplot(1, 3, 1)
        movies_df['genre'].value_counts().head(10).plot(kind='bar')
        plt.title('Top 10 Movie Genres')
        plt.xticks(rotation=45)
        plt.ylabel('Number of Movies')
        
        # Rating distribution plot
        plt.subplot(1, 3, 2)
        ratings_df['rating'].value_counts().sort_index().plot(kind='bar')
        plt.title('Rating Distribution')
        plt.xlabel('Rating')
        plt.ylabel('Number of Ratings')
        
        # Average rating by genre
        plt.subplot(1, 3, 3)
        genre_ratings = ratings_df.merge(movies_df, on='movie_id').groupby('genre')['rating'].mean().sort_values(ascending=False)
        genre_ratings.head(10).plot(kind='bar')
        plt.title('Average Rating by Genre')
        plt.xticks(rotation=45)
        plt.ylabel('Average Rating')
        
        plt.tight_layout()
        plt.savefig('data_statistics.png', dpi=300, bbox_inches='tight')
        print("\n📈 Visualization saved as 'data_statistics.png'")
        plt.show()
        
    except Exception as e:
        print(f"Could not create visualization: {e}")

def get_content_based_recommendations(engine):
    """Get content-based recommendations"""
    print("\n🎯 CONTENT-BASED RECOMMENDATIONS")
    print("-" * 40)
    
    # Show some sample movies
    print("Available movies (first 10):")
    for idx, row in engine.movies_df.head(10).iterrows():
        print(f"{row['movie_id']}: {row['title']} ({row['genre']})")
    
    try:
        movie_id = int(input("\nEnter movie ID for recommendations: "))
        
        if movie_id not in engine.movies_df['movie_id'].values:
            print("❌ Invalid movie ID!")
            return
        
        recommendations = engine.content_based_recommendations(movie_id, 10)
        
        print(f"\n🎬 Movies similar to '{engine.movies_df[engine.movies_df['movie_id'] == movie_id]['title'].iloc[0]}':")
        print("-" * 60)
        for idx, row in recommendations.iterrows():
            print(f"• {row['title']} ({row['genre']}) - Rating: {row['rating']}")
            
    except ValueError:
        print("❌ Please enter a valid movie ID!")

def get_collaborative_recommendations(engine):
    """Get collaborative filtering recommendations"""
    print("\n👥 COLLABORATIVE FILTERING RECOMMENDATIONS")
    print("-" * 45)
    
    try:
        user_id = int(input("Enter user ID (1-500): "))
        
        if user_id < 1 or user_id > 500:
            print("❌ User ID must be between 1 and 500!")
            return
        
        recommendations = engine.collaborative_filtering_recommendations(user_id, 10)
        
        if recommendations.empty:
            print("❌ No recommendations found for this user!")
            return
        
        print(f"\n🎬 Recommended movies for User {user_id}:")
        print("-" * 50)
        for idx, row in recommendations.iterrows():
            print(f"• {row['title']} ({row['genre']}) - Rating: {row['rating']}")
            
    except ValueError:
        print("❌ Please enter a valid user ID!")

def get_hybrid_recommendations(engine):
    """Get hybrid recommendations"""
    print("\n🔄 HYBRID RECOMMENDATIONS")
    print("-" * 30)
    
    try:
        user_id = int(input("Enter user ID (1-500): "))
        movie_id = int(input("Enter a movie ID you like (optional, press 0 to skip): "))
        
        if user_id < 1 or user_id > 500:
            print("❌ User ID must be between 1 and 500!")
            return
        
        if movie_id == 0:
            movie_id = None
        
        recommendations = engine.hybrid_recommendations(user_id, movie_id, 10)
        
        if recommendations.empty:
            print("❌ No recommendations found!")
            return
        
        print(f"\n🎬 Hybrid recommendations for User {user_id}:")
        print("-" * 50)
        for idx, row in recommendations.iterrows():
            print(f"• {row['title']} ({row['genre']}) - Rating: {row['rating']}")
            
    except ValueError:
        print("❌ Please enter valid IDs!")

def get_popular_movies(engine):
    """Get popular movies"""
    print("\n🔥 POPULAR MOVIES")
    print("-" * 20)
    
    recommendations = engine.get_popular_movies(10)
    
    print("🎬 Most Popular Movies:")
    print("-" * 40)
    for idx, row in recommendations.iterrows():
        print(f"• {row['title']} ({row['genre']}) - Rating: {row['rating']}")

def get_genre_recommendations(engine):
    """Get genre-based recommendations"""
    print("\n🎭 GENRE-BASED RECOMMENDATIONS")
    print("-" * 35)
    
    # Show available genres
    genres = engine.movies_df['genre'].unique()
    print("Available genres:")
    for i, genre in enumerate(genres, 1):
        print(f"{i}. {genre}")
    
    try:
        genre_idx = int(input("\nEnter genre number: ")) - 1
        
        if genre_idx < 0 or genre_idx >= len(genres):
            print("❌ Invalid genre selection!")
            return
        
        selected_genre = genres[genre_idx]
        recommendations = engine.get_genre_recommendations(selected_genre, 10)
        
        print(f"\n🎬 Top {selected_genre} Movies:")
        print("-" * 40)
        for idx, row in recommendations.iterrows():
            print(f"• {row['title']} - Rating: {row['rating']}")
            
    except ValueError:
        print("❌ Please enter a valid genre number!")

def view_user_profile(engine):
    """View user profile and preferences"""
    print("\n👤 USER PROFILE")
    print("-" * 15)
    
    try:
        user_id = int(input("Enter user ID (1-500): "))
        
        if user_id < 1 or user_id > 500:
            print("❌ User ID must be between 1 and 500!")
            return
        
        profile = engine.get_user_profile(user_id)
        
        if profile is None:
            print("❌ User not found!")
            return
        
        print(f"\n📊 Profile for User {user_id}:")
        print("-" * 30)
        print(f"Total Ratings: {profile['total_ratings']}")
        print(f"Average Rating: {profile['average_rating']:.2f}")
        
        print(f"\n🎭 Favorite Genres:")
        for genre, rating in profile['favorite_genres'].items():
            print(f"  {genre}: {rating:.2f}")
        
        print(f"\n⭐ Rating Distribution:")
        for rating, count in profile['rating_distribution'].items():
            print(f"  {rating} stars: {count} ratings")
        
        print(f"\n📝 Recent Ratings:")
        for idx, row in profile['recent_ratings'].iterrows():
            print(f"  {row['title']} ({row['genre']}) - {row['rating']} stars")
            
    except ValueError:
        print("❌ Please enter a valid user ID!")

def main():
    """Main application loop"""
    movies_df = None
    ratings_df = None
    engine = None
    
    while True:
        display_menu()
        
        try:
            choice = int(input("\nEnter your choice (1-10): "))
            
            if choice == 1:
                movies_df, ratings_df = generate_data()
                
            elif choice == 2:
                movies_df, ratings_df = load_data()
                if movies_df is not None and ratings_df is not None:
                    print("Initializing recommendation engine...")
                    engine = MovieRecommendationEngine(movies_df, ratings_df)
                    print("✅ Recommendation engine initialized!")
                
            elif choice == 3:
                if engine is None:
                    print("❌ Please initialize the recommendation engine first!")
                else:
                    get_content_based_recommendations(engine)
                    
            elif choice == 4:
                if engine is None:
                    print("❌ Please initialize the recommendation engine first!")
                else:
                    get_collaborative_recommendations(engine)
                    
            elif choice == 5:
                if engine is None:
                    print("❌ Please initialize the recommendation engine first!")
                else:
                    get_hybrid_recommendations(engine)
                    
            elif choice == 6:
                if engine is None:
                    print("❌ Please initialize the recommendation engine first!")
                else:
                    get_popular_movies(engine)
                    
            elif choice == 7:
                if engine is None:
                    print("❌ Please initialize the recommendation engine first!")
                else:
                    get_genre_recommendations(engine)
                    
            elif choice == 8:
                if engine is None:
                    print("❌ Please initialize the recommendation engine first!")
                else:
                    view_user_profile(engine)
                    
            elif choice == 9:
                show_data_statistics(movies_df, ratings_df)
                
            elif choice == 10:
                print("\n👋 Thank you for using the Movie Recommendation System!")
                break
                
            else:
                print("❌ Invalid choice! Please enter a number between 1 and 10.")
                
        except ValueError:
            print("❌ Please enter a valid number!")
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    main() 