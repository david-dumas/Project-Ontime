# IMPORTS
from flask import Flask, request, jsonify, session, redirect, url_for, render_template
from flask_login import LoginManager, UserMixin
from flask_cors import CORS, cross_origin 
from flask_sqlalchemy import SQLAlchemy
import jwt, datetime

app = Flask(__name__)

CORS(app, supports_credentials=True)

# DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///login.db'
app.config['SECRET_KEY'] = 'thisissecret'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

#USER TABLE
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#LOGIN AUTHENTICATION
@app.route('/login_request', methods = ['POST'])
def login_request():
    data = request.get_json()
    email = data['email']
    password = data['password']

    # Database query om de gebruiker op te halen
    user = User.query.filter_by(email=email).first()

    # Wachtwoord controle
    if user.password == password:
        session['active'] = True
        session.modified = True
        response = jsonify(val=True)
    if not user:
        response = jsonify(val=False)

    response.headers.add('Access-Control-Allow-Headers',
                            "Origin, X-Requested-With, Content-Type, Accept, x-auth")

    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }

    # Meegeven JWT token
    token = jwt.encode(payload, 'secret', algorithm='HS256')

    response.token = token

    return jsonify({'val': True, 'token': token})

if __name__ == 'main':
    app.run(debug=True)