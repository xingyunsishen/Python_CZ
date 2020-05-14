#-*- coding:utf-8 -*-
'''
1.局部变量只在当前函数生效，出去当前函数不生效；
2.全局变量在所有函数中均可以直接引用
3.全局变量虽可以在函数外部定义，但是一定要在调用函数开始执行前
如以下程序：a,b均可以正常输出，c会报为定义
a = 11
def test():
    print('a=%d'%a)
    print('b=%d'%b)
    print('c=%d'%c)
b = 22
test()
c = 33
4.全局变量的优先级要小于局部变量的优先级
a = 100
def test01():
    a = 200
    print('a=%d' %a)

def test02():
    print('a=%d' %a)

test01()
test02()
以上输出结果为test01中输出200，test02输出100 
'''
#局部变量
def test1():
    a = 100
    return a
def test2():
    #print('a=%d'%a)#因为a只在test1函数中定义了，这里如果直接调用会报错，因为在
                   #test2中没有定义
    #1.可以先调用test1函数
    a = test1() #test1函数还需要加return返回值
    print("a=%d" %a)

#全局变量
b = 22

def test3():
    c = b ** 2
    print('test2中c=%d,b=%d' %(c, b))
    return c

def test4():
    c = test3()
    result = b + c
    print('b= %d,c=%d' %(b, c))
    print("%d + %d = %d" %(b, c, result))

def get_temperature():
    temperature = float(input("Please input temperature:"))
    return temperature
def print_temperature():
    result = get_temperature()
    print("Current temperature is %3.2f" % result)

#使用global声明来修改全局变量的值
g = 0

def test5():
    global x 
    x = 10

def test6():
    print("g的当前值：%d" %x)

#列表、字典作为全局变量
list01 = [11, 22, 33]
dict01 = {'name':'xiaomi'}

def test7():
    list01.append(44)
    dict01['age'] = 18

def test8():
    print(list01, dict01)
#test1()
#test2()
#test3()
#test4()
#print_temperature()
#test5()
#test6()
test7()
test8()
