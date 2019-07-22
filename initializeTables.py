def initTables(c, conn):

    c.execute(""" CREATE TABLE movies (
                id,
                title,
                budget,
                revenue,
                release_date,
                vote_average
            ) """)

    conn.commit()  # Must be run after CREATE to commit changes to SQLite database

    c.execute(""" CREATE TABLE genres (
                id,
                name
            ) """)

    conn.commit()

    # Films can have multiple genres, so we should create a table with a row for each (genre,movie) pairing

    c.execute(""" CREATE TABLE movie_genres (
                movie_id,
                genre_id
            ) """)

    conn.commit()

    """ 
    Suppose a movie (id = 1) has genres  (Drama - 132, Thriller - 45, Action - 84)

    movie_genres represents as:

    movie_id, genre_id
    1, 132
    1, 45
    1, 84

    So when this is joined with the genres table on genres.id = movie_genres.genre_id, 
    and 'name' is extracted from genres, we get:

    name, movie_id
    Drama, 1
    Thriller, 1
    Action, 1 

    Making a row for each (genre, movie) pair.
    Then, this is joined with movies table on movie_id 

    """
