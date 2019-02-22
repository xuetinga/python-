#水仙花数 一个三位的正整数 个十百三位三次方之和等于这个数   abc=a*3+b*3+c*3
def shui():
    for i in range(100,1000):
        a=i%10
        b=i//10%10
        c=i//100
        if a**3 + b**3 + c**3 == i:
            print(i)
shui()