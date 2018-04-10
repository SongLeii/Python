#####coding=utf-8
#####python是动态类型语言，一个变量的类型，是运行时决定的，一个变量的类型在应用的生命周期中是可变的
from functools import lru_cache  ###lru_cache是个装饰器函数
def add(x,y):  ####可在函数中注明参数的类型
    '''
    :param x: str
    :param y: str
    :return: str
    '''
    return x+y
print(add('songlei','wangye'),help(add))####it can print the comment in help doc

def add1(x:int,y:int) -> int: ##### the type of object that you can declare before
    return x+y
print('songlei','wangye')####it's just a statment that doesn't check anything in function


#####装饰器实现参数类型检查：
from functools import wraps

def Type_check(*type_args,**type_kwargs):
    def Dec(fun):
        @wraps(fun)
        def Parameter(*args,**kwargs):
            for i,t in enumerate(type_args):###判断位置参数类型
                if not isinstance(args[i],t):#####isinstance（object，typeinfo）函数 isinstance(1,int)返回true
                    print('the {} arg is not {}'.format(args[i],t))
                    break
            for j,t in type_kwargs.items():
                for k,l in kwargs.items():
                    if not isinstance(kwargs[k],t):
                        raise TypeError('the {} kwarg is not {}'.format(kwargs[k],t))####raise 异常处理，后面跟异常名称,可自定义
                        break
            Function = fun(*args,**kwargs)
            return Function
        return Parameter
    return Dec
@Type_check(int,str,type1=str)
def Type(x,y,z=1):
    print(x,y,z)
Type('x','y',z='2')

##############impact用法 ---获取函数参数信息
import inspect
def add(x:int,y):
    return x+y

sig = inspect.signature(add)###获取函数中参数信息,以元祖输出
print(sig)
parameter = sig.parameters['x']
print(sig.parameters['x'])####输出add函数所有的参数及其类型,以列表形式输出
print(sig.parameters['x'].name)



######带过期的LRU缓存器
from functools import lru_cache  ###lru_cache是个装饰器函数
from functools import wraps
import time
'''
*FIFO:　先进显出
*LFU：最近最少使用计数
*LRU：最近最久未使用计时
当LRU缓存达到设定的最大值时将缓存中近期最少使用的对象移除。
'''
def logging(fun):
    wraps(fun)
    def parameter(*args,**kwargs):
        start = time.time()
        function = fun(*args,**kwargs)
        end = time.time()
        print('call {} took {}'.format(fun.__name__,end-start))
        return function
    return parameter
@logging
@lru_cache(maxsize=10)####maxsize参数是最多缓存多少树木，如果设置为None那么不缓存
def ab(x):
    time.sleep(x)
ab(2)####lru_cache将函数参数缓存成key，保存在字典中
ab(2)####本次返回了使用1。9s
ab(2)####本次执行0s


######functools.partail 将函数的某些参数进行固定，相当于默认参数
import functools
def add1(x,y):
    return x+y
newadd = functools.partial(add,y=3)######partial函数操作会生成一个新的函数
print(newadd(5)) ###将参数y固定，只需要介入一个参数即可
print(functools.partial(add,x=3)(y=5))#####  functools.partial(add,x=3)--相当于是一个新的函数，直接传递y=5即可