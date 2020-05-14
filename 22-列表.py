#-*- coding:utf-8 -*-
name = ['afei', 'buxiu', 'changhu', '4096', 1024, '^_^']
print(name)
print(name[0])
print(list(name))
#添加
name.append("duling")
name.append("enku")
print(list(name))
#指定位置插入
name.insert(2, "fol")
print(name)
#extend添加
str1 = ["DBA", "SRE", 65536]
name.extend(str1)# 等价于name = str1 + name
print(name)
#列表元素删除
name.pop(4)# 指定位置删除
print(name)
name.pop()# 默认从最后往前删
print(name)
name.remove("DBA") #匹配删除
print(name)
del name[0]
print(name)
# 列表元素修改
name[0] = "元素修改"
print(name)
# in not in
if "laowang" in name:
    print("哦豁，找到你了...")
elif "laowang" not in name:
    name.append("laowang")
    print(name)
    print("添加完成....")
else:
    print("没有其他情况了....")
# 获取列表索引
