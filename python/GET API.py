from flask_cors import CORS
import flask
import csv
from flask import jsonify
import mysql.connector
from mysql.connector import errorcode

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

#De inloggegevens van de database staan in een apart document in de volgende vorm: 'user','password','host','naam van de database'

with open(r"C:\Users\caspe\OneDrive\Documents\GitHub\Project-Ontime\txt\mysql.txt") as f1:
        data=csv.reader(f1,delimiter=",")
        for row in data:
            user=row[0]
            password=row[1]
            host=row[2]
            database=row[3]


try:
    ontimedb = mysql.connector.connect(
            host=host,
            database=database,
            user=user,
            password=password)
except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with username or password")
    elif e.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(e)


def ontimedb():
    return mysql.connector.connect(
        user=user,
        password=password,
        host=host,
        database=database)


@ app.route("/client", methods = ["GET"])
def get_table_detail():
    connection = ontimedb()
    cursor = connection.cursor()
    cursor.execute("""SELECT *
    FROM client""")
    
    results = cursor.fetchall()
    return jsonify(results), 200


if __name__ == "__main__":
    app.run(debug=True)