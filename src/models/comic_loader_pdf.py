import logging
import tempfile
import threading

from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError,
)

from src.models.comic_loader import ComicLoader
from src.models.constants import LOGGING_VERBOSITY
from src.models.page import Page

logger = logging.getLogger(__name__)
logger.setLevel(LOGGING_VERBOSITY)


class ComicPdfLoader(ComicLoader):
    """
    Comic PDF file loader class.
    This class is responsible for loading PDF files and creating Page
    objects with them. It inherits from the ComicLoader class and
    implements the load method to read PDF files.
    """

    def load(self, filename: str) -> None:
        """
        This method reads the contents of a PDF file, processes each file within the archive,
        and creates Page objects for valid image files. The loading process is performed
        using multiple threads to improve performance.

        Raises:
            ValueError: If the PDF file cannot be read, contains no valid pages, or if an error
            occurs during the loading process.

        Notes:
            - The method emits progress signals during the loading process:
              `startProgressSignal` is emitted with the total number of files to process,
              and `loadProgressSignal` is emitted after each file is processed.
            - Only files with extensions matching `IMAGE_FILE_FORMATS` are processed as pages.
            - Pages are sorted by their page number after loading.
        """

        logger.info("Attempting to load file: %s", filename)

        try:
            with tempfile.TemporaryDirectory() as path:
                pages = convert_from_path(
                    filename, output_folder=path, thread_count=4, dpi=300, use_cropbox=True
                )

                logger.debug("PDF file loaded successfully.")
                logger.debug("Number of pages in PDF: %d", len(pages))

                # # Emit the start progress signal with the number of files
                self.getSignals().startProgressSignal.emit(len(pages))

                def readPdfFileThread(page, number) -> None:
                    """Thread function to read a single PDF page and convert it to a QImage.

                    Args:
                        page (pymupdf.Page): The PDF page object to process.
                    """

                    try:
                        number = number + 1
                        pixmap = page
                        self._data.append(Page(pixmap, f"page {number}", number))

                    except Exception as exc:
                        logger.error("Other error reading PDF file: %s" % exc)

                # Create a list to hold the threads
                threads = []

                # Start threads to read each file in the PDF archive
                for index, page in enumerate(pages):
                    logger.debug("Processing page: %s", index)

                    thread = threading.Thread(
                        target=readPdfFileThread,
                        args=(page, index),
                    )

                    threads.append(thread)
                    thread.start()
                    thread.join()
                    self.getSignals().loadProgressSignal.emit(index)

            # Sort the pages by their number
            self._data.sort(key=lambda x: x.getNumber())

        except PDFInfoNotInstalledError as exc:
            logger.error("PDFInfoNotInstalledError: %s", exc)
            raise ValueError("PDFInfoNotInstalledError: %s" % exc) from exc

        except PDFPageCountError as exc:
            logger.error("PDFPageCountError: %s", exc)
            raise ValueError("PDFPageCountError: %s" % exc) from exc

        except PDFSyntaxError as exc:
            logger.error("PDFSyntaxError: %s", exc)
            raise ValueError("PDFSyntaxError: %s" % exc) from exc

        if not self._data:
            logger.error("No valid data found in the PDF file: %s", filename)
            raise ValueError("No valid data found in the PDF file.")

        logger.info("Successfully loaded %d pages from %s", len(self._data), filename)
