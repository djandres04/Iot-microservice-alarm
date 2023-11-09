from datetime import datetime, timedelta
import pytz

time_zone = pytz.timezone('America/Bogota')


def convert_time(isodate):
    parsed_date = datetime.strptime(isodate, "%Y-%m-%dT%H:%M:%S.%fZ")

    current_time = time_now()
    time_difference = parsed_date - current_time

    time_in_seconds = int(time_difference.total_seconds())
    return time_in_seconds


def time_now(hour=0, minute=0, second=0):
    # Obtén la hora en la zona horaria deseada
    date_string = datetime.now(time_zone) + timedelta(hours=hour, minutes=minute, seconds=second)
    # Formatea la hora en el formato deseado (sin zona horaria)
    formatted_date = date_string.strftime('%Y-%m-%d %H:%M:%S')
    # Utiliza strptime() para analizar la cadena
    date_time_obj = datetime.strptime(formatted_date, '%Y-%m-%d %H:%M:%S')
    return date_time_obj
