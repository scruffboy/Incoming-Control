from datetime import datetime, date


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
        
    def rename_
