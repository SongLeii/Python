######coding=utf-8
#####可变数量位置参数,用*号定义,是一个元祖
def fun(*args):
     return print(args)
print(fun(1,2,3,4))

####可变关键字参数，用两个星号定义 **kwargs,是一个字典
####位置参数必须在关键字参数前边，先定义位置参数，再定义关键字参数
def fun1(x,y,**kwargs):
    if x > y:
        print(x - y)
    elif x < y:
        for k in kwargs:
            print('the name is %s, the name is %s' %(k,kwargs[k]))
    else:
        for m,n in kwargs.items():
            print('the name is %s,the age is %s' %(m,n))
print(fun1(3,3,songlei='30',wangye = '28'))

d1 = {'songlei':30,'wangye':28}
for k,v in d1.items():
    print(k,v)

def fun2(x,y,*args,**kwargs):
    if x < y:
        print('x is less y')
    elif x > y:
        a = 0
        for i in args:
            a += i
        print(a)
    else:
        for j in kwargs:
            print('%s loved %s' %(j,kwargs[j]))
res = fun2(8,8,3,4,5,6,7,songlei='wangye',ssl = 'szt')
print(res)
#####fun(x,y,*args,**kwargs)  fun(2,3,4,5,6,x=7,y=8)  参数中不能有重复值
#####可变参数后置，可变参数不和默认参数一起出现

#####参数解构
def fun3(a,b,c,d):
    print(a,b,c,d)
lst = [1,2,3,4]
tup = (1,2,3,4)
print(fun3(*tup))##### 一个型号是解构线性结构数据,结构完成后是函数的位置参数
#####线性结构可以解构成位置参数
#####字典可以解构成关键字参数
d1 = {'1':'songlei','2':'wangye','3':'ding'}

def fun4(**kwargs):
    for k in kwargs:
        print('my num is %s and my name is %s' %(k,kwargs[k]))
print(fun4(**d1))

#####参数槽： *号之后的参数，必须以关键字参数的形式传递,这种用法叫做参数槽用法，*号后面的参数叫做命名参数

def fun7(x,y,z=3,*args):
    if x > y:
        print(z)
    else:
        a = 0
        for i in args:
            a += i
    return 0
print(fun7(2,1,4,5,6))

def fun5(*,x,y,z,a,b,c):
    lst=[]
    lst1=[]
    for i in x,y,z,a,b,c:
        lst.append(i)
    while True:
        try:
            j = min(lst)
            lst.remove(j)
            lst1.append(j)
        except ValueError:
            print('all process is finished')
            return lst1

print(fun5(x=5,y=15,z=21,a=1,b=10,c=4))

####函数参数类型示意：相当于注释
def fun6(x:int,y:str) -> str : ##箭头后表示返回值类型
    print(x,y)
print(fun6('songlei','wangye'))

