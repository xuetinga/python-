def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[i]>nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]#一次冒泡操作

nums = [3, 4, 9, 6, 1]
bubble_sort(nums)
print(nums)
#l累加
def fun1(n):#n为形式参数
    sum = 0
    for i in range(1,n+1):
        sum=sum + i
    print(sum)
fun1(3)#函数调用语句，实际参数，实参。
fun1(6)
def fun2(n):
    return (1+n)*n//2
    print(fun2)
fun2(3)
#折半查找
