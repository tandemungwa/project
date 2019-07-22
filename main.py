from pullAPIData import getGenres, getPopularMovies
import pandas as pd
import sqlite3
import os
from initializeTables import initTables
from populateTables import populateTables
from queryOne import queryOne
from queryTwo import queryTwo
from queryThree import queryThree
import time


# If the CSV files don't exist, pull from API and save to local CSV
if not os.path.exists('data.csv'):
    # getPopularMovies() pulls data from TMDB API
    print('- Grabbing data from API...')
    pd.DataFrame(getPopularMovies()).to_csv('data.csv', index=False, encoding = 'utf-8')
    print("Data obtained.")

    # Scattered throughout script to leave time to read print statements from terminal
    # Not necessary to operation and can be ignored
    time.sleep(2.5)


# Pull data from CSV for storage into SQL
data = pd.read_csv('data.csv', header=0, encoding = 'utf-8').to_dict('records')

# Pull genre key/name map from API
genre_keys = getGenres()


# Creates local data.db then starts connection - if it already exists, just start connection
print('- Starting SQLite database...')
conn = sqlite3.connect('database.db')


c = conn.cursor()  # SQL commands are executed via cursor
print("Server started.")
time.sleep(2.5)


# Create table schema then populate tables with API data
try:
    print('- Initializing tables...')
    initTables(c, conn)  # Create table schema

    # Populate created tables with API data
    populateTables(c, conn, data, genre_keys)

    print("Tables populated.")
    time.sleep(2.5)

except:
    # If tables already exists, initTables throws error, so try/except can bypass the error
    print('Tables already exist.')
    time.sleep(2.5)


# Run queries
print('- Running queries....')
time.sleep(2.5)

print(' \n ')
queryOne(c)
print(' \n ')
queryTwo(c)
print(' \n ')
queryThree(c)
