import re
r = re.match('www','www.baidu.com').span()
print('在起始位置匹配:',r)
r = re.match('com','www.baidu.com')
print('不在起始位置匹配:',r)
line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*',line,re.M | re.I)
if(matchObj):
    print('matchObj.group()',matchObj.group())
    print('matchObj.group(1)',matchObj.group(1))
    print('matchObj.group(2)',matchObj.group(2))
else:
    print('no match!')
r = re.search('www','www.baidu.com').span()
print(r)
r = re.search('com','www.baidu.com').span()
print(r)
print('--------------插入排序---------------')
def insertionSort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
s = [4,5,3,6,1,12,10,9]
insertionSort(s)
print(s)
print('---------------快速排序--------------')
# def partition(arr,low,high):
#     i = low-1
#     pivot = arr[high]
#     for j in range(low,high):
#         if arr[j]<=pivot:
#             i += 1
#             arr[i],arr[j] = arr[j],arr[i]
phone = "2004-959-559 # 这是一个电话号码"
num = re.sub(r'#.*$','',phone)
print('num:',num)
num = re.sub(r'\D','',phone)
print('num:',num)
def dou(match):
    value = int(match.group('value'))
    return str(value*2)
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', dou, s))
pattern = re.compile(r'\d+')
re1 = pattern.findall('runoob 123 google 445')
print(re1)
it = re.finditer(r"\d+","12ief45rew98lk23")
for m in it:
    print(m.group(),end=' ')






























































