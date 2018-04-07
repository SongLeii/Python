########coding=utf-8
####列表解析--测试列表解析的性能优势
####[expr for i in iteralbe if expr] 循环后可以添加一个if语句
import timeit ####执行10000次的用时
import random
def xh(ls):
    res = []
    for i in ls:
        res.append(i+1)
    return res

def xh2(ls):
    return [i+1  for i in ls]###直接返回新列表，列表的内容是表达式的结果

print(xh(range(10)),xh2(range(10)))
#print(help(timeit.timeit))
#print(timeit.timeit('xh(range(10))',globals=globals()))
#print(timeit.timeit('xh2(range(10))',globals=globals()))
def L(x):
    return x**2
print([L(x) for x in range(100)])###L(x)函数必须要设定返回值
#print([print(i+100) for i in range(10)])
print([i**10 for i in range(10) if i % 2 == 0 ])
a = 0
print([i**2 for i in range(100) if i % 2 ==0])
print([i for i in range(100) if i > 5 if i % 2 != 0]) ####语句逐层嵌套进去，the former expr get higher prioriry
print([(x,y) for x in range(10) if x % 2 ==0 for y in range(10)])

#####filter(function(),iterable)函数用法  过滤可迭代对象，将符合条件的元素生成新列表（迭代器）
#####列表解析的效率要高很多，python中一般很少用filter函数
#####map(fuction(),iterable)函数类似filter函数，map对于函数表达式进行映射，而不是过滤，进而生成新列表（迭代器）
print(timeit.timeit('list(filter(lambda x:x % 2 !=0,[x for x in range(10)]))',number=1000)) ###过滤可迭代对象
print(timeit.timeit('[x % 2 !=0 for x in range(10)]',number=1000))
print(map(lambda x:x**2,[x for x in range(10)]))###修改可迭代对象

#####生成器解析式：---相对于列表解析式，是按需计算，临时生成一个生成器,调用时才进行计算
#####好处是节省内存
#####坏处是：只能单个获取元素，而且不能回头调取其中元素
def func(x):
    #print('num {}'.format(x))
    return x*2
print([func(x) for x in range(10) if func(x) % 2 == 0])
num = (func(x) for x in range(10) if func(x) % 2 == 0)
print(next(num),type(num))

#####集合解析式：返回一个set对象，其中元素必须唯一，且可hash
def leiye(x,y):
    return x+y
print(random.choice(range(3,26)))
print({leiye(x,y) for x in range(3,40) for y in range(3,26)})
###zip函数将多个可迭代对象中的对应元素打包成元组的序列  返回的一个生成器
a = zip(range(10),range(11)) ##生成一个生成器
print(list(a))
#####字典解析：需要两个表达式，一个key，一个value，key元素必须是可哈希,以大括号为最外侧
def lei(m,n):
    a = m*n
    return a

print({str(m):lei(m,n) for m in range(10) for n in range(1,5)})
print({x:y for x,y in zip(range(10),range(10))})


