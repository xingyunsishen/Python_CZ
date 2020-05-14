#-*- coding: utf-8 -*-
age = int(input("请输入你的年龄："))
if age >= 0 and age <= 130:
    print("是个地球人")
    if age >= 18:
        print("可以去网吧Hi去了.....")
    elif age < 18:
        print("别闹，回家写作业去,,,,")
    else:
        print("请看如下：")
elif age > 130 and age <= 150:
    print("兄dei，你是目前已知的最大年龄的人")
elif age < 0:
    print("Sorry,请重新输入")
elif age > 150 and age < 1000:
    print("修仙路上，道阻且长.....")
elif age >= 1000 and age <= 10000:
    print("修成小仙，恭喜恭喜^_^")
elif age > 10000 and age <= 100000:
    print("上仙尊者～～～～")
elif age > 1000000:
    print("********宇宙先知***********")

