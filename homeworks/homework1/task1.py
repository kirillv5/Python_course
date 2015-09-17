word=str(input())
number=str(input())
n=(int(number))
c=int(number[len(number)-1])
d=int(number[len(number)-2])
if word=='утюг':
    if n==1 or c==1 and d!=1:
        print(n, "утюг")
    elif 2<=n<=4 or 2<=c<=4 and d!=1:
        print(n, "утюга")
    else:
        print(n, "утюгов")
if word=='ложка':
    if n==1 or c==1 and d!=1:
        print(n, "ложка")
    elif 2<=n<=4 or 2<=c<=4 and d!=1:
        print(n, "ложки")
    else:
        print(n, "ложек")









