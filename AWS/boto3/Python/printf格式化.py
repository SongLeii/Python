########coding=utf-8
#coding:utf-8

#####print格式转换符%  将特定字符转换为特格式
     #####print "String %format1 %foramt2 ..." %(variable1,variable2,...)
'''
format ---一般用于数字
a   ascii码
d,i 十进制数或长整数
u    无符号整数或长整数
o    八进制数或长整数
x    十六进制数或长整数
X     十六进制整数（大写字母的X）
f     浮点数
e      浮点数
g      浮点数
r      使用rep    r()函数生成字符串
c      单个字符
s       格式化成字符串类型，使用str()生成字符串
%       字面量%
flag 修饰符
%(name)[flag][width][.precision小数点后显示几位]typecode
-       表示左对齐默认右对齐,默认左对齐
+       增加数字符号，如正数+ 负数-
0：      表示一个零填充

'''

print('songlei loved %s and %F' %('wangye',1000))
print('%(myname)s %(middle)s %(lover)o' %{'myname':'Lei','lover':100,'middle':'Loved'})
print('my name is %(name)a' %{'name':'磊'})
####多次出现需要格式转换的情况，可以用字典的方式指定，不需要按照顺序
####只有一个element的时候，可以不适用元祖
####%s %d %f 使用较多




'''
firstname = 1
lastname = 2.00000000
print("my name is %d %f" %(firstname,lastname))
print "my name is %d %f" %(firstname,3)
print "my name is %f %s" %(firstname,lastname)
#print "%f" % num
print firstname,lastname
test = str(firstname)
print type(test)
print type(firstname)
print str(lastname)
'''
'''
num1 = 1.0000
num2 = 2.0000
print "my lucky mumber is %-+10.5f %+3.1f" %(num1,num2)
print "%-+10.5f %+3.1f"  %(num1,num2)

d = {'x':1,'y':2,'z':3}
print d['x']+d['y']
print "%(x)+10f %(y)f" %d
'''

