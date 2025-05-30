from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from bson.json_util import dumps
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Connect to MongoDB using MONGO_URI from .env
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client['interior_design_db']
designers_collection = db['designers']

# Dummy data with rating field
designers_data = [
    {
        "id": "1",
        "name": "Epic Designs",
        "description": "Passionate team of 4 designers working out of Bangalore with an experience of 4 years.",
        "projects": 57,
        "years": 8,
        "price": "$$",
        "phone1": "+91-984532853",
        "phone2": "+91-984532854",
        "shortlisted": False,
        "rating": 3.5
    },
    {
        "id": "2",
        "name": "Studio - D3",
        "description": "Passionate team of 4 designers working out of Bangalore with an experience of 4 years.",
        "projects": 43,
        "years": 6,
        "price": "$$$",
        "phone1": "+91-984532853",
        "phone2": "+91-984532854",
        "shortlisted": False,
        "rating": 3.8
    },
    {
        "id": "3",
        "name": "Creative Spaces",
        "description": "Innovative designs for modern living, specializing in minimalist aesthetics.",
        "projects": 30,
        "years": 5,
        "price": "$",
        "phone1": "+91-987654321",
        "phone2": "+91-987654322",
        "shortlisted": False,
        "rating": 5.0
    },
    {
        "id": "4",
        "name": "Urban Interiors",
        "description": "Transforming urban dwellings into functional and beautiful homes.",
        "projects": 65,
        "years": 10,
        "price": "$$$",
        "phone1": "+91-998877665",
        "phone2": "+91-998877666",
        "shortlisted": False,
        "rating": 4.2
    },
]

# Insert dummy data only if collection is empty
if designers_collection.count_documents({}) == 0:
    designers_collection.insert_many(designers_data)
    print("Initial designer data inserted.")

@app.route('/api/designers', methods=['GET'])
def get_designers():
    """
    Retrieve all interior designers.
    """
    designers_cursor = designers_collection.find()
    designers_list = list(designers_cursor)
    return dumps(designers_list), 200, {'Content-Type': 'application/json'}

@app.route('/')
def home():
    """
    Health check endpoint.
    """
    return "EmptyCup Backend API is running!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)