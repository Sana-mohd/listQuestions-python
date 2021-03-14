def perfect_roots(n):
    i=1
    while i<n:
        if i*i==n:
            return True
        i=i+1
print(perfect_roots(256))