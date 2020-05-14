#-*- coding: utf-8 -*-
#1.打印菜单选项
print("==========名片管理系统===========")
print("1. 查询")
print("2. 添加")
print("3. 删除")
print("4. 修改")
print("5. 退出系统")

names = [] #定义一个空列表用来存储添加的名字
while True:
    
    #用户选择
    num = int(input("请输入操作序号："))

    #依据用户输入进行相应的操作
    if num == 1:
        find_name = input("请输入你查询的名字：")
        if find_name in names:
            print("找到了...")
        else:    
            print("还未录入...")
    elif num == 2:
        new_name = input("请输入名字：")
        names.append(new_name)
        print(names)
    elif num == 3:
        rev_name = input("请输入名字：")
        if rev_name in names:
            names.remove(rev_name)
            print(names)
            print("删除成功！！！")
        else:
            print("未找到该名字，无需删除～～")
    elif num == 4:
        rename = input("请输入要修改的名字：")
        if rename in names:
            rename = input("请输入修改后的名字：")
            rename = names.append(rename)
    else:
        print("即将退出系统，欢迎下次使用。。。")
        break


