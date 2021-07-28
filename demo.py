print("hello world")

# 6 种标准数据类型
# 数字 number
a = 1
# 字符串 string
b = "字符串"
# 列表 list
c = ["列表1", "列表2", "列表3"]
# 元组 tuple
d = ('云课堂', '202107')
# 集合 set
e = {1, 2, 3, 4, 5}
# 字典 dict
f = {"名称": "云课堂", "时间": "202107"}
print("--------数字及运算----------")
a = 10
b = 3
c = 3.0
print("a + b = ", a + b)
print("a + c = ", a + c)
print("a * b = ", a * b)
print("a - b = ", a - b)
print("a / b = ", a / b)    # 除法
print("a / c = ", a / c)
print("a // b = ", a // b)   # 整除
print("a // c = ", a // c)
print("a % b = ", a % b)    # 取余

# 字符串的表达方式
print("--------字符串----------")
s = 'i am a string'
print(s)
s = "i am a string"
print(s)
s = 'i am a "string"'
print(s)
s = "i am a 'string'"
print(s)
s = "i am a \"string\""
s = '''连续的三个单引号"\'\'\'"可以用来表示多行字符串组成的一段文字
就像这样：
第一段
第二段
第三段'''
print(s)

# 字符串常用操作
strA = "abcdef"
strB = "hijklmn"
print("strA:", strA, sep="\t")
print("strB:", strB, sep="\t")
print("strA + strB:", strA + strB, sep="\t")
print("strA + str(2021):", strA + str(2021), sep="\t")
print("strA[0:3]:", strA[0:3], sep="\t")
print("strA[:3]:", strA[:3], sep="\t")
print("strA[1:3]:", strA[1:3], sep="\t")
print("strA[3:]:", strA[3:], sep="\t")
print("strA[-3:]:", strA[-3:], sep="\t")
print("strA[-3:-1]:", strA[-3:-1], sep="\t")

# 列表常用操作
print("--------列表------------")
li = [1,2,3,4,5]
print(li)
li2 = ['a', 'b', 'c', 'd', 'e']
print(li2)
li3 = [li, li2]
print(li3)
li.append(6)
li.remove(2)
print(li)
print(li3)
li = [1, 2, 3, 4, 5]
print(li[:3])
print(li[1:3])
print(li[3:])
print(li[-2:])
print(li[:-1])

# 元组常用操作
print("-----------元组-------------")
t = ()
t1 = (1,)
t2 = ('a', 'b', 'c')
print(t2[0])
print(t2[1:])
print(t2[0:2])

# 集合
print("-----------集合-------------")
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)
print('Jim' in student)
a = set('abracadabra')
b = set('alacazam')
print(a)
print(b)
# a与b的差集
print(a - b)
# 并集
print(a | b)
# 交集
print(a & b)
# a和b中不同时存在的元素
print(a ^ b)

# 字典
print("-----------字典-----------------")
# 定义
course = {'name':'python开发入门', 'time':'202107'}
print(course)
# 取值
print(course['name'])
# print(course['date'])
# 修改值
course['time'] = '202108'
print(course)
# 增加属性
course['studentNum'] = 3
course['students'] = {'张三', '李四', '王五'}
print(course)
# 删除属性
del course['studentNum']
print(course)

# 混合数据结构
courseList = [
    {
        "name": "python", 
        "time": ('2021', '07', '20'), 
        "stuNum":3, 
        'students':{'张三', '李四', '王五'}
    },
    {
        "name": "java",
        "time": ('2021', '08', '27'),
        "stuNum": 2,
        'students': {'张三', '李四'}
    }
]


def add(a, b):
    s = a + b
    return s

s = add(1, 2)
print(s)
print(add(10, 5))

def printInfo(name, age=20):
    print('name:', name)
    print('age:', age)


printInfo('Tom')
printInfo('Alice', 30)

def addUnlimited(*n):
    s = 0
    print(n)
    for i in n:
        s = s + i
    return s

print(addUnlimited(1,2,3,4,5,6,7,8,9,10))

def getNone():
    return

print(getNone())

def cal(a, b):
    return a + b, a * b

s, m = cal(2, 3)
print('s=',s)
print('m=',m)

for i in range(10):
    print(i)

for i in range(2,10,2):
    print(i)

for i in range(10,1,-2):
    print(i)

week = ['Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday', 'Sunday' ]
for day in week:
    print(day)

for course in courseList:
    for key in course.keys():
        print(key, '-', course[key])
    print('-------------------')


def intNum():
    print("开始执行")
    for i in range(5):
        yield i
        print("继续执行")

num = intNum()
print(next(num))
print(next(num))
print(next(num))

for i in num:
    print(i)



