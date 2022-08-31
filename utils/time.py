from datetime import datetime, timedelta


def calculate_return_date():
    today = datetime.today()
    return today + timedelta(days = 10)

