from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import PWMLED, Device, LED
from time import sleep

PWM1_PIN = 12
PWM2_PIN = 13
EN1_PIN = 22
EN2_PIN = 23
DIR1_PIN = 24
DIR2_PIN = 25

Device.pin_factory = PiGPIOFactory(host='10.42.0.1')

pwm1 = PWMLED(12)
pwm2 = PWMLED(13)
en1 = LED(22)
en2 = LED(23)
dir1 = LED(24)
dir2 = LED(25)

def enable():
    en1.on()
    en2.on()

def disable():
    en1.off()
    en2.off()

# Takes two [-1, 1] values
def set(m1_speed, m2_speed):
    if(m1_speed < 0):
        m1_speed = -m1_speed
        m1_dir_value = 1
    else:
        m1_dir_value = 0
    if(m2_speed < 0):
        m2_speed = -m2_speed
        m2_dir_value = 1
    else:
        m2_dir_value = 0


    if(m1_speed > 1):
        m1_speed = 1

    if(m2_speed > 1):
        m2_speed = 1
    
    dir1.value = m1_dir_value
    dir2.value = m2_dir_value

    pwm1.value = m1_speed
    pwm2.value = m2_speed

enable()
set(0,0)
sleep(5)
set(1,0)
sleep(5)
set(.5,.5)
sleep(5)
set(0,1)
sleep(5)
set(0,0)
disable()
