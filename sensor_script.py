import RPi.GPIO as GPIO
from firebase import firebase
import time

# Firebase configuration
fb = firebase.FirebaseApplication('https://park123-f32d7.firebaseio.com/')

# GPIO setup
Slot1 = 11
Slot2 = 13
Slot3 = 15

print "Detection in progress"

GPIO.setup(Slot1,GPIO.IN)
GPIO.setup(Slot2,GPIO.IN)
GPIO.setup(Slot3,GPIO.IN)

print "Waiting For Sensor To Settle" time.sleep(2)

while True:
time.sleep(0.00001)
if GPIO.input(Slot1)==0:
fb.put('Parking_spot','Slot_1','0')
else:
fb.put('Parking_spot','Slot_1','1')
time.sleep(0.00001)

if GPIO.input(Slot2)==0:
fb.put('Parking_spot','Slot_2','0')
else:
fb.put('Parking_spot','Slot_2','1')
time.sleep(0.00001)

if GPIO.input(Slot3)==0:
fb.put('Parking_spot','Slot_3','0')
else:
fb.put('Parking_spot','Slot_3','1')
GPIO.cleanup() 
#code end
