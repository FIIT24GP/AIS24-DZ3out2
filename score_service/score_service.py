from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/score', methods=['POST'])
def score():
    # получаем данные
    data = request.json
    login = data.get('login')
    
     # если логин пустой
    if not login:
        return jsonify({"error": "Login required"}), 400

    # проверяем на Хорошесть
    score_value = random.uniform(0, 1)  # Случайное число от 0 до 1
    
    # отдаем результат обратно 
    return jsonify({"score": score_value})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
