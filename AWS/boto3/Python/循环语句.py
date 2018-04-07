#########coding=utf-8
#########for循环 while循环
####while循环;用于通用迭代结构,顶端测试为真即会执行循环体，并会重复多次测试知道为假后执行循环后的其他语句
####for循环：通用序列迭代器，用于遍历任何有序的序列对象内的元素，可用于字符串，元组，列表和其他的内置可迭代对象，以及通过类所创建的新对象
####while
####循环体内不要修改可迭代对象
a = 0
x = 0
y = 0
z = 0
while a < 100:
    a += 1
    z += a
    if a % 2 == 0:
        x += a
    elif a % 2 != 0:
        y += a


print(x,y,z)

####for
#for i in range(100):



x = ['a','b','c','d']
y = [1,2,3,'a','c']
aa = []
for i in x:
    if i in y:
        aa.append(i)
print(aa)

#########break and continue  and the range is the xrange in python three
#########else字句判断循环结构是否提前退出，如果提前退出，执行else字句，如果没有提前退出则不执行else
bb = []
for i in range(100):
    if i % 2 == 0:
        if i == 50:
#            break
#            continue
            pass
        bb.append(i)
print(bb)

def sushu(n):
    for i in range(2,n):
        if n % i == 0:
            print('no')
            break
    else:
        print('yes')
sushu(15)

#########input函数 接受一个标准输入数据，返回string类型
'''
NUM = 100
count = 0
while count <= 3:
    YourNum = int(input('pls input a number: '))
    count += 1
    if YourNum == NUM:
      print('you win')
    elif YourNum < NUM:
        print('less')
    elif YourNum > NUM:
        print('big')
else:
    print('you lose')
'''
#######2-100所有素数

import datetime
start = datetime.datetime.now()
def sushu():
    list1 = []
    for n in range(2,100):
        for i in range(2,n):
            if n % i == 0:
                break
        else:
            list1.append(n)
    return  print(list1)
end = datetime.datetime.now() - start

def ss():
    list2 = [2]
    for n in range(2,102):
        for i in list2:
            if n % i == 0:
                break
        else:
            list2.append(n)
    return  print(list2)
res = ss()



