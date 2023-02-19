from flask import Flask, g
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return "Index view для обработки посещений на корень сайта"

