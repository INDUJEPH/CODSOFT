
movies = {
    "Avengers": "action",
    "Batman": "action",
    "Inception": "sci-fi",
    "Interstellar": "sci-fi",
    "Titanic": "romance",
    "Notebook": "romance",
    "Joker": "drama",
    "Forrest Gump": "drama"
}

print("Movie Recommendation System")
print("Available choices: action, sci-fi, romance, drama")

user_choice = input("Enter your favourite type: ")

print("\nRecommended movies:")

found = False

for movie in movies:
    if movies[movie] == user_choice:
        print("-", movie)
        found = True

if found == False:
    print("Sorry, no movies found .")
