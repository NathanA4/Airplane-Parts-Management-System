from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Manufacturer(Base):
    __tablename__ = 'manufacturer'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    
    planes = relationship('UserPlane', backref='manufacturer')

class UserPlane(Base):
    __tablename__ = 'user_plane'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    plane_name = Column(String(255))
    plane_type = Column(String(255))
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'))

    engines = relationship('Engine', secondary='plane_engine', backref='planes')
    landing_gears = relationship('LandingGear', secondary='plane_landing_gear', backref='planes')
    fuel_systems = relationship('FuelSystem', secondary='plane_fuel_system', backref='planes')
    cockpit_controls = relationship('CockpitControls', secondary='plane_cockpit_controls', backref='planes')
    avionics = relationship('Avionics', secondary='plane_avionics', backref='planes')
    electrical_systems = relationship('ElectricalSystem', secondary='plane_electrical_system', backref='planes')
    flight_instruments = relationship('FlightInstruments', secondary='plane_flight_instruments', backref='planes')
    brakes = relationship('Brakes', secondary='plane_brakes', backref='planes')
    exhaust_systems = relationship('ExhaustSystem', secondary='plane_exhaust_system', backref='planes')
    cooling_systems = relationship('CoolingSystem', secondary='plane_cooling_system', backref='planes')
    powerplants = relationship('Powerplant', secondary='plane_powerplant', backref='planes')

class Engine(Base):
    __tablename__ = 'engine'
    id = Column(Integer, primary_key=True, autoincrement=True)
    engine_type = Column(String(255))
    horsepower = Column(Integer)
    rpm = Column(Integer)
    displacement = Column(Float)
    fuel_type_avgas = Column(String(255))
    fuel_consumption = Column(Float)
    compression_ratio = Column(Float)
    torque = Column(Integer)
    egt = Column(Integer)
    cht = Column(Integer)
    oil_pressure = Column(Integer)
    oil_temperature = Column(Integer)

class LandingGear(Base):
    __tablename__ = 'landing_gear'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tire_type = Column(String(255))
    material = Column(String(255))
    shock_absorption = Column(String(255))
    tire_pressure = Column(Integer)
    retraction_system = Column(String(255))
    braking_system = Column(String(255))
    track_width = Column(Integer)
    tire_size = Column(Integer)
    weight_capacity = Column(Integer)

class FuelSystem(Base):
    __tablename__ = 'fuel_system'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fuel_type = Column(String(255))
    fuel_tank_capacity = Column(Float)
    fuel_pump_type = Column(String(255))
    fuel_filter = Column(String(255))
    fuel_lines = Column(String(255))
    fuel_management = Column(String(255))
    fuel_gauges = Column(String(255))
    fuel_flow_rate = Column(Float)
    fuel_pressure = Column(Integer)

class CockpitControls(Base):
    __tablename__ = 'cockpit_controls'
    id = Column(Integer, primary_key=True, autoincrement=True)
    control_yoke_stick = Column(String(255))
    throttle = Column(String(255))
    rudder_pedals = Column(String(255))
    trim_controls = Column(String(255))
    flap_controls = Column(String(255))
    autopilot = Column(String(255))
    landing_gear_controls = Column(String(255))
    radio_panel = Column(String(255))
    instrument_panel = Column(String(255))

class Avionics(Base):
    __tablename__ = 'avionics'
    id = Column(Integer, primary_key=True, autoincrement=True)
    gps = Column(String(255))
    nav_com_radios = Column(String(255))
    transponder = Column(String(255))
    weather_radar = Column(String(255))
    autopilot = Column(String(255))
    electronic_flight_display = Column(String(255))
    engine_monitoring = Column(String(255))
    flight_management_system = Column(String(255))
    collision_avoidance_system = Column(String(255))

class ElectricalSystem(Base):
    __tablename__ = 'electrical_system'
    id = Column(Integer, primary_key=True, autoincrement=True)
    battery_type = Column(String(255))
    battery_capacity = Column(Float)
    alternator_generator = Column(String(255))
    circuit_breakers = Column(String(255))
    electrical_bus = Column(String(255))
    lighting_system = Column(String(255))
    electrical_wiring = Column(String(255))
    avionics_power_supply = Column(String(255))
    electrical_load = Column(String(255))

class FlightInstruments(Base):
    __tablename__ = 'flight_instruments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    airspeed_indicator = Column(String(255))
    altimeter = Column(String(255))
    attitude_indicator = Column(String(255))
    heading_indicator = Column(String(255))
    vertical_speed_indicator = Column(String(255))
    turn_coordinator = Column(String(255))

class Brakes(Base):
    __tablename__ = 'brakes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    brake_type = Column(String(255))
    brake_material = Column(String(255))
    brake_size = Column(Integer)
    brake_pressure = Column(Integer)
    brake_system = Column(String(255))
    anti_skid_system = Column(String(255))
    parking_brake = Column(String(255))
    brake_lines = Column(String(255))
    brake_pads = Column(String(255))
    brake_fluid = Column(String(255))

class ExhaustSystem(Base):
    __tablename__ = 'exhaust_system'
    id = Column(Integer, primary_key=True, autoincrement=True)
    exhaust_type = Column(String(255))
    material = Column(String(255))
    exhaust_pipe_diameter = Column(Float)
    muffler_type = Column(String(255))
    heat_shields = Column(String(255))
    exhaust_gaskets = Column(String(255))
    exhaust_temperature = Column(Integer)
    exhaust_system_pressure = Column(Integer)
    exhaust_system_mounting = Column(String(255))
    emission_control = Column(String(255))

class CoolingSystem(Base):
    __tablename__ = 'cooling_system'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cooling_type = Column(String(255))
    coolant_type = Column(String(255))
    radiator_size = Column(Integer)
    cooling_fan = Column(String(255))
    oil_cooler = Column(String(255))
    cooling_system_pressure = Column(Integer)
    thermostat = Column(String(255))
    temperature_gauge = Column(String(255))
    cooling_system_pumps = Column(String(255))
    coolant_capacity = Column(Float)
    airflow_management = Column(String(255))
    cooling_fins = Column(String(255))
    cooling_system_mounting = Column(String(255))

class Powerplant(Base):
    __tablename__ = 'powerplant'
    id = Column(Integer, primary_key=True, autoincrement=True)
    engine_type = Column(String(255))
    engine_model = Column(String(255))
    horsepower = Column(Integer)
    rpm = Column(Integer)
    displacement = Column(Float)
    fuel_type = Column(String(255))
    compression_ratio = Column(Float)
    turbocharger = Column(String(255))
    intercooler = Column(String(255))
    fuel_injection = Column(String(255))
    ignition_system = Column(String(255))
    cooling_system = Column(String(255))
    exhaust_system = Column(String(255))
    oil_system = Column(String(255))
    power_output = Column(Float)
    operating_temperature = Column(Integer)
    weight = Column(Integer)
    maintenance_intervals = Column(String(255))

# Junction tables
class PlaneEngine(Base):
    __tablename__ = 'plane_engine'
    plane_id = Column(Integer, ForeignKey('user_plane.id'), primary_key=True)
    engine_id = Column(Integer, ForeignKey('engine.id'), primary_key=True)

class PlaneLandingGear(Base):
    __tablename__ = 'plane_landing_gear'
    plane_id = Column(Integer, ForeignKey('user_plane.id'), primary_key=True)
    landing_gear_id = Column(Integer, ForeignKey('landing_gear.id'), primary_key=True)

class PlaneFuelSystem(Base):
    __tablename__ = 'plane_fuel_system'
    plane_id = Column(Integer, ForeignKey('user_plane.id'), primary_key=True)
    fuel_system_id = Column(Integer, ForeignKey('fuel_system.id'), primary_key=True)

class PlaneCockpitControls(Base):
    __tablename__ = 'plane_cockpit_controls'
    plane_id = Column(Integer, ForeignKey('user_plane.id'), primary_key=True)
    cockpit_controls_id = Column(Integer, ForeignKey('cockpit_controls.id'), primary_key=True)

class PlaneAvionics(Base):
    __tablename__ = 'plane_avionics'
    plane_id = Column(Integer, ForeignKey('user_plane.id'), primary_key=True)
    avionics_id = Column(Integer, ForeignKey('avionics.id'), primary_key=True)

class PlaneElectricalSystem(Base):
    __tablename__ = 'plane_electrical_system'
    plane_id = Column(Integer, ForeignKey('user_plane.id'), primary_key=True)
    electrical_system_id = Column(Integer, ForeignKey('electrical_system.id'), primary_key=True)

class PlaneFlightInstruments(Base):
    __tablename__ = 'plane_flight_instruments'
    plane_id = Column(Integer, ForeignKey('user_plane.id'), primary_key=True)
    flight_instruments_id = Column(Integer, ForeignKey('flight_instruments.id'), primary_key=True)

class PlaneBrakes(Base):
    __tablename__ = 'plane_brakes'
    plane_id = Column(Integer, ForeignKey('user_plane.id'), primary_key=True)
    brakes_id = Column(Integer, ForeignKey('brakes.id'), primary_key=True)

class PlaneExhaustSystem(Base):
    __tablename__ = 'plane_exhaust_system'
    plane_id = Column(Integer, ForeignKey('user_plane.id'), primary_key=True)
    exhaust_system_id = Column(Integer, ForeignKey('exhaust_system.id'), primary_key=True)

class PlaneCoolingSystem(Base):
    __tablename__ = 'plane_cooling_system'
    plane_id = Column(Integer, ForeignKey('user_plane.id'), primary_key=True)
    cooling_system_id = Column(Integer, ForeignKey('cooling_system.id'), primary_key=True)

class PlanePowerplant(Base):
    __tablename__ = 'plane_powerplant'
    plane_id = Column(Integer, ForeignKey('user_plane.id'), primary_key=True)
    powerplant_id = Column(Integer, ForeignKey('powerplant.id'), primary_key=True)

