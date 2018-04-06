import media
import fresh_tomatoes

'''
Initialize a number of 'Movie' objects, which are then passed to the Fresh_Tomatoes module

The expected paramters to initialize a movie object is as follows
media.Movie(movie_title, movie_plot, movie_poster_link, movie_trailer_link)

movie_trailer_link param should be a YouTube url.

'''

# initialize movie objects
it_movie = media.Movie('IT',
                       'In the summer of 1989, a group of bullied kids band together to destroy a shapeshifting monster,'
                       ' which disguises itself as a clown and preys on the children of Derry, their small Maine town.',
                       'https://images-na.ssl-images-amazon.com/images/M/MV5BZDVkZmI0YzAtNzdjYi00ZjhhLWE1ODEtMWMzMWMzNDA0NmQ4XkEyXkFqcGdeQXVyNzYzODM3Mzg@._V1_SX300.jpg',
                       'https://youtu.be/FnCdOQsX5kc')

the_ritual = media.Movie('Ritual',
                         'Reuniting after the tragic death of their friend, four college pals set out to hike through the Scandinavian wilderness',
                         'https://ia.media-imdb.com/images/M/MV5BMjAzMzAyMDI4Ml5BMl5BanBnXkFtZTgwODMwOTY2NDM@._V1_SY1000_CR0,0,673,1000_AL_.jpg',
                         'https://youtu.be/3G3N0-6-YpA')

annihilation = media.Movie('Annihilation',
                           'A biologist signs up for a dangerous, secret expedition into a mysterious zone where the laws of nature don\'t apply.',
                           'https://ia.media-imdb.com/images/M/MV5BMTk2Mjc2NzYxNl5BMl5BanBnXkFtZTgwMTA2OTA1NDM@._V1_SY1000_CR0,0,640,1000_AL_.jpg',
                           'https://youtu.be/89OP78l9oF0')

the_matrix = media.Movie('The Matrix',
                         'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.',
                         'https://ia.media-imdb.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg',
                         'https://youtu.be/vKQi3bBA1y8')

interstellar = media.Movie('Interstellar',
                           'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.',
                           'https://ia.media-imdb.com/images/M/MV5BZjdkOTU3MDktN2IxOS00OGEyLWFmMjktY2FiMmZkNWIyODZiXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_SY1000_SX675_AL_.jpg',
                           'https://youtu.be/0vxOhd4qlnA')

ex_machina = media.Movie('Ex Machina',
                         'A young programmer is selected to participate in a ground-breaking experiment in synthetic intelligence by evaluating the human qualities of a breath-taking humanoid A.I.',
                         'https://ia.media-imdb.com/images/M/MV5BMTUxNzc0OTIxMV5BMl5BanBnXkFtZTgwNDI3NzU2NDE@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
                         'https://youtu.be/XYGzRB4Pnq8')


#add movies to list to make the call to open_movies_page(fresh_tomatoes module) cleaner
movies = [the_ritual, annihilation, it_movie, the_matrix, interstellar, ex_machina]

# Fresh tomatoes module generates an HTML page to display the movies array info, and their trailers
fresh_tomatoes.open_movies_page(movies)
