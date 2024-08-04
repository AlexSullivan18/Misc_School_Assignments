import sqlite3

from typing import Tuple, List


def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)  # connect to existing DB or create new one
    cursor = db_connection.cursor()  # get ready to read/write data
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()  # make sure any changes get saved
    connection.close()


def initialize_movie_ratings_database(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS top_250_shows(
            id TEXT PRIMARY KEY,
            title TEXT,
            full_title TEXT,
            year INTEGER,
            rank_up_down
            );''')


def initialize_database_top250(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS top_250_shows(
        id TEXT PRIMARY KEY,
        rank INTEGER DEFAULT 0,
        title TEXT,
        full_title TEXT,
        year INTEGER,
        image_url TEXT,
        crew TEXT,
        imdb_rating REAL,
        imdb_rating_count INTEGER);''')


def put_in_wheel_of_time(cursor: sqlite3.Cursor):
    """this is just a total kludge. I need a Wheel of time Entry for the foreign key to work, so I'm just adding it"""
    cursor.execute("""INSERT INTO top_250_shows(id, rank, title, full_title, year, image_url, crew, imdb_rating, imdb_rating_count)
    VALUES('tt7462410',0,'The Wheel of Time','The Wheel of Time (TV Series 2021– )',2021,'','Rosamund Pike, Daniel Henney',
    7.2,85286)""")


def initialize_database_ratings(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS top_250_show_ratings(
      ratings_key INTEGER PRIMARY KEY,
      imdb_ttcode TEXT NOT NULL,
      title TEXT,
      full_title TEXT,
      year INTEGER,
      total_rating INT DEFAULT 0,
      total_votes INTEGER,
      rating10_percent REAL,
      rating10_votes INTEGER,
      rating9_percent REAL,
      rating9_votes INTEGER,
      rating8_percent REAL,
      rating8_votes INTEGER,
      rating7_percent REAL,
      rating7_votes INTEGER,
      rating6_percent REAL,
      rating6_votes INTEGER,
      rating5_percent REAL,
      rating5_votes INTEGER,
      rating4_percent REAL,
      rating4_votes INTEGER,
      rating3_percent REAL,
      rating3_votes INTEGER,
      rating2_percent REAL,
      rating2_votes INTEGER,
      rating1_percent REAL,
      rating1_votes INTEGER,
      FOREIGN KEY (imdb_ttcode) REFERENCES top_250_shows (id)
      ON DELETE CASCADE ON UPDATE NO ACTION
      );''')


def initialize_database_pop_shows(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS popular_shows_data(
      id TEXT PRIMARY KEY,
      rank INTEGER,
      rank_movement INTEGER DEFAULT 0,
      title TEXT,
      full_title TEXT,
      year INTEGER,
      image_url TEXT,
      crew TEXT,
      imdb_rating REAL,
      imdb_rating_count INTEGER);''')


def initialize_top_250_movies(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS top_250_movies(
           id TEXT PRIMARY KEY,
           rank INTEGER DEFAULT 0,
           title TEXT,
           full_title TEXT,
           year INTEGER,
           image_url TEXT,
           crew TEXT,
           imdb_rating REAL,
           imdb_rating_count INTEGER);''')


def initialize_database_pop_movies(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS popular_movies_data(
           id TEXT PRIMARY KEY,
           rank INTEGER,
           rank_movement INTEGER DEFAULT 0,
           title TEXT,
           full_title TEXT,
           year INTEGER,
           image_url TEXT,
           crew TEXT,
           imdb_rating REAL,
           imdb_rating_count INTEGER);''')


def create_all_tables(db_cursor: sqlite3.Cursor):
    initialize_database_top250(db_cursor)
    initialize_database_pop_shows(db_cursor)
    initialize_database_ratings(db_cursor)
    initialize_top_250_movies(db_cursor)
    initialize_database_pop_movies(db_cursor)


def put_ratings_into_db(data_to_add: List[tuple], db_cursor: sqlite3.Cursor):
    db_cursor.executemany("""INSERT INTO top_250_show_ratings(imdb_ttcode, title, full_title, year, total_rating, total_votes,
    rating10_percent,
    rating10_votes, rating9_percent, rating9_votes, rating8_percent, rating8_votes, rating7_percent, rating7_votes,
    rating6_percent, rating6_votes, rating5_percent, rating5_votes, rating4_percent, rating4_votes, rating3_percent,
    rating3_votes, rating2_percent, rating2_votes, rating1_percent, rating1_votes)
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", data_to_add)


def put_most_popular_in_database(table: str, data_to_add: List[tuple], db_cursor: sqlite3.Cursor):
    db_cursor.executemany(f"""INSERT INTO {table}(id, rank, rank_movement, title, full_title, year, image_url, crew, 
    imdb_rating, imdb_rating_count) VALUES(?,?,?,?,?,?,?,?,?, ?)""", data_to_add)


def put_top_250_in_database(table: str, data_to_add: List[tuple], db_cursor: sqlite3.Cursor):
    db_cursor.executemany(f"""INSERT INTO {table}(id, rank, title, full_title, year, image_url, crew, imdb_rating,
    imdb_rating_count)
    VALUES(?,?,?,?,?,?,?,?,?)""", data_to_add)
