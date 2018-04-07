#########coding=utf-8
#####string是不可变对象 支持切片操作，支持循环遍历,
Lei = 'SongLei'
Ye = 'WangYe'
Result = ' '.join((Lei,'Loved',Ye))
print(Result)
print(Lei + ' Love ' + Ye)
###string.join
print('_'.join(Lei))###join函数是将函数前的元素连接到join函数中的参数的每个元素
'''
for i in Lei:
    Ye.append(i)
print(Ye)
'''
#print(Lei[::-1])

######string.split and rsplit####it splits target from a string to list  ##return a list
a = 'S 1 o 1 n 1 g 1 L 1 e 1 i'
print(a.split(' ',2))####第一个参数是以什么分隔符进行分割，第二个参数是分割次数
print(a.rsplit('1',1))#####rsplit从右往左分割

url = 'url:http://www.leiyeyeye.com'
t1 = (key,value) = url.split(':',1)
print(t1)

#####splitline ##split target by line

#####modify string 修改字符串
x = 'My Name Is SongLei'
print(x.lower().upper())####做文本比较时 统一转换大小写
####ljust and rjust are used to make catalog
catalog = '''concept1
concept2
concept3'''
print(catalog)
catalog1 = catalog.split('\n')
print(catalog1)
zz = 0
for i in catalog1:
    zz += 10
    print(i.ljust(40,'.') + str(zz) + '\n')

######strip清除特定字符函数，默认清除空格
f = open('C:\\Users\\YangXH\\Desktop\\ID.txt')####windows 路径需要 '\\'
print(f.readline().strip('#'))
f.close()


#######查找替换：count,find index replace
f = open('C:\\Users\\YangXH\\Desktop\\ID.txt')
print(f.readline().count('#'))####字符串中#的个数
str1 = 'SoooooongLei'
print(str1.find('o',3,8))####找到指定字符的最早出现的位置，可以指定start 及 end 索引 内搜索
print(str1.index('o',3,8))####find is defferent form index just because when you search a element that is not exist in the strings then index would got a error but find would got -1
print(str1.replace('o','l',6))####replace(old, new[, count]) -> str
str2 = str1[::-1]
print(str2)
#print(help(str1.replace))



