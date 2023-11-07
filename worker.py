import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
querydict = [{"q":"-27.5858, -48.542"},
             {"q":"-9.973, -67.80"},
             {"q":"-33.69, -53.45"},
             {"q":"-3.0558, -60.0883"},
             {"q":"48.825, 2.325"},
             {"q":"38.752, -9.039"},
             {"q":"-41.2112, 174.829"}]

RAPIDKEY = os.getenv('RAPIDKEY')

def get_weather(querystring:str):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    headers = {
        "X-RapidAPI-Key": RAPIDKEY,
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    local = {"Local": data['location']['name'], "Temperatura":data['current']['temp_c'], 
             "Condições":data['current']['condition']['text']}
    weather_forecast_json = json.dumps(local)
    return weather_forecast_json