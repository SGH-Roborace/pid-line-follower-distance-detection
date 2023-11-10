
import time
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import ColorSensor

ev3 = EV3Brick()

farbe = ColorSensor()

while True:
    ev3.screen.clear()
    reflection = farbe.reflection()
    ev3.screen.draw_text(0,0,str(reflection))
    time.sleep(1)