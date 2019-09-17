'''
read_db.py
pymysql 读操作演示 (select)
'''
import pymysql

#连接数据库
db = pymysql.connect(host = 'localhost',port = 3306,user = 'root',
                     password = '123456',
                     database = 'stu',charset = 'utf8')
#获取游标 (操作数据库，执行sql语句，得到执行结果)
cur = db.cursor()

#执行语句
sql ="select name,age from class;"
cur.execute(sql)  #执行语句

#可以直接遍历游标
# for i in cur:
#     print(i)

#获取所有查询结果  #查询不到是一个空元组
# all_row = cur.fetchmany()
# print(all_row)

#获取多个查询结果
# many_row = cur.fetchmany()
# print(many_row)

#获取一个查询结果
one_row = cur.fetchmany()
print(one_row)

cur.close()
db.close()







