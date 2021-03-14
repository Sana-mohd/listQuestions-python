list=[1,2,3,4,5,6,7,8]
squares=[]
i=0
while i<len(list):
    list[i]=list[i]**2
    squares.append(list[i])
    i=i+1
print(squares)

