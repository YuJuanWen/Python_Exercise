class Animal:
    def __init__(self, name):
        self.name=name

    def printName(self):
        print('the name is: %s'%self.name)

def myPrint(animal):
    animal.printName()

dog1=Animal("cathy")
myPrint(dog1)
dog2=Animal('Bob')
myPrint(dog2)

#----------------------烤地瓜
class SweetPotato:
    def __init__(self):
        self.cookedLevel =0
        self.cookedString="row"
        self.condiment=[]
    def __str__(self):
        msg=self.cookedString+'sweet Potato'
        if len(self.condiment)>0:
            msg =msg+"("
            for temp in self.condiment:
                msg=msg+temp +","
            msg =msg+")"
        return msg
    def cook(self, time):
        self.cookedLevel +=time
        if self.cookedLevel>8:
            self.cookedString='it was baked to be coal'
        elif self.cookedLevel >5:
            self.cookedString="yes, it was baked well."
        elif self.cookedLevel>3:
           self.cookedString ="en, it was in a dilemma, halfcooked"
        else:
            self.cookedString="it was totally raw."

    def addCondiment(self,condiments):
        self.condiment.append(condiments)

"""
mySweetPotato=SweetPotato()
print(mySweetPotato.cookedLevel)
print(mySweetPotato.cookedString)
print(mySweetPotato.condiment)

print("-----then we start to bake our sweetpotato----------")
mySweetPotato.cook(7)
print(mySweetPotato.cookedString)
print(mySweetPotato.cookedLevel)
"""
# 用来进行测试
mySweetPotato = SweetPotato()
print("------有了一个地瓜，还没有烤-----")
print(mySweetPotato.cookedLevel)
print(mySweetPotato.cookedString)
print(mySweetPotato.condiment)
print("------接下来要进行烤地瓜了-----")
print("------地瓜经烤了4分钟-----")
mySweetPotato.cook(4) #烤4分钟
print(mySweetPotato)
print("------地瓜又经烤了3分钟-----")
mySweetPotato.cook(3) #又烤了3分钟
print(mySweetPotato)
print("------接下来要添加配料-番茄酱------")
mySweetPotato.addCondiment("番茄酱")
print(mySweetPotato)
print("------地瓜又经烤了5分钟-----")
mySweetPotato.cook(5) #又烤了5分钟
print(mySweetPotato)
print("------接下来要添加配料-芥末酱------")
mySweetPotato.addCondiment("芥末酱")
print(mySweetPotato)