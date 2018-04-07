#####coding=utf-8
import os
print(help(os.getcwd))
print(os.listdir(os.getcwd())) #####listdir显示目录下的文件，getcwd获取当前目录
str1 = 'songlei.txt'
print(str1[:-4])

filenames = os.listdir(os.getcwd())###listdir 返回一个list
out = open('names1.txt', 'w')####w是file 写模式,if the file not exist then create it
'''
for name in filenames:
    filenames[filenames.index(name)] = name[:-3]
'''
for name in filenames:
    name1 = name.strip('.pytxt',)####可以指定清空字符串
    out.write(name1 + '\n')
out.close()
