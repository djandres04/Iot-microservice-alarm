from bson.json_util import dumps

from flask import Blueprint, jsonify, request

from utils import JsonMessage

from models import AlarmModel

main = Blueprint('alarm_blueprint', __name__)
database_id = "smartHome"


@main.route('/add', methods=['POST'])
def add_alarm():
    try:
        if request.json is None:
            return JsonMessage.message("Json empty")
        else:
            try:
                data = request.json

                id_alarm = data.get("id_alarm")
                time = data.get("time_alarm")
                description = data.get("description")
                person = data.get("person")

                AlarmModel.add_alarm(database_id=database_id, id=id_alarm, time=time, description=description,
                                     person=person)

                return JsonMessage.message("succesfull add alarm")
            except Exception as ex:
                print(str(ex))
                return JsonMessage.message_error(ex)

    except Exception as ex:
        print(str(ex))
        return JsonMessage.message_error(ex)


@main.route('/', methods=['GET'])
def list_alarms():
    active_alarm = AlarmModel.active_alarm()
    return JsonMessage.message(active_alarm)


@main.route('/all', methods=['GET'])
def get_alarms():
    return dumps(AlarmModel.get_alarms(database_id))


@main.route('/delete/<id>', methods=['DELETE'])
def delete_alarms(id):
    if AlarmModel.delete_alarm(id):
        return JsonMessage.message('successful delete')
    else:
        return JsonMessage.message("alarm doesn't delete")
