#####coding=utf-8
####递归：斐波拉契数列
####
import sys
#print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)
def fei(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    else:
        return fei(x-1)+x
print(fei(10))###python的递归深度只有1000，超过1000就报错了
#####调用自己的方式称作递归,递归函数调用次数很大，效率较低
import timeit
def jienew(m):
    if m == 0:
        return 1
    if m == 1:
        return 1
    return jienew(m-1)*m
print(timeit.timeit(stmt="jienew(1500)",setup="from __main__ import jienew",number=10))
####timeit函數 stmt参数中是需要执行的代码，setup参数中声明函数的来源
#print(help(timeit.timeit))

def jie(n):
    ret = 1
    for i in range(1,n+1):
        ret *= i
    return ret
print(timeit.timeit(stmt="jie(1500)",setup="from __main__ import jie",number=10))
#print(timeit.timeit(jie(6),number=10))
#####循环的效率要高于递归
#####所有循环都可以转换成递归，但不是所有递归都能转换成循环，递归需要在运算过程中频繁入栈和出栈

