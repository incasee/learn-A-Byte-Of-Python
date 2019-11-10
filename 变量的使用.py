"""
使用input()函数获取键盘输入（字符串）
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串

Version: 0.1
Author:pcb
"""
"""
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d'% (a, b, a + b))

"""
"""
a = 10
b = 3
a += b
a *= a + 2
print(a)
"""


"""
比较 逻辑和身份运算符的使用

"""


"""
flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not (1 != 2)
print('flag0 =', flag0)#flag0 = True
print(flag0)#True
print('flag1 =', flag1 )
print('flag2 =', flag2)
print('flag3 =', flag3)
print('flag4 =', flag4)
print('flag5 =',flag5)
print(flag1 is True)
print(flag2 is not False)
"""

"""
练习将华氏温度转换为摄氏温度

"""

"""
f = float(input('请输入华氏温度： '))
c = (f - 32) / 1.8
print('%.1f华氏摄氏度 = %.1f摄氏度' % (f, c))

"""
"""
练习网速转换订购带宽mbps转换成mb/s

"""
mbs = float(input('请输入实际测试的Mb/s: '))
mbps = mbs / 8
print('%.01f实际测试 = %.1f真实带宽' % (mbs, mbps))

