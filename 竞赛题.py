# 第一行输入一个整数t( 0 < t <= 105 )，代表测试用例组数
# 接下来t行每行有n+1( 0 < n <= 105)个数字，每行第一个整数为n，代表后续有n个整数。
# 输出有t行，每行两个整数，分别为奇数的和与偶数的和，两个数字用空格隔开。
# 样例输入
# 2
# 5 1 2 4 5 6
# 4 3 2 5 1
# 样例输出
# 6 12
# 9 2
#str_nums 将字符串变成了列表
# count=int(input())
# for i in range(count):
#     str_nums=input().split('')
#     nums=[]**
#     for j in range(1,len(str_nums)):
#         nums.append(int(str_nums[j]))
#         #[3 2 5 1] 再写个循环 判断奇数和偶数
#竞赛题2
# def jue(n):
#     if n<0:
#         ruturn -1*n
#     return n#是我自己定义的
# def my_sort(nums):
#     for i in range (len(nums)-1):
#         for j in range(len(nums)-1-i):
#             if jue(nums[j]>nums[j+1]):#判断绝对值:
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
#
# count=int(input())
# for i in range(count):
#     str_nums=input().split(' ')
#     nums=[]
#     for j in range(1, len(str_nums)):
#         nums.append(int(str_nums[j]))
#     my_sort(nums)
#     for j in range(len(nums)):
#         print(nums[j],end=" ")
#     print('')#换行
#竞赛题3
#str_list=input().split(' ')
#return 后面的字符串拼接到前面
