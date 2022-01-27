import csv, flask, mysql.connector, jwt, datetime
from flask_login import LoginManager, UserMixin
from flask_cors import CORS
from flask import request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


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


# Login admin
@admin_manager.user_loader
def load_admin(admin_id):
    return admin.query.get(int(admin_id))

# Login authentication
@app.route("/login_request_admin", methods = ["POST"])
def login_request_admin():
    data = request.get_json()
    email = data["email"]
    hashed_password = generate_password_hash(data["password"], method = "sha256")

# Database query
    user = admin.query.filter_by(email=email).first()
    is_non_empty=bool(user)

# Password check
    if is_non_empty == False:
        return jsonify({"message" : "Wrong email"})
    if user.password == hashed_password:
        session["active"] = True
        session.modified = True
        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, "secret", algorithm="HS256")
        return jsonify({"Val" : "True", "token" : token.decode()})
    else:
        return jsonify({"message" : "wrong password"})



if __name__ == "__main__":
    app.run(debug = True)