class People(object):
    country = 'china'

    #类方法，用classmethod来进行修饰
    @classmethod
    def getCountry(cls):
        return cls.country
    #类方法还有一个用途就是可以对类属性进行修改：
    @classmethod
    def setCountry(cls,country):
        cls.country = country

p = People()
print(p.getCountry())   #可以用过实例对象引用
print(People.getCountry())   #可以通过类对象引用

p.setCountry('japan')

print(p.getCountry())
print(People.getCountry())


#-------------------static method---------------

class People(object):
    country = 'china'

    @staticmethod
    #静态方法
    #需要通过修饰器@staticmethod来进行修饰，静态方法不需要多定义参数
    def getCountry():
        return People.country


print (People.getCountry())

"""
从类方法和实例方法以及静态方法的定义形式就可以看出来，类方法的第一个参数是类对象cls，
那么通过cls引用的必定是类对象的属性和方法；而实例方法的第一个参数是实例对象self，
那么通过self引用的可能是类属性、也有可能是实例属性（这个需要具体分析），
不过在存在相同名称的类属性和实例属性的情况下，实例属性优先级更高。
静态方法中不需要额外定义参数，因此在静态方法中引用类属性的话，
必须通过类对象来引用
"""