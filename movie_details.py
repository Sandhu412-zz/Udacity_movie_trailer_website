import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A Story of a boy and its toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
print(avatar.storyline)

up = media.Movie("Up",
                 "Story of an old man and a boy ranger",
                 "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
                 "https://www.youtube.com/watch?v=pkqzFUhGPJg")
print(up.storyline)

moana = media.Movie("Moana",
                    "Story of a girl crossing the cursed sea",
                    "https://vignette4.wikia.nocookie.net/disney/images/b/be/Moana_poster_1.jpg/revision/latest?cb=20160913172858",
                    "https://www.youtube.com/watch?v=LKFuXETZUsI")

ratatouille = media.Movie("Ratatouille",
                          "Story of a mouse chef",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=e8GBfNo3IHY")

hunger_games = media.Movie("Hunger Games",
                           "Games of skill and survival, lead by a brave girl",
                           "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                           "https://www.youtube.com/watch?v=FovFG3N_RSU")

movies = [toy_story, avatar, up, ratatouille, hunger_games, moana]
fresh_tomatoes.open_movies_page(movies)
