# 毛学姐根据御坂妹妹网络为血小板制造了一个名为「Kesshou
# Ban
# Network」的中心司令塔，有一天中心司令塔的LastOrder出事了，为了维持 「Kesshou
# Ban
# Network」的正常工作，需要临时选出一个可爱的血小板作为中心司令塔。平面上有
# n
# 个可爱的血小板，问能否找到一个血小板作为中心司令塔，使得其他血小板都在以她为圆心的一个圆上，如果找不到这样的血小板，则输出
# "-1"(不含引号)。
#
#
#
# 《工作细胞
# TV版》
#
# Input
# 第一行一个数
# n，接下来
# n
# 行，第
# i
# 行两个整数
# xi, yi ，表示第
# i
# 个血小板在平面上的坐标。
#
# Output
# 输出共一个数，表示选出的血小板的编号，如果找不到则输出
# "-1"。
# Sample
# Input
# 3
# 1
# 1
# 0
# 1
# 1
# 2
# Sample
# Output
# 1
x = [0] * 5201314;
y = [0] * 5201314;
n = int(input())
for i in range(1,n+1):
    x[i], y[i] = [int(m) for m in input().split()]

for i in range(1,n+1):
    ok = 1
    p = -1
    for j in range(1,n+1):
        if i != j:
            s = (x[i] - x[j]) * (x[i] - x[j]) + (y[i] - y[j]) * (y[i] - y[j])
            if p == -1:
                p = s;
            else:
                ok = (ok and (p==s))
    if ok:
        print(i)
        break
if ok == 0:
    print(-1)