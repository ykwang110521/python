#!/usr/bin/python
# _*_ coding: UTF-8 _*_
import uuid
import MySQLdb

#生成激活码
def generate_key():
    key_list = []
    for i in range(200):
        uuid_key = uuid.uuid3(uuid.NAMESPACE_DNS,str(uuid.uuid1()))
        key_list.append(str(uuid_key).replace('-',''))
    return key_list

#写入数据库
def write_to_db(key_list):
    db = MySQLdb.connect("localhost","homestead","secret","homestead")

    cursor = db.cursor()
#    cursor.execute("drop table if exists uuid_code")

#    sql = """create table uuid_code (
#            key_value char(40) not null
#            )"""

#    cursor.execute(sql)

    try:
        for i in range(200):
            cursor.execute('insert into uuid_code values("%s")' % (key_list[i]))
       
        db.commit()

    except:
       
       db.rollback()


    db.close()
    return 1
#print generate_key()
ret = write_to_db(generate_key())
if (ret == 1):
    print "插入数据成功"
else:
    print "插入数据失败"
