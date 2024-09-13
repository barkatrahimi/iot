from machine import Pin
import time

led = Pin(15, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_UP)

def send_sos(num_of_sos):
    for _ in range(num_of_sos):
        # 3 short
        for _ in range(3):
            led.value(1)
            time.sleep(0.2)  
            led.value(0)
            time.sleep(0.2)
        
        time.sleep(0.5)  
        
        # 3 long
        for _ in range(3):
            led.value(1)
            time.sleep(0.6)  
            led.value(0)
            time.sleep(0.2)
        
        time.sleep(0.5)  
        
        # 3 short
        for _ in range(3):
            led.value(1)
            time.sleep(0.2)
            led.value(0)
            time.sleep(0.2)
        
        time.sleep(1) 

try:
    while True:
        if not button.value():  
            send_sos(1)  
        else:
            led.value(0)  

        time.sleep(0.1)  
except:
    pass

