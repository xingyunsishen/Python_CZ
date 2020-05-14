#-*- coding:utf-8 -*-
class CarStore(object):
    def order(self, car_type):
        if car_type == "Roewe":
            return Roewe()
        elif car_type == "BMW":
            return BMW()
        elif car_type == "Vovl":
            return Vovl()

class Car(object):
    def move(self):
        print('\033[0;33;43m Car moving...\033[0m')
      
    def music(self):
        print('\033[0;34;44m Playing music...\033[0m')

    def stop(self):
        print('\033[0;35;45m Car parked...\033[0m')

class Roewe(Car):
    pass

class BMW(Car):
    pass

class Vovl(Car):
    pass

car_store = CarStore()
car = car_store.order("Roewe")
car.move()
car.music()
car.stop()


