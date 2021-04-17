

a=float(input('输入三角形的第一条边：'))
b=float(input('输入三角形的第一条边：'))
c=float(input('输入三角形的第一条边：'))

#计算半周长
s=(a+b+c)/2

#计算面积
area=(s*(s-a)*(s-b)*(s-c))**0.5
print('三角形面积为：%0.2f' %area)

