from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# Получаем URL второго сервиса из переменных окружения
SERVICE2_URL = os.getenv('SERVICE2_URL', 'http://localhost:5001')

@app.route('/')
def hello():
    return jsonify({
        "service": "Service 1",
        "message": "Hello from Service 1!",
        "status": "running"
    })

@app.route('/data')
def get_data():
    return jsonify({
        "service": "Service 1",
        "data": ["item1", "item2", "item3"],
        "count": 3
    })

@app.route('/communicate')
def communicate():
    try:
        # Вызов второго сервиса
        response = requests.get(f"{SERVICE2_URL}/info", timeout=5)
        service2_data = response.json()
        
        return jsonify({
            "service": "Service 1",
            "message": "Communication successful",
            "service2_response": service2_data
        })
    except requests.exceptions.RequestException as e:
        return jsonify({
            "service": "Service 1",
            "error": f"Failed to communicate with Service 2: {str(e)}"
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)