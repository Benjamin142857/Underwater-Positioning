"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : ---------
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


def trsh_bet(low, high, frame):
    ret_1, trsh_1 = cv2.threshold(frame, high, 255, cv2.THRESH_TOZERO_INV)
    ret_2, trsh_2 = cv2.threshold(trsh_1, low, 255, cv2.THRESH_BINARY)

    return trsh_2


def get_list_mean(lst):
    # 空列表
    if len(lst)==0:
        return 0
    else:
        sum_val = 0
        for i in lst:
            sum_val += i

        return sum_val/(len(lst))


def get_one_x(img, min_dot, max_dot):
    get_y_list = [y for y in range(600) if y%10 == 0]
    res_x_list = []
    for y in get_y_list:
        x_vec = img[y][:]
        # 取点数在 min_dot ~ max_dot 之间的横线
        if (x_vec.sum()/255 >= min_dot) & (x_vec.sum()/255 <= max_dot):
            temp_x_list = []
            for x, val in enumerate(x_vec):
                if val != 0:
                    temp_x_list.append(x)

            res_x_list.append(get_list_mean(temp_x_list))

        # 否则丢去
        else:
            pass

    return get_list_mean(res_x_list)

if __name__ == '__main__':
    pass
    img = cv2.imread('a.jpg')
    print(type(img)==)
    # b, g, r = cv2.split(img)
    #
    # trsh = trsh_bet(156, 166, g)
    #
    #
    #
    # get_y_list = [y for y in range(600) if y%10 == 0]
    # res_x_list = []
    # for y in get_y_list:
    #     x_vec = trsh[y][:]
    #     # 取点数在 10~35 之间的横线
    #     if (x_vec.sum()/255 >= 10) & (x_vec.sum()/255 <= 35):
    #         temp_x_list = []
    #         for x, val in enumerate(x_vec):
    #             if val != 0:
    #                 temp_x_list.append(x)
    #
    #         res_x_list.append(get_list_mean(temp_x_list))
    #
    #     else:
    #         pass
    #
    #
    # print(get_list_mean(res_x_list))
        # for x, val in enumerate(trsh[y][:]):
        #     # for idx in range()
        #     # if (val.sum()/255 > 10) & (val.sum()/255 < 35):
        #     #     print(idx, val.sum()/255)
        #     print(x, val.sum() / 255)


    # cv2.imshow('trsh', trsh)
    #
    # key = cv2.waitKey(0)
    # if key == 27:
    #     cv2.destroyAllWindows()
    # elif key == ord('s'):
    #     cv2.imwrite('gray_touxiang.jpg', trsh)
    #     cv2.destroyAllWindows()
