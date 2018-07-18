#encoding=utf-8
# -*- coding:utf-8 -*-

print("this is a simple test for pycharm  and github.")
print("more test.")

#if-else

knif=11

if knif > 10 :
    print("不允许上火车")

else:
    print("可以上车")


#elif  注意：elif必须和if一起使用
score = 77

if score>=90 and score<=100:
    print('本次考试，等级为A')
elif score>=80 and score<90:
    print('本次考试，等级为B')
elif score>=70 and score<80:
    print('本次考试，等级为C')
elif score>=60 and score<70:
    print('本次考试，等级为D')
elif score>=0 and score<60:
    print('本次考试，等级为E')

#if嵌套
seat =2
money=40
if money>2:
    if seat>0:
        print("上车吧")
    else:
        print("no seat to seat")
else:
    print("no seat")

#if应用--猜拳

import random

player = input('请输入：剪刀(0)  石头(1)  布(2):')

player = int(player)

computer = random.randint(0,2)

# 用来进行测试
#print('player=%d,computer=%d',(player,computer))

if ((player == 0) and (computer == 2)) or ((player ==1) and (computer == 0)) or ((player == 2) and (computer == 1)):
    print('获胜，哈哈，你太厉害了')
elif player == computer:
    print('平局，要不再来一局')
else:
    print('输了，不要走，洗洗手接着来，决战到天亮')

#while
i = 0
while i<5:
    print("当前是第%d次执行循环"%(i+1))
    print("i=%d"%i)
    i+=1

#while循环应用
i = 1
sum = 0
while i<=100:
    sum = sum + i
    i += 1

print("1~100的累积和为:%d"%sum)

#while循环应用2
i = 1
sum = 0
while i<=100:
    if i%2 == 0:
        sum = sum + i
    i+=1

print("1~100的累积和为:%d"%sum)

#while循环嵌套
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%-2d " % (j, i, i * j), end='')
        j += 1
    print('\n')
    i += 1

#for循环
name='wenyujuan'
for  x in name:
    print(x)


#break和continue
name = 'dongGe'

for x in name:
  print('----')
  if x == 'g':
      break
  print(x)

i = 0

while i<10:
  i = i+1
  print('----')
  if i==5:
      break
  print(i)

#while循环--带continue
i = 0

while i<10:
  i = i+1
  print('----')
  if i==5:
      continue
  print(i)

#exercise
name=input("please input your name:")
password=input("please input your password:")
if name=="wenyujuan":
    if password=="2017":

        print("welcome to my world!")
    else:
        print("There is something wrong with your name or password.")
else:
    print("There is something wrong with your name or password.")


