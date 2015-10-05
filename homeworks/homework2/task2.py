n = int(input())
list_k = []
while len(list_k) != n:
    i = int(input())
    list_k.append(i)
    
    
def prime(k):
    if k in range(4):
        return(True)
    else:
        i = 2
        n = []
        while i != k - 1:
            n.append(k % i)
            i += 1        
        if 0 in n:
            return(False)
        else:
            return(True)
for k in list_k:
    print(prime(k))
