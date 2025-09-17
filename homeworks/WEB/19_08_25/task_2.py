from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


@app.route('/user', methods=['POST'])
def user():
    data = request.get_json()
    if "username" not in data:
        logging.warning("Username is required!")
        return jsonify({"error": "Username is required"}), 400
    
    logging.info(f"Hello, {data['username']}!")
    return jsonify({"message": f"Hello, {data['username']}!"}), 200


if __name__ == '__main__':
    app.run(debug=True)