#!/usr/bin/env python
import RPi.GPIO as GPIO # RPi.GPIO can be referred as GPIO from now
import time
 
GPIO.setmode(GPIO.BCM) #gpio mode

GPIO.setup(24, GPIO.OUT)  #LED to GPIO24
try:
        while True:
                print 'LED on'
                GPIO.output(ledPin, GPIO.HIGH)   # LED On
                time.sleep(1.0)                  # wait 1 sec
                print 'LED off'
                GPIO.output(ledPin, GPIO.LOW)   # LED Off
                time.sleep(1.0)                 # wait 1 sec
except:
        GPIO.output(ledPin, GPIO.LOW)     # LED Off
        GPIO.cleanup()                    # Release resources
