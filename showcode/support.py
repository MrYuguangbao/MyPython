import math,pickle,pprint,builtins,os,shutil,glob,sys,re,random,smtplib,zlib,doctest,unittest,calendar,time
from urllib.request import urlopen
from datetime import date
from datetime import datetime
from timeit import Timer


if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('来自另一模块')
def fr(arg):
    print('hello:',arg)
    return

s = 'hello,\npython'
print(str(s))
print(repr(s))
for x in range(1, 11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),repr(x*x*x).rjust(4))
c = '12'.zfill(5)
print(c)
print('常量 PI 的值近似为： {!r}。'.format(math.pi))
print('常量 PI 的值近似为： {0:.4f}。'.format(math.pi))
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
for name,number in table.items():
    print('{0:10}==>{1:10d}'.format(name,number))
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
print('pi的近似值：%6.3f' % math.pi)
# istr = input('输入str:')
# print('输入的内容是：',istr)

# f = open('F:\\1.txt','a+')
# f.write('这是通过python内置的open函数写入文件')
# f.close()
# print('文件写入完成！')

print('-----------开始读取文件------------')
fres = open('F:\\1.txt','r')
s1 = fres.read()
print(s1)
fres.close()
print('-----------开始读取文件readline()------------')
fres = open('F:\\1.txt','r')
s1 = fres.readline()
print(s1)
fres.close()
print('-----------开始读取文件readlines()------------')
fres = open('F:\\1.txt','r')
s1 = fres.readlines()
print(s1)
fres.close()
print('-----------迭代读取文件每一行------------')
fres = open('F:\\1.txt','r')
for line in fres:
    print(line,end=' ')
fres.close()
fi = open('F:\\2.txt','w')
nu = fi.write('test write')
print('写入的字符数：',nu)
fi.close()
print('写入完成！')
fi = open('F:\\2.txt','w')
value = ('www.runoob.com', 14)
s2 = str(value)
fi.write(s2)
print(fi.tell())
fi.close()
print('----------with------------')
with open('F:\\2.txt','r') as f:
    read_data = f.read()
    print(read_data)
f.close()
print('----------pickle序列化------------')
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output = open('F:\\3.txt', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(data1, output)
# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)
output.close()
print('----------pickle反序列化------------')
pk1_file = open('F:\\3.txt', 'rb')
data1 = pickle.load(pk1_file)
pprint.pprint(data1)
data2 = pickle.load(pk1_file)
pprint.pprint(data2)
pk1_file.close()
print('----------异常------------')
# try:
#     pk12 = 1/0
#     print(pk12)
# except AssertionError as error:
#     print(error)
# else:
#     try:
#         with open('file.log') as file:
#             read_data = file.read()
#     except FileNotFoundError as fnf_error:
#         print(fnf_error)
# finally:
#     print('这句话，无论异常是否发生都会执行。')

# x = 10
# if x > 5:
#     raise Exception('x 不能大于 5。x 的值为: {}'.format(x))

# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

print('------------自定义异常------------')
class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
try:
    raise MyError(2*3)
except MyError as e:
    print('My Exception occurred:',e.value)

# try:
#     raise KeyboardInterrupt
# finally:
#     print('python finally module')

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide(1,0)
divide(1,2)
print('-----------文件读取------------')
with open('F:\\1.txt') as f:
    for line in f:
        print(line,end=' ')
print('文件读取完成')
class MyClass:
    i = 1
    def f(self):
        return 'hello python3'
x = MyClass()
print('属性i的值:',x.i)
print('类的方法f:',x.f())
class Comp:
    def __init__(self,real,virtual):
        self.real = real
        self.virtual = virtual
x = Comp(2.0,-3.9)
print('实部：',x.real,',虚部：',x.virtual)
class Test:
    def p(self):
        print(self)
        print(self.__class__)
t = Test()
t.p()
class Person:
    name = ''
    age = 0
    __weight = 0
    def __init__(self,name,age,weight):
        self.name = name
        self.age = age
        self.__weight = weight
    def speak(self):
        print('%s 说我 %d 岁' % (self.name,self.age))
p = Person('python3',17,120.0)
p.speak()
print('name:',p.name)

class Student(Person):
    grade = ''
    def __init__(self,name,age,weight,grade):
        Person.__init__(self,name,age,weight)
        self.grade = grade
    def speak(self):
        print('Student方法-----%s 说我 %d 岁,读 %d 年纪' % (self.name,self.age,self.grade))
s = Student('jon',16,100.0,5)
s.speak()

class Speaker():
    topic = ''
    name = ''
    def __init__(self,name,topic):
        self.name = name
        self.topic = topic
    def speak(self):
        print('Speaker方法-----我是%s，演讲的主题是%s' % (self.name,self.topic))

class sample(Student,Speaker):
    a = ''
    def __init__(self,name,age,weight,grade,topic):
        Speaker.__init__(self,name,topic)
        Student.__init__(self,name,age,weight,grade)
te1 = sample('Michle',16,100,3,'Python3')
te1.speak()

class Parent():
    def me(self):
        print('调用父类方法')

class Child(Parent):
    def me(self):
        print('调用子类方法')
c = Child()
c.me()
super(Child,c).me()
class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d,%d)' % (self.a,self.b)
    def __add__(self, other):
        return Vector(self.a+other.a,self.b+other.b)
v1 = Vector(2,12)
v2 = Vector(4,-5)
print(v1)
print(v2)
print(v1+v2)
print('-----------变量的作用域-------------')
ll = dir(builtins)
for x in ll:
    print(x,end=" -> ")
print('-------局部变量修改外部作用域的变量---------')
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()
print(num)

def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()
a = 10
def test(a):
    a = a + 1
    print(a)
test(a)
print('----------python标准库----------')
print(os.getcwd())
print(dir(os))
# print(help(os))
# shutil.copyfile('F:\\1.txt','F:\\4.txt')
# shutil.move('F:\\4.txt','F:\\工作文档')
print(glob.glob('*.py'))
print(sys.stdout.write('Warning, log file not found starting a new one\n'))
res = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(res)
res = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(res)
print('tea for too'.replace('too', 'two'))
print(math.e)
list = ['apple', 'pear', 'banana']
for i in range(5):
    print(random.random(),end=' ')
    print(random.choice(list))
print(random.sample(range(100), 10))
for i in range(10):
    print(random.randrange(6),end=' ')
print()
print('-----------访问互联网------------')
for line in urlopen('https://www.baidu.com'):
    line = line.decode('utf-8')
    if 'EST' in line or 'EDT' in line:
        print(line)
print('-----------使用邮件------------')
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org','send content')
# server.quit()
now = date.today()
print('now:',now)
nowtime = datetime.today()
print('nowtime:',nowtime)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
print(now.strftime('%b %B %a %A %y %Y'))
bir = date(2012,8,21)
age = now-bir
print(age.days)
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
print(zlib.crc32(s))
print('-----------性能度量------------')
t = Timer('t=a;a=b;b=t','a=1;b=2').timeit()
print(t)
t = Timer('a,b=b,a','a=1;b=2').timeit()
print(t)
print('-----------测试模块------------')
# def average(values):
#     return sum(values)/len(values)
# doctest.testmod()
#
# class TestStatisticalFunctions(unittest.TestCase):
#
#     def test_average(self):
#         self.assertEqual(average([20, 30, 70]), 40.0)
#         self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
#         self.assertRaises(ZeroDivisionError, average, [])
#         self.assertRaises(TypeError, average, 20, 30, 70)
# unittest.main()
print('-----------生成日历-----------')
# yy = int(input('输入年份'))
# mm = int(input('输入月份'))
# print(calendar.month(yy,mm))
print('-----------九九乘法表-----------')
for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(j,i,j*i),end=' ')
    print()
print('-----------自定义字体--------------')
name = 'yuguangbao'
lngth = len(name)
l = ""

for x in range(0, lngth):
    c = name[x]
    c = c.upper()

    if (c == "A"):
        print("..######..\n..#....#..\n..######..", end=" ")
        print("\n..#....#..\n..#....#..\n\n")

    elif (c == "B"):
        print("..######..\n..#....#..\n..#####...", end=" ")
        print("\n..#....#..\n..######..\n\n")

    elif (c == "C"):
        print("..######..\n..#.......\n..#.......", end=" ")
        print("\n..#.......\n..######..\n\n")

    elif (c == "D"):
        print("..#####...\n..#....#..\n..#....#..", end=" ")
        print("\n..#....#..\n..#####...\n\n")

    elif (c == "E"):
        print("..######..\n..#.......\n..#####...", end=" ")
        print("\n..#.......\n..######..\n\n")

    elif (c == "F"):
        print("..######..\n..#.......\n..#####...", end=" ")
        print("\n..#.......\n..#.......\n\n")

    elif (c == "G"):
        print("..######..\n..#.......\n..#.####..", end=" ")
        print("\n..#....#..\n..#####...\n\n")

    elif (c == "H"):
        print("..#....#..\n..#....#..\n..######..", end=" ")
        print("\n..#....#..\n..#....#..\n\n")

    elif (c == "I"):
        print("..######..\n....##....\n....##....", end=" ")
        print("\n....##....\n..######..\n\n")

    elif (c == "J"):
        print("..######..\n....##....\n....##....", end=" ")
        print("\n..#.##....\n..####....\n\n")

    elif (c == "K"):
        print("..#...#...\n..#..#....\n..##......", end=" ")
        print("\n..#..#....\n..#...#...\n\n")

    elif (c == "L"):
        print("..#.......\n..#.......\n..#.......", end=" ")
        print("\n..#.......\n..######..\n\n")

    elif (c == "M"):
        print("..#....#..\n..##..##..\n..#.##.#..", end=" ")
        print("\n..#....#..\n..#....#..\n\n")

    elif (c == "N"):
        print("..#....#..\n..##...#..\n..#.#..#..", end=" ")
        print("\n..#..#.#..\n..#...##..\n\n")

    elif (c == "O"):
        print("..######..\n..#....#..\n..#....#..", end=" ")
        print("\n..#....#..\n..######..\n\n")

    elif (c == "P"):
        print("..######..\n..#....#..\n..######..", end=" ")
        print("\n..#.......\n..#.......\n\n")

    elif (c == "Q"):
        print("..######..\n..#....#..\n..#.#..#..", end=" ")
        print("\n..#..#.#..\n..######..\n\n")

    elif (c == "R"):
        print("..######..\n..#....#..\n..#.##...", end=" ")
        print("\n..#...#...\n..#....#..\n\n")

    elif (c == "S"):
        print("..######..\n..#.......\n..######..", end=" ")
        print("\n.......#..\n..######..\n\n")

    elif (c == "T"):
        print("..######..\n....##....\n....##....", end=" ")
        print("\n....##....\n....##....\n\n")

    elif (c == "U"):
        print("..#....#..\n..#....#..\n..#....#..", end=" ")
        print("\n..#....#..\n..######..\n\n")

    elif (c == "V"):
        print("..#....#..\n..#....#..\n..#....#..", end=" ")
        print("\n...#..#...\n....##....\n\n")

    elif (c == "W"):
        print("..#....#..\n..#....#..\n..#.##.#..", end=" ")
        print("\n..##..##..\n..#....#..\n\n")

    elif (c == "X"):
        print("..#....#..\n...#..#...\n....##....", end=" ")
        print("\n...#..#...\n..#....#..\n\n")

    elif (c == "Y"):
        print("..#....#..\n...#..#...\n....##....", end=" ")
        print("\n....##....\n....##....\n\n")

    elif (c == "Z"):
        print("..######..\n......#...\n.....#....", end=" ")
        print("\n....#.....\n..######..\n\n")

    elif (c == " "):
        print("..........\n..........\n..........", end=" ")
        print("\n..........\n\n")

    elif (c == "."):
        print("----..----\n\n")
print('-----------实现秒表功能------------')
# print('按下回车开始计时，按下 Ctrl + C 停止计时。')
# while True:
# 
#     input("")  # 如果是 python 2.x 版本请使用 raw_input()
#     starttime = time.time()
#     print('开始')
#     try:
#         while True:
#             print('计时: ', round(time.time() - starttime, 0), '秒', end="\r")
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print('结束')
#         endtime = time.time()
#         print('总共的时间为:', round(endtime - starttime, 2), 'secs')
#         break










