try:
    print('-----test--1---')
    open('123.txt','r')
    print('-----test--2---')
except IOError:
    pass

#------except捕获多个异常
"""


    下面的程序，已经使用except来捕获异常了，为什么还会看到错误的信息提示？

答:

    except捕获的错误类型是IOError，而此时程序产生的异常为 NameError ，所以except没有生效


try:
    print num
except IOError:
    print('产生错误了')
"""
try:
    print('-----test--1---')
    open('123.txt','r') # 如果123.txt文件不存在，那么会产生 IOError 异常
    print('-----test--2---')
    print(num)# 如果num变量没有定义，那么会产生 NameError 异常

except (IOError,NameError):
    #如果想通过一次except捕获到多个异常可以用一个元组的方式
    errorMsg="some thing wrong. "
    # errorMsg里会保存捕获到的错误信息
    print(errorMsg)

#-----------------------
"""
try ... finally...
在程序中，如果一个段代码必须要执行，即无论异常是否产生都要执行，那么此时就需要使用finally。
 比如文件关闭，释放锁，把数据库连接返还给连接池等
"""
import time
try:
    f = open('test.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    except:
        #如果在读取文件的过程中，产生了异常，那么就会捕获到
        #比如 按下了 ctrl+c
        pass
    finally:
        f.close()
        print('关闭文件')
except:
    print("没有这个文件")

#---------------------------------
#else
try:
    num = 100
    print (num)
except NameError as errorMsg:
    print('产生错误了:%s'%errorMsg)
else:
    print('没有捕获到异常，真高兴')

#-------------------异常的传递-----------try嵌套中
import time
try:
    f = open('test.txt')
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print('关闭文件')
except:
    print("没有这个文件")

#-----------------函数嵌套调用中
    def test1():
        print("----test1-1----")
        print(num)
        print("----test1-2----")


    def test2():
        print("----test2-1----")
        test1()
        print("----test2-2----")


    def test3():
        try:
            print("----test3-1----")
            test1()
            print("----test3-2----")
        except Exception as result:
            print("捕获到了异常，信息是:%s" % result)

        print("----test3-2----")


    test3()
    print("------华丽的分割线-----")
    test2()
#--------------抛出自定义的异常
class ShortInputException(Exception):
    '''自定义的异常类'''
    def __init__(self, length, atleast):
        #super().__init__()
        self.length = length
        self.atleast = atleast

def main():
    try:
        s = input('请输入 --> ')
        if len(s) < 3:
            # raise引发一个你定义的异常
            raise ShortInputException(len(s), 3)
    except ShortInputException as result:#x这个变量被绑定到了错误的实例
        print('ShortInputException: 输入的长度是 %d,长度至少应是 %d'% (result.length, result.atleast))
    else:
        print('没有异常发生.')

main()

#--------------------------------------异常处理中抛出异常  可以看到出错
class Test(object):
    def __init__(self, switch):
        self.switch = switch #开关
    def calc(self, a, b):
        try:
            return a/b
        except Exception as result:
            if self.switch:
                print("捕获开启，已经捕获到了异常，信息如下:")
                print(result)
            else:
                #重新抛出这个异常，此时就不会被这个异常处理给捕获到，从而触发默认的异常处理
                raise


a = Test(True)
a.calc(11,0)

print("----------------------华丽的分割线----------------")

a.switch = False
a.calc(11,0)