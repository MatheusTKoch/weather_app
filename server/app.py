from flask import Flask, jsonify; 
import requests;
from flask_cors import CORS;
import os;
from dotenv import load_dotenv;


app = Flask(__name__)
app.config.from_object(__name__)
load_dotenv();
API_KEY = os.getenv('OPEN_WEATHER_KEY');
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__app__':
    app.run()