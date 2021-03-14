list=[1,2,8,9,65,4,78,10]
i=0
min=list[i]
while i<len(list):
    a=list[i]
    if a<min:
        min=a
    i=i+1
print(min)
    