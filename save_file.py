'''
"""
save_file.py
二进制文件存取示例

把图片保存到数据库dict中
    *存储文件路径 (占用空间少，读写效率高，一旦路径发生变化，需要修改)
    *将文件存储到数据库中(栈空间大，读写效率低)
'''
import  pymysql
import re

# 连接数据库
db = pymysql.connect(host = 'localhost',port = 3306,user = 'root',
                     password = '123456',
                     database = 'dict',charset = 'utf8')

#获取游标 (操作数据库，执行sql语句，得到执行结果)
cur = db.cursor()

# #执行语句
# with open('re1.png','rb') as f:
#     data = f.read()
#
# sql = "insert into images values(1,'你说呢',%s)"
# cur.execute(sql,[data])

#提取图片
sql = "select image from images where filname ='你说呢'"
cur.execute(sql)
data = cur.fetchone()
with open('你说呢.png','wb') as f:
    f.write(data[0])

#提交到数据库
db.commit()

#关闭游标
cur.close()

#关闭数据库
db.close()
