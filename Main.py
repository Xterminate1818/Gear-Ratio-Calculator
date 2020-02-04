import math
import tkinter


def gear(driven, driver, motor):
    if type(motor) is not dict:
        print('Gear expects dict, not ', type(motor))
        raise TypeError
    ratio = driven / driver
    motor['speed'] /= ratio
    motor['torque'] *= ratio
    return motor


revHex = {
    'speed': 6000,   # RPM
    'torque': 0.105  # NM
}

wheelDiameter = 4    # inches

print(gear(20, 1, revHex))
