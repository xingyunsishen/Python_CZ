#-*- coding:utf-8 -*-
class Cat:
    #属性：
    
    #方法
    def eat(self):
        print('\033[1;35m猫在吃鱼....\033[0m')

    def drink(self):
        print("\033[1;32;43m猫在喝茅台...\033[0m")

    def introduce(self):
        print('%s的年龄是:%d'%(self.name, self.age))

#创建一个对象
tom = Cat()
#调用对象方法
#tom.eat()
#tom.drink()
#添加属性
tom.name = 'Thoms'
tom.age = 40
#获取属性的方式
#第一种
#print('%s的年龄是：%d'%(tom.name, tom.age))
#第二种
tom.introduce()

#创建第二个对象
lanmao = Cat()
lanmao.name = '蓝猫'
lanmao.age = 19
lanmao.introduce()


