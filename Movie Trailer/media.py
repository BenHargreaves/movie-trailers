class Movie():
    '''
    Movie Class, used to store useful information about a particular movie.

    Parameters;
    title - string: The Title of the movie
    storyline - string: A brief synopsis of the movies plot
    poster_image_url - string: A URL link to the movies poster
    trailer_youtube_url - string: A URL link to the movies youtube trailer
    '''
    def __init__(self, title, storyline,
                 poster_image_url, trailer_youtube_url):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
