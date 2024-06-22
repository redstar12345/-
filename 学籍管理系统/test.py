import pymysql

conn = pymysql.connect(host = '127.0.0.1', port = 3306, user = 'root', passwd = 'Dth20030116', charset = 'utf8')
cursor = conn.cursor()

cursor.execute("use sufeclinic_db")
sql = "select * from Doctor"
cursor.execute(sql)
data = cursor.fetchall()  # 获得表格数据（二维元组）
row = len(data)
vol = len(data[0])
print(data, data[0], row, vol)