#-*- coding: utf-8 -*-
import random
i = random.randint(0, 6)
while i <= 6:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
        break#仅对当前while有效，对外面while无效
        continue
    print("")
    i += 1
