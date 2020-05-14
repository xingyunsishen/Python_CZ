#-*- coding:utf-8 -*-

class CarStore(object):
    def order(self, money):
        if money > 500000:
            return Car()

class Car(object):
    def move(self):
        print('\033[0;30;40m The Car is moving...\033[0m')

    def music(self):
        print('\033[0;31;41m Playing Music...\033[0m')

    def stop(self):
        print('\033[0;32;42m Car Parked...\033[0m')

car_store = CarStore()
car = car_store.order(1000000)
car.move()
car.music()
car.stop()

