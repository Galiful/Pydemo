#这是一条注释
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
print(str[-6:-4])           # 输出第一个到倒数第二个的所有字符
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
print('\n================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

#Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
#在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量 所指的内存 中|对象|的类型。
#Python允许你同时为多个变量赋值。例如：
a = b = c = 1
#也可以为多个对象指定多个变量
a, b, c = 1, 2, "runoob"