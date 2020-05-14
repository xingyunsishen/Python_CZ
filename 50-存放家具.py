#-*- coding: utf-8 -*-

#定义一个家类
class Home:

    #初始化对象
    def __init__(self, new_area, new_info, new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area
        self.contain_items = []

    def __str__(self):
        msg = "\033[5;37;40m 房屋总面积:%d,可用面积:%d,户型是:%s,地址是:%s\033[0m"%(self.area, self.left_area, self.info, self.addr)
        msg += '\033[25;37;40m当前房屋里面的物品有%s\033[0m'%(str(self.contain_items))
        return msg 

    def add_item(self, item):
        self.left_area -= item.get_area()
        self.contain_items.append(item.get_name())

#定义一个床类
class Bed():

    #初始化对象
    def __init__(self, new_name, new_area):
        self.name = new_name
        self.area = new_area

    def __str__(self):
        return'\033[7;37;40m %s占用的面积:%d\033[0m'%(self.name, self.area)

    def get_area(self):
        return self.area

    def get_name(self):
        return self.name

#创建房屋对象
fangwu = Home(129, '三室两厅', '北京市朝阳区666街道666号')
print(fangwu)

#创建床对象
bed1 = Bed('天堂梦', 4)
print(bed1)

fangwu.add_item(bed1)
print(fangwu)

bed2 = Bed('上下铺', 2)
fangwu.add_item(bed2)
print(fangwu)


