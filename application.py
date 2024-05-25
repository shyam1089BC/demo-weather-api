# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, make_response
from flask_api import status

from api import weather_api
from api import schema

app = Flask(__name__)

SUCCESS_RESPONSE = {"status": "success", "status_code": status.HTTP_200_OK }


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Requested URL not found.'}), status.HTTP_404_NOT_FOUND)


@app.route('/api/v1/weather', methods=['GET'])
def get_current_weather():
    args = request.args.copy().to_dict()
    status_code, data = weather_api.get_current_weather(args)
    if status_code != status.HTTP_200_OK:
        return make_response(jsonify(data), status_code)
    resp = SUCCESS_RESPONSE.copy()
    resp.update({'data': data})
    return make_response(jsonify(resp), status_code)

# Implemented a POST method just for the sake of demo, underlying  API calls to weather API is still GET
@app.route('/api/v1/forecast', methods=['POST'])
def get_weather_forecast():
    try:
        request_json = request.get_json()
        if not isinstance(request_json, dict) or not request_json:
            raise Exception("Invalid Json")
    except:
        request_json = {}
    # Validating input json body
    error, data = schema.validate_input_json(request_json)
    if error:
        resp = {'errorDescription': 'Invalid input body or missing required field.', "status": "error"}
        resp.update({"fields": data})
        return make_response(jsonify(resp), status.HTTP_400_BAD_REQUEST)
 
    status_code, data = weather_api.get_weather_forecast(request_json)
    if status_code != status.HTTP_200_OK:
        return make_response(jsonify(data), status_code)
    resp = SUCCESS_RESPONSE.copy()
    resp.update({'data': data})
    return make_response(jsonify(resp), status_code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
