
x=int(input('请输入进制x: '))#x属于2-9
n=666
a=[0,1,2,3,4,5,6,7,8]
b=[]
while True:
    s = n // x
    y = n % x
    b = b + [y]
    if s == 0:
        break
    n=s
b.reverse()
for i in b:
    print(a[i],end='')