import datetime
import logging
import sqlite3
from typing import Optional

from src.models.constants import DATABASE_FILE_NAME, LOGGING_VERBOSITY

TABLE_NAME = "ReadingList"

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_VERBOSITY)


def createTable() -> None:
    """
    Create the ReadingList table in the database if it does not already exist.

    This function ensures the database table is created with the required schema.
    """
    with sqlite3.connect(DATABASE_FILE_NAME) as connection:
        cursor = connection.cursor()

        logger.info("Database created and connected successfully!")

        cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                path TEXT NOT NULL,
                readDate TEXT NOT NULL,
                page INTEGER NOT NULL
            )
            """
        )

        # Commit the changes automatically
        connection.commit()


def addEntry(name: str, path: str, page: int = 0) -> None:
    """
    Add or update an entry in the reading list.

    If an entry with the given path already exists, it updates the page and readDate.
    Otherwise, it adds a new entry.

    Args:
        name (str): The name of the comic.
        path (str): The path to the comic file.
        page (int, optional): The last page read. Defaults to 0.
    """
    with sqlite3.connect(DATABASE_FILE_NAME) as connection:
        logger.info("Database created and connected successfully!")

        cursor = connection.cursor()

        # Check if the entry already exists
        result = cursor.execute(f"SELECT id FROM {TABLE_NAME} WHERE path = ?", (path,)).fetchall()

        if result:
            logger.info("Entry already exists in database")

            for res in result:
                query = f"""
                UPDATE {TABLE_NAME}
                SET page = ?, readDate = ?
                WHERE id = ?
                """
                cursor.execute(query, (page, datetime.datetime.now(), res[0]))

        else:
            logger.info("Adding new entry to database")

            cursor.execute(
                f"""
                INSERT INTO {TABLE_NAME} (name, path, readDate, page)
                VALUES (?, ?, ?, ?)
                """,
                (name, path, datetime.datetime.now(), page),
            )

        # Commit the changes automatically
        connection.commit()


def getLastComicPage(path: str) -> Optional[int]:
    """
    Retrieve the last page number read for a given comic path.

    Args:
        path (str): The path to the comic file.

    Returns:
        Optional[int]: The last page number read, or None if the entry does not exist.
    """
    with sqlite3.connect(DATABASE_FILE_NAME) as connection:
        logger.info("Database created and connected successfully!")

        cursor = connection.cursor()

        # Query the database for the page number
        result = cursor.execute(f"SELECT page FROM {TABLE_NAME} WHERE path = ?", (path,)).fetchone()

        if result:
            logger.info("Entry found in database")
            return result[0]
        else:
            logger.info("Entry not found in database")
            return None


# Ensure the table is created when the module is loaded
createTable()
