#-*- coding: utf-8 -*-

#定义一个Car类
class Car:
    #方法
    def getCarInfo(self):
        print('车轮个数:%d,车身颜色:%s' %(self.wheelNum, self.color))

    def move(self):
        print('车正在移动...')

    def toot(self):
        print('车在打鸣...')

#创建一个对象
BMW = Car()
BMW.color = 'black'
BMW.wheelNum = 4
BMW.move()
BMW.toot()
print(BMW.color)
print(BMW.wheelNum)
print(BMW.move)
print(BMW.toot)

#__init__方法

#定义汽车类
class Car:
    def __init__(self):
        self.wheelNum = 4
        self.color = 'blue'

    def move(self):
        print('车子在飞跑...')

#创建对象
BMW = Car()
print('车身颜色:%s'%BMW.color)
print('车轮数量:%d'%BMW.wheelNum)

#带参数的__init__方法
#定义汽车类
class Car:

    def __init__(self, newWheelNum, newColor):
        self.wheelNum = newWheelNum
        self.color = newColor
# 创建对象
BMW = Car(4, 'red')

print('车身颜色:%s,车轮数量:%d'%(BMW.color, BMW.wheelNum))

#__str__方法
#定义一个汽车类
class Car:
    
    def __init__(self, newWheelNum, newColor):
        self.wheelNum = newWheelNum
        self.color = newColor

    def __str__(self):
        msg = 'Hi...，本车衣颜色是：'+ self.color + '最新款的' + int(self.wheelNum + '只鞋子')
        return msg
    def move(self):
        print('车在飞奔...')

BMW = Car(4, 'Iron gray4')
print(BMW)
    
