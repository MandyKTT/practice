import math
#ceil()向上取整
print(math.ceil(5.1))

#floor() 向下取整操作
print(math.floor(5.6))

#打印系统保留的关键字 不可以用来当做变量命名
import keyword
print(keyword.kwlist)

#round() 四舍五入操作
print(round(5.1))
print(round(5.5))

#sqrt() 开平方 返回浮点数
print(math.sqrt(4))

# pow() 与幂运算差不多，计算一个数的几次方 第一个是底数，第二个是指数
print(math.pow(4,3))
# 幂运算 函数返回浮点型，** 返回整型
print(4**3)

# fabs() 对一个数值获取绝对值 返回浮点数
print(math.fabs(-1))

#abs() 获取绝对值操作 不是数学模块当中的 是python内置函数 返回值由本身类型而定
print(abs(-1))
print(abs(-2.5))

#fsum()

import random
# random() 获取0-1之间的随机小数 包含0 不包含1
for i in range(10):
    print(random.random())

print(random.randint(1,9))