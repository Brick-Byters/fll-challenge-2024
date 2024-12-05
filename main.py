from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

from runs_red import *
from runs_blue import *

hub = PrimeHub()

leftmotor =  Motor(Port.A,Direction.COUNTERCLOCKWISE)
rightmotor = Motor(Port.B,Direction.CLOCKWISE)
drive_base = DriveBase(leftmotor, rightmotor,56,90)
le=Motor(Port.F,Direction.CLOCKWISE)
re=Motor(Port.E,Direction.CLOCKWISE)

num_menu_options = 7

# Normally, the center button stops the program. But we want to use the
# center button for our menu. So we can disable the stop button.
hub = PrimeHub()

menu_index= 0

while True:
    hub.system.set_stop_button(None)
    
    while True:
        hub.display.char(str(menu_index+1))

        # Wait for any button.
        pressed = ()
        while not pressed:
            pressed = hub.buttons.pressed()
            wait(10)
        
        # Wait for the button to be released.
        while hub.buttons.pressed():
            wait(10)

        # Now check which button was pressed.
        if Button.CENTER in pressed:
            # Center button, so the menu is done!
            break
        elif Button.RIGHT in pressed:
            # Left button, so decrement menu menu_index.
            menu_index = (menu_index + 1) % num_menu_options
        elif Button.LEFT in pressed:
            # Right button, so increment menu menu_index.
            menu_index = (menu_index - 1) % num_menu_options

    print("button pressed")

    # Now we want to use the Center button as the stop button again.
    hub.system.set_stop_button(Button.CENTER)

    print("running program %d" % menu_index)

    program_num = menu_index + 1

    if program_num == 1:
        run1(drive_base, le, re)
    elif program_num == 2:
        run2(drive_base,le,re)
    elif program_num == 3:
        run3(drive_base,le,re)
    elif program_num == 4:
        run4(drive_base,le,re)
    elif program_num == 5:
        run5(drive_base,le,re)
    elif program_num == 6:
        run6(drive_base,le,re)
    elif program_num == 7:
        run7(drive_base,le,re)


# Based on the selection, choose a program.
# selected = menu_options[menu_index]
# if selected == "D":
#     import mission_drive
# elif selected == "L":
#     import mission_line
# elif selected == "F":
#     import mission_fly