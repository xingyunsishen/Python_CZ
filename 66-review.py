#-*- coding:utf-8 -*-
class Tool(object):
    #属性
    num = 0

    #方法
    def __init__(self, new_name):
        self.name = new_name
        Tool.num += 1

tool1 = Tool('螺丝刀')
tool2 = Tool('瑞士军刀')
tool3 = Tool('大水滑')
print(tool1, tool2, tool3)
num = Tool.num
print("num=%d"%num)
