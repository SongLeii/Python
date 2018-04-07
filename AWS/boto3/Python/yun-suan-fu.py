#################coding=utf-8
#######比较运算符，一个等号是赋值 a = 3 两个等号是判断是否相等
for i in range(100):
    if i == 5:
        break
    print(i)

print(1 != str(1))

########## 比较运算符中 两端的数据类型最好一致，除了 = 及 !=

#######逻辑运算符  and or not --参与逻辑运算的成员只能是bool类型(ture , false)，或者可以转化为隐式bool类型的类型
print(True and False)
print( not False)
print(True or False)

print(1 == 1 and 2 == 1)
print(1+2 > 3+4 or 1 == 1)
print(not 1>3)

def add(a,b):
    if a < b :
        print(a)
    else:
        print(b)
    return a + b
x = add(5,6)
print(x)

#########对象运算符 is , not is
print(1 is str(1))

##########位运算符int('0b110',2)  二进制转换  bin()--取二进制数
print(int('0b110',2))
print(bin(3))

############运算符优先级--括号可以增加优先级的清晰性
print((1+2 < 3*4) or False)