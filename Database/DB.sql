CREATE DATABASE Airplane_System;
USE Airplane_System;
CREATE TABLE userid(
    id INt PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255),
    email VARCHAR(255),
    profile VARCHAR(255),
    password VARCHAR(255)
);
CREATE TABLE manufacturer (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255)
);
CREATE TABLE user_plane (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    plane_name VARCHAR(255),
    plane_type VARCHAR(255),
    manufacturer_id INT,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(id)
);
CREATE TABLE engine (
    id INT PRIMARY KEY AUTO_INCREMENT,
    engine_type VARCHAR(255),
    horsepower INT,
    rpm INT,
    displacement FLOAT,
    fuel_type_avgas VARCHAR(255),
    fuel_consumption FLOAT,
    compression_ratio FLOAT,
    torque INT,
    egt INT,
    cht INT,
    oil_pressure INT,
    oil_temperature INT
);
CREATE TABLE landing_gear (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tire_type VARCHAR(255),
    material VARCHAR(255),
    7 shock_absorption VARCHAR(255),
    tire_pressure INT,
    retraction_system VARCHAR(255),
    braking_system VARCHAR(255),
    track_width INT,
    tire_size INT,
    weight_capacity INT
);
CREATE TABLE fuel_system (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fuel_type VARCHAR(255),
    fuel_tank_capacity FLOAT,
    fuel_pump_type VARCHAR(255),
    fuel_filter VARCHAR(255),
    fuel_lines VARCHAR(255),
    fuel_management VARCHAR(255),
    fuel_gauges VARCHAR(255),
    fuel_flow_rate FLOAT,
    fuel_pressure INT
);
CREATE TABLE cockpit_controls (
    id INT PRIMARY KEY AUTO_INCREMENT,
    control_yoke_stick VARCHAR(255),
    throttle VARCHAR(255),
    rudder_pedals VARCHAR(255),
    trim_controls VARCHAR(255),
    flap_controls VARCHAR(255),
    autopilot VARCHAR(255),
    landing_gear_controls VARCHAR(255),
    radio_panel VARCHAR(255),
    instrument_panel VARCHAR(255)
);
CREATE TABLE avionics (
    id INT PRIMARY KEY AUTO_INCREMENT,
    gps VARCHAR(255),
    nav_com_radios VARCHAR(255),
    transponder VARCHAR(255),
    weather_radar VARCHAR(255),
    autopilot VARCHAR(255),
    electronic_flight_display VARCHAR(255),
    engine_monitoring VARCHAR(255),
    flight_management_system VARCHAR(255),
    collision_avoidance_system VARCHAR(255)
);
CREATE TABLE electrical_system (
    id INT PRIMARY KEY AUTO_INCREMENT,
    battery_type VARCHAR(255),
    battery_capacity FLOAT,
    alternator_generator VARCHAR(255),
    circuit_breakers VARCHAR(255),
    electrical_bus VARCHAR(255),
    lighting_system VARCHAR(255),
    electrical_wiring VARCHAR(255),
    avionics_power_supply VARCHAR(255),
    electrical_load VARCHAR(255)
);
CREATE TABLE flight_instruments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    airspeed_indicator VARCHAR(255),
    altimeter VARCHAR(255),
    attitude_indicator VARCHAR(255),
    heading_indicator VARCHAR(255),
    vertical_speed_indicator VARCHAR(255),
    turn_coordinator VARCHAR(255)
);
CREATE TABLE brakes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    brake_type VARCHAR(255),
    brake_material VARCHAR(255),
    brake_size INT,
    brake_pressure INT,
    brake_system VARCHAR(255),
    anti_skid_system VARCHAR(255),
    parking_brake VARCHAR(255),
    brake_lines VARCHAR(255),
    brake_pads VARCHAR(255),
    brake_fluid VARCHAR(255)
);
CREATE TABLE exhaust_system (
    id INT PRIMARY KEY AUTO_INCREMENT,
    exhaust_type VARCHAR(255),
    material VARCHAR(255),
    exhaust_pipe_diameter FLOAT,
    muffler_type VARCHAR(255),
    heat_shields VARCHAR(255),
    exhaust_gaskets VARCHAR(255),
    exhaust_temperature INT,
    exhaust_system_pressure INT,
    exhaust_system_mounting VARCHAR(255),
    emission_control VARCHAR(255)
);
CREATE TABLE cooling_system (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cooling_type VARCHAR(255),
    coolant_type VARCHAR(255),
    radiator_size INT,
    cooling_fan VARCHAR(255),
    oil_cooler VARCHAR(255),
    cooling_system_pressure INT,
    thermostat VARCHAR(255),
    temperature_gauge VARCHAR(255),
    cooling_system_pumps VARCHAR(255),
    coolant_capacity FLOAT,
    airflow_management VARCHAR(255),
    cooling_fins VARCHAR(255),
    cooling_system_mounting VARCHAR(255)
);
CREATE TABLE powerplant (
    id INT PRIMARY KEY AUTO_INCREMENT,
    engine_type VARCHAR(255),
    engine_model VARCHAR(255),
    horsepower INT,
    rpm INT,
    displacement FLOAT,
    fuel_type VARCHAR(255),
    compression_ratio FLOAT,
    turbocharger VARCHAR(255),
    intercooler VARCHAR(255),
    fuel_injection VARCHAR(255),
    ignition_system VARCHAR(255),
    cooling_system VARCHAR(255),
    exhaust_system VARCHAR(255),
    oil_system VARCHAR(255),
    power_output FLOAT,
    operating_temperature INT,
    weight INT,
    maintenance_intervals VARCHAR(255)
);
-- Junction tables for many-to-many relationships
CREATE TABLE plane_engine (
    plane_id INT,
    engine_id INT,
    PRIMARY KEY (plane_id, engine_id),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id),
    FOREIGN KEY (engine_id) REFERENCES engine(id)
);
CREATE TABLE plane_landing_gear (
    plane_id INT,
    landing_gear_id INT,
    PRIMARY KEY (plane_id, landing_gear_id),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id),
    FOREIGN KEY (landing_gear_id) REFERENCES landing_gear(id)
);
CREATE TABLE plane_fuel_system (
    plane_id INT,
    fuel_system_id INT,
    PRIMARY KEY (plane_id, fuel_system_id),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id),
    FOREIGN KEY (fuel_system_id) REFERENCES fuel_system(id)
);
CREATE TABLE plane_cockpit_controls (
    plane_id INT,
    cockpit_controls_id INT,
    PRIMARY KEY (plane_id, cockpit_controls_id),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id),
    FOREIGN KEY (cockpit_controls_id) REFERENCES cockpit_controls(id)
);
CREATE TABLE plane_avionics (
    plane_id INT,
    avionics_id INT,
    PRIMARY KEY (plane_id, avionics_id),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id),
    FOREIGN KEY (avionics_id) REFERENCES avionics(id)
);
CREATE TABLE plane_electrical_system (
    plane_id INT,
    electrical_system_id INT,
    PRIMARY KEY (plane_id, electrical_system_id),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id),
    FOREIGN KEY (electrical_system_id) REFERENCES electrical_system(id)
);
CREATE TABLE plane_flight_instruments (
    plane_id INT,
    flight_instruments_id INT,
    PRIMARY KEY (plane_id, flight_instruments_id),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id),
    FOREIGN KEY (flight_instruments_id) REFERENCES flight_instruments(id)
);
CREATE TABLE plane_brakes (
    plane_id INT,
    brakes_id INT,
    PRIMARY KEY (plane_id, brakes_id),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id),
    FOREIGN KEY (brakes_id) REFERENCES brakes(id)
);
CREATE TABLE plane_exhaust_system (
    plane_id INT,
    exhaust_system_id INT,
    PRIMARY KEY (plane_id, exhaust_system_id),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id),
    FOREIGN KEY (exhaust_system_id) REFERENCES exhaust_system(id)
);
CREATE TABLE plane_cooling_system (
    plane_id INT,
    cooling_system_id INT,
    PRIMARY KEY (plane_id, cooling_system_id),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id),
    FOREIGN KEY (cooling_system_id) REFERENCES cooling_system(id)
);
CREATE TABLE plane_powerplant (
    plane_id INT,
    powerplant_id INT,
    PRIMARY KEY (plane_id, powerplant_id),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id),
    FOREIGN KEY (powerplant_id) REFERENCES powerplant(id)
);