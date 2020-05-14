#-*- coding:utf-8 -*-
try:
    open('a.txt')
    a = 1
    b = 0
    print(a/b)
    #print(Name)
    print('\033[1;31;40m ---1---\033[0m')
    print('\033[2;32;42m',"程序正常的执行流程", '\033[0m') 

except NameError:
    print('\033[1;31;40m', "打印捕获的程序的异常提示信息", '\033[0m')
except FileNotFoundError:
    print('\033[2;32;42m 文件不存在...\033[0m')
except Exception: #捕获所有异常
    print('\033[3;33;43m 无论何种异常，只要是except没有捕捉到的，exception一定会捕捉到\033[0m')
except Exception as error: #查看异常原本的信息
    print(error)
else:
    print('\033[5;35;45m 没有异常才会执行的功能\033[0m')
finally:
    print('\033[4;34;42m ---finally---\033[0m')
print('\033[2;30;43m ---2---\033[0m')

