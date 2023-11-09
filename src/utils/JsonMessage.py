from flask import jsonify


def message_error(error):
    data = {'message': str(error)}
    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json'
    return response, 500


def message(message_send):
    data = {'message': message_send}
    response = jsonify(data)
    response.headers['Content-Type'] = 'application/json'
    return response, 200


def message_all(message_send):
    print(message_send)
    response = jsonify(message_send)
    response.headers['Content-Type'] = 'application/json'
    return response, 200
