######coding=utf-8
######可迭代对象：列表，元祖，字典，字符串，生成器，集合,内部实现了__iter__方法,当调用for in 遍历时，__iter__会返回一个迭代器对象
import dis
def it():
    return list(range(10))
a = it()
print(a,type(a))



#dis.dis( '[x*2 for x in range(10)]')


######可以使用 for in 表达式，成员运算符(in or not in)
######iter(iterable,)将一个可迭代对象，生成一个迭代器
######for in 表达式其实隐式调用了__iter__()函数和__next__()方法
######if 表达式隐式调用了 bool函数
######iter()###生成迭代器函数---import dis隐式调用了__iter__()函数和__next__()方法
######迭代器不会一次性把所有元素加载到内存，而是需要的时候才生成返回结果
######迭代器内部持有一个状态，该状态用于记录当前迭代所在的位置，以方便下次迭代的时候获取正确的元素
#print(help(iter))
it = iter(range(2,10))
#print(next(it,1),type(it))#####可以设置默认值，
#print(next(it),next(it),next(it))###只能从前往后调用，如果没有下一个元素时，抛出异常
def func(x):
    return  x^2
num = (func(x) for x in range(10) if func(x) % 2 == 0)
print(sum(num))
####生成器也是迭代器的一种，不需要调用__iter__及__next__内置方法来获取元素，函数中使用yiled返回
def gen():
    for i in range(10):
        yield i  ####yield直接返回一个生成器对象
a = gen()
print(type(a),list(a))


numnew = iter(num)
print(list(numnew))
print(type(num))







