# 长度为n的序列 需要进行n-1此冒泡 即可确定顺序。冒泡：序列相邻元素依次两两比较，如果不符合，位置进行交换。外层循环与内层循环
nums = [11,10,6,9,4]
for i in range(len(nums)-1):#i从0开始依次比较，所以0跑到了在后边。第一个值最小，不用动，所以冒泡4次就行，
    if nums[i]>nums[i+1]:
        nums[i],nums[i+1] = nums[i+1],nums[i]#一次冒泡操作
print(nums)
i  j
0   0123
1   012
2   01
3   0
刚开始就是34都是最后几位了


for i in range(len(nums)-1-1):
    if nums[i]>nums[i+1]:
        nums[i],nums[i+1]=nums[i+1],nums[i]#一次冒泡操作
print(nums)
for i in range(len(nums)-1-2):
    if nums[i]>nums[i+1]:
        nums[i],nums[i+1]=nums[i+1],nums[i]#一次冒泡操作
print(nums)
for i in range(len(nums)-1-3):
    if nums[i]>nums[i+1]:
        nums[i],nums[i+1]=nums[i+1],nums[i]#一次冒泡操作
print(nums)

nums1=[10,4,9,6,10]
for i in range(len(nums1)-1):
    for j in range(len(nums1)-1-i):
        if nums1[i]>nums1[i+1]:
            nums1[i],nums1[i+1]=nums1[i+1],nums1[i]#一次冒泡操作
print(nums1)

nums = [10, 10, 6, 9, 4]
for i in range(len(nums)-1):#i等于01234j=43210
    for j in range(len(nums) - 1 - i):#这样就可以进行多次。
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)