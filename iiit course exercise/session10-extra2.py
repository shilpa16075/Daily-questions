list1 = ["Inception", "Interstellar", "Dune", "Avatar", "Joker"]
list2 = ["Dune", "Batman", "Joker", "Inception", "Thor"]

common_movies = []

for movie in list1:
    if movie in list2:
        common_movies.append(movie)

print(common_movies)