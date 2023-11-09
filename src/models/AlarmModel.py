import threading

from utils.MosquittoMessage import publish_message
from utils import ConverterTime

from models.entities.Alarm import alarm

from database.db import get_connection

# Diccionario para almacenar las alarmas
alarms = {}
topic = 'buzzer'


def add_alarm(database_id, id, time, description, person):
    def alarma(alarm_id):
        client_db = get_connection(database_id, "Alarms")
        print("alarm #"+alarm_id)
        publish_message('True', topic)

        temp = {"id": alarm_id}
        client_db.update_one(temp, {"$set": {"status": "True"}})

    client_db = get_connection(database_id, "Alarms")
    historical_db = get_connection(database_id, "AlarmHistory")

    temp = {"id": id}
    temp_search = client_db.find_one(temp)

    if temp_search:
        print("searching")
        client_db.update_one(temp, {"$set": {"date_alarm": time, "status": "False"}})
        historical_db.insert_one(alarm(id, description, time, person).to_JSON())
    else:
        print("update")
        temp_alarm = alarm(id, description, time, person).to_JSON()
        client_db.insert_one(temp_alarm)
        historical_db.insert_one(temp_alarm)

    temp_time = ConverterTime.convert_time(time)

    print(temp_time)
    timer = threading.Timer(temp_time, alarma, args=[id])
    alarms[id] = timer
    timer.start()


# Función para listar las alarmas
def active_alarm():
    return list(alarms.keys())


def get_alarms(database_id):
    client_db = get_connection(database_id, "Alarms")
    return client_db.find()


# Función para eliminar una alarma por su mensaje
def delete_alarm(id_alarm, person):
    if id_alarm in alarms:
        alarms[id_alarm].cancel()
        del alarms[id_alarm]
        return True
    else:
        return False
