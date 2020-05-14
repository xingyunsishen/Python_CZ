#-*- coding:utf-8 -*-
class F1(object):
    def show(self):
        print(F1.show)

class S1(F1):
    def show(self):
        print(S1.show)

class S2(F1):
    def show(self):
        print(S2.show)

def func(obj):
    print(obj.show())

s1_obj = S1()
func(s1_obj)

s2_obj = S2()
func(s2_obj)
