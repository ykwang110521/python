#!/usr/bin/python
# _*_ coding: UTF-8 _*_
#print "\nhello world,你好，世界";

import time;
import calendar;
import support;#引用包
print (2222)
#str1 = raw_input('please input:');
#print str1;

print support.max_num(5,8)
print '==========================================='
print support.cal(2016,1)
print '==========================================='
ticks = time.time()
print "当前时间戳:",ticks
localtime = time.localtime(ticks)
print "本地时间:",localtime
print time.strftime("%Y-%m-%d",time.localtime())
cal = calendar.month(2016,8)
print "2016年8月份日历"
print cal
print '==========================================='

str = 'this is string ....'
print str.capitalize()
print str.isdigit()

print '==========================================='

str = 'abcdefghijk'
print str[3:]

list = ['aaa','bbb','ccc','ddd','eee','fff']
print list[2:4]
print list[1:]


dict = {}
dict['one'] = ['aaa','bbb']
print dict['one']

tinydict = {'name':'sam','code':1234,'age':28}
print tinydict
print tinydict.keys()
print tinydict.values()

flag = False
name = 'python'
if name == 'python':
	flag = True
	print 'welcome boss'
	print flag
else:
	print name

count = 0
while (count < 9):
	print 'The count is:',count
	count = count + 1
print 'good bye'

print range(1,6)
