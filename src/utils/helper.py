import json
import logging
from typing import Dict, List
from dataclasses import asdict
from datetime import datetime, date


logger = logging.getLogger(__name__)


class Utils:
    """
    Task Utilities
    """

    @staticmethod
    def formatting_date(dt) -> date:
        """
        Formats datetime to date
        """
        if isinstance(dt, str):
            dt_obj = datetime.strptime(str(dt), "%d.%m.%Y %H:%M:%S")
            return dt_obj.date()
        elif isinstance(dt, datetime):
            return dt.date()
        else:
            logger.error(f"Unknown time format '{type(dt)}'")
            return dt

    @staticmethod
    def load_json(file_path) -> Dict | None:
        """
        Load JSON from a file
        """
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading: '{e}'")
            return None

    @staticmethod
    def formatting_obj_into_dict(obj_list: List) -> List[Dict]:
        """
        Formats a list of objects into a list of dictionaries
        """
        return [asdict(obj) for obj in obj_list]
