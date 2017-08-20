# -*- coding: utf-8 -*-

import logging
import tarfile

from .comic_file_loader import ComicLoader
from .utility import get_file_extension
from .utility import IMAGE_FILE_FORMATS
from .comic import Page
from .exception import NoDataFindException

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def is_tarfile(file_name):
    """Verify if file is tar file

    Args:
        file_name: name of file

    Returns: True if file is a tar file otherwise, False

    """
    return tarfile.is_tarfile(file_name)


class ComicTarLoader(ComicLoader):

    def __init__(self):
        super(ComicTarLoader, self).__init__()

    def load(self, file_name):
        """ Load zip file and create Page objects whit them.

            Args:
                file_name: name of compact zip file
        """

        with tarfile.open(file_name, 'r') as tar:

            name_list = tar.getnames()
            name_list.sort()
            aux = 100.0 / len(name_list)
            page = 1
            self.data = []

            for idx, name in enumerate(name_list):

                if get_file_extension(name).lower() in IMAGE_FILE_FORMATS:
                    try:
                        data = tar.extractfile(name).read()
                        self.data.append(Page(data, name, page))
                        page += 1
                    except tarfile.ExtractError as exc:
                        logger.exception('Error in extract %s file. %s' %
                                         (name, exc))
                    except tarfile.ReadError as exc:
                        logger.exception('Error in read %s file. %s' % (name,
                                                                        exc))

                self.progress.emit(idx * aux)

            if not self.data:
                raise NoDataFindException('No one file is loaded!')
