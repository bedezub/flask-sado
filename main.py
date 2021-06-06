from flask import Flask, request, jsonify
from flask_cors import CORS
from experta import *

# Python 3
# from .engine import *

# Python 2 - MacOS !?!?!?!
from engine import *

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def hello():
    return "Hello world"

@app.route("/runEngine", methods=["POST"])
def runEngine():
    if request.method == 'POST':
        content = request.json
        print(content)
        result = forwardChaining(content)
        return result
        # return 'naisee'
        
def forwardChaining(content):
    sado = SADO()
    sado.reset()
    sado.declare(Age(content["age"]), Height(content["height"]), Weight(content["weight"]), Gender(content["gender"]), Competing(content["participate"]), Intensity(content["intensity"]))
    sado.run()
    result = jsonify(title=sado.title, foods=sado.foods, recommendation=sado.recommendation)
    return result

@app.route("/runEngineStub", methods=["GET"])
def runEngineStub():
    if request.method == 'GET':
        # content = request.json
        result = forwardChainingStub()
        return result
        
def forwardChainingStub():
    sado = SADO()
    sado.reset()
    sado.declare(Age('21'), Height('168'), Weight('55'), Gender('male'), Competing('y'), Intensity('low'))
    sado.run()
    result = jsonify(title=sado.title, foods=sado.foods, recommendation=sado.recommendation)
    return result



