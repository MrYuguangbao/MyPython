import pymysql,sys,socket
db = pymysql.connect('localhost','root','yuguangbao','test')
cursor = db.cursor()
try:
    cursor.execute('select * from t_user')
    data = cursor.fetchall()
    for row in data:
        print(row[0], end=' ')
except:
    print('Error:unable to fetch data')


db.close()









































































































