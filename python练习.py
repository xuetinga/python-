s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(s[:2], s[6:])
print(s[::3])

flag1 = 0
flag2 = 1
flag3 = 'a'
flag4 = 'b'
print(flag2 and flag3 and flag4 )
print(flag2 and flag3)
print(flag1 or flag3)
print(flag2 or flag3)

a = [1991, 2014, 'physics', 'math']
a.insert(1,'100') #a.insert(1,'200')
a.pop( )#将最后一位弹出去
print(a)
a.pop(2)
print(a)#将某一位弹出去

def countSum(*args):
    sum = 0
    for i in args:
        sum += i
    return   sum#看清楚跟谁对齐
print(countSum(1,2,3,4,5,6,7,8,9))

a, b = 4, 5
print(a, b)
a, b = (6, 7)
print(a, b)
a, b = "AB"
print(a, b)
((a, b), c) = ('AB', 'CD')
print(a, b, c)

def f(list2):
    for i in range(0, len (list2)):
        min = i

        for j in range(i + 1, len(list2)):

            if list2[j] < list2[min]:
                print(list2[min])


            list2[i], list2[min] = list2[min], list2[i]
f([1,2,3,4,5,6])