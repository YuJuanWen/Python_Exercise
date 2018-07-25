f=open('test.txt','w')
f.write('welcome to the world of blockchain!')
f.close()

#read the data from file
#如果使用读了多次，那么后面读取的数据是从上次读完后的位置开始的
f=open('test.txt','r')
content=f.read(5)

print("-"*30)

content = f.read()

print(content)

f.close()

#就像read没有参数时一样，readlines可以按照行的方式把整个文件中的内容进行一次性读取，
# 并且返回的是一个列表，其中每一行的数据为一个元素

f = open('test.txt', 'r')

content = f.readlines()

print(type(content))

i=1
for temp in content:
    print("%d:%s"%(i, temp))
    i+=1

f.close()

f=open('test.txt','r')
content=f.readline()
print('1:%s'%content)

content=f.readline()
print('2:%s'%content)

f.close()