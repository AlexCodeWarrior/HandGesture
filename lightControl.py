# Light Control

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

# The Light class is used to control a single light.
# It uses the RPi.GPIO library to set the pin at
# which the light is connected to to either on or off.
class Light:

    #
    def __init__(self, Port):
        self.port = Port
        GPIO.setup(self.port ,GPIO.OUT)
        GPIO.output(self.port, False)

    #
    def lightOn(self):
        GPIO.output(self.port, True)

    #
    def lightOff(self):
        GPIO.output(self.port, False)
