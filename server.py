from flask import Flask, request, jsonify
from dataclasses import dataclass
@dataclass
class res:
    result: int


app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data=request.json 
    response=res(data['first']+data['second'])
    return jsonify(response)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data=request.json 
    response=res(data['first']-data['second'])
    return jsonify(response)


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
