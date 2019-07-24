from microbit import *

   
def led(self):
	pin0.write_digital(0)
	pin1.write_digital(1)

	sleep(200)
	
	pin1.write_digital(0)
	pin0.write_digital(1)
	
	sleep(200)

while True:
	led()