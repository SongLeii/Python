#####coding=utf-8
#####生成器解析式
import timeit
gen = (x*2 for x in range(10) if x % 2 ==0)
print(type(gen))
#####定义生成器--和函数定义相同，只是返回语句用yield，也是函数中的一种
#####生成器是迭代器一種，返回一個生成器對象
def gen1(x):
     for i in range(x):
         yield i ####yield是彈出一個值，當調用next函數返回yield值，再次調用，再次返回
                  #### return是返回，并銷毀函數
         if i == 5:
             return i#####if return and yield are both in function,the key of return can finish the generator early
                      ##### and the return value could be ignored
g = gen1(10) #####賦值后才是生成器，否則是函數,进行变量赋值后才是可调用对象
#print(next(gen(10)),next(gen(10)),next(gen(10)),next(gen(10)))
print(next(g),next(g),next(g),next(g),next(g),next(g))

#####交替打印
def lei1(g1):
    while True:
        yield g1
def lei2(y):
    for i in range(10):
        yield 'g2'
        yield(next(y))
g = lei2(lei1('g1'))
print(next(g),next(g))
#print(next(g))
#print(next(g))

#######生成器求階乘
######階乘 递归函数
def jienew(m):
    if m == 0:
        return 1
    if m == 1:
        return 1
    return jienew(m-1)*m

#####阶乘使用生成器实现
#####生成器替换递归，也可以排除递归限制
def jc():
    ret = 1
    xi = 1
    while True:
        xi += 1
        ret *= xi
        yield ret
jc1 = jc()
print(next(jc1),next(jc1),next(jc1),next(jc1))

def jcnew(x):###只是一個生成器函數
    ret = 1
    for i in range(x)[2:]:
        ret *= i
        yield ret
jc2 = jcnew(7)####賦值后才是生成器
print(next(jc2),next(jc2),next(jc2),next(jc2))

######range()函數返回也是生成器對象
######生成器，通過yield中斷函數并彈出一個值，然後保存該值，当反复调用__next__时，反复读取yield弹出的下一個值


#####yield from 用法
def g10(x):
    for i in range(x):
        yield i
g1 = g10(10)
print(next(g1),next(g1),next(g1))

def g11(iterator):
    yield from iterator #### -> for i in iterator : yield i
g2 = g11(range(10))
print(next(g2),next(g2),next(g2))












