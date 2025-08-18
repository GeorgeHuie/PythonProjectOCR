from flask import Flask, render_template, request, g
import sqlite3
import os

app = Flask(__name__)

DATABASE = os.path.join(os.path.dirname(__file__), r"C:\Users\huieg\PycharmProjects\PythonProject\patients.db")

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", "")
    db = get_db()
    cur = db.execute("SELECT * FROM patient WHERE name LIKE ?",
                     (f"%{query}%",))
    results = cur.fetchall()
    return render_template("results.html", results=results)


if __name__ == "__main__":
    app.run(debug=True)
