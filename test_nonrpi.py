transmission_code = dict(
    [("manual_mode", 900), ("auto_mode", 901), ("moving_typhon", 910), ("still_typhon", 911), ("anchored_typhon", 912),
     ("reverse_horn_typhon", 913), ("no_moving_typhon", 914), ("towed_typhon", 915),
     ("stay_away_typhon", 916), ("aground_typhon", 917),
     ("manual_typhon", 928), ("typhon_error", 929), ("attention_lights", 930), ("move_right_lights", 931),
     ("move_left_lights", 932), ("reverse_lights", 933), ("manual_lights", 948), ("lights_error", 949),
     ("hong_error", 958), ("bell_error", 959)])

transmitable_manual = ("manual_typhon", "manual_lights")
_transmission_code = transmission_code
_transmission_code.pop("manual_typhon")
print(_transmission_code)
_transmission_code.pop("manual_lights")  #
print(_transmission_code)

a = 1
b = 2
c, d = a, b
print (c,d)