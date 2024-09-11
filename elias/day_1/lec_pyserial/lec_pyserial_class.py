import serial
from icecream import ic
import time

# https://github.com/gruns/icecream
ic.configureOutput(includeContext=True)

class MySerial:
    def __init__(self):
        self.ser = None

    ################################################################
    # Open Serial
    ################################################################
    def openSerial(self, port, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE, timeout=None, xonxoff=False, rtscts=False,
                   dsrdtr=False):

        # 시리얼 포트객체 생성
        self.ser = serial.Serial()

        # 시리얼 포트설정
        self.ser.port = port             # Port Name : com1, com2, ....
        self.ser.stopbits = stopbits
        self.ser.baudrate = baudrate     # Baudrate 속도 : 9600, 115200, ...
        self.ser.bytesize = bytesize     # Data Bit
        self.ser.parity = parity         # Check Parity
        self.ser.timeout = timeout       # None: 무한대기, 0: Non_Blocking Mode, N: n초 대기
        self.ser.xonxoff = xonxoff       # SW Flow Control
        self.ser.rtscts = rtscts         # RTS/CTS Flow Control
        self.ser.dsrdtr = dsrdtr         # DSR/DTR Flow Control

        # 시리얼 포트열기
        self.ser.open()

    ################################################################
    # Write Port
    ################################################################
    def writePort(self, data):
        if self.ser is not None:
            self.ser.write(data)

    def writePortUnicode(self, data, encode='utf-8'):
        self.writePort(data.encode(encode))

    ################################################################
    # Read Port
    ################################################################
    def read(self, size=1, timeout=None):
        self.ser.timeout = timeout
        readed = self.ser.read(size)
        return readed

    ################################################################
    # Read EOF
    # Putty에서 EOF --> Ctrl + j
    ################################################################
    def readEOF(self):
        readed = self.ser.readline()
        return readed[:-1]

    ################################################################
    # Read Until ExitCode
    # Ctrl + C  가 들어올때까지
    ################################################################
    def readUntilExitCode(self, code=b'\x03'):
        readed = b''
        while True:
            data = self.ser.read()
            # ic(data)
            readed += data

            if data == code:
                return readed[:-1]

    ################################################################
    # Close Port
    ################################################################
    def closePort(self):
        self.ser.close()

if __name__ == '__main__':
    # 포트열기
    ser = MySerial()
    print(ser)
    # ser.openSerial(port='com2')
    #
    # # # 포트쓰기
    # # data = "HelloWorld"
    # # enc_data = data.encode()
    # # ser.writePort(enc_data)        # 인코딩 후 인자로 전달
    # # ser.writePortUnicode(data)     # 인코딩 없이 인자로 전달
    #
    # # # 1 byte만 읽기
    # # ic(ser.read(1, 5))
    #
    # # # 10 byte 읽기
    # # ic(ser.read(10))
    #
    # # # EOF 까지 읽기
    # # ic(ser.readEOF())
    #
    # # # 특정코드(Ctrl + C)가 들어올때까지 읽기
    # # ic(ser.readUntilExitCode())
    #
    # ser.closePort()

























