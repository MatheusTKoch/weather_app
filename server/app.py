from flask import Flask, jsonify; 
import requests;
from flask_cors import CORS;
import os;
from dotenv import load_dotenv;


app = Flask(__name__)
app.config.from_object(__name__)
load_dotenv()
API_KEY = os.getenv('OPEN_WEATHER_KEY')
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/resultado', methods=['GET'])
def get_weather():
    city_name = requests.args.get('city')
    state_code = requests.args.get('state_code', '')
    country_code = requests.args.get('country_code', '')
    limit = requests.args.get('limit', 1)
    lang = requests.args.get('lang', 'pt_br')

    get_string = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={API_KEY}"
    getCall = requests.get(get_string)
    if getCall.ok:
        responseCall = getCall.json()
        cityName = responseCall[0]['name']
        latitude = responseCall[0]['lat']
        longitude = responseCall[0]['lon']

        forecast_string = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric&lang={lang}"
        forecastCall = requests.get(forecast_string)
        responseForecast = forecastCall.json()
        description = responseForecast['weather'][0]['description']
        minTemp = responseForecast['main']['temp_min']
        feelsLike = responseForecast['main']['feels_like']
        
        return jsonify({
            "name": cityName,
            "latitude": latitude,
            "longitude": longitude,
            "min_temp": minTemp,
            "feels_like": feelsLike,
            "description": description
        })
    else:
        return jsonify({"error": "Unable to fetch data from the API"}), 400

if __name__ == '__app__':
    app.run()