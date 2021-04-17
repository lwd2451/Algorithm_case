# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 14:43:27 2020

@author: Administrator
"""

#交换变量
#用户输入值
x=input('输入x的值：')
y=input('输入y的值：')
#利用临时变量交换
temp=x
x=y
y=temp
print('输出交换后的X值：{}'.format(x))
print('输出交换后的Y值：{}'.format(y))

#方法二
#不使用临时变量，使用x,y=y,x