s="good"
t="odg"
f=""
i=0
while i<len(t):
    a=t[i]
    j=0
    while j<len(s):
        b=s[j]
        if a==b:
            f+=a
        j=j+1
    i=i+1
print(f)