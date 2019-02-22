# def fn(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#
#     return fn(n-1)+fn(n-2)
#
#
# print(fn(1))
a=1
b=1

n=5
if n<=2:
    print(1)
else:
    print(1,1,end=' ')#end是接在后面 默认的打印在第一行
    for i in range(1,n-1):
        a,b=b,a+b
        print(b)
