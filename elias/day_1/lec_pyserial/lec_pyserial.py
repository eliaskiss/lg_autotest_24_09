import serial
from icecream import ic
import time

# https://github.com/gruns/icecream
ic.configureOutput(includeContext=True)

################################################################
# Open Serial
################################################################
def openSerial(port, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE, timeout=None, xonxoff=False, rtscts=False,
               dsrdtr=False):

    # 시리얼 포트객체 생성
    ser = serial.Serial()

    # 시리얼 포트설정
    ser.port = port             # Port Name : com1, com2, ....
    ser.stopbits = stopbits
    ser.baudrate = baudrate     # Baudrate 속도 : 9600, 115200, ...
    ser.bytesize = bytesize     # Data Bit
    ser.parity = parity         # Check Parity
    ser.timeout = timeout       # None: 무한대기, 0: Non_Blocking Mode, N: n초 대기
    ser.xonxoff = xonxoff       # SW Flow Control
    ser.rtscts = rtscts         # RTS/CTS Flow Control
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

def writePortUnicode(ser, data, encode='utf-8'):
    writePort(ser, data.encode(encode))

################################################################
# Read Port
################################################################
def read(ser, size=1, timeout=None):
    ser.timeout = timeout
    readed = ser.read(size)
    return readed

################################################################
# Read EOF
# Putty에서 EOF --> Ctrl + j
################################################################
def readEOF(ser):
    readed = ser.readline()
    return readed[:-1]


if __name__ == '__main__':
    # 포트열기
    ser = openSerial(port='com2')

    # # 포트쓰기
    # data = "HelloWorld"
    # enc_data = data.encode()
    # writePort(ser, enc_data)        # 인코딩 후 인자로 전달
    # writePortUnicode(ser, data)     # 인코딩 없이 인자로 전달

    # # 1 byte만 읽기
    # ic(read(ser))

    # # 10 byte 읽기
    # ic(read(ser, 10))

    # EOF 까지 읽기
    ic(readEOF(ser))

    # time.sleep(10)

























