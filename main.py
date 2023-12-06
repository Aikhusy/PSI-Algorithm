from flask import Flask, request, render_template, redirect, url_for, send_file, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "HELLOW WORLD"

if __name__ == '__main__':
    app.run(debug=True)