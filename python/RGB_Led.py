from microbit import *


while True:
    if button_a.is_pressed():
        pin0.write_digital(1)
        pin1.write_digital(0)
        pin2.write_digital(0)
        
        sleep(500)
        pin1.write_digital(0)
        pin1.write_digital(1)
        pin2.write_digital(0)
        sleep(500)
        
        pin1.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(1)
        sleep(500)
    else:
        pin0.write_digital(0)
        pin1.write_digital(0)
        pin2.write_digital(0)
  
   
   