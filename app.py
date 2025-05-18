import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# Получить список всех элементов
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items=[{"id": 1, "name": "Stub Item"}]), 200

# Создать новый элемент
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    return jsonify(message="Item created", item=data), 201

# Получить элемент по ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    return jsonify(item={"id": item_id, "name": f"Stub Item {item_id}"}), 200

# Полностью обновить элемент по ID
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    return jsonify(message=f"Item {item_id} fully updated", item=data), 200

# Частично обновить элемент по ID
@app.route('/items/<int:item_id>', methods=['PATCH'])
def patch_item(item_id):
    data = request.get_json()
    return jsonify(message=f"Item {item_id} partially updated", updates=data), 200

# Удалить элемент по ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    return jsonify(message=f"Item {item_id} deleted"), 204

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
