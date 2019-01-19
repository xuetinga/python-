s=int(input('enter'))#将输入的字符串转换为数值
s=s+1
print(s)
r=float(input("请输入圆的半径："))#float将输入的转换为浮点型
s=3.14*r**2
print("圆的面积为：%.2f"%(3.14*r**2))#先弄个%。2f是保留几位小数，再来个%是即将输出的内容
#字符串的格式化
print('hello %s, i am %d!'%('tom',17))
#%s是格式化的字符串   %d是格式化的整数  %f是格式化的浮点数
#不确定的时候  %s一直可以用
#字符串的各种操作
str1="zhangsan.li.1.si"
str2="san"
print(str1.find(str2)) #结果为5#find就是在1中找有没有2中的元素  有就显示是第几位 没有就是-1

#strip的意思是剔除,需要重新定义 然后得是字符串
str2=str2.strip("s")
print(str2)#an

#将大写转小写 lower  将小写转大写   upper   总共的swapcase
str3=str1.swapcase()
print(str3)#ZHANGSAN.LI.1.SI

#replace  是替换的意思
str4=str1.replace('li','lok')#zhangsan.lok.1.si
print(str4)

#split 将字符串拆分的意思  后面阔者的是（分隔符） 注意是拆分为数列
str5=str1.split(".")
print(str5)#['zhangsan', 'li', '1', 'si']

#join是加入一个新的字符串
str6="*".join(str1)
print(str6)
#z*h*a*n*g*s*a*n*.*l*i*.*1*.*s*i

