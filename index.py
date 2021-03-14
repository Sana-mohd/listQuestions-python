list1=[1,2,[1,2,3,4],3,4,[8,9]]
i=0
while i<len(list1):
    if type(list1[i])==list:
        j=0
        while j<len(list1[i]):
            print(list1[i][j])
            j=j+1
    i=i+1
