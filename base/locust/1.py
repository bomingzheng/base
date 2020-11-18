"""
==============================
@author: bmz
@contact: bomz@dianzhong.com
@software: PyCharm
@file: 1.py
@time: 2020/11/13 16:15
@desc:
==============================
"""

def sum_number(*args):
    total = 0
    for k in args:
        total +=k
    return total

def min_number(x, y):
    if x>=y:
       x,y = y, x
    return x


