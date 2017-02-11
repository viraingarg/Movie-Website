import webbrowser


class Movie:
     """
          This class has two methods and
          stores info about movie like its
          title, storyline, image and youtube url.
     """
     
     def __init__(self, movie_title, movie_storyline, poster_image, trailer_video):
          self.title = movie_title
          self.storyline = movie_storyline
          self.poster_image_url = poster_image
          self.trailer_youtube_url = trailer_video

     def show_trailer(self):
          webbrowser.open(self.trailer_youtube_url)
