from flask_cors import CORS
from flask import Flask, jsonify, request
from model import User, Manufacturer, UserPlane, Engine, LandingGear, FuelSystem, CockpitControls, Avionics, ElectricalSystem, FlightInstruments, Brakes, ExhaustSystem, CoolingSystem, Powerplant
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

username = "root"
password = "1234"
database = "Airplane_System"

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@localhost:3000/{database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()

db.init_app(app)
CORS(app)

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    new_user = User(name=username, email=email, profile=role, password=password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

#@app.route('/api/login', methods=['POST'])
# def login():
#   data = request.get_json()
#   username = data['username']
#   password = data['password']

#   if User:
#      return jsonify({'userID': user.id}), 200
#   else:
#        return jsonify({'message': 'Invalid credentials!'}), 401

if __name__ == '__main__':
    app.run(debug=True)