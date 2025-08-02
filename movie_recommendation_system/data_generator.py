import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_movie_data(num_movies=1000, num_users=500):
    """
    Generate sample movie data for the recommendation system
    """
    # Movie genres
    genres = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 
              'Drama', 'Family', 'Fantasy', 'Horror', 'Mystery', 'Romance', 'Sci-Fi', 
              'Thriller', 'War', 'Western']
    
    # Generate movies
    movies = []
    for i in range(num_movies):
        movie = {
            'movie_id': i + 1,
            'title': f'Movie {i + 1}',
            'genre': random.choice(genres),
            'year': random.randint(1990, 2024),
            'rating': round(random.uniform(1.0, 10.0), 1),
            'director': f'Director {random.randint(1, 50)}',
            'cast': f'Actor {random.randint(1, 100)}, Actor {random.randint(101, 200)}',
            'description': f'This is a sample description for Movie {i + 1}. It is a {random.choice(genres).lower()} film.'
        }
        movies.append(movie)
    
    # Generate user ratings
    ratings = []
    for user_id in range(1, num_users + 1):
        # Each user rates 10-50 random movies
        num_ratings = random.randint(10, 50)
        rated_movies = random.sample(range(1, num_movies + 1), num_ratings)
        
        for movie_id in rated_movies:
            rating = {
                'user_id': user_id,
                'movie_id': movie_id,
                'rating': random.randint(1, 5),
                'timestamp': datetime.now() - timedelta(days=random.randint(1, 365))
            }
            ratings.append(rating)
    
    return pd.DataFrame(movies), pd.DataFrame(ratings)

def save_sample_data():
    """
    Generate and save sample data to CSV files
    """
    print("Generating sample movie data...")
    movies_df, ratings_df = generate_movie_data()
    
    # Save to CSV files
    movies_df.to_csv('movies.csv', index=False)
    ratings_df.to_csv('ratings.csv', index=False)
    
    print(f"Generated {len(movies_df)} movies and {len(ratings_df)} ratings")
    print("Data saved to movies.csv and ratings.csv")
    
    return movies_df, ratings_df

if __name__ == "__main__":
    save_sample_data() 