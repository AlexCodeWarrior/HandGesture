# System Control

import RPi.GPIO as GPIO
import time
import servoControl
from servoControl import Servo
import lightControl
from lightControl import Light

class System:

    def __init__(self):
        self.servoYaw = Servo(205,409,0)
        self.servoPitch = Servo(205,409,1)
        self.lampSpot = Servo(205,409,2)
        self.lampLight = Servo(0,4095,4)
        self.lightGreen = Light(18)
        self.lightRed = Light(22)
        self.laserPointer = Light(24)

    def cleanUp(self):
        GPIO.cleanup()

    def turnOnRed(self):
        self.lightRed.lightOn()

    def turnOffRed(self):
        self.lightRed.lightOff()

    def turnOnGreen(self):
        self.lightGreen.lightOn()

    def turnOffGreen(self):
        self.lightGreen.lightOff()

    def turnOnLaser(self):
        self.laserPointer.lightOn()

    def turnOffLaser(self):
        self.laserPointer.lightOff()

    def blinkGreen(self):
        self.lightGreen.lightOn()
        time.sleep(0.005)
        self.lightGreen.lightOff()
        time.sleep(0.005)
        self.lightGreen.lightOn()
        time.sleep(0.005)
        self.lightGreen.lightOff()
        time.sleep(0.005)
        self.lightGreen.lightOn()
        time.sleep(0.005)
        self.lightGreen.lightOff()

    def blinkRed(self):
        self.lightRed.lightOn()
        time.sleep(0.005)
        self.lightRed.lightOff()
        time.sleep(0.005)
        self.lightRed.lightOn()
        time.sleep(0.005)
        self.lightRed.lightOff()
        time.sleep(0.005)
        self.lightRed.lightOn()
        time.sleep(0.005)
        self.lightRed.lightOff()

    def decLampBright(self):
        self.lampLight.decrease()

    def incLampBright(self):
        self.lampLight.increase()

    def decLampSpot(self):
        self.lampSpot.decrease()

    def incLampSpot(self):
        self.lampSpot.increase()

    def decLampPitch(self):
        self.servoPitch.decrease()

    def incLampPitch(self):
        self.servoPitch.increase()

    def decLampYaw(self):
        self.servoYaw.decrease()

    def incLampYaw(self):
        self.servoYaw.increase()

    def servoSetAllNeutral(self):
        self.servoYaw.neutralPos()
        self.servoPitch.neutralPos()
        self.lampSpot.neutralPos()
        self.lampLight.neutralPos()

    def servoTestYaw(self):
        for i in range(self.servoYaw.min, self.servoYaw.max, 1):
            self.servoYaw.increase()
            time.sleep(0.005)

        for i in range(self.servoYaw.max-1, self.servoYaw.min-1, -1):
            self.servoYaw.decrease()
            time.sleep(0.005)

    def servoTestPitch(self):
        for i in range(self.servoPitch.min, self.servoPitch.max, 1):
            self.servoPitch.increase()
            time.sleep(0.005)

        for i in range(self.servoPitch.max-1, self.servoPitch.min-1, -1):
            self.servoPitch.decrease()
            time.sleep(0.005)
