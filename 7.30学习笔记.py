# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:02:01 2020

@author: Bird L
"""

###输入年份和月份 输出天数 主要是闰年的判断（只有两种情况，1是能被4整除但不能被100整除，2是能被400整除）
def rn(year,mon):
    if mon == 2:
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            print(29)
        else:
            print(28)
    elif mon in [1,3,5,7,8,10,12]:
        print(31)
    elif mon in [4,6,9,11]:
        print(30)
while True:
    try:
        year,mon = [int(i) for i in input().split()]
        rn(year,mon)
    except:
        break