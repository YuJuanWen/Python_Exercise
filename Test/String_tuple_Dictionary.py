# -*- coding:utf-8 -*-
#字符串输出
name = 'xiaoming'
position = '讲师'
address = '北京市昌平区建材城西路金燕龙办公楼1层'

print('--------------------------------------------------')
print("姓名：%s"%name)
print("职位：%s"%position)
print("公司地址：%s"%address)
print('--------------------------------------------------')

#字符串输入
userName = input('请输入用户名:')
print("用户名为：%s" % userName)

password = input('请输入密码:')
print("密码为：%s" % password)

#下标和切片
name = 'abcdef'

print(name[0])
print(name[1])
print(name[2])

print(name[0:3]) # 取 下标0~2 的字符
print(name[2:])  # 取 下标为2开始到最后的字符
print(name[1:-1])  # 取 下标为1开始 到 最后第2个  之间的字符

#字符串常见操作
mystr = 'hello world itcast and itcastcpp'
mystr.count("itcast") #count
mystr.replace("he","ha",1) #replace
mystr.title()#capitalize everywords
mystr.startswith("he")# turn back true or false
mystr.endswith("you")
mystr.lower()#所有字符转为小写
mystr.upper()#所有字符转为大写
mystr.ljust(5)#用空格填充至长度5  左对齐
mystr.rjust(5)#   右对齐
mystr.isalpha()
mystr.isdigit()
mystr.isalnum()
mystr.isspace()
str="wenyu"
mystr.join(str)

#列表  使用while循环

namesList = ['xiaoWang','xiaoZhang','xiaoHua']
length = len(namesList)
i = 0
while i<length:
    print(namesList[i])
    i+=1

#列表中的常见操作
A = ['xiaoWang','xiaoZhang','xiaoHua']

print("-----添加之前，列表A的数据-----")
for tempName in A:
    print(tempName)

#提示、并添加元素
temp = input('请输入要添加的学生姓名:')
A.append(temp)

print("-----添加之后，列表A的数据-----")
for tempName in A:
    print(tempName)
#extend可以将另一个集合中的元素逐一添加到列表中
a=[1,2]
b=[3,4]
a.append(b)
print(a)
a.extend(b)
print(b)
# 待查找的列表
nameList = ['xiaoWang', 'xiaoZhang', 'xiaoHua']

# 获取用户要查找的名字
findName = input('请输入要查找的姓名:')

# 查找是否存在
if findName in nameList:
    print('在字典中找到了相同的名字')
else:
    print('没有找到')

#删除
#del movieName[2]
#movieName.pop()
#movieName.remove('指环王')

#排序
#a.sort()
#a.reverse()

#列表的嵌套
import random

# 定义一个列表用来保存3个办公室
offices = [[],[],[]]

# 定义一个列表用来存储8位老师的名字
names = ['A','B','C','D','E','F','G','H']

i = 0
for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

i = 1
for tempNames in offices:
    print('办公室%d的人数为:%d'%(i,len(tempNames)))
    i+=1
    for name in tempNames:
        print("%s"%name,end='')
    print("\n")
    print("-"*20)
