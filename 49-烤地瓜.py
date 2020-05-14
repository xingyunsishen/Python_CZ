#-*- coding:utf-8 -*-

#定义一个地瓜类
class SweetPotato:
    
    #初始化对象
    def __init__(self):
        self.cookedString = "生的"
        self.cookedLevel = 0
        self.condiments = [] #为了能够存储多个数据

    def __str__(self):
        return '\033[24;37;40m 地瓜 状态:%s(%d),添加的佐料有:%s\033[0m'%(self.cookedString, self.cookedLevel, str(self.condiments))

    def cook(self, cooked_time):
        #因为这个方法被调用了多次，为了能够再一次调用这个方法的时候，能够到上
        #一次调用这个方法时的cooked_time,所以，需要在此把cooked_time保存到这个
        #对象的属性中，因为属性不会随着方法的调用而结束（一个方法被调用的时候
        #是可以用局部变量来保存数据的，但是当这个方法定义结束之后，这个方法中的
        #所有数据就没有了）
        self.cookedLevel += cooked_time

        if self.cookedLevel >= 0 and self.cookedLevel < 3:
            self.cookedString = '生的'
        elif self.cookedLevel >= 3 and self.cookedLevel < 5:
            self.cookedString = '半熟'
        elif self.cookedLevel >= 5 and self.cookedLevel < 8:
            self.cookedString = '基本烤熟'
        elif self.cookedLevel >= 8 and self.cookedLevel < 10:
            self.cookedString = '完全熟透'
        else:
            self.cookedString = '焦糊了..'

    def addCondiments(self, item):
        #因为item这个变量指向了一个佐料，所以接下来需要将item放到append里面
        self.condiments.append(item)

#创建一个对象
di_gua = SweetPotato()

##开始烤制
i = 1
while i < 10:
    di_gua.cook(1)
  #  print(di_gua)
    j = 10
    while j >= 10:
        di_gua.addCondiments('大蒜')
        di_gua.addCondiments('蕃茄酱')
        di_gua.addCondiments('孜然')
        j -= 1 
    i += 1
print(di_gua)
#di_gua.cook(1)
#print(di_gua)
#
#di_gua.cook(1)
#print(di_gua)
#di_gua.addCondiments('大蒜')
#print(di_gua)
#
#di_gua.cook(1)
#di_gua.addCondiments('番茄酱')
#print(di_gua)
#
#di_gua.cook(1)
#di_gua.addCondiments('孜然')
#print(di_gua)
#
#di_gua.cook(1)
#print(di_gua)
#
#di_gua.cook(1)
#print(di_gua)
#
#di_gua.cook(1)
#print(di_gua)
#
#di_gua.cook(1)
#print(di_gua)
#
#di_gua.cook(2)
#print(di_gua)
#
#di_gua.cook(3)
#print(di_gua)
