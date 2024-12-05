from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from missions_red import *

# hub = PrimeHub()

# leftmotor =  Motor(Port.A,Direction.COUNTERCLOCKWISE)
# rightmotor = Motor(Port.B,Direction.CLOCKWISE)
# drive_base = DriveBase(leftmotor, rightmotor,56,90)
# le=Motor(Port.F,Direction.CLOCKWISE)
# re=Motor(Port.E,Direction.CLOCKWISE)

def run2(db, le, re):
    db.straight(-300)
    db.turn(-90)
    db.straight(676)
    mission3(db,le,re)
    db.straight(-180)
    db.turn(88)
    mission1(db,le,re)
    db.turn(-45)
    db.straight(170)
    mission2(db,le,re)
    db.straight(-20)
    db.turn(-25)
    db.straight(-350)
    db.turn(-85)
    db.straight(-450)

def run3(db,le,re):
    db.straight(875.6)
    le.run_angle(720,535)
    # db.settings(50)
    db.straight(-40)
    le.run_angle(360,480)
    db.settings(25)
    db.straight(-100)
    db.settings(800)
    db.straight(-200)
    db.turn(-22)
    db.straight(-800)


def run4(db,le,re):
    db.straight(-75)
    db.straight(75)

def run5(db,le,re):
    db.settings(500)
    db.straight(-659.6)
    db.turn(45)
    db.straight(-177.8)
    db.turn(30)
    db.straight(107)
    db.turn(-50)
    db.settings(800)
    db.straight(-381)
    db.turn(-35)
    db.straight(-880)
    
def run6(db,le,re):
    mission6(db,le,re)

# main program
# run1(drive_base, le, re)
