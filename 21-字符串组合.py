#-*- coding: utf-8 -*-

a = "AAAAA"
b = "B0000B"
c = "C----1"
print(a+b+c)
string="a0b1c3d4e5"
print(string)
print(len(string))
print(string[0])
print(string[1])
print(string[4], string[7])
print(string[-9])
#切片
print(string[1:4]) #左闭右开
print(string[-4:-1])
print(string[3:-1])
#步长
print(string[0:-1:2])
print(string[1:9:2])
print(string[-1:0:-1])
print(string[-1:1:-1])
print(string[-1:2:-1])
print(string[-1:-1])
#倒排
print(string[::-1])
