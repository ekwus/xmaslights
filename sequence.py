from random import randint
from states import State

def clear_array(led_strip, state: State):
    for j in range(state.num_leds):
        led_strip.set_rgb(j, 0, 0, 0)

def chase_random(led_strip, state: State):
    # chase
    print("Chase Pattern, Random Colour")
    for i in range(4 * state.num_leds):
        clear_array(led_strip, state)
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        led_strip.set_rgb(i % state.num_leds, red, green, blue)
        state.sleep(50)
        if state.change == True:
            print("Cancelling")
            return

def run(led_strip, state: State):
    # run
    print("Run Pattern")
    for i in range(state.num_leds):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        led_strip.set_rgb(i, red, green, blue)
        #state.sleep(5)
        if state.change == True:
            print("Cancelling")
            return

    state.sleep(100)

def run_out(led_strip, state: State):
    # run out
    print("Run Out Pattern")
    for i in range(state.num_leds):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        led_strip.set_rgb(i, red, green, blue)
        state.sleep(50)
        if state.change == True:
            print("Cancelling")
            return

    state.sleep(100)
    
    clear_array(led_strip, state)

