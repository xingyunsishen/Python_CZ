#-*- coding:utf-8 -*-

class CarStore(object):
    def __init__(self):
        self.factory = Factory()

    def order(self, car_type):
        return self.factory.select_car_by_type(car_type)

class Factory(object):
    def select_car_by_type(self, car_type):
        if car_type == '朗逸':
            return Lavida()
        elif car_type == '速腾':
            return Sagitar()
        elif car_type == '途岳':
            return Tharu()
        else:
            return car_store.order(input('\033[0;34;44m 请重新输入汽车品牌: \033[0m'))

class Car(object):
    def move(self):
        print('\033[0;30;40m车子在移动...\033[0m')
    def music(self):
        print('\033[0;31;41m在放音乐...\033[0m')
    def stop(self):
        print('\033[0;32;42m车子停下了...\033[0m')

class Lavida(Car):
    pass
class Sagitar(Car):
    pass
class Tharu(Car):
    pass

car_store = CarStore()
car = car_store.order(input('\033[0;33;43m请输入汽车品牌:\033[0m'))
car.move()
car.music()
car.stop()
