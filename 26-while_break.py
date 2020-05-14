#-*- coding:utf-8 -*-
i = 1
while i <= 10:
    i += 1
    if i % 2 == 0:
        print("i = %d 是偶数" %i)
    else:
        print("终止整个循环的标志")
        print("i = %d" %i)
        break #break只会终止当前循环，对这段而言只会终止内循环，对外面的while循环不会起作用
    #    continue
print("这段话与break无关")
 #break只会终止当前循环，对这段而言只会终止内循环，对外面的while循环不会起作用
