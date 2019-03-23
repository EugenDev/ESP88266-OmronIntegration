import uos
import utime
from machine import UART


def measure_start():
    uos.dupterm(None, 1)

    uart = UART(0)
    uart.init(115200)
    step = 0
    while step < 100:
        print(uart.readline())
        step += 1
        utime.sleep_ms(200)


def pin_test():
    step = 0
    pin = machine.Pin(4, machine.Pin.IN)
    while step < 100:
        print(pin.value())
        step += 1
        utime.sleep_ms(200)
