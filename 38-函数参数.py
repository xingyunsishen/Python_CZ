#-*- coding: utf-8 -*-
'''
num1 = int(input('please input a num:'))
num2 = int(input('please input a num:'))
num3 = int(input('please input a num:'))
num4 = int(input('please input a num:'))
'''
#函数的缺省参数
def test(a, b=3):
    c = a + b
    print('%d+%d=%d' %(a, b, c))

# 多个缺省参数
def test01(a, b=11, c=22):
    result = a + b + c
    print("%d+%d+%d=%d" %(a, b, c, result))

def test02(a, b=0, c=0, d=0):
    print('a=%d, b=%d, c=%d, d=%d' %(a, b, c, d))

#注意以下test03定义函数的缺省参数是有问题的
'''
SyntaxError: non-default argument follows default argument
'''
#def test03(a=0, b, c=0, d):
#    print('a=%d, b=%d, c=%d, d=%d' %(a, b, c, d))

# 不定长参数-01
def print_nums(a, b, *args):
    print('==start=='*5)
    print('a=%d'%a)
    print('b=%d'%b)
    print(args)
    print('==end=='*5)

# 拓展:实现无论输入多少个实参，都将结果相加
def sum_nums(x, y, *args):
    result = x + y + sum(args)
   # #或者是
   # result = x + y
   # for num in args:
   #     result += num
    print(result)
# 不定长参数-02
def variable_arguments(x, y, z, *args, **kwargs): 
    print(x)
    print(y)
    print(z)
    print(args)
    print(kwargs)



#test(num1)  #没有给定的实参时，使用缺省形参b的值
#test(num1, num2) #指定实参时，使用给定的实参num2代替缺省形参b的值

#test01(num1)
#test01(num1, num2)
#test01(num1, num2, num3)

#test02(num1)
#test02(num1, d=num2) #指定形参值, 此时d为命名参数
#test02(num1, num2, num3)
#test02(num1, num2, num3, num4)
#test02() #这里会报错，因为形参a没有缺省值

#test03(num1, num2, num3, num4)

#print_nums(10, 21, 32, 43, 54, 65)
#print_nums(1, 2, 3)
#print_nums(1, 2)
#print_nums(1) #这里会报错，因为形参a,b 没有缺省参数值

#sum_nums(1, 2, 3, 4, 5, 6)
#sum_nums(1, 2, 3)

variable_arguments(1, 2, 3, 4, 5, 6, 7, id=1001, age=20)
variable_arguments(11, 22, 33, 44, 55, id=10010, name='laowang')
