# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 14:36:36 2019

@author: Administrator
"""

"""---第一个游戏猜数字---"""
temp=input("猜猜现在我想的数字：")
guess=int(temp)
if guess==8:
    print("猜对了，但是没有奖励。")
else:
    print("猜错了，我想的数字是8。")
print("游戏结束")