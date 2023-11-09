import logging
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()



def get_weather(querystring:str):
    try:
        url = "https://weatherapi-com.p.rapidapi.com/current.json"
        headers = {
            "X-RapidAPI-Key": os.getenv('RAPIDKEY'),
            "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
        print(response.status_code)
        data = response.json()
        local = {"Local": data['location']['name'], "Temperatura":data['current']['temp_c'], 
                "Condições":data['current']['condition']['text']}
        weather_forecast_json = json.dumps(local)
        return weather_forecast_json
    except Exception as e:
        logging.exception('%s', e)
        raise e