# IoT-Based-Smart-Parking-System-with-Raspberry-Pi 3

## Project Overview

This project aims to develop an intelligent, automated smart parking system using IoT technologies. The system optimizes parking space usage, reduces traffic congestion, and minimizes pollution and vehicle vandalism risks.

Features & Technologies Used

IoT Sensors: Infrared (IR) and Magnetic Sensors for real-time parking slot detection.

Processing Node: Raspberry Pi for sensor data processing.

Communication Protocol: Zigbee for low-power, secure data transmission.

Cloud Storage: Firebase Realtime Database for storing parking slot availability.

User Applications:

Android Application: Displays slot availability, allows reservations, and provides GPS tracking.

Web Portal: Enables slot booking, billing, and user management.

System Architecture

End Nodes: Sensors (IR & Magnetic) detect vacant parking slots.

Processing Node: Raspberry Pi 3 processes sensor data and transmits it.

Cloud Database: Firebase stores real-time slot data.

User Interfaces: Mobile app and web portal access parking slot availability and allow bookings.

Security Features:

Zigbee’s AES encryption for secure data transmission.

OTP-based smart lock for slot access.

Installation & Setup

Raspberry Pi Configuration

Update the system:

sudo apt-get update

Install GPIO library:

sudo apt-get install rpi.gpio

Install Firebase Python package:

pip install firebase

Running the System

Execute the sensor data collection script:

python sensor_script.py

Start the Android application (install APK on mobile device).

Access the web portal from a browser.

Web Portal Setup

Backend: PHP

Database: MySQL

Install XAMPP for local server setup

Run the web application from htdocs directory in XAMPP

Mobile App Features

Slot availability display

GPS tracking to navigate to booked slot

Secure booking with OTP-based slot access

Billing System

Base charge: Rs. 5/hour

Late arrival fee: Rs. 10/hour

Total Amount Calculation:

Total Amount = Rs. {n1 * 5 + (n2 - 1) * 10}

where n1 is the parking duration and n2 is the arrival time.

Future Enhancements

AI-based predictive parking slot availability

Integration with payment gateways

Multi-floor parking assistance using advanced GPS tracking

Contributors

Amulya Reddy Maligireddy

Keerthi Reddy Konda

Leela Lekkala

Sri Harini Chinnam

Let's Park Hassle-Free 🚗💨

License

This project is licensed under the MIT License - see the LICENSE file for details.

