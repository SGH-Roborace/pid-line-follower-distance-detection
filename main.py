#!/usr/bin/env pybricks-micropython
import time
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
drife = DriveBase(Motor(Port.B), Motor(Port.A), 43, 88)
farbe = ColorSensor(Port.S1)
weg = UltrasonicSensor(Port.S2)
zickzack = [50,50,50,50,50,50,50,50,50,50,50]
'''
while True:
    zickzack.append(farbe.reflection())
    bong = sum(zickzack) / len(zickzack)
    bing = weg.distance()

    drife.drive(max((bing)-abs(bong),0), (bong-50)*3.6 )
    zickzack.pop(0)
'''
while True:
    # Value of white 54 value of black 8 difference 46
    # linear steering from 70 degrees
    # distance between 15 and 25
    distance = weg.distance()
    reflection = farbe.reflection()
    if distance > 250:
        distance = 250
    elif distance < 150:
        distance = 150


    if reflection > 54:
        reflection = 54
    elif reflection < 8:
        reflection = 8
    speed = (distance-150) * 2 # results in speed between 0 and 300
    angle = (reflection-8-23) * -2
    drife.drive(speed, angle)

    

