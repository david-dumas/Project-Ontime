import csv
import datetime
import flask
import jwt
import mysql.connector
from flask_login import LoginManager, UserMixin
from flask import jsonify, request
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True


with open(r"C:\Users\caspe\OneDrive\Documents\GitHub\Project-Ontime\txt\mysql.txt") as f1:
    data=csv.reader(f1,delimiter=",")
    for row in data:
            host=row[0]
            database=row[1]
            user=row[2]
            password=row[3]

ontimedb = mysql.connector.connect(
    host="145.89.192.95",
    database="ontime",
    user="dbuser",
    password="Dbuser123!")


#David

# @login_manager.user_loader
# def load_user(user_id):
# 	return staff.query.get(int(user_id))

#LOGIN AUTHENTICATION
# @app.route("/login_request", methods = ["POST"])
# def login_request():
# 	data = request.get_json()
# 	email = data["email"]
# 	password = data["password"]

# 	# Database query om de gebruiker op te halen
# 	user = staff.query.filter_by(email=email).first()

# 	# Wachtwoord controle
# 	if user.password == password:
# 		session['active'] = True
# 		session.modified = True
# 		response = jsonify(val=True)
# 	if not user:
# 		response = jsonify(val=False)

# 	response.headers.add('Access-Control-Allow-Headers',
# 							"Origin, X-Requested-With, Content-Type, Accept, x-auth")

# 	payload = {
# 		'id': user.id,
# 		'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
# 		'iat': datetime.datetime.utcnow()
# 	}

# 	# Meegeven JWT token
# 	token = jwt.encode(payload, 'secret', algorithm='HS256')

# 	response.token = token

# 	return jsonify({'val': True, 'token': token})

# Niet meer David


@app.route("/addcontact", methods = ["POST"])
def add_contact():
    contact = request.get_json()
    firstname = contact["firstname"]
    surname = contact["surname"]
    phone = contact["phone"]
    mail = contact["mail"]
    city = contact["city"]
    street = contact["street"]
    housenumber = contact["housenumber"]
    postalcode = contact["postalcode"]
    try:
        dbcursor = ontimedb.cursor()
        sql_add_contact_query = """INSERT INTO contact (firstname, surname, phone, mail, city, street, housenumber, postalcode) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        dbcursor.execute(sql_add_contact_query, (firstname, surname, phone, mail, city, street, housenumber, postalcode))
        
        ontimedb.commit()
        return("commit succesful")

    except mysql.connector.Error as error:
        print("Failed to commit record to MySQL table: {}".format(error))

    finally:
        if ontimedb.is_connected():
            dbcursor.close()
            print("MySQL connection is closed")


@app.route("/getcontact", methods = ["POST"])
def get_contact_detail():
    getcontact = request.get_json()
    firstname = getcontact["firstname"]
    surname = getcontact["surname"]
    try:
        dbcursor = ontimedb.cursor()
        sql_people_query = """SELECT * FROM contact 
                                WHERE id = %s"""
        dbcursor.execute(sql_people_query, (firstname, surname,))
        record = dbcursor.fetchall()
        return jsonify(record), 200

    except mysql.connector.Error as error:
        print("Failed to get record from MySQL table: {}".format(error))

    finally:
        if ontimedb.is_connected():
            dbcursor.close()
            print("MySQL connection is closed")


@app.route("/loginrequest", methods=["POST"])
def login():
    login = request.get_json()
    mail = login["mail"]
    password = login["password"]
    
    try:
        dbcursor = ontimedb.cursor()
        sql_staff_login_query = ("""SELECT * FROM staff
                                    WHERE mail = %s AND password = %s""")
        dbcursor.execute(sql_staff_login_query, (mail, password))
        record = dbcursor.fetchall()
        return jsonify(record), 200

    except mysql.connector.Error as error:
        print("Failed to get record to MySQL table: {}".format(error))

    finally:
        if ontimedb.is_connected():
            dbcursor.close()
            print("MySQL connection is closed")


if __name__ == '__main__':
    app.run(debug=True)