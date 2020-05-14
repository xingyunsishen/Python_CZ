#-*- coding:utf-8 -*-
class Car(object):

    #定义车的方法
    def move(self):
        print('---车在奔跑---')

    def stop(self):
        print('---停车---'):

# 定义一个销售车的店类
class CarStore(object):
    def order(self):
        self.car = Car()
        self.car.move()
        self.car.stop()

