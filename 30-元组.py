#-*- coding: utf-8 -*-

a = ('aa', 'bb', 'cc')
b = (1, 2, 3, 4)
c = [11, 22, 33, 44]
d = [('dd'), ('ee')]
e = [('gg'), ('ff')]
#a.append(b) #元组是只读的，不允许修改
#print(a)
#AttributeError: 'tuple' object has no attribute 'append'

c.append(d)
print(c)

#d.append(e)
#print(d)
#TypeError: 'list' object is not callable
d.extend(e)
print(d)

#元组的特点
v, w , x= a
print(v, w, x)

#for循环遍历元组
f = ([(11, 22), ('aa', 'bb')])
for temp in f:
    print(temp)

g = (11, 'aa', 'cc', 33, 22)
for temp in g:
    print(temp)

