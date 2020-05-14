#def get_temperature():
#    temperature = float(input("Please input temperature:"))
#    print("Current temperature is:%4.2f" % temperature)
#    return temperature
#
#def get_Fahrenheit(temperature):
#    temperature = temperature + 3
#    print("Current Fahrenheit：%4.2f" % temperature)

#get_temperature()
#temp = get_temperature()
#get_Fahrenheit(temp)

#一个函数中存在多个return
def more_return():
    numList = [1, 2, 3]
    charList = ['a', 'b', 'c']
    mixList = ['aa', 'bb', 11, 22, 33]
   # return numList, charList, mixList #等价于第三种方式
   # #1.用列表来封装三个变量的值
   # List_01= [numList, charList, mixList]
   # return List_01
   ##2.直接返回列表形式
   # return [numList, charList, mixList]
    #3. 元组
    return(charList, numList, mixList)

more_return()
a = more_return()
print(a)

