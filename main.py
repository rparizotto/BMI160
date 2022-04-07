# https://github.com/serioeseGmbH/BMI160
#https://www.mouser.com/datasheet/2/783/BST-BMI160-DS000-1509569.pdf

from machine import Pin, I2C
from BMI160 import BMI160_I2C
from time import sleep_ms
import time
import math
i2c_sensor0 = I2C(sda=Pin(16), scl=Pin(17))
i2c_sensor1 = I2C(sda=Pin(25), scl=Pin(26))

bmi160_s0 = BMI160_I2C(i2c_sensor0)
bmi160_s1 = BMI160_I2C(i2c_sensor1)

bmi160_s0.set_accel_rate(11) #800Hz
bmi160_s1.set_accel_rate(11) #800Hz

#while True:
#    print("{0:>8}{1:>8}{2:>8}".format(*bmi160.getAcceleration()))
#    sleep_ms(1000//25)

def get_v(x):
    return math.sqrt(x[0]**2 + x[1]**2 + x[2]**2)
#Acceleration
f = 500 #Hz
sleepinterval = 1000*1//f

def measure_acceleration():
    print("Starting measurement")
    i = 0
    while True:
        tick = time.ticks_us()
        a_s0 = bmi160_s0.getAcceleration()
        #tick1 = time.ticks_us()
        a_s1 = bmi160_s1.getAcceleration()
        tick2 = time.ticks_us()
        #print(str(tick2-tick1))
        out0 = "D$:" + str(tick/1000000) + "|" + str(get_v(a_s0)) + "|" + str(get_v(a_s1))        
        print(out0)
        i = i + 1
        #sleep_ms(1000//25)
        #sleep_ms(sleepinterval)
        if i%10 == 0:
            tickdiff = (tick2-tick)/1000000
            print("[info] Tick" + str(tickdiff))
        

measure_acceleration()