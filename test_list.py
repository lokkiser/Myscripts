#import common_dictionary as comdict
import multiprocessing

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

    def regcollect(self):  # забор в  с инверсией
        __iter = 0
        print("test", self.but_dictionary)
        for keys in self.but_dictionary:
            self.buttons[__iter] = not self.but_dictionary[__iter]
            if debug:
                print(keys, __iter, not self.buttons[__iter])
            __iter = __iter + 1
        if debug:
            print("self.buttons[__iter] = ", self.buttons)

    def reg_collect3(self, iter_list):
        __iter = 0
        print("test", self.but_dictionary)

        for keys in iter_list:
            if self.buttons.count(keys):
                print(keys)
                #self.buttons[__iter] = not self.but_dictionary[__iter]
            else:
                pass
            if debug:
                print(keys, __iter, not self.buttons[__iter])
            __iter = __iter + 1
        if debug:
            print("self.buttons[__iter] = ", self.buttons)
# mylist = comdict.Internal()

class Test:
    def __init__(self):

        self.rear_typhon = False  # разрешение
        self.front_typhon = False  # разрешение
        self.lights_allow = False  # разрешение
        self.lights_state = 0  # тип сигнала
        self.typhon_state = 0
        self.brightness = 50
        self.time_state = 0  # тип сигнала времени
        self.time = 0  # время интервала повторения
        self.typhon_auto = False
        self.lights_auto = False
        self.typhon_manual = False
        self.lights_manual = False
        self.anchored = False
        self.aground = False

        self.rs_allow = True
        self.ether_allow = True
        self.i2c_allow = True

        self.input_list = list()
        self.output_list = list()

    def set_output_list(self, _pipes):  # внешние пайпы; get_input_list был

        if self.input_list:  # проверка элементов
            print(type(self.input_list))
            self.input_list = list(dict.fromkeys(self.input_list))  # убираем дубли
            for _elem in self.input_list:
                if debug:
                    print(_elem)


#                 if output_nmea_ethernet_send.poll():
#                     smi.send(output_nmea_ethernet_send.recv())

def set_led(led, status, inverted=True):
    brightness = 50
    # #status1 = not status  # выход открытый коллектор, именно так, отдельно, иначе ломается
    # duty_cycle = 0
    # if inverted:
    #     duty_cycle = 0xFFFF - duty_cycle * brightness
    # else:
    #     duty_cycle = (not status) * brightness * 0xFFFF / 100  # если True, светим нужной яркостью, иначе 0
    # duty_cycle = round(duty_cycle, 0) + 2

    _duty_cycle = 0
    if inverted:  # 0xFFFF выключено полностью
        _duty_cycle = 0xFFFF - (not status) * brightness * 0xFFFF / 100
    else:
        _duty_cycle = (not status) * brightness * 0xFFFF / 100  # если True, светим нужной яркостью, иначе 0
    duty_cycle = round(_duty_cycle) + 2
    print(type(duty_cycle))

    print("self.i2c_port.channels[led].duty_cycle", led, _duty_cycle, duty_cycle)





_pfc3_buf = [True, False, True, False]
print(_pfc3_buf)
_pfc3_buf.reverse()
print(_pfc3_buf)
while True & False:
    print("self.input_list.append")

pipe1, pipe2 = multiprocessing.Pipe()
my = Test()
my.set_output_list(pipe2)
set_led(1, 0)
set_led(1, 1)

a = 1
print(a//2, a%2)
a = [0,1,2,3]
b = [4,5,6,7]
z = [0,1,6,9]
c = list()
d = list()
c.extend(a)
c.extend(b)
d.append(a)
d.append(b)
print(a+b)
print(c)
print(d)
f = set()
# f.add(a)
# f.add(b)
# f.add(z)
# print(z)

if not pipe1.poll():
    print("pipe1")
    pipe2.send("error")
if pipe1.poll():
    _temp = pipe1.recv()
    print(_temp)
