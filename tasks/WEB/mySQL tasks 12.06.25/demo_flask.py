from flask import Flask

app = Flask(__name__)

@app.route("/")
def first_page():
    return "Welcome to My Website!"

@app.route("/second_page")
def second_page():
    return "This website is built using the Flask framework."

if __name__ == '__main__':
    app.run(debug=True, port = 8000)
