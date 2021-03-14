array=[1,-2,3,4,5]
i=0
sum=0
while i<len(array):
    if array[i]>=0:
        sum=sum+array[i]
    i=i+1
print(sum)
