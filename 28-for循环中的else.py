#-*- coding: utf-8 -*- 

list_01 = [11, 22, 33, 44, 55, 66, 77]

for temp in list_01:
    print(temp)
   # break #加入break之后循环一次就会退出整个for循环，只会输出'11'这个元素
else:
    print("========")
#################
print("++" * 10)
card_infors = [{"ID":"10001", "name":"xiaoming", "age":28, "post":"Sales"}, 
        {"ID":"10002", "name":"xiaowang", "age":26, "post":"SRE"}, 
        {"ID":"10003", "name":"xiaoyang", "age":25, "post":"DBA"}, 
        {"ID":"10004", "name":"xiaoxu", "age":26, "post":"R&D Engineer"}]

find_name = input("请输入要查找的名字：")
#index_card = card_infors.index(find_name) #这个是自己的想法看，是想通过索引查找
                                           #，但是temp本身就已经遍历了整个列表，
                                           #所以不需要这样多此一举，
#print(index_card)
is_ok = False
for temp in card_infors:#temp即为列表中的每一个元素（字典）
    if temp['name'] == find_name:
        #print(card_infors[index_card])
        print("所查找的名字:", find_name, "在列表中")
        print(temp)
        is_ok=True
        break
if not is_ok:
    print('over')
#else:
#    print("所查找的名字不在列表中....")
