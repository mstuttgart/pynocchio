import logging

from .comic_file_loader_dir import ComicDirLoader
from .utility import IMAGE_FILE_FORMATS, get_dir_name, get_base_name

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ComicImageLoader(ComicDirLoader):

    def __init__(self):
        super().__init__()

    def load(self, filename):
        """ Load image file and create Page objects with them.

            Args:
                filename: name of compact image file
        """

        dir_name = get_dir_name(filename)

        super().load(dir_name)

        for i, page in enumerate(self.data):
            if page.title == get_base_name(filename):
                self.initial_page = i
