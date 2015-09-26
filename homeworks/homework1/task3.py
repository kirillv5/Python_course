l = [int(i) for i in input().split()]
even = []
odd = []
for i in range(1, len(l), 2):
    odd.append(l[i])
for i in range(0, len(l), 2):
    even.append(l[i])
odd.sort()
odd.reverse()
even.sort()
sorted_list = ''
for i in range(0, len(even)):
    sorted_list += str(even[i]) + ' '
    sorted_list += str(odd[i]) + ' '
print(sorted_list)










