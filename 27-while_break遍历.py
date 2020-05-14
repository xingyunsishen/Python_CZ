#-*- coding: utf-8 -*-

nums = [11, 22, 33, 44, 55, 66, 77]
length = len(nums)
print("nums的长度为：", end="")
print(length)
# whil循环遍历列表
print("========while循环=======")
i = 0
while i < 7:
    print(nums[i])
    i += 1

#改良过的while
print("========", end="")
print("改良过的while", end="")
print("========")
i = 0
while i < len(nums):
    print(nums[i])
    i += 1
# for循环
print("========for循环=========")
for n in nums:
    print(n)

