l = list(input())
l.sort()
l.append(' ')
words = ''
c = 1
for i in range(0, len(l) - 1):
    if l[i] == l[i + 1]:
        c += 1
    else:
        words += str(l[i] + ' ' + str(c) + '\n')
        c = 1
print(words)








