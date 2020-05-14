#-*- coding: utf-8 -*-
'''
# find
myStr = 'hello world, I am Python! Nice to meet you, 123456789'
index01 = myStr.find('I')
print(myStr)
print('index01:%d'%index01)

#index
index02 = myStr.index('I')
print('index02:%d'%index02)

#rfind
index03 = myStr.rfind('I')
print('index03:%d'%index03)
index04 = myStr.rfind('n')
print('index04:%d'%index04)

#rindex
index05 = myStr.rindex('o')
print('index05:%d'%index05)

#count
c = myStr.count('xixi')
print(c) #找不到返回0
c = myStr.count('I')
print(c) #找到返回-1

#replace用法
#mystr.replace(str1, str2, mystr.count(str1))
#将mystr中的str1替换成str2,如果count指定，则替换不超过count次
result = myStr.replace('hello', 'Hi', myStr.count('hello'))
print(result)

#split用法
#以str为分隔符对mystr进行切片，如果maxsplit有指定值，则仅分隔maxspli
#个字符串
result = myStr.split(' ', 2)
print('分隔后的字符串%s'%result)

#capitalize 把字符串的首字母大写
str01 = 'wo shi yi ke wu ren zhi dao de xiao cao'
mystr = str01.capitalize()
print(mystr)

#title 将字符串的每个单词的首字母大写
res = str01.title()
print(res)

#startswith 检查字符串是否是以str开头，是返回true，否返回false
res = str01.startswith('H')
print(res)

# endswith 检查字符串是否是以str结尾，是返回true，否返回false
res = str01.endswith('cao')
print(res)

#lower 将字符串中的所有大写字母转换为小写字母
res = str01.lower()
print(res)
# upper 将字符串中的所有小写字母转换为大写字母
res = str01.upper()
print(res)

#ljust 返回一个原字符串左对齐，并使用空格填充至长度width的 新字符串
str01 = '12345678'
print(str01)
print('str01的长度为%d'%(len(str01)))
res = str01.ljust(30)
print(res)
print('res的长度为%d'%(len(res)))

#rjust 返回一个原字符串右对齐，并使用空格填充至长度width的新字符串
res = str01.rjust(30)
print('res:%s'%res)
print('res的长度为%d'%(len(res)))

# center 返回一个原字符串剧中，并使用空格填充至width的新字符串
str01 = '11 22 33 44'
res = str01.center(30)
print('res:%s' %res)
print('res的长度为%d' %(len(res)))

# lstrip 删除字符串左边的空白字符
s = '      haha 12 3 4 5 xixi zeze 00   '
print(s)
res = s.lstrip()
print('删除左边空白字符：%s'%res)
# rstrip 删除字符串右边的空白字符
res = s.rstrip()
print('删除右边空白字符%s'%res)

#partition 将字符串以指定的字符(str)分隔中三部分,str前，str，str后
s = '123445566789'
res = s.partition('44')
print(res)

#rpartition 同partition，不过是从右边开始 没有lpartition
s = '123 haha xixi  5678 aaa'
res = s.rpartition(' ')
print(res)
res = s. rpartition('haha')
print(res)

#splitlines 按照行分隔，返回一个包含各行作为元素的列表
s = '123\n445566\nhello\nworld'
res = s.splitlines()
print(res)

#isalpha 如果str中所有字符都是字母返回true，否则返回false
s1 = '123\n345\naaa'
s2 = 'asdqweasdasds  sasd sad'
s3 = 'aasdsqweq'
res1 = s1.isalpha()
res2 = s2.isalpha()
res3 = s3.isalpha()
print('s1:%s, res1:%s'%(s1, res1))
print('s2:%s, res2:%s'%(s2, res2))
print('s3:%s, res3:%s'%(s3, res3))

#isdigit 字符串中只有数字返回true，否则返回false
s = '12234223'
res = s.isdigit()
print(res)
#isalnum 所有字符都是字母或数字返回true，否则返回false
s = '12341asdcsada'
res = s.isalnum()
print(res)
'''
"""
#isspace只包含空格返回true，否则返回false
#join 每个字符后面插入str,构造出一个新的字符串
s1 = 'hello world'
char = '+'
res = char.join(s1)
print(res)
s2 = ['aa', 'bb', 'cc']
char = '_'
res = char.join(s2)
print(res)
"""
'''
注意：这里如果写成
s1 = 'hello world'
res = s1.join('_')
print(res)
不会报错，但是结果可能不容易理解
'''
'''
s1 = 'hello world'
res = s1.join(s1)
print(res)
'''

#将str字符串中的空格和制表符过滤掉
str = 'asxsadsa   sacxas \t \t \t sadadsa '
res = str.split()
print(res)
#将切割后的字符串合并成一个字符串
s = ''
res = s.join(res)
print(res)

