word=str(input())
number=str(input())
n=(int(number))
c=int(number[len(number)-1])
d=int(number[len(number)-2])
if word=='����':
    if n==1 or c==1 and d!=1:
        print(n, "����")
    elif 2<=n<=4 or 2<=c<=4 and d!=1:
        print(n, "�����")
    else:
        print(n, "������")
if word=='�����':
    if n==1 or c==1 and d!=1:
        print(n, "�����")
    elif 2<=n<=4 or 2<=c<=4 and d!=1:
        print(n, "�����")
    else:
        print(n, "�����")









