from microbit import *

s = 0

while True:
    if pin1.read_digital():
        s = 0 if s == 1 else 1
        pin2.write_digital(s)
    else:
        pin2.write_digital(0)
            

        
            
    
   