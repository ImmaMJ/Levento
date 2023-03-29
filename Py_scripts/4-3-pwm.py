import RPi.GPIO as GPIO


def Dec2Bin(num):
    return [int(el) for el in bin(int(num))[2:].zfill(8)]

GPIO.setmode(GPIO.BCM)

GPIO.setup([15, 24, 25], GPIO.OUT)
GPIO.output(25, 1)


try:
    p = GPIO.PWM(15, 1000)
    s = GPIO.PWM(24, 1000)
    while True:
        d = int(input('Enter the fill factor (from 1 to 100):'))
        
        p.start(d)
        s.start(d)
        v = (d/255)*3.3
        print(v, " volts")

finally:
    GPIO.cleanup()




p = GPIO.PWM(2, 0.5)
p.start(1)
input('Press return to stop:')   # use raw_input for Python 2
p.stop()
GPIO.cleanup()