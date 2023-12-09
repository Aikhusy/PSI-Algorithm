from flask import Flask, request, render_template, jsonify
from PSI.Controller import main
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/process_array', methods=['POST'])
def process_array():
    data = request.json  # Ambil data JSON dari permintaan

    # Panggil fungsi Python untuk memproses array
    result = main(data)

    # Return the result as JSON
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
