#这是一条注释
#以下为直接运行.py模式, 而交互式运行代码会直接给出表达式的结果
#交互式每一句代码都是一个整体，会单独运行一次，不过共享整个缓存；而运行.py文件时里面的所有代码是一个整体。

#/////////////在 python 中，类型属于对象，变量是没有类型的/////////////


import keyword
print (keyword.kwlist.append("\n"))#python保留字
message = "你好，china"
number = 3/2 
print(message.title()+str(number))#str()将数字转为字符串
print(number)#python2 =1
#Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
total = word + \
        sentence + \
        paragraph
print (total)
#python中数字有四种类型：整数、布尔型、浮点数和复数:int bool float complex
#python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {} ：
if True:
    print ("True")
else:
    print ("False")
#缩进不一致，执行后会出现类似以下错误：unindent does not match any outer indentation level

#python中单引号和双引号使用完全相同。
#使用三引号('''或""")可以指定一个多行字符串。
#转义符 '\'
#反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如 r"this is a line with \n" 则\n会显示，并不是换行。
#按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
#字符串可以用 + 运算符连接在一起，用 * 运算符重复。
#Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
#Python中的字符串不能改变。
#Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
#字符串的截取的语法格式如下：变量[头下标:尾下标:步长]

str='Runoob'
print(str)                 # 输出字符串
print(str[-6:-4])          # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
#message=input("\n按下 enter 键后退出。")
#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
print( str, end=" " )
print( str, end=" " )

#在 python 用 import 或者 from...import 来导入相应的模块。

#将整个模块(somemodule)导入，格式为： import somemodule

#从某个模块中导入某个函数,格式为： from somemodule import somefunction

#从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc

#将某个模块中的全部函数导入，格式为： from somemodule import *
import sys
print('\n================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)
 #  导入特定的成员
from sys import argv,path 
print('\n================python from import===========================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

#Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
#在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量 所指的内存 中|对象|的类型。
#Python允许你同时为多个变量赋值。例如：
a = b = c = 1
#也可以为多个对象指定多个变量
#一个变量可以通过赋值指向不同类型的对象
a, b, c, d = 20, 5.5, True, 4+3j

#***************Python3 中有六个标准的数据类型：
#不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
#可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。

print (2/4) # 除法，得到一个浮点数
print (2//4)# 除法，得到一个整数
print (2**3)# 乘方

#Python 列表截取可以接收第三个参数，参数作用是截取的步长（-1 表示逆向） letters[1:4:2],1-4以步长2截取 =1，3

#List（列表） 是 Python 中使用最频繁的数据类型。
#列表可以完成大多数集合类的数据结构实现。列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。
#列表是写在方括号 [] 之间、用逗号分隔开的元素列表。
#和字符串一样，列表同样可以被索引和截取，列表被截取后返回一个包含所需元素的新列表。\
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表
#//////Python包含以下方法:
#1	list.append(obj)
#在列表末尾添加新的对象
#2	list.count(obj)
#统计某个元素在列表中出现的次数
#3	list.extend(seq)
#在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
#4	list.index(obj)
#从列表中找出某个值第一个匹配项的索引位置
#5	list.insert(index, obj)
#将对象插入列表
#6	list.pop([index=-1])
#移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
#7	list.remove(obj)
#移除列表中某个值的第一个匹配项
#8	list.reverse()
#反向列表中元素
#9	list.sort( key=None, reverse=False)
#对原列表进行排序
#10	list.clear()
#清空列表
#11	list.copy()
#复制列表

#元组（tuple）与列表类似，不同之处在于元组的元素///不能修改。元组写在小括号 () 里，元素之间用逗号隔开。
#元组中的元素类型也可以不相同
#元组与字符串类似，可以被索引且下标索引从0开始，-1 为从末尾开始的位置。也可以进行截取（看上面，这里不再赘述）。
#其实，可以把字符串看作一种特殊的元组。
#虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。tuple(list)//将元组转换为列表：list(seq)
#但我们可以对元组进行连接组合：tup3 = tup1 + tup2;
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob')
 
print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组

#集合（set）是由一个或数个形态各异的大小整体组成的，无序的不重复元素序列。
#基本功能是进行成员关系测试和删除重复元素。
#可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)   # 输出集合，////重复的元素被自动去掉
# 成员测试
if 'Rose' in student :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中') 
 
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a) 
print(b)
print(a - b)     # a 和 b 的差集 
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素

#字典（dictionary）是Python中另一个非常有用的内置数据类型。
#列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
#字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
#键(key)必须使用不可变类型。
#在同一个字典中，键(key)必须是///唯一的。
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
 
print (dict['one'])       # 输出键为 'one' 的值
print (dict[2])           # 输出键为 2 的值
print (tinydict)          # 输出完整的字典
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值
print (tinydict.items())  # 输出键值对

#构造函数 dict() 可以直接从键值对序列中构建字典如下：
#dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
#{'Taobao': 3, 'Runoob': 1, 'Google': 2}
 
#{x: x**2 for x in (2, 4, 6)}
#{2: 4, 4: 16, 6: 36}
 
#dict(Runoob=1, Google=2, Taobao=3)
#{'Runoob': 1, 'Google': 2, 'Taobao': 3}

#Python逻辑运算符
#x and y	布尔"与"
#x or y	布尔"或"
#not x	布尔"非"
# and中含0，返回0； 均为非0时，返回后一个值， 
print(2 and 0)   # 返回0
print(2 and 1)   # 返回1
print(1 and 2)   # 返回2

# or中都是0，返回0；至少有一个非0时，返回第一个非0,
print(2 or 0)   # 返回2
print(2 or 1)   # 返回2
print(0 or 1)  # 返回1 
a =1
print (a)
a=2
print(a)

#\(在行尾时)	续行符
para_str = """当你需要一块HTML或者SQL时，这时用字符串组合，特殊字符串转义将会非常的繁琐。
这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)

#在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集。使用的语法是在字符串前面加上前缀 u。

#在Python3中，所有的字符串都是Unicode字符串。

str = "runoob"


#center(width, fillchar) 返回一个指定的宽度 width 居中的字符串
print ("str.center(40, '*') : ", str.center(10, '*'))

#Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else


#在 while … else 在条件语句为 false 时执行 else 的语句块
#如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中， 如下所示
#while (flag): print ('欢迎访问菜鸟教程!')


#Python pass是空语句，是为了保持程序结构的完整性。
#pass 不做任何事情，一般用做占位语句
for element in "Python":  
     if element == "y":  
         pass  
     else:  
         print(element)


#迭代是Python最强大的功能之一，是访问集合元素的一种方式。
#迭代器是一个可以记住遍历的位置的对象。
#迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
#迭代器有两个基本的方法：iter() 和 next()。
#字符串，列表或元组对象都可用于创建迭代器


#在 Python 中，使用了 yield 的函数被称为生成器（generator）函数

#不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
#可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了

#////////python 使用 lambda 来创建匿名函数
#!/usr/bin/python3
 
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2
 
# 调用sum函数
print ("相加后的值为 : ", sum( 10, 20 ))
print ("相加后的值为 : ", sum( 20, 20 ))


#queue.popleft()  //从左边出列

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


#rjust() 方法, 它可以将字符串靠右, 并在左边填充空格
#zfill(), 它会在数字的左边填充 0


#self指的是类实例对象本身(注意：不是类本身)


#% 操作符也可以实现字符串格式化

# Python 元素除了是 0、空、None、False 外都算 True。
#if not data //判断data 是否为空

#比较遗憾的一件事情是Python的多线程并不能发挥CPU的多核特性
#在Python语言中，单线程+异步I/O的编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序。
#协程最大的优势就是极高的执行效率，因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销。
#协程的第二个优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不用加锁，
#只需要判断状态就好了，所以执行效率比多线程高很多，如果想要充分利用CPU的多核特性，最简单的方法是多进程+协程，
#既充分利用多核，又充分发挥协程的高效率，可获得极高的性能



#通过with关键字指定文件对象的上下文环境并在离开上下文环境时自动释放文件资源：
with open('致橡树.txt', 'r', encoding='utf-8') as f:
            print(f.read())

#Python repr() 函数
#repr() 函数将对象转化为供解释器读取的形式：返回一个对象的 string 格式


#random.randint(a,b)用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n: a <= n <= b。

#type() 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。
#isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。

#isinstance() 与 type() 区别：
#type() 不会认为子类是一种父类类型，不考虑继承关系。
#isinstance() 会认为子类是一种父类类型，考虑继承关系。
#如果要判断两个类型是否相同推荐使用 isinstance()。