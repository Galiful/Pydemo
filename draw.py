from matplotlib import pyplot as plt
import numpy as np
import csv
#用来正常显示中文标签
plt.rcParams['font.sans-serif']=['SimHei'] 
#用来正常显示负号 
plt.rcParams['axes.unicode_minus']=False

#定义两个空列表存放x,y轴数据点
x=[]
y=[]
with open("C:/Users/Administrator/Desktop/file/1733.csv",'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',') 
    for row in plots: 
        x.append((row[2]))  #从csv读取的数据是str类型
#         print("x:",x)
        y.append((row[3])) 
#         print("y:",y)
#画折线图
plt.plot(x,y,label='模拟数据')
plt.xlabel('x') 
plt.ylabel('y')
plt.title('演示从文件加载数据') 
plt.legend() 
plt.show()
