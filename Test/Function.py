def printInfor():
    print("-------------------------")
    print("   人生苦短，我用python    ")
    print("-------------------------")

printInfor()

def printoneline():
    print("-"*30)

#--------------------------------

def printNumline(num):
    i=0
    while i<num:
        printoneline()
        i+=1

#---------------------------------

def meannum(n1,n2,n3):
    c=(n1+n2+n3)/3
    print(c)

printNumline(6)
meannum(1,2,3)

#——-——————————————————————

def printinfo( name, age = 35 ):
   # 打印任何传入的字符串
   print ("Name: ", name)
   print ("Age ", age)

# 调用printinfo函数
printinfo(name="miki" )
printinfo( age=9,name="miki" )