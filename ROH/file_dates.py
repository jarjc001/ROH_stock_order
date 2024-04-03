import datetime as dt

today: dt.datetime = dt.datetime.today()
tomorrow: dt.datetime = today + dt.timedelta(days=1)

# value to change if script will collect for today or tomorrow's order
for_tomorrow: bool = False

# date of order being collected
date_of_order: dt.datetime

if for_tomorrow:
    date_of_order = tomorrow
else:
    date_of_order = today

date_format_full: str = "%d.%m.%y"
date_format_day: str = "%d"

file_name: str = f"RunningOrderReport-{date_of_order.strftime(date_format_full)}.csv"


def suffix(d):
    if 11 <= d <= 13:
        return 'th'
    else:
        return {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')
