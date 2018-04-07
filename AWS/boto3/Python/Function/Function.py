######coding=utf-8
#####函数基本属性：已经组织，可重用，功能单一
#####定义函数
def func(x):
    for i in range(10):
        x += i
    return x
print(func(10))
####直接函数名调用即可 func()
#####有多个参数是，使用逗号分隔 def func(x,y):
def sum(x,y):
    return  print('{} + {} = {z}'.format(x,y,z=x+y))

print(sum(1,2))

#####作用域---全局作用域(函数外+函数参数列表(但只有函数才能使用)) > 局部作用域(函数内定义的)
#####最小作用域是函数,定义函数时，自动创建一个新的作用域，局部函数作用域，不会影响全局作用域
######语言中：函数包含值传递和引用传递(引用一个对象指针)，操作系统中，值存在程序的栈空间，引用存储在程序的堆空间
#####python总是引用传递，python一切都是对象，都是引用
l0 = [1,2]
l2 = [3,4]
#l3 = l0.append(5)
print(help(l0.append))
def swap(l0,l2):
    l0,l2 = l2,l0######如果函数中进行赋值，产生了新的变量，新变量的作用域在函数，出了函数的作用域，该新变量不存在了
    l0.append(3)######由于对函数传递进来的参数进行修改，但并没有进行新变量赋值，那么直接修改原值
    return  l0,l2

print(l0,l2,swap(l0,l2))


def lst(l1,x):
   l1.append(x)
   return l1
l1 = [1,2,3,4]
print(lst(l1,5))
print(l1)
####函数返回值 return ，如果函数中没有定义return，默认返回None
####函数只能返回一个值，如果return语句后面有多个元素，会默认封装成一个数组
####函数可以有多个return语句，但始终只会生效第一个return，函数一旦执行到return语句，就会将返回给调用方的作用域，并且销毁函数的作用域
####break语句跳出当前循环，而return将结束整个函数

def loop(l1,l2):
    for x in l1:
        for y in l2:
            print(x,y)
            if y == 3:
                return
loop(range(10),range(10))

######默认参数：函数中指定默认参数就是使代码简洁，默认使用默认参数，也可以指定其他参数
######默认参数必须在参数的最后边，也可以有多个默认参数
def default(start=0,end=10):
    return start+end

def inc(start,end=1):
    return start+end
print(inc(2),inc(2,5))

def append(x,l = []):######在函数def层定义的参数是属于全局变量
###只有在函数层内定义的变量，属于函数作用域，不会修改全局作用域
#   l = []
    l.append(x)
    print(locals())####显示函数内所有变量
    return l
append(5)
append(6)

print(locals())#####locals()函数列出了当前作用域的所有变量

#######关键字参数，位置参数，通过关键字传参
def sum(x,y):###位置参数
    return x+y
def sum1(x=1,y=2):###关键字参数
    return x+y


def lei(first,second,*cs):
    if first > second:
        print(first - second)
    else:
        print(cs)

print(lei(3,5,5,6,7))

#######位置参数和关键字参数是函数调用时的概念
#######而默认参数是函数定义时的概念
#######如果函数中都是关键字参数，那么调用时可以随意修改任意参数进行调用
#######如果函数中既有位置参数也有关键字参数，那么位置参数要在前边
#######可以事先定义好多个关键字参数，进行调用时，只修改其中几个即可
#######调用时，关键字参数及默认参数要在位置参数之后
def connect(host = '127.0.0.1',user = 'ec2-user',passwd = '1111111',db = 'lei'):###默认参数和关键字参数一起使用
    pass
connect(user = 'root')####函数调用时，修改的那个参数是关键字参数，剩下的是默认参数








