import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    # Получаем порт из переменной окружения, иначе используем 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
