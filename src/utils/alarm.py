import threading

from src.utils.MosquittoMessage import publish_message

# Diccionario para almacenar las alarmas
alarms = {}
topic = 'buzzer'

def add_alarm(id, time, mode):
    def alarma():
        publish_message('True',topic=topic)
    
    timer = threading.Timer(time, alarma)
    alarms[id] = timer
    timer.start()


# Función para listar las alarmas
def get_alarms():
    return list(alarms.keys())

# Función para eliminar una alarma por su mensaje
def delete_alarm(mensaje):
    if mensaje in alarms:
        alarms[mensaje].cancel()
        del alarms[mensaje]
        return f'Alarma "{mensaje}" eliminada.'
    else:
        return f'No se encontró una alarma con el mensaje "{mensaje}".'