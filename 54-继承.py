#-*- coding:utf-8 -*-

class Animal:
    def eat(self):
        print('\033[0;37;42m ========吃=======\033[0m')

    def drink(self):
        print('\033[0;37;43m ========喝=======\033[0m')

    def sleep(self):
        print('\033[0;37;44m =======睡========\033[0m')

    def run(self):
        print('\033[0;37;45m =======跑=======\033[0m')


class Dog(Animal):
    def bark(self):
        print('\033[0;37;46m *******汪汪*******\033[0m')

class Cat(Animal):
    def catch(self):
        print('\033[0;37;47m ++++++抓小老鼠+++++++\033[0m')

class XiaoNiao(Dog):
    def fly(self):
        print('\033[1;37;42m ~~~~~~~小鸟飞~~~~~~~\033[0m')
#wangcai只能使用Dog或者Animal中的方法，不可以使用Cat或者XiaoNiao中的方法；bird和tom同理
wangcai = Dog()
wangcai.eat()
wangcai.run()
print('--'*10,'wangcai over', '--'*10)
bird = XiaoNiao()
bird.fly()
bird.bark()
bird.eat()
print('-------bird over-------')
tom = Cat()
tom.eat()
print('-------tom over--------')
