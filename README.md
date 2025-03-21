# IoT-Based Parking Slot Management System using Raspberry Pi 3 and Firebase Cloud

## Project Overview
With the rapid increase in vehicle ownership, urban areas are facing significant challenges in managing parking spaces efficiently. Traffic congestion, pollution, and inefficient parking allocation have become persistent issues. This project introduces an __IoT-based Smart Parking Slot Management System__ designed to optimize parking utilization, reduce congestion, and enhance user experience by integrating sensor-based automation, real-time data processing, and cloud-based accessibility.

## Features & Technologies Used
- **IoT Sensors:** Infrared (IR) and Magnetic Sensors for real-time parking slot detection.
- **Processing Node:** Raspberry Pi for sensor data processing.
- **Communication Protocol:** Zigbee for low-power, secure data transmission.
- **Cloud Storage:** Firebase Realtime Database for storing parking slot availability.
- **User Applications:**
  - **Android Application:** Displays slot availability, allows reservations, and provides GPS tracking.
 

## System Architecture
![IoT-Based Parking Slot Management System using Raspberry Pi 3 and Firebase Cloud- Proposed Architecture](images/Architecture.png)

*IoT-Based Parking Slot Management System using Raspberry Pi 3 and Firebase Cloud- Proposed Architecture*

![IoT-Based Parking Slot Management System using Raspberry Pi 3 and Firebase Cloud- Working Model](images/WorkingModel.png)

*IoT-Based Parking Slot Management System using Raspberry Pi 3 and Firebase Cloud- Working Model*

1. **End Nodes:** Sensors (IR & Magnetic) detect vacant parking slots.
2. **Processing Node:** Raspberry Pi processes sensor data and transmits it.
3. **Cloud Database:** Firebase stores real-time slot data.
4. **User Interfaces:** Mobile app and web portal access parking slot availability and allow bookings.
5. **Security Features:**
   - OTP-based smart lock for slot access.

## Installation & Setup
### Raspberry Pi Configuration
1. Update the system:
   ```bash
   sudo apt-get update
   ```
2. Install GPIO library:
   ```bash
   sudo apt-get install rpi.gpio
   ```
3. Clone this repository:
   ```bash
   git clone https://github.com/Amulya275/IoT-Based-Smart-Parking-System-with-Raspberry-Pi.git
   ```
4. Install Firebase Python package:
   ```bash
   pip install firebase
   ```

### Running the System
1. Execute the sensor data collection script:
   ```bash
   python sensor_script.py
   ```
   
![Parking Slot monitoring on Firebase Cloud](images/FirebaseCloud.png)

*Parking Slot monitoring on Firebase Cloud- Obstacle here is Car*
   
3. Start the Android application (install APK on mobile device).


## Mobile App Features
![Parking Slot Booking Application- Registration and Login Pages](images/AppRegistrationandLogin.png)

*Parking Slot Booking Application- Registration and Login Pages*

![Parking Slot Booking Application- Slot availability wrt Firebase Cloud Slot data](images/SlotsDisplayonApp.png)

*Parking Slot Booking Application- Slot availability wrt Firebase Cloud Slot data*

- Slot availability display
- GPS tracking to navigate to booked slot
- Secure booking with OTP-based slot access

## Billing System
![Parking Slot Booking Application- Billing and GPS Tracking](images/BillingAndGPS.png)

*Parking Slot Booking Application- Billing and GPS Tracking*

- Base charge: Rs. 25/hour
- Late arrival fee: Rs. 50/hour
- Total Amount Calculation:
  ```
  Total Amount = Rs. {n1 * 5 + (n2 - 1) * 10}
  ```
  where `n1` is the parking duration and `n2` is the arrival time.

## Future Enhancements
- AI-based predictive parking slot availability
- Integration with payment gateways
- Multi-floor parking assistance using advanced GPS tracking

## Contributors
- **Amulya Reddy Maligireddy**  
- **Keerthi Reddy Konda**  
- **Leela Lekkala**  
- **Sri Harini Chinnam**  

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
### Let's Park Hassle-Free 🚗💨
