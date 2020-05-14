#-*- coding:utf-8 -*-

class Store(object):

    def select_car(self):
        pass
    def order(self, car_type):
        return self.select_car(car_type)

class BMWCarStore(Store):
    def select_car(self, car_type):
        return BMWFactory().select_car_by_type(car_type)

class BMWFactory(object):
    def select_car_by_type(self, car_type):
        pass

bmw_store = BMWCarStore()
bmw = bmw_store.order('Z4')

class CarStore(Store):
    def select_car(self, car_type):
        return Factory().select_car_by_type(car_type)

class Factory(object):
    def select_car_by_type(self, car_type):
        if car_type == '朗逸':
            return Lavida()
        elif car_type == '速腾':
            return Sagitar()
        elif car_type == '宝马':
            return Z4()
        else:
            return car_store.order(input('\033[0;30;40m 请输入汽车品牌\033[0m'))

class Car(object):
    def move(self):
        print('\033[0;31;41m车子正在移动...\033[0m')
    def music(self):
        print('\033[0;32;42m正在播放音乐...\033[0m')
    def stop(self):
        print('\033[0;33;43m车子已经停下...\033[0m')

class Lavida(Car):
    pass
class Sagitar(Car):
    pass
class Z4(Car):
    pass

car_store = CarStore()
car = car_store.order(input('\033[0;34;44m请输入汽车品牌:\033[0m'))
car.move()
car.music()
car.stop()

