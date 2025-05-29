from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Empty Cup Server Proof of Concept!"})

if __name__ == '__main__':
    app.run(debug=True)
