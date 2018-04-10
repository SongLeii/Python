######coding=utf-8
#####timeit实现

import time
def sleep(x):
    time.sleep(x)

def timeit(fun,*args,**kwargs):
    starttime = time.time()
    durning = fun(*args,**kwargs) ####赋值的过程也是调用
    ret = print(time.time()-starttime)
    return ret

print(timeit(sleep,1))#####发生在调用的时候
y = lambda x:time.sleep(x)
print(timeit(y,1))


def lei(lst):
    return sum(lst)
a = lei(range(10))##### 赋值的过程中也是调用的过程

fn = timeit(lei,range(100))
print(fn)

#####timeit的另外一种实现方式
def timeit1(fun):#####定义装饰器
    def parameter(*args,**kwargs):####装饰器内部再定义一个封装函数
        start = time.time()
        durning = fun(*args,**kwargs)####装饰器传入的函数，在传入的函数前后做一些操作
        print(time.time()-start)
        return durning#####返回传入的函数参数
    return parameter####返回封装函数
####这是常规调用方式
b = timeit1(lei)####函数可以进行赋值
print(b(range(100)))
####装饰器调用方法
@timeit1###调用装饰器 对下面函数进行封装
def Lei(n):####装饰器所装饰的函数，就是装饰器传入的参数
    return sum(n)
Lei(range(100))
print(Lei.__name__)###通过装饰器装饰的函数，他的很多自身属性会改变，需要做如下处理


from functools import wraps #####wrap 也是一个装饰器函数，保留原函数的属性
import logging  ####日志模块
#print(help(wraps))
def timeit2(fun):
    @wraps(fun)
    def deco(*args,**kwargs):
        durning = fun(*args,**kwargs)
        print(logging.warn("%s is good" %(fun.__name__)))
        return durning
    return deco

@timeit2
def Lei1(lst):
    return sum(lst),Lei1.__name__  ####函数的名字不会改变了
print(Lei1(range(10)))

#leiye = time.time()
#print(leiye)

####装饰器本身是一个高阶函数，接受一个函数作为参数，并且返回一个函数
####装饰器本质上是一个Python函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外功能，装饰器的返回值也是一个函数对象

