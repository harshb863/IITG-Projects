import datetime
def green(text):
    return f"\033[92m{text}\033[0m"
def format_date(date):
    try:
        return datetime.datetime.strptime(date, "%d-%m-%Y").strftime("%Y-%m-%d")
    except:
        return datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m-%d")