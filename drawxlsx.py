

import xlrd
import matplotlib.pyplot as plt
import numpy as np
import csv

import mpl_toolkits.axisartist as axisartist

#创建画布--------
fig = plt.figure(figsize=(10, 8))
#使用axisartist.Subplot方法创建一个绘图区对象ax
ax = axisartist.Subplot(fig, 111)  
#将绘图区对象添加到画布中
fig.add_axes(ax)
ax.axis[:].set_visible(False)
ax.axis["x"] = ax.new_floating_axis(0,0)
ax.axis["x"].set_axisline_style("->", size = 1.0)
ax.axis["y"] = ax.new_floating_axis(1,0)
ax.axis["y"].set_axisline_style("-|>", size = 1.0)
ax.axis["x"].set_axis_direction("top")
ax.axis["y"].set_axis_direction("right")

 
#打开文件
# data = xlrd.open_workbook(r'C:/Users/Administrator/Desktop/file/1733.csv')

x_mat = []
y_mat = []
filepath = 'C:/Users/Administrator/Desktop/file/1733.csv'
with open(filepath, 'r') as f:
     reader = csv.reader(f)
     for i in reader:
        x_mat.append(i[2])
        y_mat.append(i[5])
print(x_mat,y_mat)
# #获取表格数目
# nums = len(data.sheets())
# for i in range(nums):
#     #根据sheet顺序打开sheet
#     sheet1 = data.sheets()[i]
 
#根据sheet名称获取
# sheet2 = data.sheet_by_name('1733')
# #获取sheet（工作表）行（row）、列（col）数
# nrows = sheet2.nrows   #行
# ncols = sheet2.ncols   #列
 
# x_mat = []
# y_mat = []
 
# for i in range(nrows):
#     print(sheet2.row_values(i))
#     x_mat.append(sheet2.row_values(i)[2])
#     y_mat.append(sheet2.row_values(i)[3])
    

plt.scatter(x_mat,y_mat)
# for x, y in zip(x_mat, y_mat):
#     plt.text(x, y, (x, y), ha="center", va="bottom", fontsize=10)
plt.xticks([])
plt.yticks([])
plt.show()


