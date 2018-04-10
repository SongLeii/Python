########coding=utf-8
########高階函數：函數參數中可以传递函数，函数的返回值中包含函数，也是高阶函数
def compare(a,b):
    if a['age'] > b['age']:
        return 1
    if a['age'] == b['age']:
        return 0
    if a['age'] < b['age']:
        return -1
#########排序函數：

lst = [3,1,45,6,23,15,8,6]
print(len(lst))
def sort():
    ret = []
    for i in range(len(lst)):
        a = max(lst)
        lst.remove(a)
        #print(a)
        ret.append(a)
    return ret
print(sort())

def sort1(lst,compare,reverse=False):####將比較函數添加到參數列表中
    res = []
    for n in lst:
        for i,j in enumerate(res):
            if compare(n,j) == -1:####永遠要比較第一個，索引為0的元素，將小的值插入到前面
                res.insert(i,n)
                break ####跳出第二個for循環，当插入元素后，必须跳出该for循环
        else:
            res.append(n)
    return res
print(sort1([{'age':10},{'age':2},{'age':15},{'age':12}],compare))

#########另一種形式表現，可以將參數進行函數賦值---函數是一等對象，函數進行參數传递
def sort2(lst,compare=None,reverse=False):
    def def_com(a,b):
        if a > b:
            return 1
        elif a == b:####用if和elif都可以
            return 0
        elif a < b:
            return -1
    if compare==None:
        compare = def_com#######函数赋值不用加括号，在函数内部进行变量传递
    res = []
    for x in lst:
        for i,y in enumerate(res):
            if compare(x,y) < 0:
                res.insert(i,x)
                break
        else:
            res.append(x)
    return res
print(sort2([1,5,3,11,4,7,90,2]))

#########
###高階函數：函數參數中可以传递函数，函数的返回值中包含函数，也是高阶函数

def count(init):
    counter = [init]
    def inc():
        counter[0] += 1
    def dec():
        counter[0] -= 1
    def get():
        return  counter[0]
    def reset():
        counter[0] = init
    return inc,dec,get,reset
inc,dec,get,reset = count(0)
print(inc(),get(),dec(),get())

def lei(init):
    ye = init
    def leiye():
        #ye += 1 ####此操作是进行变量的修改，python将ye这个变量看做本地部变量了，但由于作用域的问题，ye这个变量没有定义
        #如果直接 ye = 1 这个操作相当于在此函数中声明一个本地变量，这种操作在本地作用域中是可以的
        nonlocal ye #####將变量ye声明为不是本地变量
        ye += 1      #####变量ye 就可以进行修改
        return ye  ##return不能 返回變量賦值，只能返回具体具体对象，不能返回变量赋值
    return leiye  #####返回值中包含函数，那麼此函数为高阶函数
bb = lei(1)
print(bb(),type(bb))########虽然函数已经返回--返回值，已经销毁函数内部变量，但外部bb变量调用了 函数内部的ye变量，所以指针没有被销毁

######partial 偏函数用法---將一个函数的参数值固定
from functools import partial
print(int('0b1010',base=2))####int函數默认base是10，将数字转换成整数，一旦base参数显示声明，则第一个参数必须是字符串，且是base类型字符串
####比如base=2 给定的数值必须是二进制数，int函数转换成整数
print(bin(10),oct(0b0101),hex(20))###bin函数转换成2进制,oct()函數將內容转换成10进制，hex()convert to 16hex
new = partial(int,base=16)###將函数的参数固定，
print(new('0x1344'))###直接调用赋值函数即可
####partial函数一般用于 ssh 修改端口等函数，将ssh端口改掉成其他端口后，不用每次都进行传递port参数

#myssh = partial(ssh,port=10001)
#myssh(host='')
