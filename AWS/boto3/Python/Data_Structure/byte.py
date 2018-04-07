####coding=utf-8  bytes是python3中特有数据类型
#### str数据结构是Unicode编码序列--unicode采用双字节进行编码,utf-8包含所有字符,并且都是2字节
##### bytes数据结构是bytes编码序列--一个字符一个字节8位
import sys
s1 = '宋磊爱王烨'
b1 = s1.encode()###str使用encode转换成bytes
s2 = b1.decode()###bytes使用decode转换成str
for i in s2:
    print(i)
#print(help(s1.encode))

s3 = 1
#print(len(s3))
print(sys.getsizeof(s3))

i1 =  bytes(5)###二进制
#i2 = int(i1,base=10)
print(i1)
#print(help(int))