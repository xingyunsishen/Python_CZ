#-*- coding:utf-8 -*-

class Dog(object):
    def __init__(self):
        print('\033[0;30;40m ------init方法------\033[0m')

    def __del__(self):
        print('\033[0;31;41m ------del方法-------\033[0m')

    def __str__(self):
        print('\033[0;32;42m ------str方法-------\033[0m')
        return "\033[0;33;43m 对象描述信息\033[0m"

    def __new__(cls): #cls此时指Dog指向的那个类对象
        print('\033[0;34;44m ------new方法------\033[0m')
        return object.__new__(cls)

xiaotianquan = Dog()

