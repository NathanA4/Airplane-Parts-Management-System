from flask_cors import CORS
from flask import Flask, jsonify, request
from model import WeatherData, db, User, Engine, LandingGear, FuelSystem, CockpitControl, Avionic, ElectricalSystem, FlightInstrument, Brake, ExhaustSystem, CoolingSystem, Powerplant
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import uuid
import pandas as pd
import requests 
from sqlalchemy.sql import text
from datetime import datetime, timedelta

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
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No input data provided"}), 400

        username = data.get('username')
        password = data.get('password')
        role = data.get('role')

        if not all([username, password, role]):
            return jsonify({"error": "Missing required fields"}), 400

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

        new_user = User(name=username, profile=role, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully!"}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "User with this email or username already exists"}), 409

    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

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
        "userId": user.id,
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

WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
WEATHER_API_KEY = "14820d48f26f136e2da6ed36da9dc80c"

@app.route('/api/weather', methods=['GET'])
def get_weather():
    try:
        city = request.args.get('city')
        if not city:
            return jsonify({"error": "City parameter is required"}), 400

        one_hour_ago = datetime.utcnow() - timedelta(hours=1)
        existing_weather = WeatherData.query.filter(
            WeatherData.city == city,
            WeatherData.timestamp >= one_hour_ago
        ).first()

        if existing_weather:
            return jsonify({
                "city": existing_weather.city,
                "temperature": existing_weather.temperature,
                "description": existing_weather.description,
                "cached": True
            }), 200

        params = {
            'q': city,
            'appid': WEATHER_API_KEY,
            'units': 'metric'
        }
        response = requests.get(WEATHER_API_URL, params=params)
        response.raise_for_status()
        weather_data = response.json()

        city_name = weather_data['name']
        temperature = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']

        new_weather = WeatherData(
            city=city_name,
            temperature=temperature,
            description=weather_description
        )
        db.session.add(new_weather)
        db.session.commit()

        return jsonify({
            "city": city_name,
            "temperature": temperature,
            "description": weather_description,
            "cached": False
        }), 200

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch weather data", "details": str(e)}), 500

    except Exception as e:
        return jsonify({"error": "An error occurred", "details": str(e)}), 500


Airplane_System = []

def get_parameter_value(params, key):
    """Utility function to fetch parameter value or return None."""
    return next((param['value'] for param in params if param['name'] == key), None)

@app.route('/api/save_plane', methods=['POST'])
def save_plane():
    global Airplane_System
    Airplane_System.clear()

    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400
    if 'nodes' not in data or 'edges' not in data:
        return jsonify({"error": "Missing nodes or edges"}), 400

    nodes = data['nodes']
    edges = data['edges']
    user_data = data.get('userData', {})
    user_id = data.get('userID')

    for node in nodes:
        node_type = node['type']
        params = node['parameters']

        if node_type == 'physicalModel.Engine' and node['name'] == 'Engine':
            engine = Engine(
                engine_type=get_parameter_value(params, 'Engine Type'),
                horsepower=int(get_parameter_value(params, 'Horsepower') or 0),
                rpm=int(get_parameter_value(params, 'RPM') or 0),
                displacement=float(get_parameter_value(params, 'Displacement') or 0.0),
                fuel_type_avgas=get_parameter_value(params, 'Fuel Type (AVGAS)'),
                fuel_consumption=float(get_parameter_value(params, 'Fuel Consumption (GPH)') or 0.0),
                compression_ratio=float(get_parameter_value(params, 'Compression Ratio') or 0.0),
                torque=int(get_parameter_value(params, 'Torque (lb-ft)') or 0),
                egt=int(get_parameter_value(params, 'Exhaust Gas Temperature (EGT)') or 0),
                cht=int(get_parameter_value(params, 'Cylinder Head Temperature (CHT)') or 0),
                oil_pressure=int(get_parameter_value(params, 'Oil Pressure (PSI)') or 0),
                oil_temperature=int(get_parameter_value(params, 'Oil Temperature (°F)') or 0),
                user_id=user_id
            )
            db.session.add(engine)
            Airplane_System.append(node['name'])
            print(f"Engine saved with user_id: {engine.user_id}")

        elif node_type == 'physicalModel.LandingGear' and node['name'] == 'LandingGear':
            landing_gear = LandingGear(
                tire_type=get_parameter_value(params, 'Tire Type'),
                material=get_parameter_value(params, 'Material'),
                shock_absorption=get_parameter_value(params, 'Shock Absorption'),
                tire_pressure=int(get_parameter_value(params, 'Tire Pressure (PSI)') or 0),
                retraction_system=get_parameter_value(params, 'Retraction System'),
                braking_system=get_parameter_value(params, 'Braking System'),
                track_width=float(get_parameter_value(params, 'Track Width (ft)') or 0.0),
                tire_size=float(get_parameter_value(params, 'Tire Size (in)') or 0.0),
                weight_capacity=int(get_parameter_value(params, 'Weight Capacity (lbs)') or 0),
                user_id=user_id
            )
            db.session.add(landing_gear)
            Airplane_System.append(node['name'])

        elif node_type == 'physicalModel.FuelSystem' and node['name'] == 'FuelSystem':
            fuel_system = FuelSystem(
                fuel_tank_capacity=float(get_parameter_value(params, 'Fuel Tank Capacity (gallons)') or 0.0),
                fuel_type=get_parameter_value(params, 'Fuel Type'),
                fuel_delivery_system = get_parameter_value(params, 'Fuel Delivery System'),
                fuel_pressure=int(get_parameter_value(params, 'Fuel Pressure (PSI)') or 0),
                fuel_pump=get_parameter_value(params, 'Fuel Pumps'),
                fuel_lines=get_parameter_value(params, 'Fuel Lines Type'),
                fuel_filter=get_parameter_value(params, 'Fuel Filter'),             
                fuel_value=get_parameter_value(params, 'Fuel Selector Valve'),
                fuel_flow=float(get_parameter_value(params, 'Fuel Flow Indicator (GPH)') or 0.0),
                fuel_venting_system = get_parameter_value(params, 'Fuel Venting System'),
                user_id=user_id
            )
            db.session.add(fuel_system)
            Airplane_System.append(node['name'])

        elif node_type == 'physicalModel.CockpitControls' and node['name'] == 'CockpitControls':
            cockpit_control = CockpitControl(
                control_yoke_stick=get_parameter_value(params, 'Control Yoke/stick'),
                throttle=get_parameter_value(params, 'Throttle'),
                rudder_pedals=get_parameter_value(params, 'Rudder Pedals'),
                trim_controls=get_parameter_value(params, 'Trim Controls'),
                flap_controls=get_parameter_value(params, 'Flap Controls'),
                autopilots=get_parameter_value(params, 'Autopilot'),
                landing_gear_controls=get_parameter_value(params, 'Landing Gear Controls'),
                radio_panel=get_parameter_value(params, 'Radio Panel'),
                instrument_panel=get_parameter_value(params, 'Instrument Panel'),
                user_id=user_id
            )
            db.session.add(cockpit_control)
            Airplane_System.append(node['name'])

        elif node_type == 'physicalModel.Avionics' and node['name'] == 'Avionics':
            avionic = Avionic(
                gps=get_parameter_value(params, 'GPS System'),
                nav_com_radios=get_parameter_value(params, 'Nav/Com Radio'),
                adf=get_parameter_value(params, 'ADF (Automatic Direction Finder)'),
                vor=get_parameter_value(params, 'VOR (VHF Omnidirectional Range)'),
                dme=get_parameter_value(params, 'DME (Distance Measuring Equipment)'),
                transponder=get_parameter_value(params, 'Transponder'),
                elt=get_parameter_value(params, 'ELT (Emergency Locator Transmitter)'),
                ads_b=get_parameter_value(params, 'ADS-B (Automatic Dependent Surveillance-Broadcast)'),
                weather_radar=get_parameter_value(params, 'Weather Radar'),
                autopilot_system=get_parameter_value(params, 'Autopilot System'),
                flight_director=get_parameter_value(params, 'Flight Director'),
                tcas=get_parameter_value(params, 'TCAS (Traffic Collision Avoidance System)'),
                transponder_mode=get_parameter_value(params, 'Transponder Modes'),
                user_id=user_id
            )
            db.session.add(avionic)
            Airplane_System.append(node['name'])

        elif node_type == 'physicalModel.ElectricalSystem' and node['name'] == 'ElectricalSystem':
            electrical_system = ElectricalSystem(
                battery_capacity=int(get_parameter_value(params, 'Battery Capacity (Ah)') or 0),
                alternator_rating_amps=int(get_parameter_value(params, 'Alternator Rating (Amps)') or 0),
                system_voltage=int(get_parameter_value(params, 'System Voltage (Volts)') or 0),
                wiring_type=get_parameter_value(params, 'Wiring Type'),
                circuit_breakers=get_parameter_value(params, 'Circuit Breakers'),
                electrical_buses=get_parameter_value(params, 'Electrical Buses'),
                master_switch=get_parameter_value(params, 'Master Switch'),
                generator_output_amps=int(get_parameter_value(params, 'Generator Output (Amps)') or 0),
                inverters=get_parameter_value(params, 'Inverters'),
                power_outlets=get_parameter_value(params, 'Power Outlets'),
                light_system=get_parameter_value(params, 'Lighting System'),
                aps=get_parameter_value(params, 'Avionics Power Supply'),
                battery_type=get_parameter_value(params, 'Battery Type'),
                backup_battery=get_parameter_value(params, 'Backup Battery'),
                electrical_monitoring=get_parameter_value(params, 'Electrical Fault Monitoring'),
                user_id=user_id
            )
            db.session.add(electrical_system)
            Airplane_System.append(node['name'])

        elif node_type == 'physicalModel.FlightInstruments' and node['name'] == 'FlightInstruments':
            flight_instrument = FlightInstrument(
                altimeter=get_parameter_value(params, 'Altimeter'),
                airspeed_indicator=get_parameter_value(params, 'Airspeed Indicator'),
                heading_indicator=get_parameter_value(params, 'Heading Indicator'),
                vertical_speed_indicator=get_parameter_value(params, 'Vertical Speed Indicator'),
                turn_coordinator=get_parameter_value(params, 'Turn Coordinator'),
                gyro_horizon = get_parameter_value(params, 'Gyro Horizon'),
                compass = get_parameter_value(params, 'Compass'),
                tachometer = get_parameter_value(params, 'Tachometer'),
                fuel_gauge = get_parameter_value(params, 'Fuel Gauge'),
                oil_pressure_gauge = get_parameter_value(params, 'Oil Pressure Gauge'),
                oil_temperature_gauge =get_parameter_value(params, 'Oil Temperature Gauge'),
                manifold_pressure_gauge = get_parameter_value(params, 'Manifold Pressure Gauge'),
                engine_temperature_gauge = get_parameter_value(params, 'Engine Temperature Gauge'),
                vacuum_gauge = get_parameter_value(params, 'Vacuum Gauge'),
                user_id=user_id
            )
            db.session.add(flight_instrument)
            Airplane_System.append(node['name'])

        elif node_type == 'physicalModel.Brakes' and node['name'] == 'Brakes':
            brake = Brake(
                brake_type=get_parameter_value(params, 'Brake Type'),
                brake_material=get_parameter_value(params, 'Brake Material'),
                brake_size=int(get_parameter_value(params, 'Brake Size') or 0),
                brake_pressure=int(get_parameter_value(params, 'Brake Pressure') or 0),
                brake_system=get_parameter_value(params, 'Brake System'),
                anti_skid_system=get_parameter_value(params, 'Anti-Skid System'),
                parking_brake=get_parameter_value(params, 'Parking Brake'),
                brake_lines=get_parameter_value(params, 'Brake Lines'),
                brake_pads=get_parameter_value(params, 'Brake Pads'),
                brake_fluid=get_parameter_value(params, 'Brake Fluid Type'),
                user_id=user_id
            )
            db.session.add(brake)
            Airplane_System.append(node['name'])

        elif node_type == 'physicalModel.ExhaustSystem' and node['name'] == 'ExhaustSystem':
            exhaust_system = ExhaustSystem(
                exhaust_type=get_parameter_value(params, 'Exhaust Type'),
                material=get_parameter_value(params, 'Material'),
                exhaust_pipe_diameter=float(get_parameter_value(params, 'Exhaust Pipe Diameter (in)') or 0.0),
                muffler_type=get_parameter_value(params, 'Muffler Type'),
                heat_shields=get_parameter_value(params, 'Heat Shields'),
                exhaust_gaskets=get_parameter_value(params, 'Exhaust Gaskets'),
                exhaust_temperature=int(get_parameter_value(params, 'Exhaust Temperature (°F)') or 0),
                exhaust_system_pressure=int(get_parameter_value(params, 'Exhaust System Pressure (PSI)') or 0),
                exhaust_system_mounting=get_parameter_value(params, 'Exhaust System Mounting'),
                emission_control=get_parameter_value(params, 'Emission Control'),
                user_id=user_id
            )
            db.session.add(exhaust_system)
            Airplane_System.append(node['name'])

        elif node_type == 'physicalModel.CoolingSystem' and node['name'] == 'CoolingSystem':
            cooling_system = CoolingSystem(
                coolant_type=get_parameter_value(params, 'Coolant Type'),
                radiator_size=int(get_parameter_value(params, 'Radiator Size (inches)') or 0),
                cooling_fan=get_parameter_value(params, 'Cooling Fan'),
                oil_cooler=get_parameter_value(params, 'Oil Cooler'),
                cooling_system_pressure=int(get_parameter_value(params, 'Cooling System Pressure (PSI)') or 0),
                thermostat=get_parameter_value(params, 'Thermostat'),
                temperature_gauge=get_parameter_value(params, 'Temperature Gauge'),
                cooling_system_pumps=get_parameter_value(params, 'Cooling System Pumps'),
                coolant_capacity=float(get_parameter_value(params, 'Coolant Capacity (gallons)') or 0.0),
                airflow_management=get_parameter_value(params, 'Airflow Management'),
                cooling_fins=get_parameter_value(params, 'Cooling Fins'),
                cooling_system_mounting=get_parameter_value(params, 'Cooling System Mounting'),
                user_id=user_id
            )
            db.session.add(cooling_system)
            Airplane_System.append(node['name'])

        elif node_type == 'physicalModel.Powerplant' and node['name'] == 'Powerplant':
            powerplant = Powerplant(
                engine_type=get_parameter_value(params, 'Engine Type'),
                engine_model=get_parameter_value(params, 'Engine Model'),
                horsepower=int(get_parameter_value(params, 'Horsepower') or 0),
                rpm=int(get_parameter_value(params, 'RPM') or 0),
                displacement=float(get_parameter_value(params, 'Displacment (L)') or 0.0),
                fuel_type=get_parameter_value(params, 'Fuel Type'),
                compression_ratio=float(get_parameter_value(params, 'Compression Ratio') or 0),
                turbocharger=get_parameter_value(params, 'Turbocharger'),
                intercooler= get_parameter_value(params, 'Intercooler'),
                fuel_injection=get_parameter_value(params, 'Fuel Injection'),
                ignition_system=get_parameter_value(params, 'Ignition System'),
                cooling_system=get_parameter_value(params, 'Cooling System'),
                exhaust_system=get_parameter_value(params, 'Exhaust System'),
                oil_system=get_parameter_value(params, 'Oil System'),
                power_output=float(get_parameter_value(params, 'Power Output (kW)') or 0.0),
                operating_temp=int(get_parameter_value(params, 'Operating Temperature (°C)') or 0),
                weights=int(get_parameter_value(params, 'Weight (lbs)') or 0),
                maintenance_intervals=get_parameter_value(params, 'Maintenance Intervals'),
                user_id=user_id
            )
            db.session.add(powerplant)
            Airplane_System.append(node['name'])

    db.session.commit()
    return jsonify({"status": "Plane model saved successfully"}), 201

@app.route('/api/retrieve_plane', methods=['GET'])
def retrieve_plane():
    try:
        user_id = request.args.get('userID') 

        if not user_id:
            return jsonify({"error": "User ID is required"}), 400

        engine = Engine.query.filter_by(user_id=user_id).all()
        landing_gear = LandingGear.query.filter_by(user_id=user_id).all()
        fuel_system = FuelSystem.query.filter_by(user_id=user_id).all()
        cockpit_control = CockpitControl.query.filter_by(user_id=user_id).all()
        avionics = Avionic.query.filter_by(user_id=user_id).all()
        electrical_system = ElectricalSystem.query.filter_by(user_id=user_id).all()
        flight_instruments = FlightInstrument.query.filter_by(user_id=user_id).all()
        brakes = Brake.query.filter_by(user_id=user_id).all()
        exhaust_systems = ExhaustSystem.query.filter_by(user_id=user_id).all()
        cooling_systems = CoolingSystem.query.filter_by(user_id=user_id).all()
        powerplant = Powerplant.query.filter_by(user_id=user_id).all()

        airplane_data = {
            "Engine": [engine_item.to_dict() for engine_item in engine],
            "LandingGear": [landing_gear_item.to_dict() for landing_gear_item in landing_gear],
            "FuelSystem": [fuel_system_item.to_dict() for fuel_system_item in fuel_system],
            "CockpitControl": [cockpit_control_item.to_dict() for cockpit_control_item in cockpit_control],
            "Avionic": [avionics_item.to_dict() for avionics_item in avionics],
            "ElectricalSystem": [electrical_item.to_dict() for electrical_item in electrical_system],
            "FlightInstruments": [instrument_item.to_dict() for instrument_item in flight_instruments],
            "Brakes": [brake_item.to_dict() for brake_item in brakes],
            "ExhaustSystems": [exhaust_item.to_dict() for exhaust_item in exhaust_systems],
            "CoolingSystems": [cooling_item.to_dict() for cooling_item in cooling_systems],
            "Powerplant": [powerplant_item.to_dict() for powerplant_item in powerplant],
        }

        return jsonify(airplane_data), 200

    except Exception as e:
        print(f"Error retrieving airplane data: {str(e)}")
        return jsonify({'error': f'Failed to retrieve airplane data: {str(e)}'}), 500

@app.route('/api/coolingsystemefficiency', methods=['GET'])
def get_user_coolingsystemefficiency():
    """Query a database view."""
    try:
        query = text("SELECT * FROM airplane_system.coolingsystemefficiency;")
        result = db.session.execute(query).fetchall()
        data = [dict(row._mapping) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/comprehensiveavionics', methods=['GET'])
def get_user_comprehensiveavionics():
    """Query a database view."""
    try:
        query = text("SELECT * FROM airplane_system.comprehensiveavionics;")
        result = db.session.execute(query).fetchall()
        data = [dict(row._mapping) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/highhorsepowerusers', methods=['GET'])
def get_user_highhorsepowerusers():
    """Query a database view."""
    try:
        query = text("SELECT * FROM airplane_system.highhorsepowerusers;")
        result = db.session.execute(query).fetchall()
        data = [dict(row._mapping) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/hightorqueengines', methods=['GET'])
def get_user_hightorqueengines():
    """Query a database view."""
    try:
        query = text("SELECT * FROM airplane_system.hightorqueengines;")
        result = db.session.execute(query).fetchall()
        data = [dict(row._mapping) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/useraboveaverageengines', methods=['GET'])
def get_user_useraboveaverageengines():
    """Query a database view."""
    try:
        query = text("SELECT * FROM airplane_system.useraboveaverageengines;")
        result = db.session.execute(query).fetchall()
        data = [dict(row._mapping) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/userbrakessummary', methods=['GET'])
def get_user_userbrakessummary():
    """Query a database view."""
    try:
        query = text("SELECT * FROM airplane_system.userbrakessummary;")
        result = db.session.execute(query).fetchall()
        data = [dict(row._mapping) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/usercockpitavionicsview', methods=['GET'])
def get_user_usercockpitavionicsview():
    """Query a database view."""
    try:
        query = text("SELECT * FROM airplane_system.usercockpitavionicsview;")
        result = db.session.execute(query).fetchall()
        data = [dict(row._mapping) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/userpowerplantdetails', methods=['GET'])
def get_user_userpowerplantdetails():
    """Query a database view."""
    try:
        query = text("SELECT * FROM airplane_system.userpowerplantdetails;")
        result = db.session.execute(query).fetchall()
        data = [dict(row._mapping) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/userenginelandinggearview', methods=['GET'])
def get_user_userenginelandinggearview():
    """Query a database view."""
    try:
        query = text("SELECT * FROM airplane_system.userenginelandinggearview;")
        result = db.session.execute(query).fetchall()
        data = [dict(row._mapping) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/userswithcomponents', methods=['GET'])
def get_user_userswithcomponents():
    """Query a database view."""
    try:
        query = text("SELECT * FROM airplane_system.userswithcomponents;")
        result = db.session.execute(query).fetchall()
        data = [dict(row._mapping) for row in result]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)