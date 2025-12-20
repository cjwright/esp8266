from machine import Pin, SoftI2C
import ssd1306
from time import sleep
import gfx

# ESP32 Pin assignment
#2c = SoftI2C(scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
i2c = SoftI2C(scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


graphics = gfx.GFX(oled_width, oled_height, oled.pixel)



oled.fill(0)



for x in range(0,128,8):
    for y in range(0,64,8):
        # print(x,y)
        graphics.rect(0,0,128,64,1)
        graphics.line(x, y, x, y, 1)
            
             

oled.show()
