# server.py
from flask import Flask, request

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return "pong", 200

@app.route('/data', methods=['POST'])
def data():
    content = request.get_json()
    return {"received": content}, 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)