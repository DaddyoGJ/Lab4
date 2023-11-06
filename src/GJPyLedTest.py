import socket
import time
from hal import hal_led as led
from hal import hal_input_switch as switch

def blink_led(delay):
    led.set_output(0, 1)
    time.sleep(delay)

    led.set_output(0, 0)
    time.sleep(delay)

def no_led():
    led.set_output(0,0)

def main():
    led.init()
    switch.init()
    start_timer = 0
    if time.time() - start_timer < 5.0:
        while switch.read_slide_switch() == 1:
            blink_led(0.05)
        while switch.read_slide_switch() != 0:
            no_led()
    while switch.read_slide_switch() == 0:
        blink_led(0.1)

if __name__ == "__main__":
    while 1:
        main()