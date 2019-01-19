# 众所知周，毛学姐是一只学渣，只能代表软件学院的最低水平，有一天，他在研究《高等数论》的时候，发现了一个很神奇的现象，于是毛学姐发明了一个有趣的游戏：两人各说一个数字分别为a和b，如果a能包含b的所有质数因子，那么A就获胜。于是毛学姐找来两个好基友让他们进行人肉debug，但是当数字太大的时候，两个朋友的脑算速度就有点跟不上了。聪明的你已经识破了这个游戏的内容，请你写出这个程序，帮毛学姐debug。如果A获胜输出“Yes”，否则输出“No”。
# Input
# 输入一行，有两个用空格隔开的整数，分别为n和m（1  <= n, m <= 105）。
#
# Output
# 每行输出“Yes”或 “No”。
#
# Sample Input
# 120 75
# Sample Output
# Yes
def g(n, m):
    if n % m == 0:
        return m
    return g(m, n % m)

n, m = [int(x) for x in input().split()]
tmp = g(n, m)
m = m / tmp
if( tmp % m == 0):
    print("Yes")
else:
    print("No")