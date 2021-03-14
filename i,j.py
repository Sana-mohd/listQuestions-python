list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
i=0
while i<len(list1):
    a=list1[i]
    b=list2[-(i+1)]
    i=i+1
    print(a,b)