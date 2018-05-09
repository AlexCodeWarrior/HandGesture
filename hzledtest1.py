import time
from servoControl import Servo
from lightControl import Light

led = Servo(0,4095,4)
spot = Servo(205,409,2)

#while 1:
Laser = Light(18)
led.setMin()
#spot.neutralPos()
Laser.lightOff()
Laser.lightOn()
while 1:
	print("Test")

#for i in range(spot.curpos, spot.max, 1):
		#spot.increase()
		#print("Current Pos:" + str(i))
		#led.setMax()
		#time.sleep(0.05)
#for i in range(spot.max-1, spot.min-1, -1):
		#spot.decrease()
		#print("Current Pos: " + str(i))
		#led.setMin()
		#time.sleep(0.05)
#spot.neutralPos()
