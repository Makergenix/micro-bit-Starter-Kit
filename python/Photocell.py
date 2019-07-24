from microbit import *


while True:
   led = pin0.read_analog()
   pin1.write_analog(led)
   
   