#i=1
#while i<10:
   # j=1
  #  while j<9:
     #   print('%d*%d=%d'%(i,j,i*j),end=' ')#换行end是什么？
    #    j=j+1
# print("")
 #   i=i+1#循环嵌套
#for i in range(10):#把0-9的值赋予给i 确定循环次数 用for就看容易
    #print(i)
#range 产生一个范围
#range（1，5） 1 2 3 4
#range（1，5，2）1 3
#for o in range(0,101,2):
 #   print(o)
 #无论是字符串  只要是序列  都可以加入到for in 中，因为是一个一个元素组成的
num=int(input())
if num%10 == 3:
    print('有')
    num = num//10
elif num//10%10 == 3:
    print('有')
else:
    print('没有')
n=10%3#%是整除的意思，能整除就是0  不能整除就是1
print(n)



