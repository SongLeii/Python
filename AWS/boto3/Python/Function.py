#########coding=utf-8
#####参数：位置参数及关键字参数，参数前加星号代表可选，不加星号是必填参数
#####位置参数一旦设定，引用时必须将其设定
#####*args 代表可选参数，以及可以设定任意多个参数,是一个数组类型的对象
#####**kwargs  keyword代表可选参数，以及可以设定任意多个 关键字参数
def f1(first,second):
     if first % second == 0:
         print(first+second)
     else:
         print(first - second)
f = f1(10,6)
print(f)


def f2(first, second,*args):
    a = int(0)
    if first % second == 0:
        print(first + second)
    else:
        print(first - second)
    for i in args:
        print(args)
        a += i
    return a

ff = f2(4,8,2,3)
print(ff)


d1 = {'name1':'Lei','name2':'Ye'}
print(d1.items())
def f3(first,second,**kwargs):
    if first > second:
        print(first - second)
    else:
        print(second - first)
    for k,v in kwargs.items(): #####dict.intem():生成一个列表[('name2', 'Ye'), ('name1', 'Lei')]
        #print(help(kwargs.items))
        print(k,v)
fff = f3(2,4,name1='lei',name2='ye')
print(fff)




