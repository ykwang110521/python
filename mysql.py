#!/usr/bin/python
# _*_ coding: UTF-8 _*_
import MySQLdb
#打开数据库连接
#db = MySQLdb.connect("localhost","homestead","secret","homestead") #连接本地homestead
db = MySQLdb.connect("60.12.225.137","dscs","ycp4nadIu&fcymLx4bnr","oppo_cn") #连接线上数据库从库

cursor = db.cursor()

#sql = "select * from orders where id < '%d' order by id desc" % (60)
sql = "select * from orders order by id desc limit 10"
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        ids = row[2]
        title = row[7]
        print "ids=%s,ordered_at=%s" % (ids,title)
except:
    print "Error:unable to fecth data"


#data = cursor.fetchone()

#print "Database is:%s" % data

db.close()

