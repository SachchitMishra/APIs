'''
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')  # Connect to MongoDB
db = client['CRUDS']  # Replace 'your_database_name' with your database name
collection = db['data']  # Replace 'your_collection_name' with your collection name
# Endpoint to add a new item
@app.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    # Assuming data contains fields you want to store in your MongoDB collection
    inserted_item = collection.insert_one(data)
    return jsonify({'message': 'Item added successfully', 'inserted_id': str(inserted_item.inserted_id)}), 201
@app.route('/items', methods=['GET'])
def get_all_items():
    items = list(collection.find())
    return jsonify({'items': items}), 200

# Endpoint to get a specific item by ID
@app.route('/items/<string:item_id>', methods=['GET'])
def get_item(item_id):
    item = collection.find_one({'_id': ObjectId(item_id)})
    if item:
        return jsonify(item), 200
    else:
        return jsonify({'message': 'Item not found'}), 404

# Endpoint to update an existing item
@app.route('/items/<string:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    updated_item = collection.update_one({'_id': ObjectId(item_id)}, {'$set': data})
    if updated_item.modified_count:
        return jsonify({'message': 'Item updated successfully'}), 200
 
if __name__ == '__main__':
    app.run(debug=True)
#### WORKING ####    
'''
'''
from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["CRUDS"]
collection = db["data"]

@app.route('/items', methods=["POST"])
def post():
    pass
@app.route('/items', methods=["GET"])
def get():
    items = list(collection.find())
    
if __name__ == "__main__":
    app.run(debug=True)
'''




'''
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['CRUDS']
collection = db['data']

@app.route('/GET', methods=["GET"])
def get():
    items = list(collection.find())
    return jsonify({'data':items})
@app.route('/POST', methods=['POST'])
def post():
    data=request.get_json
    inserted_item=collection.insert_one(data)
    return jsonify({'message':'Done!'})
    
if __name__ ==' __main__':
    app.run(debug=True)
'''