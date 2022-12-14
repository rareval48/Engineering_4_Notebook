# type: ignore
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import time

led = digitalio.DigitalInOut(board.GP3) # tells board the led output
led.direction = digitalio.Direction.OUTPUT

led1 = digitalio.DigitalInOut(board.GP4) # tells board the led output
led1.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP0)
button.pull = digitalio.Pull.UP

if button.value == True:
    for x in range(10, 0, -1):
        print (x) # This prints x
        led.value = True # This makes the led value true
        time.sleep(.5)
        led.value = False # This makes the led value true
        time.sleep(.5) 

print("LAUNCH")

while True:
    led1.value = True

