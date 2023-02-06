from flask import Flask
from .controllers import main_controller

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return main_controller.index()