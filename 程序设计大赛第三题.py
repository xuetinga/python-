# 为了躲避真白的好友丽塔·爱因兹渥司的追求，赤坂的开发的人工智能小女仆给他的房间设置了密码锁，密码锁由两部分组成，第一部分是一个10进制整数，要求转换成15进制整数，另一部分是一个2进制小数，要求转换成10进制小数（保留2位小数）。为了帮丽塔追到龙之介，请你写出进制转换的两个程序。
#
#
#
# (樱花庄的宠物女孩 TV版）
#
# Input
#
# 输入一行，一个10进制整数n和一个2进制小数m，用空格分开
#
# 其中( 0 < n <= 105), 且2进制小数的整数位为0。
#
#
#
# Output
# 输出一行，第一个数是15进制数，第二个数是10进制小数(保留两位小数），用空格分开
#
# Sample
# Input
# 235
# 0.101010
# Sample
# Output
# 10
# A
# 0.66
#答案
def change1(num):
    map = "0123456789ABCDEF"
    res = ""
    if num == 0:
        return 0
    while num > 0:
        res += map[num % 15]
        num //= 15
    return res[::-1]
def change2(num):
    tmp = num[2:]
    res = 0
    p = 1
    for i in tmp:
        res += int(i) * pow(1/2,p)  #每个位的位权是(1/2)的cnt次方
        p += 1
    return res

str = input().split()
num1 = int(str[0])
num2 = str[1]  #保留小数字符
print(change1(num1),change2(num2))