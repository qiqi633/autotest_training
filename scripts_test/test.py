#!/usr/bin/python
#coding:utf-8
# import sys
# sys.path.append("C:\Python27\Lib\site-packages")
# # import importlib
# # import sys
# # importlib.reload(sys)
# import time
# import pytest
# def test():
#     a= 1
#     b = 2
#     print('a:{0},b:{1},c:{2}'.format(a,b,a+b))
#二分查找,给出一个已经排好序的列表,注意是已经排好序的,查找指定元素在列表中的位置
def binary_search(order_list,item):
    low =0
    high = len(order_list)-1
    while high-low>1:
        mid = (low+high)/2
        mid = int(mid)
        print(order_list[mid])
        if order_list[mid]<item:
            low=mid+1
        elif order_list[mid]>item:
            high=mid-1
        else:
            return mid
    if high-low == 1:
        if order_list[low]==item:
            return low
        elif order_list[high] == item:
            return high
    if high-low == 0:
        return low
    print("no such num")



# str = input("please input orderlist:")
# lst = []
# list = str.split(" ")
# i=0
# print(list)
# while i<len(list):
#     lst.append(int(list[i]))
#     i+=1
# print(lst)
# loc = binary_search(lst,10)
# print(loc)
#选择排序 找到数组中最小的元素，然后往新数组里追加，时间复杂度O(n^2)

def minfind(list):
    list_new = []
    while len(list)!=0:
        min = list[0]
        tip = 0
        for i in range(len(list)):
            if list[i]<min:
                min = list[i]
                tip = i
        del list[tip]
        print(len(list))
        list_new.append(min)
    return list_new

# print(minfind(lst))


def popsort(poplist):
    le = len(poplist)
    while le>1:
        for i in range(le-1):
            if poplist[i]>poplist[i+1]:
                tmp = poplist[i+1]
                poplist[i+1] = poplist[i]
                poplist[i] = tmp
        le = le -1
    return poplist
# print(popsort(lst))

#圆桌报数算法100个小朋友围成一个圈,设定编号为1~100,依次按1,2,3,4,5,6,7,8,9循环报数,报到9的出圈,直到所有小朋友出圈.请写代码打印出各个小朋友出圈顺序,语言不限

def cycletable(tablelist,num):
    le = len(tablelist)
    #count是出局的玩家数量
    count = 0
    online = []
    #设置所有玩家在线
    for i in range(le):
        online.append(1)
    tmp = tablelist[0]
    lenth = le
    # print("count:{0},tmp:{1},le:{2}".format(count, tmp, le))
    while count<lenth:
        # print("xunhuan")
        for i in range(lenth):
            # print("bianhao:{0},online:{1},tablelist:{2}".format(i,online[i],tablelist[i]))
            if (online[i]==1):
                if(tmp%num==0):
                    online[i] =0
                    print("bianhao {0} wanjia chuju".format(tablelist[i]))
                    count = count +1
                    tmp = tmp+1
                elif((tablelist[i])%num!=0):
                    tmp=tmp+1

            else:
                continue

ll = []
for i in range(1,101):
    ll.append(i)
cycletable(ll,50)




