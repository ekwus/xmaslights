
from machine import Pin
import plasma
from plasma import plasma2040
import time
from random import randint
from sequence import chase_random, run, run_out, clear_array
from states import State

# Set how many LEDs you have
NUM_LEDS = 900 #66 300
state = State(NUM_LEDS,100)

# Setup for the button pins
user_button = machine.Pin(22, machine.Pin.IN)
a_button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

def button_isr(pin):
    print("INTERRUPT")
    if pin == user_button:
        print("INTERRUPT USER BTN")
        state.set_select(-1)
        state.set_change(True)
        
    if pin == a_button:
        print("INTERRUPT A BTN")
        state.inc_select()
        state.set_change(True)

a_button.irq(trigger=Pin.IRQ_FALLING,handler=button_isr)
user_button.irq(trigger=Pin.IRQ_FALLING,handler=button_isr)
  
# WS2812 / NeoPixel™ LEDs
led_strip = plasma.WS2812(NUM_LEDS, 0, 0, plasma2040.DAT, rgbw=True)

# Start updating the LED strip
led_strip.start()

print("NeoPixel Xmas Controller")
while True:
    if state.select == 0:
        clear_array(led_strip, state)
        state.inc_select()

    if state.select == 1:
        print("Selected 1")
        state.set_change(False)
        chase_random(led_strip, state)
        #clear_array(led_strip, state)

    if state.select == 2:
        print("Selected 2")
        state.set_change(False)
        run_out(led_strip, state)

    if state.select == 3:
        print("Selected 3")
        state.set_change(False)
        run(led_strip, state)

    time.sleep(0.2)