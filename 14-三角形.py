#-*- coding: utf-8 -*-
# 打印矩形
'''num = 1
while num <= 6:
    print("*" * 6)
    num += 1
'''
print("+"*20)
num = 1
while num <= 6:
    i = 1
    while i <= 6:
        print("*", end="")
        i += 1
    print("")
    num += 1
# 打印直角三角形
num = 1 
while num <= 6:
    i = 1
    while  i <= num:
        print("*", end="")
        i += 1
    print("")
    num += 1

# 乘法表
print("*"* 6,"乘法表", "*"*6)
n = 1
while n <= 9:
     j = 1
     while j <= n:
         print("%d*%d=%d" %(n, j, n*j), end=" ")
         j += 1
     print("")
     n += 1


