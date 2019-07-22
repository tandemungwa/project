import requests as req
import time


# Querying data from TMDB API - https://www.themoviedb.org/?language=en-US

# Base URL to be formatted for different types of calls
base_url = 'https://api.themoviedb.org/3'

# API key obtained via TMDb API account
api_key = '0ae3932382a8269880f66f9422a86376'


def getMovieDetails(movie_id):
    # Format API URL
    URL = '{base}/movie/{id}?api_key={api_key}'.format(base=base_url,
                                                       id=movie_id,
                                                       api_key=api_key)

    # Retrieve API reponse and convert to JSON
    data = req.get(URL).json()

    # Columns we want to work with
    desired_cols = ['id', 'title', 'release_date',
                    'budget', 'revenue', 'genres', 'vote_average']

    # Final data
    data = {column: data[column] for column in desired_cols}

    # Retains genre_ids only, SQL will take care of key/name map
    data['genres'] = [genre['id'] for genre in data['genres']]

    # Avoid API limit
    time.sleep(.25)

    return(data)


def getGenres():
    # Pull key reference for genre names
    genre_map = req.get(
        '{base_url}/genre/movie/list?api_key={api_key}'.format(base_url=base_url, api_key=api_key)).json()['genres']

    # Format key reference to ease creating SQL table
    genre_map = {gen['id']: gen['name'] for gen in genre_map}

    return(genre_map)


def getPopularMovies():
    total_pages = 3
    popular_movie_ids = []

    # Format URL
    URL = "{base}/movie/popular?api_key={api_key}&language=en-US".format(base=base_url,
                                                                         api_key=api_key)

    # Loop until you get 3 pages (~60 movies) of most popular movies (according to TMDB metric)
    for page_number in range(1, total_pages+1):
        d = req.get(URL+"&page="+str(page_number)).json()
        popular_movie_ids.extend([movie['id']
                                  for movie in d['results']])  # Only getting ids

    # Get detailed film data with ids
    popular_movies = [getMovieDetails(id_) for id_ in popular_movie_ids]

    return(popular_movies)
