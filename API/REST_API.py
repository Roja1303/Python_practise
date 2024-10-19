from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data
items = [{"id": 1, "name": "Item1"}, {"id": 2, "name": "Item2"}]

# GET: Retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# GET: Retrieve a specific item by ID
@app.route('/items/<int:id>', methods=['GET'])  # Corrected to 'GET'
def get_item(id):
    item = next((item for item in items if item["id"] == id), None)
    return jsonify(item) if item else ("Not found", 404)

# POST: Create a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.json
    new_item["id"] = len(items) + 1
    items.append(new_item)
    return jsonify(new_item), 201

# PUT: Update an existing item
@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    item = next((item for item in items if item["id"] == id), None)
    if item:
        data = request.json
        item.update(data)
        return jsonify(item)
    return "Item not found", 404

# DELETE: Delete an item
@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    global items
    items = [item for item in items if item["id"] != id]
    return "Item deleted", 204

if __name__ == '__main__':
    app.run(debug=True)
