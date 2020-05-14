#-*- coding:utf-8 -*-

class Dog:

    #私有方法
    def __send_msg(self):
        print('\033[1;32;40m----正在发送信息----\033[0m')

    #公有方法
    def send_msg(self, new_money):
        if new_money > 10000:
            self.__send_msg()
        else:
            print('\033[27;37;41m余额不足，请先充值....\033[0m')

dog = Dog()
#dog.send_msg(100)
num = int(input('please input your money:'))
dog.send_msg(num)
