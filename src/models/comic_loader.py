import logging
from abc import abstractmethod

from PySide6.QtCore import QObject, QRunnable, Signal, Slot

from src.models.constants import LOGGING_VERBOSITY
from src.models.page import Page

logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_VERBOSITY)


class LoaderSignals(QObject):
    """
    Signals emitted by the LoaderSignals class to communicate the state of a loading process.

    Signals:
        loadProgressSignal (Signal[int]):
            Emitted to indicate the current progress of loading, represented as an integer percentage.

        startProgressSignal (Signal[int]):
            Emitted to indicate the start of a process, with an integer parameter for initialization.

        doneProgressSignal (Signal[str, object]):
            Emitted when a process is completed, carrying the filename as a string and the loaded data as an object.

        finishProgressSignal (Signal):
            Emitted to indicate the completion of all processes, with no additional data.

        errorLoadSignal (Signal[str]):
            Emitted when an error occurs during the loading process, carrying the error message as a string.
    """

    loadProgressSignal = Signal(int)
    startProgressSignal = Signal(int)
    doneProgressSignal = Signal(str, object)
    finishProgressSignal = Signal()
    errorLoadSignal = Signal(str)


class ComicLoader(QRunnable):
    """
    Abstract class for loading comic files.

    This class serves as a base for different comic file loaders,
    such as ZIP, RAR, and TAR loaders.
    """

    def __init__(self, filename: str) -> None:
        """
        Initializes the ComicLoader instance.

        Args:
            filename (str): The path to the comic file.
        """
        super().__init__()
        self._data: list[Page] = []
        self._signals = LoaderSignals()
        self._filename: str = filename

    @Slot()
    def run(self) -> None:
        """
        Executes the `run` method to load a file and handle progress signals.

        This method attempts to load a file using the `load` method. If an exception
        occurs during the loading process, it logs the error and emits an `errorLoadSignal`
        with the error message. Upon successful loading, it emits a `doneProgressSignal`
        with the filename and loaded data. Regardless of success or failure, it emits a
        `finishProgressSignal` to indicate the completion of the process.
        """
        try:
            self.load(self._filename)

        except ValueError as exc:
            logger.exception(f"ValueError while loading {self._filename}: {exc}")
            self._signals.errorLoadSignal.emit(str(exc))

        except Exception as exc:
            logger.exception(f"Unexpected error while loading {self._filename}: {exc}")
            self._signals.errorLoadSignal.emit(str(exc))

        else:
            self._signals.doneProgressSignal.emit(self._filename, self._data)

        finally:
            self._signals.finishProgressSignal.emit()

    @abstractmethod
    def load(self, filename: str) -> None:
        """
        Abstract method to load a comic file.

        Args:
            filename (str): The path to the comic file.

        Raises:
            NotImplementedError: If the method is not implemented in a subclass.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def setData(self, data: list[Page]) -> None:
        """
        Sets the data for the comic loader.

        Args:
            data (List[Page]): The data to be set.
        """
        self._data = data

    def getData(self) -> list[Page]:
        """
        Gets the data stored in the comic loader.

        Returns:
            List[Page]: The stored data.
        """
        return self._data

    def getSignals(self) -> LoaderSignals:
        """
        Gets the signals object for the comic loader.

        Returns:
            LoaderSignals: The signals object.
        """
        return self._signals
