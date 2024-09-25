from flask_cors import CORS
from flask import Flask, jsonify, request
from model import db, User, Manufacturer, UserPlane, Engine, LandingGear, FuelSystem, CockpitControls, Avionics, ElectricalSystem, FlightInstruments, Brakes, ExhaustSystem, CoolingSystem, Powerplant
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta
import uuid
import pandas as pd

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

@app.route('/file_upload', methods=['POST'])
def file_upload():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400

        file = request.files['file']

        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400

        if not file.filename.endswith('.csv'):
            return jsonify({'error': 'File is not a CSV'}), 400

        print(f"Received file: {file.filename}")

        try:
            df = pd.read_csv(file)
            data_preview = df.head().to_json(orient="records")
            return jsonify({'message': 'File uploaded successfully', 'preview': data_preview}), 200

        except Exception as e:
            print(f"Error processing file: {str(e)}")
            return jsonify({'error': f'Failed to process file: {str(e)}'}), 500

    except Exception as e:
        print(f"Error during upload: {str(e)}")
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)