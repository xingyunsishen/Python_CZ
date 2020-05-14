#-*- coding:utf-8 -*-
class Dog(object):
    def __init__(self):#init方法只负责初始化
        print('---init方法---')
    def __del__(self):
        print('---del方法---')
    def __str__(self):
        print("---str方法---")
        return "对象描述信息"
    def __new__(cls): #new方法只负责创建
        print(id(cls))
        print('---new方法---')#cls此时是Dog指向的那个类对象
        return  object.__new__(cls)

print(id(Dog))
xiaohuang = Dog()#这一步实际上做了三件事
                 #1.先调用__new__方法来创建对象，然后找一个变量来接收__new__的
                 #返回值，这个返回值表示创建出来的对象的引用
                 #2.__init__(刚刚创建出来的对象的引用)
                 #3.返回对象的引用
                 #总结：__new__方法只负责创建；__init__方法只负责初始化

