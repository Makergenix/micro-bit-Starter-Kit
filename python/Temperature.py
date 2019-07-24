from microbit import *

Temp_Threshold = 35

while True:
    value = pin1.read_analog()
    #  Calculate Temperature from received digital value
    val = (value*3300)/1024
    temp = (val-500)/10

    display.scroll(temp)

    if Temp_Threshold < temp:
        pin2.write_digital(1)

    else:
        pin2.write_digital(0)

        
        
    
   
            

        
            
    
   