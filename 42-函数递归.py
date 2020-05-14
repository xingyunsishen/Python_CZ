#-*- coding: utf-8 -*-

# 获取用户从键盘输入，并计算该数的阶乘
num = int(input('please input a number:'))

# result = num * num -1 * num-2
'''
i = 1
result = 1
while i <= num:
    result *= i
    i += 1
print(result)
'''
def factorial(num): #注意这里的num
    if num > 1:
        return num * factorial(num-1)
    else:
        return num

result = factorial(num)
print(result)

factorial(num)

