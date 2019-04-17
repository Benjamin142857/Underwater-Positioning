"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : ---------
"""
import serial

def port_open(ser):
    ser.port = "COM7"  # 设置端口号
    ser.baudrate = 9600  # 设置波特率
    ser.bytesize = 8  # 设置数据位
    ser.stopbits = 1  # 设置停止位
    ser.parity = "N"  # 设置校验位
    ser.open()  # 打开串口,要找到对的串口号才会成功
    if (ser.isOpen()):
        print("打开成功")
    else:
        print("打开失败")



if __name__ == "__main__":
    ser = serial.Serial()

    port_open(ser)