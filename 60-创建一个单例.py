#-*- coding:utf-8 -*-

class Dog(object):

    __instance = None

    def __new__(cls):
        if cls.__instance == None:
            cls.__instance == object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance #返回上一次创建的对象的引用

a = Dog()
print(id(a))
b = Dog()
print(id(b))

