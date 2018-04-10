#####coding=utf-8
####open函数
File1 = open('/Users/leisong/pythonfile/lei.py',mode='r')###返回值是 file-like对象 该文件的open的参数信息,默认模式是读
####只要是写操作模式打开文件，都会清空文件
#print(File1.read())
#print(File1.write('lei love ye'))
File1.close()
File2 = open('/Users/leisong/pythonfile/ye.py',mode='w')####if you open a file that not exist by write mode  then create the file
File2.close()
#File3 = open('/Users/leisong/pythonfile/ye1.py',mode='x')####it always create a new file for writing
#File3.close()
File4 = open('/Users/leisong/pythonfile/ye.py',mode='a')####it 's the way to write something at the end of file
File4.write('ye love lei')
File4.write('lei lvoe ye')
File4.close()
File4 = open('/Users/leisong/pythonfile/ye.py',mode='a')####it 's the way to write something at the end of file
File4.write('ye love lei')
File4.write('lei lvoe ye')
File4.close()
#print(help(File4.close))
File5 = open('/Users/leisong/pythonfile/ye.py',mode='wt')###  the way of t is text mode and it 's default
File5.write('songlei')
File5.close()
File6 = open('/Users/leisong/pythonfile/ye.py',mode='wb')### b 二进制模式打开
File6.write('songlei'.encode(encoding='utf-8'))#### 以制定编码格式编码字符串
File6.close()
#print(help(open))
File7 = open('/Users/leisong/pythonfile/ye.py',mode='ab+')#### + mode can't work alone 会增加额外的读写操作
File7.read()
File7.write('songlei love wangye '.encode())###encode将字符串转换为字节码
print(File7.tell(),File7.seek(15,0),File7.tell(),File7.read())####seek函数改变读取指针,decode将字节码转换成字符串
File7.close()

File8 = open('/Users/leisong/pythonfile/ye.py',mode='r+')
print(File8.tell(),File8.seek(7,0),File8.write('www'))### 从tell函数返回的坐标开始写入,相当于插入
File8.close()
###seek(offset,from_where)offset--将指针改变到哪里（字节位置），from_where是0--从文件开头，1--从当前位置，2--从未见最后
#print(File7.write('\nleiye'),File7.tell(),help(File7.seek))####在文件最后追加内容,tell方法查看当前指针
####encode和decode函数  python3
####encode编码--就是将字符串编码成字节码（二进制）
####decode解码--将字节码转换成字符串
####python3将字符串数据和二进制数据进行了区分，不能将字节码和字符串拼接在一起

####buffering 缓冲区
import io
print(io.DEFAULT_BUFFER_SIZE)
File9 = open('/Users/leisong/pythonfile/ye3.py',mode='r+')
print(File9.seek(1,0),File9.write('www\n'),File9.readlines())
#print(File9.read())
File9.close()

####readlines 返回一个可迭代列表，按行计算



