from prettytable import PrettyTable  # Prints pretty command line tables


def queryTwo(c):

    # For the five highest budgeted movies of 2018 & 2019,
    # by how much did each movie's budget eclipse it's competitor?

    select_statement = \
        """
    /* EXTRACT YEAR FROM RELEASE DATE  */
    WITH formatted as (
    SELECT
    title,
    strftime('%Y',release_date) as released,
    CAST(budget as int) as budget
    FROM movies
    ),

    /* SUBRACT EACH MOVIE'S BUDGET FROM THAT OF THE ONE BELOW IT & 
    RANK BY BUDGET */
    compared as (
    SELECT 
    title,
    released,
     budget,
    (-lead(budget) OVER (PARTITION BY released ORDER BY budget DESC) + budget),
    DENSE_RANK() over (PARTITION BY released ORDER BY budget DESC) as rank
    FROM formatted
    )

    SELECT * FROM compared 
    WHERE released in ('2019','2018') AND rank < 6
    ORDER BY released DESC, budget DESC
    
    """

    c.execute(select_statement)
    d = c.fetchall()

    # If query is modified, make sure to adjust prettytable accordingly
    x = PrettyTable()
    x.field_names = ['Title', 'Released',
                     'Budget', 'Cost over nearest competitor', ' Budget Rank']
    x.align['Title'] = 'l'

    for i, (title,  released, budget, comp, rank) in enumerate(d):
        x.add_row([title,  released, budget, comp, rank])

        try:
            if d[i+1][1] != d[i][1]:
                x.add_row(['', '', '', '', ''])
        except:
            pass

    print(d[0])
    print(d[1])
    print(d[2])
    print(x)
