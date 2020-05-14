#-*- coding:utf-8 -*-

'''
可变类型:
列表
字典
'''
'''
不可变类型:
数字
字符串
元组
'''
infor = {'name':'xiaomi', 100:'haha', 3.15:'heihei'}
#print(infor)
#infor = {(11,22):'aa', [33,44]:'bb'} #这里会报错TypeError: unhashab
                                      #le type: 'list'，说明列表不可
                                      #以作为key,即可变类型不可以作
                                      #为key
#print(infor)
################################################################
'''
a = 100

def test(num):
    num += num
    print('num=%d'%num)

test(a)
print('a=%d'%a)

a = [100]

def test01(num):
    num += num
    print(num)

test01(a)
print(a)
#这两个函数说明，在函数内如果对形参修改时，需要注意传入的实参是修改了
#全局变量，还是重新定义了局部变量
'''
'''
#交换变量的值
a = 11
b = 22
c = 0

#交换方式1
c = 0
c = a
a = b 
b = c

#交换方式2
a = a + b 
b = a - b 
a = a - b

#交换方式3
a, b = b, a

#交换方式4
#??
'''
a = [100]

def test02(num):
    num = num + num #注意观察结果，可能跟想的不一样
    print(num)

test02(a)

print(a)
