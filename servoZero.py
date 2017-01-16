# servoLeft.py
#
# Created by Ebubekir Ogden & Gokhan Maden on 1/08/17
# Copyright © 2017 Ebubekir Ogden and Gokhan Maden. All rights reserved.
#

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
pwm = GPIO.PWM(18,100)
pwm.start(5)
GPIO.setwarnings(False)

duty = float(90.0)/10.0+2.5
pwm.ChangeDutyCycle(duty)
time.sleep(0.1)
os.system("pkill idle")
