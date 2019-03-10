#coding=utf-8
import xlrd
book = xlrd.open_workbook("../Data/interface_test.xlsx")
table=book.sheet_by_name("Sheet1")
# print(type(table))
# print(table)
# print(table.nrows)
# print(table.ncols)
# print(table.row_values(1,0,3))

row_num = table.nrows
col_num = table.ncols
#将表格数据输出成字典{a:xx,b:xx,c:xx,}，再每行数据组成元组
#step 1: 获得第一行标题
#step2: 获得一行的每个数据
#step3: 将这行的这个数据，放到字典里
#step4: 这行的数据遍历完后   ，加入元组
#step5: goto step2
title = table.row_values(0)
print(title[0],title[1],title[2])
lis = []
for i in range(row_num-1):
    di = {}
    for j in range(col_num):
        x = table.row_values(i+1,start_colx=j,end_colx=j+1)
        di[title[j]] = x[0]
    lis.append(di)
print(lis)
for i in range(len(lis)):+
    assert int(lis[i][title[0]])+int(lis[i][title[1]]) == int(lis[i][title[2]]),'data error'