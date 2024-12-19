import os
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


 # читаем переменную из .env
 #SCORE_THRESHOLD = os.getenv("SCORE_THRESHOLD") НЕправильно, прочиталось как строка
SCORE_THRESHOLD = float(os.getenv("SCORE_THRESHOLD"))  # Преобразуем в число

 # если в .env не нашли - даем ошибку
if SCORE_THRESHOLD is None:
    raise ValueError("SCORE_THRESHOLD not found in environment variables!")

@app.route('/composition', methods=['POST'])
def composition():
     # полуучаем данные
    data = request.json
    login = data.get('login')
    password = data.get('password')
    
     # если логин или пароль вдруг пустые - не пускаем и сообщаем
    if not login or not password:
        return jsonify({"error": "Login and password required"}), 400

    # обращаемся к score сервису
    try:
        # score_response = requests.post('http://localhost:5001/score', json={"login": login})
        score_response = requests.post('http://score_service:5001/score', json={"login": login})
        score_response.raise_for_status()
        score_data = score_response.json()
        # если ошибка, считаем что score максимально хороший
        score_value = score_data.get("score", 1.0)  
    except requests.exceptions.RequestException:
        score_value = 1.0

    # если значение так себе - сообщаем и не пускаем
    if score_value < SCORE_THRESHOLD:
        return jsonify({"auth": False, "reason": "Low score"}), 403

    # обращаемся к auth сервису
    # auth_response = requests.post('http://localhost:5002/auth', json={"login": login, "password": password})
    auth_response = requests.post('http://auth_service:5002/auth', json={"login": login, "password": password})
    auth_data = auth_response.json()

    # отдаем ответ
    return jsonify({"auth": auth_data.get("auth", False)})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5003)
