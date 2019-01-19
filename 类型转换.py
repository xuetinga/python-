a=abs(100)#abs是绝对值的意思
print(a)
b=abs(-100)
print(b)
c=max(1,2,3,2)#跟上个一样也是需要新建立一个。
print(c)
#数据转换类型int将其他数据类型转换为整数
d=int('123')
print(d)
e=int(12.236)
print(e)
#float将其他数据类型转换为小数
#bool判断正确与否
f=hex(333)
print(f)
#定义一个函数要用def开头，依次写出函数名，括号，括号中的参数和冒号，然后在缩进中编写函数体，函数的返回值用return表示

def my_abs(x):
    if x>=0:
        return x
    else:
        return -x
print(my_abs(-9966 ))
import math
def move(x,y,step,angle=0):
    nx=x=step*math.cos(angle)



