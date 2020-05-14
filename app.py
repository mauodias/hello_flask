from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Hello, World!"