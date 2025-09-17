from flask import Flask, request, jsonify
import unittest

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json({'username': 'admin', 'password': 'secret'})
        if data.get("username") == "admin" and data.get("password") == "secret":
            return jsonify({"message": "Login successful"}), 200
        return jsonify({"message": "Invalid credentials"}), 401

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_login_okay(self):
        response = self.app.post('/login', json={'username': 'admin', 'password': 'secret'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Login successful"})
    
    def test_login_bad(self):
        response = self.app.post('/login', json={'username': 'not_admin', 'password': 'not_secret'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {"message": "Invalid credentials"})

if __name__ == '__main__':
    unittest.main()