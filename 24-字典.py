#-*- coding: utf-8 -*-

dict1 = {"name":"xueji", "QQ":"1312145", "addr":"xuwucun", "job":"SRE"}
print(dict1)
print(dict1.keys())
print(dict1.values())
#添加键值对,只要是当前字典中未存在的键值对，就会自动添加到当
#前字典中
dict1["wechat"]="weixin312"
dict1["work_place", "work_city"]="changning", "shanghai"
print(dict1)

#修改键值对
#dict1["work_city"]="ShangHai"
#dict1["work_city":"ShangHai"]=["WorkCity":"ShangHai"]
#print(dict1)

#删除字典中的键值
#del dict1["QQ"]
#print(dict1)

##清空字典
#print(dict1.clear())

#比较字典,python3中cmp暂时有点问题
#dict2 = {"Id":"10001", "name":"lixu", "age":"29", "job":"enginer"}
#print("Return comper: %d" cmp (dict1, dict2))
#dict1 = {'Name': 'Zara', 'Age': 7};
#dict2 = {'Name': 'Mahnaz', 'Age': 27};
#dict3 = {'Name': 'Abid', 'Age': 27};
#dict4 = {'Name': 'Zara', 'Age': 7};
#print ("Return Value : %d" %  cmp (dict1, dict2))
#print ("Return Value : %d" %  cmp (dict2, dict3))
#print ("Return Value : %d" %  cmp (dict1, dict4))

#获取字典长度
print(len(dict1))

#
