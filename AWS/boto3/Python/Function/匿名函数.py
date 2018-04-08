########coding=utf-8
########匿名函數----lambda parameter:express
########只能写在一行中，表达式的结果就是返回值，且只能有一个表达式
########參數功能和正常函數使用方式一致，关键字参数，可变参数，可变关键字参数,參數槽e
lambda x,y:x+y
add = lambda x,y=1 : x+y####參數也可以給默認值
add1 = lambda *x : sum(x)
add2 = lambda **kwargs:kwargs
add3 = lambda x=1,*,y:sum(y)

print(add(1),add1(1,2,3,4,5,6),add2(a=1,b=2),add3(y=range(10)))
######匿名函数一般配置高阶函数，通过参数传入。或者作为函数返回值