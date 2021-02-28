from datetime import datetime


def string_to_time(str_time):
    return datetime.strptime(str_time, '%H:%M').time()


def string_to_date(str_date):
    return datetime.strptime(str_date, '%d/%m/%Y').date()


def day_of_year(date_time):
    """
        :param date_time must be datetime.datetime
        :return int
    """
    return int(date_time.strftime('%j'))


def time_to_seconds(time):
    return time.hour * 3600 + time.minute * 60
