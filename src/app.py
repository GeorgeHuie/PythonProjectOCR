from flask import Flask, render_template, request, g
import sqlite3
import os

#initialize the flask app
app = Flask(__name__)

#define the sqlite data base (patient database)
DATABASE = os.path.join(os.path.dirname(__file__), r"C:\Users\huieg\PycharmProjects\PythonProject\patients.db")

#get the database connection and store in the flask app context 'g'
def get_db():
    #create a database if not existed
    if 'db' not in g:
        #connect to the patient database
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


#automatically close the database connection after the request
@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()

#route to home page where you search for patient info with their name
@app.route('/')
def home():
    return render_template("index.html")

#route for handling search queries via Get request
@app.route("/search", methods=["GET"])
def search():
    #get the search query from URL parameter
    query = request.args.get("q", "")
    #database connection
    db = get_db()
    #execute sql query as search concept
    #find patient in database with the name like input
    cur = db.execute("SELECT * FROM patient WHERE name LIKE ?",
                     (f"%{query}%",))
    #fetch all matching rows
    results = cur.fetchall()
    #render the result html template with the search result
    return render_template("results.html", results=results)

#run app
if __name__ == "__main__":
    app.run(debug=True)
