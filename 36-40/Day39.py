import pymysql

# 1. 创建连接（Connection）
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', password='1135651301y',
                       database='hrs', charset='utf8mb4')
try:
    # 2. 获取游标对象（Cursor）
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        cursor.execute('select `dno`, `dname`, `dloc` from `tb_dept`')
        # 4. 通过游标对象抓取数据
        row = cursor.fetchone()
        while row:
            print(row)
            row = cursor.fetchone()
except pymysql.MySQLError as err:
    print(type(err), err)
finally:
    # 5. 关闭连接释放资源
    conn.close()