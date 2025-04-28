"""
Module for application settings and configuration.

This module defines constants, paths, and settings used throughout the application.
It dynamically determines the configuration folder and file locations based on the
debugging state.

Attributes:
    DEBUG (bool): Indicates whether the application is in debug mode.
    LOGGING_VERBOSITY (int): Logging verbosity level.
    YEAR (int): Current year.
    AUTHOR (str): Author of the application.
    VERSION (str): Application version.
    APP_NAME (str): Name of the application.
    DATABASE_FILE_NAME (str): Name of the database file.
    CONFIG_FILE_NAME (str): Name of the configuration file.
    HELP_URL (str): URL for help documentation.
    FEEDBACK_URL (str): URL for submitting feedback or issues.
    RELEASE_URL (str): URL for the latest release.
    LICENSE_URL (str): URL for license information.
    COPYRIGHT (str): Copyright information.
    IMAGE_FILE_FORMATS (list[str]): Supported image file formats.
    COMPACT_FILE_FORMATS (list[str]): Supported compact file formats.
    SUPPORTED_FILES (list[str]): All supported file formats.
    CONFIG_FOLDER (Path): Path to the configuration folder.
    CONFIG_FILE (Path): Full path to the configuration file.
    DATABASE_FILE (Path): Full path to the database file.
"""

import datetime
import enum
import os
from pathlib import Path
from typing import Union

from dotenv import load_dotenv
from PySide6.QtCore import QStandardPaths

from src.__version__ import __version__

# Load environment variables from a .env file
load_dotenv()

# Debugging and logging configuration
DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
LOGGING_VERBOSITY: Union[int, str] = os.getenv("LOGGING_VERBOSITY", "INFO").upper()
LANGUAGE: str = os.getenv("LANGUAGE", "Auto")

# Application metadata
YEAR: int = datetime.datetime.now().year
AUTHOR: str = "Michell Stuttgart"
VERSION: str = __version__
APP_NAME: str = "Pynocchio"

# File names
DATABASE_FILE_NAME: str = f"{APP_NAME.lower()}.db"
CONFIG_FILE_NAME: str = f"{APP_NAME.lower()}.json"

# URLs
HELP_URL: str = "https://github.com/mstuttgart/pynocchio/issues"
FEEDBACK_URL: str = "https://github.com/mstuttgart/pynocchio/issues"
RELEASE_URL: str = "https://github.com/mstuttgart/pynocchio/releases/latest"
LICENSE_URL: str = "https://github.com/mstuttgart/pynocchio/blob/develop/LICENSE"
COPYRIGHT: str = f"Copyright (C) 2014-{YEAR} {AUTHOR}"

# Image file formats (supported by the application)
IMAGE_FILE_FORMATS: list[str] = [
    ".bmp",
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
]

# Compact file formats (compressed archives)
COMPACT_FILE_FORMATS: list[str] = [
    ".cbr",
    ".cbz",
    ".rar",
    ".zip",
    ".tar",
    ".cbt",
]

SUPPORTED_FILES: list[str] = (
    IMAGE_FILE_FORMATS
    + COMPACT_FILE_FORMATS
    + [
        ".pdf",
    ]
)

CONFIG_FOLDER: str = (
    ""
    if DEBUG
    else os.path.join(
        Path(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.ConfigLocation)),
        APP_NAME,
    )
)


# config file location
CONFIG_FILE: str = os.path.join(
    CONFIG_FOLDER,
    f"{CONFIG_FILE_NAME}",
)

# database file location
DATABASE_FILE: str = os.path.join(
    CONFIG_FOLDER,
    f"{DATABASE_FILE_NAME}",
)


class Language(enum.Enum):
    """Language enumeration"""

    ENGLISH = "en"
    PORTUGUESE_BR = "pt_BR"
    AUTO = "Auto"
