
# Basic blink code

from machine import Pin
import time 

led = Pin(2, Pin.OUT)
led.off()
for i in range(10):
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
