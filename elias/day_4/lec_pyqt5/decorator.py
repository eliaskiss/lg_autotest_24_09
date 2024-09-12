from datetime import datetime
import time

def fun():
    print(datetime.now().strftime('%H:%M:%S'))
    print('fun')
    time.sleep(3)
    print(datetime.now().strftime('%H:%M:%S'))

def trace_time(func):
    def wrapper():
        print(datetime.now().strftime('%H:%M:%S'))
        func()
        print(datetime.now().strftime('%H:%M:%S'))
    return wrapper

@trace_time
def fun1():
    print('fun1')
    time.sleep(2)

@trace_time
def fun2():
    print('fun2')
    time.sleep(1)


if __name__ == '__main__':
    fun()
    print('#' * 10)
    fun1()
    print('#' * 10)
    fun2()