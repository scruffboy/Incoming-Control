import json
from datetime import datetime, date
from typing import Dict


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
            print(f"Alert: Unknown time format '{type(dt)}'")
            return dt

    @staticmethod
    def load_json(file_path) -> Dict | None:
        """
        Load JSON from a file
        """
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Eroor loading: '{e}'")
            return None
