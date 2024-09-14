from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserPlane(db.Model):
    __tablename__ = 'user_plane'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    plane_name = db.Column(db.String(255))
    plane_type = db.Column(db.String(255))
    manufacturer_id = db.Column(db.Integer, db.ForeignKey('manufacturer.id'))

    manufacturer = db.relationship('Manufacturer', backref='planes', lazy=True)
    airframe_parts = db.relationship('AirframeParts', backref='plane', lazy=True)
    engine = db.relationship('Engine', backref='plane', lazy=True)
    landing_gear = db.relationship('LandingGear', backref='plane', lazy=True)
    fuel_system = db.relationship('FuelSystem', backref='plane', lazy=True)
    cockpit_controls = db.relationship('CockpitControls', backref='plane', lazy=True)
    avionics = db.relationship('Avionics', backref='plane', lazy=True)
    electrical_system = db.relationship('ElectricalSystem', backref='plane', lazy=True)
    flight_instruments = db.relationship('FlightInstruments', backref='plane', lazy=True)
    brakes = db.relationship('Brakes', backref='plane', lazy=True)
    exhaust_system = db.relationship('ExhaustSystem', backref='plane', lazy=True)
    cooling_system = db.relationship('CoolingSystem', backref='plane', lazy=True)
    powerplant = db.relationship('Powerplant', backref='plane', lazy=True)

class Manufacturer(db.Model):
    __tablename__ = 'manufacturer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

class AirframeParts(db.Model):
    __tablename__ = 'airframe_parts'
    id = db.Column(db.Integer, primary_key=True)
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'))
    part_name = db.Column(db.String(255))

class Engine(db.Model):
    __tablename__ = 'engine'
    id = db.Column(db.Integer, primary_key=True)
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'))
    engine_type = db.Column(db.String(255))

class LandingGear(db.Model):
    __tablename__ = 'landing_gear'
    id = db.Column(db.Integer, primary_key=True)
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'))
    gear_type = db.Column(db.String(255))

class FuelSystem(db.Model):
    __tablename__ = 'fuel_system'
    id = db.Column(db.Integer, primary_key=True)
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'))
    system_type = db.Column(db.String(255))

class CockpitControls(db.Model):
    __tablename__ = 'cockpit_controls'
    id = db.Column(db.Integer, primary_key=True)
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'))
    control_type = db.Column(db.String(255))

class Avionics(db.Model):
    __tablename__ = 'avionics'
    id = db.Column(db.Integer, primary_key=True)
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'))
    avionics_type = db.Column(db.String(255))

class ElectricalSystem(db.Model):
    __tablename__ = 'electrical_system'
    id = db.Column(db.Integer, primary_key=True)
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'))
    system_type = db.Column(db.String(255))

class FlightInstruments(db.Model):
    __tablename__ = 'flight_instruments'
    id = db.Column(db.Integer, primary_key=True)
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'))
    instrument_name = db.Column(db.String(255))

class Brakes(db.Model):
    __tablename__ = 'brakes'
    id = db.Column(db.Integer, primary_key=True)
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'))
    brake_type = db.Column(db.String(255))

class ExhaustSystem(db.Model):
    __tablename__ = 'exhaust_system'
    id = db.Column(db.Integer, primary_key=True)
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'))
    system_type = db.Column(db.String(255))

class CoolingSystem(db.Model):
    __tablename__ = 'cooling_system'
    id = db.Column(db.Integer, primary_key=True)
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'))
    cooling_type = db.Column(db.String(255))

class Powerplant(db.Model):
    __tablename__ = 'powerplant'
    id = db.Column(db.Integer, primary_key=True)
    plane_id = db.Column(db.Integer, db.ForeignKey('user_plane.id'))
    mount_type = db.Column(db.String(255))
