word=str(input())
number=str(input())
n=(int(number))
c=int(number[len(number)-1])
d=int(number[len(number)-2])
if word=='óòşã':
    if n==1 or c==1 and d!=1:
        print(n, "óòşã")
    elif 2<=n<=4 or 2<=c<=4 and d!=1:
        print(n, "óòşãà")
    else:
        print(n, "óòşãîâ")
if word=='ëîæêà':
    if n==1 or c==1 and d!=1:
        print(n, "ëîæêà")
    elif 2<=n<=4 or 2<=c<=4 and d!=1:
        print(n, "ëîæêè")
    else:
        print(n, "ëîæåê")









