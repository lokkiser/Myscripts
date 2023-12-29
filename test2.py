import time
but_typhon_select = False  # K1
but_lights_active_select = False  # K2
but_lights_signal_select = False  # K3
but_typhon_auto = False  # K4
but_anchored = False  # K5
but_dimmer_up = False  # K6
but_lights_auto= False  # K7
but_typhon_manual= False  # K8
but_typhon_signal_select = False  # K9
but_time = False  # K10
but_aground = False   # K11
but_dimmer_down = False  # K12
but_lights_manual = False  # K13

input_control = ("TYPHONACTIVE", "LIGHTSACTIVE", "LIGHTSSELECT", "TYPHONAUTO", "ANCHOR", "DIMMERUP",
                 "LIGHTSAUTO", "TYPHONMANUAL", "TYPHONSELECT", "TIMESELECT", "AGROUND", "DIMMERDOWN", "LIGHTSMANUAL")

dict_of_buttons = dict.fromkeys(["but_typhon_select", "but_lights_active_select", "but_lights_signal_select",
                         "but_typhon_auto", "but_anchored", "but_dimmer_up", "but_lights_auto",
                         "but_typhon_manual", "but_typhon_signal_select", "but_time", "but_aground",
                         "but_dimmer_down", "but_lights_manual"], False)
buttons_pressed = ([])
common_buttons = ([])
buttons_remote = ([])
buttons_remote = ("LIGHTSSELECT", "DIMMERDOWN")
#buttons_remote.append()
print (dict_of_buttons)
temp_buttons = [True] * 16 #i2c3.port
temp_buttons[1] = False
temp_buttons [2] = False
temp_buttons[5] = False
temp_buttons[11] = False

button_number = 0
print (dict_of_buttons)
while True:
    button_number = 0
    for key in dict_of_buttons:
        #print (key)
        dict_of_buttons[key] = temp_buttons[button_number]
        button_number = button_number + 1
       # print (key , dict_of_buttons[key] , button_number)
        
# def button_check(self, i2c3):  # попытка переписать логику на положительную
#   temp_buttons = i2c3.Port  # забор из расширителя
    button_number = 0
    for key in input_control:  # опрос кнопок и заполнение словаря
        #print(key)
        if not temp_buttons[button_number]:  # False по кнопке
            buttons_pressed.append(input_control[button_number])
            #print(key, buttons_pressed)
            pass
        # self.dict_of_buttons[key] = temp_buttons[button_number]
        button_number = button_number + 1
    if buttons_pressed:
        #print ("any buttons_pressed")
        common_buttons = buttons_pressed.copy()
        #print ("common_buttons", common_buttons)
    #button_number = 0 # alternative
    #for key in buttons_pressed:
        #print(buttons_pressed[button_number])
        #time.sleep(0.25)
        #button_number = button_number + 1
        
        #pass
    #buttons_pressed.clear()
    if buttons_remote:
        common_buttons.extend(buttons_remote)
    print (common_buttons, "common_buttons")
    time.sleep(0.1)
    buttons_pressed.clear()
    common_buttons.clear()
    
