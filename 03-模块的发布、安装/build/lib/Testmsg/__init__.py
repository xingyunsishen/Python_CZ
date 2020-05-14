#-*- coding:utf-8 -*-

__all__ = ['sendmsg', 'recvmsg']
print('\033[0;33;43m ----__init__----\033[0m')

from . import sendmsg
print('\033[0;34;44m ---from . import sendmsg--- \033[0m')
'''如果在一个文件夹中存在__init__.py文件，则称此文件夹为包；
在导入此包时，__init__.py会被首先执行，如果该文件为空，导入
包时不会报错，但是在使用包内容时，会抛出异常；此外，在__init__.py
文件中使用__all__ = ['', '']来声明包内相应模块的导入
''' 

