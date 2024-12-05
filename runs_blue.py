from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from missions_blue import *

# hub = PrimeHub()

# motor_left=Motor(Port.A,Direction.COUNTERCLOCKWISE) #Possibly B 
# motor_right=Motor(Port.B,Direction.CLOCKWISE) #possilby A

# drive_base=DriveBase(motor_left,motor_right,56,90)

# le=Motor(Port.F,Direction.COUNTERCLOCKWISE)
# re=Motor(Port.E,Direction.CLOCKWISE)

def run1(db, le, re):
    db.straight(220)
    db.turn(-37)
    db.straight(830)
    db.settings(straight_speed=350)
    db.straight(-830)
    db.turn(-25.01)
    db.straight(401)
    db.straight(-400)
    db.turn(-40)
    db.straight(575)
    db.turn(86)
    db.straight(1045)
    db.turn(25)
    db.straight(290)
    db.turn(66)
    db.straight(600)
    #  db.straight(-220)
    #  db.turn(-35)
    #  db.straight(-830)
    #  db.settings(straight_speed=550)
    #  db.straight(830)
    #  db.turn(-25.01)
    #  db.straight(-401)
    #  db.straight(400)
    #  db.turn(-40)
    #  db.straight(-590)
    #  db.turn(90)
    #  db.straight(-1050)
    #  db.turn(25)
    #  db.straight(-290)
    #  db.turn(66)
    #  db.straight(-300)

def run6(db, le, re):
    mission9(db, le,re)
    mission11(db, le, re)

def run7(db, le, re):
    # db.straight(200)
    # db.turn(-90)
    db.straight(700)
    db.turn(-95)
    mission14(db, le, re)
