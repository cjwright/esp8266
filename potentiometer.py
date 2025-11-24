# Read a potentiometer using ADC on Adafruit Huzzah 

import machine
import time

# Configure the pin connected to the middle of the potentiometer
# For Adafruit Feather HUZZAH ESP8266, the analog pin is often A0
# Pin 0 is A0

adc = machine.ADC(0)


while True:
    # Read the raw 16-bit value from the ADC
    value = (adc.read_u16())
    print(f"Potentiometer value: {value}")
    time.sleep(0.1)
