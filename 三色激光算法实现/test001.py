"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : ---------
"""
from math import *


def three_angle_one_side(a, theta_b, theta_c):

    theta_a = pi - theta_c - theta_b
    b = a * (sin(theta_b) / sin(theta_a))
    c = a * (sin(theta_c) / sin(theta_a))

    return b, c


def two_angle_about_view(theta_0, L, L_1, L_2):

    alpha = atan((L/(2*L_1))*tan((pi-theta_0)/2))
    beta = atan((L/(2*L_2))*tan((pi-theta_0)/2))

    return alpha, beta


def get_phi(theta_0, L, L_1, L_2):
    theta_0 = theta_0 * (pi / 180)

    alpha, beta = two_angle_about_view(theta_0, L, L_1, L_2)
    b, c = three_angle_one_side(L_1-L_2, alpha, beta)
    temp_x = sqrt(L_2**2 + b**2 - 2*L_2*b*cos(pi - beta))

    phi_0 = acos((L_1**2 + temp_x**2 - c**2)/(2*temp_x*L_1)) * (180 / pi)

    return phi_0


def get_s(theta_0, phi, Lr, L, L_1):
    # 暂时假设实际中 Lr = 1m
    theta_0 = theta_0 * (pi / 180)
    phi = (phi-90) * (pi / 180)

    # s = (Lr*( (L/2)*(1/tan(theta_0/2)) + L_1*sin(phi)))/(L_1*cos(phi))
    s = (Lr * ((L / 2) * (1 / tan(theta_0 / 2)) + L_1 * (1/tan(pi/2-phi)))) / (L_1 * (1/sin(pi/2-phi)))

    return s


def get_xy(s, phi):
    phi = phi * (pi / 180)
    x = s * cos(phi)
    y = s * sin(phi)

    return x, y

if __name__ == '__main__':
    x = [90, 17.5, 10, 3.3, 2.5]
    print('-------------------------------------------------')
    print('输入模拟信息 : 相机视角[{}], 像素总宽[{}], 两光柱间距离[{}], A\'B\'[{}], A\'C\'[{}]\n'.format(*x))
    phi_1 = get_phi(x[0], x[1], x[3], x[4]) + 90
    s_1 = get_s(x[0], phi_1, x[2], x[1], x[3])
    x_1, y_1 = get_xy(s_1, phi_1)
    #
    # phi_2 = get_phi(90, 50, 10, 2) + 90
    # s_2 = get_s(90, phi_2, 1, 50, 10)
    # x_2, y_2 = get_xy(s_2, phi_2)
    #
    # phi_3 = get_phi(90, 50, 10, 3) + 90
    # s_3 = get_s(90, phi_3, 1, 50, 10)
    # x_3, y_3 = get_xy(s_3, phi_3)
    #
    # phi_4 = get_phi(90, 50, 0.1, 0.01) + 90
    # s_4 = get_s(90, phi_4, 1, 50, 0.1)
    # x_4, y_4 = get_xy(s_4, phi_4)

    print('phi_1(向量与x轴正方向夹角) = {}\ns(与原点距离) = {}\n(x, y) = ({}, {})\n'.format(phi_1, s_1, x_1, -y_1))
    print('-------------------------------------------------')
    # print('phi_2(向量与x轴正方向夹角) = {}\ns(与原点距离) = {}\n(x, y) = ({}, {})\n'.format(phi_2, s_2, x_2, -y_2))
    # print('phi_3(向量与x轴正方向夹角) = {}\ns(与原点距离) = {}\n(x, y) = ({}, {})\n'.format(phi_3, s_3, x_3, -y_3))
    # print('phi_4(向量与x轴正方向夹角) = {}\ns(与原点距离) = {}\n(x, y) = ({}, {})\n'.format(phi_4, s_4, x_4, -y_4))

