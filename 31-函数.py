# -*- coding: utf-8 -*-

def print_sanjiaoxing():
    print("*")
    print("*" * 2)
    print("*" * 3)
    print("*" * 4)
    print("*" * 5)

def print_chengfabiao():
   i = 1
   while i <= 9:
       j = 1
       while j <= i:
           print("%d*%d=%d" %(i, j, i*j), end=" ")
           j += 1
       print("")
       i += 1

def print_dengyao():
    i = 1
    while i <= 6:
        n = 1
        while n <= i:
            print("*", end = " ")
            n += 1
        print('')
        i += 1

def print_juxing():
    i = 1
    while i <= 6:
        n = 1
        while n <= 6:
            print('*', end = ' ')
            n += 1
        print('')
        i += 1

print_dengyao()
print_sanjiaoxing()
print_chengfabiao()
print_juxing()
