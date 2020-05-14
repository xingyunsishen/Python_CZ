#-*- coding: utf-8 -*-

def test(a, b, c=33, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
    print('--end--'*5)

A = (5, 6, 7)
B = {"name":"xiaomi", "age":18}

def test01(a, b, c=0, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)
    print('--end--'*5)

test(1, 2, 3, 4, *A, **B)
test01(1, 2, 3, 4, 5, 6, id=10010, name='xiaomi')
#表示对输出结果感到疑惑，拆不拆包感觉输出都一样
