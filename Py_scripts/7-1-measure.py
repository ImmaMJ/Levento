import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
import time


def Dec2Bin(num):
    return [int(el) for el in bin(int(num))[2:].zfill(8)]

def num2dac(value):
    signal = Dec2Bin(value)
    GPIO.output(dac, signal)
    return signal

def adc():
    level = 0
    for i in range(bits - 1, -1, -1):
        level += 2**i
        GPIO.output(dac, Dec2Bin(level))
        time.sleep(0.009)
        comp_val = GPIO.input(comp)
        if (comp_val == 0):
            level -= 2**i
    return level


dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds   = [21, 20, 16, 12, 7, 8, 25, 24]
comp   = 4
troyka = 17
bits   = len(dac)
levels = 2 ** bits
max_voltage = 3.3

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

GPIO.output(troyka, 0)

try:
    data = []
    start_time = time.time()

    GPIO.output(troyka, GPIO.LOW)
    while True:
        value = 3.3*adc()/256
        data.append(value)
        print(value)
        if value >= 0.97 * 3.3:
            break


    GPIO.output(troyka, GPIO.HIGH)
    while True:
        value = 3.3*adc()/256
        data.append(value)
        print(value)
        if value <= 0.02 * 3.3:
            break
            
    end_time = time.time()

    duration = end_time - start_time

    plt.plot(data)
    plt.xlabel('Measurement number')
    plt.ylabel('ADC value')
    plt.show()

    with open('data.txt', 'w') as f:
        for value in data:
            f.write(str(value) + '\n')

    sampling_rate = len(data) / duration
    quantization_step = 3.3 / 256
    with open('settings.txt', 'w') as f:
        f.write('Sampling rate: ' + str(sampling_rate) + '\n')
        f.write('Quantization step: ' + str(quantization_step) + '\n')

    print('Total duration:', duration, 'seconds')
    print('Sampling period:', duration / len(measurements), 'seconds')
    print('Sampling rate:', sampling_rate, 'Hz')
    print('Quantization step:', quantization_step, 'V')

finally:
    GPIO.cleanup()
