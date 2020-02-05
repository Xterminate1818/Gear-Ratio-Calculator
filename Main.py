import math
import tkinter


def ratio(driven, driver):
    return driven / driver


class Motor:
    def __init__(self, speed, torque, radius, ratio=1):
        self.speed = speed
        self.torque = torque
        self.radius = radius
        self.ratio = ratio

    def gear(self, ratio):
        self.ratio = ratio

    def get_speed(self):
        return self.speed / self.ratio

    def get_torque(self):
        return self.torque * self.ratio


class RevHex(Motor):
    def __init__(self, ratio=1):
        super().__init__(6000, 0.105, 0.0025, ratio)


class DriveWheel:
    def __init__(self, radius, motor):
        self.radius = radius
        self.diameter = radius * 2
        self.circumference = self.diameter * math.pi
        self.motor = motor
        self.torque = (self.radius * motor.get_torque()) / radius
        self.speed = self.circumference * (motor.speed / 60) * (1 / motor.ratio)
        self.force = self.torque / (self.radius / math.sin(90))


testMotor = RevHex(1)
testMotor.gear(ratio(40, 1))
testWheel = DriveWheel(0.0508, testMotor)

print(testWheel.speed, ' ', testWheel.torque, ' ', testWheel.force)
