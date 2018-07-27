class Car:
    def getCarInfo(self):
        print('the number of car wheel: %d, color%s'%(self.wheelNum, self.color))

    def move(self):
        print('the car is moving......')

#create the object

BMw= Car()
BMw.color='black'
BMw.wheelNum=4
BMw.move()
print(BMw.color)
print(BMw.wheelNum)


#_init_()  method
# 定义汽车类
class Car:

    def __init__(self):
        self.wheelNum = 4
        self.color = '蓝色'

    def move(self):
        print('车在跑，目标:夏威夷')

# 创建对象
BMW = Car()

print('车的颜色为:%s'%BMW.color)
print('车轮胎数量为:%d'%BMW.wheelNum)

print(BMw) #show the cache address of BMw

#-------魔方方法
"""
class Car:

    def __init__(self, newWheelNum, newColor):
        self.wheelNum = newWheelNum
        self.color = newColor

    def __str__(self):
        msg = "嘿。。。我的颜色是" + self.color + "我有" + int(self.wheelNum) + "个轮胎..."
       
        return msg

    def move(self):
        print('车在跑，目标:夏威夷')


BMW = Car(4, "白色")
print(BMW)
"""