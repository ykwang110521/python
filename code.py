#!/usr/bin/python
# _*_ coding: UTF-8 _*_
import uuid

#生成随机串
def generate_key():
    key_list = []
    for i in range(2000):
        uuid_key = uuid.uuid3(uuid.NAMESPACE_DNS,str(uuid.uuid1()))
        key_list.append(str(uuid_key).replace('-',''))
    return key_list

#打开一个文件
fo = open("a.txt","wb")
#写入文件操作
def write_to_file(key_list):
    try:
        for i in range(2000):
            fo.write(key_list[i])
            fo.write('\n')

    except:
        print '写入异常'
        return 0

    fo.close()
    return 1

ret = write_to_file(generate_key())

if (ret == 1):
    print '写入文件成功'
else:
    print '写入文件失败'
