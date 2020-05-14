#-*- coding:utf-8 -*-

#定义一个cat类
class Cat():

    #初始化对象
    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age = new_age
    
    def __str__(self):
        return '\033[4;37;40m%s的年龄是%d\033[0m'%(self.name, self.age)

    #方法
    def eat(self):
        print('\033[0;37;40m 猫在吃鱼...\033[0m')

    def drink(self):
        print('\033[1;37;40m 猫在和茅台...\033[0m')

    def introduce(self):
        print('\033[22;37;40m %s的年龄是%d'%(self.name, self.age))

#创建一个对象
tom = Cat('Thoms', 24)
#tom.eat()
#tom.drink()
#tom.introduce()

#创建第二个对象
lanmao = Cat('蓝猫', 20)
#lanmao.introduce()

#使用str方法后，可以不需要再单独调用对象方法,可以直接输出对象的结果
print(tom)
print(lanmao)
