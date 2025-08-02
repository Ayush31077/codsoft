# 🎬 Movie Recommendation System

A comprehensive movie recommendation system built with Python that implements multiple recommendation algorithms including content-based filtering, collaborative filtering, and hybrid approaches.

## 🌟 Features

- **Multiple Recommendation Algorithms**:
  - Content-based filtering using TF-IDF and cosine similarity
  - Collaborative filtering using Non-negative Matrix Factorization (NMF)
  - Hybrid recommendations combining both approaches
  - Genre-based recommendations
  - Popular movies based on ratings

- **Interactive Interfaces**:
  - Command-line interface with full functionality
  - Modern Streamlit web application with beautiful UI
  - Real-time data visualization and analytics

- **Data Management**:
  - Automatic sample data generation
  - CSV data storage and loading
  - User profile analysis and statistics

- **Analytics & Visualization**:
  - Interactive charts and graphs
  - Data statistics and insights
  - User behavior analysis

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Generate sample data**:
   ```bash
   python data_generator.py
   ```

### Running the Application

#### Option 1: Command Line Interface
```bash
python main.py
```

#### Option 2: Streamlit Web App
```bash
streamlit run streamlit_app.py
```

## 📁 Project Structure

```
movie_recommendation_system/
├── requirements.txt          # Python dependencies
├── data_generator.py         # Sample data generation
├── recommendation_engine.py  # Core recommendation algorithms
├── main.py                  # Command-line interface
├── streamlit_app.py         # Web application
├── README.md               # Project documentation
├── movies.csv              # Movie data (generated)
└── ratings.csv             # User ratings data (generated)
```

## 🎯 How It Works

### 1. Content-Based Filtering
- Analyzes movie features (genre, director, cast, description)
- Uses TF-IDF vectorization to create feature vectors
- Calculates cosine similarity between movies
- Recommends movies similar to user's liked movies

### 2. Collaborative Filtering
- Creates user-movie rating matrix
- Uses Non-negative Matrix Factorization (NMF) to find latent factors
- Predicts missing ratings based on user and movie factors
- Recommends movies with high predicted ratings

### 3. Hybrid Recommendations
- Combines content-based and collaborative filtering results
- Provides more diverse and accurate recommendations
- Balances personalization with discovery

## 🎮 Usage Guide

### Command Line Interface

1. **Generate Sample Data** (Option 1)
   - Creates 1000 movies and 500 users with ratings
   - Saves data to `movies.csv` and `ratings.csv`

2. **Load Data and Initialize Engine** (Option 2)
   - Loads existing data files
   - Initializes the recommendation engine

3. **Get Recommendations** (Options 3-7)
   - Content-based: Enter a movie ID you like
   - Collaborative: Enter a user ID (1-500)
   - Hybrid: Combine both approaches
   - Genre-based: Select a genre
   - Popular: Get most popular movies

4. **View User Profile** (Option 8)
   - Analyze user preferences and rating history
   - View favorite genres and rating patterns

5. **Show Data Statistics** (Option 9)
   - View data overview and visualizations
   - Analyze genre distribution and rating patterns

### Streamlit Web App

The web app provides a modern, interactive interface with:

- **Dashboard**: Overview of data and popular movies
- **Recommendations**: All recommendation types with easy-to-use forms
- **User Profiles**: Detailed user analysis
- **Analytics**: Interactive charts and visualizations
- **Search**: Movie search and filtering functionality

## 📊 Sample Data

The system generates realistic sample data including:

- **Movies**: 1000 movies with titles, genres, years, directors, cast, and descriptions
- **Users**: 500 users with varying rating patterns
- **Ratings**: 10-50 ratings per user (1-5 stars)
- **Genres**: 16 different movie genres
- **Years**: Movies from 1990 to 2024

## 🔧 Customization

### Adding Real Data
Replace the sample data with real movie data by:
1. Creating `movies.csv` with columns: `movie_id`, `title`, `genre`, `year`, `rating`, `director`, `cast`, `description`
2. Creating `ratings.csv` with columns: `user_id`, `movie_id`, `rating`, `timestamp`

### Modifying Algorithms
- Adjust NMF components in `recommendation_engine.py`
- Modify TF-IDF parameters for content-based filtering
- Implement additional recommendation algorithms

### Customizing the UI
- Modify Streamlit app styling in `streamlit_app.py`
- Add new visualization types
- Customize the command-line interface in `main.py`

## 🛠️ Technical Details

### Dependencies
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning algorithms (NMF, TF-IDF, cosine similarity)
- **scipy**: Scientific computing
- **matplotlib/seaborn**: Data visualization
- **plotly**: Interactive visualizations
- **streamlit**: Web application framework

### Algorithms Used
- **TF-IDF Vectorization**: For text feature extraction
- **Cosine Similarity**: For content-based similarity calculation
- **Non-negative Matrix Factorization**: For collaborative filtering
- **Hybrid Combination**: Merging multiple recommendation approaches

## 📈 Performance

- **Data Size**: Handles 1000+ movies and 500+ users efficiently
- **Speed**: Fast recommendation generation (< 1 second)
- **Memory**: Optimized for typical desktop systems
- **Scalability**: Can be extended for larger datasets

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding new recommendation algorithms
- Improving the user interface
- Adding more data visualization features
- Optimizing performance
- Adding unit tests

## 📝 License

This project is open source and available under the MIT License.

## 🆘 Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **Data Not Found**: Generate sample data first
   ```bash
   python data_generator.py
   ```

3. **Memory Issues**: Reduce the number of movies/users in `data_generator.py`

4. **Streamlit Issues**: Make sure Streamlit is installed
   ```bash
   pip install streamlit
   ```

### Getting Help

If you encounter any issues:
1. Check the error messages carefully
2. Ensure all dependencies are installed
3. Verify that data files exist
4. Check Python version compatibility

## 🎉 Future Enhancements

- Integration with real movie databases (TMDB, OMDB)
- Advanced recommendation algorithms (deep learning, neural networks)
- User authentication and personalization
- Mobile app development
- Real-time recommendation updates
- A/B testing framework
- Recommendation explanation features

---

**Enjoy discovering new movies! 🎬✨** 