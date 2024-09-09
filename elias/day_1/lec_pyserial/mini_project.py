from lec_pyserial_class import MySerial
from icecream import ic

# Echo Server
# 입력받다가 Enter키가 입력되는 순간 그동안의 데이터를 출력하는 에코서버
# Exit, exit, EXIT, eXit, EXit lower() 들어오면 프로그램 종료`
# b'\x0d'

ser = MySerial()
ser.openSerial('com2')

ic('Echo Server is running...')

RETURN_CODE = b'\x0d'

while True:
    # Enter키가 입력될때까지 데이터를 Read
    readed = ser.readUntilExitCode(RETURN_CODE)
    ic(readed)

    # byte array --> Unicode String Object
    # 문자열 객체(Unicode)로 Decode 해야만 문자열 관련 내장함수 사용가능
    readed = readed.decode()
    ic(readed)

    # 프로그램 종료조건(exit) 확인
    if readed.lower() == 'exit':
        ic('Done')
        ser.writePortUnicode('Echo server is dead.\r\n')
        break

    response = readed + '\r\n'
    ic(response)
    ser.writePortUnicode(response)

ser.closePort()


















