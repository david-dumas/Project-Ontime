from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import jwt, datetime

app = Flask(__name__)

app.config["SECRET_KEY"] = "thsisthesecretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://dbuser:Dbuser123!@145.89.192.95/ontime"

db = SQLAlchemy(app)


# Attendant table
class attendant(db.Model):
	id = db.Column(db.Integer, primary_key=True) 
	firstname = db.Column(db.String(50))
	lastname = db.Column(db.String(50))
	phonenmbr = db.Column(db.String(50))
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(50))


# Admin table
class admin(db.Model):
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


@app.route("/attendant", methods = ["GET"])
def get_all_attendants():

    all_attendants = attendant.query.all()

    output = []

    for attendants in all_attendants:
        attendant_data = {}
        attendant_data["firstname"] = attendants.firstname
        attendant_data["lastname"] = attendants.lastname
        attendant_data["phonenmbr"] = attendants.phonenmbr
        attendant_data["email"] = attendants.email
        attendant_data["password"] = attendants.password
        output.append(attendant_data)
    
    return jsonify({"attendants" : output})


@app.route("/attendant/<id>", methods = ["GET"])
def get_specific_attendants(id):

    specific_attendant = attendant.query.filter_by(id=id).first()

    if not specific_attendant:
        return jsonify({"message" : "No attendant found"})

    attendant_data = {}
    attendant_data["firstname"] = specific_attendant.firstname
    attendant_data["lastname"] = specific_attendant.lastname
    attendant_data["phonenmbr"] = specific_attendant.phonenmbr
    attendant_data["email"] = specific_attendant.email
    attendant_data["password"] = specific_attendant.password
    
    return jsonify({"attendants" : attendant_data})


@app.route("/attendant/<id>", methods = ["DELETE"])
def delete_attendant(id):
    specific_attendant = attendant.query.filter_by(id=id).first()

    if not specific_attendant:
        return jsonify({"message" : "No attendant found"})
    
    db.sessions.delete(specific_attendant)
    db.session.commit()

    return jsonify({"message" : "Attendant deleted"})


@app.route("/attendant", methods = ["POST"])
def add_attendant():
    data = request.get_json()
    
    hashed_password = generate_password_hash(data["password"], method = "sha256")

    new_user = attendant(firstname = data["firstname"], lastname = data["lastname"], phonenmbr = data["phonenmbr"], email = data["email"], password = hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message" : "attendant added"})


@app.route("/login")
def login():
    auth = request.authorization

    if not auth or not auth.username or not auth.password:
        return make_response("Could not verify1", 401, {"www-Authenticate" : "Basic realm = 'Login required'"})

    specific_attendant = attendant.query.filter_by(email = auth.username).first()

    if not specific_attendant:
        return make_response("Could not verify2", 401, {"www-Authenticate" : "Basic realm = 'Login required'"})
    
    if check_password_hash(specific_attendant.password, auth.password):
        token = jwt.encode({"email" : specific_attendant.email, "exp" : datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, app.config["SECRET_KEY"])

        return jsonify({"token" : token.decode("UTF-8")})
    
    return make_response("Could not verify3", 401, {"www-Authenticate" : "Basic realm = 'Login required'"})


if __name__ == "__main__":
    app.run(debug = True)