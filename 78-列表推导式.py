#-*- coding:utf-8 -*- 
#生成一个20以内的列表
a = [ i for i in range(1, 21)]
print(a)
print('\033[0;32;42m %s \033[0m'%a)

b = [3 for i in range(1,21)]
print('\033[0;37;41m %s \033[0m'%b)

c = [i for i in range(10) if i%2==0]
print('\033[0;37;40m %s \033[0m'%c)

#d = [i for i in range(5) for j in range(3)]
d = [(i,j) for i in range(5) for j in range(3)]
print('\033[0;37;42m %s \033[0m'%d)

e = [(i,j,k) for i in range(3) for j in range(2) for k in range(3)]
print('\033[0;37;43m %s \033[0m'%e)

