from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "simple_secret_key"

def get_db():
    return sqlite3.connect("database.db")

# Create tables
with get_db() as db:
    db.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)
    db.execute("""
    CREATE TABLE IF NOT EXISTS items(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        user_id INTEGER
    )
    """)

@app.route("/")
def home():
    return redirect("/login")

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        try:
            with get_db() as db:
                db.execute("INSERT INTO users(username,password) VALUES (?,?)",
                           (username,password))
            return redirect("/login")
        except:
            return "User already exists"
    return render_template("signup.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        db = get_db()
        user = db.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username,password)
        ).fetchone()
        if user:
            session["user_id"] = user[0]
            return redirect("/dashboard")
        return "Invalid credentials"
    return render_template("login.html")

@app.route("/dashboard", methods=["GET","POST"])
def dashboard():
    if "user_id" not in session:
        return redirect("/login")

    db = get_db()

    if request.method == "POST":
        title = request.form["title"]
        db.execute("INSERT INTO items(title,user_id) VALUES (?,?)",
                   (title, session["user_id"]))
        db.commit()

    items = db.execute(
        "SELECT * FROM items WHERE user_id=?",
        (session["user_id"],)
    ).fetchall()

    return render_template("dashboard.html", items=items)

@app.route("/delete/<int:id>")
def delete(id):
    db = get_db()
    db.execute("DELETE FROM items WHERE id=?", (id,))
    db.commit()
    return redirect("/dashboard")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
