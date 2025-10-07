from datetime import datetime, timedelta, timezone

from datetime import datetime, timedelta, timezone

def format_datetime(time_str):
    try:
        if not time_str:
            raise ValueError("Empty string detected for posted_time")

        # Remove weekday
        _, rest = time_str.split(",", 1)
        rest = rest.strip()

        # Split off timezone
        datetime_part, tz_part = rest.split("(", 1)
        datetime_part = datetime_part.strip()
        tz_offset = int(tz_part.replace("GMT", "").replace(")", "").strip())

        # Parse date and time
        dt = datetime.strptime(datetime_part, "%d/%m/%Y, %H:%M")

        # Attach timezone
        # dt = dt.replace(tzinfo=timezone(timedelta(hours=tz_offset)))

        return dt.isoformat()

    except Exception as e:
        raise ValueError(f"Failed to parse posted_time: {e}")
