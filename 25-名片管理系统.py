#-*- coding: utf-8 -*-

#1.打印菜单选项
print("=="*6, "名片管理系统", "**"*6)
print("1.查询")
print("2.添加")
print("3.删除一个成员")
print("4.修改")
print("5.退出")
print("=="*40)

while True:
    #2.获取用户输入
    num = int(input("请输入操作序号:"))

    #3.根据用户输入执行对应的功能
    if num == 1:
        new_name=input("请输入要查找的名字：")

