#-*- coding:utf-8 -*-
#类属性
class Test(object):
    a = 100 #公有类属性
    __b = 200 #私有类属性

t = Test()
a = t.a
print('a=%d'%a)
print(Test.a)
#以下调用方法是错误的
#print(t.__b)
#print(Test.__b)
#实例属性
class Test(object):
    a = 'this is A' #类属性
    def __init__(self):
        self.leng = 10 #实例属性
        self.space = 2 #实例属性

t = Test()
t.leng = 4
print(t.a)
print(t.leng)
print(t.space)
print(Test.a) #正确
#print(Test.leng) #错误
#print(Test.space) #错误
'''
实例属性：和具体的某个实例对象有关系，并且一个实例对象和另外
一个实例对象是不共享属性的
类属性：所属类对象，且多个实例对象之间共享一个类属性
'''
#通过实例（对象）修改类属性
class Test(object):
    province = '河北省'

print(Test.province)
p = Test()
p.province = '河南省'
print(p.province) #实例属性会覆盖掉同名的类属性
print(Test.province)
del p.province  #删除实例属性
print(p.province) #会输出类原来属性
'''
如果需要在类外修改类属性，必须通过类对象去引用然后进行修改。如果通过实例对
象去引用，会产生一个同名的实例属性，这种方式修改的是实例属性，不会影响到类
属性，并且止呕如果通过实例对象去引用该名称的属性，实例属性会强制屏蔽掉类属
性，即引用的是实例属性，除非删除了该实例属性
'''

# 实例属性
class Tool(object):
    def __init__(self, new_name):
        self.name = new_name 

num = 0
tool1 = Tool('铁锹')
num += 1
print(num)
tool2 = Tool('工兵铲')
num += 1
print(num)
tool3 = Tool('水桶')
num += 1
print(num)

class Tool(object):

    #类属性
    num = 0

    #方法
    def __init__(self, new_name):
        #类属性
        self.name = new_name
        #对类属性+=1
        Tool.num += 1

tool1 = Tool('铁锹')
tool2 = Tool('工兵铲')
tool3 = Tool('水桶')

print(Tool.num)

class Game(object):

    #类属性
    num = 0

    #实例方法
    def __init__(self):
        #实例属性
        self.name = 'laowang'

    #类方法
    @classmethod
    def add_num(cls):
        cls.num = 100
    #静态方法
    @staticmethod
    def print_menu():
        print('\033[0;37;42m -------------------------\033[0m')
        print('\033[0;37;41m 穿越火线 v10.0.0\033[0m')
        print('\033[0;37;41m 1.开始游戏\033[0m')
        print('\033[0;37;41m 2.结束游戏\033[0m')
        print('\033[0;37,42m -------------------------\033[0m')

game = Game()
Game.add_num() #可以通过类的名字调用类方法
print(Game.num)
game.add_num() #还可以通过这个类创建出来的对象去调用这个类方法
print(Game.num)
Game.print_menu() #通过类 去调用静态方法
game.print_menu()   # 通过实例对象 去调用静态方法
'''
类方法特点：必须要有参数
静态方法特点：静态方法可以没有任何参数
类方法特点：必须要有参数
实例方法特点：第一个参数必须写上self写上

'''
