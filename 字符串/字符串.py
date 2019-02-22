r=float(input("请输入圆的半径："))#float将输入的转换为浮点型
s=3.14*r**2
print("圆的面积为：%.2f"%(3.14*r**2))#先弄个%。2f是保留几位小数，再来个%是即将输出的内容
#字符串的格式化
str1="zhang ni ji ko"
str2="nik1"
print(str1.find(str2))
str1="zhang ni ji ko"
str2="ni"
print(str1.find(str2))
str2="zhang ni ji ko"
str2=str2.strip("")
print(str2)
str1="zhang ni ji ko"
str4="ni ji ko lp"
str4=str4.upper()
print(str4)
str5="ni bu hu yu Ji JHSU"
str5=str5.swapcase()
print(str5)
str6="ni bu hu yu Ji JHSU"
str6=str6.replace("ni","niu")
print(str6)
str7="ni bu hu yu bu Ji JHSU"
str7=str7.replace("ni bu","ni hao")
print(str7)
str8="182.36.5,26"
str8=str8.split(",")
print(str8)
str9="zhang xiaosi"
xing=str9.split(" ")[0]
print("xing")