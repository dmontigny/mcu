# https://blog.jetbrains.com/pycharm/2018/01/micropython-plugin-for-pycharm/

import utime
from machine import Pin


def blinkme():
    led = Pin(2, Pin.OUT)

    enabled = False
    while True:
        if enabled:
            led.off()
        else:
            led.on()
        utime.sleep_ms(1000)
        enabled = not enabled

