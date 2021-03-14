#desending order
list=[1,9,3,75,18,33]
i=0
while i<len(list):
    j=0
    while j<(len(list)-1):
        if list[j]<list[j+1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
        j=j+1
    i=i+1
print(list)
    