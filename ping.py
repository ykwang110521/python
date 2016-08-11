#!/usr/bin/python 
#coding:utf-8
"""
import multiprocessing
import re 
import sys,os
import commands
import datetime
def  pinger(ip):
	cmd='ping -c 2 %s' % (ip.strip())
	ret = commands.getoutput(cmd)
	loss_re=re.compile(r"received, (.*) packet loss")
	packet_loss=loss_re.findall(ret)[0]
	rtt_re=re.compile(r"rtt min/avg/max/mdev = (.*) ")
	rtts=rtt_re.findall(ret)
	#rtt.split(["/"])
	rtt=rtts[0].split('/')
	rtt_min=rtt[0]
	rtt_avg=rtt[1]
	rtt_max=rtt[2]
	print "%s\t\t%s\t\t%s\t\t%s\t\t%s"%(ip,packet_loss,rtt_min,rtt_max,rtt_avg)



if __name__ == "__main__":
    if not os.path.exists("hosts.txt") :
	print "\033[31mhosts.txt文件不存在，请重试\033[0m"
	sys.exit(1)
    now=datetime.datetime.now()
    file=open('hosts.txt','r')
    pool=multiprocessing.Pool(processes=4)
    result=[]
    print "########%s###########"%now
    print "IPADDRSS\t\t\tLOSS\t\tMIN\t\tMAX\t\tAVG"
    for i in file.readlines():
        if len(i)==1 or i.startswith("#"):
           continue
        result.append(pool.apply_async(pinger,(i.strip(),))) 
    pool.close()           
    pool.join()
"""

"""
import urllib
import re
import sys

def ISIP(s):
    return len([i for i in s.split('.') if (0<= int(i)<= 255)])== 4

def URL(ip):
	uip=urllib.urlopen('http://wap.ip138.com/ip.asp?ip=%s'%ip)
	fip=uip.read()
	rip=re.compile(r"<br/><b>查询结果：(.*)</b><br/>")
	result=rip.findall(fip)
	print "%s\t %s" %(ip,result[0])

def DO(domain):
        url=urllib.urlopen('http://wap.ip138.com/ip.asp?ip=%s'%domain)
        f=url.read()
        #print f
        r=re.compile(r'&gt; (.*)<br/><b>查询结果：(.*)</b><br/>')
        result=r.findall(f)
	#print type(result)
	for i in result:
        	print "%s\t %s\t %s\t" %(domain,i[0],i[1])

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "请输入IP地址或者域名 (例如:192.168.1.1 / www.baidu.com)"
		sys.exit()
	INPUT=sys.argv[1]
	#print len(sys.argv) 
	#sys.exit()
	if not re.findall('(\d{1,3}\.){3}\d{1,3}',INPUT):
	        if re.findall(r'(\w+\.)?(\w+)(\.\D+){1,2}',INPUT) :
	                DOMAIN=INPUT
			DO(DOMAIN)
	        else:
	                print "输入的IP地址和域名格式不对！"
	else:
	        if ISIP(INPUT)  :
	                IPADDRESS=INPUT
			URL(IPADDRESS)
	        else:
	                print "IP 地址不合法，请重新输入！"
"""

import urllib
import re
import threading
import time
import socket

# 设置这么长时间超时
socket.setdefaulttimeout(8)

# 抓网页的地址起始数字
i = 800000
# 存储线程的个数
thirdCount = 0

# 处理抓取任务
def loop():
	global i,thirdCount,titleRegex,NLRegex
	i += 1
	# 当前网页的编号
	pageNum = i
	# 表示新线程启动了
	thirdCount += 1
	
	pageUrl = "http://wapypk.39.net/manual/" + str(pageNum)
	try:
		request = urllib.urlopen(pageUrl)
	except Exception, e:
		# 减少一个线程
		thirdCount -= 1
		return
	
	# 不正常就退出
	if request.getcode() != 200:
		print "不正常的页面:" + str(pageNum) + " 返回值:" + str(request.getcode())
		# 关闭请求
		request.close()
		# 减少一个线程
		thirdCount -= 1
		return
	print "正常的页面:" + str(pageNum)
	
	f.write(pageUrl + '\n')
	# 关闭请求
	request.close()
	# 减少一个线程
	thirdCount -= 1
	
startTime = time.time()
f = open('/home/vagrant/www/swoole/python/cc.c','a+')
while i < 830000:
	num = i + 1
	# 线程要始终保持在50个
	if thirdCount < 50:
		print '【新进程】:' + str(num) + "loopThird" + "进程总数:" + str(thirdCount)
		t = threading.Thread(target = loop, name = str(num) + "loopThird")
		t.start()
	time.sleep(0.001)

thisStartTime = time.time()
while thirdCount != 0:
	# 等待超时就退出（没有这个有时候线程并不能全部退出，看资源管理器，说“等候频道 poll_scheme_time”）
	if time.time() - thisStartTime > 10:
		print "等待时间到,强行退出."
		break
	print "等待线程全部结束！还有" + str(thirdCount) + "个线程在工作"
	time.sleep(0.010)
endTime = time.time()

allTime = endTime - startTime
f.close()
print "完成!花费时间:" + str(allTime) + "s"