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


app.config["SECRET_KEY"] = "thisissecret"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://dbuser:Dbuser123!@145.89.192.95/ontime"
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
admin_manager = LoginManager()
admin_manager.init_app(app)


# Attendant table
class attendant(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True) 
	firstname = db.Column(db.String(50))
	lastname = db.Column(db.String(50))
	phonenmbr = db.Column(db.String(50))
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(50))


# Attendant table
class admin(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True) 
	firstname = db.Column(db.String(50))
	lastname = db.Column(db.String(50))
	phonenmbr = db.Column(db.String(50))
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(50))


# events
class events(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(100))
    details = db.Column(db.String(300))
    start = db.Column(db.String(50))
    end = db.Column(db.String(50), unique=True)
    color = db.Column(db.String(50))
    client = db.Column(db.String(50))


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
        ontimecursor = ontimedb.cursor()
        sql_add_contact_query = """INSERT INTO contact (firstname, lastname, phonenmbr, email, city, street, housenmbr, postalcode) 
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        ontimecursor.execute(sql_add_contact_query, (firstname, lastname, phonenmbr, email, city, street, housenmbr, postalcode,))
        
        ontimedb.commit()
        return("Commit succesful")

    except mysql.connector.Error as error:
        print("Failed to add a contact to contact table: {}".format(error))

    finally:
        if ontimedb.is_connected():
            ontimecursor.close()
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
        ontimecursor = ontimedb.cursor()
        sql_add_attendant_query = """INSERT INTO attendant (firstname, lastname, phonenmbr, email, password) 
                                VALUES (%s, %s, %s, %s, %s)"""
        ontimecursor.execute(sql_add_attendant_query, (firstname, lastname, phonenmbr, email, password,))
        
        ontimedb.commit()
        return("Commit succesful")

    except mysql.connector.Error as error:
        print("Failed to add an attendant to attendant table: {}".format(error))

    finally:
        if ontimedb.is_connected():
            ontimecursor.close()
            print("MySQL connection is closed")


# Requesting data from existing tables
@app.route("/getcontact", methods = ["POST"])
def get_contact_detail():
    getcontact = request.get_json()
    firstname = getcontact["firstname"]
    lastname = getcontact["lastname"]
    try:
        ontimecursor = ontimedb.cursor()
        sql_people_query = """SELECT * FROM contact 
                                WHERE firstname = %s AND lastname = %s"""
        ontimecursor.execute(sql_people_query, (firstname, lastname,))
        record = ontimecursor.fetchall()
        return jsonify(record), 200

    except mysql.connector.Error as error:
        print("Failed to get a contact from contact table: {}".format(error))

    finally:
        if ontimedb.is_connected():
            ontimecursor.close()
            print("MySQL connection is closed")


@app.route("/getattendant", methods = ["GET"])
def get_attendant_detail():
    data = executequery("getattendant")
    return jsonify(data)

def formatrecord(columns,record):
    number = len(columns)
    res = []
    for i in range(number):
      res.append((columns[i],record[i]))
    return res

def executequery(query):
    ontimecursor = ontimedb.cursor()
    resultset = []
    columns = []
    if (query == "getattendant"):
      sql = "DESCRIBE attendant;"
    else:
      query = "can be extended but never reached, use elif"
    ontimecursor.execute(sql)
    for (record) in ontimecursor:
      columns.append(record[0])
    ontimecursor.execute("SELECT * FROM attendant")
    for record in ontimecursor:
      resultset.append(formatrecord(columns,record))
    return resultset


@app.route("/getevents", methods = ["GET"])
def get_event_detail():
    try:
        ontimecursor = ontimedb.cursor()
        sql_get_event_query = """SELECT events.name, events.details, events.start, events.end, events.color, client.firstname, client.lastname 
                                FROM events
                                INNER JOIN client ON events.client_id=client.id;"""
        ontimecursor.execute(sql_get_event_query)
        record = ontimecursor.fetchall()
        return jsonify(record), 200

    except mysql.connector.Error as error:
        print("Failed to get events from events table: {}".format(error))

    finally:
        if ontimedb.is_connected():
            ontimecursor.close()
            print("MySQL connection is closed")


# Updating data in existing tables
@app.route("/updateattendant", methods = ["POST"])
def update_attendant():
    updateattendant = request.get_json()
    id = updateattendant["id"]
    firstname = updateattendant["firstname"]
    lastname = updateattendant["lastname"]
    phonenmbr = updateattendant["phonenmbr"]
    email = updateattendant["email"]
    password = updateattendant["password"]
    try:
        ontimecursor = ontimedb.cursor()
        sql_update_attendant_query = """UPDATE attendant 
                                SET firstname = %s, lastname = %s, phonenmbr = %s, email = %s, password = %s
                                WHERE id = %s"""
        ontimecursor.execute(sql_update_attendant_query, (firstname, lastname, phonenmbr, email, password, id,))

        ontimedb.commit()
        return("Commit succesful")
    
    except mysql.connector.Error as error:
        print("Failed to update attendant in attendant table: {}".format(error))
        
    finally:
        if ontimedb.is_connected():
            ontimecursor.close()
            print("MySQL connection is closed")


# Deleting data in existing tables
@app.route("/deleteattendantv1", methods = ["POST"])
def delete_attendant_detail():
    delete_attendant = request.get_json()
    id = delete_attendant["id"]
    try:
        ontimecursor = ontimedb.cursor()
        sql_delete_attendant_query = """DELETE FROM attendant 
                                WHERE id = %s"""
        ontimecursor.execute(sql_delete_attendant_query, (id,))

        ontimedb.commit()
        return("Delete succesful")

    except mysql.connector.Error as error:
        print("Failed to delete attendant from attendant table: {}".format(error))

    finally:
        if ontimedb.is_connected():
            ontimecursor.close()
            print("MySQL connection is closed")


# Login attendant
@login_manager.user_loader
def load_attendant(user_id):
    return attendant.query.get(int(user_id))

# Login authentication
@app.route("/login_request_attendant", methods = ["POST"])
def login_request_attendant():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

# Database query
    user = attendant.query.filter_by(email=email).first()

# Password check
    if user.password == password:
        session["active"] = True
        session.modified = True
        response = ("it works")
        response = jsonify(val=True)
    if not user:
        response = jsonify(val=False)

    response.headers.add("Access-Control-Allow-Headers",
                            "Origin, X-Requested-With, Content-Type, Accept, x-auth")

    payload = {
        "id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        "iat": datetime.datetime.utcnow()
    }

# JWT token
    token = jwt.encode(payload, "secret", algorithm="HS256")

    return jsonify({"val" : True, "token" : token.decode()})


# Login admin
@admin_manager.user_loader
def load_admin(admin_id):
    return admin.query.get(int(admin_id))

# Login authentication
@app.route("/login_request_admin", methods = ["POST"])
def login_request_admin():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

# Database query
    user = admin.query.filter_by(email=email).first()

# Password check
    if user.password == password:
        session["active"] = True
        session.modified = True
        response = ("it works")
        response = jsonify(val=True)
    if not user:
        response = jsonify(val=False)

    response.headers.add("Access-Control-Allow-Headers",
                            "Origin, X-Requested-With, Content-Type, Accept, x-auth")

    payload = {
        "id": user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        "iat": datetime.datetime.utcnow()
    }

# JWT token
    token = jwt.encode(payload, "secret", algorithm="HS256")

    return jsonify({"val" : True, "token" : token.decode()})


if __name__ == "__main__":
    app.run(debug = True)