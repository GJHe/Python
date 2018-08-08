#_*_coding:utf-8_*_
#Author：ymxowgk

a = 21
b = 10
c = 0

c = a + b
print ("1 - c 的值为：", c)

c = a - b
print ("2 - c 的值为：", c)

c = a * b
print ("3 - c 的值为：", c)

c = a / b
print ("4 - c 的值为：", c)

c = a % b
print ("5 - c 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a**b
print ("6 - c 的值为：", c)

a = 10
b = 5
c = a//b
print ("7 - c 的值为：", c)

































"""
import sys
#print(sys.path)#打印环境变量
print(sys.argv)#打印相对路径
print(sys.argv[2])"""
"""
import os
#cmd_res = os.system("dir")#执行命令，不保存结果
cmd_res = os.popen("dir").read()
print("-->",cmd_res)
os.mkdir("day2")#当前目录下创建新文件夹"""

import sys

print(sys.path)
