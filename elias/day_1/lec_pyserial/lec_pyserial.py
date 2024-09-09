import serial
from icecream import ic
import time

# https://github.com/gruns/icecream
ic.configureOutput(includeContext=True)

################################################################
# Open Serial
################################################################
def openSerial(port, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE, timeout=None, xonxoff=False, rtscst=False,
               dsrdtr=False):

    # 시리얼 포트객체 생성
    ser = serial.Serial()

    # 시리얼 포트설정
    ser.port = port             # Port Name : com1, com2, ....
    ser.baudrate = baudrate     # Baudrate 속도 : 9600, 115200, ...
    ser.bytesize = bytesize     # Data Bit
    ser.parity = parity         # Check Parity
    ser.timeout = timeout       # None: 무한대기, 0: Non_Blocking Mode, N: n초 대기
    ser.xonxoff = xonxoff       # SW Flow Control
    ser.rtscts = rtscst         # RTS/CTS Flow Control
    ser.dsrdtr = dsrdtr         # DSR/DTR Flow Control

    # 시리얼 포트열기
    ser.open()

    # 시리얼 포트객체 생성시 포트설정값을 넣으면, open할 필요없음
    # ser = serial.Serial(port, baudrate, ...)

    return ser

################################################################
# Write Port
################################################################
def writePort(ser, data):
    ser.write(data)

if __name__ == '__main__':
    # 포트열기
    ser = openSerial(port='com2')

    # 포트쓰기
    writePort(ser, "HelloWorld")

    time.sleep(10)

























