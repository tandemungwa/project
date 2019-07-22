from prettytable import PrettyTable  # Prints pretty command line tables


def queryThree(c):

    # For the years of 2018 & 2019, what were the average ratings of Action, Animation,
    # & Drama movies?

    select_statement = \
        """
    WITH mov AS (
        SELECT 
        name as genre,
        m.vote_average as rating, 
        m.title as title,
        m.release_date as released
        FROM genres g 
        JOIN movie_genres as mg on mg.genre_id = g.id
        JOIN movies m on m.id = mg.movie_id  
        ),
    
    formatted AS (
        SELECT 
        title, 
        genre,
        strftime('%Y',released) as released,
        CAST(rating as int) as rating
        FROM mov
    )
    
    SELECT 
        genre,
        released,
        round(avg(rating),2) as avg_rating 
    FROM formatted

    WHERE  genre in ("Action", "Animation","Drama") AND released in ("2018","2019")
    GROUP BY genre, released
    ORDER BY released DESC, avg_rating DESC
    """

    c.execute(select_statement)
    d = c.fetchall()

    x = PrettyTable()
    x.field_names = ['Genre', 'Released', 'Rating']
    x.align['Genre'] = 'l'

    for i, (genre,  released, rating) in enumerate(d):
        x.add_row([genre, released, rating])
        try:
            if d[i+1][1] != d[i][1]:
                x.add_row(['', '', ''])
        except:
            pass

    print(d[0])
    print(d[1])
    print(d[2])
    print(x)
