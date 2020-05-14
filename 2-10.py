#-*- coding: utf-8 -*-

t = 1
while (t):
    a = (float(input('\033[0;30;40m input a number between 1 and 100:\033[0m')))
    if a > 1 and a < 100 or a == 1 or a == 100:
       print('\033[0;31;41m Right \033[0m')
       t = 0
    else:
       print('\033[0;32;42m Sorry!try agin..\033[0m')
        
    
