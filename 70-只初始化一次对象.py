#-*- coding:utf-8 -*-
class Dog(object):
    __instance = None
    __init_flag = False

    def __new__(cls, name):
        if  cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance
    def __init__(self, name):
        if Dog.__init_flag == False:
           self.name = name
           Dog.__init_flag = True

a = Dog('小汪汪')
print(id(a))
print("\033[0;30;40m", a.name ,"\033[0m")
b = Dog('小黄')
print(id(b))
print('\033[1;31;41m', b.name, '\033[0m')
