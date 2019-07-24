from microbit import *

def disp(self):
    if button_a.is_pressed():
        pin0.write_digital(1)
        sleep(200)
        pin0.write_digital(0)
        
    elif button_b.is_pressed():
        pin1.write_digital(1)
        sleep(200)
        pin1.write_digital(0)
            
        
while True:
    disp()

                         