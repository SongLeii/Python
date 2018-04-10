####coding=utf-8
#####带参数的装饰器：是一个函数，返回一个不带参数的装饰器
####对于函数执行大于 几秒的操作 进行日志记录
from functools import wraps
import datetime ###可以返回date 日期，time时间 datetime日期时间
import time ####time.time()函数返回的是格林威治时间到现在的时间
import logging
def log(s):
    def _logger(fun):
        @wraps(fun)
        def parameter(*args,**kwargs):
            start = time.time()
            durning = fun(*args,**kwargs)
            end = time.time()
            if (end - start) > s:
                logging.warn('%s has already overtime %ds' %(fun.__name__,s))
            return durning
        return parameter
    return _logger

@log(2)
def Lei(x):
    time.sleep(x)

a = Lei(2)
print(a)

###### 装饰器的应用
#### 1. cache 应用
def joi(*args):
    x = ','.join(str(x) for x in args)
    print(x)
joi('a','b','c')

print('{}::{}::{}'.format(joi.__name__,'lei','ye'))


def cache(instacne):
    def dec(fun):
        @wraps(fun)
        def parameter(*args,**kwargs):
            pos = ','.join(str(x) for x in args)
            kw = ','.join('{}={}'.format((k,v) for k,v in sorted(kwargs.items())))
            key = '{}::{}::{}'.format(fun.__name__,pos,kw)
            ret = instacne.get(key)
            if ret is not None:
                return ret
            ret = fun(*args,**kwargs)
            instacne.set(key,ret)
            return ret
        return parameter
    return dec

class Dictcache:
    def __init__(self):
        self.cache = dict()####初始化字典就是将字典放入到内存中
    def get(self,key):
        return self.cache.get(key)
    def set(self,key,value):
        self.cache[key] = value
    def __str__(self):
        return str(self.cache)
    def __repr__(self):
        return repr(self.cache)

cache_instance = Dictcache()
@cache(cache_instance)
def Long_time_fun(x):
    time.sleep(x)
    return x

######class的基本使用
class Test:
    def __init__(self,value='songlei love wangye'):
        self.data = value
x = Test()
print(x)

class TestRepr(Test):
    def __repr__(self):####__repr__在直接调用或者print方式输出的格式相同
        return 'TestRepr %s' %(self.data)
y = TestRepr()
print(y)

class TestStr(Test):
    def __str__(self):####__str__方法纸雕调用和print输出方式不同，如果需要在所有环境环境下的输出内容相同，那么使用__repr__内置方法
        return '[value:{}]'.format(self.data)
z = TestStr()
print(z)



####python已经提供了标准库  lrucache
from functools import lru_cache


#######监控作用---程序连路上关键函数都会有这种装饰器，实现全链路监控
def Watching(Prefix,Instance):
    def Log_dec(fun):
        @wraps(fun)
        def Parameter(*args,**kwargs):
            Start = time.time()
            Ret = fun(*args,**kwargs)
            Key = '{}.{}.{}'.format(Prefix,fun.__module__,fun.__name__)
            Value = time.time()-Start
            Instance.send(Key,Value)
            return Ret
        return Parameter
    return Log_dec

class Logging:
    def send(self,Key,Value):
        print(logging.warn('{} => {}'.format(Key,Value)))

@Watching(Prefix='LongTimeFunction',Instance=Logging())
def LongTime(lst):
    sum(lst)

LongTime(range(100000000))



#######身份认证