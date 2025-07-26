import sqlite3
from flask import Flask, render_template, flash, url_for, redirect, request

app = Flask(__name__)
app.secret_key = "super_secret"

def connect_to_db():
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn

def create_users_table():
    conn = connect_to_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            time TEXT NOT NULL
        );
    ''')
    conn.commit()
    conn.close()

def get_users():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    conn.close()
    return users
    
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register/')
def register():
    return render_template("register.html")

@app.route('/participants/')
def participants():
    users = get_users()
    return render_template("participants.html", users=users)

@app.route('/add_user/', methods=["POST"])
def add_user():
    username = request.form.get("username")
    email = request.form.get("email")
    time = request.form.get("time")
    
    if not username or not email or not time:
        flash("Please, fill in all fields!", "danger")
        return redirect(url_for("register"))
    
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, email, time) VALUES (?, ?, ?)", (username, email, time))
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        flash("Username or E-Mail already exists!", "danger")
        return redirect(url_for("register"))
    except Exception as e:
        flash(f"Something went wrong: {e}", "danger")
        return redirect(url_for("register"))
    
    flash("Successfuly added new user to the event.", "success")
    return redirect(url_for("register"))
        
        
if __name__ == "__main__":
    create_users_table()
    app.run(debug=True)
