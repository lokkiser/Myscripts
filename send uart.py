import serial.tools.list_ports
import serial
import time
# import RPi.GPIO as GPIO
# GPIO.setwarnings(True)  # disable warnings
# GPIO.setmode(GPIO.BOARD)  # set pin numbering system

ports = serial.tools.list_ports.comports()

ledpin = 23  # PWM pin connected to LED

for port in ports:
    print(port.device)
ser = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.1)


# def _create_com_port(name_port, setting):
#     com_port = serial.Serial(name_port, timeout=PermanentSetting.timeout_rs)
#     com_port.baudrate = setting["baudrate_rs"]
#     com_port.parity = setting["parity_rs"]
#     com_port.stopbits = setting["stopBit_rs"]

# port = "COM8"  # Replace with the appropriate COM port name
# baudrate = 9600  # Replace with the desired baud rate

# ser = serial.Serial(port, baudrate=baudrate)
test0102_1 = {0xB5,0x62,0x01,0x07,0x92,0x00,0x00,0x00,0x00,0x00,0xE0,0x07,0x0A,0x15,0x16,0x14,0x1E,0x04,0x01,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x03,0x0C,0xE0,0x0B,0xB5,0x07,0x45,0xFF,0xE1,0x78,0x50,0x20,0xA8,0x5F,0x24,0x01,0x68,0xC3,0x23,0x01,0x01,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x2E,0x5E}
test0107_1 = {0xB5,0x62,0x01,0x07,0x92,0x00,0x00,0x00,0x00,0x00,0xE0,0x07,0x0A,0x15,0x16,0x0D,0x0A,0x04,0x01,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x03,0x0C,0xE0,0x0B,0x86,0xBE,0x2F,0xFF,0xAD,0x1F,0x21,0x20,0xE0,0xF2,0x09,0x00,0xA0,0x56,0x09,0x00,0x01,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x28,0xF3};
# B5 62 06 3E 3C 00 00 00 FF 07 00 0A 10 00 01 00 01 01 01 01 03 00 00 00 01 01 02 04 08 00 01 00 01 01 03 00 00 00 00 00 01 01 04 00 00 00 00 00 01 03 05 00 00 00 00 00 01 05 06 0A 10 00 01 00 01 01 F6 17
# {0xb5, 0x62, 0x06, 0x01, 0x08, 0x00, 0xF0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00};
# uint8_t test0107_1[100] = {0xB5,0x62,0x01,0x07,0x92,0x00,0x00,0x00,0x00,0x00,0xE0,0x07,0x0A,0x15,0x16,0x0D,0x0A,0x04,0x01,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x03,0x0C,0xE0,0x0B,0x86,0xBE,0x2F,0xFF,0xAD,0x1F,0x21,0x20,0xE0,0xF2,0x09,0x00,0xA0,0x56,0x09,0x00,0x01,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x28,0xF3};
# uint8_t test0107_2[100] = {0xB5,0x62,0x01,0x07,0x92,0x00,0x00,0x00,0x00,0x00,0xE0,0x07,0x0A,0x15,0x16,0x0D,0x14,0x04,0x01,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x03,0x0C,0xE0,0x0B,0x6F,0xE1,0x2E,0xFF,0x9C,0x6D,0x21,0x20,0xA0,0xE4,0x1B,0x00,0x60,0x48,0x1B,0x00,0x01,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x02,0x88};
# uint8_t test0107_3[100] = {0xB5,0x62,0x01,0x07,0x92,0x00,0x00,0x00,0x00,0x00,0xE0,0x07,0x0A,0x15,0x16,0x0D,0x1E,0x04,0x01,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x03,0x0C,0xE0,0x0B,0x18,0xD6,0x30,0xFF,0xF7,0x5D,0x21,0x20,0x48,0x8D,0x25,0x00,0x08,0xF1,0x24,0x00,0x01,0x00,0x00,0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xAC,0x9F};


# class PPS:
#     def __init__(self):
#         self.last_time = time.monotonic()
#         self.status = False
#         GPIO.setup(ledpin, GPIO.OUT)
#
#     def run(self):
#         if self.status:
#             if (self.last_time - time.monotonic()) <= 0.99:
#                 GPIO.output(ledpin, GPIO.HIGH)
#                 self.last_time = time.monotonic()
#                 self.status = False
#         else:
#             if (self.last_time - time.monotonic()) <= 0.01:
#                 GPIO.output(ledpin, GPIO.LOW)
#                 self.last_time = time.monotonic()
#                 self.status = True
test_seq = b'123'
ser.open()
def main():
    #pps = PPS()
    _ser_buf = ""
    while True:
        # for message in test0102_1:
        #     ser.write(message)
        # print("test0102_1")
        # for message in test0107_1:
        #     ser.write(message)
        # print("test0107_1")
        # pps.run()

        ser.write(test_seq)
        # time.sleep(0.1)
        _ser_buf = ser.readline()
        if _ser_buf:
            print(_ser_buf)

# Perform operations on the COM port


main()
ser.close()  # Remember to close the connection when done