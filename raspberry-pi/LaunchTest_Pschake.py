# Paul Schakel
# Launch Pad part 3

import board
import time
import digitalio

# Initialize variables for LEDs
led_red = digitalio.DigitalInOut(board.GP3)
led_green = digitalio.DigitalInOut(board.GP4)
led_red.direction = digitalio.Direction.OUTPUT
led_green.direction = digitalio.Direction.OUTPUT

# Initialize variables for button
button = digitalio.DigitalInOut(board.GP0)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP
button_prev = button.value

def countdown(x): # count down from x to 0 while blinking LED
    print("Starting Countdown...")
    while x > 0:
        print(f"{x} seconds left...")
        x -= 1

        # Turn LED on and off
        led_red.value = True
        time.sleep(.5)
        led_red.value = False
        time.sleep(.5)
        if button.value: # debouncing for button
            button_prev = button.value
        if not button.value and button_prev: # abort countdown
            print("Aborting...")
            led_red.value = False
            led_green.value = False
            button_prev = button.value
            return
    led_green.value = True
    print("Liftoff!")

while True:
    if button.value: # debouncing button
        button_prev = button.value
    if not button.value and button_prev: # start countdown
        led_green.value = False
        button_prev = button.value
        countdown(10)