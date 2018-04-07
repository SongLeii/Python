####coding=utf-8  tuple and list all can be 切片
l1 = list(range(1,11)) #####range函数不包含最后一位数字
t1 = tuple(range(1,10))
len(l1)
l2 = l1[0:10:1] ####from 0 to 10 步长2  the left number must bigger than right
l3 = l1[0:] ###from start to end
l4 = l1[0:-1] ###from start to end - 1
l5 = l1[::-1]####列表反转
#l1[1:8]='x'  ##一般不对切片赋值
print(l1)
print(l1[3:4])####切片：不包含最后一位索引
t2 = t1[3:8]

print(('%%%s') %('songlei'))####如果需要打印%，那么打印两个%% 进行转义即可
l = [[1,2,3],[11,22,33],[111,222,333]] ####行列转换
print(list(enumerate(l)))

#print(l[1][0])
#######行列转置
ret = []
for i,row in enumerate(l):
    for j,col in enumerate(row):
        if len(ret) -1 < j:
            ret.append([])
        ret[j].append(col)
print(ret)


####enumerate()函数 将索引和元素 一起列出
list = ['one','two','three']
for i,element in enumerate(list):
    print(i,list[i])

######
l1 = ['songlei','wangye']
print(l1[1][2])

