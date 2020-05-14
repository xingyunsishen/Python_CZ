#-*- coding:utf-8 -*-

class Animal:
    def eat(self):
        print('\033[2;37;40m ----吃---\033[0m')
    def drink(self):
        print('\033[3;37;41m ====喝===\033[0m')
    def sleep(self):
        print('\033[4;37;42m +++睡+++\033[0m')
    def run(self):
        print('\033[5;37;43m ---跑---\033[0m')

class Dog(Animal):
    def bark(self):
        print('\033[5;37;44m ····汪汪···\033[0m')
        print('----Dog----')

class Yilong(Dog):
    def fly(self):
        print('\033[6;37;45m ~~~飞~~~\033[0m')
        print('---fly---')
    def bark(self): #重写父类方法
        print('\033[7;37;46m ###怒吼###\033[0m')
        print('---fly---')
        #调用被重写之前的父类方法
        #第一种
       # Dog.bark(self)
        #第二种
        super().bark()

class test01(Dog):
    def catch(self):
        print('\033[0;30;40m ----test01-----\033[0m')
    def bark(self):
        print('\033[1;31;41m -----撕咬-----\033[0m')
       # super().bark()
       # Dog.bark(self)

bird = Yilong()
bird.fly()
bird.bark()
bird.eat()
print('='*30)
t = test01()
t.catch()
t.bark()
