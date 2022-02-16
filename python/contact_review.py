import csv, flask, mysql.connector
from flask_cors import CORS
from flask import request, jsonify


app = flask.Flask(__name__)
CORS(app, supports_credentials=True)
app.config["DEBUG"] = True


# Connection to a MySQL database with has the login stored in another document
with open(r"./mysql.txt") as f1:
    data=csv.reader(f1,delimiter=",")
    for row in data:
            host=row[0]
            database=row[1]
            user=row[2]
            password=row[3]


ontimedb = mysql.connector.connect(
    host=host,
    database=database,
    user=user,
    password=password)


# A request which lets you collect all the data from a single contact selected by entering the appropriate firstname and lastname
@app.route("/contact", methods = ["POST"])
def get_contact_detail():
    getcontact = request.get_json()
    firstname = getcontact["firstname"]
    lastname = getcontact["lastname"]

    ontimecursor = ontimedb.cursor()
    sql_people_query = """SELECT * FROM contact 
                            WHERE firstname = %s AND lastname = %s"""
    ontimecursor.execute(sql_people_query, (firstname, lastname,))
    record = ontimecursor.fetchall()
    ontimecursor.close()
    print("MySQL connection is closed")
    return jsonify(record), 200


if __name__ == "__main__":
    app.run(debug = True)