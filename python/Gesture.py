from microbit import *


while True:
    gesture = accelerometer.current_gesture()
    
    if gesture == 'left':
        pin0.write_digital(1)
        
        
    elif gesture == 'right':
        pin0.write_digital(0)
            
    elif gesture == 'up':
        pin1.write_digital(1)
        
        
    elif gesture == 'face down':
        pin1.write_digital(0)
        
    elif gesture == 'shake':
        pin2.write_digital(1)
        sleep(5)
        pin2.write_digital(0)
        
    