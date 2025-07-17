from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='../static')
CORS(app)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_file(path):
    return send_from_directory(app.static_folder, path)

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    print("Contact form data received:", data)
    return jsonify({"message": "Form submitted successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
