# -*- coding: utf-8 -*-

#圆的面积s=π*r*r
'''
#方法一
#定义方法来计算圆的面积
def findArea(r):
    PI=3.14
    return PI*(r*r)

a=input("输入半径：")

#调用方法
print("圆的面积为 %.6f" %findArea(a))

#方法二
'''
PI=3.14
r=input("输入半径：")
if r.isdigit():
    s=PI*pow(float(r),2)
    print("半径为{}的圆面积为：{:.3f}".format(r,s))
else:
    print("输入错误！")
