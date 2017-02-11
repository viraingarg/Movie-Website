import media
import fresh_tomatoes


# array containing titles of movies.
name = ["Inception", "Transformers", "John Wick 2", "Logan",
        "Justice League", "A Walk To Remember"]

# array containing story about movies.
story = ["A fantasy story about dreams", "A Movie about Robots"
         " from alien planet", "After returning to the criminal underworld to"
         " repay a debt, John Wick discovers that a large bounty has been put"
         " on his life.", "In the near future, a weary Logan cares for an"
         " ailing Professor X in a hide out on the Mexican border."
         " But Logan's attempts to hide from the world and his legacy"
         " are up-ended when a young mutant arrives, being pursued by "
         "dark forces.", "Fueled by his restored faith in humanity and"
         " inspired by Superman's selfless act, Bruce Wayne enlists the help"
         " of his newfound ally, Diana Prince, to face an even greater enemy.",
         "The story of two North Carolina teens, London "
         "Carter and Jamie Sullivan, who are thrown together "
         "after London gets into trouble and is made to do community service."]

# array containing url to movies poster.
poster = ["http://cdn.collider.com/wp-content/uploads/Inception-movie-"
          "poster-7.jpg", "http://www.firstshowing.net/img/optimus-"
          "poster-big.jpg", "https://images-na.ssl-images-amazon.com"
          "/images/M/MV5BMjE2NDkxNTY2M15BMl5BanBnXkFtZTgwMDc2NzE0MTI@"
          "._V1_UX182_CR0,0,182,268_AL__QL50.jpg", "https://images-na"
          ".ssl-images-amazon.com/images/M/MV5BMjI1MjkzMjczMV5BMl5Ban"
          "BnXkFtZTgwNDk4NjYyMTI@._V1_UX182_CR0,0,182,268_AL__QL50.jpg",
          "https://static1.squarespace.com/static/51b3dc8ee4b051b96c"
          "eb10de/t/520670e3e4b0bdc260062d14/1376153828097/DefendersOf"
          "Earth.jpg", "https://images-na.ssl-images-amazon.com/images/M/"
          "MV5BMzU3NTYxM2MtNjViMS00YmNlLWEwM2MtYWI2MzgzNTkxODFjXkEyXkFq"
          "cGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL__QL50.jpg"]

# array containing url to movies trailer.
trailer = ["https://youtu.be/YoHD9XEInc0", "https://www.youtube.com"
           "/watch?v=HKi0xnV4ZjM", "https://www.youtube.com/watch?v="
           "XGk2EfbD_Ps", "https://www.youtube.com/watch?v=gbug3zT"
           "m3Ws", "https://www.youtube.com/watch?v=fIHH5-HVS9o",
           "https://www.youtube.com/watch?v=R3b19svqbls"]

# variable which will contain objects of the movies
movie_ob = []

for i in range(0, 6):
    movie_ob.append(media.Movie(name[i], story[i], poster[i], trailer[i]))

fresh_tomatoes.open_movies_page(movie_ob)
