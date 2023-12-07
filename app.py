from flask import Flask, request, render_template, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/process_array', methods=['POST'])
def process_array():
    data = request.json  # Ambil data JSON dari permintaan

    # Panggil fungsi Python untuk memproses array
    result = process_python_function(data['array'])

    # Return the result as JSON
    return jsonify(result=result)

def convert_2d_array_to_integer(input_2d_array):
    try:
        result_array = [[int(item) for item in inner_array] for inner_array in input_2d_array]
        return result_array
    except ValueError:
        print("Error: Unable to convert the entire 2D array to integers.")
        return None

def process_python_function(input_array):
    result_array = []
    converted= convert_2d_array_to_integer(input_array)

    for inner_array in converted:
        processed_inner_array = []

        for item in inner_array:
            # Multiply each element inside the 2D array by 2
            processed_item = item * 2

            # Check the data type of the processed item
            data_type = type(processed_item)

            # Append the processed item and its data type to the result
            processed_inner_array.append(processed_item)

        result_array.append(processed_inner_array)

    return result_array

if __name__ == '__main__':
    app.run(debug=True)
