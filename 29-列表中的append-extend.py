#-*- coding: utf-8 -*-

list_01 = [11, 22, 33, ['a', 'b', 'c']]
list_02 = [11, 22, 'Dark', ['devil', ['angle']]]
        
print("list_01原列表长度:", len(list_01))
print("list_02原列表长度:", len(list_02))
print("list_01.extend:", end="")# extend会将list_01和list_02中的元素进行相加
list_01.extend(list_02)
print(list_01)
print("list_01.extend的列表长度：", len(list_01))
print("list_01.append:", end="") #append会把后面的列表作为一个整体加入到list
                                 #_01中
list_01.append(list_02)
print(list_01)
print("list_01.append的长度:", len(list_01))

#相同元素与不同元素对比
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
c = [1, 'a', 2, 'b']
d = [1, ['a', 'b', [1, 2, 3, ['f']]]]

print("原列表如下：")
print("a=", a)
print("b=", b)
print("c=", c)
print("d=", d)
a.append(b)
#注意 a=a.append(b)
#print(a) #这里的结果为none
print("a.append(b):", a)
a.append(c)
print("a.append(c):", a)

