#-*- coding:utf-8 -*- 

class Dog:

    def __del__(self):
        print('\033[7;32;40m Hero is over...\033[0m')

dog1 = Dog()
dog2 = dog1

del dog1 #不会调用__del__方法，因为这个对象，还有其他的
         #变量指向它，即引用计算不是0
print('\033[1;33;43m===dog1===\033[0m')
del dog2 #此时python解释器会自动调用__del__方法，因为没有变量指向它了
print('\033[0;37;47m+++++++++\033[0m')
