CREATE DATABASE Airplane_System;
USE Airplane_System;
CREATE TABLE Users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    profile VARCHAR(255),
    password VARCHAR(255) NOT NULL
);
CREATE TABLE AirplaneModels (
    model_id INT PRIMARY KEY AUTO_INCREMENT,
    model_name VARCHAR(255) NOT NULL,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE
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
    oil_temperature INT,
    model_id INT,
    FOREIGN KEY (model_id) REFERENCES AirplaneModels(model_id) ON DELETE CASCADE
);
CREATE TABLE landing_gear (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tire_type VARCHAR(255),
    material VARCHAR(255),
    shock_absorption VARCHAR(255),
    tire_pressure INT,
    retraction_system VARCHAR(255),
    braking_system VARCHAR(255),
    track_width FLOAT,
    tire_size FLOAT,
    weight_capacity INT,
    model_id INT,
    FOREIGN KEY (model_id) REFERENCES AirplaneModels(model_id) ON DELETE CASCADE
);
CREATE TABLE fuel_system (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fuel_tank_capacity FLOAT,
    fuel_type VARCHAR(255),
    fuel_delivery_system VARCHAR(255),
    fuel_pressure INT,
    fuel_pump VARCHAR(255),
    fuel_lines VARCHAR(255),
    fuel_filter VARCHAR(255),
    fuel_value VARCHAR(255),
    fuel_flow FLOAT,
    fuel_venting_system VARCHAR(255),
    model_id INT,
    FOREIGN KEY (model_id) REFERENCES AirplaneModels(model_id) ON DELETE CASCADE
);
CREATE TABLE cockpit_controls (
    id INT PRIMARY KEY AUTO_INCREMENT,
    control_yoke_stick VARCHAR(255),
    throttle VARCHAR(255),
    rudder_pedals VARCHAR(255),
    trim_controls VARCHAR(255),
    flap_controls VARCHAR(255),
    autopilots VARCHAR(255),
    landing_gear_controls VARCHAR(255),
    radio_panel VARCHAR(255),
    instrument_panel VARCHAR(255),
    model_id INT,
    FOREIGN KEY (model_id) REFERENCES AirplaneModels(model_id) ON DELETE CASCADE
);
CREATE TABLE avionics (
    id INT PRIMARY KEY AUTO_INCREMENT,
    gps VARCHAR(255),
    nav_com_radios VARCHAR(255),
    adf VARCHAR(255),
    vor VARCHAR(255),
    dme VARCHAR(255),
    transponder VARCHAR(255),
    elt VARCHAR(255),
    ads_b VARCHAR(255),
    weather_radar VARCHAR(255),
    autopilot_system VARCHAR(255),
    flight_director VARCHAR(255),
    tcas VARCHAR(255),
    transponder_mode VARCHAR(255),
    model_id INT,
    FOREIGN KEY (model_id) REFERENCES AirplaneModels(model_id) ON DELETE CASCADE
);
CREATE TABLE electrical_system (
    id INT PRIMARY KEY AUTO_INCREMENT,
    battery_capacity INT,
    alternator_rating_amps INT,
    system_voltage INT,
    wiring_type VARCHAR(255),
    circuit_breakers VARCHAR(255),
    electrical_buses VARCHAR(255),
    master_switch VARCHAR(255),
    generator_output_amps INT,
    inverters VARCHAR(255),
    power_outlets VARCHAR(255),
    light_system VARCHAR(255),
    aps VARCHAR(255),
    battery_type VARCHAR(255),
    backup_battery VARCHAR(255),
    electrical_monitoring VARCHAR(255),
    model_id INT,
    FOREIGN KEY (model_id) REFERENCES AirplaneModels(model_id) ON DELETE CASCADE
);
CREATE TABLE flight_instruments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    altimeter VARCHAR(255),
    airspeed_indicator VARCHAR(255),
    heading_indicator VARCHAR(255),
    vertical_speed_indicator VARCHAR(255),
    turn_coordinator VARCHAR(255),
    gyro_horizon VARCHAR(255),
    compass VARCHAR(255),
    tachometer VARCHAR(255),
    fuel_gauge VARCHAR(255),
    oil_pressure_gauge VARCHAR(255),
    oil_temperature_gauge VARCHAR(255),
    manifold_pressure_gauge VARCHAR(255),
    engine_temperature_gauge VARCHAR(255),
    vacuum_gauge VARCHAR(255),
    model_id INT,
    FOREIGN KEY (model_id) REFERENCES AirplaneModels(model_id) ON DELETE CASCADE
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
    brake_fluid VARCHAR(255),
    model_id INT,
    FOREIGN KEY (model_id) REFERENCES AirplaneModels(model_id) ON DELETE CASCADE
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
    emission_control VARCHAR(255),
    model_id INT,
    FOREIGN KEY (model_id) REFERENCES AirplaneModels(model_id) ON DELETE CASCADE
);
CREATE TABLE cooling_system (
    id INT PRIMARY KEY AUTO_INCREMENT,
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
    cooling_system_mounting VARCHAR(255),
    model_id INT,
    FOREIGN KEY (model_id) REFERENCES AirplaneModels(model_id) ON DELETE CASCADE
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
    operating_temp INT,
    weights INT,
    maintenance_intervals VARCHAR(255),
    model_id INT,
    FOREIGN KEY (model_id) REFERENCES AirplaneModels(model_id) ON DELETE CASCADE
);