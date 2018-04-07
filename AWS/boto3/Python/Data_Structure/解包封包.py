########coding=utf-8
#######封包：将变量构建成元祖，解包：将元祖及列表赋给变量
#######解包：解包中有多个元素的话，一定会形成列表
x,y = (1,2)#####the process of release packetage,不能对空列表做解包
def swap(a,b):
    a,b = b,a
    return (a,b)

t1 = 1,2,3,4,5##### assign a group values to one variable
print(x,y,t1)
print(swap(5,6))


a,*b,c = 1,2,3,4,5,6########## '*'是让函数参数及变量接受任意多的元素,
print(a,b,c)

l1 = list(range(0,10))
head,*_,end = l1###### '_'下划线表示可以丢弃该元素
print(head,end)

x = 1
y = 2
#x,y = y,x
tmp = x
x = y
y = tmp

x,y = y,x


t1 = 1,2,3,4,5,6 ###封包 结果是元祖
x,y,*z = t1
print(x,y,t1,x,y,z)

t1 = (1,2,3,4,5,6,7,8,9)###取出第一个，第三个，及倒数第二个元素
head,_,third,*_,second,_ = t1#### '_'表示丢弃该元素
print(head,third,second)

def element(x,y):
    a = x * y
    if x > y:
        b = x - y
    return a,b
m,n = element(10,9) ###解包时：也可用函数进行传递
print(m,n)