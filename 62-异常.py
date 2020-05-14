#-*- coding:utf-8 -*-

try:
    num = input('\033[0;30;40mxxx:\033[0m')
    int(num)
    print('\033[0;31;41m ----1----\033[0m')

except (NameError, FileNotFoundError):
    print('\033[0;32;42m 如果捕获到异常，处理方式....\033[0m')
except Exception as ret:
    print('\033[0;33;43m 如果使用了Exception，那么意味着只要上面的except没有捕获到异常，这个except一定会捕获到\033[0m')
    print(ret)
else:
    print('\033[0;34;44m 没有异常才会执行\033[0m')
finally:
    print('\033[0;35;45m ---finally---\033[0m')

print('\033[0;35;46m ---2---\033[0m')

import time
while True:
    print('\033[0;37;47m heihie...\033[0m')
    time.sleep(1)
    break
