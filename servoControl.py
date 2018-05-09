# Servo Control

from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Sets the frequency for the Adafruit PCA9685 servo hat.
pwm.set_pwm_freq(50)

# The Servo class is used to control a servo from the Adafruit PCA9685
# servo hat. Each instance of the class controls a single servo.
class Servo:
    #
    def __init__(self, Min, Max, Port):
        self.min = Min
        self.max = Max
        self.curpos = self.min
        self.port = Port

    #
    def minMax(self):
        return '{} {}'.format(self.min, self.max)

    #
    def increase(self):
        if self.curpos < self.max:
            self.curpos = int(self.curpos + 1)
            pwm.set_pwm(self.port, 0, self.curpos)
            return True
        else:
            return False

    #
    def decrease(self):
        if self.curpos > self.min:
            self.curpos = int(self.curpos - 1)
            pwm.set_pwm(self.port, 0, self.curpos)
            return True
        else:
            return False

    #
    def increaseRate(self, value):
        if self.curpos < self.max:
            self.curpos = int(self.curpos + value)
            if self.curpos > self.max:
                self.curpos = self.max
            pwm.set_pwm(self.port, 0, self.curpos)
            return True
        else:
            return False
            
    #
    def decreaseRate(self, value):
        if self.curpos > self.min:
            self.curpos = int(self.curpos - value)
            if self.curpos < self.min:
                self.curpos = self.min
            pwm.set_pwm(self.port, 0, self.curpos)
            return True
        else:
            return False

    #
    def neutralPos(self):
        neut = (self.min + self.max) / 2
        self.curpos = int(neut)
        pwm.set_pwm(self.port, 0, self.curpos)

    def setMin(self):
        self.curpos =  self.min
        pwm.set_pwm(self.port, 0, self.curpos)

    def setMax(self):
        self.curpos = self.max
        pwm.set_pwm(self.port, 0, self.curpos)
