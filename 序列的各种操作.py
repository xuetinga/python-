nums1=[11,22,33,44,55,66,11]
nums1.append(66)#append 将一个数据添加到列表的末尾
print(nums1)#[11, 22, 33, 44, 55, 66, 11, 66]

nums1.clear()#clear 将列表之中的所有元素都删除
print(nums1)#【】

nums2=[1,2,3,4,5,6]
nums3=nums2.copy()#要先定义一个 谁等于什么 copy是返回这个列表 就是一个样
nums4=nums2
nums4[0]=100
print(nums3)#[1, 2, 3, 4, 5, 6]

print(nums2.count(1))#count 统计1在列表中出现的次数  0次

nums1.extend(nums2)#注意 这个是将列表添加到列表的后面
nums1=nums1+nums2
nums=[1,2,2,2,2,2,2]
print(nums1)

nums.insert(1,15)#将15插入到1那个位置,注意这里是输出原列表 不需要定义新列表，
#insert是内置函数  不需要重新定义
print(nums)

c=nums.pop(1)
print(nums)
print(c)

nums.remove(2)#删除列表第一个值为2的元素
l1=[55,56,55,56,56,56,57,57]
print(l1.count(l1))#统计出现的次数

l1=[1,2,3]
l2=[4,5,6]
l1.append(12)#在末尾添加一个数据
print(l1)

l2.insert(0,0)#在某处添加一个数据
print(l2)
l3=[0,1,2,3]

l3.pop(1)#弹出一个数据
print(l3)
l4=[1,2,3,4]

l4.reverse()#反转所有的元素
print(l4)

print(l4)
l4=l4[::-1]#也是反转所有的元素
print(l4)

#内建函数  求长度 最大值最小值
s=[1,2,3,45,6,6]
print(len(s))
print(max(s))
print(min(s))

#元组
nums10=(1,2,3,44,55)
print(nums10)
