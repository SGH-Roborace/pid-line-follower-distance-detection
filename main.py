#!/usr/bin/env pybricks-micropython
import time
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import threading

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
drife = DriveBase(Motor(Port.B), Motor(Port.A), 70*36/20, 136)
farbe = ColorSensor(Port.S1)
weg = UltrasonicSensor(Port.S2)
zickzack = 44
'''
while True:
    zickzack = zickzack*1/3 farbe.reflection()*2/3
    
    bing = weg.distance()

    drife.drive(max((bing)-abs(zickzack),0), (zickzack-50)*3.6 )
    zickzack.pop(0)
'''
beans = 1
start = 0
'''
target = 10
integral = 10
Kp,Ki,Kd = 1,1,1
value = reflection

error = target-value
integral += error
derivative = error - last_error
'''
angy = 0

while True:
    distance = weg.distance()
    reflection = farbe.reflection()
    
    if distance > 250:
        distance = 250
    elif distance < 150:
        distance = 150

    if reflection < 10:
        angle = 40
        angy = -angle*beans*(reflection/10)
        while reflection < 40:

            speed = (distance-150) * 6 # results in speed between 0 and 300
            drife.drive(max(speed, 0), angle*beans*(abs(reflection-30)/80))
            distance = weg.distance()
            reflection = farbe.reflection()
            if distance > 250:
                distance = 250
            elif distance < 150:
                distance = 150
        while reflection < 70:
            speed = (distance-150) * 6
            drife.drive(max(speed, 0), -angle*beans*(abs(reflection)/80))
            distance = weg.distance()
            reflection = farbe.reflection()
            if distance > 250:
                distance = 250
            elif distance < 150:
                distance = 150


        beans *= -1
        
    
    speed = (distance-150) * 12 # results in speed between 0 and 300
    angle = 360
    angy = angle*beans*(reflection/80)+30
    drife.drive(speed, angy)





'''
black = 8
white = 80
mid = (white - black)/2
max_angle = 70
max_speed = 2.5  #in dm/s
max_speed_reduction = 100 #in mm/s
distance = 250

def set_distance():
    global distance
    while True:
        distance = weg.distance()
        if distance > 250:
            distance = 250
        elif distance < 150:
            distance = 150


threading.Thread(target=set_distance).start()

while True:
    # Value of white 54 value of black 8 difference 46
    # linear steering from 70 degrees
    # distance between 15 and 25
    reflection = farbe.reflection()

    if reflection > white:
        reflection = white
    elif reflection < black:
        reflection = black

    if reflection > 80:
        reflection = 80
    elif reflection < 8:
        reflection = 8
    
    speed = int((distance-150) * 3 - abs((reflection-8-35)/35)**3*100) # results in speed between 0 and 300
    angle = (reflection-8-36) * -2.4
    drife.drive(min(-speed, 0), angle)
    

while True:
    ev3.screen.clear()
    reflection = farbe.reflection()
    ev3.screen.draw_text(0,0,str(abs((reflection-8-35)/35)**2*170))
    time.sleep(1)
    '''
