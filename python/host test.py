import mysql.connector
import flask
from flask import jsonify,request
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

@app.route("/people", methods = ["POST"])
def get_people_detail():
    people = request.get_json(force=True)
    person = people["id"]
    try:
        ontimedb = mysql.connector.connect(
            host="145.89.192.95",
            database="ontime",
            user="dbuser",
            password="Dbuser123!")

        dbcursor = ontimedb.cursor()
        sql_people_query = """SELECT * FROM people 
                                WHERE id = %s"""
        dbcursor.execute(sql_people_query, (person,))
        record = dbcursor.fetchall()
        return jsonify(record), 200

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if ontimedb.is_connected():
            dbcursor.close()
            print("MySQL connection is closed")

if __name__ == '__main__':
    app.run(debug=True)