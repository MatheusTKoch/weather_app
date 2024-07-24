from flask import Flask, jsonify, request; 
import requests;
from flask_cors import CORS;
import os;
from dotenv import load_dotenv;


app = Flask(__name__)
app.config.from_object(__name__)
load_dotenv()
API_KEY = os.getenv('OPEN_WEATHER_KEY')
CORS(app)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/resultado', methods=['GET'])
def get_weather():
    city_name = request.args.get('city')
    state_code = request.args.get('state_code', '')
    country_code = request.args.get('country_code', '')
    limit = request.args.get('limit', 1)
    lang = request.args.get('lang', 'pt_br')

    get_string = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={API_KEY}"
    getCall = request.get(get_string)
    if getCall.ok:
        responseCall = getCall.json()
        cityName = responseCall[0]['name']
        latitude = responseCall[0]['lat']
        longitude = responseCall[0]['lon']

        forecast_string = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units=metric&lang={lang}"
        forecastCall = request.get(forecast_string)
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

if __name__ == '__main__':
    app.run(port=5000, debug=True)