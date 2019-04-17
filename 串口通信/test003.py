"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : ---------
"""

import serial
import sys
# import RPi.GPIO as GPIO
import time

class STM(object):
    def __init__(self,port="/dev/ttyAMA0",baudrate=115200,timeout=0.5):
        self.port=port
        self.baudrate=baudrate
        self.timeout=timeout
        self.data=bytearray(33)
        self.ports=["/dev/ttyAMA0","/dev/ttyAMA0"]
        self.i=0

    def TurnOn(self):
        try:
            self.ser=serial.Serial(self.port,self.baudrate,timeout=self.timeout)
            if self.ser.isOpen():
                print("Gyroscope is opened")
                return True
            else:
                self.TurnOn()
        except:
            print("串口打开失败，正在重试")
            time.sleep(0.5)
            if(self.i==0):
                self.i=1
            else:
                self.i=0
            self.port=self.ports[self.i]
            self.TurnOn()

    def Recive(self):
        while(True):
            try:
                #print 123
                self.ser.readinto(self.data)
                a=self.data.decode(encoding='utf-8')
                if ','in a:
                        print(a)
                        return a.encode('unicode-escape').decode('string_escape')
                else:
                        pass


                self.data=bytearray(33)
                '''
                if(self.data[0]==85)and(self.data[1]==81):#85是十六进制的55 代表包头
                    return self.datapros(self.data[28],self.data[29])
                else:
                    self.ser.reset_input_buffer()
                    raise Exception
                '''
            except:
                print("error")
                time.sleep(0.5)
                self.TurnOn()
    def Send(self,message):
        print(1)
        self.ser.write(message)
        self.ser.flushInput()
chip=STM()
chip.TurnOn()
while(1):
