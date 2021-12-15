import csv, flask, mysql.connector
from flask_login import LoginManager, UserMixin
from flask import jsonify, request
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


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

# Adding records to existing tables:

@app.route("/addcontact", methods = ["POST"])
def add_contact():
    addcontact = request.get_json()
    firstname = addcontact["firstname"]
    surname = addcontact["surname"]
    phonenmbr = addcontact["phonenmbr"]
    email = addcontact["email"]
    city = addcontact["city"]
    street = addcontact["street"]
    housenmbr = addcontact["housenmbr"]
    postalcode = addcontact["postalcode"]
    try:
        dbcursor = ontimedb.cursor()
        sql_add_contact_query = """INSERT INTO contact (firstname, surname, phonenmbr, email, city, street, housenmbr, postalcode) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        dbcursor.execute(sql_add_contact_query, (firstname, surname, phonenmbr, email, city, street, housenmbr, postalcode))
        
        ontimedb.commit()
        return("Commit succesful")

    except mysql.connector.Error as error:
        print("Failed to add a contact to contact table: {}".format(error))

    finally:
        if ontimedb.is_connected():
            dbcursor.close()
            print("MySQL connection is closed")


@app.route("/addattendant", methods = ["POST"])
def add_attendant():
    addattendant = request.get_json()
    firstname = addattendant["firstname"]
    surname = addattendant["surname"]
    phonenmbr = addattendant["phonenmbr"]
    email = addattendant["email"]
    password = addattendant["password"]
    try:
        dbcursor = ontimedb.cursor()
        sql_add_attendant_query = """INSERT INTO attendant (firstname, surname, phonenmbr, email, password) 
                                VALUES (%s, %s, %s, %s, %s)"""
        dbcursor.execute(sql_add_attendant_query, (firstname, surname, phonenmbr, email, password))
        
        ontimedb.commit()
        return("Commit succesful")

    except mysql.connector.Error as error:
        print("Failed to add an attendant to attendant table: {}".format(error))

    finally:
        if ontimedb.is_connected():
            dbcursor.close()
            print("MySQL connection is closed")


# Requesting data from existing tables

@app.route("/getcontact", methods = ["POST"])
def get_contact_detail():
    getcontact = request.get_json()
    firstname = getcontact["firstname"]
    surname = getcontact["surname"]
    try:
        dbcursor = ontimedb.cursor()
        sql_people_query = """SELECT * FROM contact 
                                WHERE firstname = %s AND surname = %s"""
        dbcursor.execute(sql_people_query, (firstname, surname,))
        record = dbcursor.fetchall()
        return jsonify(record), 200

    except mysql.connector.Error as error:
        print("Failed to get a contact from contact table: {}".format(error))

    finally:
        if ontimedb.is_connected():
            dbcursor.close()
            print("MySQL connection is closed")


@app.route("/getattendant", methods = ["POST"])
def get_attendant_detail():
    getattendant = request.get_json()
    firstname = getattendant["firstname"]
    surname = getattendant["surname"]
    try:
        dbcursor = ontimedb.cursor()
        sql_people_query = """SELECT * FROM attendant 
                                WHERE firstname = %s AND surname = %s"""
        dbcursor.execute(sql_people_query, (firstname, surname,))
        record = dbcursor.fetchall()
        return jsonify(record), 200

    except mysql.connector.Error as error:
        print("Failed to get an attendant from attendant table: {}".format(error))

    finally:
        if ontimedb.is_connected():
            dbcursor.close()
            print("MySQL connection is closed")


if __name__ == '__main__':
    app.run(debug = True)