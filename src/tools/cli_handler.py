import logging
import argparse
from pathlib import Path


logger = logging.getLogger(__name__)


def get_file_path() -> Path:
    """
    Gets the path to the source file via the console
    """
    parser = argparse.ArgumentParser(description="Incoming Control System")
    parser.add_argument("raw_file", nargs="?", help="Path to raw data file")
    args = parser.parse_args()

    if args.raw_file:
        path = Path(args.raw_file.strip('"'))
        logger.info(f"The path has been chosen: {path}.")
        return path

    while True:
        user_input = input(
            f"Enter the path to the file or paste the file into the console: "
        )

        if user_input:
            path = Path(user_input)
            logger.info(f"The path has been chosen: {path}.")
            return path

        logger.error(f"Alert! File path is missing.")
