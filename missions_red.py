from pybricks.tools import wait, StopWatch

def missionX(db, le, re):
    pass

def mission2(db, le, re):
    le.run_angle(720,845)
    # le.run_angle(720,-845)

def mission1(db, le, re):
    db.straight(25)
    le.run_angle(720,535)
    db.straight(40)
    le.run_angle(720,-535)
    db.straight(-65)

def mission3(db, le, re):
    le.run_angle(720,900)
    #db.straight(20)
    le.run_angle(720,-900)

def mission8(db,le,re):
    drive_base.straight(875.6)
    le.run_angle(720,535)
    drive_base.settings(50)
    drive_base.straight(-60)
    le.run_angle(360,480)
    drive_base.settings(25)
    drive_base.straight(-60)
    drive_base.settings(800)
    drive_base.straight(-200)
    drive_base.turn(-20)
    drive_base.straight(-800)
    le.run_angle(360,1015)

def mission6(db,le,re):
    le.run_angle(720,360)
    db.straight(130)
    le.run_angle(600,-720)
