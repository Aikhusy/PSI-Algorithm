from flask import Flask, request, render_template, jsonify, url_for
from PSI.Controller import main
from PSI.Controller import main2
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/process_array', methods=['POST'])
def process_array():
    data = request.json
    mergedData= data.get('array')  # Ambil data JSON dari permintaan

    # Panggil fungsi Python untuk memproses array
    result = main(mergedData)

    # Return the result as JSON
    return jsonify(result)

@app.route('/SAW', methods=['POST'])
def process_array2():
    data = request.json
    # Ambil data JSON dari permintaan
    mergedData= data.get('array') 
    # Panggil fungsi Python untuk memproses array
    result = main2()

    # Return the result as JSON
    return jsonify(result)

@app.route('/teori')
def teori():
    return render_template('teori.html')

@app.route('/contributor')
def contributor():
    return render_template('contributor.html')

if __name__ == '__main__':
    app.run(debug=True)

