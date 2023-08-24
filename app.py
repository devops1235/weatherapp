from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'your_weather_api_key'

@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter missing'}), 400

    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(weather_url)
    data = response.json()

    weather_info = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'weather': data['weather'][0]['description']
    }
    return jsonify(weather_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
