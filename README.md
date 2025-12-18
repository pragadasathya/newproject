# AWS DevOps Online Booking System

## Tech Stack
- Python (Flask)
- AWS EC2, RDS
- Docker
- Jenkins CI/CD

## Architecture
User → EC2 (Dockerized Flask App) → RDS MySQL

## Features
- Book slots
- View bookings
- CI/CD using Jenkins
- Containerized deployment

## How to Run
```bash
docker build -t booking-app .
docker run -p 5000:5000 booking-app
