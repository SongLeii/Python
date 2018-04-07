########coding=utf-8 模板语言
print('my name is {},my age is {}'.format('songlei',30))
print('my lover is {name} and my name is {my}'.format(name='Ye',my='SongLei'))
####大括号中指定了元素，需要在format方法中用key=value方式表达
print('my name is {1[0]} and my wife is {3}'.format('lei',['a','b'],'song','wang'))
####可以传递任何类型的参数
print('{1} or {2} and {name}'.format(0,'aliyun','AWS',name='lei'))
class A:
    def __init__(lei):
        lei.x = 1####  argument.xx 定义参数属性
        lei.y = 2

class B:
    def __init__(ye):
        ye.xx = 3
        ye.yy = 4
a = A()
b = B()
print('{1.yy} and {0.y}'.format(a,b))

######special situation
### ! 是 特殊格式转换
print('{0[1]!a} loved {1[0]!a}'.format(['lei','烨'],['磊 ','lei']))
### ：是特殊处理：填充符--默认是空格，左右对齐 及 是否添加数字符号 及 宽度
print('{0:+}'.format(10))#### 加减号是是否添加数字前边的数字正负号
### 可以映射变量,需要使用大括号，后边使用key = value 传递
print('{1:{fill}^{width}}'.format('lei','ye',width=100,fill='一'))


####也可以指定format方法中的index位置
#print(help(str.format))