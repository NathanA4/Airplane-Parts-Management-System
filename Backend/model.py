from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    profile = db.Column(db.String(255))
    password = db.Column(db.String(255), nullable=False)

    engines = db.relationship('Engine', backref='users', lazy=True)

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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            "Type": self.engine_type,
            "Horsepower": self.horsepower,
            "Rpm": self.rpm,
            "Displacement": self.displacement,
            "Fuel Type": self.fuel_type_avgas,
            "Fuel Consumption": self.fuel_consumption,
            "Compression Ratio": self.compression_ratio,
            "Torque": self.torque,
            "Egt": self.egt,
            "Cht": self.cht,
            "Oil Pressure": self.oil_pressure,
            "Oil Temperature": self.oil_temperature,
            "Retrived ID": self.user_id,
        }

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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            "Tire Type": self.tire_type,
            "Material": self.material,
            "Shock Absorption": self.shock_absorption,
            "Tire Pressure": self.tire_pressure,
            "Retraction System": self.retraction_system,
            "Braking System": self.braking_system,
            "Track Width": self.track_width,
            "Tire Size": self.tire_size,
            "Weight Capacity": self.weight_capacity,
            "Retrieved ID": self.user_id,
        }


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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            "Fuel Tank Capacity": self.fuel_tank_capacity,
            "Fuel Type": self.fuel_type,
            "Fuel Delivery System": self.fuel_delivery_system,
            "Fuel Pressure": self.fuel_pressure,
            "Fuel Pump": self.fuel_pump,
            "Fuel Lines": self.fuel_lines,
            "Fuel Filter": self.fuel_filter,
            "Fuel Value": self.fuel_value,
            "Fuel Flow": self.fuel_flow,
            "Retrived ID": self.user_id,
        }

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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            "Control Yoke Stick": self.control_yoke_stick,
            "Throttle": self.throttle,
            "Rudder Pedals": self.rudder_pedals,
            "Trim Controls": self.trim_controls,
            "Flap Controls": self.flap_controls,
            "Autopilots": self.autopilots,
            "Landing Gear Controls": self.landing_gear_controls,
            "Radio Panel": self.radio_panel,
            "Instrument Panel": self.instrument_panel,
            "Retrived ID": self.user_id,
        }

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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            "Gps": self.gps,
            "Nav Com Radios": self.nav_com_radios,
            "Adf": self.adf,
            "Vor": self.vor,
            "Dme": self.dme,
            "Transponder": self.transponder,
            "Elt": self.elt,
            "Ads_b": self.ads_b,
            "Weather Radar": self.weather_radar,
            "Autopilot System": self.autopilot_system,
            "Flight Director": self.flight_director,
            "Tcas": self.tcas,
            "Transponder Mode": self.transponder_mode,
            "Retrived ID": self.user_id,
        }

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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            "Battery Capacity": self.battery_capacity,
            "Alternator Rating (Amps)": self.alternator_rating_amps,
            "System Voltage": self.system_voltage,
            "Wiring Type": self.wiring_type,
            "Circuit Breakers": self.circuit_breakers,
            "Electrical Buses": self.electrical_buses,
            "Master Switch": self.master_switch,
            "Generator Output (Amps)": self.generator_output_amps,
            "Inverters": self.inverters,
            "Power Outlets": self.power_outlets,
            "Light System": self.light_system,
            "APS": self.aps,
            "Battery Type": self.battery_type,
            "Backup Battery": self.backup_battery,
            "Electrical Monitoring": self.electrical_monitoring,
            "Retrived ID": self.user_id,
        }


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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            "Altimeter": self.altimeter,
            "Airspeed Indicator": self.airspeed_indicator,
            "Heading Indicator": self.heading_indicator,
            "Vertical Speed Indicator": self.vertical_speed_indicator,
            "Turn Coordinator": self.turn_coordinator,
            "Gyro Horizon": self.gyro_horizon,
            "Compass": self.compass,
            "Tachometer": self.tachometer,
            "Fuel Gauge": self.fuel_gauge,
            "Oil Pressure Gauge": self.oil_pressure_gauge,
            "Oil Temperature Gauge": self.oil_temperature_gauge,
            "Manifold Pressure Gauge": self.manifold_pressure_gauge,
            "Engine Temperature Gauge": self.engine_temperature_gauge,
            "Vacuum Gauge": self.vacuum_gauge,
            "Retrived ID": self.user_id,
        }


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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            "Brake Type": self.brake_type,
            "Brake Material": self.brake_material,
            "Brake Size": self.brake_size,
            "Brake Pressure": self.brake_pressure,
            "Brake System": self.brake_system,
            "Anti-skid System": self.anti_skid_system,
            "Parking Brake": self.parking_brake,
            "Brake Lines": self.brake_lines,
            "Brake Pads": self.brake_pads,
            "Brake Fluid": self.brake_fluid,
            "Retrived ID": self.user_id,
        }


class ExhaustSystem(db.Model):
    __tablename__ = 'exhaust_system'
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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    def to_dict(self):
        return {
            "Exhaust Type": self.exhaust_type,
            "Material": self.material,
            "Exhaust Pipe Diameter": self.exhaust_pipe_diameter,
            "Muffler Type": self.muffler_type,
            "Heat Shields": self.heat_shields,
            "Exhaust Gaskets": self.exhaust_gaskets,
            "Exhaust Temperature": self.exhaust_temperature,
            "Exhaust System Pressure": self.exhaust_system_pressure,
            "Exhaust System Mounting": self.exhaust_system_mounting,
            "Emission Control": self.emission_control,
            "Retrived ID": self.user_id,
        }


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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            "Coolant Type": self.coolant_type,
            "Radiator Size": self.radiator_size,
            "Cooling Fan": self.cooling_fan,
            "Oil Cooler": self.oil_cooler,
            "Cooling System Pressure": self.cooling_system_pressure,
            "Thermostat": self.thermostat,
            "Temperature Gauge": self.temperature_gauge,
            "Cooling System Pumps": self.cooling_system_pumps,
            "Coolant Capacity": self.coolant_capacity,
            "Airflow Management": self.airflow_management,
            "Cooling Fins": self.cooling_fins,
            "Cooling System Mounting": self.cooling_system_mounting,
            "Retrived ID": self.user_id,
        }


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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        return {
            "Engine Type": self.engine_type,
            "Engine Model": self.engine_model,
            "Horsepower": self.horsepower,
            "RPM": self.rpm,
            "Displacement": self.displacement,
            "Fuel Type": self.fuel_type,
            "Compression Ratio": self.compression_ratio,
            "Turbocharger": self.turbocharger,
            "Intercooler": self.intercooler,
            "Fuel Injection": self.fuel_injection,
            "Ignition System": self.ignition_system,
            "Cooling System": self.cooling_system,
            "Exhaust System": self.exhaust_system,
            "Oil System": self.oil_system,
            "Power Output": self.power_output,
            "Operating Temperature": self.operating_temp,
            "Weights": self.weights,
            "Maintenance Intervals": self.maintenance_intervals,
            "Retrived ID": self.user_id,
        }
