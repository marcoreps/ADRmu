# https://docs.circuitpython.org/projects/tmp117/en/latest/index.html

import board
import adafruit_tmp117
i2c = board.I2C()
address = 0x4B
tmp117 = adafruit_tmp117.TMP117(i2c, address)
print("Temperature: %.2f degrees C"%tmp117.temperature)