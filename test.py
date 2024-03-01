from first import first
from time import sleep
import RPi.GPIO as GPIO
import subprocess
ledpin = 12				# PWM pin connected to LED _ 32 нога PWM0
GPIO.setwarnings(True)			#disable warnings
GPIO.setmode(GPIO.BCM)		#set pin numbering system USE BCM
GPIO.setup(ledpin,GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin,4000)		#creat e PWM instance with frequency
pi_pwm.start(0)				#start PWM of required Duty Cycle 

vN=[]
vN.append([0,181,179])
vN.append([180,359,1])
vN.append([0,170,185])
vN[2].append(6)
print (vN[0])
print (vN[2])
print (vN[2][0])
print (vN[2][3])
class Ebuchka:
    def __init__(self):
        self.ok = True
    def Dat(self):
        self.ok = False
    
resequences = dict([(0, "MOVING"), (1, "STILL"), (2, "ANCHORED"),(3, "REVERSE"), (4, "NOMOVING"),
                               (5, "TOWED"), (6, "STAYAWAY"), (7, "AGROUND"),
                               (8, "ATTENTION"), (9, "MOVERIGHT"), (10, "MOVELEFT"), (11, "REVERSE")])
sequences = dict([("MOVING", 0), ("STILL", 1), ("ANCHORED", 2),("REVERSEHORN", 3), ("NOMOVING", 4),
                               ("TOWED", 5), ("STAYAWAY", 6), ("AGROUND", 7),
                               ("ATTENTION", 8), ("MOVERIGHT", 9), ("MOVELEFT", 10), ("REVERSELIGHT", 11)])
clear = dict()
d  =  {'dict': 1, 'dictionary': 2} 
if (d.get('dict',False)):
    print ('ok')
if (d.get('dict',False) or d.get('dictionary',False)):
    print ('toje ok')

#if (vN.get('170',False)):
 #   print ('poidet')
print (resequences.get(0))
print (sequences.get("MOVERIGHT"))
print(clear.items())
if clear:
    print (clear.items()," again")
clear.update ([(1, "E")])
if clear:
    print (clear.items()," again")
print(first(clear))
print(clear[first(clear)])

output_message = ["a", "b"]
print (type(output_message)) #list, not dict
print (output_message)
output_message.append("eba")
output_message.append("ebat")
output_message.append("ebati")
#set (output_message)

print (output_message.count("eba"))
if output_message.count("eba"):
    print ("Eba dal")

output_message.pop()
print (output_message)




input_control = ("TYPHONACTIVE", "LIGHTSACTIVE", "LIGHTSSELECT", "TYPHONAUTO", "ANCHOR", "DIMMERUP", 
                                 "LIGHTSAUTO", "TYPHONMANUAL", "TYPHONSELECT", "TIMESELECT", "AGROUND", "DIMMERDOWN",
                                "LIGHTSMANUAL")

if (input_control.count("TYPHONACTIVE")):
    print ("TYPTONACTIVE")
if (input_control.count("LIGHTSAUTO")):
    print("LIGHTSAUTO")
typhonState = 3
print("typhonState % 2")
if typhonState % 2:
    print ("+")
else :
    print ("-")

if typhonState / 2:
    print ("+")
else :
    print ("-")
    

# for duty in range(0,10,1):
#     subprocess.run(f"/home/user/RPi-USB-Brightness/64/lite/Raspi_USB_Backlight_nogui -b {duty}", shell=True)
#     print ("duty ",duty)
#     #pi_pwm.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
#     sleep(1)
# sleep(0.5)
#
# for duty in range(10,-1,-1):
#     subprocess.run(f"/home/user/RPi-USB-Brightness/64/lite/Raspi_USB_Backlight_nogui -b {duty}", shell=True)
#     print ("duty ",duty)
#     #pi_pwm.ChangeDutyCycle(duty)
#     sleep(1)
# sleep(0.5)
#
#

initial = "120_sec"
