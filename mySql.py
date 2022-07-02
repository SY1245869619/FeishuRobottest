import pymysql

# ---------连接--------------
connect = pymysql.connect(host='localhost',  # 本地数据库
                          user='shenyuan',
                          password='123456',
                          db='feishurobot',
                          charset='utf8')  # 服务器名,账户,密码，数据库名称
cur = connect.cursor()
print(cur)
