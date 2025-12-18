CREATE DATABASE bookingdb;
USE bookingdb;

CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    date DATE,
    slot VARCHAR(50)
);
