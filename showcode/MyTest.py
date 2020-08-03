import sys,support
from collections import deque

x='runoob';sys.stdout.write(x+'\n')
str='Runoob'
print(str[0:2])
print(str[1:])
print(str*2)
print(str+'hello')
print(r'hello\npython')
# input('\n\n按enter建')
print('python路径为',sys.path)
a,b,c=1,True,'hello python'
d=2+1j
print(type(a),type(b),type(c),type(d))
print(isinstance(b,bool))
print(2/6)
print(2//6)
print(2**3)
list=[3,54,6,'hello python']
print(list[1:3])
print(list*2)
tiny=['hello','world']
print(list+tiny)
list[0]='pycharm'
print(list)


def reverseWord(input):
   inputWords = input.split(" ")
   inputWords = inputWords[-1::-1]
   output = " ".join(inputWords)
   return output


if __name__=="__main__":
    input = "i like python"
    rw = reverseWord(input)
    print('翻转后的结果：'+rw)

tuple=(2.3,True,'python',46)
tinytuple=(234,'tuple')
print(tuple[0])
print(tuple[1:4])
singletuple=(20)
print(singletuple)
sites = {'Google', 'Taobao', 'Runoob', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)
if 'Taobao' in sites:
    print('在集合中')
else:
    print('不在集合中')

seta = set('azcd')
setb = set('auzcm')
print(seta-setb)
print(seta|setb)
print(seta&setb)
print(a^b)
dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2]     = "2 - 菜鸟工具"
print(dict['one'])
print(dict[2])
print(dict)
print(dict.keys())
print(dict.values())
print(chr(65))
print(ord('a'))
print(hex(15))
'''
多行注释
'''
a=[4,5,6,7]
del a[2]
print(a)
if(n:=len(a))>3:
    print(f"list is too long")

vara=10
varb=10
if(vara is varb):
    print('1-a和b相同的标识')
else:
    print('1-a和b不同的标识')
if(id(vara)==id(varb)):
    print('1-a和b相同的地址')
else:
    print('1-a和b不同的地址')
print(id(vara))
print(id(varb))
print(2.5e2)
print(5/2)
print(5//2)
print(5//2.0)
print(range(10))
print('\a')
print('我是%s今年%d'%('Yu',18))
para_str = """这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
"""
print (para_str)
name='python'
print(f'Hello {name}')
print(f'{1 + 2}')
m=1
print(f'{1+m=}')
print(name.capitalize())
print(name.center(3,' '))
ela='elasticsearch教程'
print(ela.count('e'))
print(ela.endswith('ch'))
print(ela.expandtabs())
print(ela.isalnum())
print(ela.isalpha())
s1='a,b,c,d,e,f,g'
print(len(s1))
print(max(ela))
print(min(ela))
a1=[4,5,6,7]
del a1[2]
print(a1)
t1="a","b","c","d","e"
print(type(t1))
t2=(20)
print(type(t2))
t3=(20,)
print(type(t3))
t4=(10,)
print(id(t3))
print(id(t4))
dict = {'Alice': '2341', 'Beth': '9102', 'Alice': '3258'}
dict['Johon']='8888'
print(dict)
# del dict['Beth']
# print(dict)
# dict.clear()
# print(dict)
# del dict
# print(dict)
print(len(dict))
print(type(dict))
print(dict.pop('Beth'))
print(dict)
thisset = set(("Google", "Runoob", "Taobao"))
thisset.update({'hello','python'})
print(thisset)
thisset.remove('hello')
print(thisset)
thisset.discard('python')
print(thisset)
thisset.pop()
print(thisset)
print(len(thisset))
thisset.clear()
print(thisset)
x,y=0,1
while y<10:
    print(y,end=' ')
    x,y=y,x+y
co=1
while co<9:
    if(co%2==0):
        print(co,'是偶数')
    else:
        print(co,'是奇数')
    co+=1
cou=0
while cou<7:
    print(cou,'小于7')
    cou += 1
else:
    print(cou,'大于等于7')
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
for i in range(1,17,5):
    print(i,end=' ')
print()
arr = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(arr)):
    print(i,arr[i])

for letter in 'Runoob':
    if letter == 'o':
        pass
        print('执行 pass 块')
    print('当前字母 :', letter)

print("Good bye!")
print('------------迭代器-------------')
list1=[1,2,4,5,6]
it=iter(list1)
for x in it:
    print(x,end=" ")
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 10:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myNumbers = MyNumbers()
myiter = iter(myNumbers)
for i in myiter:
    print(i)
print('\n-------------生成器-------------')
def fa(n):
    a,b,count = 0,1,0
    while True:
        if(count>n):
            return
        yield a
        a,b = b,a+b
        count += 1
f1 = fa(7)
# while True:
#     try:
#         print(next(f1),end=" ")
#     except StopIteration:
#         sys.exit()
print('\n-------------函数-------------')
def changeInt(a):
    a = 10
b = 5
changeInt(b)
print('b=',b)
def changeList(listParam):
    listParam.append([7,8,9])
    print('函数内:',listParam)
    return
listParam=[4,5,6]
changeList(listParam)
print('函数外:',listParam)
def printParam(s):
    print(s)
    return
printParam(s='python编程')
def f2(name,age=17):
    print('name=',name)
    print('age=',age)
    return
f2(age=18,name='python数据分析')
print('\n-------------不定长参数-------------')
def pr1(arg1,*vart):
    print('arg1=',arg1)
    for v in vart:
        print(v)
    return
pr1(54,39,67,29)
def pr2(arg1,**dictp):
    print('arg1=',arg1)
    print(dictp)
pr2(1,key1=49,key2=39)
def pr3(a,b,*,c):
    return a+b+c
print(pr3(1,2,c=3))
sum = lambda a1,a2:a1+a2
print('sum:',sum(3,4))
stack=[4,5,6]
stack.append(7)
stack.append(8)
print('stack:',stack)
print('pop:',stack.pop())
print('pop:',stack.pop())
print('pop:',stack.pop())
print('pop:',stack.pop())
qu = deque(['ele1','ele2','ele3'])
qu.append('ele4')
qu.append('ele5')
qu.append('ele6')
print(qu.popleft())
print(qu.popleft())
print(qu.popleft())
print(qu.popleft())
var1=[4,5,6]
var2 = [5*x for x in var1]
print(var2)
var3 = [[x,x**2] for x in var1]
print(var3)
fruit = ['  banana','  log','pass fruit  ']
res = [w.strip() for w in fruit]
print(res)
var4 = [2*x for x in var1 if x >4]
print(var4)
vec1 = [4,5,-3]
vec2 = [6,2,7]
vec3 = [x*y for x in vec1 for y in vec2]
print(vec3)
vec4 = [x+y for x in vec1 for y in vec2]
print(vec4)
vec5 = [vec1[i]*vec2[i] for i in range(len(vec1))]
print(vec5)
vec6 = [vec1[i]-vec2[i] for i in range(len(vec1))]
print(vec6)
print('--------矩阵转置.1---------')
matrix = [
    [1,4,7,10,13],
    [2,5,8,11,14],
    [3,6,9,12,15],
]
vmatrix = [[row[i] for row in matrix] for i in range(5)]
print(vmatrix)
print('--------矩阵转置.2---------')
t = []
for i in range(5):
    t.append([row[i] for row in matrix])
print(t)
print('--------矩阵转置.3---------')
t1 = []
for i in range(5):
    t = []
    for row in matrix:
        t.append(row[i])
    t1.append(t)
print(t1)
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
del a[2:4]
print(a)
a1 = [-1, 1, 66.25, 333, 333, 1234.5]
del a1[:]
print(a1)
a2 = 12,23,'undefined'
print(a2)
print(a2[1])
u = a2,(1,2,3,4,5)
print(u)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('orange1' in basket)
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
tel = {'jack': 4098, 'sape': 4139,'rook':2309,'rzke':3420}
print(tel['jack'])
# del tel['sape']
# print(tel)
print(tel.keys())
print(tel.values())
print(sorted(tel.keys()))
print('jack' in tel)
print('rake' in tel)
v = {x:x**3 for x in (3,5,7)}
print(v)
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)
for i,v in enumerate(['tic', 'tac', 'toe']):
    print('[i]:',i,',[v]:',v)
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue','zzz']
for q,a in zip(questions,answers):
    print('questions:{0},answers:{1}'.format(q,a))
for i in reversed(questions):
    print(i)
print('-------------- 模块调用 -------------')
support.pr('python!')
print(dir(support))
print('sys:',dir(sys))
print('all',dir())



















