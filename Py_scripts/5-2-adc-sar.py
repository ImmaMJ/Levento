import RPi.GPIO as GPIO

import time

dac    = [26, 19, 13, 6, 5, 11, 9, 10]
comp   = 4
troyka = 17
bits   = len(dac)
levels = 2 ** bits
max_voltage = 3.3

def Dec2Bin(num):
    return [int(el) for el in bin(int(num))[2:].zfill(8)]

def num2dac(value):
    signal = Dec2Bin(value)
    GPIO.output(dac, signal)
    return signal

def adc():
    k = 0
    for i in range(bits - 1, -1, -1):
        k += 2**i
        GPIO.output(dac, Dec2Bin(k))
        time.sleep(0.009)
        comp_val = GPIO.input(comp)
        if (comp_val == 0):
            k -= 2**i
    return k

# def adc():
#     for value in range(levels):
#         num2dac(value)
#         time.sleep(0.001)
#         if GPIO.input(comp) == 0:
#             return value

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        val = adc()
        print(val, Dec2Bin(val), " volts - {:.3}".format(val / levels * max_voltage))

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()
