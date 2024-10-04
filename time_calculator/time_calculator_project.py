def add_time(start, duration, day=None):
    # Splitting start time into components
    parts = start.split()
    hours, minutes = map(int, parts[0].split(':'))
    period = parts[1]

    # Convert start time to 24-hour format
    if period == "PM" and hours != 12:
        hours += 12
    elif period == "AM" and hours == 12:
        hours = 0

    # Splitting duration time into components
    dur_hours, dur_minutes = map(int, duration.split(':'))

    # Adding duration to the current time
    total_minutes = hours * 60 + minutes + dur_hours * 60 + dur_minutes
    final_hour = (total_minutes // 60) % 24
    final_minutes = total_minutes % 60
    past_days = total_minutes // (24 * 60)

    # Adjusting final hour to 12-hour format and period
    if final_hour >= 12:
        period = "PM"
        if final_hour > 12:
            final_hour -= 12
    else:
        period = "AM"
        if final_hour == 0:
            final_hour = 12

    # Calculate day of the week if provided
    week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    if day:
        day = day.capitalize()
        day_index = week_days.index(day)
        new_day_index = (day_index + past_days) % 7
        new_day = week_days[new_day_index]
        day_part = f", {new_day}"
    else:
        day_part = ""

    # Adding suffix for the number of days later
    if past_days == 0:
        days_later = ""
    elif past_days == 1:
        days_later = " (next day)"
    else:
        days_later = f" ({past_days} days later)"

    # Formatting the final time
    new_time = f"{final_hour}:{final_minutes:02d} {period}{day_part}{days_later}"
    return new_time


print(add_time('3:00 PM', '3:10'))
# Returns: 6:10 PM

print(add_time('11:30 AM', '2:32', 'Monday'))
# Returns: 2:02 PM, Monday

print(add_time('11:43 AM', '00:20'))
# Returns: 12:03 PM

print(add_time('10:10 PM', '3:30'))
# Returns: 1:40 AM (next day)

print(add_time('11:43 PM', '24:20', 'tueSday'))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time('6:30 PM', '205:12'))
# Returns: 7:42 AM (9 days later)
