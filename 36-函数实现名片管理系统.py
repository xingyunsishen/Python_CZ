#-*- coding:utf-8 -*-

# 定义一个列表来存储名片信息
names = []

# 菜单函数
def menus():
    print('==' * 20, '名片管理系统v2.0.0', '==' * 20)
    print('1.查询')
    print('2.添加')
    print('3.修改')
    print('4.删除')
    print('5.退出')
    print('==' * 50) 

# 查询函数
def select():
    global names
    find_name = input("请输入你查询的名字：")
    is_ok = 0 #默认表示没有找到
    for temp in names:
        if find_name == temp['name']:
            print("找到了...")
            print(temp)
            is_ok = 1
            break
        else:
            print("还未录入...")

# 添加函数
def add_new_infor():
    name = input('please input a new_name:')
    qq = int(input('please input a qq number:'))
    wechat = input('please input a wechat number:')
    addr = input('please  input a address:')
    post = input('please input your job:')
    
    #定义一个新字典，用来存储一个新的名片
    new_infor = {}
    new_infor['name'] = name
    new_infor['qq'] = qq
    new_infor['wechar'] = wechat
    new_infor['addr'] = addr
    new_infor['post'] = post

    #将一个字典添加到列表中
    #card_infors.append(new_infor)
    global names  #用局部变量来修改全局
    names.append(new_infor)

# 删除函数 
def delete():
    global names
    rev_name = input("请输入要删除的名字：")
    is_ok = 0 #默认没有这个名字
    for temp in names:
        if rev_name == temp['name']:
            names.remove(rev_name)
            print(names)
            is_ok = 1 #找到并删除
            print("删除成功！！！")
        else:
            print("未找到该名字，无需删除～～")

# 修改函数
def modify():
    global names
    rename = input("请输入要修改的名字：")
    is_ok = 0 #默认表示没有找到该名字
    for temp in names:
        if  rename == temp['name']:
            rename = input("请输入修改后的名字：")
            is_ok = 1 #找到并修改
            rename = names.append(rename)
            break

# 1.打印菜单
menus()

# 定义主函数
def main():
    while True:
        
        #用户选择
        num = int(input("请输入操作序号："))
        
        #依据用户输入进行相应的操作
        if num == 1:
            select()
        elif num == 2:
            add_new_infor()
            #输出刚添加的名片信息
            for name in names:
                print(name, end='')
                print('添加成功!!!')
            #print(names)
        elif num == 3:
            modify()
        elif num == 4:
            delete()
        elif num == 5:
            print('欢迎下次使用....')
            break
        else:
            print('输入有误，请输入1-5内的数！')
            continue
    
# 调用主函数
main()
