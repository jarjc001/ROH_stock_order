import datetime as dt

today: dt.datetime = dt.datetime.today()
tomorrow: dt.datetime = today + dt.timedelta(days=1)

date_format_full: str = "%d.%m.%y"
date_format_day: str = "%d"

file_name: str = f"RunningOrderReport-{tomorrow.strftime(date_format_full)}.csv"


def suffix(d):
    if 11 <= d <= 13:
        return 'th'
    else:
        return {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')
