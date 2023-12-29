
debug = True

class Buttons:
    def __init__(self):
        self.but_typhon_select = False  # K1
        self.but_lights_active_select = False  # K2
        self.but_lights_signal_select = False  # K3
        self.but_typhon_auto = False  # K4
        self.but_anchored = False  # K5
        self.but_dimmer_up = False  # K6
        self.but_lights_auto = False  # K7
        self.but_typhon_manual = False  # K8
        self.but_typhon_signal_select = False  # K9
        self.but_time = False  # K10
        self.but_aground = False   # K11
        self.but_dimmer_down = False  # K12
        self.but_lights_manual = False  # K13
        self.but_dictionary = list(self.__dict__.keys())
        self.buttons = [True] * 16
        Port = [False] * 16
        if debug:
            print(self.but_dictionary)

    def get_i2c(self, i2c):
        self.regcollect()
        #i2c0.Port = self.upper_led.reverse()
        Port = self.buttons

    def regcollect(self):
        __iter = 0
        for keys in self.but_dictionary:
            self.buttons[__iter] = not self.but_dictionary[__iter]
            __iter = __iter + 1
            if debug:
                print(keys, __iter - 1, not self.buttons[__iter])
                
        if debug:
            print("self.buttons[__iter] = ", self.buttons)

        
        
my = Buttons()
my.regcollect()
