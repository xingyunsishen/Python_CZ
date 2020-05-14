#-*- coding:utf-8 -*-

class CarStore(object):
    def order(self, car_type):
        if car_type == "桑塔纳":
            return SangTana()
        elif  car_type == "BMW":
            return BMW()

class Car(object):
    def move(self):
        print('\033[0;32;43m Car  moving...\033[0m')
    def music(self):
        print('\033[0;33;44m Playing music...\033[0m')
    def stop(self):
        print('\033[0;34;45m Car parked...\033[0m')

class SangTana(Car):
    pass

class BMW(Car):
    pass

car_store = CarStore()
car = car_store.order("桑塔纳")
car.move()
car.music()
car.stop()
