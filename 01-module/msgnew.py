#-*- coding:utf-8 -*-

__all__ = ["test01", "test02"] #这里的__all__是一个全局变量，如果
                               #‘[]’内只写一个test01，在使用from 
                               #msgnew import *引用的时候，只有
                               #test01可以正常使用，test02不可
                               #以使用；__all__这个变量就是为了
                               #避免使用import *导入时出现不必
                               #要的错误
                               #

def test01():
    print("\033[0;30;40m---test01---\033[0m")

def test02():
    print("\033[0;32;42m---test02---\033[0m")

num = 100 #虽然num也是全局变量，但是，由于__all__的存在，在实际引
          #用时，num会报错，而test01和test02由于在__all__中声明了
          #故可以成功调用
class Test(object):
    pass
