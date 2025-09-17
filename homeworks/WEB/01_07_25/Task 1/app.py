from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1><b>Hello, World!</b></h1>'

@app.route('/about/')
def about():
    return '<h1><b>I am Gleb and I currently learning Python</b></h1>'

@app.route('/services/')
def services():
    return '<h1><b>I can do a small web app with no functionality</b></h1>'

@app.route('/contact/')
def contact():
    return '<h1><b>Do not contact me, please</b></h1>'

if __name__ == '__main__':
    app.run(debug=True)