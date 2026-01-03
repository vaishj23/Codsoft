import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("movies.csv")

# Convert genre text to vectors
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(df["genre"])

# Calculate similarity
similarity = cosine_similarity(genre_matrix)

# Recommendation function
def recommend(movie_title):
    if movie_title not in df["title"].values:
        print("Movie not found.")
        return

    idx = df[df["title"] == movie_title].index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print(f"\nRecommended movies for '{movie_title}':")
    for i in scores[1:6]:
        print("-", df.iloc[i[0]]["title"])

# User input
movie = input("Enter a movie name: ")
recommend(movie)
