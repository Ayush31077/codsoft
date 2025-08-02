import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.decomposition import NMF
from scipy.sparse import csr_matrix
import warnings
warnings.filterwarnings('ignore')

class MovieRecommendationEngine:
    def __init__(self, movies_df, ratings_df):
        """
        Initialize the recommendation engine with movie and rating data
        """
        self.movies_df = movies_df
        self.ratings_df = ratings_df
        self.user_movie_matrix = None
        self.tfidf_matrix = None
        self.cosine_sim = None
        self.nmf_model = None
        self._prepare_data()
    
    def _prepare_data(self):
        """
        Prepare data for different recommendation algorithms
        """
        # Create user-movie rating matrix
        self.user_movie_matrix = self.ratings_df.pivot(
            index='user_id', 
            columns='movie_id', 
            values='rating'
        ).fillna(0)
        
        # Prepare content-based features
        self.movies_df['features'] = (
            self.movies_df['genre'] + ' ' + 
            self.movies_df['director'] + ' ' + 
            self.movies_df['cast'] + ' ' + 
            self.movies_df['description']
        )
        
        # Create TF-IDF matrix for content-based filtering
        tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
        self.tfidf_matrix = tfidf.fit_transform(self.movies_df['features'])
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)
        
        # Train NMF model for collaborative filtering
        self._train_nmf()
    
    def _train_nmf(self, n_components=50):
        """
        Train Non-negative Matrix Factorization model
        """
        self.nmf_model = NMF(n_components=n_components, random_state=42)
        self.nmf_model.fit(self.user_movie_matrix)
    
    def content_based_recommendations(self, movie_id, n_recommendations=10):
        """
        Get content-based recommendations based on movie similarity
        """
        # Find movie index
        movie_idx = self.movies_df[self.movies_df['movie_id'] == movie_id].index[0]
        
        # Get similarity scores
        sim_scores = list(enumerate(self.cosine_sim[movie_idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # Get top similar movies (excluding the movie itself)
        sim_scores = sim_scores[1:n_recommendations+1]
        movie_indices = [i[0] for i in sim_scores]
        
        return self.movies_df.iloc[movie_indices][['movie_id', 'title', 'genre', 'rating']]
    
    def collaborative_filtering_recommendations(self, user_id, n_recommendations=10):
        """
        Get collaborative filtering recommendations using NMF
        """
        if user_id not in self.user_movie_matrix.index:
            return pd.DataFrame()
        
        # Get user's rating vector
        user_ratings = self.user_movie_matrix.loc[user_id].values.reshape(1, -1)
        
        # Transform user ratings using NMF
        user_factors = self.nmf_model.transform(user_ratings)
        
        # Reconstruct ratings
        predicted_ratings = np.dot(user_factors, self.nmf_model.components_)
        
        # Get movies user hasn't rated
        user_rated = self.user_movie_matrix.loc[user_id] > 0
        unrated_movies = ~user_rated
        
        # Get top recommendations
        unrated_ratings = predicted_ratings[0][unrated_movies]
        top_indices = np.argsort(unrated_ratings)[::-1][:n_recommendations]
        
        # Get movie IDs for unrated movies
        unrated_movie_ids = self.user_movie_matrix.columns[unrated_movies]
        recommended_movie_ids = unrated_movie_ids[top_indices]
        
        return self.movies_df[self.movies_df['movie_id'].isin(recommended_movie_ids)][
            ['movie_id', 'title', 'genre', 'rating']
        ]
    
    def hybrid_recommendations(self, user_id, movie_id=None, n_recommendations=10):
        """
        Get hybrid recommendations combining content-based and collaborative filtering
        """
        # Get collaborative filtering recommendations
        cf_recommendations = self.collaborative_filtering_recommendations(user_id, n_recommendations)
        
        if movie_id and not cf_recommendations.empty:
            # Get content-based recommendations
            cb_recommendations = self.content_based_recommendations(movie_id, n_recommendations)
            
            # Combine recommendations (simple average of scores)
            combined = pd.concat([cf_recommendations, cb_recommendations])
            combined = combined.drop_duplicates(subset=['movie_id'])
            
            # Sort by rating (you could implement more sophisticated ranking)
            combined = combined.sort_values('rating', ascending=False)
            
            return combined.head(n_recommendations)
        
        return cf_recommendations
    
    def get_popular_movies(self, n_recommendations=10):
        """
        Get most popular movies based on average rating and number of ratings
        """
        # Calculate average rating and count for each movie
        movie_stats = self.ratings_df.groupby('movie_id').agg({
            'rating': ['mean', 'count']
        }).reset_index()
        movie_stats.columns = ['movie_id', 'avg_rating', 'rating_count']
        
        # Filter movies with minimum number of ratings
        min_ratings = movie_stats['rating_count'].quantile(0.6)
        qualified_movies = movie_stats[movie_stats['rating_count'] >= min_ratings]
        
        # Sort by average rating
        qualified_movies = qualified_movies.sort_values('avg_rating', ascending=False)
        
        # Get movie details
        top_movies = qualified_movies.head(n_recommendations)
        return self.movies_df[self.movies_df['movie_id'].isin(top_movies['movie_id'])][
            ['movie_id', 'title', 'genre', 'rating']
        ]
    
    def get_genre_recommendations(self, genre, n_recommendations=10):
        """
        Get movie recommendations based on genre
        """
        genre_movies = self.movies_df[self.movies_df['genre'] == genre]
        return genre_movies.sort_values('rating', ascending=False).head(n_recommendations)[
            ['movie_id', 'title', 'genre', 'rating']
        ]
    
    def get_user_profile(self, user_id):
        """
        Get user's movie preferences and rating history
        """
        if user_id not in self.user_movie_matrix.index:
            return None
        
        user_ratings = self.ratings_df[self.ratings_df['user_id'] == user_id]
        user_movies = user_ratings.merge(self.movies_df, on='movie_id', suffixes=('_user', '_movie'))
        
        # Get favorite genres (use user rating, not movie rating)
        favorite_genres = user_movies.groupby('genre')['rating_user'].mean().sort_values(ascending=False)
        
        # Get rating distribution
        rating_distribution = user_ratings['rating'].value_counts().sort_index()
        
        return {
            'total_ratings': len(user_ratings),
            'average_rating': user_ratings['rating'].mean(),
            'favorite_genres': favorite_genres.head(5).to_dict(),
            'rating_distribution': rating_distribution.to_dict(),
            'recent_ratings': user_movies.sort_values('timestamp', ascending=False).head(10)[
                ['title', 'genre', 'rating_user', 'timestamp']
            ].rename(columns={'rating_user': 'rating'})
        } 