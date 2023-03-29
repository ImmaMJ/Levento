import RPi.GPIO as GPIO

import time

def Dec2Bin(num):
    return [int(el) for el in bin(int(num))[2:].zfill(8)]



GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        for i in range(0, 255):
            GPIO.output(dac, Dec2Bin(i))
            time.sleep(0.015)
        
        # for i in range(0, 3):
        #     GPIO.output(dac, 0)
        #     time.sleep(0.1)
        #     GPIO.output(dac, 1)
        #     time.sleep(0.1)

        for i in range(0, 255):
            GPIO.output(dac, Dec2Bin(255 - i))
            time.sleep(0.015)    


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()