#-*- coding:utf-8 -*-
'''
#制作文件备份

#1.获取用户输入的文件名
file_name = input("please input file name:")

#2. 打开要复制的文件
f_read = open(file_name, 'r')

#3.将原文件备份为file_name.bak
#方式1
#new_file = file_name + '.bak'
#方式2
#new_file = file_name.replace('.', '_bak.', 1)# 这种方法有个缺点：当文件名中包含
                                              #多个'.'时得到的结果会不是很友好
#方式3
position = file_name.rfind('.')
new_file = file_name[0:position] + '_bak' + file_name[position:]

#3.创建一个新文件
f_write = open(new_file, 'w')

#4.从file_name文件中，读取数据，写入到new文件中
content = f_read.read()
f_write.write(content)

#while True:
#    content = f.read.read(1024)
#    if len(content) == 0L
#        break
#    f_write.write(content)
#5.关闭文件
f_read.close()
f_write.close()
'''
'''
##############
#read readline readlines
f = open('test.py', 'r')
content = f.read(4)
content01 = f.readline()
content02 = f.readline()
content03 = f.readlines()
position = f.tell() #读取当前位置
print(content)
print(content01)
print(content02)
print(content03)
print(position)
f.close()
'''
'''
#定位到某个位置
#如果在读写文件的过程中，需要从另外一个位置进行操作时，可以使用seek()
f = open('test.txt', 'r')
str = f.read(30)
print('读取的数据是：', str)

#查找当前位置
position = f.tell()
print('当前位置：', position)

#重新设置位置
f.seek(5, 0)  #5:偏移量 0:开头  1:当前位置  2:文件末尾
position = f.tell()
print('当前位置:', position)
f.close()
'''
'''
f = open('test.txt', 'rb')

#查找当前位置
s = f.read(10)
print(s)
position = f.tell()
print('current position:', position)

#重新设置位置为距离文件末尾3字节处
f.seek(-3,2) # 注意在实际执行过程中，python3.x会报错，需要将文件打开方式改为rb模
             #式;在python2.x中虽然不报错，但是结果输出不对
#f.seek(2000,0) #在r模式下打开时，python3.x只允许从文件开头偏移，从文件末尾就
                #会报错
str = f.read()
print('读取的内容：', str)
position = f.tell()
print('current position:', position)
f.close()
'''

#rename文件重命名
import os
#os.rename('test.py', 'Test.py.new')

#remove删除文件
#os.remove('Test.py.new')

#mkdir 创建文件夹
#os.mkdir('test')

#chdir 改变默认目录
#os.chdir('../')

#listdir 获取目录列表
#os.listdir('./')
#rmdir 删除目录
#os.rmdir('test')

#批量修改文件名
import os
'''
funFlag = 1 #1表示添加标志，2表示删除标志

folderName = './test/'
#获取指定路径的所有文件名字
dirList = os.listdir(folderName)

#遍历输出所有文件名字
for name in dirList:
    print(name)

    if funFlag == 1:
        newName = '[PLXG]-' + name
    elif funFlag == 2:
        num = len('[PLXG]-')
        new_name = name[num:]
    print(newName)

    os.rename(folderName+name, folderName+newName)
这段虽然可以实现批量修改，但是结果不满意
'''
# 1.获取用户输入的文件路径
folder_name = input('please input folder-name:')

# 2.获取文件路径下所有的文件名
file_names = os.listdir(folder_name)

#3 4这两步得到的结果与上面一样，修改后的文件中文件名两边会带单引号
#我系统是ubuntu-18.04.1,python版本是3.6.9；
#但是相同代码在云主机中运行就可以得到正常结果
#云主机是CentOS Linux release 7.7.1908,python 版本是3.8.0
#这个问题估计应该是系统版本问题，个人觉得是
# 3.进入文件路径下
os.chdir(folder_name)

# 4.重命名路径下的文件
for name in file_names:
    print(name)
    os.rename(name, "[new]-"+name)
'''
# 第二种方式 
for name in file_names:
    old_name = './' + folder_name + '/' + name
    new_name = './' + folder_name + '/' + '[New]-' + name
    os.rename(old_name, new_name)
'''


