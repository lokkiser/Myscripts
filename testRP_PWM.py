import RPi.GPIO as GPIO
from time import sleep

ledpin = 12				# PWM pin connected to LED gpio 12
GPIO.setwarnings(True)			# disable warnings
GPIO.setmode(GPIO.BCM)		# set pin numbering system
GPIO.setup(ledpin, GPIO.OUT)
pi_pwm = GPIO.PWM(ledpin, 1000)		# create PWM instance with frequency
pi_pwm.start(0)				# start PWM of required Duty Cycle

pi_pwm.ChangeDutyCycle(1)
while True:
    pass
# while True:
#     print("going up")
#     for duty in range(0, 101, 1):
#         if duty > 10:
#             pi_pwm.ChangeDutyCycle(100)  # provide duty cycle in the range 0-100
#         elif duty > 50:
#             pi_pwm.ChangeDutyCycle(50)  # provide duty cycle in the range 0-100
#         elif duty > 80:
#             pi_pwm.ChangeDutyCycle(10)  # provide duty cycle in the range 0-100
#         sleep(0.1)
#     sleep(0.5)
#     print("going down")
#     for duty in range(100, -1,- 1):
#         if duty > 10:
#             pi_pwm.ChangeDutyCycle(100)  # provide duty cycle in the range 0-100
#         elif duty > 50:
#             pi_pwm.ChangeDutyCycle(50)  # provide duty cycle in the range 0-100
#         elif duty > 80:
#             pi_pwm.ChangeDutyCycle(10)  # provide duty cycle in the range 0-100
#         sleep(0.1)
#     sleep(0.5)
