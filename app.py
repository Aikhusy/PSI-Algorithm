from flask import Flask, request, render_template, redirect, url_for,  jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/process_data', methods=['POST'])

def process_data():
    data_from_js = request.json['data']
    
    # Call the countArray function with the received data
    result = countArray(data_from_js)
    
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)