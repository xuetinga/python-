# def F(a):
#     if len(a)==1:
#         return(a[0])
#     return(F(a[1:])-a[0])
#
# a=[1,4,9,16]
# print(F(a))


for i in range(10):
    print (fab(i))
m = 1
n = 1
for i in range(10):
        j = n
	    n = m
		m = j + 1
  print (fab(i))

