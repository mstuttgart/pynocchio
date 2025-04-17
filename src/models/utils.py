import os


def getFileExtension(filename: str) -> str:
    """
    Get the file extension from a filename.

    Args:
        filename (str): The name of the file.

    Returns:
        str: The file extension, including the leading dot.
    """
    return os.path.splitext(filename)[1]


def getDirName(filePath: str) -> str:
    """
    Get the directory name from a file path.

    Args:
        filePath (str): The full file path.

    Returns:
        str: The directory name.
    """
    return os.path.dirname(filePath)


def getBaseName(filePath: str) -> str:
    """
    Get the base name (file name with extension) from a file path.

    Args:
        filePath (str): The full file path.

    Returns:
        str: The base name of the file.
    """
    return os.path.basename(filePath)


def getParentPath(filePath: str) -> str:
    """
    Get the parent directory path of a given file path.

    Args:
        filePath (str): The full file path.

    Returns:
        str: The parent directory path.
    """
    return os.path.split(os.path.abspath(os.path.dirname(filePath)))[0]


def joinPath(rootDir: str, directory: str, filename: str) -> str:
    """
    Join root directory, subdirectory, and filename into a single path.

    Args:
        rootDir (str): The root directory.
        directory (str): The subdirectory.
        filename (str): The file name.

    Returns:
        str: The combined file path.
    """
    return os.path.join(rootDir, directory, filename)


def pathExist(filePath: str) -> bool:
    """
    Check if a path exists (including broken symbolic links).

    Args:
        filePath (str): The path to check.

    Returns:
        bool: True if the path exists, False otherwise.
    """
    return os.path.lexists(filePath)


def fileExist(filePath: str) -> bool:
    """
    Check if a file exists.

    Args:
        filePath (str): The file path to check.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.exists(filePath)


def isDir(filePath: str) -> bool:
    """
    Check if a path is a directory.

    Args:
        filePath (str): The path to check.

    Returns:
        bool: True if the path is a directory, False otherwise.
    """
    return os.path.isdir(filePath)


def isFile(filename: str) -> bool:
    """
    Check if a path is a file.

    Args:
        filename (str): The file path to check.

    Returns:
        bool: True if the path is a file, False otherwise.
    """
    return os.path.isfile(filename)


def convertStringToBoolean(string: str) -> bool:
    """
    Convert a string to a boolean value.

    Args:
        string (str): The string to convert. Must be "True" or "False".

    Returns:
        bool: The corresponding boolean value.

    Raises:
        ValueError: If the string is not "True" or "False".
    """
    if string == "True":
        return True
    elif string == "False":
        return False
    else:
        raise ValueError(f"Invalid string for boolean conversion: {string}")
