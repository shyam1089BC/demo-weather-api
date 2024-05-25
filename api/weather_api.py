# -*- coding: utf-8 -*-
# Adapter for the weather API
import os
import requests
import json

# Get the API key secret from secret env. However it is hardcoded here for demo
# Ideally env varibale would be set using any secret manager during docker image build step
API_KEY = os.environ.get("API_KEY", "17e7e807e57c87c05d3da344b76d31dc")
BASE_URL = "http://api.openweathermap.org/data/2.5"

APP_ID_KEY = {"appid": API_KEY}

def get_current_weather(query_params={}):
    query_params.update(APP_ID_KEY)
    url = f'{BASE_URL}/weather'
    response = requests.get(url, headers={}, params=query_params)
    return response.status_code, json.loads(response.content.decode('utf-8'))

def get_weather_forecast(query_params={}):
    query_params.update(APP_ID_KEY)
    url = f'{BASE_URL}/forecast'
    response = requests.get(url, headers={}, params=query_params)
    return response.status_code, json.loads(response.content.decode('utf-8'))