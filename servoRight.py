# servoRight.py
#
# Created by Ebubekir Ogden & Gokhan Maden on 1/08/17
# Copyright © 2017 Ebubekir Ogden and Gokhan Maden. All rights reserved.
#

import os
import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18,100)
pwm.start(5)
GPIO.setwarnings(False)

degree = sys.argv[1]

text_file = open("Output.txt", "a+") # Read File with a+ Mode -> If the file doesn't exists create it
text_file.seek(0) # File pointer is at the end of the file if file exists, so we're moving the cursor to the beginning.

currentDegree = text_file.readline() # Read one line

if not currentDegree: # If currentDegree not exists
    currentDegree = 90.0
    degree = currentDegree + float(degree)
    duty = float(degree)/10.0+2.5
    pwm.ChangeDutyCycle(duty)
    #GPIO.cleanup()
    text_file.write(str(degree)) # Write final angle of the servo
    time.sleep(0.1)
    text_file.close() # Close the file
    os.system("pkill idle")
else:
    text_file.close() # If file does exists we need to open with r+ mode to overwrite so we are closing the opened file
    text_file = open("Output.txt", "r+") # Re-open the file with r+ mode which, overwrite the file
    currentDegree = float(currentDegree) # Convert str to float
    degree = float(degree) # Convert str to float
    degree = currentDegree + degree # Currentdegree - degree which is came from argument

    # Rotate the servo's angle
    duty = float(degree)/10.0+2.5
    pwm.ChangeDutyCycle(duty)
    #GPIO.cleanup()
    #
    text_file.write(str(degree)) # Write final angle of the servo
    time.sleep(0.1)
    text_file.close() # Close the file
    os.system("pkill idle")
