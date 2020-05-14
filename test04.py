#-*- coding:utf-8 -*-

class CarStore(object):
    def order(self, car_type):
        return select_car_by_type(car_type)

def select_car_by_type(car_type):
    if car_type == 'Lavida':
        return Lavida()
    elif car_type == 'Sagitar':
        return Sagitar()
    elif car_type == '途岳':
        return Tuyue()
    else:
        print('\033[0;33;43m 对不起输入有误，请重新输入...\033[0m')
        return car_store.order(input('\033[0;34;43m请输入汽车品牌:\033[0m')) 

class Car(object):
    def move(self):
        print('\033[0;30;40m车在移动....\033[0m')
    def music(self):
        print('\033[0;31;41m正在播放音乐...\033[0m')
    def stop(self):
        print('\033[0;32;42m车子已经停了...\033[0m')

class Lavida(Car):
    pass

class Sagitar(Car):
    pass

class Tuyue(Car):
    pass

car_store = CarStore()
#car = car_store.order('Lavida')
car = car_store.order(input('请输入汽车品牌:'))
car.move()
car.music()
car.stop()

