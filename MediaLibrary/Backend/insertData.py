import os
import sqlite3
import logging
db_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def to_binary(filename):
    '''Convert data to binary format'''
    with open(filename, 'rb') as file:
        blob_data = file.read()
    return blob_data

def insertuserIntoTable(userId, email, password):
    try:

        sqliteConnection = sqlite3.connect(
            db_dir + r"\Database\mediaLibrary.sqlite")
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO usertable
                          (userId, email, password) 
                          VALUES (?, ?, ? );"""

        data_tuple = (userId, email, password)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        logging.info("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()
        result = True

    except sqlite3.Error as error:
        logging.warning("Failed to insert Python variable into sqlite table", error)
        result = False
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            logging.info("The SQLite connection is closed")
    return result

def insertMoviesIntoTable(movieName, movieYear, actorName, directorName, genreName, moviedata, userName):
    print(movieName, movieYear, actorName, directorName, genreName, userName)
    try:
        sqliteConnection = sqlite3.connect(
            db_dir + r"\Database\mediaLibrary.sqlite")
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO movie
                          ( user_id, movie_name, actor_name, movie_year, director_name, genre, moviedata) 
                          VALUES (?, ?, ?, ?, ?, ?, ?);"""

        moviedata = to_binary(moviedata)
        data_tuple = (userName, movieName, actorName, movieYear, directorName, genreName,moviedata)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        logging.info("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()
        result = True

    except sqlite3.Error as error:
        logging.warning("Failed to insert Python variable into sqlite table", error)
        result = False
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            logging.info("The SQLite connection is closed")
    return result

def insertMusicIntoTable(songNameField, artistNameField, yearField, writerField, genreField, musicdata, userName):
    print(songNameField, artistNameField, yearField, writerField, genreField, userName)
    try:
        sqliteConnection = sqlite3.connect(
            db_dir + r"\Database\mediaLibrary.sqlite")
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO music
                          ( user_id,music_name,singer_name,song_year,artist_name,genre,musicdata) 
                          VALUES (?, ?, ?, ?, ?, ?, ?);"""

        musicdata = to_binary(musicdata)
        data_tuple = (userName, songNameField, artistNameField, yearField, writerField, genreField, musicdata)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        logging.info("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()
        result = True

    except sqlite3.Error as error:
        logging.warning("Failed to insert Python variable into sqlite table", error)
        result = False
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            logging.info("The SQLite connection is closed")
    return result

def insertGameIntoTable(gameNameField, artistNameField, yearField, writerField, genreField, gamedata, userName):
    print(gameNameField, artistNameField, yearField, writerField, genreField, userName)
    try:
        sqliteConnection = sqlite3.connect(
            db_dir + r"\Database\mediaLibrary.sqlite")
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO game
                          ( game_name,game_year,game_publisher,game_platform, genre,gamedata,user_id) 
                          VALUES (?, ?, ?, ?, ?, ?, ?);"""
        gamedata = to_binary(gamedata)
        data_tuple = ( gameNameField,  yearField,artistNameField, writerField, genreField, gamedata, userName)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        logging.info("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()
        result = True

    except sqlite3.Error as error:
        logging.warning("Failed to insert Python variable into sqlite table", error)
        result = False
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            logging.info("The SQLite connection is closed")
    return result