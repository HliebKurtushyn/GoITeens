from flask import Flask, jsonify
import logging


app = Flask(__name__)


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@app.route('/error', methods=['GET'])
def error():
    logging.error('Something went wrong')
    return jsonify({"error": "Something went wrong"}), 500

if __name__ == '__main__':
    app.run(debug=True)