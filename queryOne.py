from prettytable import PrettyTable  # Prints pretty command line tables


def queryOne(c):

    # What are the five highest grossing Action, Animation & Comedy movies?

    select_statement = \
        """
    /* Mapping movie_genres, movies to genres  */
    WITH mov AS (
    SELECT
    name as genre,  
    m.title as title,
    m.revenue as revenue
    FROM genres g
    JOIN movie_genres mg on mg.genre_id = g.id
    JOIN movies m on m.id = mg.movie_id
    ),

    /* RANK MOVIES WITHIN THE SAME GENRE ACCORDING TO REVENUE */
    ranked as (
    SELECT
    title,
    genre,
    revenue,
    RANK() OVER (PARTITION BY genre ORDER BY cast(revenue as int) DESC) as rank
    FROM mov
    ORDER BY genre, rank
    )

    /* SELECT TOP FIVE HIGHEST GROSSING FOR ACTION, ANIMATION AND COMEDY GENRES */
    SELECT
    title,
    genre,
    revenue,
    rank
    FROM ranked
    WHERE (rank < 6) and genre in ('Action', 'Animation', 'Comedy')
    LIMIT 15
    """

    # Executes SQL command and gets all results
    c.execute(select_statement)
    d = c.fetchall()

    # Prints neat table in command line - not relevant to SQL
    # If query is modified, make sure to adjust prettytable accordingly
    x = PrettyTable()
    x.field_names = ['Title', 'Genre', 'Revenue', 'Rank']
    x.align['Title'] = 'l'

    for i, (title, genre, rev, rank) in enumerate(d):
        x.add_row([title, genre, rev, rank])
        try:
            if d[i+1][1] != d[i][1]:
                x.add_row(['', '', '', ''])
        except:
            pass
    print(d[0])
    print(d[1])
    print(d[2])
    print(x)
