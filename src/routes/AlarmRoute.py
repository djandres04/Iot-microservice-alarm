from flask import Blueprint, jsonify, request

from src.utils import JsonMessage
from src.utils import alarm

main = Blueprint('alarm_blueprint',__name__)

@main.route('/add', methods=['POST'])
def add_alarm():
    try:
        if request.json is None:
            return JsonMessage.message("Json empty")
        else:
            try:
                id_alarm = request["id_alarm"]
                time = request.json["time_alarm"]
                mode = request.json["mode"]

                alarm.add_alarm(id=id_alarm,time=time,mode=mode)

                return JsonMessage.message()
            except Exception as ex:
                print(str(ex))
                return JsonMessage.message_error(ex)

    except Exception as ex:
        print(str(ex))
        return JsonMessage.message_error(ex)
    
@main.route('/', methods=['GET'])
def list_alarms():
    active_alarm = alarm.get_alarms
    return jsonify({'alarmas': active_alarm})

@main.route('/delete', methods=['DELETE'])
def delete_alarms():
    return jsonify({'alarmas': list(alarmas.keys())})