###########coding uft-8
#a = int(input('please input a num: '))
######内置数据结构：list 元祖 集合 字典 字符串
####列表--可变数据结构
####可以用list()初始化一个序列，也可以使用[]直接初始化列表
#####index sign of a list is from 0
print(list(range(0,10)))
print(list([0,1,2,'songlei']))
list1 = [0,1,2,3,4,5,6]
list1[-1] = 'wangye' ####修改列表中的某个元素
print(list1) ####负数表示倒数元素
#list2 = [101,102]
list1.append(3)###append method's reture value is None ，add a element at the end of list
list1.insert(0,99)####index,element  you can add a element at anywhere###if index out of range ,add a element at the end or begin of list
list1.extend([3,3,3,3,3,3])####extend iterable target in the list
list1.pop(-2)######delete a elemnet at the end of list and select a specific index to delect
list2 = [1,2,3,4,5,1,2,3,4,5]
list2.remove(1)########remove the first element value that you specified
#list1.clear()######clear the list
print(list1.index(1,2,5))###to find where is the element from position 2 to 5 in the list
print(list1.count(3))#####show the number of element that you specified
print(len(str('sssssssss')))#### show the length of target
print(list1,list2)
#print(help(list1.remove))####help() can print all of method about target

######modify the list
List3 = [1,6,43,2,4,6,743,3]
List3.sort(reverse=True)###倒序
List3.reverse()###反转方法
List3[1] = 1
List4 = List3.copy()###copy one target to a new memory area



########应用
#######新列表  math.ceil--向上取整
import math
print(help(math.ceil))

print(math.ceil(5 ** 0.5))

#####列表去重
l1 = [1,1,1,1,22,3,3,4,4,5,5]
l2 = []
for x in l1:
    if x not in l2:
        l2.append(x)
print(l2[3:])###from the number 3 index to the end
#####列表取出最大值
z = 0
for y in l1:
    if z < y:
        z = y
print(z)






