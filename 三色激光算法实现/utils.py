"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : 2019-04-16
"""

import cv2


# 单通道固定阈值范围筛选
def threshold_scope(frame, low, high):
    if low >= high:
        print('阈值输入有误')
        return False
    else:
        ret_1, trsh_1 = cv2.threshold(frame, high, 255, cv2.THRESH_TOZERO_INV)
        ret_2, trsh_2 = cv2.threshold(trsh_1, low, 255, cv2.THRESH_BINARY)

        return trsh_2


# 计算列表的平均值
def cal_list_mean(lst):
    # 判断是否空列表
    if len(lst) == 0:
        return 0
    else:
        sum_val = 0
        for i in lst:
            sum_val += i

        return sum_val/(len(lst))


# 获取二值化图片的光柱的横坐标
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

            res_x_list.append(cal_list_mean(temp_x_list))

        # 否则丢去
        else:
            pass

    ret = cal_list_mean(res_x_list)
    return ret


if __name__ == '__main__':
    pass
