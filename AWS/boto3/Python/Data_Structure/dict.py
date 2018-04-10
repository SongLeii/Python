###########coding=utf-8
#####字典：字典的key必须是可hash对象，且唯一，value可以是任何元素
####字典是可变对象,蛋没有切片操作
d = {'songlei':1,'wangye':2}
d1 = dict()
d1.update([(1,'songlei'),(2,'wangye')])
print(d1)
d['song'] = 100###通过key 修改value，如果没有该key，直接添加到字典内
d.update({'songzt':3})###可以接手字典参数
d.update([('ssl',4),('zzz',5)]) #####可以接收两元素的元祖，多出两个元素就不行了
d.update(mm=6)###可以接收关键字参数
d.update({'son':2})###it would overwirte the value when you update the same key
#d.update(['songlei',100])
d.pop('ssl')####delete one kv of dict that you specified
d.pop('ww',-1)#### a error happen when you delete the kv pair is not exist ,but if you specify a default value,there is no error happen
#d.popitem()###随机删除一对kv pair
#d.clear()###清空字典
d.get('songlei')###get方法可以得到该key的value，如果key不存在，返回None
d.get('ye',99)
d['songlei']#####通过key查找value，如果key不存在，抛出异常，
d.setdefault('songl',-1)######如果字典中不存在，会自动创建
print(d.setdefault('songlei'))####类似get()方法得到key对应的值
##if we don't want to throw the error we can use d.get,else use d['key']
print(d['songlei'],d.get('songl'),d)##通过key来查看value

#########遍历字典  d.items,d.keys,d.values 返回对象都是set-lile 可以通过 | ^ & 求交 并 差
d1 = {1:'songlei',2:'wangye',3:'ssl'}
print(d1.items()) ###返回一个列表中以元祖为单位，可遍历的列表
for i in d1: ######可以遍历字典中的key值 or for i in d1.keys()
    print('{} -> {}'.format(i,d1[i]))
for k,v in d1.items():####直接遍历字典,相当于解包
    print(k,v)
for i in d1.values():
    print(d1.values())

#######orderdict ####可以顺序记录字典的k v
from collections import OrderedDict
dd = {}
dd['a'] = 1
dd['b'] = 2
print(dd)###字典是无序的对象
dd1 = OrderedDict()
dd1['x'] = 0
dd1['y'] = 10
dd1['z'] = 100
print(dd1,dd1.items())
####用value取出key
for k,v in dd1.items():
    dd2 = {}
    if v == 100:
        dd2.update({k:v})
    elif v == 0:
        print(k)
        dd2.update({k:v})
print(dd2)
d2 = d1.items()
print(d2)
for i,(k,v) in enumerate(d1.items()):
    print(i,k,v)


ddd = {'x':1,'y':10,'z':5,'m':3,'n':7}
#l = [3,5,2,4,7]
#print(sorted(l))
print(sorted(ddd.items(),key=lambda  x:x[1]))

####字典其他方法
print(dir(ddd))####dir函数查看对象有哪些方法

#####fromkeys方法：用在初始化一个字典，并给与一个初始值，后续再去更改
ld = range(100)
dddd = dict.fromkeys(ld,'Blank')#####dict.formkeys(可迭代对象，values)
print(dddd)

#####sorted排序呢
ls  = [{'max':10,'avg':6,'min':2},{'max':100,'avg':75,'min':50},{'max':30,'avg':19,'min':8}]
print(sorted(ls,key=lambda x:x.get('max'),reverse=True))










