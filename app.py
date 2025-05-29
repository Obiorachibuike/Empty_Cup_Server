from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS for all routes, allowing the frontend to make requests from a different origin.
CORS(app)

# Dummy data for interior designers. In a real application, this would come from a database.
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
    },
    {
        "id": "3",
        "name: "Creative Spaces",
        "description": "Innovative designs for modern living, specializing in minimalist aesthetics.",
        "projects": 30,
        "years": 5,
        "price": "$",
        "phone1": "+91-987654321",
        "phone2": "+91-987654322",
        "shortlisted": False,
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
    },
]

@app.route('/api/designers', methods=['GET'])
def get_designers():
    """
    API endpoint to retrieve a list of interior designers.
    Returns the designers_data as a JSON array.
    """
    return jsonify(designers_data)

@app.route('/')
def home():
    """
    Basic home route for the API, just to confirm it's running.
    """
    return "EmptyCup Backend API is running!"

if __name__ == '__main__':
    # Run the Flask app.
    # In a production environment, you would use a production-ready WSGI server like Gunicorn.
    # debug=True allows for automatic reloading on code changes and provides a debugger.
    app.run(debug=True, host='0.0.0.0', port=5000)
