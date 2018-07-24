#编程实现9*9乘法表
n=1
while n<10:
    m=1
    while m<=9:
        print(n,"*",m,"=",n*m)
        m+=1

    print("--------------------------------------")
    n+=1


#用函数实现求100-200里面所有的素数
num=[];
i=2
for i in range(2,100):
    j=2
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        num.append(i)
print(num)



#请用函数实现一个判断用户输入的年份是否是闰年的程序
def  leapyear(n):
    "判度是否为闰年"
    if n%4==0:
        if n%100==0:
            if(n%400==0):
                print("yes, it is  a leap year.")
            else:
                print("no, it is not a leap year.")
        else:
            print("yes ,it is a leap year.")
    else:
        print("no, it is not a leap year.")

y=int(input("please input your year number:"))
leapyear(y)