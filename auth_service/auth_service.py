from flask import Flask, request, jsonify

app = Flask(__name__)


 # типа БД
users = {
    "user1": "password1",
    "user2": "password2"
}

@app.route('/auth', methods=['POST'])
def auth():
     # получаем данные
    data = request.json
    login = data.get('login')
    password = data.get('password')
    
     # если нету логина или пароля - запрещаем и сообщаем
    if not login or not password:
        return jsonify({"error": "Login and password required"}), 400

 # если есть логин и пароль - проверяем и возварщаем ответ 
    is_authenticated = users.get(login) == password
    return jsonify({"auth": is_authenticated})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002)
