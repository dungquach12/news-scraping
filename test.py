from datetime import datetime, timedelta, timezone

time_str = "Thứ ba, 30/9/2025, 05:00 (GMT+7)"

# Remove weekday (before first comma)
_, rest = time_str.split(",", 1)
rest = rest.strip()  # "30/9/2025, 05:00 (GMT+7)"

# Split off timezone "(GMT+7)"
datetime_part, tz_part = rest.split("(", 1)
datetime_part = datetime_part.strip()           # "30/9/2025, 05:00"
tz_offset = int(tz_part.strip("GMT+)"))         # 7

# Parse date and time
dt = datetime.strptime(datetime_part, "%d/%m/%Y, %H:%M")

# Attach timezone
dt = dt.replace(tzinfo=timezone(timedelta(hours=tz_offset)))

print(dt)