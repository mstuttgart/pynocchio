# -*- coding: utf-8 -*-

import logging
import rarfile

from .comic_file_loader import ComicLoader
from .utility import get_file_extension
from .utility import IMAGE_FILE_FORMATS
from .comic import Page
from .exception import NoDataFindException

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def is_rarfile(file_name):
    """Verify if file is rar file

        Args:
            file_name: name of file

        Returns: True if file is a rar file otherwise, False

    """
    return rarfile.is_rarfile(file_name)


class ComicRarLoader(ComicLoader):

    def __init__(self):
        super(ComicRarLoader, self).__init__()

    def load(self, file_name):
        """ Load zip file and create Page objects whit them.

            Args:
                file_name: name of compact zip file
        """

        with rarfile.RarFile(file_name, 'r') as rar:

            name_list = rar.namelist()
            name_list.sort()
            aux = 100.0 / len(name_list)
            page = 1
            self.data = []

            for idx, name in enumerate(name_list):

                if get_file_extension(name).lower() in IMAGE_FILE_FORMATS:
                    try:
                        self.data.append(Page(rar.read(name), name, page))
                        page += 1
                    except rarfile.BadRarFile as exc:
                        logger.exception('Error in read %s file. %s' % (name,
                                                                        exc))

                self.progress.emit(idx * aux)

            if not self.data:
                logger.exception('No one file is loaded!')
                raise NoDataFindException('No one file is loaded!')
