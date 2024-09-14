CREATE DATABASE Airplane_System;
USE Airplane_System;
CREATE TABLE user_plane (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    plane_name VARCHAR(255),
    plane_type VARCHAR(255),
    manufacturer_id INT,
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturer(id)
);
CREATE TABLE manufacturer (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255)
);
CREATE TABLE airframe_parts (
    id INT PRIMARY KEY AUTO_INCREMENT,
    plane_id INT,
    part_name VARCHAR(255),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id)
);
CREATE TABLE engine (
    id INT PRIMARY KEY AUTO_INCREMENT,
    plane_id INT,
    engine_type VARCHAR(255),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id)
);
CREATE TABLE landing_gear (
    id INT PRIMARY KEY AUTO_INCREMENT,
    plane_id INT,
    gear_type VARCHAR(255),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id)
);
CREATE TABLE fuel_system (
    id INT PRIMARY KEY AUTO_INCREMENT,
    plane_id INT,
    system_type VARCHAR(255),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id)
);
CREATE TABLE cockpit_controls (
    id INT PRIMARY KEY AUTO_INCREMENT,
    plane_id INT,
    control_type VARCHAR(255),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id)
);
CREATE TABLE avionics (
    id INT PRIMARY KEY AUTO_INCREMENT,
    plane_id INT,
    avionics_type VARCHAR(255),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id)
);
CREATE TABLE electrical_system (
    id INT PRIMARY KEY AUTO_INCREMENT,
    plane_id INT,
    system_type VARCHAR(255),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id)
);
CREATE TABLE flight_instruments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    plane_id INT,
    instrument_name VARCHAR(255),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id)
);
CREATE TABLE brakes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    plane_id INT,
    brake_type VARCHAR(255),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id)
);
CREATE TABLE exhaust_system (
    id INT PRIMARY KEY AUTO_INCREMENT,
    plane_id INT,
    system_type VARCHAR(255),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id)
);
CREATE TABLE cooling_system (
    id INT PRIMARY KEY AUTO_INCREMENT,
    plane_id INT,
    cooling_type VARCHAR(255),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id)
);
CREATE TABLE powerplant (
    id INT PRIMARY KEY AUTO_INCREMENT,
    plane_id INT,
    mount_type VARCHAR(255),
    FOREIGN KEY (plane_id) REFERENCES user_plane(id)
);