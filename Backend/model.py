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
    __tablename__ = 'engines'
    id = db.Column(db.Integer, primary_key=True)
    engine_type = db.Column(db.String(255))
    horsepower = db.Column(db.Integer)
    rpm = db.Column(db.Integer)
    displacement = db.Column(db.Float)
    fuel_type = db.Column(db.String(255))
    fuel_consumption = db.Column(db.Float)
    compression_ratio = db.Column(db.Float)
    torque = db.Column(db.Integer)
    egt = db.Column(db.Integer)
    cht = db.Column(db.Integer)
    oil_pressure = db.Column(db.Integer)
    oil_temperature = db.Column(db.Integer)
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class LandingGear(db.Model):
    __tablename__ = 'landing_gears'
    id = db.Column(db.Integer, primary_key=True)
    tire_type = db.Column(db.String(255))
    material = db.Column(db.String(255))
    shock_absorption = db.Column(db.String(255))
    tire_pressure = db.Column(db.Integer)
    retraction_system = db.Column(db.String(255))
    braking_system = db.Column(db.String(255))
    track_width = db.Column(db.Integer)
    tire_size = db.Column(db.Integer)
    weight_capacity = db.Column(db.Integer)
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class FuelSystem(db.Model):
    __tablename__ = 'fuel_systems'
    id = db.Column(db.Integer, primary_key=True)
    fuel_type = db.Column(db.String(255))
    tank_capacity = db.Column(db.Float)
    pump_type = db.Column(db.String(255))
    filter_type = db.Column(db.String(255))
    lines = db.Column(db.String(255))
    management = db.Column(db.String(255))
    gauges = db.Column(db.String(255))
    flow_rate = db.Column(db.Float)
    pressure = db.Column(db.Integer)
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class CockpitControl(db.Model):
    __tablename__ = 'cockpit_controls'
    id = db.Column(db.Integer, primary_key=True)
    control_yoke_stick = db.Column(db.String(255))
    throttle = db.Column(db.String(255))
    rudder_pedals = db.Column(db.String(255))
    trim_controls = db.Column(db.String(255))
    flap_controls = db.Column(db.String(255))
    autopilot = db.Column(db.String(255))
    landing_gear_controls = db.Column(db.String(255))
    radio_panel = db.Column(db.String(255))
    instrument_panel = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class Avionic(db.Model):
    __tablename__ = 'avionics'
    id = db.Column(db.Integer, primary_key=True)
    gps = db.Column(db.String(255))
    nav_com_radios = db.Column(db.String(255))
    transponder = db.Column(db.String(255))
    weather_radar = db.Column(db.String(255))
    autopilot = db.Column(db.String(255))
    electronic_display = db.Column(db.String(255))
    engine_monitoring = db.Column(db.String(255))
    flight_management_system = db.Column(db.String(255))
    collision_avoidance = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class ElectricalSystem(db.Model):
    __tablename__ = 'electrical_systems'
    id = db.Column(db.Integer, primary_key=True)
    battery_type = db.Column(db.String(255))
    battery_capacity = db.Column(db.Float)
    alternator_generator = db.Column(db.String(255))
    circuit_breakers = db.Column(db.String(255))
    bus_system = db.Column(db.String(255))
    lighting_system = db.Column(db.String(255))
    wiring = db.Column(db.String(255))
    power_supply = db.Column(db.String(255))
    load_capacity = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class FlightInstrument(db.Model):
    __tablename__ = 'flight_instruments'
    id = db.Column(db.Integer, primary_key=True)
    airspeed_indicator = db.Column(db.String(255))
    altimeter = db.Column(db.String(255))
    attitude_indicator = db.Column(db.String(255))
    heading_indicator = db.Column(db.String(255))
    vertical_speed_indicator = db.Column(db.String(255))
    turn_coordinator = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class Brake(db.Model):
    __tablename__ = 'brakes'
    id = db.Column(db.Integer, primary_key=True)
    brake_type = db.Column(db.String(255))
    material = db.Column(db.String(255))
    size = db.Column(db.Integer)
    pressure = db.Column(db.Integer)
    system_type = db.Column(db.String(255))
    anti_skid = db.Column(db.String(255))
    parking_brake = db.Column(db.String(255))
    brake_lines = db.Column(db.String(255))
    brake_pads = db.Column(db.String(255))
    fluid_type = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class ExhaustSystem(db.Model):
    __tablename__ = 'exhaust_systems'
    id = db.Column(db.Integer, primary_key=True)
    exhaust_type = db.Column(db.String(255))
    material = db.Column(db.String(255))
    pipe_diameter = db.Column(db.Float)
    muffler_type = db.Column(db.String(255))
    heat_shields = db.Column(db.String(255))
    gaskets = db.Column(db.String(255))
    temperature = db.Column(db.Integer)
    pressure = db.Column(db.Integer)
    mounting = db.Column(db.String(255))
    emission_control = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class CoolingSystem(db.Model):
    __tablename__ = 'cooling_systems'
    id = db.Column(db.Integer, primary_key=True)
    cooling_type = db.Column(db.String(255))
    coolant_type = db.Column(db.String(255))
    radiator_size = db.Column(db.Integer)
    fan_type = db.Column(db.String(255))
    oil_cooler = db.Column(db.String(255))
    system_pressure = db.Column(db.Integer)
    thermostat = db.Column(db.String(255))
    temperature_gauge = db.Column(db.String(255))
    pumps = db.Column(db.String(255))
    coolant_capacity = db.Column(db.Float)
    airflow_management = db.Column(db.String(255))
    fins = db.Column(db.String(255))
    mounting = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))

class Powerplant(db.Model):
    __tablename__ = 'powerplants'
    id = db.Column(db.Integer, primary_key=True)
    engine_type = db.Column(db.String(255))
    fuel_type = db.Column(db.String(255))
    cooling_system = db.Column(db.String(255))
    exhaust_system = db.Column(db.String(255))
    ignition_system = db.Column(db.String(255))
    power_output = db.Column(db.Integer)
    thrust = db.Column(db.Integer)
    mounting = db.Column(db.String(255))
    model_id = db.Column(db.Integer, db.ForeignKey('airplane_models.model_id', ondelete='CASCADE'))
