#-*- coding:utf-8 -*-

def test1():
    print("==========", end="")
    print('test1()', end='')
    print('=========')

def test2():
    print('=========', end='')
    print('test2()', end='')
    print('========')
    test3()

def test3():
    print('=='*5, end='')
    print('test3()', end='')
    print('=='*5)
    test1()

test1()
test2()
test3()
#函数嵌套调用的应用
def print_line():
    print('-'*50)

def print_5_line():
    i = 0
    while i < 5:
        print_line()
        i += 1

#print_line()
#print_5_line()


#函数实现3个数的和
def sum_3_nums(a, b, c): #形参
    res = a + b + c
    print('%d+%d+%d=%d' %(a, b, c, res))
    return res

#函数实现找出三个数字中的最大值和最小值
def max_min_nums(x, y, z):
    if x > y:
        if x > z:
            print('max value is %d' %x)
        else:
            print('max value is %d' %z)
    elif x > z:
        if x > y:
            print('max value is %d' %x)
        else:
            print('max value is %d' %y)
    else: 
        if y > z:
            print('max value is %d' %y)
        else:
            print('max value is %d' %z)

#函数实现三个数的平均值
def average_3_nums(x, y, z): #形参
   # average = (x + y + z) / 3
    #调用求和函数
    res = sum_3_nums(x, y, z) #实参
    average = res / 3
    print('average is %d' % average)
    return average

#函数实现三个数的均值的平方
def squared(x, y, z):
    result = average_3_nums(x, y, z)
    s = result**2 #等价于s = pow(result, 2) 
    print("均值%d的平方%d" %(result, s))

num1 = int(input('please input num1:'))
num2 = int(input('please input num2:'))
num3 = int(input('please input num3:'))

#sum_3_nums(num1, num2, num3)
#max_min_nums(num1, num2, num3)
#average_3_nums(num1, num2, num3)  #实参
squared(num1, num2, num3)
#实参：实际传递的值
#形参：形式上接收的  
