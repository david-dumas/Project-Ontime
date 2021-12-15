# IMPORTS
from flask import request, jsonify, session
from flask_login import LoginManager, UserMixin
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import jwt, datetime, flask

app = flask.Flask(__name__)

CORS(app, supports_credentials=True)

# DATABASE
app.config["Debug"] = True
app.config["SECRET_KEY"] = "thisissecret"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://dbuser:Dbuser123!@145.89.192.95/ontime"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)

#USER TABLE
class staff(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True) 
	firstname = db.Column(db.String(50))
	surname	= db.Column(db.String(50))
	phone = db.Column(db.String(50))
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(50))
	role = db.Column(db.String(50))


@login_manager.user_loader
def load_user(user_id):
    return staff.query.get(int(user_id))

#LOGIN AUTHENTICATION
@app.route("/login_request", methods = ["POST"])
def login_request():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

    # Database query om de gebruiker op te halen
    user = staff.query.filter_by(email=email).first()

    # Wachtwoord controle
    if user.password == password:
        session["active"] = True
        session.modified = True
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

    # Meegeven JWT token
    token = jwt.encode(payload, "secret", algorithm="HS256")

    response.token = token

    return jsonify({"val": True, "token": token})

if __name__ == "__main__":
    app.run(debug=True)