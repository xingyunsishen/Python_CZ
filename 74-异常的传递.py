#-*- coding:utf-8 -*-
def test1():
    print('\033[0;31;40m ---test1-1---\033[0m')
    print(num)
    print('\033[1;31;41m ---test1-2---\033[0m')

def test2():
    print('\033[0;32;42m ---test2-1---\033[0m')
    test1()
    print('\033[1;31;41m ---test2-2---\033[0m')

def test3():
    try:
        print('\033[2;33;45m ---test3-1---\033[0m')
        test1()
        print('\033[3;34;42m ---test3-2---\033[0m')
    except Exception as result:
        print('捕获到的异常信息为:%s'%result)

    print('\033[4;35;45m ---test3-2---\033[0m')

test3()
print('\033[5;32;41m ---分割线---\033[0m')
test2()
