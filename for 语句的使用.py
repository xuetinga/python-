names=["ni",'li','liu']
for name in names:
    print(name)
sum=0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum=sum+x
print(sum)
sum=0
for x in range(101):
    sum=sum+x
    print(sum)
sum=0
n=99
while n>0:
    sum=sum+n
    n=n-2
    print(sum)
d={'ni':98,'in':76,'inn':87}
d['ni']
print(d['ni'])
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

#九九乘法表
for i in range(1,10):

    for j in range(1,i+1):
        print('%s*%s=%s'%(i,j,i*j),end='  ')
    print()