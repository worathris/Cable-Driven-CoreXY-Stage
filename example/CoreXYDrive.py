from machine import Pin,PWM
from picozero import LED
from math import sin, cos, pi
import utime

# Direction and enable pins (use machine.Pin)
DIR1_PIN = Pin(21, Pin.OUT)
EN1_PIN = Pin(19, Pin.OUT, value=0)

DIR2_PIN = Pin(18, Pin.OUT)
EN2_PIN = Pin(16, Pin.OUT, value=0)

# Wrap STEP pins as LEDs
STEP1_PIN = Pin(20, Pin.OUT)  # Motor A step pin
STEP2_PIN = Pin(17, Pin.OUT)  # Motor B step pin

def step_motor(step_pin, delay=1250):
    step_pin.value(1)
    utime.sleep_us(delay)  # Delay in microseconds
    step_pin.value(0)  # Set the pin low
    utime.sleep_us(delay)  # Delay after pulse

def corexy_move(X, Y): # X and Y are in mm
    r = 12
    microstep = 1
    N = 200 *microstep #1.8° per step
    n1 = int(N*(X*sin(pi/4)+Y*sin(pi/4))/(2*pi*r))
    n2 = int(N*(X*sin(pi/4)-Y*sin(pi/4))/(2*pi*r))
    DIR1_PIN.value(0 if n1 >= 0 else 1)
    DIR2_PIN.value(0 if n2 >= 0 else 1)
    EN1_PIN.value(1)
    EN2_PIN.value(1)
    x = abs(n1)
    y = abs(n2)
    while x > 0 or y > 0:
        if x > 0:
            step_motor(STEP1_PIN)
            x -= 1
        if y > 0:
            step_motor(STEP2_PIN)
            y -= 1
        print("x: , y: ",x,y)
    EN1_PIN.value(0)
    EN2_PIN.value(0)
corexy_move(0, 50)
corexy_move(50, 0)
corexy_move(0, -50)
corexy_move(-50, 0)