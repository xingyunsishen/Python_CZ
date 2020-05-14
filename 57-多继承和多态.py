# -*- coding:utf-8 -*-
#object类python解释器中默认的类，是所有类中最顶层的基类
#只要定义类，无论调用、继承，写与不写object，最终都会
#调用object
'''
class A: # 经典类
    pass
class B(object): #新式类，python3中默认的，也是推荐的
    pass
'''
class Base(object):
    def test(self):
        print('\033[0;37;42m----Base----\033[0m')

class A(Base):
    def test1(self):
        print('\033[0;37;43m ---test1---\033[0m')

class B(Base):
    def test2(self):
        print('\033[0;37;44m ---test2---\033[0m')

class C(A,B):
    pass

print('-------多继承--------')
c = C()
c.test1()
c.test2()
c.test()
#
#
##多继承的注意点
class Base(object):
    def test(self):
        print('\033[0;37;45m -----Base----\033[0m')

class A(Base):
    def test(self):
        print('\033[0;37;46m ----A-----\033[0m')

class B(Base):
    def test(self):
        print('\033[0;37;47m ----B-----\033[0m')

class C(A,B):
    #pass
    def test(self):
        print('\033[1;37;42m ---C-----\033[0m')
print('--------多继承--------')
c = C()
c.test()
print(C.__mro__)
#C.__mro__会打印出调用方法的顺序

#多态
class Dog(object):
    def print_self(self):
        print('\033[0;37;42m 我是XXX,请多关照....\033[0m')

class XiaoNiao(Dog):
    def print_self(self):
        print('\033[0;37;43m 大家好,我是小小白....\033[0m')

def introduce(temp):
    temp.print_self()

print('-------多态------')
dog1 = Dog()
dog2 = XiaoNiao()
introduce(dog1)
introduce(dog2)

