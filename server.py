from flask import Flask, request, jsonify
from dataclasses import dataclass
@dataclass
class result:
    res: int


app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data=request.json 
    sum=result(data['first']+data['second'])
    return jsonify(sum)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data=request.json 
    sum=result(data['first']-data['second'])
    return jsonify(sum)


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
