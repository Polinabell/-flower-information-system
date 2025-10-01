from flask import Flask, jsonify
import os
import datetime

app = Flask(__name__)

# Получаем URL первого сервиса из переменных окружения
SERVICE1_URL = os.getenv('SERVICE1_URL', 'http://localhost:5000')

@app.route('/')
def hello():
    return jsonify({
        "service": "Service 2",
        "message": "Hello from Service 2!",
        "status": "running"
    })

@app.route('/info')
def info():
    return jsonify({
        "service": "Service 2",
        "timestamp": datetime.datetime.now().isoformat(),
        "version": "1.0.0",
        "features": ["data processing", "analytics", "reporting"]
    })

@app.route('/process')
def process_data():
    return jsonify({
        "service": "Service 2",
        "action": "data_processing",
        "result": "data_processed_successfully",
        "processed_items": 42
    })

@app.route('/call-service1')
def call_service1():
    try:
        # Вызов первого сервиса
        import requests
        response = requests.get(f"{SERVICE1_URL}/data", timeout=5)
        service1_data = response.json()
        
        return jsonify({
            "service": "Service 2",
            "message": "Called Service 1 successfully",
            "service1_response": service1_data
        })
    except Exception as e:
        return jsonify({
            "service": "Service 2",
            "error": f"Failed to communicate with Service 1: {str(e)}"
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)