import mysql.connector
import flask
from flask import jsonify,request
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


@app.route("/addpeoplev1", methods = ["POST"])
def add_people_v1_detail():
    people = request.get_json()
    firstname = people["firstname"]
    surname = people["surname"]
    phone = people["phone"]
    mail = people["mail"]
    city = people["city"]
    street = people["street"]
    housenumber = people["housenumber"]
    postalcode = people["postalcode"]
    
    ontimedb = mysql.connector.connect(
        host="145.89.192.95",
        database="ontime",
        user="dbuser",
        password="Dbuser123!")

    dbcursor = ontimedb.cursor()
    dbcursor.execute("INSERT INTO people (firstname, surname, phone, mail, city, street, housenumber, postalcode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (firstname, surname, phone, mail, city, street, housenumber, postalcode))

    print(firstname)

    ontimedb.commit()
    dbcursor.close()
    return "commit succesful"


@app.route("/addpeoplev2", methods = ["POST"])
def add_people_v2_detail():
    peoplename = request.get_json()
    personname = peoplename["name"]
    try:
        ontimedb = mysql.connector.connect(
            host="145.89.192.95",
            database="ontime",
            user="dbuser",
            password="Dbuser123!")

        dbcursor = ontimedb.cursor()
        sql_add_people_query = """INSERT INTO test (name)
                                VALUES = (%s)"""
        dbcursor.execute(sql_add_people_query, (personname,))
        
        print(personname)
        ontimedb.commit()
        return("commit succesful")

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if ontimedb.is_connected():
            dbcursor.close()
            print("MySQL connection is closed")


@app.route("/getpeople", methods = ["POST"])
def get_people_detail():
    getpeople = request.get_json()
    person = getpeople["id"]
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