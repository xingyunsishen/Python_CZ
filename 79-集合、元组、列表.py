#-*- coding:utf-8 -*- 
#列表去重
a = [11, 22, 33, 33, 44, 44, 11, 22, 55]
#传统做法
b = []
for i in a:
    if i not in b:
        b.append(i)
print('a=%s'%a)
print('b=%s'%b)
#使用集合去重
c = set(a)
print('c=%s'%c)
b = list(c)
print('b=%s'%b)

