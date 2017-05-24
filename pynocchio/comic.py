# -*- coding: utf-8 -*-
import os

class Comic:
    """This is basic class of Pynocchio. Represents a comic object"""

    # FILE = 0
    # FOLDER = 1
    #
    # def __init__(self, name, directory, comic_type=FILE):
    #     self.name = name
    #     self.directory = directory
    #     self.type = comic_type
    #     self.pages = []

    def __init__(self, name, directory):
        """
        Comic class __init__ method

        Args:
            name (str): comic name
            directory (str): comic file directory
        """
        self.name = name
        self.directory = directory

        # list of Page: list to store the comic pages objects
        self.pages = []

    def get_number_of_pages(self):
        """ Return comic pages amount

        Returns:
            int: The retirn value. Represents amount of comic pages
        """
        return len(self.pages)

    def get_path(self):
        """ Get complete comic path, i.g. comic path concatenaded with
             comic name.

        Returns:
            str: The return value. Represents complete comic path.
        """
        return os.path.join(self.directory, self.name)


class Page:
    """This is basic class of Pynocchio. Represents a comic page object"""

    def __init__(self, data, title, number):
        self.data = data
        self.title = title
        self.number = number
