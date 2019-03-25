"""
    coding      : UTF-8
    Environment : Python 3.6
    Author      : Benjamin142857
    Data        : ---------
"""
from math import *

a = float(input('input a:\n'))

theta_b = (float(input('input theta_b:\n'))/180)*pi
theta_c = (float(input('input theta_c:\n'))/180)*pi
theta_a = pi - theta_c - theta_b



b = a*(sin(theta_b)/sin(theta_a))
c = a*(sin(theta_c)/sin(theta_a))



print('b = {}\n'.format(b))
print('c = {}\n'.format(c))