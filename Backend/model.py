from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'userid'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    profile = db.Column(db.String(255))
    password = db.Column(db.String(255))

class Manufacturer(db.Model):
    __tablename__ = 'manufacturer'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))

class UserPlane(db.Model):
    __tablename__ = 'user_plane'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    plane_name = db.Column(db.String(255))
    plane_type = db.Column(db.String(255))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'))
    manufacturer = db.relationship('Manufacturer', backref=db.backref('planes', lazy=True))

class Engine(db.Model):
    __tablename__ = 'engine'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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

class LandingGear(db.Model):
    __tablename__ = 'landing_gear'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tire_type = db.Column(db.String(255))
    material = db.Column(db.String(255))
    shock_absorption = db.Column(db.String(255))
    tire_pressure = db.Column(db.Integer)
    retraction_system = db.Column(db.String(255))
    braking_system = db.Column(db.String(255))
    track_width = db.Column(db.Integer)
    tire_size = db.Column(db.Integer)
    weight_capacity = db.Column(db.Integer)

class FuelSystem(db.Model):
    __tablename__ = 'fuel_system'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fuel_type = db.Column(db.String(255))
    fuel_tank_capacity = db.Column(db.Float)
    fuel_pump_type = db.Column(db.String(255))
    fuel_filter = db.Column(db.String(255))
    fuel_lines = db.Column(db.String(255))
    fuel_management = db.Column(db.String(255))
    fuel_gauges = db.Column(db.String(255))
    fuel_flow_rate = db.Column(db.Float)
    fuel_pressure = db.Column(db.Integer)

class CockpitControls(db.Model):
    __tablename__ = 'cockpit_controls'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    control_yoke_stick = db.Column(db.String(255))
    throttle = db.Column(db.String(255))
    rudder_pedals = db.Column(db.String(255))
    trim_controls = db.Column(db.String(255))
    flap_controls = db.Column(db.String(255))
    autopilot = db.Column(db.String(255))
    landing_gear_controls = db.Column(db.String(255))
    radio_panel = db.Column(db.String(255))
    instrument_panel = db.Column(db.String(255))

class Avionics(db.Model):
    __tablename__ = 'avionics'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gps = db.Column(db.String(255))
    nav_com_radios = db.Column(db.String(255))
    transponder = db.Column(db.String(255))
    weather_radar = db.Column(db.String(255))
    autopilot = db.Column(db.String(255))
    electronic_flight_display = db.Column(db.String(255))
    engine_monitoring = db.Column(db.String(255))
    flight_management_system = db.Column(db.String(255))
    collision_avoidance_system = db.Column(db.String(255))

class ElectricalSystem(db.Model):
    __tablename__ = 'electrical_system'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    battery_type = db.Column(db.String(255))
    battery_capacity = db.Column(db.Float)
    alternator_generator = db.Column(db.String(255))
    circuit_breakers = db.Column(db.String(255))
    electrical_bus = db.Column(db.String(255))
    lighting_system = db.Column(db.String(255))
    electrical_wiring = db.Column(db.String(255))
    avionics_power_supply = db.Column(db.String(255))
    electrical_load = db.Column(db.String(255))

class FlightInstruments(db.Model):
    __tablename__ = 'flight_instruments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    airspeed_indicator = db.Column(db.String(255))
    altimeter = db.Column(db.String(255))
    attitude_indicator = db.Column(db.String(255))
    heading_indicator = db.Column(db.String(255))
    vertical_speed_indicator = db.Column(db.String(255))
    turn_coordinator = db.Column(db.String(255))

class Brakes(db.Model):
    __tablename__ = 'brakes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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

class ExhaustSystem(db.Model):
    __tablename__ = 'exhaust_system'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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

class CoolingSystem(db.Model):
    __tablename__ = 'cooling_system'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cooling_type = db.Column(db.String(255))
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

class Powerplant(db.Model):
    __tablename__ = 'powerplant'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
    operating_temperature = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    maintenance_intervals = db.Column(db.String(255))

class PlaneEngine(db.Model):
    __tablename__ = 'plane_engine'
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'), primary_key=True)
    engine_id = db.Column(db.Integer, db.ForeignKey('engine.id'), primary_key=True)

class PlaneLandingGear(db.Model):
    __tablename__ = 'plane_landing_gear'
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'), primary_key=True)
    landing_gear_id = db.Column(db.Integer, db.ForeignKey('landing_gear.id'), primary_key=True)

class PlaneFuelSystem(db.Model):
    __tablename__ = 'plane_fuel_system'
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'), primary_key=True)
    fuel_system_id = db.Column(db.Integer, db.ForeignKey('fuel_system.id'), primary_key=True)

class PlaneCockpitControls(db.Model):
    __tablename__ = 'plane_cockpit_controls'
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'), primary_key=True)
    cockpit_control_id = db.Column(db.Integer, db.ForeignKey('cockpit_controls.id'), primary_key=True)

class PlaneAvionics(db.Model):
    __tablename__ = 'plane_avionics'
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'), primary_key=True)
    avionics_id = db.Column(db.Integer, db.ForeignKey('avionics.id'), primary_key=True)

class PlaneElectricalSystem(db.Model):
    __tablename__ = 'plane_electrical_system'
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'), primary_key=True)
    electrical_system_id = db.Column(db.Integer, db.ForeignKey('electrical_system.id'), primary_key=True)

class PlaneFlightInstruments(db.Model):
    __tablename__ = 'plane_flight_instruments'
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'), primary_key=True)
    flight_instrument_id = db.Column(db.Integer, db.ForeignKey('flight_instruments.id'), primary_key=True)

class PlaneBrakes(db.Model):
    __tablename__ = 'plane_brakes'
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'), primary_key=True)
    brake_id = db.Column(db.Integer, db.ForeignKey('brakes.id'), primary_key=True)

class PlaneExhaustSystem(db.Model):
    __tablename__ = 'plane_exhaust_system'
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'), primary_key=True)
    exhaust_system_id = db.Column(db.Integer, db.ForeignKey('exhaust_system.id'), primary_key=True)

class PlaneCoolingSystem(db.Model):
    __tablename__ = 'plane_cooling_system'
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'), primary_key=True)
    cooling_system_id = db.Column(db.Integer, db.ForeignKey('cooling_system.id'), primary_key=True)

class PlanePowerplant(db.Model):
    __tablename__ = 'plane_powerplant'
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'), primary_key=True)
    powerplant_id = db.Column(db.Integer, db.ForeignKey('powerplant.id'), primary_key=True)
