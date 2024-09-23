from flask_cors import CORS
from flask import Flask, jsonify, request
from model import db, User, Manufacturer, UserPlane, Engine, LandingGear, FuelSystem, CockpitControls, Avionics, ElectricalSystem, FlightInstruments, Brakes, ExhaustSystem, CoolingSystem, Powerplant
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta
import uuid

app = Flask(__name__)
bcrypt = Bcrypt(app)

username = "root"
password = "1234"
database = "Airplane_System"

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@localhost:3000/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
CORS(app)

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = User(name=username, email=email, profile=role, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(name=username).first()

    if user is None:
        return jsonify({"Error": "Unauthorized User"}), 401

    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"Error": "Unauthorized User"}), 401

    return jsonify({
        "username": user.name,
        "role": user.profile 
    })

if __name__ == '__main__':
    app.run(debug=True)