word = str(input())
words = []
number = str(input())
n = (int(number))
c = int(number[len(number) - 1])
d = int(number[len(number) - 2])
if word == 'утюг':
    words = ['утюг', 'утюга', 'утюгов']
elif word == 'ложка':
    words = ['ложка', 'ложки', 'ложек']
elif word == 'гармошка':
    words = ['гармошка', 'гармошки', 'гармошек']
elif word == 'чайник':
    words = ['чайник', 'чайника', 'чайников']
    
    
def plural(n, words):
    if n == 1 or c == 1 and d != 1:
        return number + " " + words[0]
    elif 2 <= n <= 4 or 2 <= c <= 4 and d != 1:
        return number + " " + words[1]
    else:
        return number + " " + words[2]
out = [i for i in plural(n, words).split()]
for i in out:
    print(i, end = " ")
