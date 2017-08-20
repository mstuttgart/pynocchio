# -*- coding: utf-8 -*-

import logging
import zipfile

from .comic_file_loader import ComicLoader
from .utility import get_file_extension
from .utility import IMAGE_FILE_FORMATS
from .comic import Page
from .exception import NoDataFindException

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def is_zipfile(file_name):
    """Verify if file is zip file

    Args:
        file_name: name of file

    Returns: True if file is a zip file otherwise, False

    """
    return zipfile.is_zipfile(file_name)


class ComicZipLoader(ComicLoader):

    def __init__(self):
        super(ComicZipLoader, self).__init__()

    def load(self, file_name):
        """ Load zip file and create Page objects whit them.

        Args:
            file_name: name of compact zip file
        """

        with zipfile.ZipFile(file_name, 'r') as zf:

            name_list = zf.namelist()
            name_list.sort()
            aux = 100.0 / len(name_list)
            page = 1
            self.data = []

            for idx, name in enumerate(name_list):

                if get_file_extension(name).lower() in IMAGE_FILE_FORMATS:
                    try:
                        self.data.append(Page(zf.read(name), name, page))
                        page += 1
                    except zipfile.BadZipfile as exc:
                        logger.exception('Error in read %s file. %s' % (name,
                                                                        exc))

                self.progress.emit(idx * aux)

            if not self.data:
                raise NoDataFindException('No one file is loaded!')
