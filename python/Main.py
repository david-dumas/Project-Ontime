import csv, flask, mysql.connector, jwt, datetime
from flask_login import LoginManager, UserMixin
from flask_cors import CORS
from flask import request, jsonify, session
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
CORS(app, supports_credentials=True)
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
    lastname = addcontact["lastname"]
    phonenmbr = addcontact["phonenmbr"]
    email = addcontact["email"]
    city = addcontact["city"]
    street = addcontact["street"]
    housenmbr = addcontact["housenmbr"]
    postalcode = addcontact["postalcode"]
    try:
        dbcursor = ontimedb.cursor()
        sql_add_contact_query = """INSERT INTO contact (firstname, lastname, phonenmbr, email, city, street, housenmbr, postalcode) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        dbcursor.execute(sql_add_contact_query, (firstname, lastname, phonenmbr, email, city, street, housenmbr, postalcode))
        
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
    lastname = addattendant["lastname"]
    phonenmbr = addattendant["phonenmbr"]
    email = addattendant["email"]
    password = addattendant["password"]
    try:
        dbcursor = ontimedb.cursor()
        sql_add_attendant_query = """INSERT INTO attendant (firstname, lastname, phonenmbr, email, password) 
                                VALUES (%s, %s, %s, %s, %s)"""
        dbcursor.execute(sql_add_attendant_query, (firstname, lastname, phonenmbr, email, password))
        
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
    lastname = getcontact["lastname"]
    try:
        dbcursor = ontimedb.cursor()
        sql_people_query = """SELECT * FROM contact 
                                WHERE firstname = %s AND lastname = %s"""
        dbcursor.execute(sql_people_query, (firstname, lastname,))
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
    lastname = getattendant["lastname"]
    try:
        dbcursor = ontimedb.cursor()
        sql_people_query = """SELECT * FROM attendant 
                                WHERE firstname = %s AND lastname = %s"""
        dbcursor.execute(sql_people_query, (firstname, lastname,))
        record = dbcursor.fetchall()
        return jsonify(record), 200

    except mysql.connector.Error as error:
        print("Failed to get an attendant from attendant table: {}".format(error))

    finally:
        if ontimedb.is_connected():
            dbcursor.close()
            print("MySQL connection is closed")


# # Login

# app.config["SECRET_KEY"] = "thisissecret"
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://dbuser:Dbuser123!@145.89.192.95/ontime"
# db = SQLAlchemy(app)


# login_manager = LoginManager()
# login_manager.init_app(app)

# # Attendant table
# class attendant(UserMixin, db.Model):
# 	id = db.Column(db.Integer, primary_key=True) 
# 	firstname = db.Column(db.String(50))
# 	lastname	= db.Column(db.String(50))
# 	phonenmbr = db.Column(db.String(50))
# 	email = db.Column(db.String(50), unique=True)
# 	password = db.Column(db.String(50))


# @login_manager.user_loader
# def load_user(user_id):
#     return attendant.query.get(int(user_id))

# # Login authentication
# @app.route("/login_request", methods = ["POST"])
# def login_request():
#     data = request.get_json()
#     email = data["email"]
#     password = data["password"]

#     # Database query om de gebruiker op te halen
#     user = attendant.query.filter_by(email=email).first()

#     # Wachtwoord controle
#     if user.password == password:
#         session["active"] = True
#         session.modified = True
#         response = ("it works")
#         response = jsonify(val=True)
#     if not user:
#         response = jsonify(val=False)

#     response.headers.add("Access-Control-Allow-Headers",
#                             "Origin, X-Requested-With, Content-Type, Accept, x-auth")

#     payload = {
#         "id": user.id,
#         "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#         "iat": datetime.datetime.utcnow()
#     }

#     # Meegeven JWT token
#     token = jwt.encode(payload, "secret", algorithm="HS256")
    
#     tokenresponse = {
#         "token" : token.decode()
#     }

#     return jsonify({"val" : True}, tokenresponse)

if __name__ == '__main__':
    app.run(debug = True)