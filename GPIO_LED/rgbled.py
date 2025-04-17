import Jetson.GPIO as GPIO
from time import sleep

#RGB pins (Red = 11, Green = 12, Blue = 13)
pins = [11,12,13]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pins[0], GPIO.OUT)
GPIO.setup(pins[1], GPIO.OUT)
GPIO.setup(pins[2], GPIO.OUT)

while True:
   GPIO.output(pins[0], GPIO.HIGH)
   GPIO.output(pins[1], GPIO.LOW)
   GPIO.output(pins[2], GPIO.LOW)
   print("LED is Red")
   sleep(2)

   GPIO.output(pins[0], GPIO.LOW)
   GPIO.output(pins[1], GPIO.HIGH)
   GPIO.output(pins[2], GPIO.LOW)
   print("LED is Green")
   sleep(2)

   GPIO.output(pins[0], GPIO.LOW)
   GPIO.output(pins[1], GPIO.LOW)
   GPIO.output(pins[2], GPIO.HIGH)
   print("LED is Blue")
   sleep(2)

