from flask import Flask, request, jsonify

from routes import AlarmRoute

from config import config

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.config.from_object(config['development'])

    app.register_blueprint(AlarmRoute.main, url_prefix='/')

    app.run(host="0.0.0.0", port=5100, debug=True)
