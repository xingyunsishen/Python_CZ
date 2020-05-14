#-*- coding:utf-8 -*-
"""
class CarStore(object):
    def order(self, money):
        if car_type == "BMW":
            return BMW()
        elif car_type == "VW":
            return VW()
        elif car_type == 'TOYOTA':
            return TOYOTA()
        elif car_type == 'HONDA':
            return HONDA()

class Car(object):
    def move(self):
        print("\033[0;31;40m车在移动...\033[0m")
    def music(self):
        print('\033[0;32;41m车在播放音乐...\033[0m')
    def stop(slef):
        print('\033[0;33;42m车已经停下啦...\033[0m')
class BMW(Car):
    pass
class VW(Car):
    pass
class BYD(Car):
    pass
class TOYOTA(Car):
    pass
class HONDA(Car):
    pass

car_store = CarStore()
car = car_store.car_type(input('\033[0;30;40mplease input VW\033[0m'))
car.move()
car.music()
car.stop()
"""
#上述程序后续添加新车比较麻烦，可以改为如下形式
class CarStore(object):
    def __init__(self):
        self.factory = Factory()
    def order(self, car_type):
        return self.factory.select_car_type(car_type)
class Factory(object):
    def select_car_type(car_type):
        if car_type == "BMW":
            return BMW()
        elif car_type == "VW":
            return VW()
        elif car_type == 'TOYOTA':
            return TOYOTA()
        elif car_type == 'HONDA':
            return HONDA()

class Car(object):
    def move(self):
        print("\033[0;31;40m车在移动...\033[0m")
    def music(self):
        print('\033[0;32;41m车在播放音乐...\033[0m')
    def stop(slef):
        print('\033[0;33;42m车已经停下啦...\033[0m')
class BMW(Car):
    pass
class VW(Car):
    pass
class BYD(Car):
    pass
class TOYOTA(Car):
    pass
class HONDA(Car):
    pass

car_store = CarStore()
car = car_store.order(input('\033[0;30;40mplease input VW\033[0m'))
car.move()
car.music()
car.stop()
