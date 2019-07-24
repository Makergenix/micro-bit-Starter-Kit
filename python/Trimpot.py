from microbit import *


while True:
   a = pin0.read_analog()
   pin1.write_analog(a)
   
   