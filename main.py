import re

def add_time(start, duration, day=None):
    # Parsing the `start` time
    match = re.match(r"(\d+):(\d+)\s?(AM|PM)", start)
    if not match:
        return "Error: Invalid start time format."

    start_hour = int(match.group(1))  # Extract the hour
    start_minute = int(match.group(2))  # Extract the minute
    start_period = match.group(3)  # Extract AM/PM

    # Convert start time to 24-hour format
    if start_period == "PM" and start_hour != 12:
        start_hour += 12
    if start_period == "AM" and start_hour == 12:
        start_hour = 0

    # Parsing `duration`
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Add duration to start time
    total_minutes = start_minute + duration_minute
    total_hours = start_hour + duration_hour + (total_minutes // 60)
    final_minutes = total_minutes % 60
    final_hour_24 = total_hours % 24
    days_later = total_hours // 24

    # Convert back to 12-hour format
    final_period = "AM" if final_hour_24 < 12 else "PM"
    final_hour_12 = final_hour_24 % 12
    if final_hour_12 == 0:
        final_hour_12 = 12

    # Construct the final time string
    new_time = f"{final_hour_12}:{final_minutes:02d} {final_period}"

    # Add day of the week if provided
    if day:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day = day.strip().capitalize()  # Normalize input day
        start_day_index = days_of_week.index(day)
        final_day = days_of_week[(start_day_index + days_later) % 7]
        new_time += f", {final_day}"

    # Add days later message
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time

# Example usage
print(add_time("3:00 PM", "64:30", "Tuesday"))