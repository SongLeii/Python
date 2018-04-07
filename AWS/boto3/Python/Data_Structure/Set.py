#########coding=utf-8
#####集合中的元素是唯一的，无序的，{}使用大括号来初始化集合,set集合中必须都是不可变对象，也就是可hash的对象
s1 = set({1,2,3,4,4})
s2 = {}###不能这样定义一个空集合，因为默认是字典的数据结构
#s3 = {1,2,3,4,5,5}###如果重复了，那么会去掉重复元素
print(s1,type(s2))

#####set相关方法,
####增删改查  add是将整个参数添加进去，update是将参数中每个元素添加到集合中
s1.add('songlei')#####add方法只能添加可hash的对象，元组，字符串，不能添加list及set等可变对象---是可变对象
s1.update('songlei')### 包含一个可迭代对象的参数，遵循去重原则,可以是字符串，元组，列表，类似于list.extend方法
####update会将参数中的每个元素增加到集合中
l1 = [1,1,1,2,2,3,3,3,4,5,65]
t1 = (1,1,2,2,2,3,4,5,6,45,5,5)
s2 = set(l1)###可以对一个列表或者元组进行set()函数的去重操作
s3 = set(t1)
print(s1,s2,s3)

#####hash函数---可变对象不能哈希，不可变对象才能被hash
ss = {1,2,3,4,5}
ss.remove(1)
ss.discard(10)#####remove删除不存在元素时返回错误，而discard不会
ss.pop()####随机抛出一个元素
ss.clear()###清空所有元素
print(ss)

######不能直接修改集合中某个元素，因为集合石无序的,不支持索引
#print(ss[0])

######筛选出单一元素
###用list完成
l = [1,2,3,1,2,5,6,4,3,5,8,9,2]
tmp = []
ret = []
for i in l:
    if i not in tmp:
        tmp.append(i)
        ret.append(i)
    else:
        if i in ret:
            ret.remove(i)
print(ret)
####使用集合完成
sss = set({})
tmp1 = set({})
for z  in l:
    if z not in tmp1:
        sss.add(z)
        tmp1.add(z)
    else:
        if z in sss:
            sss.remove(z)
print(sss)

######集合运算  并集，交集，差集，对称差集  *union *intersection *difference  *  ---返回一个新的集合，不会修改源集合
sa = {1,2,3,4,5,6}
sb = {1,3,5,7,8}
sc = {11,22,33,4}
print(sa.union(sb),sa | sb,sa.union(sb) == sb.union(sa))###并集
print(sa.difference(sb),sa.difference(sb) == sb.difference(sa)) ###差集
print(sa.intersection(sb),sa & sb,sa.intersection(sb) == sb.intersection(sa))###交集
print(sa.symmetric_difference(sb),sa.symmetric_difference(sb) == sb.symmetric_difference(sa),sa ^ sb) ###对称差集

#######超集 and 子集  不相交
sx = {1,2,3,4}
sy = {2,3}
sz = {7,8}
print(sx.issuperset(sy),sy.issubset(sa),sx.isdisjoint(sz))####一般用作判断 是否是对方的超集 或者子集,或者两者不想交

######set 应用
###元素唯一应用---用户输入主机列表，不能重复操作
def host(*args):
    host_set = set({})
    for j in range(3):
        hosts = input('pls type your host:')
        host_set.add(hosts)
    print(host_set)
if __name__ == '__main__':
    host()

######找出集合中还未执行的主机
#host_all = {'10.1','10.3','10.5','10.6','10.2','10.9','168.1','168.3'}
def host_no(*args):
    host_all = set({})
    host_doing = set({})
    for i in range(5):
        host_input = input('your host is:')
        host_all.add(host_input)
    for j in range(3):
        host_doing.add(host_all.pop())
    return  host_all - host_doing
if __name__ == '__main__':
    print(host_no())





