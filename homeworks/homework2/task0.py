word = str(input())
words = []
number = str(input())
n=(int(number))
c=int(number[len(number)-1])
d=int(number[len(number)-2])
if word == '����':
    words = ['����', '�����', '������']
elif word == '�����' :
    words = ['�����', '�����', '�����']
elif word == '��������' :
     words = ['��������', '��������', '��������']
elif word == '������' :
    words = ['������', '�������', '��������']
def plural(n, words):
    if n==1 or c==1 and d!=1:
        print(n, words[0])
    elif 2<=n<=4 or 2<=c<=4 and d!=1:
        print(n, words[1])
    else:
        print(n, words[2])
plural(n, words)