#-*- coding:utf-8 -*-
#类方法
#是类对象所拥有的方法，需要用@classmethod来标示其为类方法，对于类方法，第
#一个参数必须是类对象，一般以cls作为第一个参数（当然可以用其他名称的变量
#作为其第一个参数，但是大部分人都习惯以cls作为第一个参数的名字，就最好用
#cls了），能够通过实例对象和类对象去访问
class Person(object):
    province = 'HeBei'

    #类方法用@classmethod来进行修饰
    @classmethod
    def getProvince(cls):
        return cls.province

p = Person()
print(p.getProvince()) #可以通过实例对象引用
print(p.getProvince()) #可以通过类对象引用

#类方法的另一个用途就是对类属性进行修改：
class Person(object):
    province = 'HeBei'

    @classmethod
    def getProvince(cls):
        return cls.province

    @classmethod
    def setProvince(cls, province):
        cls.province = province

p = Person()
print(p.getProvince()) #可以用实例对象引用
print(Person.getProvince()) #可以通过类对象引用

p.setProvince('HeNan')
print(p.getProvince())
print(Person.getProvince())

#静态方法
#需要通过修饰器@classmathod来进行修饰，静态方法不需要多定义参数
class Test(object):
    province = 'henan'
    @staticmethod
    #静态方法
    def getProvince():
        return Person.province

print(Person.getProvince())

#从类方法和实例方法以及静态方法的定义形式就可以看出来，类方法的第一个参数
#是类对象cls,那么通过cls引用的必定是类对象的属性和方法；而实例方法的第一个
#参数是实例对象self,那么通过self引用的可能是类属性、也有可能是实例属性（
#这个需要具体分析），不过存在相同名称的类属性和实例属性的情况下，实例属性
#优先级更高。静态方法中不需要额外定义参数，因此在静态方法中引用类属性的话
#，必须通过类对象来引用

