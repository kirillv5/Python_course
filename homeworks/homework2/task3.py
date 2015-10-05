def euclid(n, m):
    if n % m == 0:
        return(m)
    else:
        return(euclid(m, n % m))
n, m = (int(i) for i in input().split())        
print(euclid(n, m))