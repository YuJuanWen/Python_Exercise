class People(object):

    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, newName):
        if len(newName) >= 5:
            self.__name = newName
        else:
            print("error:名字长度需要大于或者等于5")

xiaoming = People("dongGe")

xiaoming.setName("wanger")
print(xiaoming.getName())

xiaoming.setName("lisi")
print(xiaoming.getName())


