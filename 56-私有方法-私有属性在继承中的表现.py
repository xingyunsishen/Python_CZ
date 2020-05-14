#-*- coding:utf-8 -*-

class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def test1(self):
        print('\033[0;37;42m ----test1-----\033[0m')

    def __test2(self):
        print('\033[1;37;40m -----test2----\033[0m')

    def test3(self):
        self.__test2()
        print(self.__num2)

class B(A):
    def test4(self):
        self.__test2()
        print(self.__num2)

b = B()
b.test1()
#b.__test2() #私有方法不会被继承
print(b.num1)
#print(b.__num2) #私有方法不会被继承
#b.test3() #这里会继承test3,因为test3不是私有方法
b.test4() #如果调用的是继承的父类中的公有方法，则可以在这个公有
          #方法中访问父类中的私有属性和方法；但是，如果在子类中
          #自定义了一个公有方法，这个自定义的公有方法是不可以调
          #用继承父类中的私有方法和属性的


