from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def create_table():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS PARTICIPANTS (
                            name TEXT,
                            email TEXT UNIQUE,
                            city TEXT,
                            country TEXT,
                            phone TEXT)""")

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Головна сторінка
@app.route("/")
@app.route("/home")
def index():
    create_table() # Використовуємо один раз!
    return render_template('index.html')

# Форма для додавання нового учасника
@app.route("/join", methods=["GET", "POST"])
def join():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        city = request.form["city"]
        country = request.form["country"]
        phone = request.form["phone"]

        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO PARTICIPANTS (name, email, city, country, phone) VALUES (?, ?, ?, ?, ?)",
                       (name, email, city, country, phone))
        db.commit()

        return render_template("join.html")
    else:
        return render_template("join.html")

# Відображення списку учасників
@app.route("/participants")
def participants():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM PARTICIPANTS")
    data = cursor.fetchall()
    return render_template("participants.html", data=data)

if __name__ == "__main__":
    app.run(debug=True, port=8000)