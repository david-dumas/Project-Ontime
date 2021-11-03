from flask_cors import CORS
import flask
from flask import jsonify
import mysql.connector

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


def ontimedb():
    return mysql.connector.connect(
            host="localhost",
            database="ontime",
            user="root",
            password="")


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