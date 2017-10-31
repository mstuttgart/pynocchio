import logging
import subprocess
import numpy as np
from re import findall
from os import path

from .comic.file.loader import ComicLoader
from .utility import get_file_extension
from .utility import IMAGE_FILE_FORMATS, COMPACT_FILE_FORMATS
from .comic import Page
from .exception import NoDataFindException

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# The 7z program should be installed on the computer for this code to work
# Download it from http://www.7-zip.org/ or if running Linux you can
# run 'sudo apt-get install p7zip-full' in the terminal
def is_7zfile(filename):
    """ Verify if the file is a 7zip archive

    Args:
        filename: name of file

    Returns:
        True if file is 7zip archive, False otherwise"""
    if isinstance(filename,str):
        return filename.endswith('.7z')

def get_namelist(filename):
    """ List the contents of the 7zip file

    Args:
        filename: name of compressed file

    Returns:
        Numpy ndarray with the file names"""

    # Get absolute path and directory of filename
    fileloc = path.abspath(path.dirname(filename))
    # Get the listing data from the 7z tool in bytes
    bytes_list = subprocess.Popen(['7z','l', fileloc + "/" + filename],
    stdout=subprocess.PIPE).communicate()[0]
    # Convert to string and divide into lines
    f_lines = bytes_list.decode('utf-8').split('\n')

    list_fields = []
    for l in f_lines:
        fields = findall("(^.+\.A +)(\d+)( +\d* +)([]\w/.\d]+)", l)
        # check if line is a subfolder or folder
        if len(fields) != 1:
            continue
        f_name = path.basename(fields[0][3])
        list_fields.append(f_name)

    return np.array(list_fields)


class Comic7zLoader(ComicLoader):

    def __init__(self):
        super(Comic7zLoader,self).__init__()

    def load(self, filename):
        """ Load 7z file and create Page object with it.

        Args:
            filename: name of compact 7z file

        """
        # Get absolute path and directory of filename
        fileloc = path.abspath(path.dirname(filename))
        # Get the file names and order them alphabetically in descending order
        name_list = sorted(get_namelist(filename=filename), reverse=True)
        aux = 100.0 / len(name_list)
        page = 1
        self.data = []

        for idx, name in enumerate(name_list):

            if get_file_extension(name).lower() in IMAGE_FILE_FORMATS:
                try:
                    # Unpack the "name" 7z file
                    commands = ['7z', 'e', fileloc + '/' + filename, '-so', name, '-r']
                    # to keep it cleaner the commands and data are under different variables
                    data = subprocess.Popen(commands, stdout=subprocess.PIPE).communicate()[0]
                    self.data.append(Page(data, name, page))
                    page += 1
                # TODO: add a proper exception here
                except pass

            self.progress.emit(idx*aux)

        if not self.data:
            logger.exception('No one file is loaded!')
            raise NoDataFindException('No one file is loaded!')
