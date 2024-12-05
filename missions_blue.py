def missionX(db, le, re):
    pass

def mission9(db, le, re):
    db.straight(127)
    db.turn(-45)
    db.straight(420)
    db.straight(-210)
    db.turn(-48)

def mission11(db, le, re):
    # db.straight(-525) #comment(running into eleven)
    # db.turn(-5)
    # re.run_angle(360,375)
    # db.straight(203)
    #db.straight(225)
    #db.turn()
    db.straight(550)
    re.run_angle(360,380)
    db.straight(-500)
    re.run_angle(540,-380)
    db.turn(45)
    db.straight(-300)

def mission14(db, le, re):
    db.straight(100)
    le.run_angle(360,700)
    db.straight(-190)
    le.run_angle(720,-400)
    # db.turn(-8)
    db.straight(-725)
    db.turn(56)
    db.straight(-15)
    re.run_angle(360,380)
    db.straight(85)
    db.turn(9)
    re.run_angle(360,-225)
    db.turn(-80)
    db.straight(750)
    db.turn(-75)
    db.straight(700)
    #re.run_angle(360,225)
    #re.run_angle(360,-450)
    #db.straight(20)
    

 
