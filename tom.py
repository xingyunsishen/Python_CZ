#-*- coding:utf-8 -*-

class Cat(object):
    
    def __init__(self, new_name, new_age):
        print('\033[0;31;42m ======哈哈哈=======\033[0m')
        self.name = new_name
        self.age = new_age

    def __str__(self):
        return '\033[0;33;43m %s 的年龄:%d\033[0m'%(self.name, self.age)
    def eat(self):
        print('\033[0;38;47m name: %s eating...\033[0m' % (self.name))

    def drink(self):
        print('\033[0;32;43m name:%s drinking...\033[0m'%(self.name))

    def introduce(self):
        print('\033[0;33;43m 年龄:%d 名字:%s\033[0m'% (self.age, self.name))

tom = Cat('汤姆', 20)
#tom.age = 19
#tom.name = 'tangmu'
##tom.eat()
##tom.drink()
##tom.introduce()
print(tom)
lanmao = Cat('蓝猫', 22)
#lanmao.name = "蓝猫"
#lanmao.age = 20
##lanmao.eat()
##lanmao.drink()
##lanmao.introduce()
print(lanmao)
