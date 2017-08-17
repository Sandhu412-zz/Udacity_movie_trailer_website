import webbrowser


class Movie():
    # The class Movie() creats a constructor and has the show_trailer method to
    # play the movie trailer.
    def __init__(self, movie_title,
                 movie_storyline, poster_image, trailer_youtube):
        # The __init__ constructor takes 4 parameters and assigns the values to
        # its self variables.
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        # show_trailer function takes the youtube url of the movie trailer as a
        # parameter and plays the trailer using webbrowser.open lib.
        webbrowser.open(self.trailer_youtube_url)
