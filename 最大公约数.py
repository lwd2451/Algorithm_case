# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:14:47 2020

@author: Administrator
"""
"""
计算两个非负整数num_1和num_2的最大公约数：
若num_2=0，则最大公约数为num_1；
若num_2≠0，则将num_1除以num_2得到余数 r；
num_1和num_2的最大公约数即为num_2和 r 的最大公约数


print("计算两个非负整数的最大公约数")
num_1 = int(input("请输入第一个非负整数："))
num_2 = int(input("请输入第二个非负整数："))
def gcd(num_1,num_2):
    p,q=max(num_1,num_2),min(num_1,num_2)
    if q == 0:
        return p
    r = p%q
    return gcd(q,r) 
print("\n%s和%s的最大公约数是%s"%(num_1,num_2,gcd(num_1,num_2)))
"""

#-*-coding:utf-8-*- 
# 扩展欧几里得算法
# 输入m n 
# 输出 m n的最大公约数 还有s,t
# 
# 默认 m > n
 
import sys
 
def exgcd(m,n,x,y):
	if n == 0:
		x = 1
		y = 0
		return (m,x,y)
	a1 = b = 1
	a = b1 = 0
	c = m
	d = n
	q = int(c/d)
	r = c%d
	while r:
		c = d
		d = r
		t = a1
		a1 = a
		a = t-q*a
		t = b1
		b1 = b
		b = t-q*b
		q = int(c/d)
		r = c%d
	x = a
	y = b
	return (d,x,y)
 
m = int(sys.argv[1])
n = int(sys.argv[2])
ans = exgcd(m,n,0,0)
 
print("gcd(%d,%d) = %d"%(m,n,ans[0]))
print("s = %d, t = %d"%(ans[1],ans[2]))
