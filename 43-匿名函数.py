#-*- coding: utf-8 -*- 

#lambda 关键词
sum = lambda arg1, arg2: arg1+arg2

print('result :', sum(10, 20))

#lambada 匿名函数的应用
stu = [
        {'name':'xiaoming', 'age':10},
        {'name':'wangshu', 'age':20},
        {'name':'liyunlong', 'age':30}
        ]
#按name排序
stu.sort(key = lambda x:x['name'])
print(stu)

#按age排序
stu.sort(key = lambda x:x['age'])
print(stu)

def test(a, b, function):
    result = function(a, b)
    print(result)

test(11, 22, lambda x,y: x+y)

def test01(a, b, function):
    result = function(a, b)
    print(result)

func_new = input('please input a Anonymous function：')
func_new = eval(func_new) #加上这句转换即可在python3.X中执行
test01(11, 22, func_new) #这种写法只适用python2.X，因为在python3.X中
                         #input接收的是一个字符串
                        
