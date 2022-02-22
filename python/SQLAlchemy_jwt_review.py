import flask, jwt, datetime
from flask_login import LoginManager, UserMixin
from flask_cors import CORS
from flask import request, jsonify, session
from flask_sqlalchemy import SQLAlchemy


app = flask.Flask(__name__)
CORS(app, supports_credentials=True)
app.config["DEBUG"] = True

# Secret Key for jwt token
app.config["SECRET_KEY"] = "thisissecret"

# Database connection
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://dbuser:Dbuser123!@145.89.192.95/ontime"
db = SQLAlchemy(app)


admin_manager = LoginManager()
admin_manager.init_app(app)


# Admin table which is requried for SQLalchemy
class admin(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True) 
	firstname = db.Column(db.String(50))
	lastname = db.Column(db.String(50))
	phonenmbr = db.Column(db.String(50))
	email = db.Column(db.String(50), unique=True)
	password = db.Column(db.String(50))


# Login authentication
@app.route("/login_request_admin", methods = ["POST"])
def login_request_admin():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

    user = admin.query.filter_by(email=email).first()
    is_non_empty=bool(user)

    # Check to see if email exists in the database
    if is_non_empty == False:
        return jsonify("User doesn't exist")
    
    # Check to see if password in database matches input password
    if user.password != password:
        return jsonify("Wrong Password")
    
    # If everything goes well return a jwt token and the value True
    elif user.password == password:
        session["active"] = True
        session.modified = True
        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, "secret", algorithm="HS256")
        return jsonify({"val" : True, "token" : token.decode()})


if __name__ == "__main__":
    app.run(debug = True)