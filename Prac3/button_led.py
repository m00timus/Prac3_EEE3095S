import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) #gpio mode

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP ) #using gpio23 pin
GPIO.setup(24, GPIO.OUT)  #LED to GPIO24

try:

    while True:

         button = GPIO.input(23)
         if button == False:

             GPIO.output(24, True)
             print('Button Pressed...')
             time.sleep(0.2)
         else:

             GPIO.output(24, False)

except:
    GPIO.cleanup()

