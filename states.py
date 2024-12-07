import time

class State:
    MAX_STATES = 4
    _change = False
    _select = -1
    _num_leds = 0
    _rate = 0

    @property
    def change(self):
        return self._change

    @property
    def select(self):
        return self._select

    @property
    def num_leds(self):
        return self._num_leds
    
    @property
    def rate(self):
        return self._rate

    def __init__(self, num_leds, period):
        self._num_leds = num_leds
        self._rate = period/num_leds
        print("State Initialised")
        print("Rate {}".format(self._rate))
                
    def set_change(self, val):
        self._change = val
        print("Change {}".format(self._change))        

    def set_select(self, val):
        self._select = val
        print("Select {}".format(self._select))
        
    def inc_select(self):
        self._select += 1
        self._select = self._select % self.MAX_STATES
        print("Select {}".format(self._select))
    
    def get_delay(self, delay):
        return round(self._rate * delay)
    
    def sleep(self, delay):
        time.sleep_ms(self.get_delay(delay))
        

