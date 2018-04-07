################coding=utf-8
##########程序控制结构：顺序结构+分支结构+
###顺序结构
x = 0
for i in range(101):
    x += i
    print(x)


#####bool函数0，None，空的内置结构 返回值都是false，其他都是true
print(bool(-1))

#####分支结构--单分支，多分支,分支结构永远只会有一个分支执行
a = 1
b = 2
if a > b:
    c = a + b
elif a == b:
    c = a - b
else:
    c = a*b
print(c)

######break+continue :break 跳出整个循环，不再执行，continue：跳过整体循环中的本次循环
######
x = 0
for i in range(10):
    if i >= 5:
        x+=i
        continue
print(x)







