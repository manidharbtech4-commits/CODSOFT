import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings

warnings.filterwarnings("ignore")

print("starting to load movies...")
movies = pd.read_csv("movie_dataset.csv")

movies["genres"] = movies["genres"].fillna("")
movies["overview"] = movies["overview"].fillna("")
movies["keywords"] = movies["keywords"].fillna("")
movies["cast"] = movies["cast"].fillna("")
movies["director"] = movies["director"].fillna("")

print("mixing all the info together...")
movies["all_text"] = movies["genres"] + " " + movies["overview"] + " " + movies["keywords"] + " " + movies["cast"] + " " + movies["director"]

print("making numbers from words (tfidf)... this takes a sec")
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_result = vectorizer.fit_transform(movies["all_text"])

print("finding how similar movies are...")
similarity = cosine_similarity(tfidf_result, tfidf_result)

def find_movie_index(name):
    name = name.strip().lower()
    found = movies["title"].str.lower() == name
    if found.any():
        return movies[found].index[0]
    return None

def suggest_movies(movie_name, how_many=5):
    idx = find_movie_index(movie_name)
    
    if idx is None:
        print("oops cant find that movie")
        return "try these instead: Avatar, Inception, Titanic, The Avengers, Interstellar"
    
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    scores = scores[1:how_many+1]
    
    rec_list = []
    for pos, sc in scores:
        rec_list.append(movies.iloc[pos]["title"])
    
    return rec_list

print("")
print("=== My Movie Recommender Thing ===")
print("type name of movie you like or quit to stop")
print("good ones to try: Avatar, Inception, Titanic, The Dark Knight Rises")
print("==================================")

while True:
    liked_movie = input("\nMovie you like: ").strip()
    
    if not liked_movie:
        continue
    
    if liked_movie.lower() in ["quit", "exit", "q", "bye"]:
        print("see you...")
        break
    
    print("okay finding similar ones...")
    answer = suggest_movies(liked_movie)
    
    if isinstance(answer, str):
        print(answer)
    else:
        print(f"\nif you like {liked_movie.title()} maybe try these:")
        for num, m in enumerate(answer, 1):
            print(f"  {num}) {m}")