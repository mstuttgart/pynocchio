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
import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from PySide6.QtCore import QStandardPaths

from src.__version__ import __version__

# Load environment variables from a .env file
load_dotenv()

# Debugging and logging configuration
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
LOGGING_VERBOSITY = os.getenv("LOGGING_VERBOSITY", "INFO").upper()
LANGUAGE = os.getenv("LANGUAGE", "Auto")

# Application metadata
YEAR = datetime.datetime.now().year
AUTHOR = "Michell Stuttgart"
VERSION = __version__
APP_NAME = "Pynocchio"

# File names
DATABASE_FILE_NAME = f"{APP_NAME.lower()}.db"
CONFIG_FILE_NAME = f"{APP_NAME.lower()}.json"

# URLs
HELP_URL = "https://github.com/mstuttgart/pynocchio/issues"
FEEDBACK_URL = "https://github.com/mstuttgart/pynocchio/issues"
RELEASE_URL = "https://github.com/mstuttgart/pynocchio/releases/latest"
LICENSE_URL = "https://github.com/mstuttgart/pynocchio/blob/develop/LICENSE"
COPYRIGHT = f"Copyright (C) 2014-{YEAR} {AUTHOR}"

# Image file formats (supported by the application)
IMAGE_FILE_FORMATS: list[str] = [
    ".bmp",
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    ".pdf",
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

SUPPORTED_FILES: list[str] = IMAGE_FILE_FORMATS + COMPACT_FILE_FORMATS

if DEBUG:
    CONFIG_FOLDER = Path("AppData").absolute()
    LOGGING_VERBOSITY = logging.DEBUG
else:
    CONFIG_FOLDER = os.path.join(
        Path(QStandardPaths.writableLocation(QStandardPaths.AppConfigLocation)), APP_NAME
    )
    LOGGING_VERBOSITY = logging.INFO

# config file location
CONFIG_FILE = os.path.join(
    CONFIG_FOLDER,
    f"{CONFIG_FILE_NAME}",
)

# database file location
DATABASE_FILE = os.path.join(
    CONFIG_FOLDER,
    f"{DATABASE_FILE_NAME}",
)


class Language(enum.Enum):
    """Language enumeration"""

    ENGLISH = "en"
    PORTUGUESE_BR = "pt_BR"
    AUTO = "Auto"
