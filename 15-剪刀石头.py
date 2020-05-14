#-*- coding: utf-8 -*-
import random
#1.提示获取用户输入
player = int(input("请输入0:剪刀 1:石头 2:布"))

#2.电脑随机数
computer = random.randint(0,2)
#3.判断用户的输入，并显示对应的结果
if (player == 0 and computer == 2) or (player == 1 and computer == 0) or (player == 2 and computer == 1):
    print("player win~~~~gagaga")
    print("computer=%d" %(computer) )
elif player == computer:
    print("draw")
    print("computer=%d" %(computer) )
else:
    print("You lose")
    print("computer=%d" %(computer) )

