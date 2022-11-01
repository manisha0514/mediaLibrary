# -*- coding: utf-8 -*-

"""This module provides a database connection."""

from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


def createMovieTable():
    """Create the movie table in the database."""
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
                CREATE TABLE IF NOT EXISTS movie (
                    movie_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    movie_name VARCHAR(40) NOT NULL,
                    actor_name VARCHAR(40) NOT NULL,
                    movie_year VARCHAR(40) NOT NULL,
                    director_name VARCHAR(40) NOT NULL,
                    genre VARCHAR(40) NOT NULL,
                    moviedata LONGBLOB NOT NULL,
                    user_id  VARCHAR(40) NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES usertable(userId)

                );
                """
    )


def createUserTable():
    """Create the user table in the database."""
    createTableQuery1 = QSqlQuery()
    return createTableQuery1.exec(
        """
        CREATE TABLE IF NOT EXISTS usertable (
            userId VARCHAR(40) PRIMARY KEY  NOT NULL,
            email VARCHAR(40) NOT NULL,
            password VARCHAR(40) NOT NULL
        );
        """
    )


def createMusicTable():
    """Create the music table in the database."""
    createTableQuery2 = QSqlQuery()
    return createTableQuery2.exec(
        """
       CREATE TABLE IF NOT EXISTS music (
            music_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,  
            music_name VARCHAR(40) NOT NULL,
            singer_name VARCHAR(40) NOT NULL,
            song_year VARCHAR(40) NOT NULL,
            artist_name VARCHAR(40) NOT NULL,
            genre VARCHAR(40) NOT NULL,
            musicdata LONGBLOB NOT NULL,
            user_id  VARCHAR(40) NOT NULL,
            FOREIGN KEY (user_id) REFERENCES usertable(userId)
            
        );
        """
    )

def createGameTable():
    """Create the game table in the database."""
    createTableQuery3 = QSqlQuery()
    return createTableQuery3.exec(
        """
              CREATE TABLE IF NOT EXISTS game (
                   game_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                   game_name VARCHAR(40) NOT NULL,
                   game_year VARCHAR(40) NOT NULL,
                   game_publisher VARCHAR(40) NOT NULL,
                   game_platform VARCHAR(40) NOT NULL,
                   genre VARCHAR(40) NOT NULL,
                   gamedata LONGBLOB NOT NULL,
                   user_id  VARCHAR(40) NOT NULL,
                   FOREIGN KEY (user_id) REFERENCES usertable(userId)


               );
               """
    )


def createConnection(databaseName):
    """Create and open a database connection."""
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "Media Library",
            f"Database Error: {connection.lastError().text()}",
        )
        return False

    createMovieTable()
    createUserTable()
    createGameTable()
    createMusicTable()
    connection.close()
    return True
