"""
单例模式
确保某一个类只有一个实例，而且自行实例化并向整个系统提供这个实例，
这个类称为单例类，单例模式是一种对象创建型模式。

"""
# 实例化一个单例
class Singleton(object):
    __instance = None
    __first_init = False

    def __new__(cls, age, name):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, age, name):
        if not self.__first_init:
            self.age = age
            self.name = name
            Singleton.__first_init = True


a = Singleton(18, "dongGe")
b = Singleton(8, "dongGe") #这里的8没有起作用，因为__init__只能其一次作用

print(id(a))
print(id(b))


print(a.age)
print(b.age)

a.age = 19
print(b.age)  #这里出现的是19，原来明明是18的
