from flask_cors import CORS
from flask import Flask, jsonify, request
from model import db, User, Engine, LandingGear, FuelSystem, CockpitControl, Avionic, ElectricalSystem, FlightInstrument, Brake, ExhaustSystem, CoolingSystem, Powerplant
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
    new_user = Users(name=username, email=email, profile=role, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = Users.query.filter_by(name=username).first()

    if user is None:
        return jsonify({"Error": "Unauthorized User"}), 401

    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"Error": "Unauthorized User"}), 401

    return jsonify({
        "username": user.name,
        "role": user.profile 
    })
#Display .csv file
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

Airplane_System = []

def get_parameter_value(params, key):
    """Utility function to fetch parameter value or return None."""
    return next((param['value'] for param in params if param['name'] == key), None)

@app.route('/api/save_plane', methods=['POST'])
def save_plane():
    global Airplane_System
    Airplane_System.clear()  # Clear previous entries

    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    if 'nodes' not in data or 'edges' not in data:
        return jsonify({"error": "Missing nodes or edges"}), 400

    nodes = data['nodes']
    edges = data['edges']
    user_data = data.get('userData', {})
    user_id = data.get('userID')
    model_id = data.get('modelID')
    for node in nodes:
        node_type = node['type']
        params = node['parameters']

            # Example for handling Engine type node
        if node_type == 'physicalModel.Engine' and node['name'] == 'Engine':
           engine = Engine(
                engine_type=get_parameter_value(params, 'Engine Type'),
                horsepower=int(get_parameter_value(params, 'Horsepower') or 0),
                rpm=int(get_parameter_value(params, 'RPM') or 0),
                displacement=float(get_parameter_value(params, 'Displacement') or 0.0),
                fuel_type=get_parameter_value(params, 'Fuel Type (AVGAS)'),
                fuel_consumption=float(get_parameter_value(params, 'Fuel Consumption (GPH)') or 0.0),
                compression_ratio=float(get_parameter_value(params, 'Compression Ratio') or 0.0),
                torque=int(get_parameter_value(params, 'Torque (lb-ft)') or 0),
                egt=int(get_parameter_value(params, 'Exhaust Gas Temperature (EGT)') or 0),
                cht=int(get_parameter_value(params, 'Cylinder Head Temperature (CHT)') or 0),
                oil_pressure=int(get_parameter_value(params, 'Oil Pressure (PSI)') or 0),
                oil_temperature=int(get_parameter_value(params, 'Oil Temperature (°F)') or 0),
                model_id=model_id  
            )
      
        db.session.add(engine)
        Airplane_System.append(node['name']) 

        db.session.commit()
        return jsonify({"status": "Plane model saved successfully"}), 201

if __name__ == '__main__':
    app.run(debug=True)