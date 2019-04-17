"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : ---------
"""
import cv2
import numpy as np
from utils import *

if __name__ == '__main__':

    input_movie = cv2.VideoCapture(1)
    input_movie.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
    input_movie.set(cv2.CAP_PROP_FRAME_HEIGHT, 540)

    while (True):
        # 获取一帧
        ret, frame = input_movie.read()
        b, g, r = cv2.split(frame)
        trsh = threshold_scope(156, 166, g)


        print(get_one_x(trsh, 10, 35))


        # 显示图像
        cv2.imshow('g', trsh)
        if cv2.waitKey(1) == ord('q'):
            break
        elif cv2.waitKey(1) == ord('w'):
            cv2.imwrite('a.jpg', frame)
