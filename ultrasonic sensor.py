import RPi.GPIO as GPIO
import time
from gpiozero import PWMLED

SPEED_OF_SOUND = 34000
MAX_DISTANCE=30

GPIO.setmode(GPIO.BCM)
TRIGGER = 23
ECHO = 24
LED = PWMLED(18)

GPIO.setup(TRIGGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


#Function

def distance():
    GPIO.output(TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(TRIGGER, False)
    
    while (GPIO.input(ECHO) == 0):
        startTime= time.time()
        
    while (GPIO.input(ECHO) == 1):
        stopTime= time.time()
    
    timeElapsed = stopTime - startTime
    distance = timeElapsed * SPEED_OF_SOUND
    
    return distance

try:
    while True:
        currentDistance = distance()
        print("Measured distance = %.2f cm" % currentDistance)
        
        if currentDistance > MAX_DISTANCE:
            LED.value = 0
        
        if currentDistance <= MAX_DISTANCE:
            proximity = 1 - (currentDistance / MAX_DISTANCE)
            LED.value = proximity
            
        time.sleep(1)
        
except keyboardInterrupt:
    print("Measurement stopped")
    GPIO.cleanup