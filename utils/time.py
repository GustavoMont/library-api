from datetime import datetime, timedelta


def calculate_return_date():
    today = datetime.today()
    return_date = today + timedelta(days = 10)
    return return_date.date()

