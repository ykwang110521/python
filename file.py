#!/usr/bin/python
# _*_ coding: UTF-8 _*_

# 打开一个文件并写入字符串
#fo = open("a.txt","wb")
#print fo.name,fo.mode,fo.closed
#count = 0
#while (count < 100):
#    fo.write('aaaaaaaaaaaaaa\nddddddddddddddddd\n')
#    count += 1

#fo.close()

# 打开一个文件并读取内容
#fo = open('a.txt',"r+")
#str1 = fo.read()
#print str1
#fo.close()

# 创建文件夹
#import os
#os.mkdir("test")

#异常处理
try:
    fh = open('a.txt','r+')
    print fh.name
except IOError:
    print "Error: 没有找到文件"
else:
    print "文件写入/读取成功"
    fh.close()
