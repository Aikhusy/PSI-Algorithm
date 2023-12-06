from flask import Flask, request, render_template, redirect, url_for,  jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/process_input', methods=['POST'])
def process_input():
    data = request.get_json()
    input_array = data.get('inputArray', [])
    
    # Kirim data ke halaman lain
    return render_template('result.html', input_data=input_array)

if __name__ == '__main__':
    app.run(debug=True)