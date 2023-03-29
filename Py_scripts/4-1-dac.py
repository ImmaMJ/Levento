import RPi.GPIO as GPIO


def Dec2Bin(num):
    return [int(el) for el in bin(int(num))[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setup(dac, GPIO.OUT)

try:
    while True:
        b = -1
        d = int(input('Enter int number from 0 to 255:'))
        if (d >= 0)*(b <= 255):
            b = Dec2Bin(d)
            GPIO.output(dac, b)
            v = (d/255)*3.3
            print(v, " volts")


finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()