def populateTables(c, conn, data, genre_keys):

     # Load genre key reference (genre_keys)
     # genre_keys format -- {12: "Drama", 142: "Comedy"}
    for genre_id, genre_name in genre_keys.items():
        insert_statement = \
            """
            INSERT INTO genres
            VALUES ("{}","{}")
            """ \
        .format(genre_id, genre_name)

        c.execute(insert_statement)
        conn.commit()

    # Load individual movies into movies TABLE
    for movie in data:
        """ 
        movie FORMAT 

        {"id": 153,
        "title":"The Avengers", 
        "release_date": "2012-08-09", 
        "revenue": 13454231,
        "genres": '[142, 13, 45]',
        "vote_average" : 7.2}
         """
        budget, genres, id_, release_date, revenue, title, vote_average = list(
            movie.values())

        insert_statement = \
            """
            INSERT INTO movies
            VALUES ("{}","{}","{}","{}","{}","{}")
            """ \
        .format(id_, title, budget, revenue, release_date, vote_average)

        c.execute(insert_statement)
        conn.commit()

        # # Each of the movie's genre ids paired with the movie id - stored in movie_genres
        '''
        genres is formatted as a string, due to Pandas
        Remove outer brackets and parse through inner content
        '''

        
        genres = genres.replace('[', '').replace(']', '')
        genres = [int(gen)
                  for gen in genres.split(',') if gen is not '']

        for genre in genres:
            insert_statement = \
                """
                INSERT INTO movie_genres
                VALUES ("{}","{}")
                """\
            .format(id_, genre)

            c.execute(insert_statement)
            conn.commit()
