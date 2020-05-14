#-*- coding:utf-8 -*-
#import sys
#print(sys.argv)
#name = "xiaoyaozi"
#print("\033[0;31;42m ---welcome to china %s--- \033[0m"%name)
#
#以上程序按照如下运行结果如下
#[root]->python3 77-给程序传递参数.py
#['77-给程序传递参数.py']
# ---welcome to china xiaoyaozi---
#[root]->python3 77-给程序传递参数.py a b c d e f g
#['77-给程序传递参数.py', 'a', 'b', 'c', 'd', 'e', 'f', 'g']

import sys
print(sys.argv)
#name = sys.argv[0] #0会把程序本身执行命令打印出来
name = sys.argv[1]  #1会把程序执行后的参数打印出来
print('\033[0;32;41m ---welcome to china %s ---\033[0m'%name)
#运行结果如下
#[root]->python3 77-给程序传递参数.py
#['77-给程序传递参数.py']
# ---welcome to china 77-给程序传递参数.py ---
#[root]->vim 77-给程序传递参数.py
#[root]->python3 77-给程序传递参数.py laoxi
#['77-给程序传递参数.py', 'laoxi']
# ---welcome to china laoxi ---
#[root]->python3 77-给程序传递参数.py sishen
#['77-给程序传递参数.py', 'sishen']
# ---welcome to china sishen ---
#[root]->python3 77-给程序传递参数.py sishen laowang
#['77-给程序传递参数.py', 'sishen', 'laowang']
# ---welcome to china sishen ---
