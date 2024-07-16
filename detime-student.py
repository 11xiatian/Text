# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 15:21:17 2021

@author: lilin
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 11:01:37 2021

@author: lilin
"""
import random
import time

#字符串长度
length = 8000000 #值太小会出现计时偏差错误




# 模拟第一种登录过程
def different_time_compare(Stringright, Stringguess):
    """2100300308敖显泽
    存在计时攻击的字符串比较方法
    """
    t1 = time.time()
    # 1、补充判断密码和猜测的密码的长度是否相同
    if len(Stringright) != len(Stringguess):
        t2 = time.time()
        runTime = t2 - t1
        return False,runTime

    # 2、利用基本的字符串比较方法，补充登录密码的比较程序
    for i in range(len(Stringright)):
        if Stringright[i] != Stringguess[i]:
            t2 = time.time()
            runTime = t2 - t1
            return False,runTime

    t2 = time.time()
    runTime = t2 - t1
    return True, runTime

# 模拟第二种登录过程
def constant_time_compare(Stringright, Stringguess):
    """2100300308敖显泽
    防止计时攻击的字符串比较方法
    """
    t1 = time.time()
    # 3、补充判断密码和猜测的密码的长度是否相同
    if len(Stringright) != len(Stringguess):
        return False

    # 4、补充登录密码的比较程序
    result = 0
    for i in range(len(Stringright)):
        result |= ord(Stringright[i]) ^ ord(Stringguess[i])

    t2 = time.time()
    runTime = t2 - t1
    return result == 0, runTime


#生成字符串
seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
str1 = []
for i in range(length):
  str1.append(random.choice(seed))
Stringright = ''.join(str1)


str2 = []
for i in range(length):
  str2.append(random.choice(seed))
Stringguess = ''.join(str2)


# 比较相同字符串
print("2100300308敖显泽")
print("比较相同字符串：")
print("不考虑时间的字符串比较方法：")
result, runtime = different_time_compare(Stringright, Stringright)
print("比较结果：", result)
print("用时：", runtime)

print("改进的字符串比较方法：")
result, runtime = constant_time_compare(Stringright, Stringright)
print("比较结果：", result)
print("用时：", runtime)

# 比较不同字符串
print("\n比较不同字符串：")
print("不考虑时间的字符串比较方法：")
result, runtime = different_time_compare(Stringright, Stringguess)
print("比较结果：", result)
print("用时：", runtime)

print("改进的字符串比较方法：")
result, runtime = constant_time_compare(Stringright, Stringguess)
print("比较结果：", result)
print("用时：", runtime)





