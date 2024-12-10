def add_time(start, duration, day=None):
    # Parsing the `start` time (12-hour format with AM/PM)
    start_hour, start_minute_period = start.split(":")
    start_minute, start_period = start_minute_period.split(" ")

    start_hour = int(start_hour)
    start_minute = int(start_minute)
    start_period = start_period.upper()  # Handle mixed case input like 'am' or 'pm'
    
    # Convert start time to 24-hour format
    if start_period == "PM" and start_hour != 12:
        start_hour += 12
    elif start_period == "AM" and start_hour == 12:
        start_hour = 0

    # Parsing the `duration` time
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Add duration to start time
    total_minutes = start_minute + duration_minute
    total_hours = start_hour + duration_hour + (total_minutes // 60)
    final_minutes = total_minutes % 60
    final_hour_24 = total_hours % 24
    days_later = total_hours // 24

    # Convert the result back to 12-hour format
    final_period = "AM" if final_hour_24 < 12 else "PM"
    final_hour_12 = final_hour_24 % 12
    if final_hour_12 == 0:
        final_hour_12 = 12

    # Construct the final time string
    new_time = f"{final_hour_12}:{final_minutes:02d} {final_period}"

    # Add day of the week if provided
    if day:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_day_index = days_of_week.index(day.strip().capitalize())
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