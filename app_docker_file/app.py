# app.py
from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__, template_folder='.')

data_store = []

@app.route('/', methods=['GET'])
def home():
    return render_template('frontend.html')

@app.route('/data', methods=['GET', 'POST'])
def manage_data():
    if request.method == 'GET':
        return jsonify(data_store)
    elif request.method == 'POST':
        new_data = request.get_json()
        data_store.append(new_data)
        return jsonify(new_data), 201

if __name__ == '__main__':
    # Set the port to 5000
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
