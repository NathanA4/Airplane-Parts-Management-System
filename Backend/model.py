from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    profile = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)

    airplane_models = db.relationship('AirplaneModel', backref='user', cascade="all, delete")

class AirplaneModel(db.Model):
    __tablename__ = 'airplane_models'
    model_id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))

    engines = db.relationship('Engine', backref='airplane_model', cascade="all, delete")
    landing_gears = db.relationship('LandingGear', backref='airplane_model', cascade="all, delete")
    fuel_systems = db.relationship('FuelSystem', backref='airplane_model', cascade="all, delete")
    cockpit_controls = db.relationship('CockpitControl', backref='airplane_model', cascade="all, delete")
    avionics = db.relationship('Avionic', backref='airplane_model', cascade="all, delete")
    electrical_systems = db.relationship('ElectricalSystem', backref='airplane_model', cascade="all, delete")
    flight_instruments = db.relationship('FlightInstrument', backref='airplane_model', cascade="all, delete")
    brakes = db.relationship('Brake', backref='airplane_model', cascade="all, delete")
    exhaust_systems = db.relationship('ExhaustSystem', backref='airplane_model', cascade="all, delete")
    cooling_systems = db.relationship('CoolingSystem', backref='airplane_model', cascade="all, delete")
    powerplants = db.relationship('Powerplant', backref='airplane_model', cascade="all, delete")

class Engine(db.Model):
    __tablename__ = 'engine'
    id = db.Column(db.Integer, primary_key=True)
    engine_type = db.Column(db.String(255))
    horsepower = db.Column(db.Integer)
    rpm = db.Column(db.Integer)
    displacement = db.Column(db.Float)
    fuel_type_avgas = db.Column(db.String(255))
    fuel_consumption = db.Column(db.Float)
    compression_ratio = db.Column(db.Float)
    torque = db.Column(db.Integer)
    egt = db.Column(db.Integer)
    cht = db.Column(db.Integer)
    oil_pressure = db.Column(db.Integer)
    oil_temperature = db.Column(db.Integer)
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class LandingGear(db.Model):
    __tablename__ = 'landing_gear'
    id = db.Column(db.Integer, primary_key=True)
    tire_type = db.Column(db.String(255))
    material = db.Column(db.String(255))
    shock_absorption = db.Column(db.String(255))
    tire_pressure = db.Column(db.Integer)
    retraction_system = db.Column(db.String(255))
    braking_system = db.Column(db.String(255))
    track_width = db.Column(db.Float)
    tire_size = db.Column(db.Float)
    weight_capacity = db.Column(db.Integer)
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class FuelSystem(db.Model):
    __tablename__ = 'fuel_system'
    id = db.Column(db.Integer, primary_key=True)
    fuel_tank_capacity = db.Column(db.Float)
    fuel_type = db.Column(db.String(255))
    fuel_delivery_system = db.Column(db.String(255))
    fuel_pressure = db.Column(db.Integer)
    fuel_pump = db.Column(db.String(255))
    fuel_lines = db.Column(db.String(255))
    fuel_filter = db.Column(db.String(255))
    fuel_value = db.Column(db.String(255))
    fuel_flow = db.Column(db.Float)
    fuel_venting_system = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class CockpitControl(db.Model):
    __tablename__ = 'cockpit_controls'
    id = db.Column(db.Integer, primary_key=True)
    control_yoke_stick = db.Column(db.String(255))
    throttle = db.Column(db.String(255))
    rudder_pedals = db.Column(db.String(255))
    trim_controls = db.Column(db.String(255))
    flap_controls = db.Column(db.String(255))
    autopilots = db.Column(db.String(255))
    landing_gear_controls = db.Column(db.String(255))
    radio_panel = db.Column(db.String(255))
    instrument_panel = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class Avionic(db.Model):
    __tablename__ = 'avionics'
    id = db.Column(db.Integer, primary_key=True)
    gps = db.Column(db.String(255))
    nav_com_radios = db.Column(db.String(255))
    adf = db.Column(db.String(255))
    vor = db.Column(db.String(255))
    dme = db.Column(db.String(255))
    transponder = db.Column(db.String(255))
    elt = db.Column(db.String(255))
    ads_b = db.Column(db.String(255))
    weather_radar = db.Column(db.String(255))
    autopilot_system = db.Column(db.String(255))
    flight_director = db.Column(db.String(255))
    tcas = db.Column(db.String(255))
    transponder_mode = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class ElectricalSystem(db.Model):
    __tablename__ = 'electrical_system'
    id = db.Column(db.Integer, primary_key=True)
    battery_capacity = db.Column(db.Integer)
    alternator_rating_amps = db.Column(db.Integer)
    system_voltage = db.Column(db.Integer)
    wiring_type = db.Column(db.String(255))
    circuit_breakers = db.Column(db.String(255))
    electrical_buses = db.Column(db.String(255))
    master_switch = db.Column(db.String(255))
    generator_output_amps = db.Column(db.Integer)
    inverters = db.Column(db.String(255))
    power_outlets = db.Column(db.String(255))
    light_system = db.Column(db.String(255))
    aps = db.Column(db.String(255))
    battery_type = db.Column(db.String(255))
    backup_battery = db.Column(db.String(255))
    electrical_monitoring = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class FlightInstrument(db.Model):
    __tablename__ = 'flight_instruments'
    id = db.Column(db.Integer, primary_key=True)
    altimeter = db.Column(db.String(255))
    airspeed_indicator = db.Column(db.String(255))
    heading_indicator = db.Column(db.String(255))
    vertical_speed_indicator = db.Column(db.String(255))
    turn_coordinator = db.Column(db.String(255))
    gyro_horizon = db.Column(db.String(255))
    compass = db.Column(db.String(255))
    tachometer = db.Column(db.String(255))
    fuel_gauge = db.Column(db.String(255))
    oil_pressure_gauge = db.Column(db.String(255))
    oil_temperature_gauge = db.Column(db.String(255))
    manifold_pressure_gauge = db.Column(db.String(255))
    engine_temperature_gauge = db.Column(db.String(255))
    vacuum_gauge = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class Brake(db.Model):
    __tablename__ = 'brakes'
    id = db.Column(db.Integer, primary_key=True)
    brake_type = db.Column(db.String(255))
    brake_material = db.Column(db.String(255))
    brake_size = db.Column(db.Integer)
    brake_pressure = db.Column(db.Integer)
    brake_system = db.Column(db.String(255))
    anti_skid_system = db.Column(db.String(255))
    parking_brake = db.Column(db.String(255))
    brake_lines = db.Column(db.String(255))
    brake_pads = db.Column(db.String(255))
    brake_fluid = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class ExhaustSystem(db.Model):
    __tablename__ = 'exhaust_systems'
    id = db.Column(db.Integer, primary_key=True)
    exhaust_type = db.Column(db.String(255))
    material = db.Column(db.String(255))
    exhaust_pipe_diameter = db.Column(db.Float)
    muffler_type = db.Column(db.String(255))
    heat_shields = db.Column(db.String(255))
    exhaust_gaskets = db.Column(db.String(255))
    exhaust_temperature = db.Column(db.Integer)
    exhaust_system_pressure = db.Column(db.Integer)
    exhaust_system_mounting = db.Column(db.String(255))
    emission_control = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class CoolingSystem(db.Model):
    __tablename__ = 'cooling_system'
    id = db.Column(db.Integer, primary_key=True)
    coolant_type = db.Column(db.String(255))
    radiator_size = db.Column(db.Integer)
    cooling_fan = db.Column(db.String(255))
    oil_cooler = db.Column(db.String(255))
    cooling_system_pressure = db.Column(db.Integer)
    thermostat = db.Column(db.String(255))
    temperature_gauge = db.Column(db.String(255))
    cooling_system_pumps = db.Column(db.String(255))
    coolant_capacity = db.Column(db.Float)
    airflow_management = db.Column(db.String(255))
    cooling_fins = db.Column(db.String(255))
    cooling_system_mounting = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class Powerplant(db.Model):
    __tablename__ = 'powerplant'
    id = db.Column(db.Integer, primary_key=True)
    engine_type = db.Column(db.String(255))
    engine_model = db.Column(db.String(255))
    horsepower = db.Column(db.Integer)
    rpm = db.Column(db.Integer)
    displacement = db.Column(db.Float)
    fuel_type = db.Column(db.String(255))
    compression_ratio = db.Column(db.Float)
    turbocharger = db.Column(db.String(255))
    intercooler = db.Column(db.String(255))
    fuel_injection = db.Column(db.String(255))
    ignition_system = db.Column(db.String(255))
    cooling_system = db.Column(db.String(255))
    exhaust_system = db.Column(db.String(255))
    oil_system = db.Column(db.String(255))
    power_output = db.Column(db.Float) 
    operating_temp = db.Column(db.Integer)
    weights = db.Column(db.Integer)
    maintenance_intervals = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))
