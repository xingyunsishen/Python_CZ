#-*- coding:utf-8 -*-
class Dog(object):
    __instance = None

    def __new__(cls, name):
        if  cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
    def __init__(self, name):
           self.name = name

a = Dog('小汪汪')
print(id(a))
print('\033[2;32;42m',a.name,'\033[0m')
b = Dog('小黄')
print(id(b))
print('\033[3;33;43m', b.name, '\033[0m')
