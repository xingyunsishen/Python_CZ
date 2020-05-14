#-*- coding:utf-8 -*-
'''隐藏对象的属性'''
"""
#定义一个类
class Dog:

    def set_age(self, new_age):
        if new_age > 0 and new_age <= 100:
            self.age = new_age
        else:
            self.age = 0

    def get_age(self):
        return self.age

dog = Dog()

dog.set_age(-10)
age = dog.get_age()
print(age)

dog.age = -10
print(dog.age)
"""
#私有属性
class Dog:

    def __init__(self, new_name):
        self.name = new_name
        self.__age = 0 #定义了一个私有的属性，属性的名字是__age

    def set_age(self, new_age):
        if new_age > 0 and new_age <= 100:
            self.__age = new_age
        else:
            self.__age = 0

    def get_age(self):
        return self.__age

dog = Dog('小黄')

dog.set_age(10)
age = dog.get_age()
print(age)

#print(dog.__age)
