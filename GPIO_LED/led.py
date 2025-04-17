import Jetson.GPIO as GPIO
from time import sleep
 
pin = 22
 
# GPIO Setup
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(pin, GPIO.OUT) 

# LED ON/OFF
while True: 
  GPIO.output(pin, GPIO.HIGH)
  print("LED is ON")
  sleep(2)
  GPIO.output(pin, GPIO.LOW)
  print("LED is OFF")
  sleep(2)
