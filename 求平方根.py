# -*- coding: utf-8 -*-


#方法一
num=float(input('请输入一个数字：'))
num_sqrt=num**0.5
print('%0.3f的平方根是%0.3f' %(num,num_sqrt))


#方法二
'''计算复数（负数）的平方根
import cmath
num=int(input("请输入一个数字："))
num_sqrt=cmath.sqrt(num)
print('{0}的平方根是{1:0.3f}+{2:0.3f}i'.format(num,num_sqrt.real,num_sqrt.imag))
'''

