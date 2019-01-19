def if_test(score):
    if score>=90:
        print("excellent")
    elif score>=80:
        print('very good')
    else:
        print('fail')
if_test(100)
#if  有且仅能出现一次。最先判断
#elif  可以出现许多次 0-n，前面条件都不满足
#else  一次或者零次，最后判断
#注意冒号  还有冒号

#while语句的使用
# x=10
# while x>0:
#     if x % 3 == 0:#如果x满满足这个条件  才执行x-1 不满足就输出
#         x=x-1
#         continue#继续执行这个循环
#     print(2*x,end = ' .')
#     x=x-1
#break 就是不再执行这个循环  执行他后面的‘
x=10
while x>0:
    if x%6==0:
        break#直接就停了 不再执行
    print(2*x,end='.')
    x=x-1
#for语句  for  1 in  2   把2 中的元素依次赋给1

nums=2
if nums== 0:
    print("这个数是零")
elif nums%2==0:
                  #这个叫做嵌套   #加冒号条件结束,通过缩进控制代码
    print("这个数是个偶数")
    print("真的是偶数")

else:
    print("这是个奇数")
    print('真的是奇数')
print('我是一条鱼')#没有缩进，不属于if这个分支，与if同级，会一直执行
#另一个例子
n=1
while n<=100:
    if n>10:#n=11时，条件满足，执行break语句
        break#会结束循环
    print(n)
    n=n+1
    print('end')
    #如果想打印奇数，则用contiue语句

n=2
while n<100:
    n=n+1
    if n%2==0:#n是偶数，则往下执行
     continue
    else:#会直接进行下一轮循环，后续的print不会继续
     print(n)


