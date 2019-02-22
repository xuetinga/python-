#选择排序  从第一个位置开始比较  找出一个最小的 和第一个位置互换
lt = [3, 5, 2, 1, 8, 4]
#求出lt的长度
n = len(lt)
#外层循环确定比较的轮数，x是下标，lt[x]在外层循环中代表lt中所有元素
for x in range(n-1):#x等于012345#内层循环开始比较
    print('x=',x)
    for y in range(x+1,n):
        print('y=',y)
        if lt[x] > lt[y]:
            # 让lt[x]和lt列表中每一个元素比较，找出小的
            lt[x], lt[y] = lt[y], lt[x]
    print(lt)
# x= 0y= 1y= 2y= 3y= 4y= 5
#153284
# x= 1y= 2y= 3y= 4y= 5
#125384
# x= 2y= 3y= 4y= 5
#123584
# x= 3y= 4y= 5
#123485
# x= 4y= 5\
#123458
