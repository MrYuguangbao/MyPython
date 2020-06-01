import pymysql

class User(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password

# 操作MySQL
# db = pymysql.connect('localhost', 'root', 'yuguangbao', 'test')
# cursor = db.cursor()
# sql = 'select * from course_dashboard'
#
# try:
#     # 查询数据
#     # result = cursor.execute(sql)
#     # print(result)
#     # info = cursor.fetchmany(result)
#     # for li in info:
#     #     print(li)
#
#     # 添加数据
#     user = User('Y','123')
#     sqli = "insert into user(username,password) values (%s, %s)"
#     cursor.executemany(sqli, [(user.username, user.password)])
#     cursor.close()
#     db.commit()
# except:
#     # 回滚
#     db.rollback()
# db.close()
# print('数据库操作完成')
lists = []
user1 = User('naem1','adfd12')
lists.append(user1)
user2 = User('naem2','adfd13')
lists.append(user2)
print(len(lists))
s = "wwww/baido/com"
print(s[s.rfind('/'):])
courses = ['1','2','3','4','5','6','7']
print(courses[len(courses)-2])
print(''.join(courses[2:len(courses)-2]))
arrs = s.split("/")
for e in arrs:
    print(e)
mystr = 'abc'
if mystr == 'bc':
    print('bingo')
