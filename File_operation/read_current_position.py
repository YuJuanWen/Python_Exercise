#获取当前位置
f=open('test.txt','r')
str=f.read(3)

print('读取的数据是：',str)

position=f.tell()
print('current positon is :', position)

str=f.read(3)
print("the reading data is ",str)

position=f.tell()
print("current position is :", position)

#定位到某个位置
f=open('test.txt','r')
str=f.read(30)
print("current data is :",str)

#find current position
position=f.tell()
print("the current position is :",position)

#reset the position
f.seek(6,0)

#find current position
position=f.tell()
print("current position is :",position)

'''
f.seek(-3, 2)
str=f.read()
print("the current data is :",str)

'''



f.close()

