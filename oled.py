# Import machine and OLED libraries -----------------------------------------------

from machine import Pin, UART, I2C
from ssd1306 import SSD1306_I2C

# Import utime library to implement delay

import utime, time

# Oled I2C connection

# i2c=I2C(0,sda=Pin(4), scl=Pin(5), freq=400000)
i2c=I2C(sda=Pin(4), scl=Pin(5), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

oled.text("Latitude : ", 0, 0)
oled.show()